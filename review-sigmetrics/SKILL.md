---
name: "review-sigmetrics"
description: "Simulated ACM SIGMETRICS / POMACS (CCF-A / TH-CPL A) Program Committee final review protocol. Tailored to POMACS journal-grade absolute quality and One-Shot Revision standards (acmsmall, <= 20 body pages, double-blind). Audits analytical modeling rigor vs. real non-stationary/correlated trace fidelity (diurnal rolling windows & Markov session-stickiness correction), modern caching/systems baselines (LFU/ARC/S3-FIFO/W-TinyLFU + Belady-MIN offline oracle + B/entry metadata accounting), statistical validity (95% CIs, warm-up sensitivity, LP/grid discretization convergence), Decimal ROUND_HALF_UP zero-drift table reconciliation, boundary-sentinel proof completeness, and native POMACS prose. Use alongside write-sigmetrics."
---

# Simulated ACM SIGMETRICS / *POMACS* PC Final Review (`review-sigmetrics`)

Use after `write-sigmetrics` and before submission to **ACM SIGMETRICS / *POMACS*** (*Proceedings of the ACM on Measurement and Analysis of Computing Systems*).

## 1. Official Desk-Reject & *POMACS* Format Gate (0 Tolerance)

- **Template & Page Cap**: Official `acmart` (`\documentclass[acmsmall,review,anonymous]{acmart}`), **strictly <= 20.0 pages main body** (sweet spot **18.5–20.0 pages**; References & optional Appendix follow page 20). Bundle `acmart.cls` and `ACM-Reference-Format.bst` flat for Overleaf portability.
- **Double-Blind Anonymization**: Zero author names, affiliations, personal GitHub handles, internal hostnames/ports, or PDF `/Author` metadata leaks.
- **Native *POMACS* Style**: Crisp analytical prose closings—**zero** database-engineering `\textbf{Takeaway.}` stamps, zero AI clichés, zero em-dashes, clean Halmos QED alignment (`proof_and_math_audit.py` `0 FAIL`), and `0%` un-upgraded arXiv citations where published versions exist.

## 2. Independent 3-Lens SIGMETRICS Panel + PC Chair Meta-Review

*POMACS* uses journal-grade absolute quality gates with **Accept**, **One-Shot Revision**, or **Reject**. Reviewers split cleanly across theory and measurement—a paper must satisfy BOTH camps:

1. **R1 — Analytical Modeling, Queueing & Optimization Theory Referee**:
   - Audits **Tractability vs. Realism**: refuses hand-waving claims like "a rolling window handles non-stationarity" without empirical error bounds; demands explicit quantification of model prediction error under (a) diurnal non-stationary arrival sweeps and (b) short-range temporal correlation / session stickiness (plus first-order effective-rate corrections).
   - Audits **Proof & Discretization Completeness**: verifies boundary sentinels for degenerate discrete extrema (e.g., $\psi_{\sigma(0)} = +\infty$ when $k^* = 0$), Lipschitz discretization error bounds for grid-based LP/DP solvers, and clean separation of assumptions from consequences.
   - Tests **Structural Insight Over Brute Force**: asks whether the closed-form analysis uncovers scaling laws, physical lower bounds (e.g., TTL-expiry miss floors), or optimality conditions that simulation alone would miss.
2. **R2 — Systems Measurement, Modern Baselines & Statistical Validity Referee**:
   - Performs **100% `Decimal(..., ROUND_HALF_UP)` Cell-by-Cell Reconciliation** across every breakdown table, 95% CI half-width, summary row, and prose number against raw `results/*.json` (specifically hunting for "headline updated, breakdown rows stale" drift).
   - Enforces **Modern Baselines + Offline Oracle + Metadata Accounting**: for caching/tiering papers, demands modern eviction policies (**LFU, ARC, S3-FIFO, W-TinyLFU**) alongside **Belady-MIN offline oracle** AND transparent **bytes/entry** metadata overhead—never LRU-only comparisons.
   - Enforces **Statistical Validity Four-Pack**: (1) multi-seed 95% CIs (using Common Random Numbers where appropriate), (2) explicit **warm-up period sensitivity** verification (proving steady-state convergence), (3) **solver/grid refinement convergence** verification, and (4) full parameter-space coverage with zero cherry-picking.
3. **R3 — Outside-Area Performance Generalist & 180 DPI Visual/Artifact Referee**:
   - Runs `figure_formula_consistency_audit.py` to guarantee every symbol printed inside figure annotations matches the final renamed notation in `main.tex` verbatim.
   - Inspects every modified and float-bearing page at **180 DPI PNG** for readable legends, uncluttered captions (`<= 28–30` words claim-first table captions clarifying summary-row definitions), float proximity (`|\Delta p| \le 1`), and crisp `<= 20.0`-page body fit.
   - Verifies **Cleanroom `/tmp` Execution from Scratch**: deletes pre-generated JSONs/PDFs inside `/tmp`, runs `bash run_all.sh`, and verifies every table, figure, and assertion reproduces verbatim with `exit 0` and zero leaks.
4. **PC Chair Meta-Review**:
   - Flags every gap that would otherwise trigger a **One-Shot Revision** (missing modern baselines, unverified non-stationarity/warm-up, stale table cells) as **Blocking** so it is fixed completely *before* initial submission.

## 3. Top-8 SIGMETRICS / *POMACS* Rejection & One-Shot Revision Triggers

| # | Rejection / Revision Trigger | Typical SIGMETRICS PC Pushback | Concrete Pre-Submission Cure |
|---|---|---|---|
| **T1** | **Stale breakdown rows vs. updated headline** | "Headline matches JSON, but Table 4 breakdown rows and 95% CIs differ from the code outputs." | Run an automated `Decimal(..., ROUND_HALF_UP)` cell-by-cell assertion script verifying `0` discrepancies across every table row, CI half-width, and prose percentage. |
| **T2** | **LRU-only comparison without modern policies or oracle** | "Why not compare against ARC, S3-FIFO, W-TinyLFU, and Belady-MIN, and report metadata bytes?" | Benchmark LFU, ARC, S3-FIFO, W-TinyLFU, and Belady-MIN under identical CRN seeds, tabulate `B/entry` metadata, and show how physical freshness floors limit even the offline oracle. |
| **T3** | **Unverified non-stationary & correlated arrivals** | "Your closed-form model assumes stationary IRM; real workloads have diurnal swings and bursty repeats." | Add lightweight diurnal sine-wave rolling-window validation (`< 1%` error) AND Markov sticky-session stress test showing naive IRM bias vs. effective non-repeat rate `(1 - p_rep)\lambda` correction (`< 1%` error). |
| **T4** | **Unproven warm-up & numerical grid convergence** | "How do we know 15K warm-up reached steady state and LP grid `G=40` isn't coarse?" | Run explicit warm-up sweep (`0–30K`, confirming `< 0.2%` miss / `< 0.1 ms` P99 drift) and grid-refinement sweep (`G=10..160`, confirming objective convergence + Lipschitz error bound). |
| **T5** | **Cross-media symbol drift after notation edits** | "Figure 1 labels `Rank by \phi_j/w_j`, whereas Section 5 Equation (21) defines `\eta_j(r)`." | Gate every revision with `figure_formula_consistency_audit.py` (`0 FAIL`) and re-render all vector PDFs from synchronized scripts. |
| **T6** | **Degenerate-case gaps in discrete optima** | "In Prop. 2, what if no positive index satisfies `\psi_{\sigma(k)} \ge \theta` so `k^*=0`?" | Explicitly define boundary sentinels (e.g., `\psi_{\sigma(0)} = +\infty`) and verify every edge case in theorem statements and proofs. |
| **T7** | **Ambiguous ablation summary rows / verbose captions** | "Does Table 6's bottom mean include the full system or only the 5 ablations?" | State exact summary-row scope inside crisp claim-first `<= 28`-word captions alongside bold-best / underline-second rules. |
| **T8** | **Artifact passes only with cached pre-built JSONs** | "Running `run_all.sh` only re-reads pre-shipped JSON instead of re-executing the new experiments." | Delete all pre-generated JSONs and PDFs inside an isolated `/tmp` copy and assert `bash run_all.sh` regenerates every experiment, figure, and table cleanly (`exit 0`). |

## 4. Last-Mile Pre-Submission Catch Patterns (Distilled from Real Final Reviews)

1. **Full-Grid `Decimal(ROUND_HALF_UP)` Audit**: Never spot-check only headline totals—mechanically diff EVERY row of EVERY sensitivity, scaling, and baseline table against `results/*.json` (including CI half-widths and sub-decimal P95/P99 values).
2. **Oracle-Anchored Physical Lower Bound**: Pairing Belady-MIN with modern L1 policies (`LFU / ARC / S3-FIFO / W-TinyLFU`) turns an engineering comparison into a deep *POMACS* systems-modeling finding whenever TTL/refresh physics impose an unavoidable miss floor.
3. **Diurnal + Sticky-Session Realism Pair**: Two compact robustness runs—piecewise rolling windows on a 16-window diurnal sine wave + Markov repeat-access correction `(1 - p_rep)\lambda`—preempt the #1 theoretical objection to IRM/Poisson cache models.
4. **Warm-Up + Solver-Grid Convergence Pair**: Quantifying both simulation warm-up stability and discretization-grid invariance takes seconds to run and closes the #1 statistical-methodology objection.
5. **Sentinel-Closed Discrete Extrema**: Audit every `\max\{0 \le k \le N : ...\}` or `\min` formula for empty-set / zero-index boundary sentinels (`\psi_{\sigma(0)} = +\infty`).
6. **Zero-Cache Cleanroom `/tmp` Rebuild**: Always test `reviewer_repo/run_all.sh` AFTER wiping pre-generated `.json` and `.pdf` artifacts inside `/tmp` to confirm genuine end-to-end reproducibility.
7. **Native *POMACS* 20-Page Closure**: Confirm `<= 20.0` body pages, `0` `\textbf{Takeaway.}` stamps, `0` AI clichés, `0` Overfull `\hbox`, and 180 DPI visual clarity on every modified page.

## 5. Final Sign-Off Checklist
- [ ] `acmsmall,review,anonymous`, strictly `<= 20.0` body pages, double-blind clean, `0` TeX/Bib errors, `0` Overfull `\hbox`, `0%` un-upgraded arXiv citations.
- [ ] 3-lens SIGMETRICS PC review + Chair meta-review completed; all Blocking/Major items cured at root cause.
- [ ] Zero cell/CI/prose discrepancies against `results/*.json` under `Decimal(..., ROUND_HALF_UP)`.
- [ ] Modern baselines + offline oracle + `B/entry` metadata + diurnal/Markov non-stationarity + warm-up & grid convergence verified in code and tables.
- [ ] `figure_formula_consistency_audit.py`, `proof_and_math_audit.py`, `float_proximity_audit.py`, `latex_table_and_cite_lint.py`, `ai_smell_audit.py`, and `master_8gate_audit.py` all pass (`0 FAIL / 0 WARN`).
- [ ] 180 DPI visual proofread passed and zero-cache `/tmp` cleanroom run of `bash run_all.sh` passes (`exit 0`) with `0` leaks.
