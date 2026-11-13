#!/usr/bin/env python3
"""check_pdf_layout.py — PVLDB / acmart two-column pre-delivery layout lint.

Flags:
  - text-box overlaps (body colliding with itself, with figures, with footnotes)
  - text overflowing the page or the conventional acmart letter margins
  - unusually small body/table fonts (unreadable at print size)
  - LaTeX log issues, if a .log is provided: Overfull/Underfull \\hbox/\\vbox,
    undefined citations/references, multiply-defined labels

Usage:
  python check_pdf_layout.py paper.pdf [--log main.log] [--dpi 150]
      [--out report.txt] [--render-dir pages/] [--margin-pt 54]

Exit codes: 0 = no errors (warnings allowed); 1 = errors found; 2 = usage/IO.
This script never modifies the PDF. It does not invent numbers from the paper.
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from typing import List, Optional, Tuple

try:
    import pymupdf
except ImportError:
    sys.stderr.write("error: pymupdf is required (pip install pymupdf)\n")
    sys.exit(2)


BBox = Tuple[float, float, float, float]


def area(b: BBox) -> float:
    return max(0.0, b[2] - b[0]) * max(0.0, b[3] - b[1])


def intersection(a: BBox, b: BBox) -> Optional[BBox]:
    x0, y0 = max(a[0], b[0]), max(a[1], b[1])
    x1, y1 = min(a[2], b[2]), min(a[3], b[3])
    if x1 - x0 > 0.5 and y1 - y0 > 0.5:
        return (x0, y0, x1, y1)
    return None


def inter_area(a: BBox, b: BBox) -> float:
    i = intersection(a, b)
    return area(i) if i else 0.0


def min_frac(a: BBox, b: BBox) -> float:
    ia = inter_area(a, b)
    m = min(area(a), area(b))
    return ia / m if m > 1 else 0.0


@dataclass
class Span:
    page: int
    bbox: BBox
    text: str
    size: float
    font: str
    kind: str  # text | image | drawing
    block_no: int = -1


@dataclass
class Issue:
    severity: str  # error | warning
    page: int
    code: str
    message: str
    bbox: Optional[BBox] = None
    evidence: str = ""


@dataclass
class Report:
    issues: List[Issue] = field(default_factory=list)
    pages: int = 0
    page_size: Optional[Tuple[float, float]] = None
    log_overfull: List[str] = field(default_factory=list)
    log_underfull: List[str] = field(default_factory=list)
    log_undefined: List[str] = field(default_factory=list)
    log_multiply: List[str] = field(default_factory=list)
    small_font_pages: dict = field(default_factory=dict)

    def add(self, *a, **k):
        self.issues.append(Issue(*a, **k))

    @property
    def n_error(self) -> int:
        return sum(1 for i in self.issues if i.severity == "error")

    @property
    def n_warn(self) -> int:
        return sum(1 for i in self.issues if i.severity == "warning")


def collect_spans(page, page_no: int) -> List[Span]:
    spans: List[Span] = []
    d = page.get_text("dict")
    for bi, block in enumerate(d.get("blocks", [])):
        if block.get("type") == 1:  # image
            spans.append(Span(page_no, tuple(block["bbox"]), "[IMAGE]", 0, "", "image", bi))
            continue
        for line in block.get("lines", []):
            for s in line.get("spans", []):
                txt = s.get("text") or ""
                spans.append(
                    Span(
                        page_no,
                        tuple(s["bbox"]),
                        txt,
                        float(s.get("size") or 0),
                        s.get("font") or "",
                        "text",
                        bi,
                    )
                )
    return spans


def is_page_number(span: Span, page_w: float, page_h: float) -> bool:
    t = span.text.strip()
    if not t:
        return False
    if re.fullmatch(r"\d{1,3}", t) and span.bbox[3] > page_h - 55:
        cx = (span.bbox[0] + span.bbox[2]) / 2
        if abs(cx - page_w / 2) < 90:
            return True
    return False


def nearly_same_line(a: Span, b: Span, tol: float = 2.5) -> bool:
    ya = (a.bbox[1] + a.bbox[3]) / 2
    yb = (b.bbox[1] + b.bbox[3]) / 2
    return abs(ya - yb) < tol


def adjacent_glyphs(a: Span, b: Span) -> bool:
    """Horizontal neighbors on the same line (kerning / italic overlap is normal)."""
    if not nearly_same_line(a, b, 3.0):
        return False
    # small horizontal gap or slight overlap of italic glyphs
    gap = max(a.bbox[0], b.bbox[0]) - min(a.bbox[2], b.bbox[2])
    # gap negative = overlap; italic letter pairs often overlap < 2-3 pts
    if gap > 2:
        return False
    ia = inter_area(a.bbox, b.bbox)
    # tiny italic overlap
    if ia < 20 and abs(a.size - b.size) < 1.5:
        return True
    # if overlap is only a sliver at the edge
    inter = intersection(a.bbox, b.bbox)
    if inter and (inter[2] - inter[0]) < 3.5 and nearly_same_line(a, b, 4):
        return True
    return False


def lint_pdf(path: str, margin_pt: float = 54.0, small_body: float = 7.0,
             small_table: float = 6.0) -> Report:
    rep = Report()
    doc = pymupdf.open(path)
    rep.pages = len(doc)
    if not len(doc):
        rep.add("error", 0, "EMPTY", "PDF has no pages")
        return rep
    r0 = doc[0].rect
    rep.page_size = (r0.width, r0.height)
    # PVLDB / acmart letter is 612 x 792
    if abs(r0.width - 612) > 8 or abs(r0.height - 792) > 8:
        rep.add(
            "warning",
            1,
            "PAGE_SIZE",
            f"page size is {r0.width:.1f}x{r0.height:.1f} pt; PVLDB/acmart letter is 612x792",
        )

    for pi, page in enumerate(doc, 1):
        W, H = page.rect.width, page.rect.height
        spans = collect_spans(page, pi)
        texts = [s for s in spans if s.kind == "text" and s.text.strip()]
        images = [s for s in spans if s.kind == "image"]

        # --- overlaps between text spans ---
        # cluster reported overlaps so we don't flood with per-glyph reports
        overlap_clusters: List[Issue] = []
        for i, a in enumerate(texts):
            if is_page_number(a, W, H):
                continue
            for b in texts[i + 1 :]:
                if is_page_number(b, W, H):
                    continue
                # same span text on identical bbox
                if a.bbox == b.bbox:
                    continue
                ia = inter_area(a.bbox, b.bbox)
                frac = min_frac(a.bbox, b.bbox)
                if ia < 10 or frac < 0.12:
                    continue
                if adjacent_glyphs(a, b):
                    continue
                ta = a.text.strip()
                tb = b.text.strip()
                # Combining accents (bar, hat, underbrace) stacked on a glyph are normal.
                ACCENT = set("¯ˉˆ˜˙¨˚ˇ⃗⃑⏞⏟‾-–—̂̃̇̈")
                if (set(ta) <= ACCENT or set(tb) <= ACCENT) and len(ta) < 8 and len(tb) < 8:
                    continue
                # Two short math glyphs (N ∩ bar already handled; ∑ ∩ x, ⟦ ∩ word-initial)
                # are typical in formal papers and are not body-text collisions.
                if len(ta) <= 2 and len(tb) <= 2:
                    continue
                # skip superscript citation digits overlapping slightly
                if (len(ta) <= 3 and a.size < b.size - 1) or (
                    len(tb) <= 3 and b.size < a.size - 1
                ):
                    if ia < 25:
                        continue
                # A 1–2 char math italic token (J, K, =, x) slightly kissing a
                # nearby word in a syntax display is common; only keep it when
                # the other span is a real phrase AND the overlap is wide,
                # which is the signature of a formula colliding with a paragraph
                # or of two columns running into each other.
                short, long_ = (ta, tb) if len(ta) <= len(tb) else (tb, ta)
                inter = intersection(a.bbox, b.bbox)
                iw = (inter[2] - inter[0]) if inter else 0
                ih = (inter[3] - inter[1]) if inter else 0
                if len(short) <= 2 and len(long_) >= 8:
                    if iw < 6 or ih < 3.5:
                        continue  # a thin math glyph brushing a sentence
                elif len(short) <= 2:
                    continue
                # two columns colliding: different x-centers, similar y, large overlap
                ca = (a.bbox[0] + a.bbox[2]) / 2
                cb = (b.bbox[0] + b.bbox[2]) / 2
                two_col = abs(ca - cb) > 20 and nearly_same_line(a, b, 8) and len(ta) >= 3 and len(tb) >= 3
                ev = f"{a.text[:70]!r}  ∩  {b.text[:70]!r}"
                sev = "error" if (frac >= 0.18 or two_col or ia >= 40) else "warning"
                if len(short) <= 2 and not two_col:
                    sev = "warning"  # math glyph brushing a sentence: inspect, do not fail the run
                overlap_clusters.append(
                    Issue(
                        sev,
                        pi,
                        "TEXT_OVERLAP",
                        f"overlapping text boxes (min-area fraction {frac:.2f}, intersection {ia:.0f} pt²)",
                        intersection(a.bbox, b.bbox),
                        ev,
                    )
                )
        # merge near-duplicate overlap reports (same y-band)
        seen = []
        for iss in overlap_clusters:
            key = (iss.page, round((iss.bbox or (0, 0, 0, 0))[1] / 8), iss.evidence[:40])
            if key in seen:
                continue
            seen.append(key)
            rep.issues.append(iss)

        # --- text overlapping images ---
        # Labels that live *inside* a figure's bbox are expected (axis ticks, legends).
        # Flag only body-sized text that is not contained in the figure, or a caption
        # that has clearly run into the plot.
        for a in texts:
            if is_page_number(a, W, H) or not a.text.strip():
                continue
            for im in images:
                ia = inter_area(a.bbox, im.bbox)
                if ia <= 15:
                    continue
                # contained in the figure → label
                frac_of_text = ia / area(a.bbox) if area(a.bbox) > 1 else 0
                if frac_of_text >= 0.65:
                    continue
                # captions sitting just under a figure are OK if they only kiss the edge
                if a.bbox[1] >= im.bbox[3] - 2:
                    continue
                # short ticks
                if len(a.text.strip()) <= 4 and a.size < 8:
                    continue
                frac = min_frac(a.bbox, im.bbox)
                if frac < 0.15:
                    continue
                # body paragraph colliding with a figure is an error
                sev = "error" if (a.size >= 8 and len(a.text.strip()) >= 8) else "warning"
                rep.add(
                    sev,
                    pi,
                    "TEXT_OVER_FIGURE",
                    f"body-like text overlaps a figure/image (fraction {frac:.2f})",
                    intersection(a.bbox, im.bbox),
                    a.text[:80],
                )

        # --- margin / page overflow ---
        for a in texts:
            if is_page_number(a, W, H) or not a.text.strip():
                continue
            x0, y0, x1, y1 = a.bbox
            # hard overflow past the physical page (almost always a fatal layout bug)
            if x1 > W + 0.4 or x0 < -0.4 or y1 > H + 0.4:
                rep.add(
                    "error",
                    pi,
                    "PAGE_OVERFLOW",
                    f"text extends outside the page box (x1={x1:.1f}, page width={W:.1f})",
                    a.bbox,
                    a.text[:80],
                )
                continue
            # conventional acmart letter margins (~0.75 in = 54 pt).
            # footnotes and page footers are allowed closer to the bottom.
            bottom_allow = 42
            if x0 < margin_pt - 3 and x0 > 8:
                # left-column start at ~54 is exact; only flag clear intrusions
                if x0 < margin_pt - 8:
                    rep.add(
                        "warning",
                        pi,
                        "LEFT_MARGIN",
                        f"text starts at x={x0:.1f} pt (margin ≈ {margin_pt:.0f} pt)",
                        a.bbox,
                        a.text[:60],
                    )
            if x1 > W - margin_pt + 4:
                # right overflow of a formula or a tightly packed table is an error if past 6 pt into the margin
                sev = "error" if x1 > W - margin_pt + 10 else "warning"
                # ignore isolated punctuation
                if len(a.text.strip()) <= 2 and a.size < 8:
                    continue
                rep.add(
                    sev,
                    pi,
                    "RIGHT_MARGIN",
                    f"text reaches x={x1:.1f} pt (right margin starts ≈ {W - margin_pt:.0f} pt)",
                    a.bbox,
                    a.text[:80],
                )
            if y1 > H - bottom_allow + 8 and not is_page_number(a, W, H):
                if y1 > H - 20:
                    rep.add(
                        "warning",
                        pi,
                        "BOTTOM_MARGIN",
                        f"text reaches y={y1:.1f} pt on a {H:.0f} pt page",
                        a.bbox,
                        a.text[:60],
                    )

        # --- small fonts ---
        # Body text in acmart is 9 pt; captions ~8-9; footnotes ~7-8.
        # Tables squeezed with \tiny / \resizebox often drop to 5–6 pt.
        small = [
            s
            for s in texts
            if 0 < s.size < small_body
            and not is_page_number(s, W, H)
            and len(s.text.strip()) > 0
        ]
        # ignore isolated math subscripts (1-2 chars at 6-7 pt is normal)
        table_like = [s for s in small if s.size < small_table + 0.05 and len(s.text.strip()) >= 3]
        if len(table_like) >= 20:
            sizes = sorted({round(s.size, 1) for s in table_like})
            sample = " | ".join(s.text.strip()[:20] for s in table_like[:8])
            rep.add(
                "error" if len(table_like) >= 40 else "warning",
                pi,
                "TINY_TABLE_FONT",
                f"{len(table_like)} spans at <{small_table:.1f} pt (sizes {sizes}); "
                "likely an over-shrunk table, unreadable at print size",
                evidence=sample,
            )
            rep.small_font_pages[pi] = len(table_like)
        # figure labels at tiny sizes
        fig_tiny = [s for s in small if s.size < 6.0 and len(s.text.strip()) >= 4]
        if 3 <= len(fig_tiny) < 20:
            rep.add(
                "warning",
                pi,
                "TINY_FIGURE_LABEL",
                f"{len(fig_tiny)} figure/diagram labels below 6 pt",
                evidence=" | ".join(s.text.strip()[:30] for s in fig_tiny[:6]),
            )

        # --- corresponding-author footnotes stacked at the first-page foot,
        #     colliding with the PVLDB license / reference-format block ---
        if pi == 1:
            corr = [
                s
                for s in texts
                if "corresponding author" in s.text.lower()
                or (s.text.strip() in {"∗", "†", "*", "‡"} and s.bbox[1] > H * 0.75)
            ]
            license_spans = [
                s
                for s in texts
                if "this work is licensed" in s.text.lower()
                or "vldb endowment" in s.text.lower()
                or "pvldb reference format" in s.text.lower()
                or "creativecommons" in s.text.lower()
            ]
            if len(corr) >= 2:
                # two corresponding-author notes: warn if they sit in the same
                # vertical band as the mandatory PVLDB license block
                if license_spans:
                    cy = min(s.bbox[1] for s in corr)
                    ly = max(s.bbox[3] for s in license_spans)
                    # if corresponding notes are at or below the license, or overlap in y
                    corr_box = (
                        min(s.bbox[0] for s in corr),
                        min(s.bbox[1] for s in corr),
                        max(s.bbox[2] for s in corr),
                        max(s.bbox[3] for s in corr),
                    )
                    lic_box = (
                        min(s.bbox[0] for s in license_spans),
                        min(s.bbox[1] for s in license_spans),
                        max(s.bbox[2] for s in license_spans),
                        max(s.bbox[3] for s in license_spans),
                    )
                    y_overlap = min(corr_box[3], lic_box[3]) - max(corr_box[1], lic_box[1])
                    if y_overlap > 2:
                        rep.add(
                            "error",
                            1,
                            "FOOTNOTE_COLLISION",
                            "two (or more) corresponding-author footnotes sit in the same "
                            "vertical band as the PVLDB license / reference-format block; "
                            "this is a common first-page collision",
                            evidence=f"corresponding-author y={corr_box[1]:.1f}–{corr_box[3]:.1f}; "
                            f"license/ref-format y={lic_box[1]:.1f}–{lic_box[3]:.1f}",
                        )
                    elif len(corr) >= 2:
                        rep.add(
                            "warning",
                            1,
                            "TWO_CORR_AUTHOR_NOTES",
                            "two corresponding-author footnotes are present on page 1; "
                            "confirm they do not collide with \\vldbtopmatter (license + "
                            "PVLDB Reference Format + Artifact Availability). Prefer a single "
                            "corresponding-author footnote, or raise the footnote block.",
                            evidence=" | ".join(s.text.strip()[:40] for s in corr[:4]),
                        )

    doc.close()
    return rep


def lint_log(log_path: str, rep: Report, overfull_pt: float = 1.0) -> None:
    try:
        text = open(log_path, "r", encoding="utf-8", errors="replace").read()
    except OSError as e:
        rep.add("warning", 0, "LOG_UNREADABLE", f"cannot read LaTeX log: {e}")
        return
    for m in re.finditer(
        r"Overfull \\(?:hbox|vbox) \(([-\d.]+)pt[^\n]*\)[^\n]*(?:\n[^\n]*)?",
        text,
    ):
        pt = float(m.group(1))
        line = m.group(0).replace("\n", " ").strip()
        rep.log_overfull.append(line)
        sev = "error" if pt >= overfull_pt else "warning"
        # extract page if present
        pg = 0
        pm = re.search(r"\[(\d+)\]", text[m.end() : m.end() + 400])
        if pm:
            try:
                pg = int(pm.group(1))
            except ValueError:
                pg = 0
        rep.add(sev, pg, "OVERFULL", f"Overfull box {pt} pt: {line[:200]}")
    for m in re.finditer(
        r"Underfull \\(?:hbox|vbox) \(badness (\d+)\)[^\n]*",
        text,
    ):
        bad = int(m.group(1))
        line = m.group(0).strip()
        rep.log_underfull.append(line)
        if bad >= 10000:
            rep.add("warning", 0, "UNDERFULL", f"Underfull box badness {bad}: {line[:200]}")
    for m in re.finditer(
        r"LaTeX Warning: (Citation|Reference) [`']([^`']+)[`'] on page (\d+) undefined",
        text,
    ):
        kind, key, pg = m.group(1), m.group(2), int(m.group(3))
        rep.log_undefined.append(m.group(0))
        rep.add(
            "error",
            pg,
            "UNDEFINED_CITE" if kind == "Citation" else "UNDEFINED_REF",
            f"undefined {kind.lower()} '{key}' on page {pg}",
        )
    for m in re.finditer(r"LaTeX Warning: There were undefined references", text):
        if not rep.log_undefined:
            rep.add("error", 0, "UNDEFINED_REF", "log reports undefined references")
    for m in re.finditer(r"LaTeX Warning: Label [`']([^`']+)[`'] multiply defined", text):
        rep.log_multiply.append(m.group(0))
        rep.add("error", 0, "MULTIPLY_DEFINED", f"label '{m.group(1)}' is multiply defined")


def render_pages(pdf_path: str, out_dir: str, dpi: int) -> List[str]:
    os.makedirs(out_dir, exist_ok=True)
    doc = pymupdf.open(pdf_path)
    zoom = dpi / 72.0
    mat = pymupdf.Matrix(zoom, zoom)
    paths = []
    for i, page in enumerate(doc, 1):
        pix = page.get_pixmap(matrix=mat, alpha=False)
        dest = os.path.join(out_dir, f"page-{i:02d}.png")
        pix.save(dest)
        paths.append(dest)
    doc.close()
    return paths


def format_report(rep: Report, pdf_path: str, log_path: Optional[str]) -> str:
    lines = []
    lines.append(f"check_pdf_layout.py")
    lines.append(f"PDF: {pdf_path}")
    if log_path:
        lines.append(f"LOG: {log_path}")
    if rep.page_size:
        lines.append(f"Pages: {rep.pages}    size: {rep.page_size[0]:.1f} x {rep.page_size[1]:.1f} pt")
    else:
        lines.append(f"Pages: {rep.pages}")
    lines.append(f"Errors: {rep.n_error}    Warnings: {rep.n_warn}")
    lines.append("")
    # group by page
    by = defaultdict(list)
    for iss in rep.issues:
        by[iss.page].append(iss)
    if not rep.issues:
        lines.append("No layout issues flagged. Still do a 150 dpi visual pass of every page.")
    else:
        for pg in sorted(by):
            header = f"--- page {pg} ---" if pg else "--- document / log ---"
            lines.append(header)
            for iss in by[pg]:
                loc = ""
                if iss.bbox:
                    loc = "  @ ({:.1f},{:.1f})-({:.1f},{:.1f})".format(*iss.bbox)
                lines.append(f"  [{iss.severity.upper()}] {iss.code}{loc}")
                lines.append(f"      {iss.message}")
                if iss.evidence:
                    ev = iss.evidence.replace("\n", " ")
                    lines.append(f"      evidence: {ev}")
            lines.append("")
    lines.append("Mandatory next step (not automated): open every page at 150 dpi and")
    lines.append("confirm no remaining visual collision, no unreadable table, and no")
    lines.append("formula that runs into the gutter or the margin.")
    return "\n".join(lines) + "\n"


def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pdf", help="compiled paper PDF (letter, acmart two-column)")
    ap.add_argument("--log", help="pdflatex/latexmk .log file")
    ap.add_argument("--dpi", type=int, default=150, help="dpi if --render-dir is set (default 150)")
    ap.add_argument("--out", help="write the text report here as well as stdout")
    ap.add_argument("--render-dir", help="optional directory to write page-N.png at --dpi")
    ap.add_argument("--margin-pt", type=float, default=54.0, help="nominal left/right margin in pt (default 54 = 0.75 in)")
    ap.add_argument("--overfull-pt", type=float, default=1.0, help="treat Overfull boxes at or above this many pt as errors")
    args = ap.parse_args(argv)

    if not os.path.isfile(args.pdf):
        sys.stderr.write(f"error: PDF not found: {args.pdf}\n")
        return 2

    rep = lint_pdf(args.pdf, margin_pt=args.margin_pt)
    if args.log:
        if not os.path.isfile(args.log):
            sys.stderr.write(f"error: log not found: {args.log}\n")
            return 2
        lint_log(args.log, rep, overfull_pt=args.overfull_pt)
    if args.render_dir:
        paths = render_pages(args.pdf, args.render_dir, args.dpi)
        # note in report
        rep.add(
            "warning" if False else "warning",
            0,
            "RENDERED",
            f"wrote {len(paths)} page images at {args.dpi} dpi under {args.render_dir}; inspect every page",
        )
        # that would always be a warning which is messy — just print
        # Actually don't add as issue. Print separately.

    text = format_report(rep, args.pdf, args.log)
    if args.render_dir:
        text += f"\nRendered {rep.pages} pages at {args.dpi} dpi → {args.render_dir}\n"
    sys.stdout.write(text)
    if args.out:
        os.makedirs(os.path.dirname(os.path.abspath(args.out)) or ".", exist_ok=True)
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(text)
    return 1 if rep.n_error else 0


if __name__ == "__main__":
    sys.exit(main())
