# Co-author review lessons (ICDE 2027 R2, collected 2026-11-10)

A senior co-author (a data-visualization and database researcher) read the near-final manuscripts of the
ICDE 2027 Round 2 portfolio. The papers were Ladder, TopUp, CertKP and Agent-RLS EAB; the same lessons
were then applied to AuthZ-Graph, ScopeCache, RateQ, Certify-Join, N1 EAB, Labeler EAB and Conserve. The
comments are not about the science. They are about what a PC member sees in the first two minutes, so a
reviewer should check them before anything else. Each comment below is paraphrased, followed by what the
official rules say and the fix applied.

## 1. Presentation comments and fixes

| # | Co-author comment (paraphrased) | Rule / evidence | Fix applied |
|---|---|---|---|
| P1 | "I cannot tell at a glance whether our method is good: nothing is bolded. Is it SOTA on most metrics, or at least second?" | Accepted ICDE papers mark winners. | Bold the best value and underline the second best, ranking by the *printed* value so that ties share the mark. Add a per-method count row ("Best/2nd") and one standing sentence per RQ ("best in X of Y, second in Z"). State each loss once, with its cause. |
| P2 | "Decimals are not unified in Tables 4/5/7." | — | Within a table, one metric has one number of decimals (e.g., all percentages to 1 decimal, all coverages to 2). Fix this in the table generator, not by hand. |
| P3 | "Units in Table 5 are mixed." | — | One unit per column (all ms or all s); put the unit in the header or caption. |
| P4 | "Fonts inside the figures are not unified." | — | Every figure uses the body font family (Times-like) at 8–9 pt. Regenerate all figures from one style file. |
| P5 | "Only line and bar charts; tiring. Other papers have good palettes and figures." | Accepted ICDE/PVLDB papers use Pareto scatters, heatmaps, CDFs and small multiples. | Use a colour-blind-safe palette with our method in one fixed highlight colour. Pick the chart type that shows the claim: a cost–quality Pareto scatter for trade-offs, a heatmap for two factors, a CDF for latency distributions. |
| P6 | "Fig. 3 and Fig. 1(a) do not show our advantage." | — | Every figure must carry a claim. Redraw a validity-only plot (e.g., coverage dots) as cost versus coverage with the nominal line, so that the method is visibly cheapest while valid. Start each caption with the takeaway. |
| P7 | "This table looks like an experiment log, an unprocessed intermediate product." | — | Turn it into a summary that answers one question (e.g., counts of best/tie/behind per scenario), or move it to the artifact or a technical report. |
| P8 | "Tables 1 and 9 are mostly missing data ('–'); no need to show them." | — | Turn a prior-work comparison with many "–" cells into a ✓/✗/partial matrix or one paragraph. Drop rows or columns that are mostly empty. |
| P9 | "The title does not convey what the method name means." | Accepted ICDE titles: "Name: what it does over what". | Make the title explain the name's mechanism (e.g., "...by Topping Up Samples..."). |

## 2. Scope and venue questions, answered from the official ICDE 2027 pages

| # | Question | Official answer (ICDE 2027 CFP, https://icde2027.github.io/cf-research-papers.html, read 2026-11-10) | Action |
|---|---|---|---|
| V1 | Should "[Experiment, Analysis, and Benchmark]" appear in the title? | "The title of an EAB paper should start with the tag ... the tag will be removed in the CR of accepted EAB papers." | Keep the tag at submission; drop it in the camera-ready version. |
| V2 | Should the notation table and the algorithms go to an appendix? | "No appendix is allowed." Only references and the AI acknowledgment are outside the 12 pages. | Compress the notation table into prose or 4–5 rows; keep the algorithms in the body (standard for ICDE graph papers) with tighter pseudocode; put long proofs in a public technical report. |
| V3 | Does ICDE always put related work last? | No rule. In 21 deep-read accepted papers, LLM and theory papers mostly place it after the experiments, while problem-driven papers and EAB papers place it right after the introduction. | EAB: move related work to Section II. Research papers: either placement is fine. |
| V4 | "All LLMs are Chinese models (Kimi, DeepSeek, GLM); an international venue may call the experiments insufficient." | No rule, but "the strongest or newest system is missing" is a top rejection reason for benchmark papers. | Add at least one international vendor (GPT, Claude). Send only public or de-identified data through third-party channels. Report each channel in its own column, and name the model ID, channel and date in the paper and the artifact. |
| V5 | "The production dataset cannot be released; that will be attacked." | EAB: all artifacts are mandatory. Regular papers must explain in the submission form why an artifact cannot be released. | The main conclusions must stand on public data alone. Enterprise data is supplementary evidence, released as de-identified statistics, a generator or recomputable aggregates. |
| V6 | "No need to mention the companion paper in related work." | Only overlap with *published* work must be cited. | Cite a concurrent submission once where it is needed. Do not give it its own paragraph. |

## 3. Reviewer checklist (run before the science review)
- [ ] Every results table marks best/second; has a Best/2nd row where space allows; each RQ states the standing.
- [ ] Decimals unified per metric within each table; one unit per column.
- [ ] All figures share the body font and size, use one palette, and highlight our method in one colour.
- [ ] Every figure and table carries a claim. The caption starts with the takeaway; no experiment-log tables;
      no mostly-"–" tables.
- [ ] The chart type matches the claim (Pareto, heatmap, CDF), not only lines and bars.
- [ ] The title explains the method name; an EAB paper carries the exact tag.
- [ ] No appendix; any "move to appendix" request becomes compress-or-technical-report.
- [ ] Papers that use LLMs cover at least one international vendor, with the channel and date stated.
- [ ] Conclusions hold on public data; enterprise data is supplementary.
- [ ] Companion submissions are cited once and have no dedicated paragraph; papers that are not submitted in
      the same round are not cited at all.
- [ ] Second round (skill `results-presentation-review`, `references/round2-lessons.md` there):
  - [ ] every visual feature is explained (empty bands, clusters, outliers);
  - [ ] near-ties are visible through the second-best underline;
  - [ ] box plots or percentile whiskers are used instead of mean bars on skewed strips;
  - [ ] ablation tables have a set-off average row;
  - [ ] a why/when sentence exists for every baseline that wins a row;
  - [ ] there is a where-it-wins / where-it-loses paragraph;
  - [ ] table captions are about 2 lines and open with the claim.

## 4. Worked case: CertKP (dynamic maximum k-plex, ICDE 2027 R2), fixes and pitfalls

The co-author's comments on this paper, verbatim in substance: Table 5 mixes units, Table 7 mixes decimals,
figure fonts differ, Table 6 reads like an experiment log, and Table 1 and Algorithms 1–2 belong in an appendix.
An earlier comment asked whether the method is SOTA on most metrics, or at least second. What was done, and
what was learned on the way:

| Comment | Fix applied | Pitfall found while fixing |
|---|---|---|
| Winners not visible (P1) | Bold/underline by printed value in all five result tables, a count row per table, one standing sentence per RQ, and standing macros (`\NumMainBest` of `\NumMainCells`) reused in the abstract, contributions and conclusion. Result: main table 61 best / 13 second / 0 third of 74 cells. | Rank on the printed value: two cells printed as 1.0 tie, even if the raw ratios differ. Generate the counts in the same script as the table, never by hand. |
| Mixed units (P3) | One time unit per column (µs); the absolute columns that only restated a ratio (slowest update in ms, static time in ms) moved to the artifact, leaving Avg (µs), ×ST and ×BX⁺. | **"k"/"M" suffixes look like a unit change** (5.4k µs next to 189 µs). Remove them; print integers with thousands separators instead. Dropping redundant absolute columns also freed the width needed for the longer numbers. |
| Mixed decimals (P2) | One rule for every table, implemented once in the generator: one decimal below 1,000, integers with separators above. Static solver times (4 ms to 2 h) use seconds with two decimals throughout. | Prose needs a different format from tables: "8,789,090×" in the abstract reads badly. Use a separate prose formatter (two significant digits, "8.8 million") for the text macros. |
| Figure fonts (P4) | All figures regenerated with Times at 8 pt (`font.serif` = Times New Roman/Times/Nimbus Roman, `mathtext.fontset` = stix, every tick, legend and label size set to 8). | matplotlib `font.family: serif` alone falls back to **DejaVu Serif**, not Times. Per-bar value labels at 5.5 pt had to become 8 pt; rotating them 90° kept them from colliding. |
| Experiment-log table (P7) | The two-column "Experiment / Result" table (26 rows of prose results) became a generated standing table: per experiment and baseline, the number of cells where CertKP is faster (ratio > 1.05), on par (0.95–1.05) or slower, plus the median ratio. Total row: 147 faster, 26 on par, 39 slower of 212. The script reads the facts printed by the analysis scripts, so the table is reproducible. | The replaced table carried design-choice evidence (region size vs. alternatives). Check what disappears with a removed table and move the essential sentence into the text (here: one sentence in the ablation RQ). |
| "Table 1 and Algorithms 1–2 to the appendix" (V2) | No appendix is allowed. Table 1 was not a notation table but a method-comparison table with the closest prior work; it became a "Differences from LazyMC" paragraph. Both algorithms stayed, with merged steps and fewer lines. | Read the table the comment points to before applying the generic fix. After editing algorithm2e pseudocode, look at the compiled algorithm: `\lIf{..}{.. \tcp*{..}}` produced an empty numbered line containing only ";". |
| Page budget | The full-width log table (one third of a page) became a one-column summary; the experiments text was cut from 3,630 to about 3,000 words; the body ends on page 12 again with the two-author block. | Recheck after every number refresh: a single extra line moved the conclusion onto page 13. |

Experiment-side lessons from the same revision (they decide whether the new tables are fair):
- **Paired reruns.** When many runs share a machine, start all methods of one table cell together, so each ratio
  compares runs made under the same load, and say so in the setup. Mixing batches from different nights made
  CertKP look slower than its baseline in several cells.
- **Merging capped runs.** A run stopped by a time cap reports a load-dependent number of processed updates.
  A merge keyed on (graph, k, stream, seed, tag, updates) silently keeps the old record. Merge again on the key
  without the update count, and count the unmatched new records.
- **Memory when pairing large runs.** Two billion-edge runs started together (48 GB + 51 GB on a 110 GB server)
  got one of them killed by the OOM killer (signal 9, no output record). Check the peak resident memory of
  each run before pairing them, and rerun the killed one alone.
