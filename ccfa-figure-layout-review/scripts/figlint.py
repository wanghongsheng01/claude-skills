#!/usr/bin/env python3
"""figlint: render + crop + layout lint for LaTeX paper PDFs (CCF-A figure/layout review).

Usage: figlint.py PAPER.pdf OUTDIR [--log main.log] [--dpi 200]

Produces in OUTDIR:
  pages/page-NN.png        full-page renders
  crops/fig-N_pP.png       crop of each Figure (caption + region above it)
  crops/tab-N_pP.png       crop of each Table
  lint.md                  machine findings (text-on-text overlaps, out-of-margin text,
                           tiny text inside figures, overfull boxes from the log)
The script never edits sources. Visual checks (arrows through boxes, legend on data,
clipped labels) still require a human/agent to look at every crop.
"""
import argparse, os, re, subprocess, html, statistics, glob
from PIL import Image

def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True, errors="ignore").stdout

def words_by_page(pdf):
    xml = run(["pdftotext", "-bbox-layout", pdf, "-"])
    pages = []
    for pm in re.finditer(r'<page width="([\d.]+)" height="([\d.]+)">(.*?)</page>', xml, re.S):
        W, H, body = float(pm.group(1)), float(pm.group(2)), pm.group(3)
        lines = []
        for li, lm in enumerate(re.finditer(r'<line xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</line>', body, re.S)):
            ws = [(float(a), float(b), float(c), float(d), html.unescape(t)) for a, b, c, d, t in
                  re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>', lm.group(5))]
            if ws:
                lines.append(dict(id=li, x0=float(lm.group(1)), y0=float(lm.group(2)), x1=float(lm.group(3)), y1=float(lm.group(4)), words=ws,
                                  text=" ".join(w[4] for w in ws)))
        pages.append(dict(W=W, H=H, lines=lines))
    return pages

def inter(a, b):
    w = min(a[2], b[2]) - max(a[0], b[0]); h = min(a[3], b[3]) - max(a[1], b[1])
    return max(0, w) * max(0, h)


def pdfminer_scan(pdf, body_pt=9.0, min_pt=6.0):
    """Glyph-height-based scan (needs pdfminer.six). Uses rendered glyph box heights, so text
    shrunk by \\resizebox or by scaling an included plot is measured at its printed size.
    Effective pt = glyph height / median body glyph height * body_pt."""
    try:
        from pdfminer.high_level import extract_pages
        from pdfminer.layout import LTTextLine, LTChar, LAParams
    except Exception:
        return None
    pages = list(extract_pages(pdf, laparams=LAParams(line_margin=0.2)))
    allh = []
    per = []
    for page in pages:
        lines = []
        def walk(o):
            if isinstance(o, LTTextLine):
                lines.append(o); return
            for c in getattr(o, "_objs", []) or []:
                walk(c)
        walk(page)
        per.append((page, lines))
        for ln in lines:
            allh += [c.height for c in ln if isinstance(c, LTChar) and c.get_text().isalpha()]
    med = statistics.median(allh) if allh else 1
    tiny, overlaps = [], []
    for pi, (page, lines) in enumerate(per, 1):
        for ln in lines:
            chars = [c for c in ln if isinstance(c, LTChar) and c.get_text().isalnum()]
            small = [c for c in chars if c.height / med * body_pt < min_pt - 0.05]
            txt = "".join(c.get_text() for c in small)
            if len(txt) >= 3 and len(small) >= 0.6 * max(1, len(chars)):
                tiny.append((pi, txt[:60], min(c.height for c in small) / med * body_pt, ln.y1))
        good = [l for l in lines if len(re.sub(r"[^A-Za-z0-9]", "", l.get_text())) >= 3]
        for i in range(len(good)):
            a = good[i]
            for j in range(i + 1, len(good)):
                b = good[j]
                w = min(a.x1, b.x1) - max(a.x0, b.x0); h = min(a.y1, b.y1) - max(a.y0, b.y0)
                if w <= 0 or h <= 0: continue
                ar = min((a.x1-a.x0)*(a.y1-a.y0), (b.x1-b.x0)*(b.y1-b.y0))
                if ar > 0 and w*h/ar > 0.30 and h > 0.5*min(a.y1-a.y0, b.y1-b.y0):
                    overlaps.append((pi, a.get_text().strip()[:40], b.get_text().strip()[:40], a.x0, page.height - a.y1))
    return tiny, overlaps

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf"); ap.add_argument("out")
    ap.add_argument("--log"); ap.add_argument("--dpi", type=int, default=200)
    ap.add_argument("--body-pt", type=float, default=9.0, help="body font size (ACM sigconf 9, PVLDB 9-10)")
    a = ap.parse_args()
    os.makedirs(f"{a.out}/pages", exist_ok=True); os.makedirs(f"{a.out}/crops", exist_ok=True)
    for f in glob.glob(f"{a.out}/pages/*.png") + glob.glob(f"{a.out}/crops/*.png"):
        os.remove(f)
    subprocess.run(["pdftoppm", "-r", str(a.dpi), "-png", a.pdf, f"{a.out}/pages/page"])
    imgs = sorted(glob.glob(f"{a.out}/pages/page-*.png"))
    pages = words_by_page(a.pdf)
    s = a.dpi / 72.0
    heights = [l["y1"] - l["y0"] for p in pages for l in p["lines"] if len(l["words"]) > 6]
    body_h = statistics.median(heights) if heights else 10
    rep = [f"# figlint report: {os.path.basename(a.pdf)}", "", f"pages={len(pages)}, body line height≈{body_h:.1f}pt", ""]
    overlaps, margins, tiny = [], [], []
    for pi, p in enumerate(pages, 1):
        W, H = p["W"], p["H"]
        allw = [(w, l["id"]) for l in p["lines"] for w in l["words"]]
        # text-on-text: words from different lines whose boxes intersect substantially
        for i in range(len(allw)):
            (wa, la) = allw[i]
            for j in range(i + 1, len(allw)):
                (wb, lb) = allw[j]
                if la == lb: continue
                ar = min((wa[2]-wa[0])*(wa[3]-wa[1]), (wb[2]-wb[0])*(wb[3]-wb[1]))
                if ar <= 0: continue
                if inter(wa, wb) / ar > 0.25:
                    overlaps.append((pi, wa[4], wb[4], wa[0], wa[1]))
        for l in p["lines"]:
            if l["x1"] > W - 36 or l["x0"] < 36:
                margins.append((pi, l["text"][:60], l["x0"], l["x1"]))
            hgt = l["y1"] - l["y0"]
            if hgt < 0.65 * body_h and len(l["text"]) > 1:
                tiny.append((pi, l["text"][:50], hgt))
        # crops
        img = Image.open(imgs[pi - 1]) if pi - 1 < len(imgs) else None
        if img is None: continue
        for l in p["lines"]:
            m = re.match(r'^(Figure|Fig\.|Table)\s+(\d+)[:.]', l["text"])
            if not m: continue
            kind = "fig" if m.group(1).startswith("F") else "tab"
            colw = W / 2
            full = (l["x1"] - l["x0"]) > colw * 1.05 or (l["x0"] < colw < l["x1"])
            x0, x1 = (0, W) if full else ((0, colw) if l["x0"] < colw else (colw, W))
            # caption block: following lines within same column close below
            cap_bottom = l["y1"]
            for l2 in sorted(p["lines"], key=lambda z: z["y0"]):
                if l2["y0"] > cap_bottom and l2["y0"] - cap_bottom < body_h * 0.9 and l2["x0"] >= x0 - 2 and l2["x1"] <= x1 + 2:
                    cap_bottom = l2["y1"]
            if kind == "fig":
                # region above caption up to last body-text paragraph line in the column
                top = 40
                for l2 in p["lines"]:
                    if l2["y1"] < l["y0"] - 2 and l2["x0"] >= x0 - 2 and l2["x1"] <= x1 + 2 and len(l2["words"]) >= 9 \
                       and abs((l2["y1"] - l2["y0"]) - body_h) < 1.5 and (l2["x1"] - l2["x0"]) > 0.8 * (x1 - x0) - 20:
                        top = max(top, l2["y1"])
                box = (x0, top, x1, cap_bottom + 4)
            else:
                # tables: caption on top; take until next body paragraph line below
                bot = H - 40
                for l2 in p["lines"]:
                    if l2["y0"] > cap_bottom + 4 and l2["x0"] >= x0 - 2 and l2["x1"] <= x1 + 2 and len(l2["words"]) >= 9 \
                       and abs((l2["y1"] - l2["y0"]) - body_h) < 1.5 and (l2["x1"] - l2["x0"]) > 0.8 * (x1 - x0) - 20:
                        bot = min(bot, l2["y0"])
                box = (x0, max(0, l["y0"] - 4), x1, bot)
            crop = img.crop(tuple(int(v * s) for v in box))
            crop.save(f"{a.out}/crops/{kind}-{m.group(2)}_p{pi}.png")
    pm = pdfminer_scan(a.pdf, body_pt=a.body_pt)
    if pm is not None:
        tiny = [(p, t, h) for p, t, h, _ in pm[0]]
        overlaps = pm[1]
        rep += ["(sizes = printed glyph height relative to median body glyph, scaled to --body-pt; overlaps via pdfminer)", ""]
    rep += ["## Text-on-text overlaps (words from different lines whose boxes intersect >25%)", ""]
    rep += [f"- p{p}: '{x}' ∩ '{y}' at ({cx:.0f},{cy:.0f})pt from top-left" for p, x, y, cx, cy in overlaps[:200]] or ["- none"]
    rep += ["", "## Text within 0.5in of page edge (possible margin overflow; ignore page numbers/headers if expected)", ""]
    rep += [f"- p{p}: x=[{x0:.0f},{x1:.0f}] '{t}'" for p, t, x0, x1 in margins[:100]] or ["- none"]
    rep += ["", "## Tiny text (glyphs < 6 pt at print size; pdfminer) / or line height < 65% body (fallback)", ""]
    agg = {}
    for p_, t_, h_ in tiny:
        d = agg.setdefault(p_, [99, 0, []]); d[0] = min(d[0], h_); d[1] += 1
        if len(d[2]) < 6: d[2].append(t_[:30])
    rep += [f"- p{p_}: {d[1]} runs, min {d[0]:.1f}pt, e.g. " + " | ".join(d[2]) for p_, d in sorted(agg.items())] or ["- none"]
    if a.log and os.path.exists(a.log):
        lg = open(a.log, errors="ignore").read()
        ov = re.findall(r'([^\n]*Overfull \\[hv]box \(([\d.]+)pt too \w+\)[^\n]*)', lg)
        rep += ["", "## Overfull boxes from log", ""]
        ov = sorted(set(x for x in ov if float(x[1]) > 1.0), key=lambda x: -float(x[1]))
        rep += [f"- {x[0][:160]}" for x in ov] or ["- none (>1pt)"]
        fl = re.findall(r'(Float too large[^\n]*|LaTeX Warning: [^\n]*undefined[^\n]*)', lg)
        rep += [f"- {x[:140]}" for x in fl]
    open(f"{a.out}/lint.md", "w").write("\n".join(rep) + "\n")
    print(f"{a.out}/lint.md", len(overlaps), "overlaps", len(margins), "margin", len(tiny), "tiny",
          len(glob.glob(f"{a.out}/crops/*.png")), "crops")

if __name__ == "__main__":
    main()
