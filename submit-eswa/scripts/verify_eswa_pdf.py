#!/usr/bin/env python3
"""Check a compiled ESWA manuscript PDF before upload (pure Python, needs `pip install pypdf`).

  python3 verify_eswa_pdf.py --pdf Manuscript.pdf --identity 'Surname|University|Company|github-user' \
      [--expect 'sentence from the newest edit'] [--forbid 'Old Journal Name'] [--previous old.pdf]

Checks: PDF metadata (Author/Creator fields must not identify anyone), identity strings in the
text (double-anonymized review), unresolved references ('??', '[?]'), placeholders, Type 3 or
non-embedded fonts, expected/forbidden text and, with --previous, whether the text changed at all.
Prints PASS/FAIL lines; exits 1 on any FAIL.
"""
import argparse
import re
import sys

try:
    from pypdf import PdfReader
except ImportError:
    sys.exit("pip install pypdf")

fails = 0


def say(ok, msg):
    global fails
    fails += 0 if ok else 1
    print(("PASS " if ok else "FAIL ") + msg)


def text_of(path):
    r = PdfReader(path)
    return r, "\n".join((p.extract_text() or "") for p in r.pages)


def fonts(reader):
    bad_type3, not_embedded = set(), set()
    for page in reader.pages:
        res = page.get("/Resources") or {}
        fd = res.get("/Font") or {}
        for _, ref in fd.items():
            f = ref.get_object()
            name = str(f.get("/BaseFont", "?"))
            if f.get("/Subtype") == "/Type3":
                bad_type3.add(name)
                continue
            desc = f.get("/FontDescriptor")
            if f.get("/Subtype") == "/Type0":
                df = f["/DescendantFonts"][0].get_object()
                desc = df.get("/FontDescriptor")
            if desc is not None:
                d = desc.get_object()
                if not any(k in d for k in ("/FontFile", "/FontFile2", "/FontFile3")):
                    not_embedded.add(name)
    return bad_type3, not_embedded


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", required=True)
    ap.add_argument("--identity", default=None)
    ap.add_argument("--expect", action="append", default=[])
    ap.add_argument("--forbid", default=None)
    ap.add_argument("--previous", default=None)
    a = ap.parse_args()

    reader, txt = text_of(a.pdf)
    flat = " ".join(txt.split())
    print(f"INFO {len(reader.pages)} pages, {len(flat.split())} words")
    meta = reader.metadata or {}
    for k in ("/Author", "/Creator", "/Producer", "/Title", "/Subject", "/Keywords"):
        if k in meta:
            print(f"INFO metadata {k} = {meta[k]}")
    if a.identity:
        rx = re.compile(a.identity, re.I)
        say(not rx.search(str(meta.get("/Author", "")) + str(meta.get("/Creator", ""))),
            "metadata carries no identity string")
        hits = sorted(set(m.group(0) for m in rx.finditer(flat)))
        say(not hits, "text carries no identity string" + (f" (found: {hits})" if hits else ""))
    say("??" not in flat and "[?]" not in flat, "no unresolved references (?? or [?])")
    say(not re.search(r"\[(placeholder|TODO|XXX)|TBD|lorem ipsum", flat, re.I), "no placeholders")
    t3, ne = fonts(reader)
    say(not t3, "no Type 3 fonts" + (f" ({sorted(t3)[:5]})" if t3 else ""))
    say(not ne, "all fonts embedded" + (f" ({sorted(ne)[:5]})" if ne else ""))
    for e in a.expect:
        say(" ".join(e.split()) in flat, f"expected text present: {e[:60]}")
    if a.forbid:
        m = re.search(a.forbid, flat)
        say(not m, "no forbidden text" + (f" (found '{m.group(0)}')" if m else ""))
    if a.previous:
        _, old = text_of(a.previous)
        say(" ".join(old.split()) != flat, "text differs from the previous build (otherwise a stale source was compiled)")
    print("RESULT", "PASS" if not fails else f"FAIL ({fails})")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
