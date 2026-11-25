---
name: "review-pods"
description: "Simulated ACM PODS Program Committee review and formal-rigor deep-audit protocol. Calibrated against 8 officially accepted PODS 2024-2027 papers and the PODS 2027 CFP. Evaluates (1) Desk-Reject compliance (acmsmall, <=15 body pages, strict double-anonymous, no dual submission), (2) Formal Depth & Non-Triviality (tight if-and-only-if characterizations, complexity separations, sound reductions, complete proofs), (3) Self-Contained 15-Page Body vs. Appendix proof balance, (4) Empirical Foundations Alignment, and (5) Independent 3-Reviewer PODS PC Simulation (Database Theory Purist, Algorithms & Complexity Referee, Data-Quality Foundations & Artifacts Referee) plus PC Chair Meta-Review and Revision Closure Table."
---

# Simulated ACM PODS PC Review & Deep Revision Protocol (`review-pods`)

## Language Convention
- Reviewer reports and PC Chair meta-review: **English** (authentic PODS EasyChair register).
- Author executive summary, proof-audit table, and Revision Closure Table: **Simplified Chinese (简体中文)**.

## 5-Stage PODS PC Review Procedure
1. **Stage 1 — PODS 2027 Desk-Reject & Double-Anonymous Screen**:
   - `\documentclass[acmsmall,review,anonymous]{acmart}` exact match.
   - Body strictly **≤ 15 pages** (before References); unlimited References & clearly marked Appendix.
   - Zero author/institution/personal-GitHub leaks in `.tex`, `.bib`, and PDF metadata.
   - Zero dual-submission overlap risk flagged explicitly to the author.
2. **Stage 2 — Proof & Formal-Rigor Line-by-Line Audit**:
   - Verify EVERY Definition, Theorem, Proposition, Lemma, and Corollary:
     - Are all hypotheses explicit and minimal?
     - Does every complexity reduction preserve instance size, polynomial time, and exact solution correspondence (bidirectional)?
     - Are all edge cases handled (empty sets, ties, duplicate rows, constant columns, $0/0$ denominators)?
     - Does every theorem earn PODS depth (no trivial 2-line restatements of code)?
3. **Stage 3 — Anti-AI-Smell & Self-Negation Audit (`pods_human_craft_audit.py`)**:
   - Confirm `0` `Threats to Validity` / `Limitations` headings (`0/8` in PODS 2024–2027), `0` self-negation confessions, `≤ 0.35/1K` AI clichés, and crisp human mathematical prose.
4. **Stage 4 — Independent 3-Reviewer PODS PC Simulation + Meta-Review**:
   - **Reviewer 1 (Database Theory & Logic Purist)**: Checks connection to CQA, database repairs, provenance semirings, and whether the formalisms are deep and canonical.
   - **Reviewer 2 (Algorithms & Complexity Referee)**: Checks every proof step of the $O(n^3)$ SCC algorithm, $\#\mathsf{P}$-completeness reduction, coding-theoretic threshold, and tight bounds.
   - **Reviewer 3 (Data-Quality Foundations & Artifact Referee)**: Checks whether the empirical analysis truly sheds light on scientific foundations, verifies every number against reproducible artifacts, and tests clarity for the broader SIGMOD/PODS audience.
   - **PC Chair Meta-Review**: Identifies the #1 rejection risk and separates must-fix proof/framing defects from polish items.
5. **Stage 5 — Revision Closure & Full Re-Compile Verification**:
   - Close every actionable flaw in LaTeX, recompile, inspect every rendered page visually, and output the Revision Closure Table.
