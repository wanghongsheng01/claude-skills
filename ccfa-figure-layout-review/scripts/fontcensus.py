#!/usr/bin/env python3
"""fontcensus: per page, list text lines whose printed glyph size is below a threshold (default 7pt).
Usage: fontcensus.py paper.pdf [threshold]"""
import sys, statistics
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextLine, LTChar
thr = float(sys.argv[2]) if len(sys.argv) > 2 else 7.0
for pi, page in enumerate(extract_pages(sys.argv[1]), 1):
    out = {}
    def walk(o):
        if isinstance(o, LTTextLine):
            cs = [c for c in o if isinstance(c, LTChar) and c.get_text().isalpha()]
            if len(cs) >= 2:
                k = round(statistics.median([c.size for c in cs]), 1)
                if k < thr: out.setdefault(k, []).append(o.get_text().strip()[:25])
            return
        for c in getattr(o, "_objs", []) or []: walk(c)
    walk(page)
    for k, v in sorted(out.items()):
        print(f"p{pi}: {k}pt x{len(v)} e.g. {' | '.join(v[:4])}")
