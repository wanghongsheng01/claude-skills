# Claim-to-evidence review worksheet

Use this worksheet for one candidate paper and one explicitly identified draft. This is a review artifact, not a source of permission to alter a paper, rerun a test, publish data, or submit. Keep completed worksheets private when they contain unpublished or proprietary information. A public skill should retain the empty template and generic method only.

## 1. Identify the decision and material

- Draft/version and date:
- Target venue, cycle and category:
- Current official rules URL and check date:
- Main reader decision or falsifiable claim:
- Closest published neighbour and precise proposed increment:
- Evidence actually inspected (source, results, logs, PDF pages); missing material:
- Reading depth: extracted text / selected visual pages / all-page visual review / paragraph or sentence annotations. Record which was done, not which was requested.

## 2. Claim ledger

| Claim ID | Exact draft location | Proposed claim and scope | Alternative explanation | Evidence IDs | Counterexample or result that would weaken it | Status |
|---|---|---|---|---|---|---|
| C1 | section/paragraph/line | object, setting, outcome | budget, label, workload or mechanism confound | run/table/figure IDs | prespecified disconfirming outcome | supported / qualified / contradicted / untested |

A persuasive rewrite cannot turn contradicted or untested evidence into supported evidence. A narrowed claim needs its own explicit scope; it does not erase the original failure.

## 3. Comparison contract

For each comparison, record task, input population, split/version, unit of analysis, paired/unpaired status, exclusions and denominator; baseline implementation/version and tuning; visible labels, schema, contracts, feedback and other information; model/version; hardware; time, calls, tokens, interaction and training budgets; metric direction, failure handling, repetition and uncertainty.

A same-budget label must name the budget matched. Equal calls do not imply equal tokens, equal information, equal wall time or equal cost. Report unmatched-resource comparisons separately when informative. Cached replay cost is not historical inference cost. If units, available information or budgets differ materially, label the comparison incomparable or qualified rather than manufacture a winner.

## 4. Per-metric result ledger

| Claim / comparison ID | Metric, unit, direction | Population and n | Candidate value | Strongest actually-run comparable baseline | Delta and uncertainty | Win / tie / loss / incomparable | Failures or missing cells | Provenance |
|---|---|---|---|---|---|---|---|---|
| C1/B1 | specify ↑ or ↓ | denominator, exclusions | observed, not estimated | method/version and value | absolute/relative; CI if supported | declared rule | count and reason | immutable run + table generator |

- Keep every prespecified metric and measured cell. Show failed, timed-out, missing and unsupported cases explicitly; they are not wins and must not silently disappear from denominators.
- Define the tie rule before interpreting results. Nonsignificance does not demonstrate equivalence; printed rounding ties do not prove scientific equivalence.
- Identify both the strongest comparable baseline per metric and a stable named baseline across the main comparison. Do not quietly switch comparators to maximize wins.
- A win/tie/loss count is descriptive, not an official acceptance threshold. Do not average incompatible units or count a derived duplicate as independent evidence.
- Loss explanations require measured diagnostics or clearly labelled hypotheses. Test the hypothesis or retain it as unresolved.

## 5. Manuscript anchors

| Claim ID | Paragraph function | Evidence pointer in text | Figure/table ID and reader question | Citation anchor and supported fact | Scope/uncertainty stated where? | Requested change |
|---|---|---|---|---|---|---|
| C1 | define / claim / method / observe / explain / bound | section + result ID | question, population, budget, units | citation + source page/section | one clear factual boundary | retain / clarify / reframe / test |

For every headline number, compare the abstract, introduction, table, caption and conclusion against one source of truth. Figures should make comparison conditions and tradeoffs legible. References justify a specific fact or contrast; a published paper's reference count is descriptive and never an official quota. Do not turn a reference into an assertion that a baseline was locally reproduced.

## 6. Category-specific decision

**Regular research:** assess the precise increment over the closest work, technical depth, correctness within the stated assumptions, and experiments that distinguish the claimed mechanism. A high score cannot repair a false theorem or missing novelty. Not every metric must win.

**EA&B:** assess the evaluation object, new insight or workload characterization, representativeness, protocol validity and decision consequences. A tie or a simple baseline winning may be the main finding. Check the target cycle's initial-submission artifact requirement against all main experiments, not only one cached reproduction. Do not require an invented new method or universal winner.

**Industrial:** assess requirements, operational design choices, generalizable lessons, actual rollout boundary and measured effects. Distinguish production, replay, simulation and static analysis. Actual cost savings require evidence beyond potentially avoidable work. Check current affiliation/format/overlap eligibility separately.

## 7. Repair and verification plan

| Priority | Defect class | Affected claims | Proposed repair | Required input/authorization | Verification and stop condition | Outcome |
|---|---|---|---|---|---|---|
| P0 | correctness / evidence / eligibility / presentation | IDs | minimal discriminating change | data, compute, author decision | exact regression, new test or document check | pending / passed / failed / blocked |

- Separate editorial changes from method changes and experiments. Preserve frozen results and the original dataset; label developmental checks, reruns, newly frozen evaluation and corrections accurately.
- After a repair, rerun affected validation only within authorization, regenerate dependent tables and recheck every affected claim anchor. Record both successful and failed repairs.
- Do not retune on a held-out set and continue calling it untouched. If the evaluation role changes, document that and design an independent confirmation when warranted.
- Close with: supported conclusions; unresolved blockers; evidence needed to reconsider; and whether the next step is review, revision or author decision. Do not promise acceptance or quietly convert the plan into execution.
