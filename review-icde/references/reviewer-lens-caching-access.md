# Reviewer lens: result caching, view reuse, and fine-grained access control (ICDE)

Built on 2026-11-10 from two independent mock-review rounds of a permission- and version-safe result cache
(ScopeCache, ICDE 2027 R2; three reviewers per round, scores WA/WR/WA) and from the accepted papers in
`write-icde/references/limitations-writing-caching-access.md` and `limitations-writing-reachability.md`.
Use it in addition to `reviewer-lens.md`. In pre-submission mode a reviewer may request added, supplemented,
re-run or removed experiments, and the authors run them before submission.

## 1. Questions every reviewer in this area asks

| # | Question | Evidence that answers it | Typical request if missing |
|---|---|---|---|
| 1 | Is the new idea isolated from the engineering around it? | A baseline that shares every component except the idea (e.g. the same lifting, measure bundles and pinned views, but partitioned by scope) | Add the "same machinery, partitioned" baseline on the full grid |
| 2 | Is the strongest classical design in the comparison? | Materialized views with a query-time row filter (VPD over views), selected on the same training prefix; an adaptive variant that re-selects and pays its rebuilds | Add VR-adapt; report rebuild cost as warehouse work |
| 3 | Is every answer correct, and checked by something other than the system's own code? | Value-by-value differential test against fresh execution; an independent oracle (formulas in SQL) on sampled calls | Re-run the safety table with the independent oracle |
| 4 | Are the unsafe designs really unsafe on the paper's workloads? | Over-privileged / stale counts for intent-keyed and TTL caches, adversarial replay after revocation | Add the adversarial replay at a high event rate |
| 5 | Does it scale? | TPC-H/TPC-DS at SF10+ or a real warehouse; policy-domain sweep up to owner-level scopes | Add one large-scale run and a domain sweep |
| 6 | Are the policies realistic? | A real grant set (de-identified) or a cited role-mining dataset; synthetic generators described with precedent | Add a real-grant setup; report scope-size distribution |
| 7 | Are the numbers reproducible? | Deterministic counts for a seed; no eviction/selection driven by wall-clock time on a shared machine; mean ± sd over seeds | Make costs deterministic and re-run; move wall-clock claims to an isolated machine |
| 8 | What about timing side channels? | Threat model names the observables; a mitigation (uniform miss latency) that keeps the claimed cost metric | One sentence in the threat model; never "needs its own analysis" |
| 9 | Do events (revocation, grant edits, republishes) cost anything? | Event-rate sweep; snapshot-flush ablation; theorem on zero invalidation | Add the sweep at 0/4/16x |
| 10 | Is the standing of the method visible? | Best bold, second underlined (ties share), a best/second count column, one "Standing" sentence per RQ | Mark every results table |

## 2. Presentation checks specific to this area
- Infrastructure sentences that undermine all numbers ("the machine was shared", "counts differ between
  reruns") are a P0 even if true: fix the cause (deterministic cost, isolated timing) and then state the
  setup neutrally.
- Ranges taken over individual traces/runs that overlap with a baseline's range look like no gain; report
  setup means when the figure shows means, and keep per-run ranges in tables.
- A tie with the strongest competitor is stated with its mechanism and next to the regime where the method
  wins ("matches X where views already cover the shareable calls; up to 19% fewer as the domain grows").
- An ablation that looks dispensable needs the regime where it matters (lifting saves 21-46% on the online
  path even if it is within 6% once views are pinned).
- "only", "barely", "none", "needs its own analysis", "cannot tell" about the paper's own method or data are
  flagged by the reviewer as self-negation.
