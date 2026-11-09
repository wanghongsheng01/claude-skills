---
name: pr-experiment-design
description: Turn an evidence-backed Pattern Recognition research question into falsifiable hypotheses and fair experiments, after venue learning and full-text baseline analysis are complete.
---

# Pattern Recognition hypothesis and experiment design

Use after the literature learning stage or when the user explicitly asks for experiments. It does not authorize purchases, external data writes, use of private data in models, or premature experimentation during a requested survey.

## Enter with a scientific gap

Require an explicit problem, strongest relevant published baselines, their failure conditions and a candidate mechanism. Popularity, a new model name or a combination of modules is not a sufficient gap. Compare the proposed mechanism with the nearest prior mechanisms and a cheap alternative such as reweighting, thresholding, regularization or better tuning.

Write a falsifiable prediction before running experiments: the intervention, expected change, metric, conditions, and an outcome that would reject the explanation. Separate utility claims from mechanism claims. Decide whether the task actually needs an LLM; API availability does not determine venue fit.

## Design decisive controls

Match supervision, external data, pretrained backbone, tuning budget, candidate count and inference resources. When exact equality is impossible, report both performance and resource frontiers. Include a simple repair of the strongest baseline and isolate each claimed mechanism through an intervention or independent ablation. Removing two interacting modules together cannot identify each module's contribution.

Retain a relevant state-of-the-art method with additional labels or private/pretraining data in an explicitly separate reference group. Make the main causal comparison within matched supervision and resource strata. A performance/cost frontier does not erase unequal information access; do not call the resulting differences pure algorithmic gains.

Use train/development splits for tuning and freeze the final test protocol. Group correlated observations by subject, object, scene, sequence, source or domain as appropriate. Fit preprocessing only on permitted data. Prespecify metrics and uncertainty units, record all seeds and failed runs, and distinguish training seeds from repeat inference on fixed weights.

Start with the smallest experiment able to refute the claim. Expand only if it survives meaningful baselines. Report null and negative results; stop or revise a hypothesis that fails rather than hiding the failure with a new headline metric.

Published PR cases motivate these distinctions: [SAMOSA Table2](https://doi.org/10.1016/j.patcog.2023.109909) separates regularization from synthetic-example gains; [Back-to-Bones Tables1/4](https://doi.org/10.1016/j.patcog.2024.110762) separates backbone and algorithm effects; [SigTree Tables2/5](https://doi.org/10.1016/j.patcog.2025.111364) measures clustering quality and rule complexity; [Big-Clust §6–7](https://doi.org/10.1016/j.patcog.2025.111654) makes the quality/time tradeoff explicit. These are methodological examples, not instructions to repeat their exact seeds or thresholds.

## Record enough to reproduce the conclusion

Save data version/license and split hashes, code commit, complete configuration, interpreter/libraries, hardware, model/API version, raw per-observation outputs, aggregated metrics, logs, runtime and cost. Recompute tables and figures from those saved records. Specify the timing boundary and whether preprocessing, feature extraction, training and inference are included.

For API experiments use the user's approved DataHub/LLM route and per-model budget. Confirm current price and all same-model usage contributing to the daily cap; reserve worst-case cost before calls. Preserve provider failures and retries. Do not silently switch providers or model versions, and never commit credentials.

Deliver a preregistered-in-project protocol (do not claim external registration), run manifest, baseline fairness table, raw-to-table scripts, ablation/intervention results, generalization/efficiency/failure evidence and a claim-evidence map for writing. A protocol is not an experimental result.
