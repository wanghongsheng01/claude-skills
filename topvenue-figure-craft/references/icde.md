# IEEE ICDE: observed figure profile

Sample (arXiv versions, acceptance from arXiv comments):
PURPLE: Making a Large Language Model a Better SQL Writer (ICDE'24 research, Fig. 1, 3);
DataLab: A Unified Platform for LLM-Powered Business Intelligence (ICDE'25, industry & applications track per secondary source, Fig. 1, 5);
S/C: Speeding up Data Materialization with Bounded Memory (ICDE'23 research, Fig. 1, 4, 5);
An Efficient and Effective Evaluator for Text2SQL Models on Unseen and Unlabeled Data (ICDE'26 research, Fig. 1, 2).

## Profile
- **The archetype depends on the track, but always serves the problem or insight.** Research papers use a failure-case table (three strong systems
  failing on the same question, with red/green spans), a before/after timeline sketch, or a top/bottom contrast. Only the industry/platform
  paper leads with a full-width overview with numbered zoom-in panels.
- **Single column** in research papers (about 250 pt, page-1 right column or page 2). The industry paper is full width.
- **Small text is the main defect** in IEEE layout: 4–6 pt figures against a 10 pt body. The best-looking figure (S/C) is TikZ in Times at 7 pt.
- **Semantic colour reused across panels:** three entity colours run through both a DAG and a timeline; agent types match cell types; red = wrong, green = gold.
- **Captions:** the strongest open directly with the point ("Our intuition: …", "Top: … Bottom: …"). Noun-phrase captions waste the slot.
- **Tools:** TikZ (best), LaTeX tables with pasted blocks, raster slides (visibly weaker), browser-based vector tools.

## Transferable practices
1. Research Figure 1: **strong baselines failing on the same real input, next to the gold answer**, with span-level red/green; or a before/after
   sketch on a shared axis that shows the insight.
2. The same entity keeps the same colour in structure and process views. At most 3–4 semantic colours.
3. Point at the contribution with 1–2 call-outs (a brace over the saved interval plus one mechanism phrase). Do not annotate everything.
4. In top/bottom contrasts, align "current" and "ours" rows exactly and replace one component. Give that component a unique shape and the accent colour.
5. Industry/platform papers: a full-width overview plus ①②③ zoom-in panels. The numbers appear on the overview anchors, the panel titles and in the text.
6. In protocol figures, write step numbers in the arrow labels; request and response are parallel arrows in opposite directions.
7. Text ≥ 7–8 pt in the body font. Check that figure and caption bounding boxes do not overlap.

## Avoid
Noun-phrase captions over a screen of identical boxes; clip-art; one colour used for both "problem" and "our result"; 4–5 pt annotations;
semi-transparent overlays carrying key information; raster figures; figures overlapping their captions; labels sitting on polylines.

## Lessons from a real Figure 1 redesign (industry track, authorization paper)
1. Standalone TikZ previews for IEEEtran must load `\usepackage[T1]{fontenc}` and `\usepackage{courier}`; IEEEtran typesets `\ttfamily` in the wider Courier, so a preview compiled with the narrower default typewriter font can pass the audit and then collide once embedded.
2. Use `anchor=base` for grid column headers so words with and without descenders sit on one baseline.
3. Under OT1, `\_` is drawn as a separate rule that a PDF audit reports as text-on-line; T1 encoding renders it as a glyph (check that no Type 3 fonts appear).
4. An A8 before/after matrix works for industry papers when paired with a flat 3–4 node deployment anchor on the left (25–30% width, no nesting), leaving about 70% of the width for the aligned grids and ending each grid with the production number.
5. Horizontal grouped bars pass the 2 pt clearance only when the gap between paired bars exceeds half the bar height plus about 0.08 and value labels sit 3–4% of the axis width beyond the bar end.
6. On log-scale line plots, place the annotation for a real production point in the whitespace to the right of the last data point, with a short horizontal arrow, instead of between curves.
