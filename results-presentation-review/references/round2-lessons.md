# Round-2 co-author review of Ladder (ICDE 2027 R2, 2026-11-11), lessons and worked case

The reviewer was a senior co-author, a data-visualization and database researcher, who read the version of
Ladder from before the 11-11 revision. The comments below are paraphrased in substance. Each is followed by the
rule it became and what was done or is still to do. The first round of comments (winner marks, decimals, fonts,
palettes, chart types, experiment-log tables, title, CFP facts) is in
`../../review-icde/references/coauthor-review-lessons.md`.

| # | Comment (paraphrased) | Rule | Status on Ladder |
|---|---|---|---|
| D1 | "In the cost-vs-quality figure, most of the middle is empty and the points pile up: Hate (triangles) at the bottom, Yelp and IMDB at the top. What does that mean? Explain it." | S09 | Fixed. The panel became three zoomed rows (IMDB, Yelp AVG, Hate) sharing the x-axis, so the empty band disappeared. Still worth adding one sentence in the text: easy datasets reach ρ² ≈ 0.8–0.87 for every labeler, while Hate stays ≤ 0.41. The gap is task difficulty, not missing data. |
| D2 | "Emo anger: the baseline is 451 and yours is 452. Smaller is better, so mark the second best too: bold the best, underline the second. Then almost all of yours are marked." | S03, S04 | Fixed. Every comparison table marks bold best / underlined second best by printed value and has a Cheapest/2nd count row (Table I: 14/5 of 20). |
| D3 | "The mean bar for the green method (Strat) looks odd: the points sit higher than the bar. Check the data, or use a box plot." | S08 | Data checked. Unsmoothed Strat has 7 configurations below 0.8 (sparse strata report zero variance), which pull the mean to 0.90 while most points sit near 0.95. The figure was replaced by cost versus coverage, with median-free percentile whiskers and the nominal line. |
| D4 | "Some datasets you win, some the baseline wins (0.48 vs 0.48, lost in the decimals). Strat looks strong. Discuss in which scenarios you are better and why, where it is better and why, and whether you are faster." | S07, S10 | Fixed in Overleaf 106c8aa (see 'Applied' below). Before that: RQ1 states the standing and the 3.5% worst case. Still missing: a dedicated paragraph that explains when Strat-shrink (single-surrogate stratification) beats a ladder (rare classes isolated by one labeler: Yelp 1-star, Amazon pos, Emo anger) and when MultiPPI or SRS win (LLM oracle priced like the labelers). It should also cite the planning time (milliseconds). |
| D5 | "In the ablation, some components increase cost and some decrease it; I cannot see which module helps. Add an average row." | S06 | The geometric-mean row already existed but was not seen. Lesson: set it off with a rule, name it in the caption, and quote it in the text ("stratified plans matter most: +9.1% on average"). |
| D6 | "Against one baseline you seem to lose. Discuss why. Not everything has to be best; all-best is not credible. What matters is discussing advantages and shortcomings, with takeaways." | S07, S10 | Same as D4. Every RQ already has a takeaway; the win/loss paragraph is the open item. |
| D7 | "Table captions are too long. Papers do not write such long headers." | S01, S02 | Fixed in 106c8aa: every table caption is at most 40 words and opens with the claim. Before that: Table I's caption has 126 words, and five other captions have more than 40 words. Move the protocol into Sec. V-A and open each caption with the claim. |

## Lint on Ladder
- Version reviewed in round 2: 26 warnings. These cover all of D1–D7 except D4/D6 for MultiPPI, plus S05 in Tables I and IV.
- Version 11-11 (Overleaf cdd4dcb): 14 warnings. These are the open S01/S02 captions (D7) and S07 for Strat-shrink, MultiPPI and SRS (D4/D6).

## Template sentences (adapt, never copy numbers without the summary script)
- **Standing (S04):**
  "X is the cheapest method in 14 of the 20 configurations (two tied) and the second cheapest in five; in the
  remaining one it is within 3.5% of the cheapest."
- **Why a baseline wins (S07):**
  "<Baseline> is cheaper on <rows>, where <mechanism: e.g., one labeler isolates the rare class in a few cells,
  so stratifying on it needs fewer oracle labels than any ladder>; X considers the same plan, but its 200-tuple
  pilot <cannot separate the two families / overrates a surrogate>, which costs <k%>."
- **Noise (S07):**
  "The difference is within one standard error of the mean cost over 200 runs (<k%>)."
- **Where it wins / loses (S10):**
  "X pays off most when <large tables / oracle much dearer than the labelers / a cheap labeler tracks the
  oracle>. A single-family baseline is preferable when <one plan family dominates and is known in advance>.
  Oracle-only sampling is preferable when <the oracle costs about as much as the labelers>."
- **Visual feature (S09):**
  "The gap between the clusters reflects task difficulty: on IMDB and Yelp every labeler reaches ρ² of
  0.80–0.87, whereas on Hate none exceeds 0.41."

## Applied (Overleaf 106c8aa, 2026-11-11): lint 14 warnings -> 0, body still on 12 pages
- **Evidence first.** Each why/when sentence uses numbers from existing runs or from a planning-only diagnostic on
  the same data:
  - the plan family Ladder chooses on 60 pilots (Yelp 1-star: stratified in 57; Amazon pos: a two-labeler bundle in 38);
  - the pilot's labeling cost under the LLM oracle ($0.26–0.76, which is 16–64% of the total, so SRS, which labels
    the pilot with the oracle only, wins Yelp AVG);
  - the cheapest labeler's scan cost at 10^5 tuples ($0.84–2.05, so PPI++ wins two GROUP BY rows at 10^5 tuples and
    loses at 10^6).

  One reason that was not backed by data (enterprise rows) was dropped rather than guessed.
- **Verify every count against the table.** The first draft said "cheaper on six queries" where the table had four
  strict wins and three ties, and missed one row (Emo anger at 10^6). Recount from the printed values before writing.
- **Page budget.** Moving the protocol out of the captions into one setup sentence ("In every cost table, bold marks
  ... ; unless stated otherwise, every method meets its target") roughly paid for the new paragraph. The rest came
  from tightening the conclusion's list of extensions.
- **Checker fixes found while applying.** Header abbreviations ("Strat-shr.") now match the full name in the
  text, and claim verbs include "matter(s)", "help(s)" and "pay(s) off".
