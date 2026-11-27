---
name: write-sigir
description: "ACM SIGIR (CCF-A / TH-CPL A) information retrieval, counterfactual learning-to-rank, review reranking, and bias-calibrated LLM evaluation paper craft distilled from accepted SIGIR 2024-2025 papers (Balog-Metzler-Qin SIGIR '25, Two-Stage CLTR, Self-Calibrated Listwise Reranking)."
---

# ACM SIGIR Paper Craft (`write-sigir`)

## 1. Official SIGIR 2027 Hard Guardrails
- **Format & Page Limit**: `\documentclass[sigconf,natbib=true,anonymous=true]{acmart}`, **strictly <= 9.0 pages main body** (excluding unlimited References; **strictly `0` appendix pages beyond the 9-page body**).
- **Double-Blind & Clean Typography**: Suppress hollow trailing `□` (`\AtBeginDocument{\providecommand{\qedsymbol}{}\renewcommand{\qedsymbol}{}\providecommand{\qed}{}\renewcommand{\qed}{}}`); zero em-dash chains (`<= 1.0/1K`), zero AI clichés; keep inline math in two-column proofs compact by promoting multi-term derivations to centered `equation`/`align` displays.

## 2. Five Signature Laws of Accepted SIGIR Papers

1. **Native IR Statistical & Closing Discipline (No Mechanical `Takeaway.` Stamps)**:
   - Report paired statistical significance tests (paired $t$-test / Fisher randomization test with Bonferroni correction, marked via superscripts) and multi-seed 95% CIs; close subsections with crisp natural IR prose rather than mechanical `\textbf{Takeaway.}` headers.
2. **Prevent LLM Judge Self-Preference Bias (`Leave-One-Family-Out` + Behavioral Ground Truth)**:
   - Follow *Balog, Metzler, & Qin (SIGIR '25)*: pair objective post-hoc behavioral/outcome signals (e.g., verified RMA defect outcomes) with **Leave-One-Family-Out (LOFO) heterogeneous judging**, and explicitly explain any row/metric where an oracle or judge variant edges out the proposed ranker (`Rule S07`).
3. **Propensity Clipping Sensitivity & Operating-Regime Crossover**:
   - Sweep inverse-propensity clipping $\tau_{\mathrm{clip}}$ (bias–variance frontier) and exposure/syndication skew, explicitly quantifying the **low-skew verified-only regime** where standard cross-encoder rerankers already approach optimal nDCG without counterfactual correction.
4. **Two-Minute Scannable IR Tables**:
   - Keep table captions `<= 28` words opening with the quantitative claim; unify decimal precision per metric column (e.g., 4 decimals for nDCG/MRR or 2 decimals for percentages); bold best, underline second-best, and separate ablation mean rows with `\midrule`.
5. **Reproducible IR Artifact**:
   - Include an anonymized artifact URL in Setup/Conclusion with full ranking evaluation scripts and de-identified query-document-outcome benchmarks.
