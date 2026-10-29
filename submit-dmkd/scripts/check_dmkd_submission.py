#!/usr/bin/env python3
"""Pre-submission checks for a Data Mining and Knowledge Discovery (Springer, sn-jnl) LaTeX manuscript.

Usage:
  python3 check_dmkd_submission.py FOLDER [--main main.tex] [--forbid REGEX]
                                   [--abstract-min 150] [--abstract-max 250]

Prints ERROR / WARN / OK lines and exits 1 if any ERROR is found. Reads files only.
"""
import argparse
import pathlib
import re
import sys

DECLARATIONS = ["Funding", "Competing interests", "Ethics approval", "Consent for publication",
                "Data availability", "Materials availability", "Code availability", "Author contribution"]
problems = {"ERROR": 0, "WARN": 0}


def report(level, msg):
    if level in problems:
        problems[level] += 1
    print(f"{level:5s} {msg}")


def strip_comments(s):
    return re.sub(r"(?<!\\)%.*", "", s)


def braced(s, start):
    """Return the content of the brace group that opens at s[start] == '{'."""
    depth = 0
    for i in range(start, len(s)):
        if s[i] == "{":
            depth += 1
        elif s[i] == "}":
            depth -= 1
            if depth == 0:
                return s[start + 1:i]
    return None


def macro_arg(tex, name):
    m = re.search(r"\\" + name + r"\s*(\[[^\]]*\])?\s*\{", tex)
    return braced(tex, m.end() - 1) if m else None


def words(s):
    s = re.sub(r"\\[a-zA-Z]+\*?(\[[^\]]*\])?", " ", s)
    s = re.sub(r"[{}$~]", " ", s)
    return [w for w in s.split() if re.search(r"[A-Za-z0-9]", w)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder")
    ap.add_argument("--main", default="main.tex")
    ap.add_argument("--forbid", default=None, help="regex that must not occur, e.g. the previous journal name")
    ap.add_argument("--abstract-min", type=int, default=150)
    ap.add_argument("--abstract-max", type=int, default=250)
    a = ap.parse_args()

    folder = pathlib.Path(a.folder)
    tex_path = folder / a.main
    if not tex_path.exists():
        report("ERROR", f"main file not found: {tex_path}")
        sys.exit(1)
    raw = tex_path.read_text(errors="ignore")
    tex = strip_comments(raw)

    m = re.search(r"\\documentclass(\[[^\]]*\])?\{([^}]*)\}", tex)
    opts = (m.group(1) or "").strip("[]") if m else ""
    if not m or m.group(2) != "sn-jnl":
        report("ERROR", "documentclass is not sn-jnl")
    else:
        o = [x.strip() for x in opts.split(",")]
        report("OK" if "pdflatex" in o else "ERROR", f"sn-jnl options [{opts}] {'include' if 'pdflatex' in o else 'lack'} pdflatex")
        if "Numbered" in o:
            report("ERROR", "option Numbered gives numbered citations; DMKD uses author-year")
        if "sn-basic" not in o:
            report("WARN", "reference style option is not sn-basic (Springer basic author-year, as in published DMKD papers)")
        else:
            report("OK", "sn-basic author-year reference style")

    for inc in re.findall(r"\\(input|include)\{([^}]*)\}", tex):
        report("ERROR", f"\\{inc[0]}{{{inc[1]}}}: Snapp needs one flat .tex file")

    title = macro_arg(tex, "title")
    report("OK" if title else "ERROR", f"title: {title.strip()[:90] if title else 'missing'}")
    authors = re.findall(r"\\author\*?(\[[^\]]*\])?\{", tex)
    report("OK" if authors else "ERROR", f"{len(authors)} \\author entries")
    if not re.search(r"\\author\*", tex):
        report("ERROR", "no corresponding author marked with \\author*")
    if not re.search(r"\\email\{", tex):
        report("ERROR", "no \\email")
    if not re.search(r"\\affil\*?(\[[^\]]*\])?\{", tex):
        report("ERROR", "no \\affil")
    if not re.search(r"\\country\{", tex):
        report("WARN", "affiliations lack \\country{}")

    ab = macro_arg(tex, "abstract")
    if ab is None:
        report("ERROR", "no \\abstract{...}")
    else:
        n = len(words(ab))
        if re.search(r"\\cite", ab):
            report("ERROR", "abstract contains a citation")
        level = "OK" if a.abstract_min <= n <= a.abstract_max else "ERROR"
        report(level, f"abstract has {n} words (DMKD: {a.abstract_min}-{a.abstract_max})")

    kw = macro_arg(tex, "keywords")
    if kw is None:
        report("ERROR", "no \\keywords{...}")
    else:
        k = [x.strip() for x in kw.split(",") if x.strip()]
        report("OK" if 4 <= len(k) <= 6 else "ERROR", f"{len(k)} keywords (DMKD: 4-6): {'; '.join(k)}")

    if "\\backmatter" not in tex:
        report("WARN", "no \\backmatter before the declarations")
    sd = re.search(r"\\section\*\{(Statements and Declarations|Declarations)\}", tex)
    if not sd:
        report("ERROR", "no 'Statements and Declarations' section (submission is returned as incomplete)")
    else:
        body = tex[sd.end():]
        for h in DECLARATIONS:
            found = re.search(re.escape(h), body[:20000], re.I)
            report("OK" if found else "ERROR", f"declaration '{h}' {'found' if found else 'missing'}")
        bib_pos = min([p for p in (tex.find("\\begin{thebibliography}"), tex.find("\\bibliography{")) if p >= 0] or [len(tex)])
        if sd.start() > bib_pos:
            report("ERROR", "Statements and Declarations must come before the reference list")
    da = re.search(r"\\(?:bmhead|section\*|subsection\*|paragraph)\{Data availability[^}]*\}(.{0,4000})", tex, re.S | re.I)
    if da and not re.search(r"doi\.org|zenodo|figshare|dryad|osf\.io|github\.com|softwareheritage", da.group(1), re.I):
        report("WARN", "data availability names no repository or persistent identifier")
    if not re.search(r"\b(LLM|large language model|ChatGPT|Codex|Claude|GPT|generative AI|AI-assisted|AI assist)", tex, re.I):
        report("WARN", "no LLM/AI-use statement found; DMKD asks for one in the Methods section if any LLM was used")
    if re.search(r"Declaration of generative AI and AI-assisted technologies", tex):
        report("ERROR", "Elsevier AI heading left over; move the disclosure into the Methods section")
    if re.search(r"\\begin\{(keyword|frontmatter)\}|\\journal\{|\\sep\b|highlights", tex):
        report("ERROR", "elsarticle leftovers (frontmatter/keyword/\\journal/\\sep/highlights)")

    plain_cites = re.findall(r"\\cite\{", tex)
    if plain_cites:
        report("WARN", f"{len(plain_cites)} bare \\cite{{}}: use \\citep{{}} (parenthetical) or \\citet{{}} (textual) for author-year")
    keys = set()
    for c in re.findall(r"\\cite[pt]?\*?(?:\[[^\]]*\])*\{([^}]*)\}", tex):
        keys.update(x.strip() for x in c.split(","))
    items = re.findall(r"\\bibitem(\[[^\]]*\])?\{([^}]*)\}", tex)
    if items:
        defined = {k for _, k in items}
        if any(not opt for opt, _ in items):
            report("ERROR", "\\bibitem without [Author(Year)] label: natbib author-year needs \\bibitem[{Name(Year)}]{key}")
        miss = sorted(keys - defined)
        unused = sorted(defined - keys)
        report("ERROR" if miss else "OK", f"{len(keys)} cited keys; undefined: {miss[:10]}")
        if unused:
            report("WARN", f"bibitems never cited: {unused[:10]}")
        labels = [re.sub(r"[{}\\~]", "", o) for o, _ in items]
        if labels != sorted(labels, key=str.lower):
            report("WARN", "reference list does not look alphabetical by its labels")
        nodoi = [k for (o, k), body in zip(items, re.split(r"\\bibitem", tex)[1:]) if "doi" not in body[:800].lower()]
        if nodoi:
            report("WARN", f"{len(nodoi)} references without a DOI link: {nodoi[:8]}")
    elif re.search(r"\\bibliography\{([^}]*)\}", tex):
        bib = re.search(r"\\bibliography\{([^}]*)\}", tex).group(1)
        for b in bib.split(","):
            p = folder / (b.strip() + ".bib")
            report("OK" if p.exists() else "ERROR", f"bib file {p.name} {'present' if p.exists() else 'missing'}")
        bst = folder / "sn-basic.bst"
        report("OK" if bst.exists() else "WARN", "sn-basic.bst next to main.tex" if bst.exists() else "sn-basic.bst not in folder")
    else:
        report("ERROR", "no bibliography")

    if not (folder / "sn-jnl.cls").exists():
        report("ERROR", "sn-jnl.cls missing from the folder")
    for g in re.findall(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]*)\}", tex):
        if "/" in g:
            report("ERROR", f"figure path uses a subfolder: {g}")
        cand = [folder / g] + [folder / (g + e) for e in (".pdf", ".eps", ".png", ".jpg")]
        report("OK" if any(c.exists() for c in cand) else "ERROR", f"figure {g} {'present' if any(c.exists() for c in cand) else 'missing'}")
    labels = re.findall(r"\\label\{([^}]*)\}", tex)
    refs = set(re.findall(r"\\(?:ref|autoref|cref|Cref)\{([^}]*)\}", tex))
    dup = sorted({l for l in labels if labels.count(l) > 1})
    if dup:
        report("ERROR", f"duplicate labels: {dup}")
    miss = sorted(refs - set(labels))
    report("ERROR" if miss else "OK", f"{len(refs)} referenced labels; undefined: {miss}")
    if re.search(r"\\subsubsubsection", tex):
        report("ERROR", "more than three heading levels")
    if a.forbid:
        for hit in sorted(set(re.findall(a.forbid, raw))):
            report("ERROR", f"forbidden string present: {hit}")
    sub = [p for p in folder.iterdir() if p.is_dir() and not p.name.startswith(".")]
    if sub:
        report("WARN", f"subfolders present (keep the upload flat): {[p.name for p in sub]}")

    print(f"\n{problems['ERROR']} errors, {problems['WARN']} warnings")
    sys.exit(1 if problems["ERROR"] else 0)


if __name__ == "__main__":
    main()
