---
name: "write-dse"
description: "Writing guide for papers aimed at the Springer journal Data Science and Engineering (DSE, CCF B), built from 39 published DSE articles 2021-2026 (19 chosen for topic closeness to data quality, evaluation and anomaly work, 20 random recent ones): titles, abstracts, gap-then-proposal openings, sections, experiments, data availability, figures, tables, references, length. Use when drafting, restructuring or repositioning a manuscript for DSE (写 DSE / 改投 DSE 写作), including evaluation, benchmark, data-quality or reproducibility papers. Includes a structure checker."
---

# Writing for Data Science and Engineering (Write-DSE 写作指南)

Evidence: `references/dse_paper_survey.csv` (one row per article, DOIs 10.1007/s41019-...) and `references/observed-papers.md`. Counts such as "28/39" are observations, not acceptance thresholds. The sample is parsed from the article pages by script; the five closest papers were read by hand.

Use with `submit-dse` (format, blinding, portal) and `review-dse` (simulated review).

## Language convention
Manuscript, captions and letters in **English**; notes, plans and reports to the author in **Chinese (中文)**.

## What a DSE paper looks like
Median 10.9k words, 7 top-level sections, 7 figures, 5 tables, 53 references, 207-word abstract, 4 keywords. Standard skeleton:

1 Introduction / 2 Related Work (or Preliminaries) / 3 Method / 4 Experiments / 5 Discussion (optional) / 6 Conclusion.

Related Work is commonly section 2 (23/39), though the closest paper (Data Validation in Data Spaces, 2025) places it just before the conclusion. A survey or an experimental study replaces the method section with taxonomy and experiment sections (Link Prediction: An Experimental Survey, 2022).

## Title
Median 10 words; 18/39 use a colon. Name the object and the approach, in title case. Good models: "Operationalizing and Automating Data Validation in Data Spaces"; "Link Prediction on Complex Networks: An Experimental Survey"; "Identifying E-Commerce Fraud Through User Behavior Data: Observations and Insights"; "An Exploratory Study on Information Cocoon in Recommender Systems"; "Relational Data Cleaning Meets Artificial Intelligence: A Survey".

## Abstract (150-250 words)
Pattern of the closest papers: domain context in one or two sentences; what current solutions lack; "To address this gap, we present ..."; the key idea; what makes it better; the evaluation result in one sentence. The result is stated positively, even for a proof of concept: "We accompany the description of our approach with a proof of concept that demonstrates the feasibility of this solution in real data spaces." No citations, abbreviations defined.

## Introduction
1. Why the data task matters; 2. why current practice falls short, with citations; 3. a running example or figure where it helps ("Example 1" with Figure 1 in the data-validation paper); 4. the proposal in one sentence; 5. a contribution list (28/39); 6. optional roadmap (13/39). Explicit research questions are uncommon but accepted (7/39), and they suit empirical studies.

## Preliminaries and method
Definitions and notation in a Preliminaries section; formal problem statement where there is one. Present the workflow as a named framework with a figure, and describe each component with what it enables. Use the affirmative register: "the framework enables", "this enhances transparency and traceability".

## Experiments
- Name datasets and baselines, then state results per question. Tables carry the numbers; figures show trends.
- An evaluation can be small if its purpose is stated: feasibility, flexibility, overhead. The data-validation paper's section is a proof of concept. A complete comparison is not required when the contribution is a framework.
- Empirical studies state the factors varied and the finding per factor (Evaluation of Estimation Methods, 2025).
- Report runtime with hardware when efficiency is claimed.

## Discussion, limitations, conclusion
Limitations are brief. Median one mention per paper; several have none. The usual form: one short paragraph in Discussion ("This work still has some limitations ...", Information Cocoon, 2025), or a sentence of future work. Conclusions restate what was presented and what the evaluation demonstrated, then give future directions. Do not end the paper on what was not shown.

## Availability
16/39 print an availability section, and repositories are linked in 19/39. Under double-blind review, cite the blinded Online Resource and restore public links afterwards.

## Figures and tables
Framework or workflow diagram first; vector; "Fig. n"; captions short and without a final period. Numbered tables with booktabs rules, kept upright. Do not refer to colour alone.

## References
Median 53 (evaluation or survey papers run up to 194). Numeric in the text. Mix recent VLDB, SIGMOD, ICDE and journal work, and cite the journal's own related articles where relevant, such as the DSE data-cleaning survey (DOI 10.1007/s41019-024-00266-7) for a cleaning paper. Verify every reference against Crossref or the publisher page.

## Repositioning an audit or evaluation paper for DSE
1. Open with data quality, the first topic in the journal's scope, not with a tool.
2. Give the concept a name and present it as a framework with a workflow figure.
3. Lead with what the framework makes possible, then the measured evidence.
4. Convert negative framing ("does not establish X") into scope statements, keeping claims within the evidence.
5. Move protocol history into supplements, and state in the paper only what a reader needs in order to trust the numbers.
6. Keep every number traceable to the supplement.

## Checker
`python3 scripts/dse_structure_check.py main.tex` compares a manuscript with the observed medians and counts hedging phrases. It reads files only.

## Final checklist
- [ ] Gap and proposal are stated in the abstract.
- [ ] Named framework with a workflow figure.
- [ ] Contribution list; results by question.
- [ ] Limitations in one short paragraph; conclusion ends on what was shown and what comes next.
- [ ] About 50 verified references, including some DSE articles.
