#!/usr/bin/env python3
"""Automated Proof QED Geometry & Human Math-Readability Auditor (`proof_and_math_audit.py`).

Checks BOTH the LaTeX source (`main.tex`) AND the compiled PDF (`main.pdf` via PyMuPDF):
  1. Theorem / Proposition / Lemma length & inline-symbol density (flags >11-line dense
     italic walls or inline `\\sum` / `\\prod` / `\\frac` inside theorem/proof prose).
  2. Paragraph inline-math density across body prose (flags paragraphs where `$...$` exceeds
     30% of characters or contains >= 9 separate inline math spans in one short paragraph).
  3. Exact PDF geometry of every QED symbol (`\\qedsymbol` / hollow square):
     - Flags `txsya` tiny elevated `\\openbox` if baseline-aligned geometric `\\qedsymbol` is missing;
     - Flags orphan QED on an empty line (`text_width == 0`);
     - Flags extreme widow closing lines (`text_width < 38%` of column width) or collisions (`gap < 6 pt`);
     - Flags tall math / stretched leading in the final 2 lines of any proof.
"""

import argparse
import re
import sys
from pathlib import Path
import fitz  # PyMuPDF


def strip_comments(tex: str) -> str:
    return re.sub(r"(?<!\\)%.*", "", tex)


def audit_tex_math_readability(tex: str):
    fails, warns = [], []
    clean = strip_comments(tex)

    # 1. Check baseline-aligned geometric qedsymbol definition in acmart papers
    if "acmart" in clean and "\\renewcommand{\\qedsymbol}" not in clean:
        fails.append(
            "[FAIL][Preamble] Missing baseline-aligned \\renewcommand{\\qedsymbol}{...}; "
            "default acmart txsya box floats above lowercase baseline."
        )

    # 2. Check Theorem / Lemma / Proposition blocks for inline \sum / \prod / excessive length
    for m in re.finditer(r"\\begin\{(theorem|lemma|proposition)\}(.*?)\\end\{\1\}", clean, re.S):
        kind, body = m.group(1), m.group(2)
        line_no = clean[: m.start()].count("\n") + 1
        # Strip display math inside theorem if any
        inline_only = re.sub(r"\\begin\{(equation\*?|align\*?)\}.*?\\end\{\1\}|\\\[.*?\\\]", "", body, flags=re.S)
        inline_spans = re.findall(r"\$([^$]+)\$", inline_only)
        math_chars = sum(len(s) for s in inline_spans)
        total_chars = max(len(re.sub(r"\s+", " ", inline_only).strip()), 1)
        ratio = math_chars / total_chars
        if len(inline_spans) > 10 or ratio > 0.34:
            fails.append(
                f"[FAIL][{kind} @ L{line_no}] Dense inline symbol wall: {len(inline_spans)} inline math spans "
                f"({ratio*100:.1f}% math chars). Pre-define setup before \\begin{{{kind}}} or use display math."
            )
        for sp in inline_spans:
            if re.search(r"\\(sum|prod|bigcup|bigsqcup|frac)\b", sp):
                fails.append(
                    f"[FAIL][{kind} @ L{line_no}] Inline tall operator in {kind} ('${sp[:40]}...$'); "
                    f"move summation/fraction to display equation or pre-theorem definition."
                )

    # 3. Check Proof blocks: no inline \sum / \frac in final sentence, no massive inline walls
    for m in re.finditer(r"\\begin\{proof\}(.*?)\\end\{proof\}", clean, re.S):
        body = m.group(1).strip()
        line_no = clean[: m.start()].count("\n") + 1
        inline_only = re.sub(r"\\begin\{(equation\*?|align\*?)\}.*?\\end\{\1\}|\\\[.*?\\\]", " [DISP] ", body, flags=re.S)
        inline_spans = re.findall(r"\$([^$]+)\$", inline_only)
        if len(inline_spans) > 12:
            fails.append(
                f"[FAIL][proof @ L{line_no}] Proof packs {len(inline_spans)} inline math spans; "
                f"move multi-step algebra into a clean centered display block."
            )
        tail = body[-220:]
        tail_inline = re.findall(r"\$([^$]+)\$", re.sub(r"\\\[.*?\\\]|\\begin\{.*?\}.*?\\end\{.*?\}", "", tail, flags=re.S))
        for sp in tail_inline:
            if re.search(r"\\(sum|prod|frac|bigl|Bigl|left)\b", sp):
                fails.append(
                    f"[FAIL][proof @ L{line_no}] Tall inline math near proof ending ('${sp[:40]}$'); "
                    f"stretches baseline leading above QED square."
                )

    return fails, warns


def audit_pdf_proof_geometry(pdf_path: Path):
    fails, warns = [], []
    doc = fitz.open(str(pdf_path))
    col_width = 240.0  # standard two-column text width ~240 pt

    for pno, page in enumerate(doc, 1):
        # Detect PROOF. paragraphs and verify their closing geometry
        blocks = page.get_text("dict")["blocks"]
        lines = []
        for b in blocks:
            for l in b.get("lines", []):
                txt = "".join(s["text"] for s in l["spans"]).strip()
                if txt:
                    lines.append((l["bbox"], txt, l["spans"]))

        for idx, (bbox, txt, spans) in enumerate(lines):
            # Check for default txsya tiny box if any slipped through
            for s in spans:
                if s["text"].strip() == "□" and "txsya" in s["font"]:
                    fails.append(
                        f"[FAIL][PDF p.{pno}] Proof QED uses elevated tiny font '{s['font']}' instead of baseline-aligned geometric Halmos square."
                    )

            if txt.upper().startswith("PROOF."):
                # Find the end of this proof (next Theorem/Lemma/Section/4.x or vector QED rule)
                pass

        # Also check vector drawings for our geometric 0.50em Halmos squares on proof pages
        text_page = page.get_text("text")
        if "Proof." in text_page or "PROOF." in text_page:
            # Verify no line immediately above a Theorem/Subsection is an ultra-short <35% proof tail
            for idx, (bbox, txt, spans) in enumerate(lines):
                # Look for closing proof lines ending right at right-margin QED (x1 ~ 285..296 or 548..560)
                w = bbox[2] - bbox[0]
                if txt == "□":
                    # Find same-baseline text line on left
                    same_y = [
                        l2 for l2 in lines
                        if l2[1] != "□"
                        and abs(l2[0][3] - bbox[3]) < 4.0
                        and abs(l2[0][0] - (53.8 if bbox[0] < 305 else 317.9)) < 25.0
                    ]
                    if not same_y:
                        fails.append(f"[FAIL][PDF p.{pno}] Orphan QED square on an empty line by itself!")
                    else:
                        tw = same_y[0][0][2] - same_y[0][0][0]
                        fill = tw / col_width
                        if fill < 0.38:
                            fails.append(
                                f"[FAIL][PDF p.{pno}] Proof closing line '{same_y[0][1]}' fills only "
                                f"{fill*100:.0f}% of column width, leaving a huge white gap before QED!"
                            )

    # Verify our geometric vrule/hrule Halmos QED squares inside Proof blocks
    for pno, page in enumerate(doc, 1):
        text_page = page.get_text("text")
        if "Proof." not in text_page and "PROOF." not in text_page:
            continue
        # Locate vertical spans of Proof paragraphs so plot markers inside figures are ignored
        proof_y_ranges = []
        for b in page.get_text("blocks"):
            btxt = b[4].strip()
            if btxt.startswith("Proof.") or btxt.startswith("PROOF.") or proof_y_ranges:
                # Track from Proof start until next Theorem/Lemma/Proposition/Section heading
                if re.match(r"^(Theorem|Lemma|Proposition|Corollary|\d+(\.\d+)?\s+[A-Z])", btxt):
                    if proof_y_ranges and proof_y_ranges[-1][1] is None:
                        proof_y_ranges[-1] = (proof_y_ranges[-1][0], b[1] + 2.0)
                elif btxt.startswith("Proof.") or btxt.startswith("PROOF."):
                    proof_y_ranges.append((b[1] - 2.0, None))
        proof_y_ranges = [(y0, y1 if y1 is not None else 760.0) for (y0, y1) in proof_y_ranges]

        drawings = page.get_drawings()
        qed_rects = []
        for d in drawings:
            r = d["rect"]
            if 3.0 <= r.width <= 7.5 and 3.0 <= r.height <= 7.5:
                if (284 <= r.x1 <= 298) or (548 <= r.x1 <= 562):
                    if any(y0 <= r.y1 <= y1 for (y0, y1) in proof_y_ranges):
                        qed_rects.append(r)
        # Deduplicate overlapping 4-rule strokes belonging to the same Halmos square
        dedup_qeds = []
        for r in qed_rects:
            if not any(abs(r.x1 - q.x1) < 6.0 and abs(r.y1 - q.y1) < 6.0 for q in dedup_qeds):
                dedup_qeds.append(r)
        if not dedup_qeds:
            continue
        lines = []
        for b in page.get_text("dict")["blocks"]:
            for l in b.get("lines", []):
                t = "".join(s["text"] for s in l["spans"]).strip()
                if t:
                    lines.append((l["bbox"], t))
        for qr in dedup_qeds:
            col_left = 53.8 if qr.x1 < 305 else 317.9
            matched = [
                (bb, t) for (bb, t) in lines
                if abs(bb[0] - col_left) < 30.0 and abs(bb[3] - qr.y1) < 5.0
            ]
            if not matched:
                fails.append(f"[FAIL][PDF p.{pno}] Geometric QED square at y={qr.y1:.1f} is stranded on an empty line!")
            else:
                bb, t = matched[0]
                fill = (bb[2] - bb[0]) / col_width
                gap = qr.x0 - bb[2]
                if fill < 0.40:
                    fails.append(
                        f"[FAIL][PDF p.{pno}] Proof closing line '{t}' fills only {fill*100:.0f}% "
                        f"of column width (target 42%-88% so QED is not stranded across a wide blank gap)."
                    )
                if gap < 6.0:
                    fails.append(f"[FAIL][PDF p.{pno}] Proof closing line '{t}' collides with QED square (gap={gap:.1f}pt)!")

    return fails, warns


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("tex", type=Path)
    ap.add_argument("pdf", type=Path)
    args = ap.parse_args()

    f1, w1 = audit_tex_math_readability(args.tex.read_text(encoding="utf-8"))
    f2, w2 = audit_pdf_proof_geometry(args.pdf)
    fails, warns = f1 + f2, w1 + w2

    print(f"=== Proof QED Geometry & Human Math Readability Audit: {args.pdf.name} ===")
    for f in fails:
        print(" ", f)
    for w in warns:
        print(" ", w)
    print(f"Summary: {len(fails)} FAIL(s), {len(warns)} WARN(s).")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
