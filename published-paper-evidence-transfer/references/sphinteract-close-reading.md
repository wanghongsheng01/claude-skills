# Sphinteract: close-reading functions and review actions

Source: https://www.vldb.org/pvldb/vol18/p1145-zhao.pdf · DOI: https://doi.org/10.14778/3717755.3717772

## Coverage, 2026-11-19

This pass revisited the abstract, introduction, section 6.2, Algorithm 1, experiments and references, with visual checks of printed pages 1150 and 1153. The labels below are analyst-created functional labels, not original paper labels. This is not a sentence-level annotation of the entire paper. The notes paraphrase; they do not reproduce the paper's sentences, prompts or diagrams.

## Abstract and introduction as argument

The eight abstract sentences perform these functions in sequence: establish the task; acknowledge progress; isolate an unresolved issue; introduce the approach and goal; describe an intervention; identify its mechanism; outline the strategy family; summarize evaluation scope and a strongest result. Eight sentences is an observation, not a template requirement.

A useful review action is to label a candidate abstract by function, then check that the gap has a nearest-neighbour comparison, the intervention is more specific than merely using an LLM, and the evidence sentence has an identifiable result source. A maximum gain needs its comparator and scope; it is not a substitute for overall results.

The introduction moves from broad task importance to a specific problem, uses a small ambiguity example, generalizes the cause, distinguishes prior interactive approaches, and then presents the solution and contributions. A candidate running example should genuinely distinguish competing interpretations, rather than silently assume the chosen answer. Reuse its objects across the definition, algorithm trace and failure analysis where that helps the argument.

## Method paragraph functions

Section 6.2 proceeds from simple feedback to richer questions and explanation strategies. Its local functions suggest concrete checks:

| Observed function | Proposed candidate review action |
|---|---|
| Establish a basic feedback-and-update procedure | Identify the stored state after a failed answer and the next invocation's input |
| Separate external feedback from model-generated feedback | Record who supplies feedback and what information they can see |
| Motivate a richer question through a basic strategy's weakness | State a testable mechanism rather than only naming a module |
| Describe history in generation and questioning | Trace actual state through both call sites, prompts and logs |
| Translate concepts into an operational sequence | Identify removable steps for a valid ablation |
| Constrain the response format | Specify malformed output, no suitable choice and free-text handling |
| Recognize failure after clarification | Separate remaining semantic uncertainty from generator limitations |
| Explain continued interaction versus stopping | Fix a stopping rule and measure both quality and interaction cost |

The pseudocode and surrounding prose warrant a consistency check about which history reaches which stage. This observation alone does not establish an implementation bug; inspecting the actual functions, prompts and execution traces is needed.

## Figure and table roles

The paper's figures serve different questions: human ambiguity judgments, interaction flow, accuracy versus rounds, few-shot sensitivity, and user feedback. Tables cover category examples, zero-shot performance, cost/efficiency, structural matching, few-shot performance and prompt-information controls. A candidate should preserve this division of evidentiary labour, not copy the number of figures or their layout.

The framework visualization on printed page 1150 separates user and system regions and uses step numbers and feedback loops. For a new figure, make transmitted objects, information permissions, state updates and stopping conditions explicit. A diagram that only connects named agents does not show the mechanism. Check the drawing against executed traces, not only the prose.

When translating results to a candidate review:
- Distinguish a clarification round, SQL generation and model call; they are not interchangeable denominators.
- Report percentage-point and relative changes separately.
- Identify whether cost includes feedback generation and retries. If oracle cost is excluded, state that and, where possible, provide a total-cost view.
- Keep quality/cost tradeoffs visible; a curve does not prove universal dominance.
- Explain sample size, uncertainty, model/data versions and axis choices.

## General-purpose verification card

For each check, record `PASS`, `FAIL`, `BLOCKED` or `NOT_APPLICABLE`, along with evidence version and what would permit re-evaluation. No evidence is not a pass.

1. Nearest-neighbour increment has a falsifiable comparison.
2. Prompt/threshold/model-selection inputs are distinguished from evaluation inputs.
3. Oracle, simulated human and actual participant evidence are labelled separately; AI role-play is not independent human annotation.
4. Baselines have explicit implementation, information and resource contracts.
5. Predictions, failures and aggregation procedures can reconstruct headline tables.
6. Mechanism or ablation evidence supports each new component's claimed effect.
7. The evaluation measures the risk/coverage and interaction consequences relevant to the task, not accuracy alone.
8. Benchmark studies preserve legitimate alternative interpretations and uncertainty rather than require the authors' method to win.
9. Claims and units match measured results; untested generalizations remain untested.
10. The final PDF, algorithm and implementation are checked for consistency at the level actually inspected.

These are proposed internal review checks, not PVLDB's official scorecard. Existing user acceptance targets remain targets: report unmet targets rather than silently replacing them with this checklist.

## What not to transfer

Historical model versions and baseline choices are not automatically sufficient for a new paper. Published examples are fallible: 76 numbered bibliography entries are not 76 verified unique papers. Entries 17/18 point to the same title/authors/volume/pages; entries 71/72 warrant a version-deduplication check. Do not copy duplicates or convert the count into a required bibliography size.

An accepted paper is evidence that this particular argument was published, not that a similar abstract or checklist guarantees acceptance. Generic active clarification and the observation that annotations affect rankings already have prior work; a candidate must identify its own narrower increment.
