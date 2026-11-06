#!/usr/bin/env python3
"""Layout checks on a compiled two-column (or one-column) paper: rules L01-L07 of references/defect-catalog.md.
Needs PyMuPDF (pip install pymupdf).

Usage: python3 layout_check.py PAPER.pdf [--out DIR] [--dpi 120]
  L01 text that crosses the column gutter or runs into the other column (overfull table/figure in one column)
  L02 text past the page margin
  L03 words drawn on top of other words (table over body text, legend over labels)
  L04 text drawn on top of filled shapes inside figures (legend or annotation over bars)
  L05 end-of-proof glyphs (filled or open boxes) that authors read as garbled characters
  L06 replacement / missing glyphs, '??', '[?]'
  L07 text clipped at the edge of an embedded figure (word cut off by the figure's bounding box)
With --out, every page is rendered to DIR/page-NN.png for the mandatory visual pass.
Exit code 1 if any ERROR is found.
"""
import argparse, os, re, sys

try:
    import fitz
except ImportError:
    sys.exit("PyMuPDF is required: pip install pymupdf")

QED = {"■": "filled end-of-proof box", "□": "open end-of-proof box", "∎": "end-of-proof glyph", "◻": "open box"}
BAD = {"�": "U+FFFD replacement character", "⊮": "wrong glyph (\\mathbb 1)"}


def area(r):
    r = fitz.Rect(r)
    return 0.0 if r.is_empty else r.width * r.height


def inter(a, b, pad=0.6):
    return min(a[2], b[2]) - max(a[0], b[0]) > pad and min(a[3], b[3]) - max(a[1], b[1]) > pad


def columns(words, W):
    """Return (left_col_right, right_col_left) for a two-column page, or None for one column."""
    xs0 = sorted(w[0] for w in words if w[0] > W * 0.45)
    xs1 = sorted(w[2] for w in words if w[2] < W * 0.55)
    if len(xs0) < 30 or len(xs1) < 30:
        return None
    # most common right edge of the left column and left edge of the right column
    def mode(v):
        h = {}
        for x in v:
            h[round(x)] = h.get(round(x), 0) + 1
        return max(h, key=h.get)
    l, r = mode(xs1), mode(xs0)
    return (l, r) if r - l > 4 else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf"); ap.add_argument("--out"); ap.add_argument("--dpi", type=int, default=120)
    a = ap.parse_args()
    d = fitz.open(a.pdf)
    if a.out:
        os.makedirs(a.out, exist_ok=True)
    F = []
    allw = [w for p in d for w in p.get_text("words") if w[4].strip()]
    cols = columns(allw, d[0].rect.width) if len(d) else None
    for i, p in enumerate(d, 1):
        W = p.rect.width
        words = [w for w in p.get_text("words") if w[4].strip()]
        if a.out:
            p.get_pixmap(dpi=a.dpi).save(os.path.join(a.out, f"page-{i:02d}.png"))
        # L01: a word that enters the column gutter while the other column has body text on the same line
        if cols:
            L, R = cols
            starts = {}
            for v in words:
                k_ = (v[5], v[6])
                starts[k_] = min(starts.get(k_, 1e9), v[0])
            for w in words:
                if starts[(w[5], w[6])] > L / 2:  # line does not start in the left column (title, full-width text)
                    continue
                if (w[0] < L - 1 and w[2] > L + 2) or (L + 1 < w[0] < R - 2):
                    if any(abs(v[0] - R) < 1.5 and abs(v[3] - w[3]) < 4 for v in words):
                        F.append(("ERROR", "L01", i, f"text runs into the other column (x {w[0]:.0f}-{w[2]:.0f}, column ends at {L}): '{w[4]}' - overfull table/figure"))
        # L02: past the margin
        for w in words:
            if w[2] > W - 36 or w[0] < 30:
                F.append(("ERROR", "L02", i, f"text past the page margin (x {w[0]:.0f}-{w[2]:.0f} of {W:.0f}): {w[4]}"))
        # L03: overlapping words (ignores sub/superscripts: small overlap or one-character words)
        ws = sorted(words, key=lambda w: (round(w[1]), w[0]))
        for j in range(len(ws)):
            for k in range(j + 1, min(j + 40, len(ws))):
                A, B = fitz.Rect(ws[j][:4]), fitz.Rect(ws[k][:4])
                if (ws[j][5], ws[j][6]) == (ws[k][5], ws[k][6]) or len(ws[j][4]) < 2 or len(ws[k][4]) < 2:
                    continue
                I = A & B
                if not I.is_empty and area(I) > 0.1 * min(area(A), area(B)):
                    F.append(("ERROR", "L03", i, f"text over text: '{ws[j][4]}' / '{ws[k][4]}' at y={ws[j][1]:.0f}"))
        # L04: text over coloured shapes inside a figure (legend or annotation over bars); shapes are clipped to the
        # smallest white panel (axes background) that contains them, since log-scale bars extend far beyond the axes
        dr = [x for x in p.get_drawings() if x.get("fill") is not None and x["rect"].width > 1 and x["rect"].height > 1]
        white = [x["rect"] for x in dr if min(x["fill"]) > 0.97]
        for x in dr:
            f, r = x["fill"], x["rect"]
            if min(f) > 0.97:
                continue
            # L05: IEEEtran draws its QED mark as a small black square, not as a glyph
            if max(f) < 0.05 and 4 < r.width < 8 and abs(r.width - r.height) < 0.5:
                F.append(("ERROR", "L05", i, f"end-of-proof box at y={r.y0:.0f} - readers report it as a garbled character; drop the QED mark"))
                continue
            panes = [wr for wr in white if wr.contains(fitz.Point(r.x0 + 0.1, r.y0 + 0.1))]
            if not panes:
                continue
            r = r & min(panes, key=area)
            for w in words:
                if fitz.Rect(w[:4]).intersects(r) and area(fitz.Rect(w[:4]) & r) > 2:
                    F.append(("ERROR", "L04", i, f"figure text overlaps a bar/shape: '{w[4]}'"))
        # L07: figure text cut off at the edge of its panel (legend or label placed outside the figure canvas)
        outer = [wr for wr in white if not any(o != wr and o.contains(wr) for o in white)]
        for wr in outer:
            for w in words:
                if wr.contains(fitz.Point(w[0] + 0.1, w[1] + 0.1)) and w[2] >= wr.x1 - 0.5 and wr.width < W * 0.95:
                    F.append(("ERROR", "L07", i, f"figure text cut off at the figure edge: '{w[4]}'"))
        # L05/L06: glyphs
        t = p.get_text()
        for g, why in QED.items():
            if g in t:
                F.append(("ERROR", "L05", i, f"{why} '{g}' - readers report it as a garbled character; drop the QED mark"))
        for g, why in BAD.items():
            if g in t:
                F.append(("ERROR", "L06", i, why))
        if re.search(r"\?\?|\[\?\]", t):
            F.append(("ERROR", "L06", i, "unresolved reference or citation"))
        # L07: words clipped by an embedded figure's box
        for b in p.get_text("dict", clip=None)["blocks"]:
            for l in b.get("lines", []):
                for s in l["spans"]:
                    if s["text"].strip() and s["bbox"][2] > W + 1:
                        F.append(("ERROR", "L07", i, f"text drawn outside the page (clipped): {s['text'][:40]}"))
    seen, out = set(), []
    for f in F:
        if f not in seen:
            seen.add(f); out.append(f)
    F = out
    for sev, rule, pg, msg in F:
        print(f"{sev:5} {rule}  p{pg}  {msg}")
    n = sum(1 for f in F if f[0] == "ERROR")
    print(f"\n{n} errors, {sum(1 for f in F if f[0] == 'WARN')} warnings, {len(d)} pages"
          + (f"; page PNGs in {a.out} - open EVERY page" if a.out else ""))
    sys.exit(1 if n else 0)


if __name__ == "__main__":
    main()
