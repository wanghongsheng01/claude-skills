---
name: "experiment-icde"
description: "From gap to validated idea to real experiments for an IEEE ICDE paper, especially LLM-for-data papers run on paid LLM APIs: gap -> falsifiable hypothesis -> pilot measurement (Figure 1) -> experiment matrix modelled on accepted ICDE papers (main result with cost, validity, when-it-helps sweeps, ablations, cross-model/vendor, extensions, overhead) -> label-once/replay-many design with cached calls and measured dollar costs. Includes a key-free cached multi-vendor LLM client and the complete example code of an ICDE 2027 submission (Ladder, cost-optimal approximate semantic aggregation). Use when designing or running experiments for ICDE (ICDE 实验设计 / 想 idea / 真实实验 / LLM API 实验)."
---

# Ideas and experiments for ICDE (想 idea 与做实验)

Builds on `read-icde` (gaps of accepted papers). Feeds `write-icde`. Example code in `scripts/example_ladder/` is the full pipeline of a real submission; `scripts/llm.py` is the client.

## Language convention
Experiment logs and reports to the author in **Chinese (中文)**; code comments, figures and paper text in English.

## 1. From gap to hypothesis
1. Start from a gap that several accepted papers leave open, tied to sections (e.g. "no LLM-for-data paper accepts a user accuracy target with a statistical guarantee": SPARQ Eq. 1 fixed threshold, ZenDB heuristic cost model, FusionSQL interval not delivered).
2. Search the last 12 months of arXiv/VLDB/SIGMOD for the nearest neighbours and write one line on what each assumes. The new paper should drop an assumption they all share (e.g. "one proxy, applied to every tuple").
   **Also search ML and statistics venues** (ICLR, NeurIPS, ICML, AISTATS, arXiv stat.ML) for the same estimator or allocation idea under another name. Ladder missed MultiPPI (ICLR 2026, budget allocation across subsets of predictors) until the second simulated review. Implement the closest such method as a baseline (Ladder: an MLBLUE/MultiPPI-style allocator over subsets of the skyline labelers), not just a citation.
3. Write the problem as input/output/constraint/objective and the hypothesis as something a measurement can refute.
4. Prefer an idea that admits a theorem (unbiasedness, variance or complexity bound, optimality) and has known methods as special cases: reviewers accept "we contain the baseline" more easily than "we beat it".

## 2. Pilot measurement before building
Measure the phenomenon the paper rests on (here: per-labeler accuracy, cost per 1k tuples, cross-validated rho^2 with the oracle, cross-vendor error correlation). This becomes Figure 1. If the pilot does not show the gap, change the idea.

## 3. Real LLM experiments: label once, replay many
- Call every model once per tuple, cache every raw response on disk keyed by the request hash, and log tokens; compute dollars from the vendors' list prices with the date (`label.py` PRICES). Restarting is then free.
- Store per-tuple predictions and costs (`results/labels/<task>__<labeler>.csv`). Methods are evaluated by replaying sampling plans hundreds of times on these labels (`simulate.py`), which gives coverage, variance and paired comparisons at no extra API cost.
- Larger populations can be built by resampling labelled tuples with replacement; state this in the paper.
- **Adaptive top-up must extend samples.** Take every sample (oracle draws inside strata included) as a prefix of one fixed random order, so the final round contains the earlier ones and charging the final round is exact. A reviewer who reads `rng.choice` per round will call the accounting unfair.
- **No cell may miss its target.** Give the planner a fallback so every configuration meets the user's error target: grow a stagnating stratified plan geometrically, and label the remaining tuples exactly once the oracle sample would exceed half of them. A table with † "missed the target" rows reads as a failed method; a fallback turns it into a cost number.
- Rate limits differ by vendor: batch several tuples per call (also a cheaper "physical labeler"), lower concurrency for strict vendors, retry 429s with backoff, and use a repair mode that re-runs only failed rows.
- Disable reasoning where a vendor allows it for cheap modes, and keep reasoning variants as separate labelers.
- Never put keys in the repository: the client reads `LLM_KEYS_JSON` (a chmod-600 file outside the repo). Respect the author's daily spending cap; log spend per model.

## 4. Experiment matrix (what accepted ICDE papers include)
| Block | Content |
|---|---|
| Setup | datasets (number, source, size), baselines incl. ICDE/VLDB/SIGMOD ones and the special cases of your method, metrics, cost unit and prices, hardware |
| RQ1 main | quality and cost in one table, every dataset/query, best per row in bold |
| RQ2 validity | guarantees hold (e.g. empirical coverage vs nominal, error distribution) |
| RQ3 when it helps | sweeps over the factors your theory says matter (table size, oracle price, error target); report weak regimes with their cause and a worst-case bound ("never more than X above the best plan"), not as failures |
| RQ4 variants | other oracle or backbone, other vendors |
| RQ5 ablation | remove each component; restricted catalogs |
| RQ6 extension | e.g. GROUP BY / multi-query |
| RQ7 overhead | planning time, pilot-size sensitivity |
Use >= 200 replays per cell, report mean and a dispersion measure, and keep a single script per table/figure.

## 5. Example (Ladder)
`tasks.py` (7 public datasets, semantic attributes), `label.py` (9 physical labelers from DeepSeek, GLM, Kimi; batching; cost), `ladder.py` (surrogates, nested control-variate estimator, closed-form allocation, chain search, GROUP BY convex allocation), `simulate.py` (replay harness and baselines SRS, PPI++, stratified), `experiments.py` (all experiment blocks). Run `python experiments.py main` etc.

## Final checklist
- [ ] Gap tied to accepted papers; nearest arXiv/VLDB/SIGMOD work listed.
- [ ] Hypothesis refutable; pilot measurement supports it.
- [ ] All LLM calls cached; costs from list prices with date; keys outside the repo.
- [ ] Every RQ block present; negative regions reported.
- [ ] One script and one CSV per number in the paper.

## Paired reruns on a shared server (from CertKP, ICDE 2027 R2)
- Start all methods of one table cell together, so every ratio compares runs under the same load; state this in the setup.
- Runs stopped by a time cap process a load-dependent number of updates: never merge new records on a key that includes that count.
- Check peak memory before pairing large runs; an OOM-killed run leaves no record and is easy to miss. Count records per job after every batch.
- Details: `../review-icde/references/coauthor-review-lessons.md`, section 4.
