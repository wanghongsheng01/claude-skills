---
name: published-paper-evidence-transfer
description: Learn from formally published database papers by tracing claims to mechanisms and evidence, then turn those observations into bounded review questions and experiment plans for a candidate manuscript. Use for paper dissection and evidence transfer, not as a venue acceptance predictor.
---

# Transfer evidence design from published papers

Use this skill when a manuscript needs more than a stylistic imitation of accepted papers: identify what makes an argument testable, how the evidence separates explanations, and which habits transfer to a different problem. For official requirements, use the current venue CFP; for EA&B protocol review, complement rather than replace `pvldb-eab-review`.

## Evidence available here

This corpus contains five purposively selected formal publications, not a representative venue census. Read only the relevant note:
- Interactive text-to-SQL methods: [Sphinteract](references/sphinteract.md).
- Benchmark validity and reevaluation: [Annotation-error audit](references/annotation-errors.md).
- Industrial resource-management design: [ProRP](references/prorp.md).
- Industrial architecture and governance: [BigLake](references/biglake.md).
- Industrial metadata provenance and operational reasoning: [Goods close reading](references/goods-close-reading.md).
- For finer abstract, method-paragraph and figure checks after the Sphinteract overview: [Sphinteract close reading](references/sphinteract-close-reading.md).

Each note distinguishes observed paper structure, interpretation, proposed transfer, and reading limits. Neither acceptance rates nor hidden reviewer preferences can be inferred from this sample. Reference counts, section orders, and figure counts are descriptions, not targets.

## Work from an argument, not a template

1. **Define the candidate's decision.** State its object, inputs, outputs, assumptions, and the decision a reader can make differently. Distinguish a method contribution, an empirical finding, and industrial operating guidance.
2. **Make the closest-neighbour contrast explicit.** Record what the published paper already establishes, what is actually new in the candidate, and an experiment that could falsify that increment. A changed business setting alone is not a new mechanism.
3. **Trace a headline claim.** Link claim → mechanism or hypothesis → comparison → experimental unit and denominator → measurement → scope. Mark missing links; do not repair them by rhetoric.
4. **Design a discriminating test.** Control the strongest competing explanation. Match available information and budgets where the comparison requires it; separate oracle feedback from real users, cached recomputation from fresh inference, replay from production deployment, and static analysis from observed operational effects.
5. **Read prose as argument.** For a paragraph, record its question, new assertion, evidence pointer, scope, and logical relation to adjacent paragraphs. For a sentence, distinguish definition, claim, procedure, observation, explanation, and boundary. An explanation is not automatically causal evidence.
6. **Check figures against decisions.** Identify the question each figure/table answers, its units, population, uncertainty, comparison conditions, and losses or costs. The prose should explain the result and boundary, not restate every cell.
7. **Deliver a bounded plan.** Separate presentation fixes, missing experiments, correctness defects, and submission-eligibility issues. Give each proposed task a hypothesis, required inputs, measurable completion condition, and dependency. Stop at recommendations when the user has not authorized edits or experiments.

## Type-specific transfer

- **Method paper:** show the incremental mechanism against the closest runnable neighbour; test ablations and failure regimes, not just a champion score.
- **EA&B:** seek insight about systems or measurement. A simple baseline winning, tied rankings, or a metric-dependent ordering can be a finding. Do not force an invented method victory.
- **Industrial:** show requirements, design alternatives, deployment boundary, and operational lessons. Label rollout, replay, simulation, and case studies separately. Do not turn potential avoided work into realized cost savings.

## Executable review worksheet

For a candidate-level audit, use the [claim-to-evidence worksheet](references/claim-review-template.md). It connects per-metric outcomes and budget comparability to paragraph, figure, citation, repair and revalidation anchors. Keep completed candidate worksheets private.

## Output

Produce a concise author-facing report with: source and reading depth; observed design; candidate-specific inference; proposed test; what would refute the claim; and remaining uncertainty. Keep the candidate report private. Only public-source paraphrases and generic transferable lessons belong in a public skill repository.

## Boundaries

Do not upload copyrighted PDFs or long extracts; retain official/author-hosted source links and paraphrase. Do not copy private drafts, enterprise data, manuscript-specific vulnerabilities, credentials, or unpublished results into this skill. Do not select test inputs after seeing outcomes, weaken baselines, hide failed cells, or treat a simulated review as a real decision. A source-reading claim must match actual work: text extraction, selective visual inspection, full visual inspection, and sentence-level annotation are different depths.
