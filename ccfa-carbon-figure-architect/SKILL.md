---
name: "ccfa-carbon-figure-architect"
description: "Unified Stage-2 figure reverse-engineering, critique, and vector redesign skill for both ACM SIGMOD (Research & Industrial) and PVLDB papers. Distilled from visual comparison of 13 published 2024-2027 SIGMOD and PVLDB papers (WAIR, Enzyme, AlayaDB, Measures in SQL, FinSQL, Data-Juicer, DIVER, SALUS, LOTUS, DocETL, FlockMTL, DAIL-SQL). Upgrades both system architecture schematics and multi-panel analytical/experimental plots: enforces theoretical-bound overlays, multi-scale invariance & sensitivity panels, cross-benchmark model matrices with strict international-venue neutrality (zero 'International/Domestic' banners or dividers), functional module names (zero port numbers), Okabe-Ito colorblind-safe vector styling, and 300-DPI dual-level visual verification."
---

# CCF-A Stage-2 Figure Architect: SIGMOD & PVLDB (`ccfa-carbon-figure-architect`)

While Stage-1 figure skills establish basic clean layout, **Stage-2 Figure Architecture** upgrades figures from *"clean descriptive charts"* to *"reviewer-convincing scientific proof visuals"* — matching the exact visual grammar of top-rated **SIGMOD Industrial/Research** and **PVLDB** papers.

---

## 1. Visual Reverse-Engineering: SIGMOD vs. PVLDB Figure Grammar

Detailed figure-by-figure comparisons appear in `references/SIGMOD_PVLDB_FIGURE_COMPARISON.md`. Key structural insights:

### A. System Architecture & Overview Schematics (Fig. 1 / Fig. 2)
| Aspect | SIGMOD Industrial Exemplars (`FinSQL` '24, `AlayaDB` '25, `Enzyme` '26) | PVLDB Exemplars (`LOTUS` '25, `DocETL` '25) | Unified Carbon Standard |
|---|---|---|---|
| **Primary Goal** | Show **offline-to-online governance/compilation boundary**, **multi-plane runtime isolation**, and **closed-loop production verification**. | Show **concrete tuple/document transformation through algebraic operators**, **plan rewrite / provenance check**, and **state output**. | Combine a **concrete mini query/tuple input** on the left, **spotlighted deterministic core** in the center, and **explicit Pass vs. Quarantine/Audit outcomes** on the right. |
| **Component Naming** | **Semantic functional roles ONLY** (`Unified MCP Gateway`, `Recursive Planner`, `Guarded SQL`, `Immutable Snapshot`). **ZERO internal port numbers (`4444`, `7211`) or cryptic version tags!** | **Algebraic operator names + symbols** ($\pi^{\text{sem}}_{\mathcal{G}}$, $\bowtie_{\text{asof}}$, $\sqcup$-View, Empirical-Bayes Router). | Every box title must tell a first-time reviewer *what the module does* in $\le 4$ crisp words. |
| **Visual Hierarchy** | 75–80% neutral slate/sand supporting planes; 20–25% Deep Navy (`#0B4F8C`) hero engine; Teal (`#0F766E`) `✓` vs. Vermilion (`#C2410C`) `⊘` outcomes. | Clean white/light-gray cards, operator pills, concrete schema/span highlights, dashed optimization/feedback loops. | High whitespace ($\ge 22\%$), crisp `0.8–1.3 pt` strokes, vector database cylinders & decision diamonds, 1-line bottom legend. |

### B. Multi-Panel Experimental & Analytical Figures (Figs. 2–4)
Why Stage-1 experimental figures look "thin" compared to `WAIR` (SIGMOD '26 Figs. 6–11), `AlayaDB` (SIGMOD '25 Figs. 5–11), and `LOTUS` (PVLDB '25 Figs. 5–8):
1. **Stage-1 plots show single-point descriptive bars; Stage-2 plots show *scaling laws, regime boundaries, and theoretical-vs-empirical agreement*!**
   - Example (SIGMOD Engine Latency & Scale Fig.): Instead of just 2 panels of fixed-size boxplots, use a **3-panel full-width `figure*` (`7.1 in × 2.35 in`)**:
     - **Panel (a)**: Cross-warehouse execution-path latency distributions (Enterprise vs. Public TPC-DS, P50/P95/P99).
     - **Panel (b)**: **Multi-Scale Estate Invariance & Hit-Ratio Sweep** (`36 → 105 → 500 → 1,599` tables across materialization hit ratios $\rho$), contrasting flat lineage-scoped planning (`< 20 µs`, matching Theorem 4.2's $O(1)$-in-$|T|$ bound) against super-linear unscoped schema search!
     - **Panel (c)**: End-to-end log-scale latency share (`< 0.001%` deterministic governance cost vs. `99.99%+` LLM parsing + SQL scan).
2. **Cross-Model Evaluation Plots MUST Obey Strict Model-Naming Neutrality**:
   - **FORBIDDEN**: Dividing x-axes with vertical dashed lines labeled `International (3)` vs. `Domestic (3)` or coloring bars by national origin!
   - **REQUIRED**: Order models systematically (e.g., monotonically by baseline Direct-SQL accuracy or grouped by open-weights vs. proprietary API / reasoning vs. non-reasoning ONLY if technically relevant — best is **clean monotonic or consistent benchmark order across all 6 named models** without geopolitical headers!), pairing **Public Benchmark** and **Enterprise Production** side-by-side (`figure*`) so cross-workload generalization jumps off the page!
3. **Overlay Analytical Predictions / Thresholds Directly on Curves**:
   - In PVLDB calibration/triage figures: annotate the **analytical cold-start crossover $N^*$** or **optimal budget knee $q^*$** directly with a crisp vertical dashed reference line and non-overlapping callout badge.
   - In SIGMOD drift/evolution figures: annotate **schema-drift velocity ($\lambda_{\text{break}}$)** and **Pareto dominance arrows** cleanly inside open canvas space.

---

## 2. Mandatory 8-Point Figure Review & Redesign Checklist

Run this checklist on **every figure** in the manuscript before submission:
1. **[Neutrality Gate]** Zero `International` / `Domestic` / `Intl.` / `Dom.` labels anywhere in titles, legends, axes, or callouts.
2. **[Zero Cryptic Codenames]** Zero internal port numbers (`7207`, `4444`), raw container names, or unexplained version strings (`v3`) without functional meaning.
3. **[Mechanism Over Flat Bars]** At least one multi-panel figure demonstrates **multi-scale scaling or analytical sensitivity** (sweeping table count $|T|$, sample size $N$, or budget $q$) validating a formal theorem or cost model.
4. **[Print Typography]** Designed at exact LaTeX target width (`7.0–7.1 in` for `figure*`, `3.33 in` for `figure`); all axis labels `8.0–9.0 pt`, ticks/annotations `>= 7.0 pt`, bold panel headers `(a)`, `(b)`, `(c)` aligned horizontally.
5. **[Colorblind & Grayscale Safety]** Okabe-Ito / restrained academic palette (`#0B4F8C` Navy, `#0F766E` Teal, `#D97706` Amber, `#C2410C` Vermilion, `#64748B` Slate) reinforced with distinct markers (`o`, `s`, `^`, `D`), line styles (`-`, `--`, `:`), or bar hatches (`//`, `..`).
6. **[Zero Visual Collisions]** Zero legend-curve overlaps, zero text-border collisions, $\ge 15\%$ headroom above max bar/error-bar for value annotations.
7. **[Exact Data Fidelity (`R16`)]** Every plotted point, bar height, and callout number is programmatically read from frozen experiment JSONs and matches `main.tex` prose/tables to the exact digit.
8. **[Rendered Page Inspection]** Convert both standalone figure `.pdf` AND the compiled `main.pdf` figure pages to 200+ DPI PNGs and visually inspect every panel via image reader.

---

## 3. Reference Files
- `references/SIGMOD_PVLDB_FIGURE_COMPARISON.md` — Visual comparison matrix and multi-panel matplotlib recipes distilled from 13 published SIGMOD & PVLDB papers.
