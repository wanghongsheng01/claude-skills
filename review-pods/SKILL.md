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

### Stage 2 — PODS Theoretical Depth, Mother-Tongue Alignment & Completeness Audit (CRITICAL)
Ask the exact questions a senior PODS PC member asks (`write-pods/references/pods-evaluation-and-mother-tongue-positioning.md`):
1. **Community Mother-Tongue Alignment (建议 0.1)**: Does the paper open and reason in native PODS ontology (**Incomplete Representation Systems**, **Valuations vs. Completions**, **Certain / Possible / Expected Evaluation**, **Operational vs. State Repairs**, **Morphism Commutativity**, **Data vs. Combined Complexity**), or does it read like an ML/engineering pipeline audit with lemmas bolted on?
2. **Data Complexity vs. Combined Complexity & Valuations vs. Completions**: Does the paper analyze fixed schema arity $m = O(1)$ ($m=1$ vs. $m \ge 2$) AND distinguish syntactic witness bijections (`valuations`) from induced target instances (`completions`, parsimonious `#P`-completeness)?
3. **The Four-Way Evaluation Separation (Certain, Possible, Exact Expected/Counting, Approximate `FPRAS`)**: When exact counting/expected evaluation is `#P`-hard, does the paper resolve **approximability (`FPRAS` / `FPAUS`)** (e.g., via `Jerrum–Sinclair–Vigoda` on tight bipartite matchings) rather than embarrassingly listing a known permanent FPRAS as an open problem in Conclusion?
4. **Beyond Unit Weights & Boundary Completeness**: Are unbalanced cardinalities ($n' \neq n$), **attribute-weighted / general additive costs** (e.g., fractional Dinkelbach matching when error denominators vary), and $\varepsilon$-perturbed tolerances proved formally rather than punted to Future Work?
5. **Zero Orphan Artifacts & High-Taste Open Problems**: Does every benchmark in the experimental section map 1-to-1 to a formal theorem (zero unmodeled side-benchmarks), and do Conclusion open problems target genuine theoretical frontiers?
6. **Story Novelty, Anti-Folklore Boundary & Cross-Axis Coupling (`write-pods/references/pods-story-novelty-and-reviewer-recognition.md`)**:
   - **Skeptical PC Test #1 ("Why isn't this folklore Hungarian/Tarjan?")**: Does the paper establish a **counter-intuitive complexity inversion** AND prove the **exact structural boundary** where polynomial time breaks into `NP`/`coNP`-hardness (e.g., row-separable vs. pairwise-coupled evaluation at $m=2$)?
   - **Skeptical PC Test #2 ("Why isn't this 4 independent mini-notes bundled into a tuple?")**: Does the paper prove a **cross-axis non-commutativity / interaction theorem** (e.g., correspondence $\mathcal{I}_{\mathrm{min}}$ failing to commute with value endomorphism $\nu$) that algebraically couples the chapters?
7. **Scaffolding**: Are there **framed `PROBLEM / INPUT / OUTPUT` boxes** (`≥ 2`), **numbered `\begin{example}`s** (`≥ 3`), and **structural `\begin{lemma}`s** (`≥ 3`)?

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
- For papers involving **view determinacy, authorization-safe query rewriting, TGDs/EGDs, $\Pi_2^p$/$\mathrm{coNP}$ reductions, or Dinkelbach fractional repair**, additionally run every red-team proof check in `references/pods-view-rewriting-review-rubric.md` (singleton-value & FD EGD completeness, zero implicit anchor-tuple assumptions, feasible-assignment Dinkelbach initialization, explicit `FPT` layering, and 1-to-1 body-to-appendix proof accounting).
