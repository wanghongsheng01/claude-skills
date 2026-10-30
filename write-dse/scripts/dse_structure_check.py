#!/usr/bin/env python3
"""Compare a LaTeX manuscript with the medians of 39 published DSE articles and count hedging phrases.
Usage: python3 dse_structure_check.py main.tex   (reads files only)"""
import re, sys
s = re.sub(r"(?<!\\)%.*", "", open(sys.argv[1], errors="ignore").read())
body = s[s.find("\\section"):]
text = re.sub(r"\\[a-zA-Z]+\*?(\[[^\]]*\])?|[{}$]", " ", body)
title = re.search(r"\\title(?:\[[^\]]*\])?\{(.+?)\}\n", s)
tw = len(title.group(1).split()) if title else 0
HEDGE = ["does not establish", "do not establish", "not establish", "establish no", "establishes neither", "exploratory", "unknown", "unmeasured", "not measured", "cannot", "not a ", "rather than", "only", "neither", "undetermined", "not evaluated", "no independent", "does not"]
rows = [
 ("title words", tw, "10"),
 ("colon in title", int(":" in (title.group(1) if title else "")), "18/39"),
 ("top-level sections", len(re.findall(r"\\section\{", body)), "7"),
 ("figures", len(re.findall(r"\\begin\{figure", body)), "7"),
 ("tables", len(re.findall(r"\\begin\{table", body)), "5"),
 ("references", len(re.findall(r"\\bibitem", s)), "53"),
 ("words", len(text.split()), "10.9k"),
 ("research questions", len(set(re.findall(r"RQ\d", body))), "7/39 use them"),
 ("contribution list", int(bool(re.search(r"contributions?", body, re.I))), "28/39"),
 ("'limitation|threat' mentions", len(re.findall(r"limitation|threats? to validity", body, re.I)), "median 1"),
]
for n, v, m in rows:
    print(f"{n:32s} {v:>7}   DSE median/share: {m}")
print("\nHedging phrases:")
total = 0
for h in HEDGE:
    c = len(re.findall(re.escape(h), text, re.I))
    total += c
    if c:
        print(f"  {h:24s} {c}")
print(f"  total {total}, i.e. {1000 * total / max(len(text.split()), 1):.1f} per 1000 words")
