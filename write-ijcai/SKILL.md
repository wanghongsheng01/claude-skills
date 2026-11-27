---
name: write-ijcai
description: "IJCAI (CCF-A / TH-CPL A) neuro-symbolic & AI paper craft, strict 7+2 page-budget engineering, exact automata-guided vs. greedy masking analysis, and clean typography guide distilled from accepted IJCAI 2024-2026 papers."
---

# IJCAI Paper Craft (`write-ijcai`)

## 1. Official IJCAI 2027 Hard Guardrails
- **Format & Ultra-Strict Page Cap**: Official `ijcai27.sty` + `named.bst`, **strictly <= 7.0 pages main body + strictly <= 2.0 pages references = <= 9.0 pages total (`0` appendix pages in main PDF — exceeding 7 body pages or 9 total pages is automatic desk reject)**.
- **Double-Blind & Clean Typography**: Strict double-blind review; suppress trailing hollow `□` (`\AtBeginDocument{\providecommand{\qedsymbol}{}\renewcommand{\qedsymbol}{}\providecommand{\qed}{}\renewcommand{\qed}{}}`); zero em-dash chains (`<= 1.0/1K`), zero AI clichés.

## 2. Four Signature Laws of Accepted IJCAI Papers

1. **High-Density Native IJCAI Prose (Zero Wasted Boilerplate)**:
   - Under the 7-page body cap, never waste lines on repetitive `\textbf{Takeaway.}` headers or separate `Limitations` sections; weave concise 1-sentence analytical syntheses and operating-regime crossovers naturally into paragraph endings.
2. **Prove & Measure Why Greedy Local Masking Fails vs. Exact Global Automata Decoding**:
   - Neuro-symbolic IJCAI reviewers always ask: *"Why not just mask invalid next states greedily step-by-step?"* Provide both a crisp formal separation (showing myopic local masking gets trapped in dead-end or high-cost absorbing paths under noisy observations) and an empirical comparison against **Greedy Step-Masking** alongside unconstrained neural/LLM baselines.
3. **Dual Enterprise + Public Sequence Benchmarks & Audit-Budget Pareto**:
   - Pair noisy real-world operational streams (e.g., quoted reply chains) with standardized public sequence/workflow benchmarks; plot the **Pareto frontier of Human-Audit Budget (%) vs. End-to-End Accuracy** at certified `0.0%` invariant violation, and state the regime where unconstrained classifiers suffice (short 2-step linear threads without quoted history).
4. **Two-Minute Scannable Tables (`<= 28`-Word Claim Captions & Unified Precision)**:
   - Open every table/figure caption with the quantitative claim; unify decimal places within every metric column; bold best, underline second-best, and separate ablation mean rows with `\midrule`.
