---
name: "review-icml"
description: "Simulated ICML (CCF-A / TH-CPL A) OpenReview Program Committee & Area Chair final review protocol. Tailored to ICML's OpenReview pillars (Claims and Evidence, Soundness, Theoretical Assumptions, Impact Statement, Reproducibility) and strict 8-page main body + unlimited References/Appendix format. Audits line-by-line proof soundness (catching inverted ESS/weight bounds and data-dependent random-threshold concentration traps via deterministic upper-surrogate arguments), assumption-violation stress tests & 100-split risk/coverage quantile stability, Decimal ROUND_HALF_UP zero-drift table/figure parity, zero-shift crossover honesty, 180 DPI page-8 widow & sparse-tail checks, PDF /Author scrubbing after printAffiliationsAndNotice, and wipe-first /tmp cleanroom reproduction. Use alongside write-icml."
---

# Simulated ICML OpenReview PC & Area Chair Review (`review-icml`)

Use after `write-icml` and before OpenReview submission to **ICML** (International Conference on Machine Learning).

## 1. Official Desk-Reject & ICML Format Gate (0 Tolerance)

- **Template & Strict 8-Page Cap**: Official ICML cycle style (`icml2026.sty` / cycle-updated `icml2027.sty`, `icml*.bst`, `algorithm.sty`, `algorithmic.sty`, `fancyhdr.sty` bundled flat at project root for Overleaf), **strictly <= 8.0 pages main body** (excluding `Impact Statement`, References, and unlimited Appendix).
- **Mandatory Unnumbered `Impact Statement`**: Placed immediately after Conclusion and before References (exempt from 8-page limit); addresses societal impact honestly—including long-horizon deployment monitoring / human-audit caveats where relevant—never skipped.
- **Double-Blind & Hidden PDF `/Author` Scrub**: ICML templates can silently populate PDF metadata inside `\printAffiliationsAndNotice`; explicitly add `\hypersetup{pdfauthor={}}` afterward and verify PDF `/Author == ""`.
- **Native ICML Style**: Smooth academic prose closings—**zero** database-engineering `\textbf{Takeaway.}` stamps, zero AI clichés, zero em-dashes, clean QED box discipline (`\renewcommand{\qedsymbol}{}` or baseline-aligned Halmos square without hollow trailing tofu artifacts).

## 2. Independent 3-Lens ICML OpenReview Panel + Area Chair Meta-Review

ICML's OpenReview form centers on **Claims and Evidence**, **Soundness**, **Theoretical Assumptions**, **Significance**, **Clarity**, and **Impact Statement**:

1. **R1 — ML Theory & Proof-Verification Referee**:
   - Line-by-line checks EVERY inequality direction in main body AND Appendix—specifically hunting for two classic lethal theory bugs:
     1. **Inverted bounded-weight / ESS inequalities** (`W_{\min}` vs. `W_{\max}` flipped when bounding effective sample size $n_{\mathrm{eff}}$ or denominators);
     2. **Random-threshold concentration trap** (applying single-point Hoeffding/Bernstein directly to a data-dependent threshold $\hat\lambda$ without uniform convergence!). Require the clean **deterministic upper-surrogate proof**: apply single-point concentration at a deterministic $\lambda^+$, show $\lambda^+$ is feasible with high probability, and conclude $\hat\lambda \le \lambda^+$ by infimum/optimality definition.
   - Scrutinizes **Theoretical Assumptions**: checks whether relaxing restrictive assumptions from prior work is clearly demonstrated AND whether mild assumption violations (e.g., noisy indicators, imperfect weights) are empirically stress-tested rather than ignored.
2. **R2 — Empirical ML Rigor, Multi-Split Stability & Claims-vs-Evidence Referee**:
   - Performs **100% `Decimal(..., ROUND_HALF_UP)` Four-Way Reconciliation** (`prose == main tables == appendix tables == figure labels == results/*.json`), forbidding hardcoded numbers inside plotting scripts and eliminating IEEE-754 banker's rounding `.xx25/.xx75` drift.
   - Enforces **Assumption-Violation Stress Test + 100-Split Stability Distribution**: for risk-control / conformal / calibration methods, demands (a) a controlled assumption-violation gradient (e.g., `5%–20%` detector FN/FP) and (b) **100 independent random calibration/test splits** reporting mean, median, 90th percentile, and empirical target-satisfaction fraction $\mathbb{P}(\text{risk} \le \alpha + \epsilon)$ (never single-split cherry-picking).
   - Audits **Zero-Shift / Clean-Regime Honesty**: sweeps shift intensity starting from `0` and candidly reports any slight finite-sample slack (`< 0.3 pp`) under i.i.d. data plus the exact crossover threshold where the method dominates.
   - Verifies strict **calibration/test split isolation** (zero data leakage) and standalone public-benchmark validity.
3. **R3 — Outside-Area ML Generalist, 180 DPI Typography & Wipe-First Artifact Referee**:
   - Inspects ALL rendered pages (main body AND Appendix) at **180 DPI PNG** to eliminate: (a) a 1–2 line widow spilling onto Page 8 right column before `Impact Statement`, (b) a 2–4 line sparse trailing Appendix page, (c) narrow-column wrapped equation numbers or `Overfull \hbox`, and (d) figure-to-prose symbol mismatches (`figure_formula_consistency_audit.py`, banning STIX `\setminus` in plot scripts).
   - Exploits ICML's unlimited Appendix generously: breaks dense walls of inline proof math into crisp 3–5 line prose paragraphs paired with centered `equation*/align*` blocks.
   - Runs **Wipe-First `/tmp` Cleanroom Execution**: deletes ALL pre-generated `.json` and `.pdf` outputs inside `/tmp`, executes `bash run_all.sh`, and verifies `exit 0` with identical reproduced numbers and `0` identity/path/secret leaks.
4. **Area Chair Meta-Review**:
   - Synthesizes OpenReview scores (`Soundness`, `Presentation`, `Contribution`, `Overall`) and flags any Claims-vs-Evidence gap or proof jump as **Blocking** before submission.

## 3. Top-8 ICML OpenReview Rejection Triggers (Symptom -> Reviewer Pushback -> Pre-Submission Cure)

| # | Rejection Trigger | Typical ICML Reviewer Pushback | Concrete Pre-Submission Cure |
|---|---|---|---|
| **T1** | **Proof jump: Hoeffding applied to random $\hat\lambda$** | "Appendix B applies single-point Hoeffding to data-dependent $\hat\lambda$ without uniform convergence; Theorem 2 is invalid." | Evaluate single-point concentration at a deterministic surrogate upper threshold $\lambda^+$, prove $\lambda^+$ is feasible with high probability, and deduce $\hat\lambda \le \lambda^+$ by infimum definition. |
| **T2** | **Inverted weight / ESS inequality direction** | "Using $W_{\min}$ gives the opposite bound on $\sum w^2$ and breaks Theorem 1(c)." | Derive direction step-by-step explicitly (`w_i >= W_min => \sum w^2 >= W_min \sum w => \sum w >= W_min n_eff`) and cross-check numerically with 10,000 Monte Carlo trials. |
| **T3** | **Unverified assumption-violation fragility** | "What if the shift/premise detector has 10%–20% FN/FP noise? Does your guarantee collapse?" | Run a controlled `5%–20%` FP/FN assumption-violation gradient stress test (`Table 8` / Section 4) proving graceful linear degradation and strong margin over standard baselines. |
| **T4** | **Small-seed risk means without 100-split quantiles** | "5–10 seeds don't show the tail distribution of finite-sample risk across calibration splits." | Evaluate 100 independent random splits reporting mean, median, 90th percentile, and $\mathbb{P}(\text{risk} \le \alpha + \epsilon)$ vs. baselines. |
| **T5** | **Stale Appendix tables / hardcoded figure numbers** | "Table 6 and Figure 3 disagree with the updated JSON by `0.001–0.01`." | Load ALL plot values directly from `results/*.json`, enforce `Decimal(..., ROUND_HALF_UP)` globally, and run an automated JSON↔TeX↔Figure assertion check. |
| **T6** | **Hiding i.i.d. zero-shift slack** | "Under zero shift, weighting shrinks ESS—why aren't you showing $\delta = 0$?" | Plot continuous shift curves starting at $\delta = 0$, state the minor clean-regime trade-off honestly, and show the immediate crossover threshold. |
| **T7** | **Page-8 widow / sparse tail page / `Takeaway` stamps** | "Conclusion leaves a 1-line widow above Impact Statement; Appendix p.17 has 3 lines; uses non-ICML bold Takeaway labels." | Tighten 4–6 words so Conclusion ends cleanly at Page 8 left-column bottom with `Impact Statement` aligned at right-column top, compact Appendix tables to eliminate sparse tail pages, and strip all mechanical `Takeaway` stamps. |
| **T8** | **PDF `/Author` leak or cache-only artifact script** | "PDF metadata isn't blank, or `run_all.sh` breaks once cached JSONs are deleted." | Add `\hypersetup{pdfauthor={}}` after `\printAffiliationsAndNotice{}`, verify `PDF /Author == ""`, and pass wipe-first `/tmp` cleanroom `bash run_all.sh` (`exit 0`). |

## 4. Last-Mile Pre-Submission Catch Patterns (Distilled from Real Final Reviews)

1. **Deterministic Upper-Surrogate Concentration Check**: Audit every proof that bounds an empirically selected hyperparameter/threshold $\hat\lambda$—never substitute random $\hat\lambda$ straight into a pointwise Hoeffding/Bernstein bound.
2. **Sign & Direction Audit on Bounded-Weight / ESS Steps**: Independently check every inequality involving $W_{\min}$, $W_{\max}$, and Kish ESS both symbolically and on 10,000 synthetic random weight vectors.
3. **100-Split Distribution + Noisy-Assumption Stress Block**: Adding one lightweight script covering `5%–20%` detector noise and 100-split risk quantiles resolves both `Theoretical Assumptions` and `Claims & Evidence` objections simultaneously.
4. **Zero-Hardcoded-Numbers Figure Audit**: Inspect plotting code to confirm every plotted bar/curve reads directly from `results/*.json` using `Decimal(..., ROUND_HALF_UP)` and contains zero `\setminus` or stale draft symbols.
5. **Page-8 Column Balance & Appendix Tail-Page Polish (180 DPI)**: Visually inspect `page_08.png` (exact alignment of Conclusion & `Impact Statement`) and the final Appendix page (never leave a 2–4 line orphan tail page).
6. **Post-Notice PDF Metadata Scrub**: Always re-verify PDF `/Author` metadata *after* compiling with `\printAffiliationsAndNotice{}`.
7. **Wipe-First `/tmp` Cleanroom + Full-Style Overleaf Bundle**: Verify `icml*.sty`, `icml*.bst`, `algorithm*.sty`, `fancyhdr.sty`, and all vector PDFs live inside `overleaf_upload.zip`, and verify `/tmp` execution after deleting all pre-built `.json`/`.pdf` outputs.

## 5. Final Sign-Off Checklist
- [ ] Official ICML style (`icml*.sty` + `icml*.bst` + `algorithm*.sty` + `fancyhdr.sty`), strictly `<= 8.0` body pages, mandatory unnumbered `Impact Statement`, PDF `/Author == ""`, `0` TeX/Bib errors, `0` Overfull `\hbox`.
- [ ] Line-by-line proof verification completed (`0` inverted bounds, `0` random-threshold concentration jumps).
- [ ] Assumption-violation stress test + 100-split stability quantiles + zero-shift crossover verified against `results/*.json`.
- [ ] `Decimal(..., ROUND_HALF_UP)` four-way parity (`prose == main tables == appendix tables == figures == JSON`) passed with `0` discrepancies.
- [ ] 180 DPI visual proofread of all pages passed (`0` Page-8 widows, `0` sparse tail pages, `0` figure-formula mismatches, `0` non-ICML `\textbf{Takeaway.}` stamps).
- [ ] Wipe-first `/tmp` cleanroom run of `bash run_all.sh` passes (`exit 0`) with `0` leaks.
