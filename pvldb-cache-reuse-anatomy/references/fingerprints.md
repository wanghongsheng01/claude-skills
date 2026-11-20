# Fingerprints of the four exemplars (counted from the official PDFs)

| Item | STsCache (STS) PVLDB 18 | Crystal (CRY) PVLDB 14 | Sieve (SIE) PVLDB 13 | Purview (PUR) PVLDB 16, *industrial* |
|---|---|---|---|---|
| Total / body pages | 14 / 12 | 13 / 12 | 14 / 12 | 12 / ≈11.7 |
| References | 80 (≈29 core-DB, 13 PVLDB, 20 URLs) | 52 (25 PVLDB/VLDB/SIGMOD/ICDE, 19 web) | 34 | 19 (all product/web) |
| Figures (result figures) | 25 (16) | 16 (10; 26 panels) | 6 (5) | 4 (1) |
| Tables | 2 | 1 | 4 | 0 |
| Algorithms | 4 | 3 | 1 | 0 |
| Definitions / theorems | 5 / 0 (+2 worked examples) | 0 / 0 | 0 / 2 (+NP-hardness) | 0 / 0 (+11 examples) |
| Contribution list | 4 bullets, "We propose" | bullets with § pointers | none (prose) | none |
| Numbers in abstract | 7 ranges | none | none | none |
| Numbers in intro | none | yes (up to 20×, 8× avg, 41 %) | none | none |
| External-system baselines | 4 (2 TSDBs, TSCache, BSCache reimpl.) + resource-matched dual server | 2 (Spark, Alluxio) + 6 internal variants | 0 (3 author rewrite variants) + 2 ablations | 1 (no-Purview) + caching-off |
| Engines / hosts | 2 TSDBs | 2 (Spark 3.0.1, Greenplum 6.16) | 2 (MySQL, PostgreSQL) | SQL Server |
| Data / workloads | 2 TSBS cases × 3 scales (26–423 GB, ≤50.5 B points) + 3 production-style | 4 datasets (TPC-H SF50 …), 5 patterns | 2 (real 3.9 M events; synthetic) ; 869 K and 19 K policies | TPC-C-like W=200 |
| Primary performance metrics | throughput, mean e2e latency, hit ratio (full/partial) | latency distributions, CDFs, time series, bytes, background cost | generation/eval time, speedup | normalized throughput |
| Explicit RQs | 0 (6 subsections by module) | 0 (7 goal subsections) | 0 (5 numbered experiments) | 0 |
| Sweeps / ablations | 8 / 5 | several / central step not ablated | crossover plots / 2 | load sweep / caching-off |
| Statistics | mean of 5 runs, no error bars | none | none | single run |
| Experiments, pages (% body) | ≈4.0 (33 %) | ≈3.1 (26 %) | ≈2.9 (24 %) | ≈0.95 (8 %) |
| Related work | §2, early, ≈0.7 p, 4 groups | end, ≈1 p, 5 groups, 26 refs | §2.2, early, 3 groups, 11 refs | short |
| Artifact | badge + link p.1 | workload queries only | GitHub + extended version | none |

## Ranges a research-track candidate should be compared with (STS, CRY, SIE only)

- Figures 6–25; result figures 5–16. Tables 1–4. References 34–80 (median of the three: 52).
- Experiments 24–33 % of the body (2.9–4.0 pages). External systems run: 0–4, but every paper either runs an outside
  system or reimplements a published one; each paper uses **two** engines/hosts or a resource-matched configuration.
- Measured performance (latency and/or throughput on a real engine) is the primary result in **3/3**. No paper relies on
  a count proxy (hits, executions) as its only performance evidence.
- Statistical treatment is weak in all three (≤ 5 runs, no error bars); a candidate that reports repetitions and CIs exceeds
  the exemplars there and should keep doing so.

General PVLDB distribution (12 accepted papers, `vldb-exemplar-sop`): figures 4–16 (median 7), tables 0–17 (median 3),
experiments 15.5–44 % of the body (median 27.8 %), intro 0.78–2.2 pages, related work 0.38–1.9 pages.
