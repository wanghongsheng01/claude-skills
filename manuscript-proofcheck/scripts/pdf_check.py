#!/usr/bin/env python3
"""Compiled-PDF checks for submissions: rules P01-P19 of references/defect-catalog.md. Needs PyMuPDF (pip install pymupdf).

Usage: python3 pdf_check.py PAPER.pdf --out DIR [--body-limit 12] [--dpi 110]
Writes DIR/page-NN.png for the visual pass and DIR/text.txt, and prints the findings.
"""
import argparse, os, re, sys

try:
    import fitz
except ImportError:
    sys.exit("PyMuPDF is required: pip install pymupdf")

BAD_GLYPHS = {"⊮": "⊮ (wrong glyph, usually \\mathbb 1)", "�": "U+FFFD replacement character",
              "□": "□ empty box (missing glyph or foreign QED mark)", "☐": "☐ empty box"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf"); ap.add_argument("--out", required=True)
    ap.add_argument("--body-limit", type=int, default=None); ap.add_argument("--dpi", type=int, default=110)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    d = fitz.open(a.pdf)
    find = []
    texts = []
    ref_page = None
    for i, p in enumerate(d, 1):
        p.get_pixmap(dpi=a.dpi).save(os.path.join(a.out, f"page-{i:02d}.png"))
        t = p.get_text(); texts.append(f"=== page {i}\n{t}")
        for ln in t.split("\n"):
            for g, why in BAD_GLYPHS.items():
                if g in ln: find.append(("ERROR", "P01", i, f"{why}: {ln.strip()[:90]}"))
            if re.search(r"\?\?|\[\?\]", ln): find.append(("ERROR", "P02", i, f"unresolved reference/citation: {ln.strip()[:90]}"))
            if re.search(r"\bTODO\b|\bXXX\b|\[citation needed\]", ln): find.append(("ERROR", "P09", i, f"draft marker: {ln.strip()[:90]}"))
            if re.match(r"\s*(\[\d+\]\s*)?(——|---|—{2,}|_{3,})\s*,", ln): find.append(("WARN", "P03", i, f"dash for repeated author names: {ln.strip()[:90]}"))
        if ref_page is None and re.search(r"^\s*(R\s*EFERENCES|References|REFERENCES|Bibliography)\s*$", t, re.M):
            ref_page = i
        # text beyond the right margin (overfull floats, rotated headers, long lines)
        W = p.rect.width
        for b in p.get_text("dict")["blocks"]:
            for l in b.get("lines", []):
                for s in l["spans"]:
                    if s["text"].strip() and s["bbox"][2] > W - 36:
                        find.append(("ERROR", "P19", i, f"text past the right margin (x={s['bbox'][2]:.0f} of {W:.0f}pt): {s['text'].strip()[:60]}"))
        if re.search(r"(?i)names? withheld|withheld in this draft|to be completed|ANONYMI[SZ]ED|Affiliation to be", t):
            find.append(("ERROR", "P09", i, "placeholder author block, affiliation or link in the PDF"))
        # coloured text spans (draft markers are often red)
        for b in p.get_text("dict")["blocks"]:
            for l in b.get("lines", []):
                for s in l["spans"]:
                    c = s["color"]; rr, gg, bb = (c >> 16) & 255, (c >> 8) & 255, c & 255
                    if rr > 150 and gg < 100 and bb < 100 and s["text"].strip():
                        find.append(("WARN", "P09", i, f"red text: {s['text'].strip()[:80]}"))
    # title: largest spans on page 1
    spans = [(round(s["size"], 1), s["bbox"][1], s["text"]) for b in d[0].get_text("dict")["blocks"] for l in b.get("lines", []) for s in l["spans"] if s["text"].strip()]
    if spans:
        top = max(x[0] for x in spans)
        rows = {}
        for sz, y, tx in spans:
            if sz == top: rows.setdefault(round(y), []).append(tx)
        lines = [" ".join(v).strip() for _, v in sorted(rows.items())]
        msg = f"title has {len(lines)} line(s): " + " | ".join(lines)
        short = [x for x in lines[1:] if len(x.split()) <= 2]
        find.append(("WARN" if len(lines) > 3 or short else "INFO", "P08", 1, msg + ("  <- short/orphan line" if short else "")))
    # fonts
    fonts = {}
    for p in d:
        for f in p.get_fonts():
            fonts[f[3]] = (f[1], f[2])
    for name, (ext, typ) in sorted(fonts.items()):
        if typ == "Type3": find.append(("WARN", "P17", 0, f"Type 3 font {name} (bitmap/figure font; set pdf.fonttype=42 in matplotlib)"))
        if ext in ("", "n/a"): find.append(("WARN", "P17", 0, f"font {name} may not be embedded"))
    n = len(d)
    find.append(("INFO", "P13", 0, f"{n} pages; reference heading on page {ref_page}"))
    if a.body_limit and ref_page and ref_page > a.body_limit:
        find.append(("ERROR", "P13", ref_page, f"body runs to page {ref_page} (> limit {a.body_limit}); check how the venue counts pages"))
    with open(os.path.join(a.out, "text.txt"), "w") as fh: fh.write("\n".join(texts))
    order = {"ERROR": 0, "WARN": 1, "INFO": 2}
    seen = set()
    for lev, rule, pg, msg in sorted(find, key=lambda x: (order[x[0]], x[1], x[2])):
        if (rule, pg, msg) in seen: continue
        seen.add((rule, pg, msg)); print(f"{lev:5s} {rule}  p{pg}  {msg}")
    print(f"\nPNG pages and text in {a.out}; now inspect every page visually (SKILL.md checklist).")
    sys.exit(1 if any(x[0] == "ERROR" for x in find) else 0)


if __name__ == "__main__":
    main()
