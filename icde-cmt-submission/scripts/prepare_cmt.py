#!/usr/bin/env python3
"""Prepare every field of the ICDE CMT "Create New Submission" form from a paper and check it against the PDF.

usage: prepare_cmt.py <paper_dir> --pdf <submitted.pdf> --artifact-url <url> [--authors authors.json]
                      [--relevance relevance.txt] [--withheld "reason ..."] [--eab] [--out cmt_form.md]

Writes one Markdown file with the reviewer-facing English text for each CMT field (title, abstract, authors,
subject areas, file, TPMS, the ten additional questions with the two text boxes) and a check list:
- the abstract is rebuilt from the LaTeX source (\\newcommand macros expanded, so numbers.tex values appear) and
  compared word for word with the abstract printed on page 1 of the PDF; CMT limit 2,000 characters;
- the title is compared with the PDF; the PDF must be <= 20 MB, US Letter, fonts embedded, body <= 12 pages;
- the relevance text must stay within 1,000 characters (CFP) and answer (a), (b), (c);
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
    body_end = next((i for i, t in enumerate(text) if re.search(r'^\s*(AI-?\s*G\s*ENERATED|R\s*EFERENCES)', t, re.M | re.I)), len(text))
    heading_first = body_end < len(text) and len(re.split(r'^\s*(AI-?\s*G\s*ENERATED|R\s*EFERENCES)', text[body_end], flags=re.M | re.I)[0].strip()) < 40
    body_pages = body_end if heading_first else body_end + 1
    return dict(pages=len(d), size=(round(d[0].rect.width), round(d[0].rect.height)), mb=os.path.getsize(path) / 1e6,
                type3=[f[0] for f in fonts if f[1] == 'Type3'], first=first, body_pages=body_pages)


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
    chk(norm(abstract) in norm(info['first']), 'abstract identical to page 1 of the PDF (word for word, punctuation ignored)')
    chk(len(abstract) <= CMT_ABSTRACT_MAX, f'abstract {len(abstract)} characters (CMT limit {CMT_ABSTRACT_MAX})')
    chk(info['mb'] <= FILE_MAX_MB, f"PDF {info['mb']:.2f} MB (limit {FILE_MAX_MB} MB)")
    chk(info['size'] == (612, 792), f"page size {info['size']} pt (US Letter is 612 x 792)")
    chk(not info['type3'], 'no Type 3 fonts' + (f": {info['type3'][:3]}" if info['type3'] else ''))
    chk(info['body_pages'] <= 12, f"body on {info['body_pages']} pages (limit 12; references and AI declaration excluded)")
    chk(bool(re.search(r'AI-?\s*Generated', tex, re.I)), 'AI-generated content declaration present in the paper')
    if rel:
        chk(len(rel) <= RELEVANCE_MAX, f'relevance text {len(rel)} characters (CFP: 1000)')
        chk(all(re.search(p, rel) for p in [r'\(a\)', r'\(b\)', r'\(c\)']), 'relevance text answers (a), (b), (c)')
    chk(bool(re.match(r'https?://', a.artifact_url)), 'artifact URL given')
    try:
        u = subprocess.run(['curl', '-s', '-o', '/dev/null', '-w', '%{http_code}', a.artifact_url], capture_output=True, text=True, timeout=30).stdout
        chk(u == '200', f'artifact URL reachable without login (HTTP {u})')
    except Exception as e:
        chk(False, f'artifact URL check failed: {e}')
    areas = ''
    sa = os.path.join(os.path.dirname(__file__), '..', '..', 'icde-subject-areas', 'scripts', 'suggest_areas.py')
    if os.path.exists(sa):
        areas = subprocess.run([sys.executable, sa, a.paper] + (['--eab'] if a.eab else []), capture_output=True, text=True).stdout
    avail = a.artifact_url + ('\n\n' + a.withheld if a.withheld else '')
    L = ['# CMT submission form (ICDE research track) — reviewer-facing text, English', '',
         '## Title', title, '', f'## Abstract ({len(abstract)} characters; paste as plain text)', abstract, '',
         '## Authors (CMT order; tick Primary Contact for the first)', '| Primary | Email | First Name | Last Name | Organization | Country/Region | ORCID |', '|---|---|---|---|---|---|---|']
    for x in authors:
        L.append(f"| {'x' if x.get('primary_contact') else ''} | {x['email']} | {x['first']} | {x['last']} | {x['organization']} | {x['country']} | {x.get('orcid', '')} |")
    L += ['', '## Subject areas (see icde-subject-areas; apply its rules before ticking)', '```', areas.strip() or '(run icde-subject-areas)', '```', '',
          f"## Files\nUpload exactly one PDF: `{os.path.basename(a.pdf)}` ({info['mb']:.2f} MB, {info['pages']} pages).", '',
          '## Toronto Paper Matching System\nTick "I agree".', '', '## Additional questions']
    for n, t, kind in QUESTIONS:
        if kind == 'agree':
            L.append(f'{n}. {t}: tick "I agree".')
        elif n == 3:
            L.append(f'{n}. {t} (text box; keep within 1,000 characters):\n\n' + (rel or '(write (a) challenge, (b) contributions with section numbers, (c) ICDE/VLDB/SIGMOD work it builds on)') + '\n')
        else:
            L.append(f'{n}. {t} (text box: artifact URL, and the reason for anything withheld):\n\n' + avail + '\n')
    L += ['', '## Checks', ''] + ['- ' + c for c in checks]
    open(a.out, 'w').write('\n'.join(L) + '\n')
    print('\n'.join(checks)); print('wrote', a.out)
    sys.exit(1 if any(c.startswith('FAIL') for c in checks) else 0)


if __name__ == '__main__':
    main()
