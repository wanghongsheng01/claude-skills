---
name: "review-ijcai"
description: "Simulated IJCAI (CCF-A / TH-CPL A) two-phase Program Committee & Senior PC (SPC) final review protocol. Tailored to IJCAI's Phase-1 summary-reject filter (no rebuttal), Phase-2 PC/SPC/AC discussion, strict 7-page body + 2-page references limit (9 pages total, zero appendix), Pineau/IJCAI Reproducibility Checklist, general-AI significance framing, neuro-symbolic/global-vs-greedy optimality proofs, Decimal ROUND_HALF_UP precision reconciliation, weight-perturbation sensitivity sweeps, and 180 DPI narrow-column visual checks. Use alongside write-ijcai."
---

# Simulated IJCAI PC & Senior PC (SPC) Final Review (`review-ijcai`)

Use after `write-ijcai` and before submission to **IJCAI** (International Joint Conference on Artificial Intelligence).

## 1. Official Desk-Reject & 7+2 Page Gate (0 Tolerance)

- **Template & Strict 7+2 Page Cap**: Official `ijcai27.sty` (or cycle-matching `ijcaiXX.sty`) + `named.bst` bundled flat at project root, **strictly <= 7.0 pages main body** + **<= 2.0 pages references** (`<= 9` pages total, **strictly 0 appendix pages** in main submission PDF; supplementary material goes separately if allowed).
- **Double-Blind Anonymization**: Zero author names, affiliations, personal GitHub links, identifying acknowledgements, or PDF `/Author` metadata leaks.
- **Native IJCAI Style**: Clean academic prose closings per experiment subsection—**zero** database-engineering `\textbf{Takeaway.}` stamps, zero standalone `Limitations` top-level headings (weave honest operating regimes cleanly into the final experimental subsection), zero AI clichés, zero em-dashes, hollow trailing QED boxes suppressed (`\renewcommand{\qedsymbol}{}`).

## 2. Independent Two-Phase IJCAI Panel (Phase-1 Filter + Phase-2 PC/SPC/AC)

IJCAI uses **two-phase reviewing**: weak or unfocused papers are **summary-rejected in Phase 1 with NO author rebuttal**, while surviving papers advance to Phase 2 (`>= 3` PC reviews + rebuttal + SPC Meta-Review + AC calibration).

1. **Phase-1 Survival Filter (3-Minute General-AI Triage)**:
   - Tests whether Title + Abstract + Fig. 1 + Intro immediately establish **general AI/KR/planning/neuro-symbolic significance** (rather than reading like a narrow vertical business tool), plus crisp novelty, formal rigor, and convincing SOTA standing in 3 minutes.
2. **R1 — AI Theory, Neuro-Symbolic / Algorithmic Soundness & Boundary Referee**:
   - Scrutinizes every theorem, counterexample, and constraint-coupling edge case (e.g., global constrained decoding vs. greedy local masking—demanding BOTH a formal $\Omega(T)$ local-trap lower bound AND empirical trap rates on identical inputs; checking every fallback rule when interacting constraints collide, matching code line-for-line; verifying brute-force exact optimality on small instances).
3. **R2 — Empirical Rigor, Reproducibility Checklist & Sensitivity Referee**:
   - Enforces the **IJCAI Reproducibility Checklist five-tuple** cleanly inside 7 pages: (1) deterministic algorithm steps/pseudocode, (2) fixed random seed set, (3) all model/prior/regularization/API hyperparameters (`max_tokens`, temperature), (4) exact hardware & solver versions, (5) anonymous artifact mirror.
   - Audits **fixed-weight / scoring-formula sensitivity**: any fixed linear/routing weight must be backed by a multi-configuration weight/slope perturbation sweep showing conclusions do not hinge on fragile hand-tuning.
   - Runs **100% `Decimal(..., ROUND_HALF_UP)` Claim-to-JSON Reconciliation**: catches IEEE-754 banker's rounding `.x5` drifts AND **rounding-induced ratio paradoxes** (always compute ratios and pp deltas from unrounded raw counts/floats, never from already-rounded table cells!).
   - Verifies standalone **public-benchmark** strength alongside any domain benchmark, with multi-seed CIs and exact statistical significance ($p$-values).
4. **R3 — Outside-Area Generalist & 180 DPI Tight-Column Typography Referee**:
   - Inspects every single one of the 9 pages at **180 DPI PNG** for: (a) Abstract final-line overflow spilling under a top-right float on page 1, (b) wrapped equation numbers `(k)` in narrow 3.3-inch columns, (c) figure-to-prose symbol mismatches (`figure_formula_consistency_audit.py`), (d) font consistency (`8–9 pt` Times matching `ijcai.sty`), and (e) float proximity (`|\Delta p| \le 1`).
5. **SPC / AC Meta-Review**:
   - Evaluates **Novelty, Technical Quality, Significance, Clarity, and Reproducibility (`Convincing / Credible / Irreproducible`)**, issuing prioritized **Blocking / Major / Minor** surgical cures to fix before submission.

## 3. Top-8 IJCAI Rejection Triggers (Symptom -> PC/SPC Pushback -> Pre-Submission Cure)

| # | Rejection Trigger | Typical IJCAI PC/SPC Pushback | Concrete Pre-Submission Cure |
|---|---|---|---|
| **T1** | **Phase-1 summary reject (too domain-narrow)** | "Incremental application to one business vertical; limited interest to the broader AI community." | Frame Abstract & Intro opening sentences around the general AI/KR/neuro-symbolic/inference primitive first, then introduce the real-world domain as a rigorous testbed. |
| **T2** | **Unanswered "Why not greedy local masking?"** | "Why pay for global DP/ILP decoding when per-step masked argmax is simpler?" | Prove an explicit formal local-trap counterexample ($\Omega(T)$ irreversible regret) AND benchmark greedy masking on identical emissions showing exact trap rate and accuracy gap. |
| **T3** | **Constraint-interaction edge cases diverge from code** | "What happens when state-persistence collides with a unary mask? Your text omits the fallback." | Audit every interacting constraint pair in Section 3 against the implementation bit-for-bit, state the exact fallback transition & preconditions (e.g., $\bar{L} \ge 1$), and brute-force check 500 small instances. |
| **T4** | **IJCAI Reproducibility Checklist gaps** | "Seeds, solver versions, prior weights, or LLM `max_tokens` are missing; rating: Irreproducible." | Compress a crisp 4-line Experimental Protocol block reporting exact seeds, hyperparameters, solver/hardware versions, LLM sampling settings, and anonymous artifact URL. |
| **T5** | **Unverified fixed routing/scoring weights** | "The score weights look hand-tuned to this dataset." | Run a fast 9-configuration weight/slope perturbation sensitivity sweep (`results/v3_sensitivity.json`) confirming all perturbations stay in a tight accuracy band and significantly beat baselines ($p < 0.001$). |
| **T6** | **IEEE-754 `.x5` & rounding-ratio paradoxes** | "Sec. 4.2 writes `17.98x` (from `81.82/4.55`) while Abstract writes `18.0x` (`198/11`), and F1 differs by `0.001`." | Switch all table/figure generators to `Decimal(..., ROUND_HALF_UP)` and compute every ratio and pp delta strictly from unrounded raw JSON counts/values. |
| **T7** | **Figure-vs-prose symbol drift** | "Figure 1 shows `$s_3 = s_2$` which is never defined in Section 3." | Enforce `figure_formula_consistency_audit.py` (`0 FAIL`) and replace concrete toy step indices in schematics with the paper's general notation (`$s_t = s_{t-1}$`). |
| **T8** | **Tight 7-page visual glitches at 180 DPI** | "Abstract last line spills into right column under Table 1; Eq. (6) wraps its `(6)` tag onto a blank line." | Inspect all 9 pages at 180 DPI PNG: trim 4–6 words to keep Abstract cleanly inside left column, introduce compact notation (`p_s`) to pull wrapped `(k)` tags inline, and verify `7` body + `2` ref pages exact. |

## 4. Last-Mile Pre-Submission Catch Patterns (Distilled from Real Final Reviews)

1. **Unrounded-Source Delta & Ratio Enforcement**: Never subtract or divide printed rounded percentages (`81.82 / 4.55 = 17.98` vs. true `198 / 11 = 18.0`); compute every ratio and percentage-point gain from raw JSON counts/floats and round once with `Decimal(..., ROUND_HALF_UP)`.
2. **Constraint-Collision & Emission-Neutralization Verification**: Check persistence/stay steps in constrained DP/Viterbi models for (a) accidental emission noise leakage across stay steps and (b) explicit fallback transitions when stay constraints collide with unary feasibility masks—confirmed by `500/500` brute-force exact optimality checks.
3. **Lightweight 9-Point Weight Sensitivity Sweep**: A 10-second deterministic sensitivity script over 9 weight/slope perturbations eliminates "fragile hand-tuned hyperparameters" attacks in Phase-2 discussion.
4. **Page-1 Abstract Column Spill Check (180 DPI)**: In IJCAI's compact title header, an Abstract that runs 1–2 lines long silently wraps under a top-right Table 1—always check `page_01.png` at 180 DPI.
5. **Narrow-Column Equation Tag Pull-In**: Long square-root or multi-subscript formulas in `3.3 in` columns drop `(k)` below the equation with zero TeX warnings; pre-define a clean shorthand in prose (`p_s = ...`) to align `(k)` on the same line.
6. **Honest Operating-Regime Crossover Without Non-IJCAI Stamps**: Replace mechanical `\textbf{Takeaway.}` stamps with crisp natural academic prose quantifying the exact sequence-length/noise crossover where lightweight local baselines suffice vs. where global decoding dominates.
7. **Cleanroom `/tmp` Verification + Self-Contained Overleaf Zip**: Bundle `ijcaiXX.sty`, `named.bst`, `main.tex`, `refs.bib`, and all vector figures flat; verify `/tmp` compilation (`7+2=9` pages, `0` errors) and `/tmp` execution of `reviewer_repo/run_all.sh` (`exit 0`, `0` identity/path/secret leaks).

## 5. Final Sign-Off Checklist
- [ ] `ijcaiXX.sty` + `named.bst`, strictly `<= 7.0` body pages + `<= 2.0` ref pages (`<= 9` total, `0` appendix), double-blind clean, `0` TeX/Bib errors, `0` Overfull `\hbox`.
- [ ] Phase-1 general-AI significance & Phase-2 3-lens PC + SPC meta-review completed; all Blocking/Major items resolved at root cause.
- [ ] Full IJCAI Reproducibility Checklist five-tuple + weight-perturbation sensitivity sweep verified against `results/*.json`.
- [ ] `Decimal(..., ROUND_HALF_UP)` reconciliation passed with `0` rounding/ratio paradoxes and `0` figure-formula mismatches.
- [ ] 180 DPI visual proofread of all 9 pages passed (`0` Abstract column spills, `0` wrapped equation tags, `0` hollow QED boxes, `0` non-IJCAI `\textbf{Takeaway.}` stamps).
- [ ] Cleanroom `/tmp` execution of `reviewer_repo/run_all.sh` passes (`exit 0`) with `0` leaks.
