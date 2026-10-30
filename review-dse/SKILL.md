---
name: "review-dse"
description: "Simulated peer review for the Springer journal Data Science and Engineering (DSE, CCF B): editor desk screen, two or three independent double-blind reviewer reports on seven criteria, and an associate-editor decision letter, followed by a Chinese fix list and a re-check. Use before submitting or resubmitting to DSE (审稿 DSE / 模拟审稿), when answering DSE reviews, or when asked how DSE reviewers judge data-quality, benchmark, evaluation or reproducibility papers."
---

# Review a manuscript the way DSE does (Review-DSE 审稿指南)

DSE reviews are closed; no public reports were found. This skill is built from the journal's scope and rules, Springer Nature's reviewer guidance, the editorial board's research areas and 39 accepted papers. Evidence and the status of each claim are in `references/evidence-notes.md`. Everything about reviewer behaviour is inference.

## Language convention
Reviewer reports and letters in **English**; the summary, fix list and re-check log for the author in **Chinese (中文)**.

## How DSE handles a submission
1. Editors-in-Chief screen scope and completeness [INFERRED order; first decision median 26 days, VERIFIED]. Hard gates: editable sources, declarations, blinding.
2. An associate editor handles the paper and invites reviewers [INFERRED]. The review is double-blind [VERIFIED]: reviewers judge the work, not the names, and a blinding failure can be returned to the authors.
3. Springer guidance: reviewers "assess papers exclusively against the journal's criteria", check data and supplementary material, and comment on the validity of the approach [VERIFIED].

## Procedure
Run roles independently, with each reviewer given only the manuscript and supplement, not the authors' self-assessment.
1. **Desk screen**: fill `assets/desk_screen.md`.
2. **Reviewers**, two or three of:
   - *Data-quality reviewer*: data cleaning, integrity constraints, functional dependencies, data validation; related work and fairness to audited tools.
   - *Data-engineering systems reviewer*: benchmarks, experiments, reproducibility, whether a reader can use the framework; "what does this enable?"
   - *Applied data-science reviewer*: a generalist asking what the takeaway is, whether jargon is defined, and whether the paper is readable.
3. **Associate-editor letter**: combine reports with the rule below.
4. **Fix list (中文)**: each major issue becomes an edit, experiment or rebuttal.
5. **Re-check** with fresh reviewers.

## Criteria (1-5; weights are a working convention)
| | Criterion | Weight | Questions |
|---|---|---|---|
| C1 | Scope fit | 15% | Which scope area? Is it about data, its quality, or data-intensive systems? Is the DSE reader the audience? |
| C2 | Contribution and novelty | 20% | Is the contribution clear from the abstract? Is it more than the sum of known ideas? Is a named framework or artefact offered? |
| C3 | Technical soundness | 15% | Definitions, assumptions, correct proofs, a validated reference, a simpler way? |
| C4 | Evaluation | 20% | Do experiments support the claims? Enough systems and data? Baselines? Are numbers traceable? Statistics where comparisons are claimed? |
| C5 | Practical value | 10% | Who uses it and what changes for them? Is there a demonstrated consequence? |
| C6 | Reproducibility and blinding | 10% | Are materials complete? Is authorship hidden? Can third parties rerun them? |
| C7 | Clarity | 10% | Length, jargon, structure, figures; confident without overclaiming |

Recommendation: Accept / Minor / Major / Reject. **Rule [INFERRED]:** reject on a fatal C1, C2 or C4 flaw; otherwise major revision is the default in a first round.

## Objections to expect
1. Out of scope or too narrow: one generator and one tool, not a data-science problem.
2. "So what?": no effect on any published result.
3. The contribution is hard to state in one sentence.
4. The concepts are already known: tuple identity, normalization.
5. Small scale: small tables or synthetic errors.
6. Two loosely coupled parts: benchmark audit and metric-reference checker.
7. Too many caveats: the paper argues against itself.
8. Too few caveats: claims not supported by the evidence.
9. Version-specific findings without a general lesson.
10. Unfair to audited tools; maintainers not contacted.
11. Blinding failure: public deposit or identical title with names.
12. The own reference or verifier is not independently validated.
13. Dependent cases counted as independent.
14. Too long for its findings; number-dense prose; few figures.
15. Sparse references, especially recent ones.

## Output files
`review/desk_screen.md`, `review/reviewer_<n>.md`, `review/ae_decision.md` (English); `review/修改清单.md`, `review/复审记录.md` (Chinese).

## Lessons from use (2026-10-30, benchmark-audit paper)
Two independent reviewers given the supplement found problems that the authors' summaries hid:
- **Pseudo-replication.** Both hashed the raw run files and found that a "30 fresh runs" task had one distinct outcome. Before submitting, count distinct outcomes for every repeated-run claim and report them next to raw counts.
- **By-construction results.** An oracle probe or a tie guaranteed by the task definition is not evidence; say so in the abstract, or remove the experiment.
- **Caveats come in three kinds.** Ask reviewers to separate caveats that only weaken the paper, caveats a claim needs, and caveats that are missing. Removing hedges without this split overclaims.
- **Residue reveals history.** Stale file names, citations to other venues and process notes tell an editor that an earlier version exists. Sweep supplements before uploading.
