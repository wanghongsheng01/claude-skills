#!/usr/bin/env python3
"""reflint.py — reference & citation linter for CCF-A database / NL2SQL papers.

Usage:
  reflint.py --tex main.tex [--bib refs.bib ...] [--pdf main.pdf] --type method|benchmark|industrial
             [--venue pvldb|sigmod|icde|acl] [--online] [--cache ~/.cache/reflint.json]
             [--out report.md] [--json report.json]

Checks (each finding has severity BLOCKER / MAJOR / MINOR):
  * printed-reference count vs. the published-paper norm for the paper type
  * citation density per section (intro / related / method / experiments) and per related-work paragraph
  * related-work paragraphs with zero citations; captions that carry citations
  * cited keys missing from .bib; .bib entries never cited
  * system / baseline / dataset / metric / tool names used in text or tables without a citation
  * arXiv / CoRR entries for which a peer-reviewed version exists (Crossref, Semantic Scholar, DBLP)
  * entries missing DOI, pages, venue, or year; inconsistent venue naming
  * existence check of every entry (DOI -> Crossref; title -> Crossref / arXiv / Semantic Scholar / DBLP;
    URL-only entries -> HTTP status). Entries that cannot be verified are listed for manual check.
Network lookups only run with --online. Results are cached.
"""
import argparse, json, os, re, sys, time, difflib, unicodedata, urllib.parse
from collections import Counter, defaultdict

# ---------------------------------------------------------------- norms
# Measured on 56 accepted 2024-26 PVLDB / SIGMOD (research + industrial) / ICDE / ACL-family papers
# (demo papers excluded). Values: (P25, median, P75) of printed references.
NORMS = {
    'method':     {'refs': (41, 51.5, 64), 'intro': (9, 12.5, 16.5), 'related': (11.5, 16.5, 25), 'exp': (7.75, 13, 27.5),
                   'cite_instances': (50, 60, 74), 'per_related_para': (2.2, 3.6, 5.6), 'recent3': (0.43, 0.57, 0.70),
                   'arxiv': (0.04, 0.13, 0.24)},
    'benchmark':  {'refs': (45.5, 57, 75.5), 'intro': (11.5, 16, 22.5), 'related': (0, 12, 26), 'exp': (3.5, 10, 19.5),
                   'cite_instances': (52, 71, 116), 'per_related_para': (3.0, 4.5, 6.0), 'recent3': (0.26, 0.42, 0.67),
                   'arxiv': (0.06, 0.14, 0.21)},
    'industrial': {'refs': (35.5, 47, 60.5), 'intro': (3, 11, 17), 'related': (7.5, 15, 22), 'exp': (0, 1, 4.5),
                   'cite_instances': (29.5, 52, 67.5), 'per_related_para': (2.6, 5.0, 7.5), 'recent3': (0.22, 0.32, 0.45),
                   'arxiv': (0.0, 0.0, 0.01)},
}
# red-line floor = P25 of the type (below the bottom quartile of accepted papers)
VENUE_ALIASES = {
    'pvldb': [r'Proc\.?\s*VLDB\s*Endow', r'PVLDB', r'Proceedings of the VLDB Endowment'],
    'sigmod': [r'SIGMOD', r'Proc\.?\s*ACM\s*Manag\.?\s*Data', r'PACMMOD', r'Management of Data'],
    'icde': [r'ICDE', r'International Conference on Data Engineering'],
    'acl': [r'\bACL\b', r'Association for Computational Linguistics'],
    'emnlp': [r'EMNLP', r'Empirical Methods in Natural Language'],
    'neurips': [r'NeurIPS', r'Neural Information Processing'],
    'iclr': [r'ICLR', r'Learning Representations'],
    'cidr': [r'CIDR', r'Innovative Data Systems'],
}
PEER = re.compile(r'(?i)SIGMOD|VLDB|ICDE|Manag\.?\s*Data|ACL|EMNLP|NAACL|COLING|NeurIPS|Neural Information|ICML|ICLR|'
                  r'Learning Representations|KDD|CIDR|OSDI|SOSP|NSDI|EuroSys|TODS|Trans\.|Transactions|Journal|AAAI|WWW|'
                  r'Web Conference|SIGIR|IJCAI|CIKM|WSDM|EDBT|PODS|ICDT|Proceedings|Conference|Symposium|Workshop|Proc\.')

# ---------------------------------------------------------------- LaTeX handling
def strip_comments(s):
    return re.sub(r'(?<!\\)%.*', '', s)

def load_tex(path, seen=None):
    seen = seen or set()
    path = os.path.abspath(path)
    if not os.path.exists(path) and os.path.exists(path + '.tex'):
        path += '.tex'
    if path in seen or not os.path.exists(path):
        return ''
    seen.add(path)
    base = os.path.dirname(path)
    s = strip_comments(open(path, encoding='utf-8', errors='ignore').read())
    def rep(m):
        p = m.group(2).strip()
        cand = os.path.join(base, p)
        root = ROOT_DIR or base
        if not os.path.exists(cand) and not os.path.exists(cand + '.tex'):
            cand = os.path.join(root, p)
        return '\n' + load_tex(cand, seen) + '\n'
    return re.sub(r'\\(input|include|subfile)\s*\{([^}]+)\}', rep, s)

ROOT_DIR = None
OWN = []
FULL_TEX = ''
NAMES_OWN = set()
CITE_RE = re.compile(r'\\(?:no)?cite[a-zA-Z]*\*?\s*(?:\[[^\]]*\]\s*){0,2}\{([^}]+)\}')

def body_only(s):
    m = re.search(r'\\begin\{document\}', s)
    if m: s = s[m.end():]
    m = re.search(r'\\end\{document\}', s)
    if m: s = s[:m.start()]
    return s

def split_sections(body):
    parts = re.split(r'\\section\*?\s*(?:\[[^\]]*\])?\s*\{', body)
    out = [('front', parts[0])]
    for p in parts[1:]:
        depth, i = 1, 0
        while i < len(p) and depth:
            depth += {'{': 1, '}': -1}.get(p[i], 0); i += 1
        out.append((p[:i - 1], p[i:]))
    return out

def sec_kind(title):
    t = re.sub(r'\\[a-zA-Z]+', '', title).lower()
    if 'introduction' in t: return 'intro'
    if 'related' in t or 'prior work' in t or 'literature' in t: return 'related'
    if re.search(r'experiment|evaluation|empirical|results|benchmarking', t): return 'exp'
    if re.search(r'conclusion|acknowledg|limitation|discussion|lessons|future|ethic', t): return 'other'
    if re.search(r'background|preliminar|problem|motivation', t): return 'prelim'
    if t == 'front': return 'front'
    return 'method'

def keys_in(s):
    ks = []
    for g in CITE_RE.findall(s):
        ks += [k.strip() for k in g.split(',') if k.strip()]
    return ks

def cite_cmds(s):
    return CITE_RE.findall(s)

# ---------------------------------------------------------------- bib parsing (no dependency required)
def parse_bib(paths):
    ents = {}
    for p in paths:
        s = open(p, encoding='utf-8', errors='ignore').read()
        for m in re.finditer(r'@(\w+)\s*\{\s*([^,\s]+)\s*,', s):
            typ, key = m.group(1).lower(), m.group(2)
            if typ in ('string', 'comment', 'preamble'): continue
            i = m.end(); depth = 1
            while i < len(s) and depth:
                depth += {'{': 1, '}': -1}.get(s[i], 0); i += 1
            raw = s[m.end():i - 1]
            ents[key] = {'type': typ, 'key': key, 'fields': parse_fields(raw), 'file': os.path.basename(p)}
    return ents

def parse_fields(raw):
    f = {}; i = 0; n = len(raw)
    while i < n:
        m = re.compile(r'\s*,?\s*([A-Za-z_\-]+)\s*=\s*').match(raw, i)
        if not m: break
        name = m.group(1).lower(); i = m.end()
        if i < n and raw[i] == '{':
            depth = 1; j = i + 1
            while j < n and depth:
                depth += {'{': 1, '}': -1}.get(raw[j], 0); j += 1
            val = raw[i + 1:j - 1]; i = j
        elif i < n and raw[i] == '"':
            j = raw.find('"', i + 1); val = raw[i + 1:j]; i = j + 1
        else:
            j = i
            while j < n and raw[j] not in ',\n': j += 1
            val = raw[i:j]; i = j
        f[name] = ' '.join(val.split())
    return f

def clean(t):
    t = re.sub(r'\\[a-zA-Z]+\s*', ' ', t or '')
    t = re.sub(r'[{}$\\]', '', t)
    t = unicodedata.normalize('NFKD', t)
    return ' '.join(t.split())

def norm_title(t):
    return re.sub(r'[^a-z0-9 ]', '', clean(t).lower())

def sim(a, b):
    return difflib.SequenceMatcher(None, norm_title(a), norm_title(b)).ratio()

def sim_cr(title, item):
    """Similarity of a bib title to a Crossref item, accounting for title/subtitle splits."""
    ts = [re.split(r'\*\*|\u2020', (item.get('title') or [''])[0])[0]]
    subs = item.get('subtitle') or []
    cands = [ts[0]] + [ts[0] + ': ' + x for x in subs] + [ts[0] + ' ' + x for x in subs]
    best = max(sim(title, c) for c in cands)
    a, b = norm_title(title), norm_title(ts[0])
    if not subs and len(b) >= 4 and a.startswith(b) and a[len(b):len(b) + 1] in ('', ' '):
        best = max(best, 0.9)   # Crossref holds only the main title before the colon
    ta = set(norm_title(re.sub(r'\([^)]*\)', '', title)).split()); tb = set(norm_title(re.sub(r'\([^)]*\)', '', ts[0])).split())
    if len(ta) >= 3 and len(tb) >= 3 and (ta <= tb or tb <= ta) and min(len(ta), len(tb)) / max(len(ta), len(tb)) >= 0.6:
        best = max(best, 0.9)
    return best

def is_arxiv(e):
    f = e['fields']
    blob = ' '.join([f.get('journal', ''), f.get('booktitle', ''), f.get('eprint', ''), f.get('archiveprefix', ''),
                     f.get('howpublished', ''), f.get('url', ''), f.get('note', ''), f.get('publisher', '')])
    if re.search(r'(?i)arxiv|corr\b', blob) and not re.search(r'(?i)proceedings|proc\.|pvldb|vldb|sigmod|icde', f.get('booktitle', '') + f.get('journal', '').replace('CoRR', '')):
        return True
    return False

def arxiv_id(e):
    f = e['fields']
    blob = ' '.join(f.get(k, '') for k in ('eprint', 'journal', 'url', 'note', 'howpublished', 'volume'))
    doi = f.get('doi', '')
    if doi.lower().startswith('10.48550/arxiv.'): blob += ' ' + doi
    m = re.search(r'(?i)(?:arxiv[:/\s.]*|abs/|pdf/|eprint\W*)?(\d{4}\.\d{4,5})', blob)
    if m and not re.search(r'(?i)arxiv|abs/|pdf/', blob) and not f.get('eprint'): return None
    return m.group(1) if m else None

def is_web(e):
    f = e['fields']
    return e['type'] in ('misc', 'online', 'electronic', 'software', 'manual', 'techreport') and not is_arxiv(e) \
        and not PEER.search(f.get('booktitle', '') + f.get('journal', ''))

# ---------------------------------------------------------------- name detection
NAME_PAT = re.compile(r'(?<![\\\w/-])([A-Z][A-Za-z0-9]*(?:-[A-Za-z0-9]+)+|[A-Z]{2,}[a-z]*[A-Z0-9][A-Za-z0-9]*|[A-Z][a-z]+[A-Z][A-Za-z0-9]+)(?![\w-])')
GENERIC = set(('''SQL NL LLM LLMs API APIs JSON CSV GPU GPUs CPU CPUs RAM SSD HDD ETL ELT DAG DAGs BI KPI KPIs ID IDs UDF UDFs
DDL DML OLAP OLTP HTAP JOIN JOINs SELECT WHERE GROUP BY HAVING ORDER WITH UNION DISTINCT COUNT SUM AVG MAX MIN AND OR NOT
NULL TRUE FALSE PK FK RQ RQs EA EAB TP FP FN TN AUC ROC IQR CI CIs QED TODO FIXME URL URLs PDF HTML DOI IEEE ACM VLDB PVLDB
SIGMOD ICDE AI ML NLP QA LaTeX BibTeX IO I/O PII GDPR SLA SLAs SLO SLOs OK USA UTC PT PST PDT AoE CMT WTL WLT W/T/L
Table Figure Section Appendix Algorithm Theorem Lemma Definition Example Proof Fig Tab Eq Sec SHA MD5 UUID HTTP HTTPS REST YAML XML CoRR arXiv FROM ALL OUTER INNER LEFT RIGHT FULL EXCEPT INTERSECT INSERT UPDATE DELETE MERGE CREATE VIEW CASE WHEN THEN ELSE END LIMIT OFFSET OVER PARTITION WINDOW ROW ROWS RANGE CTE CTEs SKU SKUs DBA DBAs YoY MoM QoQ''').split())
ROLEWORDS = re.compile(r'(?i)^(ours|ablation|w/o|without|full|baseline|oracle|random|naive|default|rule|manual|human)')

def names_used(body, bib):
    """Return {name: [(pos, cited_nearby)]} for candidate system/baseline/dataset names."""
    titles = {k: clean(e['fields'].get('title', '')) for k, e in bib.items()}
    # names that are the title prefix of a bib entry ("DIN-SQL: ...", "BIRD: ...") are strong candidates
    prefix = {}
    for k, t in titles.items():
        m = re.match(r'([A-Za-z][\w\-\.\+]{1,30})\s*:', t)
        if m: prefix[m.group(1).lower()] = k
    text = re.sub(r'\\(label|ref|cref|Cref|autoref|eqref|url|href|includegraphics|input|begin|end|usepackage|newcommand|renewcommand|def)\*?\s*(\[[^\]]*\])?\{[^}]*\}', ' ', body)
    out = defaultdict(list)
    own = set(OWN)
    for m in re.finditer(r'\(([A-Z][A-Za-z0-9\-]{1,20})\)', text):   # "... rate (CRR)" defines a local term
        own.add(m.group(1))
    for m in re.finditer(r'\\(?:newcommand|def)\s*\{?\\(\w+)\}?(?:\[\d\])?\s*\{(?:\\[a-z]+\{)?([A-Za-z][\w\-]+)', FULL_TEX):
        own.add(m.group(2))
    for m in re.finditer(r'\\title(?:\[[^\]]*\])?\{([^:}]+)', FULL_TEX):
        own.add(clean(m.group(1)).strip())
    NAMES_OWN.update(own)
    for m in NAME_PAT.finditer(text):
        n = m.group(1)
        if n in own or n in GENERIC or ROLEWORDS.match(n) or len(n) < 3 or re.match(r'^[A-Z]\d', n) or re.match(r'^(RQ|Q|T|C|H|R|P|S|SF|V|v)\d', n):
            continue
        window = text[m.end():m.end() + 200]
        sent_end = re.search(r'(?<!e\.g)(?<!i\.e)(?<!et al)[.;:]\s|\\\\|&|\n\s*\n', window)
        near = window[:sent_end.start() if sent_end else 200]
        cited = bool(re.search(r'\\cite', near))  # list 'A, B, and C ~\cite{a,b,c}' counts
        out[n].append((m.start(), cited))
    return out, prefix

KNOWN_EXTERNAL = ['DuckDB', 'PostgreSQL', 'Postgres', 'SQLite', 'MySQL', 'Apache Spark', 'Spark SQL', 'Spark', 'Flink', 'Kafka', 'Hive', 'Presto', 'Trino',
    'StarRocks', 'Apache Doris', 'ClickHouse', 'Snowflake', 'BigQuery', 'Redshift', 'Databricks', 'dbt', 'Airflow', 'DolphinScheduler', 'Calcite',
    'sqlglot', 'SQLGlot', 'SQLMesh', 'TPC-H', 'TPC-DS', 'TPC-C', 'JOB', 'Spider 2.0', 'Spider', 'BIRD', 'KaggleDBQA', 'GPT-4o', 'GPT-4', 'GPT-5', 'GPT-6', 'Claude',
    'Qwen', 'DeepSeek', 'Llama', 'LLaMA', 'Gemini', 'GLM', 'Mistral', 'Iceberg', 'Delta Lake', 'Hudi', 'Z3', 'cvc5', 'NumPy', 'pandas', 'scikit-learn',
    'PyTorch', 'vLLM', 'LangChain', 'OpenLineage', 'MetricFlow', 'LookML', 'Cube', 'Power BI', 'Tableau', 'Oracle', 'SQL Server', 'Materialize', 'Noria', 'DBToaster']

STAT_TERMS = {r'Wilson (score )?(interval|lower bound|bound|CI)': 'Wilson 1927, JASA 22(158), DOI 10.1080/01621459.1927.10502953',
    r'Clopper[-\u2013 ]Pearson': 'Clopper & Pearson 1934, Biometrika 26(4), DOI 10.1093/biomet/26.4.404',
    r'McNemar': 'McNemar 1947, Psychometrika 12(2), DOI 10.1007/BF02295996',
    r'bootstrap': 'Efron 1979, Ann. Statist. 7(1), DOI 10.1214/aos/1176344552 (or Efron & Tibshirani 1993, book)',
    r"Cohen'?s\W+(\\kappa|kappa)|Cohen's \$\\kappa": 'Cohen 1960, Educ. Psychol. Meas. 20(1), DOI 10.1177/001316446002000104',
    r"Krippendorff": 'Krippendorff, Content Analysis (book), or Hayes & Krippendorff 2007, DOI 10.1080/19312450709336664',
    r'Wilcoxon': 'Wilcoxon 1945, Biometrics Bulletin 1(6), DOI 10.2307/3001968',
    r'Holm(\W|-)(Bonferroni|correct\w*|procedure)': 'Holm 1979, Scand. J. Statist. 6(2), JSTOR 4615733',
    r'Benjamini|Hochberg': 'Benjamini & Hochberg 1995, JRSS-B 57(1), DOI 10.1111/j.2517-6161.1995.tb02031.x',
    r'Kendall.{0,6}(tau|\\tau)': 'Kendall 1938, Biometrika 30(1-2), DOI 10.1093/biomet/30.1-2.81',
    r'Spearman': 'Spearman 1904, Am. J. Psychol. 15(1), DOI 10.2307/1412159',
    r"Fisher'?s exact": 'Fisher 1922, JRSS 85(1), DOI 10.2307/2340521'}

def stat_uncited(body, bib=None, printed=()):
    out = []
    for pat, ref in STAT_TERMS.items():
        ms = list(re.finditer(pat, body))
        if not ms: continue
        surname = ref.split()[0].strip(',')
        if bib and any(surname.lower() in bib[k]['fields'].get('author', '').lower() for k in printed if k in bib):
            continue  # the method's original paper is already cited somewhere
        if not any(re.search(r'\\cite', body[max(0, m.start() - 80):m.end() + 120]) for m in ms):
            out.append((ms[0].group(0), len(ms), ref))
    return out

def known_uncited(body):
    out = []
    # keys / labels / file names are not mentions: \cite{sqlglot2026} must not count as a mention of 'sqlglot'
    body = re.sub(r'(\\(?:cite[a-z]*|ref|eqref|autoref|cref|Cref|label|input|include|includegraphics|url|href)\*?(?:\[[^\]]*\])*)\{[^}]*\}', r'\1{}', body)
    for n in KNOWN_EXTERNAL:
        ms = list(re.finditer(r'(?<![\\\w-])' + re.escape(n) + r'(?![A-Za-z])', body))
        if not ms: continue
        first = ms[0]
        pat = r'^(?:[\w\-~{}()]|\.(?=\d))*[^;.\n]{0,50}?\\cite|^(?:[^.;\n]|e\.g\.|i\.e\.|et al\.){0,150}?\\cite'  # same clause or 'A, B, and C~\cite{...}' list
        near = body[first.end():first.end() + 200]
        anycite = any(re.search(pat, body[m.end():m.end() + 200]) for m in ms)
        if not re.search(pat, near):
            out.append((n, len(ms), anycite))
    # drop shorter names subsumed by a longer one already flagged (Spider vs Spider 2.0)
    return out

def table_names(body):
    names = Counter()
    for tb in re.findall(r'\\begin\{tabular\*?\}.*?\\end\{tabular\*?\}', body, flags=re.S):
        for m in NAME_PAT.finditer(tb):
            names[m.group(1)] += 1
    return names

# ---------------------------------------------------------------- online lookups
UA = {'User-Agent': 'reflint/1.0 (mailto:reflint@example.org)'}
class Lookup:
    def __init__(self, cache_path, online):
        self.cache_path = cache_path; self.online = online
        try: self.cache = json.load(open(cache_path))
        except Exception: self.cache = {}
        self.last_s2 = 0
        import requests; self.rq = requests
    def save(self):
        os.makedirs(os.path.dirname(self.cache_path) or '.', exist_ok=True)
        json.dump(self.cache, open(self.cache_path, 'w'), indent=0)
    def get(self, url, params=None, key=None, s2=False):
        ck = key or (url + json.dumps(params or {}, sort_keys=True))
        if ck in self.cache: return self.cache[ck]
        if not self.online: return None
        for attempt in range(2 if s2 else 4):
            if s2:
                wait = 1.2 - (time.time() - self.last_s2)
                if wait > 0: time.sleep(wait)
                self.last_s2 = time.time()
            try:
                r = self.rq.get(url, params=params, headers=UA, timeout=25)
            except Exception:
                time.sleep(2 * (attempt + 1)); continue
            if r.status_code == 429:
                time.sleep(4 * (attempt + 1)); continue
            if r.status_code == 404:
                self.cache[ck] = {'_status': 404}; return self.cache[ck]
            ctype = r.headers.get('content-type', '')
            if r.status_code == 200 and 'json' in ctype:
                self.cache[ck] = r.json(); return self.cache[ck]
            if r.status_code == 200:
                self.cache[ck] = {'_text': r.text[:20000]}; return self.cache[ck]
            if r.status_code == 202:   # DBLP anti-bot interstitial
                return None
            time.sleep(1)
        return None
    def head(self, url):
        ck = 'HEAD ' + url
        if ck in self.cache: return self.cache[ck]
        if not self.online: return None
        try:
            r = self.rq.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=20, allow_redirects=True, stream=True)
            code = r.status_code; r.close()
        except Exception:
            code = None
        self.cache[ck] = code; return code
    # -- sources
    def crossref_doi(self, doi):
        d = self.get('https://api.crossref.org/works/' + urllib.parse.quote(doi), {'mailto': 'reflint@example.org'})
        if d and 'message' in d: return d['message']
        return None
    def crossref_title(self, title, author=None):
        p = {'query.bibliographic': clean(title), 'rows': 5, 'mailto': 'reflint@example.org',
             'select': 'DOI,title,subtitle,container-title,type,published,author,page,event'}
        if author: p['query.author'] = author
        d = self.get('https://api.crossref.org/works', p)
        return (d or {}).get('message', {}).get('items', []) if d else []
    def arxiv(self, aid):
        d = self.get('http://export.arxiv.org/api/query', {'id_list': aid})
        t = (d or {}).get('_text', '')
        m = re.findall(r'<title>(.*?)</title>', t, flags=re.S)
        return ' '.join(m[1].split()) if len(m) > 1 else None
    def s2(self, title=None, aid=None, doi=None):
        fields = 'title,venue,year,externalIds,publicationVenue,publicationTypes'
        if aid: d = self.get(f'https://api.semanticscholar.org/graph/v1/paper/arXiv:{aid}', {'fields': fields}, s2=True)
        elif doi: d = self.get(f'https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}', {'fields': fields}, s2=True)
        else:
            d = self.get('https://api.semanticscholar.org/graph/v1/paper/search/match', {'query': clean(title), 'fields': fields}, s2=True)
            if d and 'data' in d and d['data']: d = d['data'][0]
        return d if d and 'title' in d else None
    def dblp(self, title):
        d = self.get('https://dblp.org/search/publ/api', {'q': clean(title), 'format': 'json', 'h': 5})
        try: return [h['info'] for h in d['result']['hits'].get('hit', [])]
        except Exception: return []

FAMILIES = {'vldb': r'(?i)PVLDB|VLDB|Very Large Data Bases', 'sigmod': r'(?i)SIGMOD|Manag\.?\s*Data|Management of Data|PACMMOD',
            'icde': r'(?i)ICDE|Conference on Data Engineering', 'neurips': r'(?i)NeurIPS|Neural Information Processing',
            'iclr': r'(?i)ICLR|Learning Representations', 'icml': r'(?i)ICML|International Conference on Machine Learning',
            'acl': r'(?i)\bACL\b|Annual Meeting of the Association for Computational', 'emnlp': r'(?i)EMNLP|Empirical Methods',
            'naacl': r'(?i)NAACL|North American Chapter', 'cidr': r'(?i)CIDR|Innovative Data Systems', 'kdd': r'(?i)KDD|Knowledge Discovery',
            'edbt': r'(?i)EDBT|Extending Database Technology', 'tkde': r'(?i)TKDE|Knowledge and Data Engineering', 'tods': r'(?i)TODS|Transactions on Database Systems'}
def family(v):
    if not v: return None
    hits = [k for k, p in FAMILIES.items() if re.search(p, v)]
    if 'sigmod' in hits and 'kdd' in hits: hits.remove('kdd')
    return hits[0] if len(hits) == 1 else None
NO_DOI_VENUES = re.compile(r'(?i)NeurIPS|Neural Information Processing|ICLR|Learning Representations|ICML|Machine Learning Research|CIDR|Innovative Data Systems|OSDI|NSDI|USENIX|AAAI')

def verify(e, L):
    """Return dict(status=verified|unverified|mismatch, source, published_version, notes)."""
    f = e['fields']; title = clean(f.get('title', '')); res = {'status': 'unverified', 'source': None, 'pub': None, 'notes': []}
    first_author = None
    if f.get('author'):
        a = f['author'].split(' and ')[0]
        first_author = clean(a.split(',')[0] if ',' in a else a.split()[-1] if a.split() else a)
    doi = f.get('doi', '').replace('https://doi.org/', '').strip()
    if doi:
        m = L.crossref_doi(doi)
        if m and m.get('title'):
            s = sim_cr(title, m) if title else 1
            if s > 0.85: res.update(status='verified', source='crossref-doi', venue_found=' '.join(m.get('container-title') or []))
            else: res.update(status='mismatch', source='crossref-doi'); res['notes'].append(f"DOI resolves to a different title: \"{m['title'][0][:90]}\"")
        elif m is None and not L.online:
            return res
        elif not m: res['notes'].append('DOI did not resolve on Crossref')
    aid = arxiv_id(e) if is_arxiv(e) or f.get('eprint') else None
    if is_arxiv(e):
        if aid:
            at = L.arxiv(aid)
            if at and (not title or sim(title, at) > 0.8):
                if res['status'] == 'unverified': res.update(status='verified', source='arxiv')
            elif at:
                res['notes'].append(f'arXiv id {aid} has a different title: "{at[:90]}"'); res['status'] = 'mismatch'
        # published version? Crossref first (fast), then Semantic Scholar
        pub = None
        if title:
            for it in L.crossref_title(title, first_author):
                ct = ' '.join(it.get('container-title') or [])
                if it.get('title') and sim_cr(title, it) > 0.92 and it.get('type') in ('proceedings-article', 'journal-article') \
                        and not re.search(r'(?i)arxiv', ct) and not it['DOI'].startswith('10.48550'):
                    pub = {'venue': ct or (it.get('event') or {}).get('name', ''), 'year': (it.get('published') or {}).get('date-parts', [[None]])[0][0], 'doi': it['DOI']}
                    break
        if not pub:
            s = L.s2(aid=aid) if aid else (L.s2(title=title) if title else None)
            if s and (not title or sim(title, s.get('title', '')) > 0.9):
                ven = (s.get('venue') or '') + ' ' + ((s.get('publicationVenue') or {}).get('name') or '')
                ext = s.get('externalIds') or {}
                if ven.strip() and not re.search(r'(?i)arxiv|corr', ven):
                    pub = {'venue': ven.strip(), 'year': s.get('year'), 'doi': ext.get('DOI') if not str(ext.get('DOI', '')).startswith('10.48550') else None, 'dblp': ext.get('DBLP')}
                if res['status'] == 'unverified': res.update(status='verified', source='semanticscholar')
        if not pub and title:
            for h in L.dblp(title):
                if sim(title, h.get('title', '')) > 0.92 and h.get('venue') not in ('CoRR', None):
                    pub = {'venue': h.get('venue'), 'year': h.get('year'), 'doi': h.get('doi'), 'dblp': h.get('url')}; break
        res['pub'] = pub
        if res['status'] == 'unverified' and title:
            s2 = L.s2(title=title)
            if s2 and sim(title, s2['title']) > 0.9: res.update(status='verified', source='semanticscholar')
        return res
    if res['status'] != 'unverified': return res
    if title and e['type'] not in ('misc', 'online', 'software', 'manual', 'electronic'):
        for it in L.crossref_title(title, first_author):
            if it.get('title') and sim_cr(title, it) > 0.9:
                res.update(status='verified', source='crossref-title', venue_found=' '.join(it.get('container-title') or [])); res['found_doi'] = it.get('DOI')
                if it.get('page'): res['found_pages'] = it['page']
                break
        if res['status'] == 'unverified':
            s2 = L.s2(title=title)
            if s2 and sim(title, s2['title']) > 0.9:
                res.update(status='verified', source='semanticscholar', venue_found=(s2.get('venue') or '') + ' ' + ((s2.get('publicationVenue') or {}).get('name') or ''), year_found=s2.get('year')); res['found_doi'] = (s2.get('externalIds') or {}).get('DOI')
        if res['status'] == 'unverified':
            for h in L.dblp(title):
                if sim(title, h.get('title', '')) > 0.9: res.update(status='verified', source='dblp'); break
    url = f.get('url') or (re.search(r'\\(?:url|href)\{([^}]+)\}', f.get('howpublished', '') + f.get('note', '')) or [None, None])[1]
    if res['status'] == 'unverified' and url:
        code = L.head(url)
        if code and code < 400: res.update(status='verified', source=f'url-{code}')
        elif code: res['notes'].append(f'URL returns HTTP {code}')
    if res['status'] == 'unverified' and title and e['type'] in ('misc', 'online', 'software', 'manual', 'electronic'):
        s2 = L.s2(title=title)
        if s2 and sim(title, s2['title']) > 0.9: res.update(status='verified', source='semanticscholar')
    return res

# ---------------------------------------------------------------- PDF helper (optional)
def pdf_ref_count(pdf):
    try:
        import pymupdf
    except Exception:
        try: import fitz as pymupdf
        except Exception: return None
    doc = pymupdf.open(pdf); txt = []
    for pg in doc:
        W = pg.rect.width
        bl = sorted([b for b in pg.get_text('blocks') if b[6] == 0], key=lambda b: (0 if b[0] < W * 0.45 else 1, b[1]))
        txt += [b[4] for b in bl]
    t = '\n'.join(txt)
    i = max(t.rfind('\nREFERENCES'), t.rfind('\nReferences'))
    nums = [int(x) for x in re.findall(r'(?m)^\s*\[(\d{1,3})\]', t[i:])] if i > 0 else []
    return {'pdf_refs': max(nums) if nums else None, 'pages': len(doc)}

# ---------------------------------------------------------------- main
def main():
    global ROOT_DIR
    ap = argparse.ArgumentParser()
    ap.add_argument('--tex', required=True); ap.add_argument('--bib', nargs='*')
    ap.add_argument('--pdf'); ap.add_argument('--type', default='method', choices=list(NORMS))
    ap.add_argument('--venue', default='pvldb'); ap.add_argument('--online', action='store_true')
    ap.add_argument('--cache', default=os.path.expanduser('~/.cache/reflint_cache.json'))
    ap.add_argument('--out'); ap.add_argument('--json'); ap.add_argument('--pubyear', type=int, default=time.localtime().tm_year)
    ap.add_argument('--max-lookups', type=int, default=400)
    ap.add_argument('--own', help='comma-separated names of this paper\'s own artefacts/metrics to ignore')
    a = ap.parse_args()
    ROOT_DIR = os.path.dirname(os.path.abspath(a.tex))
    full = load_tex(a.tex); body = body_only(full)
    global FULL_TEX, OWN
    FULL_TEX = full; OWN = [x.strip() for x in (a.own or '').split(',') if x.strip()]
    bibs = a.bib or []
    if not bibs:
        for b in re.findall(r'\\(?:bibliography|addbibresource)\{([^}]+)\}', full):
            for x in b.split(','):
                x = x.strip(); x = x if x.endswith('.bib') else x + '.bib'
                p = os.path.join(ROOT_DIR, x)
                if os.path.exists(p): bibs.append(p)
    bib = parse_bib(bibs)
    findings = []
    def add(sev, where, msg, fix=''):
        findings.append({'sev': sev, 'where': where, 'msg': msg, 'fix': fix})
    N = NORMS[a.type]
    nocite_all = bool(re.search(r'\\nocite\{\*\}', full))
    cited_order = []
    for k in keys_in(body):
        if k not in cited_order and k != '*': cited_order.append(k)
    printed = list(bib) if nocite_all else [k for k in cited_order if k in bib]
    missing = [k for k in cited_order if k not in bib]
    uncited = [k for k in bib if k not in cited_order]
    nref = len(printed)
    lo, med, hi = N['refs']
    if nref < lo:
        add('BLOCKER', 'References', f'{nref} printed references; accepted {a.type} papers: median {med}, IQR [{lo}, {hi}]. Below the bottom quartile.',
            f'Raise to >= {int(lo)} (target ~{int(med)}) by citing the works the text already relies on (baselines, datasets, metrics, tools, every related-work claim); never pad.')
    elif nref < med:
        add('MINOR', 'References', f'{nref} printed references, between P25 {lo} and median {med} for {a.type} papers.', 'Check that every baseline/dataset/tool/claim is cited.')
    if missing: add('BLOCKER', 'bib', f'{len(missing)} cited keys missing from .bib (render as [?]): {", ".join(missing[:12])}', 'Add the entries or fix the keys.')
    if uncited and not nocite_all: add('MINOR', 'bib', f'{len(uncited)} .bib entries are never cited (not printed): {", ".join(uncited[:15])}', 'Either cite where the text relies on them or leave out; they do not count toward the reference list.')
    if nocite_all: add('MAJOR', 'bib', '\\nocite{*} prints uncited entries; reviewers read it as padding.', 'Remove \\nocite{*}; cite every entry in text.')
    # sections
    secs = split_sections(body); per = defaultdict(lambda: [0, 0, set()]); rel_paras = []; sec_rows = []
    for title, txt in secs:
        k = sec_kind(title); c = cite_cmds(txt); ks = keys_in(txt)
        per[k][0] += len(c); per[k][1] += len(ks); per[k][2].update(ks)
        sec_rows.append((clean(title)[:40], k, len(c), len(set(ks))))
        if k == 'related':
            txt2 = re.sub(r'\\(sub)*section\*?\{[^}]*\}', '\n\n', txt)
            for p in re.split(r'\n\s*\n|\\paragraph\*?\{', txt2):
                if len(clean(p)) > 250: rel_paras.append((len(cite_cmds(p)), clean(p)[:80]))
    inst = sum(v[0] for v in per.values())
    groups = [len([k for k in g.split(',') if k.strip()]) for g in cite_cmds(body)]
    grouped_share = sum(1 for g in groups if g > 1) / max(1, len(groups))
    big = sum(1 for g in groups if g >= 6)
    if big:
        add('MINOR', 'Citations', f'{big} citation group(s) with >= 6 references in one bracket (largest {max(groups)}).',
            'Accepted papers group 2-4 works for one shared claim and otherwise name each work with its own citation; split long dumps and say what each work does.')
    if inst and nref / inst > 1.6:
        add('MINOR', 'Citations', f'{nref} references for only {inst} citation commands: most references are cited in bulk once.',
            'Spread citations to where each work is used (intro claim, baseline, dataset, metric, tool, design choice).')
    for k, label in (('intro', 'Introduction'), ('related', 'Related work'), ('exp', 'Experiments')):
        lo_, med_, hi_ = N[k]
        if k in per or k != 'related':
            v = per[k][0] if k in per else 0
            if v < lo_ * 0.5 and lo_ > 1:
                add('MAJOR', label, f'{v} citation commands; accepted {a.type} papers: median {med_}, IQR [{lo_}, {hi_}].', f'Support each claim/system/dataset mentioned in {label.lower()} with a citation.')
            elif v < lo_:
                add('MINOR', label, f'{v} citation commands; P25 for {a.type} papers is {lo_}.', '')
    if 'related' not in per:
        add('BLOCKER' if a.type != 'industrial' else 'MAJOR', 'Related work', 'No Related Work section found.', 'Add a Related Work section (or a clearly titled subsection) with 3-6 themed paragraphs, each citing 3-6 works and ending with how this paper differs.')
    zero = [p for p in rel_paras if p[0] == 0]
    for c, head in zero:
        add('MAJOR', 'Related work', f'Related-work paragraph without any citation: "{head}..."', 'Every related-work paragraph cites the works it describes.')
    if rel_paras:
        ppp = sum(p[0] for p in rel_paras) / len(rel_paras)
        if ppp < N['per_related_para'][0]:
            add('MINOR', 'Related work', f'{ppp:.1f} citation commands per related-work paragraph; P25 = {N["per_related_para"][0]}.', 'Name and cite the representative works of each line of research.')
    # captions
    for cap in re.findall(r'\\caption\{((?:[^{}]|\{[^{}]*\})*)\}', body):
        if '\\cite' in cap:
            add('MINOR', 'Caption', f'Citation inside a caption: "{clean(cap)[:70]}"', 'Accepted papers almost never cite in captions (5 of 694); move the citation to the body text that introduces the figure/table.')
    # names
    nb = re.sub(r'\\begin\{abstract\}.*?\\end\{abstract\}', ' ', body, flags=re.S)
    m_ = re.search(r'\\maketitle', nb)
    if m_: nb = nb[m_.end():]
    # AI-use acknowledgements name tools/models by policy, not as scholarly claims: skip them for name checks
    nb = re.sub(r'\\section\*?\{[^}]*(?:Generative AI|AI-Generated|Use of AI|AI Use)[^}]*\}.*?(?=\\section|\\bibliography|\\end\{document\}|$)', ' ', nb, flags=re.S | re.I)
    nb = re.sub(r'\\paragraph\*?\{[^\n]{0,40}?(?:Generative AI|AI\}?-Generated|Use of AI|AI Use)[^\n]*?\n.*?(?=\n\s*\n|\\section|\\paragraph|\\bibliography|$)', ' ', nb, flags=re.S | re.I)
    nu, prefix = names_used(nb, bib)
    tabn = table_names(body)
    cited_names = {n for n, occ in nu.items() if any(c for _, c in occ)}
    uncited_names = []
    for n, occ in sorted(nu.items(), key=lambda x: x[1][0][0]):
        first_cited = any(c for _, c in occ[:2])
        if first_cited: continue
        strong = n.lower() in prefix
        if strong or (len(occ) >= 3 and n not in cited_names) or (n in tabn and n not in cited_names and len(occ) >= 2):
            uncited_names.append((n, len(occ), strong, prefix.get(n.lower())))
    ku = known_uncited(nb)
    ku = [(n, c, a_) for n, c, a_ in ku if n not in NAMES_OWN]
    if ku:
        add('MAJOR' if any(not a_ for _, _, a_ in ku) else 'MINOR', 'Names',
            'Well-known external systems / benchmarks / models / tools whose first mention carries no citation: ' + ', '.join(f'{n}({c}x{"" if a_ else ", never cited"})' for n, c, a_ in ku),
            'Cite at first use: system/benchmark paper, model technical report or official model card, tool paper or official documentation (@misc with URL).')
    # LLMs used as baselines/generators/judges must cite a technical report or official model/system card (R2)
    MODEL_PAT = re.compile(r'(?i)(?<![\w-])(gpt-\d[\w.]*(?:-[a-z]+)?|claude|opus[~ ]?\d[\d.]*|sonnet[~ ]?\d[\d.]*|deepseek[\w.-]*|qwen[\w.-]*|kimi[\w.-]*|glm-\d[\w.-]*|gemini[\w.-]*|llama[\w.-]*|mistral[\w.-]*)')
    VENDOR = re.compile(r'(?i)openai|anthropic|deepseek|qwen|alibaba|moonshot|kimi|zhipu|z\.ai|\bglm|gemini|llama|mistral|system card|model card|technical report')
    models = Counter(m.group(1).lower().replace('~', ' ') for m in MODEL_PAT.finditer(nb))
    if models:
        vend = [k for k in printed if k in bib and VENDOR.search(' '.join(bib[k]['fields'].get(x, '') for x in ('author', 'title', 'howpublished', 'url', 'note', 'institution')))]
        if not vend:
            add('MAJOR', 'Models', 'LLMs are used but no technical report / official model or system card is cited: ' + ', '.join(f'{m}({c}x)' for m, c in models.most_common(12)),
                'Cite each model family once at first use: its arXiv technical report or the vendor system/model card (@misc with URL, access date, exact version).')
    for term, cnt, ref in stat_uncited(body, bib, printed):
        add('MINOR', 'Statistics', f'Statistical method "{term}" used {cnt}x without a citation.', f'Cite the original method once at first use (e.g., {ref}); verify the DOI before adding.')
    strong_list = [(n, c, k) for n, c, st_, k in uncited_names if st_]
    weak_list = [(n, c) for n, c, st_, k in uncited_names if not st_]
    for n, cnt, key in strong_list:
        add('MAJOR', 'Names', f'"{n}" is used {cnt}x; first mention not cited although the bib holds {key}.', f'Add \\cite{{{key}}} at the first mention.')
    if weak_list:
        add('MAJOR' if len(weak_list) >= 5 else 'MINOR', 'Names', f'{len(weak_list)} capitalised names used without a citation at first mention: ' + ', '.join(f'{n}({c})' for n, c in weak_list[:40]),
            'For each external system / baseline / dataset / benchmark / metric / tool / model: cite its paper (or official doc / model card / repo) at first use. Own artefacts: pass --own.')
    # entries
    venue_forms = defaultdict(Counter)
    L = Lookup(a.cache, a.online); lookups = 0; ver = {}
    for k in printed:
        e = bib[k]; f = e['fields']; t = e['type']
        if not f.get('title'): add('MAJOR', k, 'Entry has no title.', 'Fill title.')
        if not f.get('year') and not f.get('date'): add('MINOR', k, 'Entry has no year.', 'Add year.')
        if not f.get('author') and t not in ('misc', 'online', 'software', 'manual'): add('MINOR', k, 'Entry has no author.', 'Add authors.')
        if t in ('inproceedings', 'article', 'conference') and not is_arxiv(e):
            if not f.get('doi') and not NO_DOI_VENUES.search(f.get('booktitle', '') + f.get('journal', '')): add('MINOR', k, f'@{t} without DOI.', 'Add DOI (ACM/IEEE/ACL Anthology DOIs exist for nearly all CCF-A venues).')
            if not f.get('pages') and not f.get('articleno') and not f.get('numpages') and not re.search(r'(?i)corr|arxiv', f.get('journal', '')):
                add('MINOR', k, f'@{t} without pages/article number.', 'Add pages (or articleno for PACMMOD).')
            ven = f.get('booktitle', '') + ' ' + f.get('journal', '')
            for vn, pats in VENUE_ALIASES.items():
                for p in pats:
                    if re.search(p, ven):
                        if vn == 'sigmod' and re.search(r'(?i)SIGACT|PODS|Principles of Database|ACM on Management of Data|Record|Companion', ven): break
                        form = re.sub(r'(?i)\b(\d+(st|nd|rd|th)?|first|second|third|[a-z]+-?(first|second|third|fourth|fifth|sixth|seventh|eighth|ninth)|[a-z]*(tenth|eleventh|twelfth|teenth|tieth)|annual)\b', ' ', clean(ven))
                        form = re.sub(r'\(?(SIGMOD|ICDE|VLDB)\s*\d*\)?|\d{2,4}|[\'’]', ' ', form)
                        venue_forms[vn][' '.join(form.lower().split())[:60]] += 1; break
        if a.online and lookups < a.max_lookups:
            lookups += 1
            r = verify(e, L); ver[k] = r
            if r['status'] == 'mismatch':
                add('BLOCKER', k, 'Metadata does not match the record found online: ' + '; '.join(r['notes']), 'Correct the entry from the publisher/DBLP record.')
            elif r['status'] == 'unverified':
                add('MAJOR', k, f'Could not verify existence online (title: "{clean(f.get("title", ""))[:80]}"). ' + '; '.join(r['notes']), 'Check manually; if it cannot be found on DBLP/Crossref/publisher/official site, remove it.')
            fv = family(f.get('booktitle', '') + ' ' + f.get('journal', '')); ff = family(r.get('venue_found', ''))
            if r['status'] == 'verified' and fv and ff and fv != ff:
                add('MAJOR', k, f'Venue in .bib ({fv}) differs from the venue found online ({ff}: "{r.get("venue_found", "")[:60]}").', 'Fix booktitle/journal from the DBLP or publisher record.')
            if r.get('pub'):
                p = r['pub']
                add('MAJOR', k, f'arXiv/CoRR entry, but a peer-reviewed version exists: {p.get("venue")} DOI {p.get("doi") or "-"} (index year {p.get("year") or "?"} may be the arXiv year; take edition/year/pages from DBLP or the publisher page)', 'Cite the published version (keep arXiv only for extended versions explicitly needed).')
            if r.get('found_doi') and not f.get('doi'):
                for x in findings:
                    if x['where'] == k and 'without DOI' in x['msg']: x['fix'] = f'Add doi = {{{r["found_doi"]}}}'
            if lookups % 20 == 0: L.save()
        elif is_arxiv(e):
            add('MINOR', k, 'arXiv/CoRR entry; run with --online to check for a published version.', '')
    L.save()
    for vn, c in venue_forms.items():
        if len(c) > 1:
            add('MINOR', 'bib', f'Venue "{vn}" spelled {len(c)} ways: ' + ' | '.join(f'"{x}"x{n}' for x, n in c.most_common(4)), 'Use one form for every entry of the same venue.')
    # shares
    yrs = []
    for k in printed:
        y = re.search(r'(19|20)\d\d', bib[k]['fields'].get('year', '') or bib[k]['fields'].get('date', ''))
        if y: yrs.append(int(y.group(0)))
    recent = sum(1 for y in yrs if y >= a.pubyear - 2) / max(1, len(yrs))
    arx = sum(1 for k in printed if is_arxiv(bib[k])) / max(1, nref)
    web = sum(1 for k in printed if is_web(bib[k])) / max(1, nref)
    if arx > max(0.30, N['arxiv'][2] + 0.1):
        add('MAJOR', 'References', f'{arx:.0%} of references are arXiv-only; accepted {a.type} papers: median {N["arxiv"][1]:.0%}, P75 {N["arxiv"][2]:.0%}.', 'Replace with published versions; balance with peer-reviewed DB/NLP venues.')
    if recent < 0.2 and a.type != 'industrial':
        add('MINOR', 'References', f'Only {recent:.0%} of references are from the last 3 years.', 'Cite the current SOTA (last 3 years) the reviewers will expect.')
    if web > 0.25:
        add('MINOR', 'References', f'{web:.0%} of references are web/software/manual entries.', 'Keep docs for tools, but cite papers for ideas and systems.')
    pdfinfo = pdf_ref_count(a.pdf) if a.pdf else None
    summary = {'tex': a.tex, 'type': a.type, 'printed_refs': nref, 'bib_entries': len(bib), 'norm_refs': N['refs'],
               'cite_instances': inst, 'grouped_share': round(grouped_share, 2), 'max_group': max(groups) if groups else 0, 'per_section': {k: v[0] for k, v in per.items()},
               'per_section_unique': {k: len(v[2]) for k, v in per.items()},
               'related_paragraphs': len(rel_paras), 'related_zero_cite_paragraphs': len(zero),
               'recent3': round(recent, 2), 'arxiv_share': round(arx, 2), 'web_share': round(web, 2), 'pdf': pdfinfo,
               'verified': sum(1 for r in ver.values() if r['status'] == 'verified'), 'checked': len(ver),
               'counts': dict(Counter(x['sev'] for x in findings))}
    order = {'BLOCKER': 0, 'MAJOR': 1, 'MINOR': 2}
    findings.sort(key=lambda x: order[x['sev']])
    md = [f"# reflint report: {os.path.basename(a.tex)} ({a.type})", '',
          f"- printed references: **{nref}** (bib entries {len(bib)}; norm for {a.type}: median {N['refs'][1]}, IQR [{N['refs'][0]}, {N['refs'][2]}])",
          f"- citation commands: {inst}; per section: " + ', '.join(f'{k}={v[0]} ({len(v[2])} refs)' for k, v in per.items()),
          f"- related-work paragraphs: {len(rel_paras)}, without citation: {len(zero)}",
          f"- last-3-years share {recent:.0%}; arXiv-only {arx:.0%}; web/software {web:.0%}",
          f"- online verification: {summary['verified']}/{summary['checked']} verified" if a.online else '- online verification: not run (use --online)',
          f"- findings: {summary['counts']}", '', '| Sev | Where | Finding | Fix |', '|---|---|---|---|']
    for x in findings:
        md.append(f"| {x['sev']} | {x['where']} | {x['msg'].replace('|', '/')} | {x['fix'].replace('|', '/')} |")
    md += ['', '## Sections', '| Section | Kind | \\cite cmds | unique refs |', '|---|---|---|---|'] + [f'| {t} | {k} | {c} | {u} |' for t, k, c, u in sec_rows]
    if ver:
        md += ['', '## Verification', '| key | status | source | published version |', '|---|---|---|---|']
        for k, r in ver.items():
            md.append(f"| {k} | {r['status']} | {r['source'] or ''} | {(r.get('pub') or {}).get('venue', '') or ''} {(r.get('pub') or {}).get('doi', '') or ''} |")
    rep = '\n'.join(md)
    if a.out: open(a.out, 'w').write(rep)
    else: print(rep)
    if a.json: json.dump({'summary': summary, 'findings': findings, 'verification': ver}, open(a.json, 'w'), indent=1, ensure_ascii=False)
    print(json.dumps(summary, ensure_ascii=False), file=sys.stderr)

if __name__ == '__main__':
    main()
