---
name: pvldb-cache-reuse-anatomy
description: "Section-by-section anatomy of published PVLDB papers on caching, result reuse and access control (STsCache PVLDB 18, Crystal PVLDB 14, Microsoft Purview PVLDB 16, Sieve PVLDB 13), turned into a two-gate reviewer loop for a candidate PVLDB paper in that direction. Gate A: does the proposed method beat every baseline on every reported metric, and if not, what algorithm-level change is required. Gate B: is the manuscript, from title to references, at the level of these published papers. Use when writing, self-reviewing or acceptance-reviewing a PVLDB paper about a cache, semantic/result reuse, materialized views, permission-aware or policy-aware query processing (写/审 PVLDB 缓存论文、结果复用、权限感知缓存、范文对齐、全指标超过 baseline、Gate A/Gate B、审稿循环)."
---

# PVLDB cache / result-reuse / access-control paper anatomy

Four published PVLDB papers were read in full and deconstructed down to sentence function (see `references/exemplars/`):

| ID | Paper | Venue | Why it is an exemplar |
|---|---|---|---|
| STS | STsCache — semantic cache for time-series workloads | PVLDB 18(9), 2964–2977 | semantic result reuse; resource-matched and reimplemented baselines; 25 figures |
| CRY | Crystal — cache storage for analytical databases (Durner et al.) | PVLDB 14, 2432–2444 | cache of query regions across DBMSs; cost-based (knapsack) admission; 16 figures |
| PUR | Microsoft Purview — data governance / access control incl. SQL Server permission-decision caches (Ahmad, Kaushik et al.) | PVLDB 16(12), 3624–3635 | permission caching and revocation in a production system |
| SIE | Sieve — middleware for scalable fine-grained access control (Pappachan et al.) | PVLDB 13, 2424–2437 | policy-aware query rewriting with a cost model and security criterion |

Official PDFs: `https://www.vldb.org/pvldb/vol18/p2964-li.pdf`, `vol14/p2432-durner.pdf`, `vol16/p3624-kaushik.pdf`,
`vol13/p2424-pappachan.pdf`. Page numbers in the references are PDF or proceedings pages as each file states.

Companion skills: `review-pvldb` (official process, self-negation pass), `submit-pvldb` (format, caps, declarations),
`pvldb-paper-craft` (layout checks), `vldb-exemplar-sop` (12-paper general PVLDB distribution). Official PVLDB pages
always win over anything here. Never output an acceptance probability.

## When to use

- Writing a PVLDB paper whose contribution is a cache, a reuse mechanism, a view/predicate/result store, or policy-aware query
  processing, and you want the structure of published papers of exactly that kind.
- Acting as the **independent reviewer** of such a paper in a reviewer/fixer loop (`references/review-loop.md`).
- Deciding whether the experimental evidence is enough: run Gate A (`references/gate-a-all-metrics.md`) before arguing about prose.

## Workflow

1. **Freeze the object.** Record the exact PDF/source hashes, page count, and the DEV/TEST evidence files you are judging.
2. **Gate A first.** Build the all-metric dominance matrix (`references/gate-a-all-metrics.md`): every metric the paper or its
   artifacts report, every baseline, per cell and in total. Classify each row PASS / PARTIAL (ties) / FAIL / MISSING.
   For every non-PASS row write a *method-level* requirement with an acceptance test. Wording changes never close a Gate-A row.
3. **Fingerprint.** Count pages per section, figures (and result panels), tables, algorithms, formal claims, baselines
   (external vs author-built), metrics, datasets/workloads and scale, references (total, DB-venue share, year bands).
   Compare with `references/fingerprints.md`. A number outside the exemplar range is a question, not automatically a defect.
4. **Section-by-section alignment.** Walk `references/section-anatomy.md` from title to references. For each rule record
   met / partial / gap, with the manuscript location and the exemplar evidence.
5. **Write the review** as: verdict per gate → Gate-A matrix → Gate-B findings ordered by impact → numbered fix requests
   (ID, input, required change, acceptance test). Send fix requests to the fixer; do not fix them yourself in the same role.
6. **Re-review** each new delivery against the previous fix list; a request closes only when its acceptance test is met on the
   new exact version. Approve only when both gates pass.

## The ten things these exemplars all do (and weak candidates usually miss)

1. **A system spine.** One architecture figure early in the design section; its modules map one-to-one onto design
   subsections and later onto experiment subsections (STS Fig. 5; CRY design overview; SIE overview).
2. **Gap as named mechanisms, not adjectives.** Prior work is critiqued by system name with concrete mechanism drawbacks,
   which become 2–4 named challenges; each design mechanism is mapped back to a challenge (STS intro; CRY
   "Challenges → Opportunities → Introducing X").
3. **Formalism after the example.** Concrete queries first, then the definition, then an immediate worked example (STS §3;
   SIE case study before the model).
4. **Cost model before the algorithm.** The admission/rewrite decision is a stated cost model (CRY knapsack, SIE read-cost
   vs evaluation-cost) and every adaptive switch is validated with a crossover plot (SIE Figs. 3–4).
5. **Every constant justified.** Each magic number is forward-referenced to the experiment that justifies it (STS slab size,
   batch size).
6. **Performance is measured, not modeled.** Throughput and/or end-to-end latency on a real engine (often two engines:
   CRY Spark + Greenplum, SIE MySQL + PostgreSQL). Counting proxies (hits, executions) are supporting metrics, never the
   only performance evidence.
7. **Fair, resource-matched baselines including at least one outside system.** External systems run as released; unavailable
   ones are reimplemented on the same code base "strictly following" the original; resource budgets are equalized and
   stated; if a baseline cannot run the benchmark, the paper says why and gives it an equal-resource tailored workload (STS).
8. **Trade-offs with numbers, once, next to the result.** The regime where the method stops paying off is shown by a sweep
   of the property that drives reuse together with the one that drives overhead (STS overlap × request size; cost stated as
   −6–15 % throughput for −75 % memory).
9. **Claims scoped once, then not repeated.** Assumptions are stated in the problem section or a short scope paragraph; the
   abstract, intro and conclusion do not re-disclaim them sentence by sentence.
10. **Numbers in the abstract are traceable.** Every abstract number appears verbatim in the evaluation (STS is a negative
    example: one abstract number is nowhere in §5).

## What not to copy blindly

- STS assumes consistency away (append-only data) and gives no correctness theorem; a permission-aware cache must model,
  prove and evaluate invalidation/revocation.
- CRY has no repetitions, error bars or ablation of its approximate-merging step; SIE has no error bars and leaves security
  correctness to a citation. Published ≠ flawless: align with the *strengths*, not the gaps.
- Industry papers (PUR) can lean on deployment narrative without controlled baselines; a research-track paper cannot.

## Output format

Reports to the author in Chinese; any simulated PC review text in English. Each finding: severity (blocking / major / minor),
manuscript location, exemplar evidence (paper ID + page/section), required change, acceptance test.
