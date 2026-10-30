#!/usr/bin/env python3
"""Pre-submission checks for a double-blind Data Science and Engineering (Springer, sn-jnl) LaTeX manuscript.

Usage: python3 check_dse_submission.py FOLDER [--main main.tex] [--forbid REGEX] [--title-page FILE]
Prints ERROR / WARN / OK lines and exits 1 on any ERROR. Reads files only.
"""
import argparse, pathlib, re, sys

problems = {"ERROR": 0, "WARN": 0}


def report(level, msg):
    if level in problems:
        problems[level] += 1
    print(f"{level:5s} {msg}")


def strip_comments(s):
    return re.sub(r"(?<!\\)%.*", "", s)


def braced(s, start):
    depth = 0
    for i in range(start, len(s)):
        if s[i] == "{":
            depth += 1
        elif s[i] == "}":
            depth -= 1
            if depth == 0:
                return s[start + 1:i]
    return None


def macro(s, name):
    m = re.search(r"\\" + name + r"(\[[^\]]*\])?\s*\{", s)
    return braced(s, m.end() - 1) if m else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder")
    ap.add_argument("--main", default="main.tex")
    ap.add_argument("--forbid", default="")
    a = ap.parse_args()
    root = pathlib.Path(a.folder)
    raw = (root / a.main).read_text(errors="ignore")
    s = strip_comments(raw)

    report("OK" if re.search(r"\\documentclass\[[^\]]*sn-mathphys-num[^\]]*\]\{sn-jnl\}", s) else "ERROR", "sn-jnl with sn-mathphys-num (39/39 published DSE articles print numeric citations)")
    report("OK" if "pdflatex" in s.split("\n")[0] else "WARN", "pdflatex class option")
    report("OK" if (root / "sn-jnl.cls").exists() else "ERROR", "sn-jnl.cls in folder")
    report("ERROR" if re.search(r"\\(input|include)\{", s) else "OK", "flat source without \\input or \\include")

    ab = macro(s, "abstract") or ""
    n = len(re.sub(r"\\[a-zA-Z]+|[{}]", " ", ab).split())
    report("OK" if 150 <= n <= 250 else "ERROR", f"abstract {n} words (150-250)")
    report("ERROR" if re.search(r"\\cite", ab) else "OK", "no citation in the abstract")
    kw = macro(s, "keywords") or ""
    k = len([x for x in kw.split(",") if x.strip()])
    report("OK" if 4 <= k <= 6 else "ERROR", f"{k} keywords (4-6)")

    report("ERROR" if "\\subsubsubsection" in s or "\\paragraph*" in s else "OK", "at most three heading levels")
    report("WARN" if re.search(r"sidewaystable|sidewaysfigure|landscape", s) else "OK", "no rotated floats")

    # blinding
    report("ERROR" if re.search(r"\\author\*|\\affil|\\email|\\orcid", s) else "OK", "no author block, affiliation, email or ORCID macro")
    for head in ["Funding", "Competing interests", "Declaration of competing", "CRediT", "Author contribution", "Acknowledg"]:
        report("ERROR" if re.search(r"\\(section\*?|bmhead)\{[^}]*" + head, s) else "OK", f"no '{head}' heading in the blinded manuscript")
    if a.forbid:
        hits = sorted({m.group(0) for m in re.finditer(a.forbid, s)})
        report("ERROR" if hits else "OK", f"forbidden strings: {hits or 'none'}")
    report("WARN" if re.search(r"(zenodo\.org|10\.5281/zenodo|github\.com/wanghongsheng)", s) else "OK", "no public deposit link that could reveal authors")
    report("WARN" if re.search(r"\b(our|we) (previous|prior|earlier) (work|paper|study)", s, re.I) else "OK", "no 'our earlier work' phrasing")

    # LLM documentation
    report("OK" if re.search(r"Codex|Claude|ChatGPT|GPT|LLM|language model", s) else "WARN", "LLM use documented in the body, if any was used")
    report("ERROR" if "Declaration of generative AI" in s else "OK", "no Elsevier AI heading")
    report("ERROR" if re.search(r"elsarticle|\\journal\{|\\begin\{frontmatter\}|\\sep\b", s) else "OK", "no elsarticle leftovers")
    report("OK" if "Online Resource" in s else "WARN", "supplements cited as Online Resource")

    # figures
    figs = re.findall(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}", s)
    for f in figs:
        ok = (root / f).exists()
        report("OK" if ok else "ERROR", f"figure file present: {f}")
        report("OK" if re.match(r"Fig\d+\.", f) else "WARN", f"figure named FigN: {f}")
    caps = re.findall(r"\\begin\{figure\}.*?\\caption\{(.*?)\}\s*\n?\\label", s, re.S)
    for c in caps:
        if c.rstrip().endswith("."):
            report("WARN", f"figure caption ends with a period: ...{c.rstrip()[-40:]}")

    # references
    keys = re.findall(r"\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}", s)
    cited = set(x.strip() for g in re.findall(r"\\cite[a-z]*(?:\[[^\]]*\])?\{([^}]+)\}", s) for x in g.split(","))
    report("OK" if not (cited - set(keys)) else "ERROR", f"undefined citations: {sorted(cited - set(keys)) or 'none'}")
    report("OK" if not (set(keys) - cited) else "WARN", f"uncited references: {sorted(set(keys) - cited) or 'none'}")
    entries = re.findall(r"\\bibitem(?:\[[^\]]*\])?\{[^}]+\}\s*(.+)", s)
    last = [re.sub(r"[^a-z]", "", re.sub(r"\\[\"'~`^]\{?|\{|\}", "", e).split(",")[0].split(":")[0].lower()) for e in entries]
    report("OK" if last == sorted(last) else "WARN", "reference list alphabetized by first author")
    nodoi = [e[:40] for e in entries if "doi.org" not in e and "http" not in e]
    report("OK" if not nodoi else "WARN", f"references without DOI or URL: {nodoi or 'none'}")

    print(f"\n{problems['ERROR']} ERROR, {problems['WARN']} WARN")
    sys.exit(1 if problems["ERROR"] else 0)


if __name__ == "__main__":
    main()
