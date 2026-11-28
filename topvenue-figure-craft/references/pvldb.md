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
