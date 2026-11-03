---
name: "review-icde"
description: "Simulated IEEE ICDE program-committee review of a manuscript before submission: desk-reject screen (format, scope, COI, AI disclosure), three independent reviewer reports on an ICDE-style form (novelty, technical depth and soundness, experiments, presentation, reproducibility, relevance), a senior-PC meta-review with Accept/Reject (ICDE has no revision), an adversarial check of numbers, proofs and references, and a revision table. Built from the ICDE 2027 CFP and the strengths/weaknesses of 21 deep-read accepted papers. Use for 模拟审稿 / 独立审阅 / 预审 of an ICDE paper or rebuttal preparation."
---

# Simulated ICDE review (模拟 ICDE 审稿)

Use after `write-icde`, before `submit-icde`. Forms in `assets/`; evidence in `references/reviewer-lens.md`.

## Language convention
Reviews, meta-review and rebuttal drafts in **English**; the summary for the author and the revision table in **Chinese (中文)**.

## 1. Independence
The reviewer must not be the author of the text. When using sub-agents, give each reviewer only the PDF/LaTeX, the CFP rules and the review form, not the author's own assessment, and ask for the three most likely rejection reasons. Use three reviewers with different lenses (method/theory, systems/experiments, outside-area generalist) and one meta-reviewer who reads the three reports.

## 2. Desk screen (`assets/desk_screen.md`)
Template and 12-page limit without appendix; author block (single-blind); AI disclosure; scope: a data-engineering challenge and ICDE/VLDB/SIGMOD lineage in related work; EAB title tag and complete artifacts if EAB.

## 3. Reviewer report (`assets/review_form.md`)
Summary; 3 strengths; 3 weaknesses (each actionable); detailed comments by section; scores for novelty, technical depth/soundness, experiments, presentation, reproducibility, relevance; overall (Strong Accept / Accept / Weak Accept / Weak Reject / Reject); confidence; questions for the rebuttal.

What ICDE reviewers look for (from accepted papers, `references/reviewer-lens.md`):
- A gap shown with evidence (Figure 1 measurement), not asserted.
- One clear insight with a provable property; known methods as special cases.
- Baselines that include the strongest recent methods and core-venue work; fair tuning; same pilot/budget.
- Real costs (dollars/tokens/latency) for LLM papers; scalability for systems and graph papers.
- Validity of any guarantee measured (e.g. coverage vs nominal), dispersion over repetitions.
- Honest limits: where the method does not help.
Typical rejection reasons: incremental over a named prior paper; guarantee assumed but not checked; toy scale; missing a key baseline; out of scope (pure ML); claims in abstract not matched by tables.

## 4. Adversarial checks
- Every number in the abstract/introduction appears in a table or figure and matches the result files.
- Each proof step is checked; assumptions are stated in the theorem.
- Every reference exists with the stated venue/year (Crossref/OpenAlex/arXiv); no citation supports a claim it does not make.
- Figures readable at column width; captions self-contained.

## 5. Meta-review and revision
Meta-review: consensus strengths/weaknesses and a decision. Then a revision table: weakness -> change made -> location; re-run the checkers of `submit-icde` and `write-icde`.

## Final checklist
- [ ] Desk screen passed.
- [ ] Three independent reports and a meta-review.
- [ ] Numbers, proofs and references verified.
- [ ] Revision table completed and changes applied.
