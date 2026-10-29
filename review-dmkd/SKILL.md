---
name: "review-dmkd"
description: "Simulated peer review for the Springer journal Data Mining and Knowledge Discovery (DMKD): an editor-in-chief desk screen, two or three independent reviewer reports scored on seven DMKD criteria, and an action-editor decision letter, followed by a fix list and a re-check. Use before submitting or resubmitting to DMKD (审稿 DMKD / 模拟审稿 / pre-submission review), when answering DMKD reviews, or when the user asks how DMKD reviewers judge benchmark, evaluation-methodology, reproducibility or data-cleaning papers."
---

# Review a manuscript the way DMKD does (Review-DMKD 审稿指南)

DMKD reviews are closed: no public DMKD reports exist. This skill is built from the journal's own judging criteria, the ECML PKDD journal-track call (the same editors and portal), first-hand writings of current DMKD action editors (Keogh's SIGKDD 2009 tutorial and 2021 benchmark talk), the statistical-comparison papers DMKD reviewers rely on (Demšar 2006; Benavoli et al. 2016, 2017), and 13 accepted DMKD papers that propose no new algorithm. Evidence and sources are in `references/evidence-notes.md`; everything in Part B of that file is inference and is labelled so.

## Language convention (permanent agreement with the author)
Reviewer reports, the decision letter and responses to reviewers are written in **English**. The summary for the author, the fix list and the re-check log are written in **Chinese (中文)**.

## How DMKD handles a submission [VERIFIED]
1. Editor-in-chief screen, typically within two weeks: scope, article type, completeness (editable sources, 150-250-word abstract, 4-6 keywords, Statements and Declarations, data availability, LLM documentation). Many decisions are desk decisions (median of 3 days to first decision).
2. An action editor ("Responsible editor") invites reviewers (plan for two or three). Review is single-anonymous.
3. Review takes 1-3 months. Acceptance after the first round is "very rare"; accepted papers usually go through two or three rounds.

## Procedure
Run the roles independently: each reviewer reads the manuscript, not the other reports. When subagents are available, give each reviewer only the PDF or `.tex` and its persona, not the authors' own assessment.

1. **Desk screen (EiC).** Fill `assets/desk_screen.md`. Any failed hard gate ends the review with "returned to authors"; any failed substantive item is a likely desk reject.
2. **Reviewer reports.** Two or three personas, chosen to match the action editors who handle such papers:
   - *Benchmark-critique reviewer* (Keogh/Paparrizos style): triviality, flawed benchmarks, spurious precision, "is there an easier way", reproducibility from the authors' artefacts alone.
   - *Evaluation-methodology reviewer* (Campos/Zimek, Demšar/Benavoli style): measures, dataset preparation and variants, statistical treatment, fairness to prior work.
   - *Domain reviewer* for the paper's own area (for example data cleaning or entity resolution): related work outside data mining, technical correctness, whether the audited systems are treated fairly.
   Each report uses `assets/review_form.md`: summary in the reviewer's words, the one-sentence claim, seven scored criteria, 3-5 numbered major issues, minor issues, recommendation, confidential note to the editor.
3. **Action-editor letter.** Combine the reports with the rule below, list the required changes in priority order and write the decision letter.
4. **Fix list (中文).** Translate every major issue into a concrete edit, experiment or rebuttal, with the file and section it touches. Mark which ones the author must decide.
5. **Re-check.** After the edits, run fresh reviewer instances on the new version and record which issues are closed, open or new.

## Seven criteria (score 1-5; weights)
| | Criterion | Weight | Questions |
|---|---|---|---|
| C1 | Contribution and claim | 20% | Is the main contribution clear after the abstract alone? Can the reviewer write the claim in one sentence? Is it specific and matched by the evidence? |
| C2 | Research gap and significance | 15% | Is there "a clearly defined research gap" that existing methods cannot address? Why should KDD researchers care? What changes in practice or in published conclusions? |
| C3 | Novelty and relation to the literature | 10% | Beyond what the cited papers establish? Are the 3-5 closest recent works by other groups contrasted? Are DMKD/KDD/ECML PKDD/JMLR works cited, not only database venues? Is prior work treated fairly? |
| C4 | Technical soundness | 15% | Precise definitions; justified choices and parameters; validated ground truth ("who audits the auditor?"); hidden assumptions; a simpler way? |
| C5 | Experimental methodology | 20% | Do experiments answer the research questions? Enough datasets, systems and versions? Simple baselines included? Metrics justified? Variance and statistical tests where comparisons are claimed, or a reason why they do not apply? Precision of numbers matched to their uncertainty? |
| C6 | Reproducibility and artefacts | 10% | Code, data, configurations, pinned versions and scripts archived with a DOI? Data availability statement? Could a third party regenerate every table? |
| C7 | Clarity and presentation | 10% | Readable by a data-mining generalist? Jargon defined once and kept small? Figures and tables carry the argument? Length justified? |

Recommendation: Accept / Minor revision / Major revision / Reject (state whether a resubmission would be welcome).

**Action-editor rule [INFERRED].** Reject if any reviewer finds a fatal C1, C2 or C5 flaw that no revision can fix (for example, no research gap, or experiments that cannot support the claim). Otherwise the default first-round decision is major revision.

## The objections DMKD reviewers raise most (ranked by evidence)
1. The contribution is not clear from the abstract; the claim cannot be stated in one sentence.
2. No clearly defined research gap; why does it matter to KDD?
3. "So what?": no demonstrated consequence for a reported result, ranking or conclusion.
4. Out of scope: a database or software-engineering paper not framed for data mining (no DMKD/KDD/ECML/JMLR references).
5. Experiments not fully reproducible from the released artefacts.
6. Breadth too narrow (one system, one dataset family, one version).
7. Missing data-mining evaluation-methodology literature (Keogh and Kasetty 2003; Campos et al. 2016; Bagnall et al. 2017; Wu and Keogh 2023; Hewamalage et al. 2023; Demšar 2006).
8. Weaknesses not acknowledged, or so many caveats that the claim is empty.
9. "There is an easier way" (a simpler baseline would catch the problem).
10. Unjustified complexity or terminology.
11. Arbitrary choices and magic numbers (run counts, thresholds, k).
12. If typed as a Survey: not comprehensive or balanced, no insight beyond the cited papers.
13. The authors' own reference or verifier is not validated.
14. Spurious precision; dependent cases counted as independent successes.
15. No statistics or variance where differences are claimed.
16. Metrics not justified.
17. Unfair tone toward audited tools; maintainers not consulted.
18. Synthetic errors not representative of real ones.
19. Two loosely coupled contributions; lack of focus.
20. Version-specific findings without a general lesson.
21. No constructive artefact (corrected benchmark, tool, guidelines, crosswalk).
22. Overlap with earlier work not declared.
23. Practical impact not demonstrated.
24. Dense, number-heavy prose; tables and figures do not carry the argument.
25. Efficiency claims without a runtime methodology (hardware, repetitions, implementation effects; Kriegel et al. 2017).

## What made accepted no-new-algorithm DMKD papers work
Keogh and Kasetty 2003, Campos et al. 2016, Bagnall et al. 2017, Hewamalage et al. 2023, Sørbø and Ruocco 2024 and Middlehurst et al. 2024 share six traits. Check the manuscript against each:
1. A named field-level problem with at least one case where a published or plausible conclusion flips.
2. Breadth: several systems, datasets, generators or versions.
3. A reusable artefact: repository, tool, archive, taxonomy or guidelines.
4. Correct statistics wherever rankings are claimed; an explicit reason when checks are deterministic.
5. Fair treatment of the audited work.
6. A deliberate article type: a new procedure → Regular Paper; an extensive independent comparison → Survey Paper.

## Lessons from use (2026-10-29, benchmark-audit paper)
Two independent reviewer instances raised the same three points, and all three changed the paper:
- **Noise floor.** A "ranking changes in X of Y comparisons" claim must be compared with the variation between replicates the producer itself provides (random downsamples, resamples, seeds), with a tolerance for near-ties and more than one measure. Check whether most comparisons are pseudo-replicates of a few datasets, and whether the headline survives a binomial or bootstrap test.
- **Validate the procedure, not only the systems.** A paper whose contribution is an audit or attribution procedure should plant perturbations with known causes and report recovery, including the cases the procedure gets wrong.
- **Attribution conventions.** "Nobody but X is responsible" results depend on the attribution rule; ask for a formal rule, a "documentation" outcome where producer documentation and implementation disagree, and counting one policy as one cause.
Reviewers also re-derived numbers from the released JSON files; give them result files with a one-to-one map to every number in the paper.

## Output files
- `review/desk_screen.md`, `review/reviewer_<n>.md`, `review/ae_decision.md` (English).
- `review/修改清单.md` (Chinese fix list) and `review/复审记录.md` (Chinese re-check log).
