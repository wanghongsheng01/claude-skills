# Experiment-analysis guidance from 邓老师's meetings

Canonical quotes and source files: `../../paper-presubmission-review/references/deng-meeting-lessons.md` (sections 3–4). This file exists so a later `experiment-analysis-writing` skill, or a co-worker committing to the same branch, can link here **without rewriting** `write-vldb/SKILL.md` §§1–6 or `official-rules.md`.

Operational rules to apply when designing or writing PVLDB experiments:

1. A result table that wins some datasets and loses others must discuss both regimes and give takeaways. Second-best with a mechanism is acceptable; "all best" is not required and is not realistic.
2. Add an average (or geometric-mean) row when ups and downs hide the overall effect. This is not a substitute for the Best/2nd count row.
3. Argue *problem necessity* with a compact figure if existing iterative repair still leaves residual error. Do not spend body pages on low-information module-ablation charts.
4. Empty regions and anomalous aggregate curves must be explained or redrawn (box plot). 95% CI is acceptable.
5. Public data carries the main conclusions (already in write-vldb §4). Enterprise numbers are supplementary.
6. Page budget is a first-class review item: PVLDB appendix counts toward the 12-page body.

Official PVLDB pages always win when they conflict with this advice.
