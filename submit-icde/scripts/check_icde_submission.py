#!/usr/bin/env python3
"""Pre-submission checks for an IEEE ICDE research-track LaTeX manuscript (rules of the ICDE 2027 CFP).

Usage: python3 check_icde_submission.py FOLDER [--main main.tex] [--pdf main.pdf] [--eab] [--scope scope.txt]
Prints ERROR / WARN / OK lines and exits 1 on any ERROR. Reads files only.
Page counting needs pypdf (pip install pypdf); without it the PDF checks are skipped with a WARN.
"""
import argparse, pathlib, re, sys

problems = {"ERROR": 0, "WARN": 0}


def report(level, msg):
    if level in problems:
        problems[level] += 1
    print(f"{level:5s} {msg}")


def strip_comments(s):
    return re.sub(r"(?<!\\)%.*", "", s)


def expand(root, name, seen=None):
    """Inline \\input/\\include files so that the checks see the whole manuscript."""
    seen = seen or set()
    p = root / (name if name.endswith(".tex") else name + ".tex")
    if p in seen or not p.exists():
        return ""
    seen.add(p)
    s = strip_comments(p.read_text(errors="ignore"))
    return re.sub(r"\\(?:input|include)\{([^}]+)\}", lambda m: expand(root, m.group(1), seen), s)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder")
    ap.add_argument("--main", default="main.tex")
    ap.add_argument("--pdf", default=None)
    ap.add_argument("--eab", action="store_true", help="Experiment, Analysis and Benchmark paper")
    ap.add_argument("--scope", default=None, help="text file with the out-of-scope justification (<=1000 chars)")
    a = ap.parse_args()
    root = pathlib.Path(a.folder)
    s = expand(root, a.main)

    report("OK" if re.search(r"\\documentclass\[[^\]]*conference[^\]]*\]\{IEEEtran\}", s) else "ERROR",
           "IEEEtran conference class (CFP: IEEE format)")
    for bad, why in [(r"\\vspace\*?\{\s*-", "negative \\vspace (CFP forbids negative spaces)"),
                     (r"\\setlength\{\\(textheight|textwidth|columnsep|topmargin|oddsidemargin)", "page geometry changed"),
                     (r"\\usepackage(\[[^\]]*\])?\{geometry\}", "geometry package"),
                     (r"\\(small|footnotesize|scriptsize)\s*\\selectfont", "global font shrink")]:
        report("ERROR" if re.search(bad, s) else "OK", "no " + why)
    report("ERROR" if re.search(r"\\appendix|\\section\*?\{\s*Appendix", s, re.I) else "OK", "no appendix (CFP: no appendix allowed)")

    title = re.search(r"\\title\{(.+?)\}\s*\n", s, re.S)
    t = title.group(1) if title else ""
    if a.eab:
        report("OK" if t.strip().startswith("[Experiment, Analysis, and Benchmark]") else "ERROR",
               "EAB title starts with [Experiment, Analysis, and Benchmark]")
    report("WARN" if re.search(r"Author Name|Anonymous|Affiliation", s) else "OK",
           "author block filled in (ICDE is single-blind: real names and affiliations)")

    ack = re.search(r"\\section\*?\{\s*(Acknowledg(e)?ments?|AI-Generated Content[^}]*)\}(.*?)(\\bibliography|\\end\{document\})", s, re.S | re.I)
    ack_txt = ack.group(3) if ack else ""
    report("OK" if re.search(r"\b(AI|LLM|GPT|language model|Claude|DeepSeek|ChatGPT)\b", ack_txt) else "ERROR",
           "AI-generated content disclosure in the acknowledgments (system, sections, level of use)")

    abst = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", s, re.S)
    n = len(re.sub(r"\\[a-zA-Z]+|[{}$]", " ", abst.group(1)).split()) if abst else 0
    report("OK" if 150 <= n <= 260 else "WARN", f"abstract {n} words (published ICDE median ~200)")
    report("ERROR" if abst and re.search(r"\\cite", abst.group(1)) else "OK", "no citation in the abstract")

    cites = set(k.strip() for m in re.findall(r"\\cite[pt]?\*?(?:\[[^\]]*\])?\{([^}]+)\}", s) for k in m.split(","))
    bibs = list(root.glob("*.bib"))
    keys = set()
    for b in bibs:
        keys |= set(re.findall(r"@\w+\{([^,\s]+),", b.read_text(errors="ignore")))
    missing = sorted(c for c in cites if c not in keys)
    report("ERROR" if missing else "OK", f"{len(cites)} cited keys resolved" + (f"; missing {missing[:10]}" if missing else ""))
    core = sum(1 for b in bibs for e in re.split(r"\n@", b.read_text(errors="ignore"))
               if re.search(r"VLDB|SIGMOD|Manag\.? Data|ICDE|Data Engineering", e))
    report("OK" if core >= 10 else "WARN", f"{core} references to VLDB/SIGMOD/ICDE (desk-reject risk if the paper does not build on core DB venues)")
    defined = set(re.findall(r"\\newcommand\{\\([A-Za-z]+)\}", s))
    undefined = sorted(set(re.findall(r"\\(NUM[A-Za-z]+)", s)) - defined)
    report("WARN" if re.search(r"TODO|XXX", s) or undefined else "OK",
           "no TODO/XXX or undefined number macro left" + (f" (undefined: {undefined})" if undefined else ""))

    link = re.search(r"https?://(github\.com|anonymous\.4open\.science|zenodo\.org|figshare)[^\s}]*", s)
    report("OK" if link else "WARN", "artifact link in the paper (CFP expects code/data via a public repository; EAB: mandatory)")
    if a.eab and not link:
        report("ERROR", "EAB papers must provide all artifacts")

    if a.scope:
        txt = pathlib.Path(a.scope).read_text().strip()
        report("OK" if len(txt) <= 1000 else "ERROR", f"scope justification {len(txt)} characters (<= 1000)")

    pdf = pathlib.Path(a.pdf) if a.pdf else root / (pathlib.Path(a.main).stem + ".pdf")
    if pdf.exists():
        try:
            from pypdf import PdfReader
            r = PdfReader(str(pdf)); pages = [p.extract_text() or "" for p in r.pages]
            ref_page = next((i for i, p in enumerate(pages) if re.search(r"^\s*REFERENCES\s*$", p, re.M)), None)
            body = (ref_page + 1) if ref_page is not None else len(pages)
            report("OK" if body <= 12 else "ERROR", f"{len(pages)} pages, references start on page {body} (body <= 12 pages)")
            sz = r.pages[0].mediabox
            report("OK" if abs(float(sz.width) - 612) < 2 and abs(float(sz.height) - 792) < 2 else "WARN", "US Letter page size (IEEE template)")
        except ImportError:
            report("WARN", "pypdf not installed; page count not checked")
    else:
        report("WARN", f"no PDF at {pdf}; compile first to check the 12-page limit")

    print(f"\n{problems['ERROR']} errors, {problems['WARN']} warnings")
    print("Manual: ORCID for every author; CMT profile with domain + individual conflicts for EVERY author;\n"
          "COIs (co-authors since 2023, same institution, advisor); <=5 submissions per author per round;\n"
          "not under review elsewhere; not rejected by ICDE within the last year.")
    sys.exit(1 if problems["ERROR"] else 0)


if __name__ == "__main__":
    main()
