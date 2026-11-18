# Pervasive Annotation Errors Break Text-to-SQL Benchmarks and Leaderboards

## Source and scope
- Formal source: https://www.vldb.org/pvldb/vol19/p931-jin.pdf
- DOI: https://doi.org/10.14778/3796195.3796206
- PVLDB 19(5), 931–944, 2026.
- Checked 2026-11-18. Read page-by-page extracted text and visually inspected PDF page 9. Not a full visual audit or sentence-level rhetorical annotation.
- Observed document: 14 pages, 12 body + 2 references; 69 numbered references, 11 figures and 7 tables. These counts describe this paper only.

## Observed argument and evidence
Pages 1–2 present the problem and evidence examples; pages 3–5 specify research questions, sampling, tooling and audit protocol. Pages 6–7 categorize errors and corrections. Pages 8–10 reevaluate systems and connect score changes, correctness flips, rankings and correlation. Pages 11–12 address audit cost, ablations, related work and conclusions.

The study reevaluates 16 systems on original versus corrected versions of a 100-example subset. Figures 6–9 develop different links in the evidence chain: scores, correctness flips, rankings, and correlation. Human adjudication and tool diagnosis are distinct. Changes to SQL, questions, schemas and data need separate explanations; the studied subset does not mean an entire benchmark has been repaired.

## Transferable interpretation
An empirical title is a hypothesis requiring a chain of evidence, not merely a dramatic description. Score shifts are more useful when linked to individual corrections and then to system-selection consequences. Audit samples and reevaluation samples must be identified rather than treated as an interchangeable population.

## Proposed review questions, not source requirements
For a benchmark study, separate legitimate multiple interpretations from annotation errors. Version semantic labels, executable answers and adjudications; record annotator-visible information, disagreement and decisions. Preserve originals, make each correction inspectable, and isolate question, SQL and data changes. Use paired comparisons and confidence intervals where appropriate; explain how sample size and model selection constrain inference. The contribution can be a conditional ordering or measurement insight, not a new winning method.
