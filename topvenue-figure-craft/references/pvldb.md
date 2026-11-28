# PVLDB: observed figure profile

Sample (vldb.org open access): LLM-R2: A Large Language Model Enhanced Rule-based Rewrite System for Boosting Query Efficiency (PVLDB 18, 2024, Fig. 1, 2);
R-Bot: An LLM-based Query Rewrite System (PVLDB 18, 2025, Fig. 1, 2);
SPADE: Synthesizing Data Quality Assertions for Large Language Model Pipelines (PVLDB 17, 2024, Fig. 1, 3);
Membrane: Safe and Performant Data Access Controls in Apache Spark in the Presence of Imperative Code (PVLDB 17, 2024, Fig. 1, 7).

## Profile
- **Figure 1 favours a real query instance plus a measurable gain.** Both query-rewrite papers draw a real SQL query. One turns it into a complete worked
  example that ends with "> 5 min → 1.67 s" in red. Database reviewers respond most to "real query, real gain".
- **Single column** for all four Figure 1s (about 240–250 pt). Full width is kept for the overview.
- **Colour:** the two best figures use one accent (SPADE: gray existing workflow + one light-blue contribution column) or three "syntax"
  colours. Colour also links an SQL clause to its plan node, so no connecting lines are needed. Figures with 7 or more hues look messy.
- **Tools:** slide or diagram software at 3–6 pt (too small) vs TikZ in the body font (Libertine, 8 pt), which looks most publication-grade.
- **Mechanism figures show intermediate artifacts:** JSON and code, plans with the injected predicate highlighted, output SQL.
- **Captions** state the mechanism or claim ("Before a developer deploys …, SPADE …; then …").

## Transferable practices
1. Figure 1 = **one real query or data instance plus one quantitative result** (before → after number in the alert colour).
2. **Gray status quo plus a single-colour contribution column**, with numbered internal steps ①② that the caption repeats.
3. Code ↔ structure correspondence through **shared colour instead of lines**, so nothing crosses.
4. Dashed boxes for input/output data, solid boxes for processing; dashed/solid can also encode untrusted/trusted.
5. Mechanism or access-control figures as **small multiples**: two plans side by side that differ only at the injection point, highlighted.
6. Text ≥ 80% of the body size (body about 9 pt, so ≥ 7 pt), preferably in the body font.
7. Overview: a narrow main loop plus dashed leader lines to detail panels; online/offline separated by a thin vertical rule.

## Avoid
A background architecture (for example a stock engine diagram) in Figure 1 with the change not marked; 3–5 pt gray italic explanations;
6 or more hues, logos or icon piles; long dashed loops across containers; labels on colour-block borders; raster figures.

## Lessons from a real Figure 1 redesign (multi-plane lineage / validation paper)
1. For multi-representation / multi-plane database problems, align one concrete metric across equal-width columns separated only by thin `0.45 pt` vertical hairlines and pair matching elements strictly by semantic color (accent blue = controlled premise, alert vermilion = silent disagreement)—eliminating every box-in-box nesting and cross-container arrow.
2. In native TikZ bottom contrast strips, avoid vertical divider lines drawn inside a rounded outer frame (they trigger `LINE_THROUGH_TITLE`); instead place three flat side-by-side cards (dashed prior blind-spot card, solid method card, short orthogonal border-to-border arrow, solid outcome-numbers card) for zero nesting and zero dangling arrows.
3. Compile standalone PVLDB TikZ previews with the exact `acmart.cls` + `pvldb.sty` + `[T1]{fontenc}` + `anchor=base` so Linux Libertine (9 pt body) and Inconsolata metrics match 1:1; setting readable text/code at `\footnotesize` (8 pt, 88.9% of body) avoids `\resizebox` scaling distortion.
4. Decouple matplotlib annotation text (`ax.text` in whitespace) from arrows (`ax.annotate("", ...)`) on line and sensitivity curves so combined annotation bboxes never cross plotted lines.
5. On paired horizontal bar charts (e.g., FNR vs. FPR), remove vertical gridlines (`axis="x"`), use `h = 0.24`, `offset = ±0.19`, and `>= 4` data units of right-end clearance so labels pass the 2 pt border clearance rule cleanly.
6. Eliminate PVLDB narrow-column `Underfull \hbox >= 2000` stretches caused by long Inconsolata table/column names by inserting `\_\allowbreak`, splitting adjacent inline math tokens (`$\mathcal{P}_1$, $\mathcal{P}_2$`), sizing multi-table code lists with `{\small\texttt{...}}`, and adding `\hyphenation{}` + BibTeX `?`/proper-noun capitalization braces.
