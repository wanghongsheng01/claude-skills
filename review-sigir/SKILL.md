---
name: "review-sigir"
description: "Simulated ACM SIGIR (CCF-A / TH-CPL A) Program Committee final review protocol. Tailored to SIGIR's strict 9-page body + zero-appendix double-anonymous review format (acmart sigconf,anonymous=true,review=true), query-level distribution-free paired randomization tests (>= 10,000 permutations) with Holm-Bonferroni family-wise correction and exact p-values, cross-artifact PYTHONHASHSEED determinism guards (main table == sensitivity sweep at default hyperparameter), Decimal ROUND_HALF_UP sub-millisecond latency & anti-rounding-paradox audits, judge-blindspot slot-counter attribution, 180 DPI two-column equation-tag checks, and wipe-first /tmp cleanroom artifact verification. Use alongside write-sigir."
---

# Simulated ACM SIGIR Program Committee Final Review (`review-sigir`)

Use after `write-sigir` and before submission to **ACM SIGIR** (International ACM SIGIR Conference on Research and Development in Information Retrieval).

## 1. Official Desk-Reject & SIGIR Format Gate (0 Tolerance)

- **Template & Strict 9-Page Cap**: Official ACM `acmart` with `\documentclass[sigconf,natbib=true,anonymous=true,review=true]{acmart}` (review line numbers enabled; `acmart.cls` and `ACM-Reference-Format.bst` bundled flat for Overleaf), **strictly <= 9.0 pages main body** (excluding references), **strictly 0 appendix pages**.
- **Double-Anonymous Compliance**: Zero author names, affiliations, personal GitHub links, identifying acknowledgements, or PDF `/Author` metadata leaks.
- **Native SIGIR Style**: Crisp natural-prose closing sentences per experiment subsection—**zero** database-engineering `\textbf{Takeaway.}` stamps, zero AI clichés, zero em-dashes, `0%` un-upgraded arXiv citations where published versions exist.

## 2. Independent 3-Lens SIGIR PC Panel + PC Chair Meta-Review

1. **R1 — IR Modeling, Ranking Theory & Counterfactual Debiasing Referee**:
   - Scrutinizes ranking objectives, inverse-propensity / outcome-debiasing estimators, normalization operators, and proofs for **degenerate boundary cases** (e.g., clipped propensity lower bounds guaranteeing nonzero denominators, and all-zero candidate-pool fallbacks in min-max/norm operators).
   - Audits **IR Community Relevance & Operating Regimes**: verifies crisp connection to core IR evaluation/ranking problems and honest crossover analysis showing where simple relevance rankers suffice in low-bias regimes vs. where counterfactual/outcome-aware rankers dominate.
2. **R2 — IR Evaluation Methodology, Query-Level Significance & Determinism Referee**:
   - Enforces **Query-Level Distribution-Free Significance + Multiple-Testing Correction**: rejects raw NDCG/MAP/MRR gains or bare `$p < 0.05$` tags; requires **`>= 10,000` paired sign-flip randomization permutations** (alongside paired $t$-test) with **Holm–Bonferroni** (or Benjamini–Hochberg) family-wise correction and **exact corrected $p$-values** across BOTH main comparison tables AND supplementary/LLM reranker tables.
   - Enforces **Cross-Artifact Determinism Guard**: asserts `abs(main_table[default_param] - sweep_curve[default_param]) < 1e-6`—catching `PYTHONHASHSEED`-induced drift whenever vocabularies/features are built from unsorted Python `set()`s feeding randomized SVD or tie-breaking rankers.
   - Enforces **`Decimal(..., ROUND_HALF_UP)` & Sub-Millisecond Latency Accounting**: bans `0.000 s` rounded latency rows (use `ms` to 2 decimals), computes every speedup ratio strictly from unrounded raw means, verifies bold-best / underline-second ranks on printed strings, and validates **judge-blindspot** divergences using slot-level ground-truth counters rather than hand-waving.
   - Checks **Multi-Collection & Public-Data Generalization**: ensures headline conclusions hold on public IR collections independently of any proprietary log slice.
3. **R3 — Outside-Area Generalist, 180 DPI Typography & Wipe-First Artifact Referee**:
   - Inspects every rendered page at **180 DPI PNG** for wrapped equation tags `(k)` in narrow `sigconf` columns, scatter/Pareto label-marker collisions, figure-vs-prose symbol drift (`figure_formula_consistency_audit.py`), `Overfull \hbox`, and clean page-9 transition into `References`.
   - Runs **Wipe-First `/tmp` Cleanroom Verification**: copies `reviewer_repo/` to `/tmp`, runs `rm -rf results/*.json *.pdf`, then executes `bash run_all.sh` (`exit 0`), proving every metric, 10k Holm–Bonferroni test, and theorem check recomputes cleanly from lightweight anonymized slices with `0` leaks.
4. **PC Chair Meta-Review**:
   - Consolidates into prioritized **Blocking / Major / Minor** cures so zero methodological, statistical, or reproducibility weaknesses survive into PC discussion.

## 3. Top-8 SIGIR Rejection Triggers (Symptom -> PC Pushback -> Pre-Submission Cure)

| # | Rejection Trigger | Typical SIGIR PC Pushback | Concrete Pre-Submission Cure |
|---|---|---|---|
| **T1** | **Cross-table/figure drift at default hyperparameter** | "Table 4 reports `0.7136` at `\tau=0.20`, but Fig. 4(a) plots `0.6873` at the exact same `\tau=0.20`!" | Sort all vocabulary/feature/candidate sets deterministically (`sorted()`), unify table & sweep execution under one deterministic driver, and assert `< 1e-6` agreement. |
| **T2** | **Uncorrected / missing query-level significance** | "Only paired $t$-test without multiple-testing correction, and the 6-LLM reranker table has no $p$-values at all." | Run `>= 10,000` paired randomization tests + Holm–Bonferroni correction across ALL comparison tables (main & LLM/reranker) and print exact adjusted $p$-values. |
| **T3** | **`0.000 s` latency illusion & rounding-ratio paradox** | "Deterministic baselines print as `0.000 s`, making claimed speedups unverifiable from Table 5." | Report cross-order latencies in `ms` (2 decimal places: e.g., `0.02–0.76 ms` vs. `1819.90+ ms`) and compute speedups strictly from unrounded means. |
| **T4** | **IEEE-754 `.x5` rounding & wrong underline** | "`0.2375` rounded down to `0.237` via Python banker's rounding and shifted second-best underline." | Standardize all table/figure formatters on `Decimal(..., ROUND_HALF_UP)` and auto-verify best/second-best marks against raw JSONs. |
| **T5** | **Unstated degenerate-pool & denominator guards** | "What if `Norm(C)` encounters an all-zero candidate pool or unclipped zero propensity?" | State exact clipping lower bounds (`\tau_clip > 0 => w_\tau >= 1`) and zero-variance pool fallbacks (`Norm = 0`) right beside the defining equations. |
| **T6** | **Unexplained LLM-judge vs. outcome divergence** | "Text judges prefer the baseline while outcome metrics prefer your method—are you gaming metrics?" | Quantify the unobservable blindspot using Top-$K$ slot-level empirical counters (e.g., unverified/stale share vs. true outcome hit rate). |
| **T7** | **Narrow-column equation wrap & missing `review=true`** | "Eqs. (1)/(6)/(8) drop `(k)` to blank lines, Pareto labels touch markers, and line numbers are off." | Split wide equations into clean two-line `align`, nudge label offsets on 180 DPI inspection, enable `review=true`, and hold `<= 9.0` body pages + `0` appendix. |
| **T8** | **Cache-dependent artifact scripts** | "Deleting pre-saved JSONs causes `run_all.sh` to crash with `FileNotFoundError`." | Support full from-scratch recomputation from anonymized data slices inside `run_all.sh`, verified in `/tmp` after `rm -rf results/*.json *.pdf`. |

## 4. Last-Mile Pre-Submission Catch Patterns (Distilled from Real Final Reviews)

1. **`sorted()` Vocabulary & Matrix-Column Determinism Audit**: Check every TF-IDF / SVD / feature-hash / candidate-pool index for unsorted `set()` iteration; assert `main_table[default] == sensitivity_curve[default]` to `1e-6`.
2. **10K Paired Randomization + Holm–Bonferroni Across Every Table**: Include BOTH main LTR/IR baselines AND auxiliary LLM rerankers in exact family-wise corrected significance tests.
3. **Milliseconds (2 Decimals) for Fast-vs-Slow Latency Tables**: Never print `0.000 s` for sub-millisecond rankers; switching to `ms` makes both latency and exact unrounded speedup ratios immediately auditable.
4. **Two-Line `align` Audit at 180 DPI**: Inspect every numbered equation in ACM `sigconf` 3.3-inch columns to pull any wrapped `(k)` tag cleanly inline.
5. **Pareto Marker-Label Clearance Check (180 DPI)**: Inspect tight clusters of ablation/baseline diamonds on Pareto frontiers and fine-tune annotation offsets (`(dx, dy)`) so zero text touches markers.
6. **Enable `review=true` Line Numbers Before Final Page-Budget Check**: Turning on `review=true` slightly alters visual margin rhythm; confirm `body_pages <= 9`, `0` appendix, and `0 Overfull \hbox` *after* enabling it.
7. **Wipe-First `/tmp` Cleanroom Test**: Run `rm -rf results/*.json *.pdf && bash run_all.sh` in `/tmp` to guarantee zero hidden dependence on pre-shipped results.

## 5. Final Sign-Off Checklist
- [ ] `acmart` (`sigconf,natbib=true,anonymous=true,review=true`), strictly `<= 9.0` body pages, **strictly `0` appendix**, `0` TeX/Bib errors, `0` Overfull `\hbox`, `0%` un-upgraded arXiv citations.
- [ ] Cross-artifact determinism (`main_table[default] == sweep[default]`) verified to `1e-6`.
- [ ] `>= 10,000` paired randomization + Holm–Bonferroni exact $p$-values verified across ALL comparison tables.
- [ ] `Decimal(..., ROUND_HALF_UP)` zero-drift audit & sub-ms `ms` latency accounting verified against `results/*.json`.
- [ ] 180 DPI visual proofread passed (`0` wrapped equation tags, `0` Pareto label collisions, `0` figure-formula mismatches, `0` non-SIGIR `\textbf{Takeaway.}` stamps).
- [ ] Wipe-first `/tmp` cleanroom run of `bash run_all.sh` passes (`exit 0`) with `0` leaks.
