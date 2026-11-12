# Recipes (generator side)

Fix causes in the table/figure **generator**, then regenerate. Never hand-edit a generated number. After regeneration, diff every cell against the previous table: only marks, units in headers, a count row, and agreed rounding may change.

## Marks and count rows (A1–A2)

- Rank on the formatted string (`mark(vals, fmt)`), so `1.0` and `1.04` that both print as `1.0` tie.
- Bold rank 1, underline rank 2; ties share the mark.
- A `Best/2nd` row counts, per method column, how many comparison cells are best and how many are second. Skip non-comparison columns (ids, *n*, evals, speedup-vs-self).
- Keep the count in the same script as the table. Put the same macros in the abstract, contributions and standing sentences.

## Precision and units (B1–B2)

- One formatter per metric: costs one decimal or a stated rule ("one decimal below 1,000, integer with thousands separators above"); ratios two decimals; percentages one decimal.
- Put the unit in the **column header**. Convert a mixed-unit column to one unit; do not leave "5.4k µs" next to "189 µs."
- Prose may use a coarser formatter than the table ("8.8 million" not "8,789,090×").

## Fonts and palette (B3–B4)

- Times / Times New Roman / Nimbus Roman, 8–9 pt, `mathtext.fontset = stix` (or the body math font). Verify in the PDF that the font is not DejaVu Serif.
- Colour-blind-safe (Okabe–Ito or equivalent). Our method: one highlight colour, solid line, markers. Baselines: dashed/dotted, no markers, or hollow markers.
- Pick the chart that shows the claim: cost–quality Pareto, heatmap, CDF, small multiples. A validity-only scatter that hides a cost advantage must be redrawn.

## Experiment-log tables (C1)

Replace a "Experiment / Result" prose table with a generated standing table: per experiment and baseline, counts of faster / on par / slower and a median ratio. If the log held a design-choice sentence, move that **one sentence** into the body so it is not lost.

## EAB title (D2)

Copy the official string, do not paraphrase. ICDE: prefix `[Experiment, Analysis, and Benchmark]`. VLDB: suffix `[Experiment, Analysis & Benchmark]`. Confirm on the live page.

## Public-data confirmation (E2)

One paragraph (or a takeaway) of the form: "The official / public X independently supports conclusions C1–Ck. The production result Y that does not appear on public data is reported as a fidelity ceiling / a portfolio-size lesson, not as a claim that holds only on private data." If a conclusion holds only on private data, do not offer it.


## Average row vs Best/2nd row (A5, 邓-会议)

The Best/2nd count row (A2) answers “how often are we first or second.” The **average (or geometric-mean) row** answers “when some datasets go up and some go down, what is the overall effect.” Add it when a first glance cannot tell. Do not average incomparable units. For ratios, prefer a geometric mean (already S06).

## Empty regions and anomalous aggregates (B6, 邓-会议)

If a scatter or cost plot has a large empty band, one sentence in the caption or the body must say why (all models concentrate on one dataset; a method is undefined in that range; a filter removed points). If a plotted mean looks inconsistent with the points, **check the data** before redrawing; a box plot is the fallback Deng asked for, not a decoration.

## Dataset-only tables (C4, 邓-会议)

Keep a dataset table if it also reports something the method produces (index size, signatures, build time, coverage). Delete it from the body if it is only a listing of public datasets taken from prior work.

## Figure 1 story marks (F4, 邓-会议)

In the architecture / running-example figure, a two-minute reader should see: (1) the gap vs prior work, (2) which blocks are this paper's contribution, (3) offline vs online, (4) where an LLM is involved (a small icon is enough), (5) a negative / refuse path if the method can refuse. Do not draw a strict pipeline arrow among modules that may run in parallel.

## Compact necessity figures (F5, B7, 邓-会议)

One row of small panels beats three large low-density figures. Captions stay 1–2 lines and do not restate the body. 95% CI bands are fine. Drop a module-ablation figure from the body if it does not earn its height against the venue page limit. If whitespace, overflow or text–graphics overlap make the figure look generated, tighten it or redraw by hand — do not ship the messy automated version.
