---
name: write-sigmetrics
description: "ACM SIGMETRICS / POMACS (CCF-A / TH-CPL A) stochastic performance modeling, queueing & TTL/Che cache analysis, delayed-hit vs. coalescing validation, and breathable acmsmall math typesetting guide distilled from accepted POMACS / SIGMETRICS 2022-2025 papers."
---

# ACM SIGMETRICS / POMACS Paper Craft (`write-sigmetrics`)

## 1. Official SIGMETRICS 2027 Hard Guardrails
- **Format & Page Limit**: `\documentclass[acmsmall,screen,review,anonymous]{acmart}`, **strictly <= 20 pages main body** (single-column *POMACS* layout, excluding unlimited References).
- **Breathable Single-Column Math**: With 20 `acmsmall` pages available, **never cram `\sum`, `\prod`, `\frac`, or 10+ compound formulas inline inside italic theorems or proof paragraphs!** Pre-define notation in upright Roman prose before `\begin{theorem}`, keep theorem statements `<= 7` lines, promote all multi-term expressions to centered `equation`/`align` displays, and suppress hollow trailing `□` (`\AtBeginDocument{\providecommand{\qedsymbol}{}\renewcommand{\qedsymbol}{}\providecommand{\qed}{}\renewcommand{\qed}{}}`).

## 2. Five Signature Laws of Accepted SIGMETRICS Papers

1. **Analytical-to-Simulation Fidelity (`< 2%–3%` Relative Error Across Skew & Burstiness)**:
   - SIGMETRICS reviewers judge theory by how tightly closed-form / fixed-point equations match discrete-event simulation (DES) and real traces across **Zipf popularity skew $\alpha$, arrival burstiness (Poisson vs. Markov-Modulated / bursty arrivals), and TTL jitter**.
2. **Account for Delayed Hits vs. Request Coalescing Under Contention**:
   - Following *Atre et al. (Delayed Hits)* and *POMACS* TTL cache network analyses: explicitly analyze what happens when concurrent queries arrive during an in-flight cache miss or batch refresh — contrasting **Uncoalesced Delayed-Hit Stampedes** against **In-Flight Request Coalescing + Jittered Stale-While-Revalidate**, validating both mean and P99 tail latency.
3. **Native *POMACS* Prose Style & Crisp Sentence Cadence**:
   - Keep mean sentence length in the **21–25 word** human *POMACS* range (never 30+ word run-on sentences), zero AI clichés (`strictly`, `expose`, `cleanly`, `importantly`), and natural analytical closing sentences (no mechanical `\textbf{Takeaway.}` stamps).
4. **Explicit Crossover Regimes (When Simple Caching or Direct Queries Suffice)**:
   - Quantify the exact structural crossover (e.g., shallow lineage depth $d = 1$, low fan-out, or ultra-high mutation rate $\mu \gg \lambda$) where direct metadata queries or plain LRU match slice caching without slice-maintenance overhead.
5. **Claim-First Captions & Unified Precision**:
   - Open every table/figure caption with the quantitative finding (`<= 30` words for tables) and enforce uniform decimal precision per metric column.
