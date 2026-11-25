---
name: "ccfa-visual-table-ref-mastery"
description: "End-to-end visual, tabular, float-proximity, proof-formatting, and reference-verification mastery skill for ACM SIGMOD Industrial and PVLDB papers. Distilled from page-by-page reverse-engineering of 3 representative SIGMOD Industrial papers (FinSQL SIGMOD'24, AlayaDB SIGMOD'25, Enzyme SIGMOD'26 + WAIR SIGMOD'26) and 3 representative PVLDB papers (DAIL-SQL PVLDB'24, LOTUS PVLDB'25, DocETL PVLDB'25). Enforces five submission-critical gates: (1) Hero-spotlighted figures with embedded data/plan micro-structures, orthogonal non-crossing routing, and zero label/legend collisions (shared-y-axis matrices for multi-model plots), (2) Pure booktabs tables (zero vertical pipes '|', mandatory \\cmidrule(lr) under grouped headers, zero robotic filler rows), (3) Strict Float-to-Text Proximity (every Figure/Table/Algorithm on the exact page or adjacent column of its prose analysis), (4) Clean acmart/pvldb proof typography, and (5) Exhaustive reference verification (published venue over arXiv, complete author lists, zero arXiv DOIs on conference entries, pinpoint <=4-key citations)."
---

# CCF-A Visual, Table, Float-Proximity & Reference Mastery (`ccfa-visual-table-ref-mastery`)

Grounded in direct visual and structural reverse-engineering of **six representative published CCF-A database papers** (`references/EXEMPLAR_6PAPER_FIG_TAB_ANATOMY.md`):
- **SIGMOD Industrial (3)**: `FinSQL` (SIGMOD '24 Ind), `AlayaDB` (SIGMOD '25 Ind), `Enzyme` (SIGMOD '26 Ind), plus `WAIR` (SIGMOD '26 Research) for `acmart` proof typography;
- **PVLDB (3)**: `DAIL-SQL` (PVLDB '24), `LOTUS` (PVLDB '25), `DocETL` (PVLDB '25).

---

## 1. Deep Figure Architecture: How Top Authors Think & Build

### A. System / Algebraic Overview Figures (Fig. 1)
Why amateur architecture diagrams look "flat and generic" (6 white boxes each holding 3 lines of prose + diagonal crossing arrows) versus why `FinSQL` Fig. 1, `LOTUS` Fig. 2, `DocETL` Figs. 1–2, and `Enzyme` Fig. 4 command immediate authority:
1. **Embed Concrete Data/Plan Micro-Visuals Inside Every Hero Operator**:
   - Instead of writing *about* an operator in 3 lines of prose, draw a **compact visual micro-representation** of what it transforms:
     - *Tokenizer / Provenance*: draw a concrete byte-offset slice bar (`[0:44] current_reply ✓` in soft teal vs. `[45:92] quoted_history ✗` in muted coral);
     - *Temporal / Lineage Index*: draw a mini timeline or B-tree cutoff (`t_val, t_tx <= t_m` | `PO-99 future blocked ✗`) or 3-tier OneData path cards (`ADS 3.2 µs` / `DWS+DIM <=3-Hop 13.3 µs` / `Hybrid SUM(num)/NULLIF(SUM(den),0) 16.7 µs`);
     - *Algebraic State / Lattice*: draw the actual 5-node Hasse chain (`L1 -> L2 -> L3 -> L4 --[SampleGuard ⊘]--> L5`) or AST / delta tree (`ψ, ψ', Δψ` as in `Enzyme` Fig. 4).
2. **Spotlight Contribution vs. Commodity LLM/Storage**:
   - Render swappable black-box LLMs and external storage cylinders in **low-contrast neutral slate (`#F8FAFC` fill, `#94A3B8` dashed/thin border)**; render the paper's contributed deterministic engine in **crisp Deep Navy (`#0B4F8C`)** with numbered execution badges (`1`–`5` online, `①`–`②` / `A` offline).
3. **100% Orthogonal Non-Crossing Routing**:
   - Route pass/quarantine/recalibration channels along dedicated **outer perimeter buses** with $90^\circ$ elbows. **Zero diagonal arrows and zero lines cutting across other boxes or connectors.**

### B. Multi-Panel Experimental Plots (Figs. 2–4): Zero Crowding By Construction
1. **Shared-Y-Axis Horizontal Matrix Law for $\ge 6$-Model Comparisons**:
   - **Anti-pattern**: Squeezing two or three vertical 6-model bar charts side-by-side in one `7.0 in` row — multi-word x-tick labels (`DeepSeek V4`, `Qwen3.8 27B`, `Kimi K3.1`) inevitably collide horizontally, and numbers inside `0.12 in` bars turn illegible!
   - **Master Solution**: Place the $M$ model names **once** horizontally on the left y-axis (`sharey=True`) across 2–3 aligned columns (e.g., `(a) Enterprise Safety (%)` | `(b) Public Benchmark Safety (%)` | `(c) Glossary Latency, +Tok & Leaks`). Every bar extends horizontally with its exact value printed cleanly in open space to the right of the bar — **zero x-label collisions, zero vertical text rotation, and instant left-to-right per-model visual scanning!**
2. **Legend & Annotation Breathing Room**:
   - Never place a 2-row legend closer than `24 pt` (`pad >= 24`) to a panel title, and never let adjacent bar value badges touch each other. Put shared series legends in a single clean top strip (`ncol=3..4`, `frameon=False`).

---

## 2. CCF-A Table Taxonomy & Pure `booktabs` Craft

Published SIGMOD Industrial & PVLDB papers use **four clean table archetypes**:
1. **T1 — Schema / Workload / Operator Catalog Table** (`DocETL` Table 1, `HermesGov` Table 1): Summarizes real domain scale, empty vs. populated tables, or formal operator signatures.
2. **T2 — Qualitative System Positioning Matrix** (`HermesGov` Table 2, `LedgerTag` Table 1): Contrasts 5–7 orthogonal system guarantees (`\checkmark`, `$\triangle$`, `$\times$`) against closest published systems.
3. **T3 — Multi-Workload / Multi-Model Benchmark Table** (`LOTUS` Tables 6–7, `FinSQL` Table 7): Uses **hierarchical column groups separated by `\cmidrule(lr){a-b}`**.
4. **T4 — Orthogonal Component Ablation & Scale Verification Table** (`FinSQL` Table 8, `HermesGov` Table 6, `LedgerTag` Tables 5–6): Reports exact metric drops when each invariant/operator is disabled.

### Mandatory Table Hygiene Rules (Automated by `scripts/latex_table_and_cite_lint.py`)
- **Rule T-1 (Zero Vertical Pipes `|`)**: Never mix `\toprule/\midrule/\bottomrule` with vertical bars `|` (`{l|ccc|r}` creates broken vertical segments and violates ACM/VLDB `booktabs` typography). Use `@{}l...r@{}` + `\cmidrule(lr){...}` exclusively!
- **Rule T-2 (Mandatory `\cmidrule(lr)` Under Every `\multicolumn`)**: Every multi-column header group MUST have a trimmed `\cmidrule(lr){start-end}` underneath so sub-columns never run together visually.
- **Rule T-3 (Zero Robotic Summary Rows)**: Never append template-like rows such as `Best / 2nd | Best | Best | Best`; bold the best value and underline the second-best directly in data rows (`FinSQL` / `LOTUS` convention).

---

## 3. Float-to-Prose Proximity Law (`scripts/float_proximity_audit.py`)

In `FinSQL`, `Enzyme`, `AlayaDB`, `LOTUS`, `DocETL`, and `DAIL-SQL`, **every Figure and Table appears on the exact same page (`Δp = 0`) or immediately adjacent column/page (`|Δp| <= 1`) where its main prose analysis begins**, and **never floats past subsequent sections** (such as *Lessons Learned*, *Related Work*, or *Conclusion*).

### Two-Column LaTeX Placement Mechanics (Zero Margin Hacks)
- In two-column LaTeX (`acmart` and `pvldb`), `\begin{figure*}[t]` and `\begin{table*}[t]` **cannot** land on the page currently being typeset; TeX always places double-column floats at the earliest on the **following** page!
- Therefore, to make `Figure k` or `Table k` appear at the top of **Page $P$** right above Section $X$'s analysis on Page $P$, place the `\begin{figure*}[t]` / `\begin{table*}[t]` block **1.5–2 columns earlier in `main.tex`** (inside Page $P-1$'s text stream), and place at most one `figure*` + one `table*` targeting the same page so they never queue-spill into *Conclusion*!
- Verify after every compile with:
  ```bash
  python3 ccfa-visual-table-ref-mastery/scripts/float_proximity_audit.py paper/main.pdf
  ```
  Target: **`0` floats with `|Δp| >= 2`** and **`0` floats landing after their section's end page**!

---

## 4. Proof & Inline-Math Typography (`WAIR` SIGMOD '26 Standard)

- Never place tall delimiters (`\bigl(\sum ... \bigr)`, `\left( ... \right)`, or display-style `\frac`) on the closing line of a `\begin{proof}...\end{proof}` environment: tall inline math stretches baseline leading and makes the right-flushed QED box (`□`) appear vertically misaligned or like a stray tofu glyph!
- Always end every `\begin{proof}` with a clean, normal-height English clause (e.g., `"...recovering $R^*(u)$ and completing the proof."`) so line spacing is uniform and `\qed` sits flush on the baseline right margin.

---

## 5. Exhaustive Reference & In-Text Citation Verification

References are a primary trust signal for CCF-A reviewers. Run `submission-integrity-check/scripts/ref_check.py` **plus** `scripts/latex_table_and_cite_lint.py` and web verification on every single entry:
1. **100% Real, Verified Metadata**: Every cited paper must exist with exact title, **complete untruncated author list** (never drop trailing authors without `and others`, and prefer complete author lists in BibTeX!), exact venue, volume/number, page range, and resolving DOI.
2. **Published Peer-Reviewed Source Over `arXiv`**:
   - If a paper has been formally published (e.g., at SIGMOD, PVLDB, ICDE, NeurIPS, ICLR, ACL, EMNLP, CIDR), you **MUST** cite the official published proceedings/journal entry (with official pages/URL/DOI) and **NEVER** attach an `arXiv` DOI (`10.48550/arXiv...`) to a conference entry!
   - Cite `arXiv` **only** when no peer-reviewed conference or journal publication exists, verified via live search.
3. **Surgical, Pinpoint In-Text Citations ($\le 4$ Keys Per Bracket)**:
   - Never dump 8–10 citations into a single undifferentiated bracket (`\cite{a,b,c,d,e,f,g,h,i,j}`). Group references into crisp 1–4 paper brackets tied directly to the specific architectural mechanism discussed in that clause!
   - Format `@misc` software/specification entries cleanly with official organization/authors, version/year, `\url{...}`, and access note if appropriate.

---

## 6. Files in This Skill
- `references/EXEMPLAR_6PAPER_FIG_TAB_ANATOMY.md` — Concrete dissection of all figures, tables, and float layouts across `FinSQL`, `AlayaDB`, `Enzyme`, `DAIL-SQL`, `LOTUS`, and `DocETL`.
- `scripts/float_proximity_audit.py` — Automated PDF float-to-first-analysis page distance & section-spill auditor.
- `scripts/latex_table_and_cite_lint.py` — Automated LaTeX/BibTeX linter for vertical table pipes, missing `\cmidrule(lr)`, proof-end math collisions, citation dumps, and `arXiv`-DOI/author-truncation defects.
