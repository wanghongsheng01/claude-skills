---
name: results-presentation-review
description: "Senior co-author lens for the experiments section of a top-venue data-systems paper (ICDE, VLDB/PVLDB, SIGMOD, and their benchmark tracks): what a reader sees in the first two minutes of the figures and tables, and whether the analysis explains where the method wins AND where it loses. Rules from two rounds of a senior co-author's review of ICDE 2027 Round 2 manuscripts: every visual feature explained (empty bands and clusters in scatter plots), best bold and second best underlined so near-ties are visible, summary statistics that match the visual mass (box plots, not mean bars on skewed strips), ablation tables with a visible average row, win/loss discussion with mechanisms and takeaways, short table captions that open with the claim, unified decimals. Includes results_lint.py (rules S01-S10) that finds these defects in the LaTeX, figure scripts and figure PDFs, and a fix recipe per rule. Use automatically whenever an ICDE/VLDB/SIGMOD paper is written, reviewed, revised or prepared for submission (投稿前自审 / 合作者审稿 / 图表审查 / 结果分析 / 实验部分修改 / 消融表 / 优劣势讨论 / 表头太长), together with write-icde, review-icde, submit-icde and manuscript-writing-review."
---

# Results presentation review (senior co-author lens)

A PC member decides how much to trust the experiments from the figures, the tables and the text that comes
right after them. They do this before reading any proof. This skill collects what a senior co-author (a
data-visualization and database researcher) asked for in two review rounds of ICDE 2027 Round 2 manuscripts.
It turns those requests into rules S01–S10, a checker and a fix recipe for each rule.

It complements the other checks:
- `manuscript-writing-review` handles layout (cut-off labels, overlaps, tables past the margin);
- `manuscript-proofcheck` handles typesetting and the bibliography;
- `review-icde` handles the science.

Run this skill between those layout checks and the simulated science review.

## Language
- Fixes to the paper are made in formal academic English.
- The report to the author is written in the author's reporting language (Chinese for this author) and delivered as a document.

## Rules

| Rule | What the reader sees | What to do |
|---|---|---|
| S01 | A table caption that runs over many lines ("the header is too long; papers do not write captions this long") | Keep a table caption to about 2 lines, at most 40 words. Say what is measured, the unit, and how winners are marked. Move the protocol (runs per cell, oracle price, top-up rule) to the setup text and refer to it. A figure caption is at most about 60 words. |
| S02 | A caption that only says what is plotted | Make the first sentence the takeaway ("X is the cheapest method at every table size"). Then describe the axes, the encodings, and which direction is better. |
| S03 | A results table where only the best value is bold, and a near-tie (451 vs. 452) makes our method look like it lost | Bold the best and underline the second best, ranked by the *printed* value so that ties share a mark. Do this in the table generator. |
| S04 | The reader has to count wins by eye | Add a count row ("Best/2nd: 14/5") for each method, and give one standing sentence per RQ. |
| S05 | One column mixes 344 and 95.8, or a percentage column mixes 0% and +9.6% | Use one precision per metric in each table (costs 1 decimal, ratios 2, coverages 2 or 3, percentages 1). Fix it in the generator. Then check that only the rounding changed, by comparing every cell with the old table. |
| S06 | An ablation table where some cells go up and others go down, so it is unclear which component helps | Add a summary row (geometric mean for ratios, mean otherwise) and, if useful, the number of rows that improve. Set the row off with a `\midrule`, name it in the caption ("last row: geometric mean"), and quote it in the text. A summary row that exists but is not visually separated gets missed: in this review it was requested even though it was there. |
| S07 | Our method is second or third in some rows, and the text never says why ("if I were a reviewer I would want to know why you win here and lose there") | For every baseline that wins any row, write at least one sentence that names it and gives the mechanism and the scenario. Example: "Strat-shrink is cheaper on Yelp 1-star and Amazon pos, where one surrogate isolates the rare class in a few cells, so a stratified plan on a single labeler needs no ladder; Ladder includes that plan family and is within 3%, because its pilot sometimes prefers a control-variate plan." Also say whether the difference is within run-to-run noise. Never hide a loss, and never present a loss as a limitation of the whole method (no self-negation). |
| S08 | A strip plot with a mean bar that sits below where most points are ("the green mean line looks odd; check the data or use a box plot") | A few far-off points pull the mean away from the visual mass. Check the data first. Then show a box plot (median, IQR, whiskers) or median + percentile whiskers, or replace the plot with one that carries the claim (for example cost versus coverage, see S10). State the summary statistic in the caption. |
| S09 | A scatter plot with a large empty band, with all points stacked at the top or bottom ("most of the middle is empty; explain why") | Say in the caption and the text what separates the clusters. Example: "easy datasets: every labeler reaches ρ² ≈ 0.8–0.87; hard datasets: all stay below 0.41". Better still, plot one zoomed panel per group (small multiples sharing the x-axis), so that the gap no longer wastes space and the points are no longer crowded. |
| S10 | Every RQ lists numbers, but the section never says where the method helps and where it does not | Close each RQ with a takeaway, and add one "where it wins / where it loses" paragraph. That paragraph covers the scenarios (table size, price ratio, task difficulty, rare classes), the mechanism, and when a practitioner should choose the baseline instead. "All-best" results look unrealistic; an honest, explained loss raises credibility. |

Earlier presentation rules from the first round (winner marks, units, figure fonts and palette, chart type, no
experiment-log tables, title, CFP facts) are in `../review-icde/references/coauthor-review-lessons.md`. This
skill assumes them.

## Workflow
1. **Lint.** Run
   `python3 scripts/results_lint.py <paper_dir> --method <Name in the table header> --figscripts <scripts that draw figures>`.
   It reads `main.tex` with all `\input`s, the figure scripts, and the PDFs of the included figures. It needs PyMuPDF for S09.
2. **Look at every figure and table as a first-time reader.** For each one, write down three things:
   - the claim it should show;
   - whether a two-minute reader sees that claim;
   - any visual feature that is not explained (bands, clusters, outliers, a mean that sits off the points, a broken axis).
3. **Fix in the generator**, never in the generated `.tex` or `.pdf`:
   - captions;
   - winner marks and count rows;
   - decimals;
   - summary rows;
   - plot type;
   - panels.

   Regenerate everything and check that no value changed beyond rounding.
4. **Write the analysis**, using numbers from the summary script only:
   - the standing sentence per RQ (S04);
   - the per-baseline why/when sentences (S07);
   - the where-it-wins / where-it-loses paragraph (S10);
   - the explanations of visual features (S09).
5. **Keep the page budget.** Shorter captions (S01) usually pay for the added analysis. Recompile and run
   `manuscript-writing-review` and `manuscript-proofcheck` again.
6. **Report to the author**, as a document: each finding, the fix, the before/after numbers, and anything not fixed and why.

## Rule-by-rule recipes (generator side)
- **Marks and counts:**
  - rank on the formatted string (`mark(vals, fmt)`), bold rank 1 and underline rank 2;
  - a "Best/2nd" row counts per column;
  - keep the counts in the same script as the table.
- **Precision:** use one formatter per metric (`fmt_cost = "%.1f"`, `fmt_ratio = "%.2f×"`, `fmt_pct` with one decimal and sign).
- **Ablation summary:**
  - the last row is the geometric mean of variant/full (print as a signed percentage) after a `\midrule`;
  - optionally add "improves in k/n";
  - in the text, name the component with the largest mean effect and the largest single effect.
- **Strip/mean plots:** use a box plot or median + 10th/90th percentile whiskers; or a cost–quality scatter with one marker per method and percentile whiskers (a cost-versus-coverage plot with the nominal line).
- **Scatter with clusters:**
  - use small multiples with one row per dataset, each with its own zoomed y-axis, sharing the x-axis;
  - hollow markers for one vendor/class keep coincident points visible.
- **Line plots with many near-equal methods:** put markers only on our method (thick line, highlight colour); give the others distinct colour/line style without markers, so coinciding lines do not hide markers.

## Worked case: Ladder (cost-optimal semantic aggregation, ICDE 2027 R2)
See `references/round2-lessons.md`. It covers:
- the second-round comments on Ladder, in substance;
- the lint result before and after;
- the fixes applied and those still open when the skill was written;
- template sentences for S07/S10.
