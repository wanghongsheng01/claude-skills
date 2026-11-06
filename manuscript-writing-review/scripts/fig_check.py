#!/usr/bin/env python3
"""Check vector figure files (PDF, as produced by matplotlib and similar) before they go into the paper:
rules F01-F04 of references/defect-catalog.md. Needs PyMuPDF (pip install pymupdf).

Usage: python3 fig_check.py figs/*.pdf [--png DIR]
  F01 text cut off at the canvas edge (legend or label placed outside the saved area)
  F02 text drawn over other text (annotation over a bar label, legend over tick labels)
  F03 text drawn over a coloured shape (legend or label over bars, lines or markers)
  F04 scatter markers drawn on top of each other (clustered points that the reader cannot tell apart)
With --png, each figure is rendered for the visual check. Exit code 1 if any problem is found.
"""
import argparse, os, sys

try:
    import fitz
except ImportError:
    sys.exit("PyMuPDF is required: pip install pymupdf")


def area(r):
    r = fitz.Rect(r)
    return 0.0 if r.is_empty else r.width * r.height


def check(path, png=None):
    out = []
    d = fitz.open(path)
    p = d[0]
    page = p.rect
    if png:
        p.get_pixmap(dpi=200).save(os.path.join(png, os.path.basename(path)[:-4] + ".png"))
    raw = [w for w in p.get_text("words", clip=fitz.Rect(-1e4, -1e4, 1e4, 1e4)) if w[4].strip()]
    words = [w for w in p.get_text("words") if w[4].strip()]
    # F01: compare clipped and unclipped extraction, and words touching the canvas edge
    if len(raw) > len(words) or any(w[2] > page.x1 + 0.5 or w[0] < page.x0 - 0.5 or w[1] < page.y0 - 0.5 or w[3] > page.y1 + 0.5 for w in raw):
        for w in raw:
            if not page.contains(fitz.Rect(w[:4])):
                out.append(("F01", f"text outside the canvas, cut off in the paper: '{w[4]}'"))
    for w in words:
        if w[2] >= page.x1 - 0.3:
            out.append(("F01", f"text touches the right canvas edge (likely cut): '{w[4]}'"))
    # F02: text over text
    for j in range(len(words)):
        for k in range(j + 1, len(words)):
            A, B = fitz.Rect(words[j][:4]), fitz.Rect(words[k][:4])
            if (words[j][5], words[j][6]) == (words[k][5], words[k][6]) or min(len(words[j][4]), len(words[k][4])) < 2:
                continue
            if area(A & B) > 0.1 * min(area(A), area(B)):
                out.append(("F02", f"text over text: '{words[j][4]}' / '{words[k][4]}'"))
    # F03: text over coloured fills (bars), fills clipped to the axes panels (white rectangles)
    dr = [x for x in p.get_drawings() if x.get("fill") is not None and x["rect"].width > 1 and x["rect"].height > 1]
    white = [x["rect"] for x in dr if min(x["fill"]) > 0.97]
    for x in dr:
        if min(x["fill"]) > 0.97:
            continue
        r = x["rect"] & page
        panes = [wr for wr in white if wr.contains(fitz.Point(r.x0 + 0.1, r.y0 + 0.1))]
        if panes:
            r = r & min(panes, key=area)
        for w in words:
            if area(fitz.Rect(w[:4]) & r) > 2:
                out.append(("F03", f"text over a coloured shape: '{w[4]}'"))
    # F04: small filled shapes (scatter markers) that cover each other; legend handles never overlap one another
    marks = [x["rect"] for x in dr if min(x["fill"]) <= 0.97 and 1 < x["rect"].width < 12 and 1 < x["rect"].height < 12]
    for j in range(len(marks)):
        for k in range(j + 1, len(marks)):
            if area(marks[j] & marks[k]) > 0.25 * min(area(marks[j]), area(marks[k])):
                c = marks[j]
                out.append(("F04", f"markers overlap at ({c.x0:.0f}, {c.y0:.0f}) pt: separate them (broken or zoomed axis, "
                                   "larger figure, direct labels) instead of a legend lookup"))
    return sorted(set(out))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("figs", nargs="+"); ap.add_argument("--png")
    a = ap.parse_args()
    if a.png:
        os.makedirs(a.png, exist_ok=True)
    n = 0
    for f in a.figs:
        for rule, msg in check(f, a.png):
            print(f"ERROR {rule}  {os.path.basename(f)}  {msg}")
            n += 1
    print(f"\n{n} problems in {len(a.figs)} figures" + (f"; PNGs in {a.png} - look at each one" if a.png else ""))
    sys.exit(1 if n else 0)


if __name__ == "__main__":
    main()
