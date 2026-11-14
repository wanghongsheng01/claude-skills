---
name: ccfa-figure-layout-review
description: "Use when making, reviewing or fixing figures, captions, tables and page layout for CCF-A database papers (SIGMOD, PVLDB, ICDE and siblings): hard red lines R1–R16 (arrows never cross boxes, lines never run over labels, legends never cover data, no clipped axis labels, no text-on-text overlap, fonts ≥ 6 pt printed, no overflow or placeholders) and style rules S1–S29 distilled from 26 accepted 2024–2026 SIGMOD/PVLDB/ICDE papers, plus a render+crop+lint script. The reviewer and the fixer must be different agents; loop review → fix → re-review until the reviewer reports 0 blocker and 0 major, and only then show the author. Use for 审图 / 改图 / 图注 / 表格版式 / 线穿框 / 图例压数据 / 轴标题被裁 / 叠字 / 页眉重叠 / figure review."
---

# CCF-A figure, caption, table and layout review

This skill holds the rules and the workflow for making figures in CCF-A database papers. It complements `pvldb-paper-craft` (whole-paper pipeline and PDF layout lint), `write-pvldb`, `write-sigmod` and `amp-figure-design`. It does not replace or edit them.

- Checklist (Chinese): `references/FIGURE_PRINCIPLES.md`. It has the 26 source papers with codes, R1–R16 with examples, S1–S29, the severity definitions and the reviewer steps.
- Scripts: `scripts/figlint.py` (render, crop and lint), `scripts/fontcensus.py` (lines below a font-size threshold, per page) and `scripts/montage.py` (stack crops into one image).

## 1. Roles: two different agents, looped

1. **Reviewer** (read-only). Reviews the latest **pdfTeX/Overleaf** PDF (S29: XeTeX/tectonic builds differ in fonts, line breaks and overfull boxes, so don't judge layout on them). Writes `reviews/<paper>_figreview_rN.md`. It never edits sources.
2. **Fixer** (a different agent). Applies the review item by item and recompiles. It never changes data or numbers (R16).
3. The reviewer runs round N+1 on the new PDF. **Deliver to the author only when the reviewer reports 0 blocker and 0 major.** Clear minors where cheap.

## 2. Red lines: any violation is a blocker

| | Rule |
|---|---|
| R1 | No arrow or edge may cross a box, node, label or legend. Route edges through empty channels using orthogonal paths (`-|`, `|-`), with return paths in their own outer channel. |
| R2 | No line may run over text. Put edge labels (yes/no) beside the line on white fill. Annotation lines, iso-curves and grid lines must not strike through point labels. |
| R3 | A legend never covers data: curves, bars, points, error bars or the plot frame. Default: outside the axes on top (`loc="lower center", bbox_to_anchor=(0.5,1.02), ncol=k`), one legend shared across panels. |
| R4 | Axis titles, ticks, legends and panel titles are never clipped and never cross the frame. Use `bbox_inches="tight"` and check the crop in the final PDF. |
| R5 | No text-on-text: running header versus venue line, labels, caption versus figure, adjacent panel ticks ("80" touching "0"). Crowded rotated tick labels that touch also count here. |
| R6 | The smallest printed font in a figure is ≥ 6 pt (target 7–8 pt). Draw plots at final width (3.33 in or 7 in). Never shrink TikZ with `\resizebox`. |
| R7 | No overflow into margins or the other column. Every Overfull \hbox > 1 pt in the log gets fixed. |
| R8 | No placeholders, TODO, "pending", TBD, ?? or undefined references. |
| R9 | Every axis has a title with units, and log scale is stated. |
| R10 | Never rely on colour alone, and never on red versus green. Add line style, marker or hatch so it survives grayscale. |
| R11 | Panels with different scales each carry their own y title. |
| R12 | Data labels don't touch bars, error bars, axes or each other. |
| R13 | No hyphenation inside a node, and no text overflowing a node. Use explicit `\\` breaks or a wider `text width`. |
| R14 | Arrowheads end on edge midpoints or evenly spread anchors, never on corners or on top of another edge, and are visible at print size. |
| R15 | No dangling nodes, or the caption says the node is an output. |
| R16 | Numbers in the figure, the caption, the tables and the text agree. Spot-check at least 3. |

Style rules S1–S29 (diagrams, plots, tables, captions, page layout) are in the checklist. The ones reviewers hit most:
- booktabs with no vertical rules (S16).
- Ragged-right p-columns with no stretched word spacing (S17).
- Best value bold and second-best underlined (S18).
- Tables ≥ 7 pt with no resizebox (S19).
- Caption first sentence = takeaway (S21).
- Figure font matches the body font (S8).
- Okabe-Ito colours (S7).
- Plots: horizontal bars instead of 45° crowded ticks (S10), and dodge or hollow markers for overlapping points (S14).

## 3. Reviewer workflow

```bash
pip install -r scripts/requirements.txt      # pdfminer.six, pillow; plus poppler-utils
python3 scripts/figlint.py main.pdf out/ --log main.log --dpi 200 --body-pt 9
#  out/pages/page-NN.png, out/crops/fig-N_pP.png, out/crops/tab-N_pP.png, out/lint.md
python3 scripts/fontcensus.py main.pdf 6.5   # lines printed below 6.5 pt, per page
python3 scripts/montage.py out/montage.png out/crops/fig-*.png
```

1. Read `lint.md`. It lists text-on-text overlaps (≥ 30% bbox intersection), text near the page edge, tiny text measured by printed glyph height, and overfull boxes. Treat these as leads, not verdicts. Accents and sub- or superscripts give false overlaps.
2. **Open every crop and every page at ≥ 150 dpi, then zoom to 300–400 dpi on each figure.** Check every edge (R1, R2, R14), every legend (R3), every axis (R4, R9, R10), every tick row (R5, S10), node text (R13), and table rules and wrapping (S16, S17, S19). Check the running header on every page (S25).
3. For each issue write: the **rule id**, the **exact location** (figure, panel, element, source file and line), the **severity** (blocker/major/minor), and a **concrete fix the fixer can apply without guessing**. For example: "move legend to `loc='lower center', bbox_to_anchor=(0.5,1.02), ncol=2`"; or "route (2)→(4) out of (2).north, up 4 mm, right, into (4).north at 1/3 width".
4. Header of the review: the commit and PDF reviewed, the counts by severity, and a page-layout verdict (overfull, overlaps, header).

## 4. Fixer recipes

- **TikZ pipelines.** Lay nodes on a `matrix` or grid with equal sizes. Use one main direction (left→right; snake only with an outer return channel). Use orthogonal edges on distinct anchors (`([xshift=…]a.north)`). Put labels on `fill=white, inner sep=1pt`. Use `font=\footnotesize` with no resizebox. Use `figure*` if it does not fit.
- **matplotlib.** Set `rcParams`: a serif family matching the body, 7–8 pt, final `figsize`. Put the legend outside on top. Use `bbox_inches="tight"`, `pad_inches=0.02`. Use Okabe-Ito colours plus hatch or markers. Put a visible "0" label on zero bars. Use barh for many categories. Draw major grid only on log axes.
- **Tables.** booktabs; `\cmidrule(lr)` for groups instead of `|`; `>{\raggedright\arraybackslash}p{}` for text; `\addlinespace`; split or use `table*` instead of shrinking.

## 5. Examples that triggered rules (anonymised)

- A pipeline figure in which two orthogonal edges ran through intermediate boxes (R1), with arrowheads on corners (R14).
- A CDF whose legend sat on the curves (R3). A bar chart whose legend overlapped the frame and the top bars (R3), with a clipped y title (R4) and 45° crowded ticks (S10/R5).
- A decision-flow figure whose "no" labels were struck through by routing lines (R2).
- A panel annotation that crossed an axis tick and spine (R2/R5). Iso-F1 curves that ran through point labels (R2).
- A node with "met-ric" hyphenated (R13). A visible "[pending: …]" cell in a table (R8).
