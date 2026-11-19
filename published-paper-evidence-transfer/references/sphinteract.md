# Sphinteract: interactive text-to-SQL evidence design

## Source and scope
- Formal source: https://www.vldb.org/pvldb/vol18/p1145-zhao.pdf
- DOI: https://doi.org/10.14778/3717755.3717772
- PVLDB 18(4), 1145–1158; the PDF citation year is 2024.
- Checked 2026-11-18. Read page-by-page extracted text and visually inspected PDF page 9. Not a full visual audit or sentence-by-sentence rhetorical annotation.
- Observed document: 14 pages, 12 body + 2 references; 76 numbered reference entries (not a deduplicated paper count), 5 figures, 6 tables, 1 algorithm box. These are not recommended quotas.

## Observed argument and evidence
Pages 1–2 motivate the task with examples and contributions; pages 3–4 establish the problem, objectives, user study and ambiguity categories. Pages 5–7 introduce the framework, feedback strategies and algorithm. Pages 8–11 compare zero-/few-shot settings, interactions, accuracy, cost and prompt choices; page 12 discusses real user feedback, scope and conclusions.

The experiments build on DAIL-SQL and separate Simple, CQs and CQs&ES variants across two models and two datasets. Main-experiment feedback comes from a GPT-4o oracle with access to gold SQL; an additional 11-person study supplies a different kind of evidence. Figure 3 and Tables 3–4 jointly show accuracy, rounds, cost, and schema matching. The early-stopping analysis explicitly considers accuracy/cost tradeoffs.

## Transferable interpretation
The argument demonstrates the problem before introducing components, and evaluates interaction quality together with burden. An accuracy headline alone does not capture the evidence. Oracle feedback is useful for a controlled study but does not establish real-user effectiveness.

## Proposed review questions, not source requirements
For a new interactive method, define action inputs/outputs and failure conditions; distinguish mechanism novelty from a new setting. Compare matched base models, information and interaction budgets, while also reporting unmatched-budget tradeoffs where useful. Evaluate correct clarification, post-interaction correctness, refusal/coverage and user burden. Separate gold-aware oracle, independent human interaction and real deployment evidence. Test erroneous or absent feedback without leaking gold into the tested method.

## Follow-up close reading
For the 2026-11-19 abstract/method/figure functional analysis and citation-count qualification, read [the close-reading appendix](sphinteract-close-reading.md). Its review actions are analyst recommendations, not official rules.
