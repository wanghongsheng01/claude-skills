#!/usr/bin/env python3
"""Prepare every field of the ICDE CMT "Create New Submission" form from a paper and check it against the PDF.

usage: prepare_cmt.py <paper_dir> --pdf <submitted.pdf> --artifact-url <url> [--authors authors.json]
                      [--relevance relevance.txt] [--withheld "reason ..."] [--eab] [--out cmt_form.md]
                      [--areas "Primary; Secondary 1; Secondary 2"]

Writes one Markdown file with the reviewer-facing English text for each CMT field (title, abstract, authors,
subject areas, file, TPMS, the ten additional questions with the two text boxes) and a check list:
- the abstract is rebuilt from the LaTeX source (\\newcommand macros expanded, so numbers.tex values appear) and
  compared word for word with the abstract printed on page 1 of the PDF; CMT limit 2,000 characters;
- the title is compared with the PDF; the PDF must be <= 20 MB, US Letter, fonts embedded, body <= 12 pages;
- the relevance text must stay within 1,000 characters (CFP; line breaks counted as CMT counts them) and follow the
  form's instructions: name the topic area(s), (a) the data-engineering challenge, (b) the contributions with section
  numbers that exist in the PDF, (c) work published in ICDE or another core outlet (VLDB, SIGMOD) that it builds on,
  each cited as NAME, VENUE'YY with a matching entry in the paper's .bib files; non-core venues in (c) are flagged;
- the subject areas come from ../icde-subject-areas/scripts/suggest_areas.py when it is installed.
authors.json: [{"email": ..., "first": ..., "last": ..., "organization": ..., "country": ..., "orcid": ...,
"primary_contact": true}, ...] in author order. Without it, names and e-mails are parsed from the IEEEtran block.
"""
import argparse, glob, json, os, re, subprocess, sys

CMT_ABSTRACT_MAX = 2000      # CMT counter on the ICDE 2027 form ("characters left")
RELEVANCE_MAX = 1000         # CFP: "explain (in 1000 characters)"; the CMT box itself allows 8,000
FILE_MAX_MB = 20             # CMT: "Maximum file size is 20 Mb. We accept doc, docx, pdf formats."

QUESTIONS = [  # (number, title, kind) as on the ICDE 2027 Research Second Round form (2026-11-11)
    (1, "Desk Rejection Policy", "agree"),
    (2, "Maximum number of submissions per author", "agree"),
    (3, "Relevance", "text"),
    (4, "Duplicate Submissions", "agree"),
    (5, "Conflicts of Interest", "agree"),
    (6, "Integrity of the review process", "agree"),
    (7, "Authorship", "agree"),
    (8, "Availability", "text"),
    (9, "Registration for accepted papers", "agree"),
    (10, "Presentation for accepted papers", "agree"),
]


def load_tex(root):
    main = next((f for f in glob.glob(os.path.join(root, '*.tex')) if '\\documentclass' in open(f, errors='ignore').read()), None)
    if not main:
        sys.exit('no main .tex found in ' + root)
    seen = set()

    def expand(f):
        if f in seen or not os.path.exists(f):
            return ''
        seen.add(f)
        t = re.sub(r'(?<!\\)%.*', '', open(f, errors='ignore').read())
        return re.sub(r'\\(input|include)\{([^}]+)\}',
                      lambda m: expand(os.path.join(root, m.group(2) if m.group(2).endswith('.tex') else m.group(2) + '.tex')), t)
    return expand(main)


def macros(tex):
    M = {}
    for m in re.finditer(r'\\(?:re)?newcommand\{?\\([A-Za-z]+)\}?(?:\[\d\])?\{((?:[^{}]|\{[^{}]*\})*)\}', tex):
        M[m.group(1)] = m.group(2)
    return M


def plain(s, M):
    for _ in range(4):   # nested macros
        s = re.sub(r'\\([A-Za-z]+)\b', lambda m: M.get(m.group(1), '\\' + m.group(1)), s)
    greek = {'epsilon': 'ε', 'varepsilon': 'ε', 'delta': 'δ', 'Delta': 'Δ', 'rho': 'ρ', 'alpha': 'α', 'beta': 'β',
             'gamma': 'γ', 'lambda': 'λ', 'theta': 'θ', 'sigma': 'σ', 'tau': 'τ', 'phi': 'φ', 'Omega': 'Ω', 'omega': 'ω',
             'pi': 'π', 'le': '≤', 'leq': '≤', 'ge': '≥', 'geq': '≥', 'approx': '≈', 'cdot': '·', 'infty': '∞'}
    s = re.sub(r'\\(' + '|'.join(sorted(greek, key=len, reverse=True)) + r')(?![A-Za-z])', lambda m: greek[m.group(1)], s)
    s = re.sub(r'\(([εδρα-ω]),\s*([εδρα-ω])\)', r'(\1, \2)', s)  # (\epsilon,\delta) -> (ε, δ) as printed
    rep = [(r'\\xspace', ''), (r'\\ensuremath\{\\times\}', '×'), (r'\$\\times\$', '×'), (r'\\times', '×'),
           (r'\{,\}', ','), (r'\\,', ' '), (r'~', ' '), (r'--', '–'), (r'\\url\{([^}]*)\}', r'\1'),
           (r'\\emph\{([^}]*)\}', r'\1'), (r'\\textit\{([^}]*)\}', r'\1'), (r'\\textbf\{([^}]*)\}', r'\1'),
           (r'\\texttt\{([^}]*)\}', r'\1'), (r'\\%', '%'), (r'\$([^$]*)\$', r'\1'), (r'\\mu', 'µ'), (r'``|\'\'', '"'),
           (r'\\[A-Za-z]+\{([^}]*)\}', r'\1'), (r'[{}]', ''), (r'\s+', ' ')]
    for a, b in rep:
        s = re.sub(a, b, s)
    return s.strip()


def norm(s):
    return re.sub(r'[^a-z0-9]', '', s.lower().replace('×', 'x'))


def pdf_info(path):
    import fitz
    d = fitz.open(path)
    first = d[0].get_text()
    fonts = {(f[3], f[2], f[1]) for p in d for f in p.get_fonts(full=True)}
    text = [p.get_text() for p in d]
    # the heading is a whole line in capitals ("REFERENCES", small caps may extract as "R EFERENCES"); a case-
    # insensitive prefix match also hit body lines such as "references of ..." and under-counted the body
    head = r'^\s*(AI-G\s?ENERATED C\s?ONTENT A\s?CKNOWLEDGE?MENT|R\s?EFERENCES)\s*$'
    body_end = next((i for i, t in enumerate(text) if re.search(head, t, re.M)), len(text))
    heading_first = body_end < len(text) and len(re.split(head, text[body_end], flags=re.M)[0].strip()) < 40
    body_pages = body_end if heading_first else body_end + 1
    secs = re.findall(r'^\s*([IVX]+)\. [A-Z][A-Z]', '\n'.join(text), re.M)
    return dict(pages=len(d), size=(round(d[0].rect.width), round(d[0].rect.height)), mb=os.path.getsize(path) / 1e6,
                type3=[f[0] for f in fonts if f[1] == 'Type3'], first=first, body_pages=body_pages, sections=set(secs))


CORE = r"ICDE|PVLDB|VLDB|VLDBJ|SIGMOD|PODS|TODS|PACMMOD"
VENUE_OF_BIB = [(r"data engineering|\bicde\b", "ICDE"), (r"vldb endowment|vldb endow\b|\bpvldb\b", "PVLDB"), (r"vldb journal", "VLDBJ"),
                (r"management of data|acm manag\. data|\bsigmod\b", "SIGMOD"), (r"principles of database systems|\bpods\b", "PODS"),
                (r"transactions on database systems", "TODS"), (r"\bcidr\b|innovative data systems", "CIDR"),
                (r"statistical database|\bssdbm\b", "SSDBM"), (r"\bedbt\b|extending database", "EDBT")]


def bib_venues(root):
    """(venue, two-digit year) of every entry in the .bib files next to the paper."""
    out = set()
    for f in glob.glob(os.path.join(root, '*.bib')):
        for e in re.split(r'\n@', open(f, errors='ignore').read()):
            v = ' '.join(re.findall(r'(?:journal|booktitle)\s*=\s*[{"](.*?)[}"]\s*,', e, re.S | re.I)).lower()
            y = re.search(r'year\s*=\s*[{"]?(\d{4})', e, re.I)
            for pat, key in VENUE_OF_BIB:
                if y and re.search(pat, v):
                    out.add((key, y.group(1)[2:]))
    return out


def relevance_checks(rel, info, root, chk):
    flat = rel.replace('\r\n', '\n')
    chk(len(flat.replace('\n', '\r\n')) <= RELEVANCE_MAX,
        f'relevance text {len(flat)} characters ({len(flat.replace(chr(10), chr(13) + chr(10)))} if CMT counts a line break as two; CFP: 1000)')
    chk(all(re.search(p, rel) for p in [r'\(a\)', r'\(b\)', r'\(c\)']), 'relevance text answers (a), (b), (c)')
    try:
        sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'icde-subject-areas', 'scripts'))
        from suggest_areas import AREAS
        topics = [n.split(',')[0].lower() for n, _, _ in AREAS]
        chk(any(t in rel.lower() for t in topics), 'relevance text names at least one ICDE topic area (form: "must align with at least one of the ICDE 2027 topic areas")')
    except ImportError:
        pass
    b = re.search(r'\(b\)(.*?)(\(c\)|$)', rel, re.S)
    refs = re.findall(r'Sec(?:tion|s?\.)\s*([IVX]+)', b.group(1) if b else '')
    chk(bool(refs) and set(refs) <= info['sections'],
        f"(b) refers to sections of the PDF ({', '.join(refs) or 'none'}; PDF has {', '.join(sorted(info['sections'])) or '?'})")
    c = re.search(r'\(c\)(.*)', rel, re.S)
    c = c.group(1) if c else ''
    cites = re.findall(r"\b(" + CORE + r"|CIDR|SSDBM|EDBT|arXiv|NeurIPS|ACL|KDD|AAAI|ICML)\s*'?\s*(\d{2}|\d{4})\b", c)
    noncore = sorted({v for v, _ in cites if not re.fullmatch(CORE, v)})
    chk(bool(cites) and not noncore, "(c) cites ICDE/VLDB/SIGMOD work as NAME, VENUE'YY" + (f"; non-core venues: {', '.join(noncore)}" if noncore else ''))
    have = bib_venues(root)
    miss = [f"{v}'{y[-2:]}" for v, y in cites if (v.replace('VLDB', 'PVLDB') if v == 'VLDB' else v, y[-2:]) not in have]
    chk(not miss, '(c) every cited venue/year has an entry in the bibliography' + (f": missing {', '.join(miss)}" if miss else ''))
    chk(bool(re.search(r'extend|build|generali|differ|from .* to', c)), '(c) says how the paper extends the cited work, not only that it exists')


def authors_from_tex(tex):
    blk = re.search(r'\\author\{(.*?)\\maketitle', tex, re.S)
    if not blk:
        return []
    names = re.findall(r'\\IEEEauthorblockN\{(.*?)\}\s*\n', blk.group(1), re.S)
    names = re.split(r',| and ', re.sub(r'\\IEEEauthorrefmark\{\d\}|\\thanks\{.*?\}', '', ' '.join(names)))
    mails = re.findall(r'[\w.+-]+@[\w.-]+', blk.group(1))
    out = []
    for i, n in enumerate([x.strip() for x in names if x.strip()]):
        parts = n.split()
        out.append({'first': ' '.join(parts[:-1]), 'last': parts[-1], 'email': mails[i] if i < len(mails) else '?',
                    'organization': '(fill in)', 'country': '(fill in)', 'orcid': '(fill in)', 'primary_contact': i == 0})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('paper'); ap.add_argument('--pdf', required=True); ap.add_argument('--artifact-url', required=True)
    ap.add_argument('--authors'); ap.add_argument('--relevance'); ap.add_argument('--withheld', default='')
    ap.add_argument('--eab', action='store_true'); ap.add_argument('--out', default='cmt_form.md')
    ap.add_argument('--areas', help='final choice, verbatim CMT names: "Primary; Secondary 1; Secondary 2"')
    a = ap.parse_args()
    tex = load_tex(a.paper); M = macros(tex)
    title = plain(re.search(r'\\title\{(.*?)\}\s*\n', tex, re.S).group(1), M)
    abstract = plain(re.search(r'\\begin\{abstract\}(.*?)\\end\{abstract\}', tex, re.S).group(1), M)
    info = pdf_info(a.pdf)
    authors = json.load(open(a.authors)) if a.authors else authors_from_tex(tex)
    rel = open(a.relevance).read().strip() if a.relevance else ''
    checks = []
    def chk(ok, what):
        checks.append(('OK  ' if ok else 'FAIL') + '  ' + what)
    chk(norm(title) in norm(info['first']), 'title identical to the PDF')
    same = norm(abstract) in norm(info['first'].replace('ϵ', 'ε'))
    diff = ''
    if not same:
        import difflib
        pw = re.sub(r'-\n', '', info['first']).replace('ϵ', 'ε').split()
        aw = abstract.split()
        sm = difflib.SequenceMatcher(None, [norm(w) for w in pw], [norm(w) for w in aw])
        best = max(sm.get_matching_blocks(), key=lambda b: b.size)
        lo = max(0, best.a - best.b)
        sm = difflib.SequenceMatcher(None, [norm(w) for w in pw[lo:lo + len(aw) + 20]], [norm(w) for w in aw])
        diff = '; '.join(f"PDF '{' '.join(pw[lo + i1:lo + i2])}' vs form '{' '.join(aw[j1:j2])}'"
                         for t, i1, i2, j1, j2 in sm.get_opcodes() if t != 'equal')[:400]
    chk(same, 'abstract identical to page 1 of the PDF (word for word, punctuation ignored)' + (f': {diff}' if diff else ''))
    chk(len(abstract) <= CMT_ABSTRACT_MAX, f'abstract {len(abstract)} characters (CMT limit {CMT_ABSTRACT_MAX})')
    chk(info['mb'] <= FILE_MAX_MB, f"PDF {info['mb']:.2f} MB (limit {FILE_MAX_MB} MB)")
    chk(info['size'] == (612, 792), f"page size {info['size']} pt (US Letter is 612 x 792)")
    chk(not info['type3'], 'no Type 3 fonts' + (f": {info['type3'][:3]}" if info['type3'] else ''))
    chk(info['body_pages'] <= 12, f"body on {info['body_pages']} pages (limit 12; references and AI declaration excluded)")
    chk(bool(re.search(r'AI-?\s*Generated', tex, re.I)), 'AI-generated content declaration present in the paper')
    if rel:
        relevance_checks(rel, info, a.paper, chk)
    chk(bool(re.match(r'https?://', a.artifact_url)), 'artifact URL given')
    u, err = '', ''
    for _ in range(3):  # a slow network once timed out a reachable repository: retry before failing
        try:
            u = subprocess.run(['curl', '-s', '-L', '-m', '45', '-o', '/dev/null', '-w', '%{http_code}', a.artifact_url],
                               capture_output=True, text=True, timeout=60).stdout
            if u == '200':
                break
        except Exception as e:
            err = str(e)
    chk(u == '200', f'artifact URL reachable without login (HTTP {u or err})')
    areas = ''
    sa = os.path.join(os.path.dirname(__file__), '..', '..', 'icde-subject-areas', 'scripts', 'suggest_areas.py')
    if os.path.exists(sa):
        if a.areas:
            r = subprocess.run([sys.executable, sa, '--choose', a.areas], capture_output=True, text=True)
            areas = r.stdout + r.stderr
            chk(r.returncode == 0, 'subject areas are verbatim CMT names, one Primary, no area twice')
        else:
            areas = subprocess.run([sys.executable, sa, a.paper] + (['--eab'] if a.eab else []), capture_output=True, text=True).stdout
    avail = a.artifact_url + ('\n\n' + a.withheld if a.withheld else '')
    L = ['# CMT submission form (ICDE research track) — reviewer-facing text, English', '',
         '## Title', title, '', f'## Abstract ({len(abstract)} characters; paste as plain text)', abstract, '',
         '## Authors (CMT order; tick Primary Contact for the first)', '| Primary | Email | First Name | Last Name | Organization | Country/Region | ORCID |', '|---|---|---|---|---|---|---|']
    for x in authors:
        L.append(f"| {'x' if x.get('primary_contact') else ''} | {x['email']} | {x['first']} | {x['last']} | {x['organization']} | {x['country']} | {x.get('orcid', '')} |")
    L += ['', '## Subject areas' + (' (final choice; tick exactly these boxes)' if a.areas else ' (scorer ranking; apply the rules of icde-subject-areas, then rerun with --areas)'),
          '```', areas.strip() or '(run icde-subject-areas)', '```', '',
          f"## Files\nUpload exactly one PDF: `{os.path.basename(a.pdf)}` ({info['mb']:.2f} MB, {info['pages']} pages).", '',
          '## Toronto Paper Matching System\nTick "I agree".', '', '## Additional questions']
    for n, t, kind in QUESTIONS:
        if kind == 'agree':
            L.append(f'{n}. {t}: tick "I agree".')
        elif n == 3:
            L.append(f'{n}. {t} (text box; {len(rel)} characters, CFP limit 1,000; paste exactly):\n\n' + (rel or '(write: Topics: <areas>. (a) challenge, (b) contributions with section numbers, (c) ICDE/VLDB/SIGMOD work it builds on and how it extends it)') + '\n')
        else:
            L.append(f'{n}. {t} (text box: artifact URL, and the reason for anything withheld):\n\n' + avail + '\n')
    L += ['', '## Checks', ''] + ['- ' + c for c in checks]
    open(a.out, 'w').write('\n'.join(L) + '\n')
    print('\n'.join(checks)); print('wrote', a.out)
    sys.exit(1 if any(c.startswith('FAIL') for c in checks) else 0)


if __name__ == '__main__':
    main()
