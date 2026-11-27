---
name: write-icde-industrial
description: "Specialized IEEE ICDE Industry & Applications Track writing, experimental design, and reviewer-defense craft distilled from accepted ICDE 2022-2026 Industrial/Systems papers (Data Guard ICDE '26, Amazon Athena Fusion ICDE '22, BlendHouse ICDE '25) and adjacent FGAC/caching exemplars (Sieve PVLDB '20, Predicate Caching SIGMOD '24 Ind, Blockaid OSDI '22). Use alongside write-icde, review-icde, submit-icde, and results-presentation-review."
---

# IEEE ICDE Industry & Applications Track Acceptance Craft (`write-icde-industrial`)

## 1. Hard CFP & Track Guardrails (ICDE 2027 Industry)
- **Format & Page Limit**: `\documentclass[conference]{IEEEtran}`, **strictly <= 12 pages total including references (or per track CFP cap — zero Appendix allowed; 0 pages of Appendix)**. Redefine `\renewcommand{\IEEEQED}{}` so narrow columns never render hollow trailing `□` boxes.
- **Review Mode & Authorship**: **Single-blind**; requires `>= 1` non-academic industry co-author; mandatory unnumbered **AI-Generated Content Acknowledgement** immediately before References.
- **Abstract Budget**: **180–220 words** (published ICDE median ~203 words; never exceed 240 words or include negative self-limiting sentences).

## 2. Six Previously Uncodified Industrial-Track Acceptance Laws

1. **Formal Preliminaries + Named Theorems Inside Industrial Papers**:
   - Accepted ICDE industrial/systems papers do NOT skip formalization: include an explicit `Preliminaries and Problem Formulation` section defining catalog/schema state, workload, safety invariant, and latency/cost objective, plus **2–3 named `\begin{theorem}` blocks** with concise constructive `\begin{IEEEproof}` inline (since appendices are forbidden).
2. **Isolate Gains Against the "Strongest Safe Same-Catalog Baseline"**:
   - Never compare only against unsafe/unfiltered execution or broken legacy scripts. Always evaluate against the strongest *safe* alternative built over the *same* policy metadata: (a) **Per-App Materialized Safe Views** (quantifying view-count blowup & refresh cost) and (b) **Uncached Per-Call Policy Join / Dynamic Rewrite** (quantifying per-query control-plane RTT & SQL join overhead).
3. **Amortization Crossover ($q^*$) & Cold-vs-Warm Path Accounting**:
   - Follow *Sieve (PVLDB '20)* and *Athena Fusion (ICDE '22)*: report both cold-compile/miss latency and warm-snapshot latency, and compute the exact **queries-per-policy-update break-even threshold $q^*$** above which pre-compiled/snapshot-cached enforcement amortizes control-plane compilation.
4. **Positive Safety Vocabulary (Zero Self-Negating `fail` Triggers)**:
   - Avoid naming your own architecture headers or positive properties with `"Fail-Closed"` / `"Fail-Open"` or repeating `"fail"` in Abstract/Intro/Conclusion (which triggers self-negation detectors and negative framing). Use crisp positive systems terminology: **`Default-Deny Context Resolution`**, **`Zero-Leakage Scope Enforcement`**, **`Sound Tuple Projection`**, and **`Unauthorized Exposure Rate (UER)`**.
5. **Production Rollout & Shadow-Audit Path**:
   - Follow *Data Guard (ICDE '26)* and *Blockaid (OSDI '22)*: explain how enterprises migrate safely without breaking live traffic (e.g., **Shadow-Audit / Dual-Run Verification** logging policy diffs before enforcing hard rejection, plus HR-to-IM identity reconciliation).
6. **Two-Minute Table & RQ Craft (`results_lint` S01–S11 + 50+ Core DB Refs)**:
   - Every table/figure caption opens with the quantitative **takeaway claim** (`<= 30` words for tables); bold best, underline second-best, unify decimal precision per column; close every RQ with a bold **Takeaway** and dedicate one counter-backed paragraph to **Operating Regimes** (when database-native RLS suffices on single-app static schemas vs. multi-app high-churn gateways). Cite `>= 50` verified references with strong ICDE/PVLDB/SIGMOD coverage.
