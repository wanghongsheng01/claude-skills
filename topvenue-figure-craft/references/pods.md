# ACM PODS: observed figure profile

Sample (arXiv versions; acceptance from arXiv comments or the ACM footer "Proc. ACM Manag. Data (PODS)"):
When is Shapley Value Computation a Matter of Counting? (PODS'24, Fig. 1, 2);
Consistent Query Answering for Primary Keys on Rooted Tree Queries (PODS'24, Fig. 1, 4, 5);
Evaluating Datalog over Semirings: A Grounding-based Approach (PODS'24, Fig. 1);
A faster FPRAS for #NFA (PODS'24, Fig. 1); control: Rewriting Consistent Answers on Annotated Data (PODS'25, no figures).

## Profile
- **Few figures, often not on page 1.** One paper has no figures, one has only an algorithm box, and one places Fig. 1 on page 13.
  Reviewers read theorems first.
- **Archetypes are the formal objects themselves, never systems:** a complexity/reduction landscape, a Hasse diagram of inclusions,
  a minimal pair of query trees, a concrete database instance with blocks, a join tree annotated with rules, an algorithm template.
  **No architecture or pipeline figure** appears.
- **Font = body font (TikZ/LaTeX).** Text is usually 9–10 pt = body size. Only the dense landscape drops to 6.7 pt.
- **Colour is minimal:** 3 of 5 main figures are pure black and white. When colour is used: **red = this paper, green = prior work, gray = structure**.
- **Emphasis by notation, not decoration:** underline = key, dashed = block or conditional reduction, star = chosen repair, bold edge = exogenous fact, hatching = "needs both lemmas".
- **Caption = reading rules + conclusion** ("An arrow from A to B means …; red arrows indicate our contributions").

## Transferable practices
1. A classification, dichotomy or set of reductions → draw the **landscape**: problems as nodes, reductions or inclusions as edges,
   **new edges in the single accent colour**, prior results in gray or green with citations next to the nodes.
2. A subtle structural condition decides complexity → show a **minimal pair of instances** that differ in one place, and **write the
   verdict in the sub-figure labels or the caption** ("q₁ coNP-complete, q₂ ∈ FO").
3. Database instances as LaTeX tables: relation name top-left, keys underlined, conflict blocks separated by dashed rules,
   a marker column for the chosen subset.
4. Text ≥ 0.8× body (8–10 pt) in the body family (TikZ/pgfplots), so the figure looks like part of the paper.
5. At most 3 semantic colours. Encode further dimensions with line style, fill pattern or stroke width.
6. The caption's first sentence gives the encoding or the claim, not "Overview of our approach".
7. For long proofs, a lemma → theorem roadmap (as used in SIGMETRICS and ICML) fits the venue's style.

## Avoid
Slide-style architectures with icons, shadows or gradients (they read as a systems paper posing as theory); box-and-arrow pipelines without
any concrete query, instance, class or reduction; decorative colours; text < 6 pt; undeclared encodings.
