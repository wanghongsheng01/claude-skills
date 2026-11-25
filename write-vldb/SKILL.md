---
name: "write-vldb"
description: "Writing guide for PVLDB / VLDB research papers (CCF-A; PVLDB Vol. 20 and VLDB 2027). Covers official monthly deadlines (abstract on the 25th of the previous month, full paper on the 1st, 17:00 PT), the 12-page body limit including appendix and acknowledgements but excluding references, single-blind policy, the two-papers-per-author-per-month and twelve-per-year caps, and the requirement to submit an EA&B reproducibility package at initial submission when the paper is an experiment, analysis or benchmark contribution. Presentation rules are Deng S01–S11 and results-presentation-review. Title, abstract and introduction structure is still started from write-icde. Experiment-analysis paragraphs were updated on 2026-11-12 from a 12-paper PVLDB Vol. 17–19 reading; use sibling skill `experiment-analysis-writing` and `references/experiment-analysis-from-pvldb-2023-2026.md` (this file’s §§1–6 official constraints are unchanged; §7 is advisor meetings; §8 is the sample). Use when drafting, restructuring or polishing a paper for PVLDB or VLDB (写 VLDB / 写 PVLDB / Vol. 20 / EA&B 复现包 / 每月截稿 / 实验分析 / 第二名)."
---

# Writing for PVLDB / VLDB (Write-VLDB)

**Re-read the official pages immediately before every submission.** The rules below were checked on **2026-11-12**. If a page disagrees with this file, the official page wins.

- Important dates: https://www.vldb.org/2027/important-dates.html
- Research-track CFP: follow the links from that page (call-for-research-track / submission guidelines for the current volume).
- For ICDE-specific wording, page budgets or EAB title tags, use `write-icde`, `submit-icde` and `review-icde`. **Do not rewrite those skills.**
- For tables and figures, always also apply `results-presentation-review` (S01–S11) and, for English, `academic-latex-polish`.

**Update, 2026-11-12 (later the same day, additive):** experiment-analysis writing is now also grounded in a fresh reading of **12 official PVLDB Vol. 17–19 PDFs** (NL2SQL, semantic benchmarks, MV rewriting, k-plex, columnar EA&B). The list and the habits taken are in `references/experiment-analysis-from-pvldb-2023-2026.md`. Apply `experiment-analysis-writing` whenever you write the evaluation section. Title, abstract and introduction structure is still started from `write-icde` §§2–4 (measured on ICDE), not a VLDB frequency table. Official pages still win. **§§1–6 and `references/official-rules.md` are unchanged.** §7 (advisor meetings, added by a co-worker) and §8 (the 12-paper sample) are additive.

## Language
Manuscript, captions and reviews in **English**. Plans and reports to the author in **Chinese**.

## 1. Official constraints (Vol. 20 / VLDB 2027)

- **Monthly research cycle.** Abstract: 25th of the previous month, 17:00 PT. Full paper: 1st of the month, 17:00 PT. Convert to Beijing time when reporting to the author (PT + 16 hours in standard time; check DST). The last cycle that accepts **new** papers for VLDB 2027 was stated as **2027-03-01 17:00 PT** — confirm on the important-dates page, because the conference may stop accepting new work after a stated month.
- **Length.** Regular research papers: at most **12 pages** of body, **including** appendix and acknowledgements, **excluding** references. Use the official PVLDB / acmart template for the current volume (`vldbproceedings` / the volume’s posted class). Do not steal space with margin or spacing hacks.
- **Blindness.** Single-blind: author block is present. Still do not deanonymize **other** co-submissions or confidential enterprise data.
- **Author caps.** At most **two** papers per author per month, and **twelve** per year (confirm the exact wording on the current CFP; do not exceed it). Scheme A already books January and February slots — do not silently add a third paper in those months.
- **EA&B / reproducibility.** For experiment, analysis and benchmark papers, a **reproducibility package is due at initial submission**, not after acceptance. Declare the official EA&B label if the track requires it. The package must run on public data or a documented generator; enterprise dumps do not belong in the package.
- **Dual submission.** A manuscript under review at PVLDB must not also be under review at TKDE or another venue. After a VLDB reject, wait for the venue’s own resubmission rules.

## 2. Framing

PVLDB wants a **data-management** problem: a query or operator, a cost or correctness constraint, a guarantee or a clearly scoped empirical claim. Pure ML methods without a data-system interface are a poor fit. Industrial experience belongs in SIGMOD Industrial (`write-sigmod-industrial`) unless the contribution is a generalizable system or algorithm with public evidence.

## 3. Title, abstract, introduction

Follow `write-icde` §§2–4 as a starting structure (they were measured on ICDE, not VLDB):

- Title: technical paradigm or hard setting first; EA&B papers use the official label, not a homemade synonym.
- Abstract: context → shared false assumption → “We present X” → insight → 2–3 components → evaluation scope → 1–2 headline numbers with the **same wording** as the body. No citations. Do not put a loss sentence at the end of the abstract (Deng / write-icde limitations guide).
- Introduction: scenario with a concrete number; existing work and its shared assumption; Figure 1 as a real measurement that breaks the assumption; challenges C1–C3; mapping from challenges to components; 3 contributions with section numbers; the last contribution holds experiments and headline results plus artifact availability. Answer one obvious reviewer objection in the introduction.

## 4. Method and experiments

- Define inputs, constraints and the objective. If there is a guarantee, state it as a theorem or a checkable certificate; **do not use an LLM’s self-statement as a certificate**.
- Experiments: one subsection per RQ, each ending with a bold **Takeaway**. Required: main quality-and-cost table, where the method helps and where it does not (mechanism from counters, not guesses), ablation, other backbones **including GPT and Claude** when the paper uses LLMs, overhead. Say how many repetitions and report dispersion.
- Public data is the main table. Any conclusion drawn on non-public enterprise data must also hold on public data; say so and show it.
- Presentation: S01–S11 — claim-first captions; bold best / underline second; a count row; colour-blind-safe figures; keep every losing cell; explain losses once, in the experiment that measures them, as fact → mechanism → regime.

## 5. Related work, limitations, integrity

- 3–5 themed paragraphs; end each with how this paper differs. Actively declare relationship to the authors’ already-submitted papers (ICDE 2027 Ladder 2258, AuthZ-Graph 2034, Certify-Join 2052, N1 2066, and sibling PVLDB submissions in other months).
- Limitations: follow write-icde §9. No “where we fail” heading; no self-negation in the abstract or the conclusion; no hiding losses.
- AI-generated-content declaration: include if the volume requires it; state tools honestly.
- Never invent numbers, never drop a measured cell, never claim SOTA on a fixture the method was written against (see BindOrClarify v0.1: 100% on template rules is not a main-table result).

## 6. Workflow

1. Re-open the official important-dates and submission-guidelines pages; record the access date.
2. Check author monthly/yearly caps against other submissions in the same month.
3. Draft against the 12-page body budget; move only references beyond page 12.
4. If EA&B: finish the reproducibility package **before** the full-paper deadline.
5. Run `results-presentation-review` and `academic-latex-polish`; then a compliance pass (page count, template, AI declaration, artifact URL).
6. Enterprise traces stay out of the repo and the artifact; public generators and SHA-pinned downloads stay in.

## 7. Advisor meeting lessons for experiment analysis (additive, 2026-11-12)

This section is **additive**. It does not change §§1–6 or `references/official-rules.md`. Official PVLDB pages still win. Full quotes: `paper-presubmission-review/references/deng-meeting-lessons.md`. Run `paper-presubmission-review` and `ccfa-submission-workflow` before submitting.

- **Wins and losses by scenario.** If the method is better on some datasets and a baseline on others, discuss *why* and in which regime, with a takeaway. "All best is not realistic" and is not required (邓-会议). The loss must still have a mechanism from counters (already §4).
- **Average row** when a table goes up and down across datasets, in addition to the Best/2nd count row. Geometric mean for ratios.
- **Problem-necessity figures** (iterative repair plateaus, residual error) are welcome but compact: one row of panels, captions 1–2 lines, no body restatement. 95% CI bands are fine. Secondary module-ablation figures may leave the 12-page body if they do not earn their height. Appendix still counts toward those 12 pages.
- **Figure 1** should make the gap visible, mark this paper's contribution vs upstream work, offline vs online, and an LLM icon where an LLM is used. Empty plot regions need one sentence. A suspicious mean curve is checked or drawn as a box plot. Large whitespace or overlapping labels look "model-generated" — tighten or redraw by hand.
- **Do not** put a body table that only lists other people's datasets. Drop low-information figures rather than overflowing the 12-page body.
- Before the CMT/portal packet: page-by-page check of the Overleaf PDF against the local latest (`ccfa-submission-workflow`); declare related concurrent submissions (already §5).

## 8. Experiment analysis from a 12-paper PVLDB sample (additive, 2026-11-12)

This section is **additive**. It does not change §§1–7 or `references/official-rules.md`. Full recipes and English paragraph templates: `experiment-analysis-writing`. Paper-by-paper habit table and official PDF links: `references/experiment-analysis-from-pvldb-2023-2026.md` and `experiment-analysis-writing/references/pvldb-sample-2023-2026.md`. Advisor-meeting rules stay in §7 and `references/deng-meeting-experiment-analysis.md`.

- Structure the evaluation as RQs (Dawn of NL2SQL’s “Q2: Are LLM-based Models the Clear Winner?” is the model for refusing a blanket win). End each RQ with a bold **Takeaway**. Close with three to five numbered **Lessons** that contain a “because” and, where useful, a measurable regime (Zeng et al., Vol. 17: “When the NDV ratio grows larger (e.g., > 0.1), dictionary encoding becomes less effective”).
- First-place metric: name the *component*, the *problem* it targets, and the ablation row that returns the metric to the baseline when the component is removed (REDSQL’s “we attribute this difference to…” is legitimate only with that row). Lead with a numeric delta, then “This is because…” (Sphinteract, Vol. 18).
- Second-place or loss: four moves in one subsection — standing in numbers (winner bolded); why the winner is strong *here* (design or workload, a threshold if you have one); where ours is better; a practitioner **choice rule**. The cleanest published model is Hu & Miao, Vol. 19, “workload-feature → method-choice”. Evaporate (Vol. 17) reports a quality loss as a cost–quality crossover rather than hiding it. Ahmad et al. (Vol. 18, k-plex) report a technique that *hurts* for large *k*. If a baseline “wins” a metric by construction (always-answer systems have zero unnecessary clarifications), call it a protocol signature and point to the metric where that signature is costly; do not delete the cell.
- Captions in the sample are often descriptive; for this campaign, first sentence claim-first, second sentence the setting, 1–2 lines, no pasted tables (§7 and 邓老师). Failure-case figures may be named as such (Miao et al., “Rewriting Failure Case of Sys-B”).
- Related work in the sample is often §2, not uniformly last; PVLDB does not mandate a final related-work section. Sibling in-flight papers must be declared (official Vol. 20 rule, already §5), including BindOrClarify ↔ MetricSemBench.
- EA&B papers (MetricSemBench, Agent-RLS, CertSQL): official scientific contribution is insight, a new evaluation, or a workload characterization. Still apply the SOTA gate to any *method* the paper proposes, and ship the **full reproducibility package at initial submission**. Title suffix `[Experiment, Analysis & Benchmark]` (ampersand) in the PDF and in CMT.
