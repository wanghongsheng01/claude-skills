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
