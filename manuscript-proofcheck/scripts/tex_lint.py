#!/usr/bin/env python3
"""Source lint for LaTeX submissions: rules T01-T17 of references/defect-catalog.md.

Usage: python3 tex_lint.py PAPER_DIR [--class IEEEtran|acmart|llncs|elsarticle] [--year 2026]
Prints one line per finding: RULE  file:line  message. Exit code 1 if any ERROR-level finding.
"""
import argparse, datetime, glob, os, re, sys

ERR, WARN, INFO = "ERROR", "WARN", "INFO"
out = []


def add(level, rule, path, line, msg):
    out.append((level, rule, path, line, msg))


def strip_comments(s):
    return re.sub(r"(?<!\\)%.*", "", s)


def sqrt_args(t):
    """Arguments of every \\sqrt{...} in t (brace-matched)."""
    res = []
    for m in re.finditer(r"\\sqrt\s*(\[[^\]]*\])?\s*\{", t):
        k, depth = m.end(), 1
        while k < len(t) and depth:
            depth += {"{": 1, "}": -1}.get(t[k], 0); k += 1
        res.append(t[m.end():k - 1])
    return res


def tall(x):
    return any(z in x for z in (r"\sum", r"\prod", r"\frac", "/"))


def lines_of(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read().split("\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paper_dir")
    ap.add_argument("--class", dest="cls", default=None)
    ap.add_argument("--year", type=int, default=datetime.date.today().year)
    a = ap.parse_args()
    root = a.paper_dir
    texs = sorted(glob.glob(os.path.join(root, "**", "*.tex"), recursive=True))
    bibs = sorted(glob.glob(os.path.join(root, "**", "*.bib"), recursive=True))
    src = {p: lines_of(p) for p in texs}
    alltex = "\n".join(strip_comments("\n".join(v)) for v in src.values())
    m = re.search(r"\\documentclass(\[[^\]]*\])?\{([^}]*)\}", alltex)
    cls = a.cls or (m.group(2) if m else "")
    ieee = cls.lower() == "ieeetran"
    bst = re.search(r"\\bibliographystyle\{([^}]*)\}", alltex)
    bst = bst.group(1) if bst else ""

    # ---------------- per-line rules
    labels, refs = {}, set()
    for p, L in src.items():
        rp = os.path.relpath(p, root)
        for i, raw in enumerate(L, 1):
            s = strip_comments(raw)
            if re.search(r"\\mathbb\s*\{?\s*\d", s):
                add(ERR, "T01", rp, i, "\\mathbb with a digit prints a wrong glyph (msbm has no digits); use \\mathds{1} (dsfont) or \\mathbf{1}")
            if re.search(r"[×–—’‘“”≤≥±→←∈∑√∞≈]", s) and not re.search(r"\\usepackage(\[[^\]]*\])?\{(inputenc|newunicodechar)\}", alltex):
                add(WARN, "T02", rp, i, "Unicode math/punctuation typed directly; prefer LaTeX commands under pdfLaTeX")
            if re.search(r"\\begin\{proof\}", s) and ieee:
                add(ERR, "T07", rp, i, "amsthm proof under IEEEtran gives a foreign open QED box; use \\begin{IEEEproof}[...]")
            if re.search(r"\\qedhere", s) and ieee:
                add(WARN, "T07", rp, i, "\\qedhere is amsthm-only; use \\IEEEQEDhere inside IEEEproof")
            if re.search(r"\\todo\b|\bTODO\b|\bXXX\b|\\textcolor\{red\}|\[citation needed\]", s) and not re.search(r"\\newcommand\{\\todo\}", s):
                add(ERR, "T09", rp, i, "draft marker left in the text")
            if re.search(r"\\(vspace|vskip)\*?\s*\{?\s*-", s):
                add(ERR, "T13", rp, i, "negative vertical space (desk-reject risk); cut text instead")
            if re.search(r"\\(renewcommand\{?\\baselinestretch|linespread|setlength\{?\\(textheight|textwidth|columnsep|abovedisplayskip|belowdisplayskip|parskip|floatsep|textfloatsep)|titlespacing|addtolength\{?\\textheight)", s) or re.search(r"\\usepackage(\[[^\]]*\])?\{geometry\}", s):
                add(ERR, "T13", rp, i, "layout or spacing change; venues forbid altering the template")
            # tall inline math: $...\sqrt{...\sum...}$ or \frac with \sum inside $...$
            for mm in re.finditer(r"(?<!\\)\$([^$]+)\$", s):
                t = mm.group(1)
                if any(tall(x) for x in sqrt_args(t)) or r"\dfrac" in t or (r"\frac" in t and r"\sum" in t):
                    add(WARN, "T11", rp, i, f"tall inline math may collide with the line above: ${t[:60]}$")
            if re.search(r"\\begin\{multline\*?\}", s):
                add(INFO, "T12", rp, i, "multline right-aligns its last line; in narrow columns align* with a left-aligned continuation usually reads better")
            if re.search(r"[A-Za-z\)\.,]\s\\(cite|ref|eqref)\{", s):
                add(INFO, "T14", rp, i, "use a non-breaking space (~) before \\cite/\\ref")
            for w in re.finditer(r"\b(\w+)\s+\1\b", s):
                if w.group(1).lower() in {"the", "a", "an", "of", "to", "in", "is", "and", "that", "we", "for", "on", "with"}:
                    add(WARN, "T17", rp, i, f"repeated word '{w.group(0)}'")
            for lab in re.findall(r"\\label\{([^}]*)\}", s):
                labels[lab] = (rp, i)
            for r_ in re.findall(r"\\(?:ref|eqref|autoref|cref|Cref)\{([^}]*)\}", s):
                refs.update(x.strip() for x in r_.split(","))

    # ---------------- document-level rules
    t = re.search(r"\\title(\[[^\]]*\])?\{(.*?)\}\s*\n", alltex, re.S)
    if t and "\\\\" in t.group(2):
        add(WARN, "T08", "main", 0, "hand-made line break in \\title; let the class break it and check for orphan words")
    if ieee and re.search(r"\\usepackage(\[[^\]]*\])?\{[^}]*\bamsthm\b", alltex):
        add(ERR, "T07", "preamble", 0, "amsthm with IEEEtran: conflicting theorem/proof styles and an open QED box")
    if bst.lower().startswith("ieeetran") and "CTLdash_repeated_names" not in "".join("\n".join(lines_of(b)) for b in bibs):
        add(WARN, "T03", "bib", 0, "IEEEtran.bst prints a dash for repeated author names; add an IEEEtranBSTCTL entry with CTLdash_repeated_names = \"no\" and \\bstctlcite")
    if "IEEEtranBSTCTL" in "".join("\n".join(lines_of(b)) for b in bibs) and "\\bstctlcite" not in alltex:
        add(ERR, "T03", "main", 0, "BST control entry exists but \\bstctlcite{...} is not called after \\begin{document}")
    if ieee and "\\thanks" in alltex and "\\IEEEoverridecommandlockouts" not in alltex:
        add(WARN, "T10", "preamble", 0, "\\thanks in IEEEtran conference mode needs \\IEEEoverridecommandlockouts")
    for lab, (rp, i) in labels.items():
        if re.match(r"(fig|tab|alg|sec|thm|eq|cor|prop|def|lem)", lab) and lab not in refs:
            add(INFO, "T15", rp, i, f"label '{lab}' is never referenced")
    low = alltex.lower()
    pairs = [("labelling", "labeling"), ("labelled", "labeled"), ("modelling", "modeling"), ("normalise", "normalize"),
             ("optimise", "optimize"), ("materialise", "materialize"), ("summarise", "summarize"), ("behaviour", "behavior")]
    for gb, us in pairs:
        ng, nu = low.count(gb), low.count(us)
        if ng and nu:
            add(WARN, "T16", "text", 0, f"mixed spelling: '{gb}' x{ng} vs '{us}' x{nu}")

    # ---------------- bibliography
    keys = {}
    for b in bibs:
        rb = os.path.relpath(b, root)
        txt = "\n".join(lines_of(b))
        for em in re.finditer(r"@(\w+)\s*\{\s*([^,\s]+)\s*,(.*?)\n\}", txt, re.S):
            typ, key, body = em.group(1).lower(), em.group(2), em.group(3)
            line = txt[:em.start()].count("\n") + 1
            if typ == "ieeetranbstctl":
                continue
            if key in keys:
                add(ERR, "T06", rb, line, f"duplicate bib key {key}")
            keys[key] = line
            f = {k.lower(): v.strip() for k, v in re.findall(r"(\w+)\s*=\s*[{\"](.*?)[}\"]\s*,?\s*(?=\n\s*\w+\s*=|\Z)", body, re.S)}
            if re.search(r"\band\s+others\b|et al", f.get("author", "")):
                add(WARN, "T04", rb, line, f"{key}: author list truncated ('and others'/'et al.'); give every author (self-citations especially)")
            y = re.search(r"\d{4}", f.get("year", ""))
            if not y:
                add(WARN, "T06", rb, line, f"{key}: no year")
            elif int(y.group()) > a.year:
                add(ERR, "T05", rb, line, f"{key}: year {y.group()} is in the future")
            elif int(y.group()) >= a.year - 1 and ("doi" in f or typ in ("article", "inproceedings")):
                add(INFO, "T05", rb, line, f"{key}: recent {typ} ({y.group()}); verify venue, pages and DOI online")
            if typ == "article" and "pages" not in f:
                add(INFO, "T06", rb, line, f"{key}: journal article without pages")
    cited = set()
    for c in re.findall(r"\\(?:no)?cite[tp]?\*?(?:\[[^\]]*\])?\{([^}]*)\}", alltex):
        cited.update(x.strip() for x in c.split(","))
    for k in cited - set(keys) - {"*"}:
        add(ERR, "T06", "text", 0, f"\\cite{{{k}}} has no bib entry")

    order = {ERR: 0, WARN: 1, INFO: 2}
    for lev, rule, p, i, msg in sorted(out, key=lambda x: (order[x[0]], x[1], x[2], x[3])):
        print(f"{lev:5s} {rule}  {p}:{i}  {msg}")
    n = {k: sum(1 for x in out if x[0] == k) for k in order}
    print(f"\n{n[ERR]} errors, {n[WARN]} warnings, {n[INFO]} notes (class={cls or '?'}, bst={bst or '?'})")
    sys.exit(1 if n[ERR] else 0)


if __name__ == "__main__":
    main()
