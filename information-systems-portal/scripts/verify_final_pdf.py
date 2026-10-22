#!/usr/bin/env python3
"""Check the Overleaf-compiled Manuscript.pdf before it is uploaded to the Information Systems portal.

Catches the failures seen in practice:
  - Type 3 (bitmap) or unembedded fonts;
  - unresolved references ("??") and placeholders (XXXXX, TODO);
  - a PDF compiled from a stale main.tex: every --expect sentence must appear, and with
    --previous the script prints the word-level text changes against an earlier build;
  - an upload zip that does not contain the current main.tex (--zip with --tex).

Usage:
  python3 verify_final_pdf.py --pdf Manuscript.pdf [--expect "sentence" ...] [--forbid TERM ...]
                              [--previous OLD.pdf] [--zip LaTeX_source.zip --tex main.tex]
Exit status 1 when any check fails.
"""
import argparse
import difflib
import hashlib
import re
import subprocess
import sys
import zipfile

ap = argparse.ArgumentParser()
ap.add_argument("--pdf", required=True)
ap.add_argument("--expect", action="append", default=[], help="text that must appear (latest edits, DOI, ...)")
ap.add_argument("--forbid", action="append", default=[], help="text that must not appear (old journal, project codes)")
ap.add_argument("--previous", help="earlier compiled PDF to diff against")
ap.add_argument("--zip", help="LaTeX source zip that was uploaded to Overleaf")
ap.add_argument("--tex", help="current main.tex to compare with the zip")
a = ap.parse_args()

fail = []


def run(*cmd):
    return subprocess.run(cmd, capture_output=True, text=True, check=True).stdout


def text_of(pdf):
    return run("pdftotext", "-q", pdf, "-")


def flat(s):
    s = s.replace("­", "")
    s = re.sub(r"-\n(?=[a-z])", "", s)          # rejoin hyphenated line breaks
    return re.sub(r"\s+", " ", s)


info = run("pdfinfo", a.pdf)
pages = re.search(r"Pages:\s+(\d+)", info).group(1)
created = (re.search(r"CreationDate:\s+(.*)", info) or [None, "?"])[1]
fonts = run("pdffonts", a.pdf).splitlines()[2:]
type3 = [f for f in fonts if "Type 3" in f]
unemb = [f for f in fonts if not re.search(r"\s(yes)\s+(yes|no)\s+(yes|no)\s+\d+\s+\d+\s*$", f)]
print(f"pages {pages} | created {created.strip()} | fonts {len(fonts)} | Type 3 {len(type3)} | not embedded {len(unemb)}")
if type3:
    fail.append("Type 3 fonts present: compile on Overleaf or a full TeX Live (cm-super)")
if unemb:
    fail.append("unembedded fonts: " + "; ".join(f.split()[0] for f in unemb))

txt = flat(text_of(a.pdf))
for bad in ["??"] + a.forbid:
    n = txt.count(bad)
    if n:
        ctx = txt[max(0, txt.find(bad) - 40):txt.find(bad) + 40]
        fail.append(f"found {bad!r} x{n}: ...{ctx}...")
if re.search(r"X{5,}|\bTODO\b|\bTBD\b", txt):
    fail.append("placeholder text (XXXXX/TODO/TBD) in the PDF")
for e in a.expect:
    ok = flat(e) in txt
    print(("OK    " if ok else "MISS  ") + e[:90])
    if not ok:
        fail.append(f"expected text missing (stale source?): {e[:80]}")

if a.previous:
    old = flat(text_of(a.previous)).split(" ")
    new = txt.split(" ")
    sm = difflib.SequenceMatcher(None, old, new, autojunk=False)
    ch = [(op, " ".join(old[i1:i2]), " ".join(new[j1:j2])) for op, i1, i2, j1, j2 in sm.get_opcodes() if op != "equal"]
    # ignore page-number-only moves
    ch = [c for c in ch if not (re.fullmatch(r"\d*", c[1].strip()) and re.fullmatch(r"\d*", c[2].strip()))]
    print(f"text changes against {a.previous}: {len(ch)}")
    for op, x, y in ch[:30]:
        print(f"  {op}: {x[:100]!r} -> {y[:100]!r}")
    if not ch:
        fail.append("identical text to the previous build: the new edits were not compiled")

if a.zip:
    with zipfile.ZipFile(a.zip) as z:
        names = [n for n in z.namelist() if n.endswith("main.tex")]
        if not names:
            fail.append("no main.tex in the zip")
        elif a.tex:
            zh = hashlib.sha256(z.read(names[0])).hexdigest()
            th = hashlib.sha256(open(a.tex, "rb").read()).hexdigest()
            print(f"zip main.tex {zh[:12]} | current main.tex {th[:12]}")
            if zh != th:
                fail.append("the zip does not contain the current main.tex: rebuild and re-copy it, then read it back")

for f in fail:
    print("FAIL", f)
print("RESULT", "FAIL" if fail else "PASS")
sys.exit(1 if fail else 0)
