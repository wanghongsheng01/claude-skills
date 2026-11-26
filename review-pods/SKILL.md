---
name: "review-pods"
description: "Rigorous ACM PODS Program Committee review and deep-upgrade protocol grounded in 8 published PODS 2024–2027 papers (Kolaitis et al., Karmakar et al., Esmailpour et al., Fan-Koutris-Roy, Lin-Nguyen-Woodruff, Surianarayanan et al., Liu-Zhang, Nakos-Ngo-Panayi). Audits 7 dimensions: (1) CFP/Double-Anonymous/15p format, (2) Theoretical Depth (data vs. combined complexity dichotomies, CQA certain/possible semantics, tight upper/lower bounds), (3) Formal Scaffolding (PROBLEM boxes, numbered Examples, Lemmas, complete proofs), (4) Mathematical Figure Craft (concrete tuple/graph schematics vs. PowerPoint boxes), (5) Dedicated Single-Topic Table Craft, (6) Experimental Foundations & Numbered Insights, and (7) Authentic Human PODS Prose."
---

# Simulated ACM PODS PC Review & Deep Upgrade Protocol (`review-pods`)

## Mandatory 6-Stage Deep PODS Audit

### Stage 1 — Desk-Reject, Double-Anonymous & Body-Completeness Screen
- `\documentclass[acmsmall,review,anonymous]{acmart}` + `\acmJournal{PACMMOD}`.
- Main body strictly **≤ 15.0 pages** AND **≥ 14.3 pages** (flags both `> 15.0p` desk-reject overflow and `< 14.0p` thin/under-developed exposition).
- Zero author/institution/personal-GitHub leaks in `.tex`, `.bib`, and PDF `/Author` metadata; zero concurrent dual-submission risk.

### Stage 2 — PODS Theoretical Depth & Completeness Audit (CRITICAL)
Ask the exact questions a senior PODS PC member asks:
1. **Data Complexity vs. Combined Complexity**: Does the paper analyze fixed schema arity $m = O(1)$ (e.g., $m=1$ vs. $m \ge 2$) AND bounded vs. unbounded attribute domains $|\mathcal{V}|$, or did it only prove an easy unbounded-arity reduction?
2. **Certain & Possible Semantics (CQA Connection)**: When optimal alignments/repairs are non-unique, does the paper characterize extremal (`min` / `max`) evaluation scores (`CertEval` / `PossEval`), or stop at testing uniqueness?
3. **Generalizations & Boundary Completeness**: Are unbalanced cardinalities ($n' \neq n$), weighted/metric extensions, and $\varepsilon$-perturbed floating-point tolerances analyzed formally rather than hand-waved?
4. **Scaffolding**: Are there **framed `PROBLEM / INPUT / OUTPUT` boxes** (`≥ 2`), **numbered `\begin{example}`s** (`≥ 3`), and **structural `\begin{lemma}`s** (`≥ 3`)?

### Stage 3 — Visual & Tabular Craft Audit (`Fan–Koutris–Roy` & `Karmakar et al.` Bar)
- **Figure 1**: Must show concrete relational instances, cost/potential matrices, and residual graphs — **REJECT** vague pastel block diagrams!
- **Data Plots**: Multi-panel vector plots with zero text overlap, exact theorem badges, error/interval bars where applicable, and crisp legends.
- **Tables**: Every table must be **single-topic and self-contained** — **REJECT** side-by-side hybrid tables that mash two unrelated experiments into 6 columns!

### Stage 4 — Human Mathematical Readability, Visual Breathing Room & Anti-AI-Smell Pass (CRITICAL)
- Run `pods_human_craft_audit.py`, `proof_and_math_audit.py`, `figure_formula_consistency_audit.py`, `latex_table_and_cite_lint.py`, and `ai_smell_audit.py` (`0 FAIL` across all 5!).
- **Inspect for "Symbol-Soup / Wall-of-Math" Anti-Patterns** (`write-pods/references/pods-human-readable-math-and-prose.md`):
  * **REJECT** paragraphs packing inline set-builders (`\{... : ...\}`), inline slash-fractions, or `> 32%` inline math characters without centered display equations;
  * **REJECT** italic `\begin{theorem}` / `\begin{lemma}` blocks stuffed with inline parameter definitions or `\sum/\prod/\frac`;
  * **REJECT** unbroken 15–25 line reduction bricks (enforce bulleted gadget construction + displayed distance/cost cases as in `Kolaitis et al. PODS '25 p. 16`);
  * **REJECT** compressed inline-math bricks in the Appendix (PODS grants **unlimited Appendix pages** — every Appendix proof must breathe with short `4–7` line paragraphs and centered `align*` / `equation` / `cases` displays!).
- Confirm `0` `Threats to Validity`/`Limitations` headings, `0` AI clichés, `0` em-dashes, mean sentence length `19–26` words, and clean analytical prose in Experiments.

### Stage 5 — Independent 3-Reviewer PODS PC Simulation + PC Chair Meta-Review
- **R1 (Database Logic, CQA & Data-Complexity Theorist)**
- **R2 (Combinatorial Optimization, Graph Algorithms & `#P` Complexity Referee)**
- **R3 (Data-Quality Foundations, Visual/Tabular Craft & Artifact Referee)**

### Stage 6 — Deep Code, Proof, Figure, Table & LaTeX Closure
- Implement and machine-verify every new theorem/formula in Python; regenerate all figures and tables from `verified_results.json`; compile with `0` errors, `0` warnings, `0` Overfull `\hbox`; inspect rendered PNGs of every page!
