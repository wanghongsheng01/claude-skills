#!/usr/bin/env python3
"""Automated Vector-Figure Box-Overflow & Text-Overlap Auditor (`figure_overlap_audit.py`).

Uses PyMuPDF (`fitz`) to inspect compiled PDF figures directly in vector coordinates and catch:
  1. [FAIL] Horizontal text overflow past enclosing schematic boxes / callout frames
     (e.g., a math expression like `\\Pi^*(\\nu(D),\\nu(D'))` spilling across a FancyBboxPatch
     border and colliding with an incoming arrowhead).
  2. [WARN] Very tight horizontal box padding (< 0.8 pt) inside diagram nodes.
  3. [WARN] Axis-label collisions with numeric tick labels.

Usage:
  python3 figure_overlap_audit.py <figures_dir_or_pdf> [...]
Exit code 1 if any FAIL is detected.
"""

import re
import sys
from pathlib import Path
import fitz  # PyMuPDF


def audit_pdf(pdf_path: Path):
    fails, warns = [], []
    doc = fitz.open(str(pdf_path))
    p = doc[0]

    lines = []
    for b in p.get_text("dict")["blocks"]:
        for l in b.get("lines", []):
            txt = "".join(s["text"] for s in l["spans"]).strip()
            if txt:
                lines.append((fitz.Rect(l["bbox"]), txt))

    # Candidate diagram nodes / callout boxes (exclude full-panel axes frames)
    boxes = []
    for d in p.get_drawings():
        r = d["rect"]
        if (
            r.width > 20
            and r.height > 12
            and (d.get("stroke") or d.get("color"))
            and r.width < p.rect.width * 0.48
            and r.width < 160
            and r.height < 80
        ):
            boxes.append(r)

    for tr, txt in lines:
        cx, cy = (tr.x0 + tr.x1) / 2.0, (tr.y0 + tr.y1) / 2.0
        # Pick the tightest enclosing box containing the text center
        containing = [br for br in boxes if br.contains(fitz.Point(cx, cy))]
        if not containing:
            continue
        br = min(containing, key=lambda r: r.width * r.height)
        pad_l = tr.x0 - br.x0
        pad_r = br.x1 - tr.x1
        h_min = min(pad_l, pad_r)
        if h_min < -0.1:
            fails.append(
                f"[FAIL][{pdf_path.name}] Horizontal box overflow (L={pad_l:+.1f}pt, R={pad_r:+.1f}pt) "
                f"in {br.width:.0f}x{br.height:.0f}pt box: {txt!r}"
            )
        elif h_min < 0.8:
            warns.append(
                f"[WARN][{pdf_path.name}] Tight horizontal box margin (L={pad_l:+.1f}pt, R={pad_r:+.1f}pt) "
                f"in {br.width:.0f}x{br.height:.0f}pt box: {txt!r}"
            )

    # Check axis-label vs tick-label collision (shrink bboxes by 1.5pt to ignore CM mathtext whitespace/subscripts)
    tick_re = re.compile(r"^[+-]?\d+(\.\d+)?$")
    for i in range(len(lines)):
        r1, t1 = lines[i]
        if not tick_re.match(t1):
            continue
        # Skip single-digit subscripts embedded inside a formula box
        if any(br.contains(fitz.Point((r1.x0 + r1.x1) / 2, (r1.y0 + r1.y1) / 2)) for br in boxes):
            continue
        s1 = fitz.Rect(r1.x0 + 1.5, r1.y0 + 1.5, r1.x1 - 1.5, r1.y1 - 1.5)
        if s1.is_empty:
            continue
        for j in range(len(lines)):
            if i == j:
                continue
            r2, t2 = lines[j]
            if len(t2) < 8 or tick_re.match(t2):
                continue
            s2 = fitz.Rect(r2.x0 + 1.5, r2.y0 + 1.5, r2.x1 - 1.5, r2.y1 - 1.5)
            if s2.is_empty:
                continue
            inter = s1 & s2
            if not inter.is_empty and (inter.width * inter.height) > 6.0:
                warns.append(
                    f"[WARN][{pdf_path.name}] Tick {t1!r} overlaps label {t2!r} "
                    f"(area={inter.width * inter.height:.1f}pt^2)"
                )

    return fails, warns


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 figure_overlap_audit.py <figures_dir_or_pdf> [...]")
        sys.exit(2)

    pdfs = []
    for arg in sys.argv[1:]:
        p = Path(arg)
        if p.is_dir():
            pdfs.extend(sorted(p.glob("*.pdf")))
        elif p.suffix.lower() == ".pdf":
            pdfs.append(p)

    all_fails, all_warns = [], []
    print(f"=== Vector Figure Geometric Box-Overflow & Overlap Audit ({len(pdfs)} PDFs) ===")
    for pdf in pdfs:
        fails, warns = audit_pdf(pdf)
        all_fails.extend(fails)
        all_warns.extend(warns)
        for msg in fails + warns:
            print(" ", msg)
        if not fails and not warns:
            print(f"  [PASS] {pdf.name}: 0 box overflows, 0 tick-label overlaps")

    print(f"Summary: {len(all_fails)} FAIL(s), {len(all_warns)} WARN(s).")
    sys.exit(1 if all_fails else 0)


if __name__ == "__main__":
    main()
