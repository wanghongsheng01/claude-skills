#!/usr/bin/env python3
"""Rank the ICDE 2027 CMT subject areas for a paper.

usage: suggest_areas.py <paper_dir | main.tex | paper.pdf> [--top 6] [--eab] [--md areas.md]
                        [--choose "Primary area; Secondary 1; Secondary 2; ..."]

Reads LaTeX sources (main file plus \\input/\\include files, recursively) or a PDF (needs PyMuPDF or pypdf),
splits title, abstract, keywords/index terms, headings and body, and scores every area by the signal words in
AREAS below: weight 3 in title, abstract and keywords, 2 in headings, 1 in the body (body hits capped per word so
long papers do not drown the front matter). Prints the ranking with the matched words, a suggested Primary and
2-3 Secondaries, and the reminders of SKILL.md section 2. The ranking is evidence; the final choice applies the
rules (primary = community that judges the main contribution).
Signal words prefixed with "~" are generic (edges, joins, queries, schema, maintenance ...): they occur in most data
papers, so they count with a third of the weight. The titles in the paper's .bib files are a separate evidence
source (weight 1.5, capped): the community of the cited work is the community of the reviewers.
--choose validates the final choice against the verbatim CMT names and prints where each box is on the form
(the form lists the areas alphabetically in two columns; each row has a Primary box, then a Secondary box).
--md writes references/areas.md from AREAS (the single source of the signal words).
"""
import argparse, glob, os, re, sys

# (CMT name, short scope, signal regexes). Names are verbatim from the ICDE 2027 CMT form (checked 2026-11-11).
AREAS = [
    ("AI and machine learning for data systems and vice versa", "learned components inside data systems; data systems for ML",
     [r"machine learning", r"\blearned (index|optimizer|cost|cardinality)", r"neural network", r"reinforcement learning",
      r"deep learning", r"\bml model", r"training data", r"feature store", r"model serving"]),
    ("Benchmarking, performance modeling, tuning, and testing", "benchmarks, experimental studies, cost/performance models, tuning, testing",
     [r"\bbenchmark", r"experimental (study|survey|evaluation of)", r"performance model", r"\btuning\b", r"knob",
      r"\btesting\b", r"\bfuzz", r"reproducib"]),
    ("Cloud data management", "cloud-native, serverless, multi-tenant, disaggregated data systems",
     [r"\bcloud", r"serverless", r"multi-tenan", r"disaggregat", r"object stor", r"\bsaas\b"]),
    ("Data mining with a data-centric focus", "mining algorithms over data (patterns, clusters, outliers, communities)",
     [r"data mining", r"frequent (pattern|itemset)", r"clustering", r"outlier", r"anomaly detection", r"community detection",
      r"cohesive subgraph", r"\bk-core\b", r"\bk-plex\b", r"dense subgraph"]),
    ("Data models, semantics, and query languages", "data models, query languages, formal semantics, Datalog",
     [r"query language", r"\bdatalog\b", r"semantics", r"data model", r"relational algebra", r"recursive quer",
      r"~\bschema\b", r"type system", r"declarative"]),
    ("Data preparation, cleaning, and integration", "cleaning, entity resolution, schema matching, integration, discovery",
     [r"data cleaning", r"entity (resolution|matching)", r"schema matching", r"data integration", r"data lake",
      r"join discovery", r"table union", r"imputation", r"\betl\b", r"data preparation", r"deduplicat",
      r"join inference", r"foreign[- ]key (detection|discovery)", r"(data|dataset) discovery", r"view discovery",
      r"key detection", r"bi-?models?"]),
    ("Data pricing and markets", "pricing data and queries, data marketplaces",
     [r"data (pricing|market)", r"query pricing", r"marketplace", r"\bprice\b"]),
    ("Data quality, curation, provenance, and workflows", "quality, constraints, provenance/lineage, curation, workflows",
     [r"data quality", r"provenance", r"lineage", r"curation", r"workflow", r"data validation", r"integrity constraint",
      r"functional dependenc", r"denial constraint", r"inclusion dependenc", r"unique column combination",
      r"dependency discovery", r"data profiling", r"\bprofil", r"\bcertif", r"verification of (keys|constraints)",
      r"orphan", r"duplicate(d)? key", r"data defect", r"dirty data"]),
    ("Data security and privacy", "access control, authorization, privacy, encryption, secure query processing",
     [r"access control", r"authori[sz]ation", r"permission", r"privacy", r"differential privacy", r"encrypt",
      r"\bsecurity\b", r"row-level security", r"\bpolicy\b", r"\bpolicies\b", r"revocation", r"\bdeny\b", r"zanzibar",
      r"\brebac\b", r"\brbac\b", r"\babac\b"]),
    ("Data streams, complex event processing, and edge computing", "streams, windows, CEP, IoT and edge",
     [r"\bstream", r"complex event", r"sliding window", r"edge computing", r"\biot\b", r"continuous quer", r"event processing"]),
    ("Data systems on modern hardware", "GPU, FPGA, NVM/CXL, RDMA, SIMD-aware data systems",
     [r"\bgpu", r"\bfpga", r"persistent memory", r"\bnvm\b", r"\brdma\b", r"\bsimd\b", r"\bcxl\b", r"modern hardware", r"accelerator"]),
    ("Data visualization and interactive data exploration", "visual analytics, interactive exploration, dashboards",
     [r"visuali[sz]ation", r"interactive (data )?exploration", r"dashboard", r"visual analytic"]),
    ("Distributed and parallel data management", "distribution, replication, partitioning, parallel processing",
     [r"distributed", r"parallel", r"replica", r"replication", r"partitioning", r"consensus", r"scale-out", r"\bshard"]),
    ("Distributed ledgers and blockchains", "blockchains, ledgers, smart contracts",
     [r"blockchain", r"\bledger", r"smart contract"]),
    ("Domain-specific data engineering (scientific, medical, climate, urban, etc.)", "data engineering for a science or application domain",
     [r"scientific data", r"medical", r"clinical", r"climate", r"\burban\b", r"genom", r"healthcare", r"e-commerce", r"\berp\b"]),
    ("Energy-efficient data engineering", "energy and carbon efficiency of data processing",
     [r"\benergy", r"power consumption", r"carbon", r"green comput"]),
    ("Explainability, fairness, bias, trust, authentication, and regulatory compliance", "explanations, fairness, trust, authentication, compliance",
     [r"explanation", r"explainab", r"fairness", r"\bbias\b", r"\btrust", r"authenticat", r"compliance", r"\bgdpr\b", r"regulat", r"\baudit"]),
    ("Foundation models and LLMs for data engineering and vice versa", "LLMs/foundation models used for or served by data systems",
     [r"\bllms?\b", r"large language model", r"foundation model", r"\bgpt", r"\bprompt", r"text-to-sql", r"\bnl2sql\b",
      r"semantic operator", r"\bagent", r"\brag\b"]),
    ("Graph data", "graph storage, indexing, querying and algorithms (reachability, paths, subgraphs, dynamic graphs)",
     [r"~\bgraphs?\b", r"reachability", r"shortest path", r"subgraph", r"\bvertex", r"\bvertices", r"2-hop", r"hub label",
      r"transitive closure", r"dynamic graph", r"~\bedges?\b", r"\bbfs\b", r"~traversal"]),
    ("Knowledge graphs for data engineering", "KGs, RDF, SPARQL, ontologies, entity linking",
     [r"knowledge graph", r"\brdf\b", r"sparql", r"ontolog", r"entity linking", r"\btriples?\b"]),
    ("Multi-modal and heterogeneous data", "text, images, video, tables and mixed-model data",
     [r"multi-?modal", r"heterogeneous data", r"\bimages?\b", r"\bvideo", r"unstructured", r"semi-structured", r"\bjson\b"]),
    ("Multidimensional data, data warehousing, OLAP, and analytics", "OLAP, cubes, warehouses, BI and aggregate analytics",
     [r"\bolap\b", r"data cube", r"data warehous", r"~aggregat", r"~analytic", r"\bbi\b", r"business intelligence",
      r"summarizab", r"fan trap", r"semantic layer", r"star schema", r"snowflake", r"fact table", r"dimension table"]),
    ("Query processing and optimization", "query execution, joins, cardinality, plans, caching and reuse",
     [r"query processing", r"query optimi", r"~\bjoins?\b", r"~cardinality", r"cost model", r"query plan", r"~execution",
      r"materiali[sz]ed view", r"\bcache", r"top-k", r"~\bqueries\b", r"~\blatency\b", r"view maintenance"]),
    ("Responsible and ethical data management", "responsible, ethical, consent-aware data management",
     [r"responsible", r"ethic", r"consent", r"societal"]),
    ("Storage, indexing, and physical database design", "indexes, storage layouts, compression, physical design",
     [r"\bindex", r"indexing", r"\bstorage", r"physical design", r"b\+?-tree", r"\blsm", r"compression", r"~\blabels?\b",
      r"\blayout", r"index size", r"~maintenance"]),
    ("Time-series, temporal, spatial, and spatio-temporal data", "time series, temporal databases, spatial and trajectory data",
     [r"time[- ]series", r"temporal", r"spatial", r"trajector", r"geo", r"spatio-temporal"]),
    ("Transaction management, concurrency control, and recovery", "transactions, isolation, concurrency, logging, recovery",
     [r"transaction", r"concurren", r"isolation", r"serializab", r"recovery", r"write-ahead", r"\bmvcc\b", r"snapshot",
      r"acknowledg", r"consistency"]),
    ("Uncertain, probabilistic, and approximate data", "approximation, sampling, probabilistic data, error guarantees",
     [r"approximat", r"~sampling", r"probabilistic", r"uncertain", r"confidence interval", r"error bound", r"\bsketch",
      r"\baqp\b", r"~estimat"]),
    ("Vector data", "vector search, ANN indexes, embeddings",
     [r"\bvector", r"\bann\b", r"nearest neighbo", r"embedding", r"similarity search", r"\bhnsw\b", r"filtered search"]),
]
NONE = "None Of Above"


def read_tex(path):
    root = path if os.path.isdir(path) else os.path.dirname(path)
    main = path if path.endswith('.tex') else next((f for f in glob.glob(os.path.join(root, '*.tex'))
                                                     if '\\documentclass' in open(f, errors='ignore').read()), None)
    if not main:
        sys.exit('no main .tex with \\documentclass found')
    seen = set()

    def expand(f):
        if f in seen or not os.path.exists(f):
            return ''
        seen.add(f)
        t = open(f, errors='ignore').read()
        t = re.sub(r'(?<!\\)%.*', '', t)
        return re.sub(r'\\(input|include)\{([^}]+)\}',
                      lambda m: expand(os.path.join(root, m.group(2) if m.group(2).endswith('.tex') else m.group(2) + '.tex')), t)
    t = expand(main)
    title = re.search(r'\\title\{(.*?)\}\s*\n', t, re.S)
    abstract = re.search(r'\\begin\{abstract\}(.*?)\\end\{abstract\}', t, re.S)
    kw = re.search(r'\\begin\{(IEEEkeywords|keywords)\}(.*?)\\end\{\1\}', t, re.S)
    heads = ' '.join(re.findall(r'\\(?:sub)*section\*?\{([^}]*)\}', t) + re.findall(r'\\textbf\{([^}]{3,60})\}', t))
    body = re.sub(r'\\begin\{thebibliography\}.*', '', t, flags=re.S)
    bib = ' '.join(re.findall(r'\btitle\s*=\s*[{"](.*?)[}"]\s*,', ' '.join(open(f, errors='ignore').read()
                   for f in glob.glob(os.path.join(root, '*.bib'))), re.S | re.I))
    bib += ' '.join(re.findall(r'\\bibitem.*?\n(.*?)(?=\\bibitem|\\end\{thebibliography\})', t, re.S))
    return (title.group(1) if title else ''), (abstract.group(1) if abstract else ''), (kw.group(2) if kw else ''), heads, body, bib


def read_pdf(path):
    try:
        import fitz
        pages = [p.get_text() for p in fitz.open(path)]
    except ImportError:
        from pypdf import PdfReader
        pages = [p.extract_text() or '' for p in PdfReader(path).pages]
    t = '\n'.join(pages)
    t = t.split('\nREFERENCES')[0].split('\nReferences')[0]
    first = pages[0]
    m = re.search(r'Abstract[—\-–:.]+(.*?)(Index Terms|Keywords|I\. I|1 I)', first, re.S)
    k = re.search(r'(Index Terms|Keywords)[—\-–:.]+(.*?)(I\. I|1 I|\n\n)', first, re.S)
    title = first.strip().split('\n')[0:3]
    heads = ' '.join(re.findall(r'\n([IVX]+\. [A-Z][A-Z ,\-]+)\n', t))
    full = '\n'.join(pages)
    refs = re.split(r'\n\s*R\s?EFERENCES\s*\n|\nReferences\s*\n', full)
    return ' '.join(title), (m.group(1) if m else ''), (k.group(2) if k else ''), heads, t, (refs[-1] if len(refs) > 1 else '')


def score(parts, eab=False):
    title, abstract, kw, heads, body, bib = [re.sub(r'\s+', ' ', p.lower()) for p in parts]
    front = title + ' ' + abstract + ' ' + kw
    res = []
    for name, scope, pats in AREAS:
        s, ev = 0.0, []
        for p in pats:
            w = 1 / 3 if p.startswith('~') else 1.0  # generic words (in most data papers) count a third
            p = p.lstrip('~')
            nf, nh, nb, nr = (len(re.findall(p, x)) for x in (front, heads, body, bib))
            sub = w * (3 * nf + 2 * nh + min(nb, 25) ** 0.5 * 2 + 1.5 * min(nr, 9) ** 0.5 * 2)
            if sub:
                s += sub; ev.append((sub, p.replace('\\b', ''), nf, nb, nr))
        if eab and name.startswith('Benchmarking'):
            s += 10; ev.append((10, 'EAB paper', 0, 0, 0))
        res.append((s, name, scope, sorted(ev, reverse=True)[:5]))
    return sorted(res, reverse=True)


def write_md(path):
    out = ['# ICDE 2027 CMT subject areas: scope and signal words', '',
           'Generated from `scripts/suggest_areas.py` (AREAS). Names are verbatim from the CMT form (checked 2026-11-11).', '',
           '| Area | Covers | Signal words (regex) |', '|---|---|---|']
    for name, scope, pats in AREAS:
        out.append(f'| {name} | {scope} | ' + ', '.join(f'`{p}`' for p in pats).replace('|', '\\|') + ' |')
    out += ['', f'"{NONE}" exists as a Primary box only; never use it when an area fits.', '',
            '## Typical pairings seen in ICDE papers', '',
            '- Index or algorithm for a data type: primary = the data type (Graph data, Vector data, Time-series ...); '
            'secondary = Storage, indexing, and physical database design and/or Query processing and optimization.',
            '- Security/privacy application of a data-management technique: primary = the technique\'s area; secondary = '
            'Data security and privacy (primary only if the contribution is the security mechanism or guarantee).',
            '- LLM labels with statistical guarantees: primary = Uncertain, probabilistic, and approximate data; secondary = '
            'Foundation models and LLMs ...; add Multidimensional data ... for aggregate/BI queries.',
            '- EAB / benchmark paper: Benchmarking, performance modeling, tuning, and testing (primary if the benchmark is '
            'the contribution) plus the area of the systems benchmarked.',
            '- Cleaning/integration/discovery with constraints: Data preparation, cleaning, and integration + Data quality, '
            'curation, provenance, and workflows.']
    open(path, 'w').write('\n'.join(out) + '\n')


def form_position(name):
    """Row and column of an area on the CMT form: alphabetical order, left column 1-16, right column 17-30."""
    names = [n for n, _, _ in AREAS] + [NONE]
    i = names.index(name)
    return ('left', i + 1) if i < 16 else ('right', i - 15)


def choose(spec):
    names = {n.lower(): n for n, _, _ in AREAS}
    picks = [x.strip() for x in spec.split(';') if x.strip()]
    bad = [x for x in picks if x.lower() not in names]
    if bad:
        sys.exit('not a CMT area name (copy it verbatim): ' + '; '.join(bad))
    picks = [names[x.lower()] for x in picks]
    if len(set(picks)) != len(picks):
        sys.exit('an area is listed twice: tick only one of its two boxes')
    if not 2 <= len(picks) <= 5:
        print('warning: choose one Primary and 2-3 (at most 4) Secondary areas')
    print('Tick on the CMT form (each row: Primary box, then Secondary box):')
    for k, n in enumerate(picks):
        col, row = form_position(n)
        print(f'  {"PRIMARY  " if k == 0 else "Secondary"}  {col} column, row {row:2d}: {n}  -> tick the '
              f'{"first (Primary)" if k == 0 else "second (Secondary)"} box')
    print('Leave every other box empty, including "None Of Above"; never tick both boxes of one area.')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('paper', nargs='?')
    ap.add_argument('--top', type=int, default=6)
    ap.add_argument('--eab', action='store_true')
    ap.add_argument('--md', help='write the area reference table to this path and exit')
    ap.add_argument('--choose', help='"Primary; Secondary; ..." verbatim CMT names: validate and print where to tick')
    a = ap.parse_args()
    if a.md:
        write_md(a.md); print('wrote', a.md); return
    if a.choose:
        choose(a.choose)
        if not a.paper:
            return
    if not a.paper:
        ap.error('paper path required')
    parts = read_pdf(a.paper) if a.paper.lower().endswith('.pdf') else read_tex(a.paper)
    eab = a.eab or 'experiment, analysis' in parts[0].lower()
    ranked = score(parts, eab)
    print('Ranking (score, area, top evidence: word [front-matter / body / cited titles]):')
    for i, (s, name, scope, ev) in enumerate(ranked[:a.top], 1):
        print(f'{i:2d}. {s:6.1f}  {name}')
        print('        ' + '; '.join(f'{w} [{nf}/{nb}/{nr}]' for _, w, nf, nb, nr in ev))
    top = [r for r in ranked if r[0] > 0]
    if not top:
        print(f'\nNo area matched; check the input. Use "{NONE}" only if no area fits after reading the paper.')
        return
    print(f'\nSuggested Primary  : {top[0][1]}')
    sec = [r[1] for r in top[1:4] if r[0] >= 0.3 * top[0][0]]
    print('Suggested Secondary: ' + ('; '.join(sec) if sec else '(none above 30% of the primary score)'))
    print('\nBefore ticking (SKILL.md section 2): primary = the community that judges the main contribution and appears '
          'in the title/abstract; keep 2-3 secondaries that a section of the paper supports; drop areas matched only by '
          'incidental words; never use "None Of Above" when an area fits.')


if __name__ == '__main__':
    main()
