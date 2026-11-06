#!/usr/bin/env python3
"""Source-level readability and layout-risk lint for a LaTeX paper: rules R01-R12 of references/defect-catalog.md.
It follows the \\input/\\include chain of the main file and also scans figure scripts given with --figscripts.

Usage: python3 review_lint.py PAPER_DIR [--main main.tex] [--figscripts code/make_paper.py ...]
Severity: ERROR = fix before handing over; WARN = check in the compiled PDF and fix if visible.
"""
import argparse, os, re, sys

INLINE = re.compile(r"(?<!\\)\$(?!\$)(.+?)(?<!\\)\$", re.S)
HEAVY = re.compile(r"\\(sum|prod|bigcup|bigcap|int)\b|\\\{.*?:.*?\\\}|\\begin\{cases\}")
TALL = re.compile(r"\\(frac|binom|dfrac|tfrac)\b")
OPS = re.compile(r"\\(cap|cup|setminus|subseteq|ge|le|in|notin|cdot|times)\b|[<>=+]")


def files(root, main):
    seen, order = set(), []

    def visit(f):
        p = os.path.join(root, f if f.endswith(".tex") else f + ".tex")
        if p in seen or not os.path.exists(p):
            return
        seen.add(p); order.append(p)
        for m in re.finditer(r"^[^%\n]*\\(?:input|include)\{([^}]+)\}", open(p, encoding="utf-8").read(), re.M):
            visit(m.group(1))
    visit(main)
    return order


def strip_comments(t):
    return re.sub(r"(?<!\\)%.*", "", t)


def lint_tex(path, text, refs, out):
    rel = path
    lines = text.split("\n")
    body = strip_comments(text)
    # R01/R02: dense inline math in running text (outside display environments)
    para_start = 0
    for para in re.split(r"\n\s*\n", body):
        lineno = body[:body.find(para)].count("\n") + 1 if para else 0
        if re.search(r"\\begin\{(equation|align|tabular|algorithm)", para):
            continue
        segs = [m.group(1) for m in INLINE.finditer(para)]
        for s in segs:
            n_ops = len(OPS.findall(s))
            if HEAVY.search(s) or len(s) > 55 or n_ops >= 5:
                out.append(("ERROR", "R01", f"{rel}:{lineno}", f"heavy inline formula, set it as a display: ${s.strip()[:70]}$"))
            elif TALL.search(s):
                out.append(("WARN", "R01", f"{rel}:{lineno}", f"tall inline fraction/binomial pushes the line spacing apart; consider a display or a/b: ${s.strip()[:70]}$"))
        if "\\newcommand" in para:
            continue
        for sent in re.split(r"(?<=[.;:])\s+", para):
            # count only real formulas, not single symbols such as $k$ or $\times$
            k = sum(1 for x in INLINE.findall(sent) if OPS.search(x) and "\\times" not in x)
            if k >= 7:
                out.append(("WARN", "R02", f"{rel}:{lineno}", f"{k} inline formulas in one sentence; split it or move the conditions into a display/cases: {sent.strip()[:70]}"))
    # R03: inline math that starts with a binary operator right after a comma (broken split formula)
    for i, ln in enumerate(lines, 1):
        if re.search(r",\s*\$\s*[+\-=]\s*\\?,?", ln) and not ln.lstrip().startswith("%"):
            out.append(("ERROR", "R03", f"{rel}:{i}", f"formula split by a comma, an operator starts a new $...$: {ln.strip()[:70]}"))
    # R04: end-of-proof glyph policy
    if re.search(r"\\documentclass(\[[^]]*\])?\{IEEEtran\}", body) and "\\renewcommand{\\IEEEQED}{}" not in body.replace(" ", "") \
            and re.search(r"\\begin\{(IEEEproof|proof)\}", body):
        out.append(("ERROR", "R04", f"{rel}:1", "proofs end in a box (IEEEtran closed box, amsthm open box) that authors read as a garbled glyph; "
                    "add \\renewcommand{\\IEEEQED}{} after the packages (or follow the venue template if it mandates a mark)"))
    if re.search(r"\\usepackage(\[[^]]*\])?\{[^}]*amsthm", body) and "IEEEtran" in body:
        out.append(("ERROR", "R04", f"{rel}:1", "amsthm under IEEEtran: use IEEEproof and drop amsthm"))
    for i, ln in enumerate(lines, 1):
        s = strip_comments(ln)
        # R05: narrow justified p{} columns (word rivers) in tables
        if re.search(r"\\begin\{tabular\}\{[^}]*p\{", s) and "raggedright" not in s:
            out.append(("ERROR", "R05", f"{rel}:{i}", "p{} columns are justified and leave large gaps between words; use >{\\raggedright\\arraybackslash}p{..} (needs \\usepackage{array})"))
        # R06: algorithm comments that wrap
        for m in re.finditer(r"\\tc[pc]\*?(?:\[[a-z]\])?\{((?:[^{}]|\{[^{}]*\})*)\}", s):
            txt = re.sub(r"\\[a-zA-Z]+|[{}~$]", "", m.group(1))
            if len(txt) > 18:
                out.append(("WARN", "R06", f"{rel}:{i}", f"long algorithm comment ({len(txt)} chars) wraps in a narrow column; shorten it or move it to the text: {m.group(1)[:50]}"))
        if re.search(r"\\l(If|ElseIf|Else|ForEach|For|While)\b.*\\tc[pc]", s) and len(s) > 110:
            out.append(("WARN", "R06", f"{rel}:{i}", "one-line algorithm statement with a comment is likely to wrap; use the block form or drop the comment"))
        # R07: enumerate with an optional label but no enumitem/enumerate package
        if re.search(r"\\begin\{enumerate\}\[", s):
            out.append(("WARN", "R07", f"{rel}:{i}", "enumerate[...] needs enumitem/enumerate (and enumitem clashes with IEEEtran); inside theorems write (a)~ (b)~ inline"))
    # R08: numbered equations that are never referenced
    for m in re.finditer(r"\\begin\{equation\}\s*\\label\{([^}]+)\}", body):
        if m.group(1) not in refs:
            out.append(("WARN", "R08", rel, f"equation {m.group(1)} is numbered but never referenced; use \\[ \\] or cite it with \\eqref"))
    for m in re.finditer(r"\\begin\{equation\}(?!\s*\\label)", body):
        out.append(("WARN", "R08", rel, "numbered equation without a label; use \\[ \\] if it is never referenced"))
    # R09: single-column tables with many columns at \small or larger
    for m in re.finditer(r"\\begin\{table\}(.*?)\\end\{table\}", body, re.S):
        t = m.group(1)
        spec = re.search(r"\\begin\{tabular\}\{([^}]*(?:\{[^}]*\}[^}]*)*)\}", t)
        if not spec:
            continue
        ncol = len(re.findall(r"[lcrpXS](?![^{]*\})", spec.group(1)))
        size = "small" if "\\small" in t else "footnotesize" if "\\footnotesize" in t else "scriptsize" if "\\scriptsize" in t else "normal"
        if (ncol >= 7 and size in ("normal", "small")) or (ncol >= 8 and size == "footnotesize"):
            ln = body[:m.start()].count("\n") + 1
            out.append(("WARN", "R09", f"{rel}:{ln}", f"{ncol}-column table in one column at {size}: high overflow risk; verify the width in the PDF (layout_check L01/L02)"))


def lint_bib(path, out):
    t = open(path, encoding="utf-8").read()
    for m in re.finditer(r"(note|howpublished)\s*=\s*\{([^}]*)\}", t):
        v = m.group(2)
        if re.search(r"(?i)according to|comments?\b|TODO|\?|unverified|check", v):
            ln = t[:m.start()].count("\n") + 1
            out.append(("ERROR", "R10", f"{path}:{ln}", f"bib note reads like an internal remark: '{v}'"))


def call_args(text, start):
    """Text of the call whose opening parenthesis is at text[start], across lines."""
    depth = 0
    for j in range(start, len(text)):
        depth += {"(": 1, ")": -1}.get(text[j], 0)
        if depth == 0:
            return text[start:j + 1]
    return text[start:]


def lint_figscript(path, out):
    text = open(path, encoding="utf-8").read()
    for m in re.finditer(r"legend\(", text):  # a legend call may span several lines
        args, i = call_args(text, m.end() - 1), text[:m.start()].count("\n") + 1
        if "bbox_to_anchor" not in args and re.search(r"loc\s*=\s*['\"](upper|lower|center|best|right|left)", args):
            out.append(("WARN", "R11", f"{path}:{i}", "legend placed inside the axes can cover bars or labels; put it above the axes "
                        "(loc='lower center', bbox_to_anchor=(0.5, 1.0)) or check with fig_check.py"))
        if re.search(r"ncol\s*=\s*([5-9])", args) and "bbox_to_anchor" not in args:
            out.append(("WARN", "R12", f"{path}:{i}", "legend with many columns in a one-column figure can run past the canvas and be cut off"))
    for i, ln in enumerate(text.splitlines(), 1):
        if re.search(r"\.text\([^)]*transform\s*=\s*ax\.transAxes", ln):
            out.append(("WARN", "R11", f"{path}:{i}", "free text placed in axes coordinates may overlap data labels; move it to the caption"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paper"); ap.add_argument("--main", default="main.tex"); ap.add_argument("--figscripts", nargs="*", default=[])
    a = ap.parse_args()
    fs = files(a.paper, a.main)
    alltext = "\n".join(strip_comments(open(f, encoding="utf-8").read()) for f in fs)
    refs = set(x for m in re.finditer(r"\\(?:eq)?ref\{([^}]+)\}", alltext) for x in m.group(1).split(","))
    out = []
    for f in fs:
        lint_tex(os.path.relpath(f, a.paper), open(f, encoding="utf-8").read(), refs, out)
    for m in re.finditer(r"\\bibliography\{([^}]+)\}", alltext):
        for b in m.group(1).split(","):
            p = os.path.join(a.paper, b.strip() + ("" if b.strip().endswith(".bib") else ".bib"))
            if os.path.exists(p):
                lint_bib(p, out)
    for f in a.figscripts:
        lint_figscript(f, out)
    for sev, rule, where, msg in out:
        print(f"{sev:5} {rule}  {where}  {msg}")
    n = sum(1 for o in out if o[0] == "ERROR")
    print(f"\n{n} errors, {len(out) - n} warnings")
    sys.exit(1 if n else 0)


if __name__ == "__main__":
    main()
