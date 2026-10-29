#!/usr/bin/env python3
"""Pre-submission checks for an Expert Systems with Applications (ESWA, Elsevier) LaTeX manuscript.

ESWA uses double-anonymized review and APA (author-year) references, so this checker
looks at two files: the anonymized manuscript and the separate title page.

Usage:
  python3 check_eswa_submission.py FOLDER --main manuscript.tex [--bib references.bib]
        [--title-page title_page.txt|.tex|.md] [--highlights highlights.txt]
        [--identity 'Surname1|Surname2|univ-domain|Company|github-user|zenodo\\.1234567']
        [--forbid 'Old Journal Name|OLDCODE'] [--abstract-limit 250] [--max-keywords 7]

Prints ERROR / WARN / OK lines and exits 1 if any ERROR is found. It only reads files.
"""
import argparse
import pathlib
import re
import sys

AI_HEADING = ("Declaration of generative AI and AI-assisted technologies "
              "in the manuscript preparation process")
JOURNAL = "Expert Systems with Applications"
# Files that are seen by the editor only and are not anonymized (skipped by identity/forbid scans).
NON_ANON = re.compile(r"title|cover|declaration|response|portal|readme", re.I)

problems = {"ERROR": 0, "WARN": 0}


def report(level, msg):
    if level in problems:
        problems[level] += 1
    print(f"{level:5s} {msg}")


def strip_comments(s):
    return re.sub(r"(?<!\\)%.*", "", s)


def words(s):
    s = re.sub(r"\\[a-zA-Z@]+\*?(\[[^\]]*\])?", " ", s)
    s = re.sub(r"[{}$~]", " ", s)
    return [w for w in s.split() if re.search(r"[A-Za-z0-9]", w)]


def read_inputs(folder, tex):
    """Inline \\input{...} files so that tables and numbers are scanned too."""
    def repl(m):
        p = folder / m.group(1)
        if p.suffix != ".tex":
            p = p.with_suffix(".tex")
        return strip_comments(p.read_text(errors="ignore")) if p.exists() else ""
    return re.sub(r"\\input\{([^}]*)\}", repl, tex)


def check_scope(tex):
    if re.search(r"\b(military|defen[cs]e system|weapon|battlefield)\b", tex, re.I):
        report("WARN", "military/defence wording found: ESWA no longer considers military/defence applications")
    if re.search(r"(inspired|metaphor)[^.]{0,60}(algorithm|optimi[sz]er)", tex, re.I):
        report("WARN", "metaphor-inspired algorithm wording: the guide asks for formal, mathematically grounded "
                       "differences from established methods and standard optimisation terminology")
    intro = re.search(r"\\section\{Introduction\}(.*?)\\section", tex, re.S)
    if intro and not re.search(r"expert|intelligent system|decision support|human-in-the-loop|deploy|practitioner|industr",
                               intro.group(1), re.I):
        report("WARN", "Introduction never names the expert/intelligent-system application or deployment setting "
                       "(ESWA aims: design, development, testing, implementation or management of such systems)")
    if not re.search(r"practical|guideline|implication|deploy", tex, re.I):
        report("WARN", "no practical guidelines/implications text: ESWA asks for practical guidelines for building "
                       "and managing intelligent systems")


def check_citations(tex, folder, bib_arg):
    m = re.search(r"\\documentclass(\[[^\]]*\])?\{elsarticle\}", tex)
    opts = (m.group(1) or "") if m else ""
    authoryear = "authoryear" in opts or re.search(r"\\biboptions\{[^}]*authoryear", tex) \
        or re.search(r"\\usepackage\[[^\]]*authoryear[^\]]*\]\{natbib\}", tex)
    report("OK" if authoryear else "ERROR",
           "natbib author-year citations " + ("enabled" if authoryear else "missing: ESWA requires APA (author-year) "
                                              "citations; use \\documentclass[...,authoryear]{elsarticle} or \\biboptions{authoryear}"))
    st = re.search(r"\\bibliographystyle\{([^}]*)\}", tex)
    if st:
        s = st.group(1)
        if s in ("model5-names", "elsarticle-harv", "apalike", "apa"):
            report("OK", f"bibliography style {s} (author-year, alphabetical)")
        else:
            report("ERROR" if "num" in s else "WARN", f"bibliography style {s}: use model5-names (Elsevier APA model) "
                                                      "or elsarticle-harv")
    elif "thebibliography" not in tex:
        report("ERROR", "no bibliography")
    bare = re.findall(r"[^\\]\\cite\{", tex)
    if bare:
        report("WARN", f"{len(bare)} bare \\cite{{...}}: in author-year mode write \\citet (narrative) or "
                       "\\citep (parenthetical) explicitly")
    if re.search(r"et al\.(~|\s)\\cite[p]?\{", tex):
        report("ERROR", "'X et al.~\\cite{..}' is numeric-style; write \\citet{key} so the year appears once")
    if re.search(r"\\cite[pt]?\{[^}]*\}\s*\\cite", tex):
        report("WARN", "consecutive \\cite commands: merge into one \\citep{a,b}")

    cited = set(k.strip() for grp in re.findall(r"\\cite(?:t|p|author|year|alp|alt)?\*?(?:\[[^\]]*\]){0,2}\{([^}]*)\}", tex)
                for k in grp.split(",") if k.strip())
    bibname = bib_arg or (re.search(r"\\bibliography\{([^}]*)\}", tex).group(1).split(",")[0] + ".bib"
                          if re.search(r"\\bibliography\{([^}]*)\}", tex) else None)
    if not bibname:
        return cited
    bp = folder / bibname
    if not bp.exists():
        report("ERROR", f"bib file not found: {bp}")
        return cited
    bib = bp.read_text(errors="ignore")
    entries = dict((k.strip(), body) for k, body in
                   re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,(.*?)\n\}", bib, re.S))
    for k in sorted(cited - set(entries)):
        report("ERROR", f"cited but not in bib: {k}")
    unused = sorted(set(entries) - cited)
    if unused:
        report("WARN", f"{len(unused)} bib entries never cited (harmless with BibTeX, but remove before archiving): "
                       + ", ".join(unused[:8]))
    nodoi = [k for k in cited & set(entries) if not re.search(r"\bdoi\s*=|eprint\s*=|\burl\s*=", entries[k], re.I)]
    if nodoi:
        report("WARN", f"{len(nodoi)} cited entries without DOI/URL/eprint (guide asks for DOIs where available): "
                       + ", ".join(sorted(nodoi)[:10]))
    arx = [k for k in cited & set(entries)
           if re.search(r"(howpublished|journal|note)\s*=\s*\{[^}]*(arxiv|preprint)", entries[k], re.I)
           or (re.search(r"arxiv", entries[k], re.I) and not re.search(r"booktitle|journal", entries[k], re.I))]
    if arx:
        report("WARN", f"{len(arx)} cited arXiv/preprint entries: mark them 'preprint', give the preprint DOI "
                       "(10.48550/arXiv.<id>) and replace with the formal version where one exists: " + ", ".join(sorted(arx)))
    n = len(cited)
    report("OK" if n >= 40 else "WARN", f"{n} distinct references cited "
           + ("" if n >= 40 else "(published ESWA research articles usually cite far more; check related-work coverage)"))
    return cited


def check_anonymity(folder, tex_raw, tex, identity):
    for cmd in ("author", "ead", "affiliation", "address", "cortext", "corref", "fnref"):
        if re.search(r"\\" + cmd + r"\b", tex):
            report("ERROR", f"\\{cmd} in the anonymized manuscript: author details belong on the separate title page")
    if re.search(r"\\section\*?\{\s*Acknowledg", tex, re.I):
        report("ERROR", "Acknowledgements section in the manuscript: ESWA wants acknowledgements on the title page only")
    if re.search(r"\\section\*?\{[^}]*CRediT", tex):
        report("ERROR", "CRediT statement names authors: move it to the title page / submission system")
    if re.search(r"\\section\*?\{[^}]*competing interest", tex, re.I):
        report("WARN", "competing-interest section in the anonymized manuscript: keep it only if it names nobody; "
                       "otherwise use the title page and the Declarations-tool file")
    if re.search(r"github\.com/|gitlab\.com/|zenodo\.org/record|10\.5281/zenodo|huggingface\.co/[^ }]*/", tex, re.I):
        for u in sorted(set(re.findall(r"(?:github|gitlab)\.com/[\w.-]+|10\.5281/zenodo\.\d+|zenodo\.org/records?/\d+", tex, re.I))):
            report("WARN", f"repository link in manuscript may identify the authors: {u} (use an anonymized mirror "
                           "or 'link given on the title page')")
    if re.search(r"\b(our|my) (previous|prior|earlier) (work|paper|study)\b", tex, re.I):
        report("WARN", "'our previous work' wording de-anonymizes self-citations: cite in the third person")
    if re.search(r"pdfauthor|pdfinfo\{[^}]*Author", tex_raw):
        report("ERROR", "PDF metadata sets an author (hyperref pdfauthor / \\pdfinfo)")
    if identity:
        rx = re.compile(identity, re.I)
        for f in sorted(folder.rglob("*")):
            if f.is_file() and f.suffix in {".tex", ".bib", ".txt", ".md", ".bst", ".cls"} and not NON_ANON.search(f.name):
                if f.suffix in {".bst", ".cls"}:
                    continue
                for i, line in enumerate(f.read_text(errors="ignore").splitlines(), 1):
                    if line.lstrip().startswith("%"):
                        if rx.search(line):
                            report("WARN", f"identity string in a comment {f.name}:{i} (comments ship in the source zip)")
                        continue
                    if rx.search(line):
                        report("ERROR", f"identity string in {f.name}:{i}: {line.strip()[:100]}")
            if f.is_file() and rx.search(f.name) and not NON_ANON.search(f.name):
                report("ERROR", f"identity string in file name: {f.name}")


def check_title_page(path, identity):
    if not path.exists():
        report("ERROR", f"title page not found: {path}")
        return
    t = path.read_text(errors="ignore") if path.suffix in {".tex", ".txt", ".md"} else ""
    if not t:
        report("WARN", f"title page {path.name} not text; check it by eye")
        return
    for label, pat in [("e-mail address", r"[\w.+-]+@[\w-]+\.[\w.]+"),
                       ("corresponding author", r"[Cc]orrespond"),
                       ("country in an affiliation", r"China|USA|United|Germany|France|Japan|Korea|India|Italy|Spain|Canada|Australia"),
                       ("acknowledgements", r"[Aa]cknowledg"),
                       ("competing interests", r"[Cc]ompeting interest|[Dd]eclaration of interest")]:
        report("OK" if re.search(pat, t) else "WARN", f"title page: {label} {'found' if re.search(pat, t) else 'missing'}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder")
    ap.add_argument("--main", default="manuscript.tex")
    ap.add_argument("--bib", default=None)
    ap.add_argument("--title-page", default=None)
    ap.add_argument("--highlights", default=None)
    ap.add_argument("--identity", default=None, help="regex of author names, e-mails, institutions, user names, DOIs")
    ap.add_argument("--forbid", default=None, help="regex of earlier journal names or internal codes")
    ap.add_argument("--abstract-limit", type=int, default=250)
    ap.add_argument("--max-keywords", type=int, default=7)
    a = ap.parse_args()

    folder = pathlib.Path(a.folder)
    tp = folder / a.main
    if not tp.exists():
        report("ERROR", f"main file not found: {tp}")
        sys.exit(1)
    raw = tp.read_text(errors="ignore")
    tex = read_inputs(folder, strip_comments(raw))

    m = re.search(r"\\documentclass(\[[^\]]*\])?\{([^}]*)\}", tex)
    report("OK" if m and m.group(2) == "elsarticle" else "WARN",
           f"document class {m.group(2) if m else '?'} (Elsevier elsarticle template encouraged)")
    j = re.search(r"\\journal\{([^}]*)\}", tex)
    report("OK" if j and j.group(1).strip() == JOURNAL else "ERROR",
           f"\\journal{{{j.group(1) if j else ''}}} (expected '{JOURNAL}')")

    tm = re.search(r"\\title\{(.*?)\}\s*\n", tex, re.S)
    if tm:
        title = " ".join(tm.group(1).split())
        n = len(words(title))
        report("OK" if n <= 20 else "WARN", f"title has {n} words: {title}")
        abbr = [w for w in re.findall(r"\b[A-Z]{2,}s?\b", title) if w not in {"DNA", "AI"}]
        if abbr:
            report("WARN", f"abbreviations in title {abbr}: the guide asks to avoid them unless widely understood")

    ab = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", tex, re.S)
    if not ab:
        report("ERROR", "no abstract")
    else:
        n = len(words(ab.group(1)))
        if "\\cite" in ab.group(1):
            report("ERROR", "abstract cites a reference (guide: avoid; if essential give author and year in full)")
        report("ERROR" if n > a.abstract_limit else "OK", f"abstract has {n} words (limit {a.abstract_limit})")

    kw = re.search(r"\\begin\{keyword\}(.*?)\\end\{keyword\}", tex, re.S)
    if not kw:
        report("ERROR", "no keyword environment")
    else:
        k = [" ".join(x.split()) for x in kw.group(1).split("\\sep") if x.strip()]
        report("OK" if 1 <= len(k) <= a.max_keywords else "ERROR", f"{len(k)} keywords: {'; '.join(k)}")
        for x in k:
            if re.search(r"\b(and|of)\b", x):
                report("WARN", f"keyword with 'and'/'of' (guide advises against): {x}")

    check_scope(tex)
    check_citations(tex, folder, a.bib)
    check_anonymity(folder, raw, tex, a.identity)

    report("OK" if re.search(r"[Dd]ata (and code )?availability|[Dd]ata statement", tex) else "WARN",
           "data availability statement (Option C: deposit + cite, or explain why not)")
    report("OK" if re.search(r"did not receive any specific grant|[Ff]unding:|supported by", tex) else "WARN",
           "funding statement (standard sentence if none)")
    ai = re.search(r"\\section\*\{([^}]*generative AI[^}]*)\}", tex, re.I)
    if not ai:
        report("WARN", "no generative-AI declaration (required if AI tools were used beyond grammar/spelling/reference checks)")
    else:
        head = " ".join(ai.group(1).split()).rstrip(".")
        report("OK" if head == AI_HEADING else "WARN", f"AI declaration heading: '{head}'")
        after = tex[ai.end():].split("\\bibliography{")[0].split("\\begin{thebibliography}")[0]
        if re.search(r"\\section|\\appendix", after):
            report("ERROR", "AI declaration must be the last section before the reference list")

    # Floats restricted to [t]/[h] without "p" are deferred to the end of the document
    # when they are taller than the top-float limit, and every later figure queues behind them.
    for env, spec in re.findall(r"\\begin\{(figure\*?|table\*?)\}\[([^\]]*)\]", tex):
        if "p" not in spec:
            report("WARN", f"{env}[{spec}] cannot go on a float page; use [!tbp] and check in the .aux "
                           "that every figure lands near its first mention, not after the references")

    labels = set(re.findall(r"\\label\{([^}]*)\}", tex))
    for r in sorted(set(re.findall(r"\\(?:eq)?ref\{([^}]*)\}", tex)) - labels):
        report("ERROR", f"reference to undefined label: {r}")
    for env in ("figure", "table"):
        for lab in re.findall(r"\\begin\{" + env + r"\*?\}.*?\\label\{([^}]*)\}.*?\\end\{" + env, tex, re.S):
            if not re.search(r"\\ref\{" + re.escape(lab) + r"\}", tex):
                report("WARN", f"{env} {lab} is never cited in the text (guide: cite all tables and figures)")
    if re.search(r"\\begin\{tabular\}\{[^}]*\|", tex):
        report("WARN", "vertical rules in a table (guide: avoid vertical rules and shading)")
    for g in re.findall(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]*)\}", tex):
        if not re.match(r"Figure_[A-Z]?\.?\d+", pathlib.Path(g).name):
            report("WARN", f"figure file '{g}': name separate artwork files Figure_1, Figure_2, ...")
        if not any((folder / (g + e)).exists() for e in ("", ".pdf", ".png", ".jpg", ".eps", ".tif")):
            report("ERROR", f"figure file missing: {g}")

    if a.forbid:
        rx = re.compile(a.forbid)
        for f in sorted(folder.rglob("*")):
            if f.is_file() and f.suffix in {".tex", ".bib", ".txt", ".md"} and not NON_ANON.search(f.name):
                for i, line in enumerate(f.read_text(errors="ignore").splitlines(), 1):
                    if rx.search(line):
                        report("ERROR", f"forbidden string in {f.name}:{i}: {line.strip()[:90]}")

    if a.title_page:
        check_title_page(folder / a.title_page, a.identity)
    else:
        report("WARN", "no --title-page given: ESWA needs a separate title page with author details")

    if a.highlights:
        hp = folder / a.highlights
        if "highlights" not in hp.name.lower():
            report("ERROR", "highlights file name must contain 'highlights'")
        if hp.exists():
            hl = [x.strip().lstrip("-•* ").strip() for x in hp.read_text().splitlines() if x.strip()]
            hl = [x for x in hl if x.lower() != "highlights"]
            report("OK" if 3 <= len(hl) <= 5 else "ERROR", f"{len(hl)} highlights (3-5)")
            for x in hl:
                report("ERROR" if len(x) > 85 else "OK", f"highlight {len(x)} chars: {x}")
        else:
            report("ERROR", f"highlights file not found: {hp}")
    else:
        report("WARN", "no highlights file (encouraged at submission; 3-5 bullets, <=85 characters each)")

    log = tp.with_suffix(".log")
    if log.exists():
        lg = log.read_text(errors="ignore")
        report("WARN" if "undefined" in lg else "OK", f"log: {lg.count('undefined')} 'undefined' messages")
    else:
        report("WARN", "no .log next to the main file; compile (Overleaf) and re-run, or check the PDF by eye")

    print(f"\nSummary: {problems['ERROR']} error(s), {problems['WARN']} warning(s)")
    sys.exit(1 if problems["ERROR"] else 0)


if __name__ == "__main__":
    main()
