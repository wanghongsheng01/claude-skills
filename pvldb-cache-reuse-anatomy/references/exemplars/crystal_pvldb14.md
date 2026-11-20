# Exemplar deconstruction: Crystal (Durner, Chandramouli, Li), PVLDB 14(11), 2021

Source read in full: `downloads/pvldb_exemplars/p2432-durner.pdf` (13 PDF pages) + `p2432-durner.txt` (pdftotext -layout); figure layout checked on 60-dpi page renders of pp. 2436, 2440-2442.
Page numbers below are the printed proceedings page numbers (PDF page 1 = p.2432, PDF page 13 = p.2444). All passages are paraphrased; quoted fragments are short terms only.

---

## 1. Bibliographic facts

| Field | Value (evidence) |
|---|---|
| Title | Crystal: A Unified Cache Storage System for Analytical Databases (p.2432) |
| Authors / affiliation types | Dominik Durner (academia: TU Munich; footnote says work done at Microsoft Research), Badrish Chandramouli (industry: Microsoft Research), Yinan Li (industry: Microsoft Research) (p.2432). Mixed academia-industry, industry-lab-led. |
| Venue | PVLDB Vol. 14, No. 11, pp. 2432-2444, 2021; DOI 10.14778/3476249.3476292 (PVLDB reference box and copyright block, p.2432) |
| Total pages | 13 (pdfinfo: 13 pages) |
| References start | p.2444 (PDF p.13), top of left column; references occupy only that one page |
| Body pages | 12 (pp.2432-2443, incl. Related Work, Conclusion, Acknowledgments on p.2443) |
| Reference count | 52 entries ([1]-[52], counted on p.2444) |
| Figures | 16 numbered figures (Fig.1-16), 26 panels in total (Fig.8: 3, Fig.9: 2, Fig.11: 2, Fig.13: 2, Fig.14: 3, Fig.15: 2, Fig.16: 3, the rest single) |
| Tables | 1 (Table 1, dataset sizes, p.2440) |
| Algorithms | 3 boxed pseudocode listings (Alg.1 p.2436; Alg.2 and Alg.3 p.2438) |
| Definitions / theorems / lemmas | 0 formal environments. Region relations (superset, intersection, partial superset, equality) are defined as a prose bullet list (p.2436); three "geometric rules" are an enumerated list (p.2438). |
| Equations | 0 numbered equations; approx. 8 inline math expressions (0/1 knapsack objective and constraint p.2437; O(n*W), O(n*B), v=b/w, O(n log n) p.2437-2438; O(n^2 log n), container weight/benefit sums, v_k >= v_c >= v_c' p.2438) |
| Footnotes | 1 (asterisk on first author: work done at Microsoft Research, p.2432) |
| Artifact / code availability | No code release statement. Only the regions-workload queries are published via a short link, cited as [12] (p.2440). Software versions and a pinned commit of the Azure client library are given (p.2439). |

---

## 2. Title anatomy

Structure: `<SystemName>: A <Adjective> <Category noun phrase> for <Domain>`.

- "Crystal" - a memorable single-word system name placed first, so the paper is citable as "Crystal".
- "Unified" - the core claim compressed into one word: one cache shared across many DBMSs instead of each DBMS building its own (the gap stated in abstract sentence 3 and the first challenge bullet, p.2432).
- "Cache Storage System" - announces the contribution type (a system, not an algorithm or a theory), which tells reviewers to expect architecture + implementation + end-to-end evaluation.
- "for Analytical Databases" - scopes the domain (read-mostly analytics over cloud storage); consistent with the later read-only scoping (p.2433).
- Why it works: it names the artifact, its distinguishing property, and its scope; it carries no numbers and no hype words; every word maps to a section of the paper (unified -> 2.2 Generality; cache -> 3-4; analytical -> 6 workloads).

---

## 3. Abstract (7 sentences, p.2432)

| # | Rhetorical function | Concrete object / number carried |
|---|---|---|
| S1 | Context: deployment model of cloud analytics | disaggregated storage; elastic compute; remote cloud storage; block-oriented columnar formats |
| S2 | Motivation: why caching matters now | high latency / low bandwidth to remote storage; limited fast local storage; "renewed interest" in caching |
| S3 | Gap / status quo | every DBMS builds its own cache, typically file- or block-level LRU |
| S4 | Proposal: name the system and its placement | Crystal, a "smart cache storage system" co-located with compute |
| S5 | Interface / integration point | clients are DBMS-specific "data sources" with push-down predicates |
| S6 | Key idea + core abstraction | DBMS-like query processing + optimization inside the cache; single-table hyper-rectangles called "regions" |
| S7 | Results (qualitative) | small DBMS-specific connector; lower query latency on unmodified Spark and Greenplum; bandwidth savings |

Observations: the abstract contains **no numbers** (the 20x / 8x / 41% figures appear only in the intro, p.2433). It names the two host systems (Spark, Greenplum) and stresses "unmodified" twice in spirit (S5, S7), reinforcing the integration-cost claim.

---

## 4. Introduction (pp.2432-2433)

Structure: untitled opening (2 paragraphs) + three numbered subsections 1.1 Challenges, 1.2 Opportunities, 1.3 Introducing Crystal. This explicit challenge/opportunity/solution scaffold is the main craft feature.

| ¶ | Page | Function | Key moves |
|---|---|---|---|
| P1 | 2432 L | Context / trend | Analytics moving to the cloud; tiered/disaggregated storage (S3, Azure Blobs); Spark, Greenplum, Hive, Presto query cloud storage directly; vendor services (Athena, Synapse, BigQuery). |
| P2 | 2432 L | Problem + industrial evidence | Remote latency/bandwidth make compute-side caching important; cites three industrial caches (Alluxio, Databricks Delta Cache, Snowflake). |
| 1.1 lead | 2432 R | Gap framing | Existing caches are black-box file/block caches with LRU; they leave architectural and performance challenges unsolved. |
| 1.1 bullet 1 | 2432 R | Challenge: duplication | Each DBMS re-implements what/where/when/how to cache. |
| 1.1 bullet 2 | 2432 R | Challenge: raw formats | CSV/JSON/Avro processing is slower and costlier even when cached; converting everything to columnar is expensive because only a small changing fraction is hot. |
| 1.1 bullet 3 | 2432 R | Challenge: utilization | Page granularity wastes cache space; zone maps cannot skip a block with even one relevant record. |
| 1.1 bullet 4 | 2432 R | Challenge: new storage features | Storage push-down (S3 Select, Azure Query Acceleration) avoids full reads but makes local caching harder to exploit. |
| 1.2 ¶1 | 2432 R | Opportunity 1 | Plug-in data sources with push-down predicates were designed for pruning, but authors "find" they enable semantic caching. |
| 1.2 ¶2 | 2432 R-2433 L | Opportunity 2 | Convergence on Parquet + Arrow/LLVM filtering enables processing outside the DBMS without loss and DBMS-agnostic caching. |
| 1.3 ¶1 | 2433 L | Idea | Crystal as storage middleware / "mini-DBMS" / cache management system (CMS); two sub-components as bullets (CMS on compute node; DB-specific connectors). |
| 1.3 ¶2 | 2433 L | How it works + benefits | Manages SSD cache, chooses regions to transform and cache in columnar form, answers with local or remote paths; 3 benefit bullets (shareable across unmodified DBMSs; automatic semantic regions in open format; independent optimization with multiple views). |
| 1.3 ¶3 | 2433 L | Technical challenges = de-facto contributions | 3 bullets each prefixed with section pointers: "(Sections 2 & 3)" API/protocol; "(Section 3)" downloading/transforming/metadata/matching without hurting latency; "(Section 4)" cache optimization with 5 numbered sub-issues (short- vs long-term, overlapping queries, beneficial duplication, small-file overhead, statistics). |
| 1.3 ¶4 | 2433 R | Results | Lower latency and better bandwidth use vs state of the art; Spark + Greenplum connectors (Sec 5); beats block caching at smaller cache sizes; up to 20x per-query, up to 8x on average, adapts to workload change, up to 41% average bandwidth saving (Sec 6). |
| 1.3 ¶5 | 2433 R | Positioning + scoping + roadmap | Regions relate to materialized views and semantic caches; restriction to single-table predicates (DNF) is exploited, not just tolerated; cross-table predicates, updates, and storage push-down are explicitly deferred; roadmap sentence for Sec 7-8 only. |

Move sequence: context -> problem -> gap (4 challenge bullets) -> enabling trends (2 opportunities) -> idea (system + components) -> benefits -> technical challenges mapped to sections -> quantified results -> related-work hook + limitations -> roadmap.

Contribution list: there is **no "Our contributions are" list**. The contribution role is played by the "technical challenges that we address" list (3 bullets, gerund-led: "Defining", "Efficiently downloading and transforming", "Optimizing"), whose objects are (1) an API/protocol, (2) region download/transform/metadata/matching, (3) cache-content optimization with five sub-goals. Each bullet carries a section pointer (p.2433).

First figure: Figure 1 (ecosystem placement) and Figure 2 (components) sit at the top of p.2433 but are first referenced in Section 2 (p.2433 R), not in the intro. The intro itself is text-only; the first illustrative example (Fig.3) arrives on p.2434.

---

## 5. Remaining sections in order

### 2 System Overview (pp.2433-2434)
- Opening ¶ (2433 R): points to Fig.1; Crystal co-located with each DBMS instance, serving via connectors.
- 2.1 Architecture: design goal stated first (pluggable with minimum engineering effort), then two components.
  - 2.1.1 Data Source Connector (2433 R-2434 L): defines "query"/"requested region" as push-down information; connector is a data source to the DBMS and a client to Crystal.
  - 2.1.2 Crystal CMS (2434 L): Fig.2; two caches - small requested-region (RR) cache and large oracle-region (OR) cache = short- vs long-term knowledge; numbered miss-handling options (1) and (2); RR admitted with LRU-2 per request; OR computed in background by an Oracle Plugin; forward pointers to Sec 3 and 4.
- 2.2 Generality (2434 L): three extensibility points (custom oracle, storage adapter, connector); path-based protocol; Parquet as DBMS-agnostic format; connectors < 350 LOC (forward pointer to Sec 5).
- 2.3 Revisiting the Caching Problem (2434 R): defines regions as views; two-fold advantage over file caching illustrated with Fig.3 (semantic cache covers Q1-Q3, LRU file cache keeps less than half); argues overlap is the norm in warehouses/lakes; claims prior semantic-cache replacement ignores overlap; justifies the RR/OR split with an analogy to C-Store's write store vs read store.
- Craft: the problem is re-stated inside the overview (not in a separate "Problem Definition" section) and the key hard sub-problem (overlap-aware replacement) is foreshadowed with a section pointer to Sec 4.

### 3 Region Processing (pp.2434-2437)
- Lead ¶: scope (matching + creation), then "first we transform requests".
- 3.1 API (2435 L): socket + shared filesystem; path rewriting; completeness guarantee for given predicates and fields; tree-string syntax operation(left,right), atomic predicates, not(exp).
- 3.2 Transformation & Caching Granularity (2435): AST -> NNF (De Morgan, negation pushed into predicates, example not(lt(id,1)) -> gteq(id,1)) -> DNF (distributive law example). Admits worst-case 2^n leaves, says experiments never showed blow-up. Fig.4 worked example (predicate on m, n, c -> two hyper-rectangles). Then a design-decision argument: why NOT split into non-overlapping regions - (a) combinatorial growth, quantified by a mini-experiment (3 random 8-dimensional lineitem queries need 16 non-overlapping rectangles); (b) sampling/statistics cost; (c) each extra region costs ~50 ms in Spark (Fig.5). Conclusion: keep overlapping regions, pay the price in Sec 4.5.
- 3.3 Region Matching (2435 R-2436 L): restriction representation (min/max, equal value, non-equal set, null flags); procedure for superset of restrictions, then conjunctions, then four region relations as a bullet list with set notation; Fig.6 example.
- 3.4 Request Matching (2436 L): Fig.7 flow (OR -> RR -> download); full supersets preferred; overlap requires reduced temp files for correctness (A and B-A example); Alg.1 greedy reduction (pick region satisfying most unsatisfied conjunctions). Partitioning by file-name and schema bitsets; R-trees mentioned as optional, no perf issue observed. No complexity stated for Alg.1.
- 3.5 Creating Regions (2436 R): Parquet + Arrow + Gandiva/LLVM filters; sample created on first access for size prediction and planning.
- 3.6 Client Database Connector (2436 R-2437 L): three control messages (scan request, scan finished, optional sample request).
- 3.7 Cloud Connection (2437 L): file-operation interface; discusses storage push-down cost/latency and argues Crystal complements it; ramdisk download manager with reference counting.
- Formalism style: notation introduced after the intuition and immediately before use (p.2436); examples are given as figures (Fig.4, Fig.6) rather than a single running example.

### 4 Cache Optimization (pp.2437-2439)
- Lead ¶ (2437 L): roadmap of the section.
- 4.1 RR and OR caches: recap; pluggable oracle; default oracle = knapsack variant; background low-priority computation; RR can skip regions already covered by OR; OR can adopt RR regions.
- 4.2 Metadata Management: ring buffer of historic requests with schema, tuple count, size; result statistics from DBMS or samples.
- 4.3 Oracle Region Cache (2437 R): benefit = bytes not downloaded over the history; cost = materialized size; formal 0/1 knapsack stated inline; then states the flaw - static benefits double-count overlapping history elements (forward pointer to 4.5).
- 4.4 Knapsack Algorithms (2437 R-2438 L): DP complexity O(n*W) / O(n*B); two reasons DP fails here (huge W and B; sub-problem optimality breaks under overlap); greedy benefit/cost ratio O(n log n) solving fractional knapsack optimally, cited [24].
- 4.5 Overlap-aware Greedy (2438): Alg.2; recompute ratios after each pick; only ratio > 1 candidates; complexity O(n^2 log n); three geometric rules (superset, subset, intersection) with explanatory paragraphs (1)-(3); honest admission that exact optimality would require exponential branching and that the greedy gives up the fractional guarantee; justified empirically ("our experiments show").
- 4.6 Region Augmentation (2438 R-2439 L): overfitting argument; approximative merging (global min/max over merged predicates, only if intersecting in at least one dimension, delta for neighbors); Alg.3; parameter values for experiments (at most 20% extra regions, max size 20% of semantic cache).
- 4.7 Requested Region Cache (2439 L): LRU and LRU-k; reduce history by RR/OR split; eager-write overhead acknowledged, client-side offload left as future work.
- Claim scoping: assumptions surface where they bite (overlap and double counting in 4.3; optimality loss in 4.5), not in a separate assumptions section.

### 5 Implementation Details (p.2439)
- Stand-alone parallel C++ process; per-connection thread; download thread pool; lock-free / optimistic / fine-grained locks; smart pointers.
- Large unsplit Parquet files handled by translating part offsets to regions.
- Spark data source: < 350 lines of Scala extending Parquet connector, meta-iterator over multiple files, dynamically loaded jar.
- Greenplum: PXF Parquet reader modified with < 150 lines; no recompilation of core DB.
- Neither connector sends regions back; Crystal fills RR itself (a disclosed deviation from the design in 2.1.2).
- Azure connection via azure-storage-cpplite translating to HTTPS/CURL; provider inferred from path.
- Engineering-effort claim quantified in LOC - this is the evidence for "lightweight connector".

### 6 Experimental Evaluation (pp.2439-2442) - see Section 6 below.

### 7 Related Work (pp.2442-2443) - see Section 8 below.

### 8 Conclusion (p.2443) - see Section 10 below.

---

## 6. Experiments in depth

### Goals (no explicit RQs; one goal per subsection)
| Subsection | Implicit goal |
|---|---|
| 6.2 Regions of Query Accesses (p.2440) | Does long-term, overlap-aware OR caching beat other policies on a regional access pattern? |
| 6.3 Crystal vs Block Caching (p.2440-2441) | How does Crystal compare with a production block cache (Alluxio) and file LRU across cache sizes and over time? |
| 6.4 Benefit of RR/OR (p.2441) | Is the combined short-term + long-term design needed under bursty "event" queries? |
| 6.5 Changing Regions (p.2441) | How fast do policies adapt when the hot region moves? |
| 6.6 DB-agnostic design (p.2441) | Does the benefit carry over to a second DBMS (Greenplum)? |
| 6.7 TPC-H (p.2441) | Behavior on a standard benchmark, incl. queries whose predicates cannot be pushed down |
| 6.8 Microbenchmarks (p.2442) | Cost breakdown (online/offline), network footprint, parameter sensitivity |

### Setup (p.2439)
- Hardware: single Azure DS14_v2 VM - 16 cores, 112 GB RAM, 224 GB premium SSD, up to 12 Gbit/s network; Azure Blob Storage standard, hot tier.
- Software: Spark 3.0.1 (pre-built for Hadoop 3.2); Apache Arrow 3.0.0; azure-storage-cpplite at commit be490ed; Greenplum 6.16 (p.2441).
- Not disclosed: Alluxio version and configuration, Spark executor/memory configuration, number of runs.

### Datasets and workloads (p.2439-2441; Table 1 p.2440)
| Dataset | Raw (MB) | Parquet (MB) | Notes |
|---|---|---|---|
| TPC-H SF50 | 54,344 | 16,822 | Q6 template with zipfian shipdate; all 22 queries run twice |
| Lineitem (TPC-H fact table) | 37,701 | 10,915 | main synthetic regions workload |
| NYC Taxi | 32,473 | 6,858 | real-world |
| Stocks (NYSE history) | 19,100 | 4,021 | real-world |

Workload generation follows Tsunami [18]: mixed range and equality filters, 5 query types per dataset. Regions workload: each type's region holds 10-15% of tuples; a query reads 8-13% of a sample of the region (~1% of tuples); 200 precomputed queries per region; 400 queries per run; non-uniform (zipfian) region choice (p.2440). Hot-event variant: event queries recur up to 8 times per 200, mix of 2/3 region and 1/3 event queries (p.2441). Changing regions: hot region shifts after 400 queries, theta = 2 (p.2441). Defaults: cache = 20% of Parquet data size; history = 128 regions; augmentation <= 20% extra regions, max region size 20% of cache (p.2439-2440).

### Baselines / compared configurations (p.2439-2440)
| Name | What it is | Original vs reimplementation | Fairness / disclosure |
|---|---|---|---|
| No cache | vanilla Spark, no code changes | original | reference point |
| Alluxio | widely used block-level analytics accelerator [1,32,33] | original external system | Same cache-size budget as % of data (Fig.9); version/config not stated |
| F-LRU | file/block-level LRU cache | implemented inside Crystal | Authors disclose it benefits from Crystal's optimized Parquet download (p.2441) |
| RR-LRU1 / RR-LRU2 | semantic RR cache with LRU / LRU-2 | inside Crystal | same budget |
| OR-LRU1 | oracle cache driven by LRU | inside Crystal | same budget |
| OR-K_DP | oracle cache with DP knapsack (+ augmentation) | inside Crystal | same augmentation as K_G |
| OR-K_G | proposed overlap greedy knapsack (+ augmentation) | proposed | - |
| F/RR/OR | equal 1/3 split of F-LRU, RR-LRU2, OR-K_G | inside Crystal | combination variant |
| RR/OR | proposed default: RR-LRU2 + OR-K_G, 95% to OR | proposed | - |

Fairness device: cache size is always expressed as a percentage of the remote Parquet data, explicitly "for a fair comparison" (p.2440). Greenplum is configured with as many segments as hardware threads (p.2441). Most competitors are ablation-style variants within the same system, so only two are external (vanilla Spark, Alluxio).

### Metrics reported (all latency/bytes; no throughput, hit ratio, tail percentiles beyond p75, memory, or dollar cost)
1. Per-query latency distribution: violin plots with 25th/50th/75th percentiles and mean (Fig.8, 10, 12, 13b).
2. Mean latency vs cache size (Fig.9a, Fig.16b).
3. Mean latency over query sequence / moving average with window 40 (Fig.9b, Fig.11).
4. Latency CDF (Fig.13a).
5. Per-operation latency breakdown per Parquet part: download, create, match, Spark (Fig.14a).
6. Oracle cache refresh latency (Fig.14b) and summed background compute time (Fig.14c).
7. Total downloaded network traffic in GB (Fig.15).
8. Preliminary: latency overhead per extra region (~50 ms each, Fig.5) and count of non-overlapping rectangles (16 from 3, p.2435).
9. Engineering effort: connector LOC (< 350 Scala, < 150 Greenplum, p.2439).

### Per-figure results
| Fig | Varied | Measured | Headline the text draws (paraphrased) |
|---|---|---|---|
| 5 (p.2436) | # rectangles returned (2-10) | latency | each extra region adds roughly linear ~50 ms in Spark, so splitting into non-overlapping regions is infeasible |
| 8a-c (p.2440) | strategy (9 configs); Lineitem, Taxi cold, Stocks warm | latency distribution | greedy knapsack and RR/OR with overlap adaptation beat all competitors on all three workloads; warm-up shows OR learns a better subset over time |
| 9a (p.2441) | cache size 10%-150% | mean latency after warm-up | RR/OR is fast even with small caches; Alluxio is initially slower than no cache and only matches RR/OR at 110% when everything is local |
| 9b (p.2441) | #queries; 90% vs 110% cache | mean latency over time, cold | traditional caches reach their optimum immediately; RR/OR learns and eventually matches even the 110% setting |
| 10 (p.2441) | strategy under hot events | latency distribution | OR alone misses bursts, RR alone loses long-term trends; only RR/OR handles both |
| 11a-b (p.2442) | #queries with hot-region shift | moving-avg latency | OR-K_G dominates and adapts quickly; OR-K_DP is slow to recover; OR-LRU1 adapts but gains less |
| 12 (p.2442) | strategy on Greenplum | latency distribution | absolute Greenplum latency slightly worse than Spark but relative benefits similar |
| 13a (p.2442) | latency | CDF of Q6 with zipfian dates | (RR/)OR-K_G captures hot regions |
| 13b (p.2442) | strategy incl. Alluxio | 22 TPC-H queries | OR approaches improve mean by up to 20% despite join predicates not being pushable |
| 14a-c (p.2442) | strategy | online breakdown; refresh latency; compute time | download and eager creation dominate online cost; matching adds no visible overhead; K_DP is costly offline; K_G is cheap; OR-LRU1 wastes work on infrequent regions |
| 15a-b (p.2442) | theta 0.6-1.0; Lineitem, Stocks | downloaded GB | RR/OR-K_G uses less traffic than the file-cache baseline; traffic falls with skew |
| 16a-c (p.2443) | theta; cache size 10-30%; history 50-250 | latency | OR strategies beat baseline across skews; 10% cache already good; history < 64 hurts, large history adapts slower |

### Negative results, trade-offs, regimes where the method loses
- p.2441 (6.3): with cold caches, traditional caches reach peak at once while RR/OR needs time to learn; at 110% cache Alluxio matches RR/OR ("only in this extreme scenario").
- p.2440 (6.2): during warm-up, semantic caches are similar and fail to generalize until OR has learned.
- p.2441 (6.4): RR-LRU1 is better on short-term queries; OR fails to catch events.
- p.2441 (6.6): Greenplum's absolute performance is worse than Spark's.
- p.2441 (6.7): on full TPC-H most restrictions come from joins, which cannot be pushed down, so gains shrink to up to 20%.
- p.2442 (6.8): background oracle runs at high nice level, increasing refresh latency under load (framed as protecting the DBMS).
- p.2442 (6.8): history size trade-off (too small mispredicts, too large adapts slowly).
- Design-level admissions: DNF worst case 2^n (p.2435); greedy loses the fractional-knapsack guarantee (p.2438); eager RR writes add overhead (p.2439).

### Ablations
- Policy/component ablation via configuration matrix (F vs RR vs OR; LRU vs LRU-k vs DP vs greedy; single vs combined caches) across Fig.8, 10, 11, 12, 13, 14, 15.
- Not ablated: approximative merging augmentation (both knapsack variants always use it, p.2439), so the claim that K_G benefits most from augmentation (p.2440) has no augmentation-off control; RR/OR split ratio (fixed 95%) not swept.

### Sensitivity sweeps
Cache size (Fig.9a 10-150%; Fig.16b 10-30%), skew theta (Fig.15, Fig.16a), history size (Fig.16c), number of regions returned (Fig.5).

### End-to-end / production evaluation
End-to-end on unmodified Spark and Greenplum over real Azure Blob Storage; no production deployment, no multi-node cluster, and no experiment of two DBMSs sharing one Crystal instance (despite this being an architectural benefit, p.2433).

### Statistical treatment
None stated: no repetition count, no error bars, no confidence intervals. Distributional reporting is across queries (violins with quartiles and mean) and smoothing by moving average (n=40). TPC-H's "executed twice" is a workload design, not a repetition protocol (p.2441).

### Traceability note
The intro headline numbers (up to 20x per query, up to 8x average, up to 41% average bandwidth saving, p.2433) are not restated in Section 6 text; readers must recover them from Fig.8-15. Section 6's only explicit percentage is the 20% TPC-H mean improvement (p.2441).

---

## 7. Figure and table inventory

| # | Page | Type | Purpose | What a reviewer can recover | Caption style |
|---|---|---|---|---|---|
| Fig.1 | 2433 | architecture (deployment) | where Crystal sits between DBMS and cloud storage on a compute node | placement, no DBMS modification | descriptive |
| Fig.2 | 2433 | architecture (components) | CMS internals: connector, cache manager, RR/OR caches, matcher, oracle plugin, downloader | data/control flow | descriptive |
| Fig.3 | 2434 | conceptual example | semantic vs LRU file cache on Q1-Q3 over 4 file parts | why semantic caching yields higher hit coverage | claim-first (2nd/3rd sentence state the takeaway) |
| Fig.4 | 2435 | worked example (tree transform) | predicate tree -> DNF -> hyper-rectangles | the transformation rule | descriptive |
| Fig.5 | 2436 | line plot (preliminary experiment) | per-region overhead | ~50 ms linear cost per region, motivating overlap | short descriptive-claim |
| Fig.6 | 2436 | geometric example | query matched by two stored regions | superset/partial-superset matching | descriptive |
| Fig.7 | 2436 | flow diagram | request handling order OR -> RR -> download | control path | descriptive |
| Fig.8a-c | 2440 | violin plots | 9 strategies on 3 datasets | full latency distribution, quartiles, mean | descriptive + encoding legend |
| Table 1 | 2440 | table | raw vs Parquet sizes | dataset scale | descriptive |
| Fig.9a-b | 2441 | line plots | vs Alluxio / file LRU over cache size and over time | crossover at ~110%, learning curve | descriptive |
| Fig.10 | 2441 | violin | hot-event workload | short- vs long-term trade-off | descriptive |
| Fig.11a-b | 2442 | line (moving average) | hot-region shift | adaptation speed per policy | descriptive with method detail (window 40) |
| Fig.12 | 2442 | violin | Greenplum | generality | descriptive |
| Fig.13a-b | 2442 | CDF + violin | TPC-H Q6 skewed; all 22 queries | benchmark behaviour incl. limited pushdown | descriptive |
| Fig.14a-c | 2442 | stacked bars | online latency breakdown; offline refresh latency; compute time | where time goes; oracle cost | descriptive |
| Fig.15a-b | 2442 | grouped bars | network GB vs theta | bandwidth saving | descriptive ("plotted on a varying theta") |
| Fig.16a-c | 2443 | line plots | theta, cache size, history size | parameter robustness | descriptive ("Microbenchmarks") |

Pattern: 7 explanatory figures (Fig.1-7) in the first 5 pages, 9 result figures + 1 table in the evaluation; one preliminary experiment (Fig.5) placed in the design section to justify a design decision. Captions are mostly descriptive; only Fig.3 states its takeaway.

---

## 8. Related work

- Position: Section 7, after experiments, before conclusion (pp.2442-2443), ~1 page. A short related-work hook also appears in the intro (MVs and semantic caches, p.2433) and in 2.3 (overlap not handled by prior semantic-cache replacement, p.2434).
- Opening ¶: four research lines, then a 3-point differentiation list: (1) no DBMS modification; (2) caching views at the storage layer, shareable across DBMSs; (3) automatic choice of cached views via a replacement policy aware of semantic dependencies (p.2443).

| Group | Refs | Count | Differentiation pattern |
|---|---|---|---|
| Materialized View | [20,44,45] | 3 | "unlike Crystal" views are user/DBA defined; implementing MV matching/maintenance in a DBMS is heavy |
| Semantic Caching | [47],[11,14,17,29,30,42,43] | 8 | concede similarity (automatic, budgeted choice), then: caches whole query results (less reusable); most ignore overlap; Dar et al. split into non-overlapping regions (refuted with own Sec 3.2 evidence); chunk-based caching is static |
| Intermediate Results Reusing | [49,50],[19,25-27,38,41] | 8 | some only share among concurrent queries; others need deep DBMS integration vs Crystal's light connector and cross-DBMS sharing |
| Mid-tier Database Caching | [2,10,31] | 3 | not co-located; cached views predefined manually; hard to adapt |
| Vendor caches (untitled closing ¶) | [9,15],[1],[13] | 4 | page/block-level caching with LRU vs Crystal's query-driven layout and Parquet format |

Sentence pattern: "Similarly to Crystal, X does A. However, X requires/caches/assumes B, whereas Crystal ..." and the reverse "Unlike Crystal, X ...". The paper reuses its own Sec 3.2 measurement as an argument against a competitor's design (p.2443 -> p.2435).

---

## 9. References (52 entries, p.2444)

By type:
| Type | Count | Entries |
|---|---|---|
| DB conferences (peer reviewed) | 28 | SIGMOD 10 [13,17,19,20,25,27,30,34,47,48]; VLDB (pre-PVLDB proceedings) 6 [2,14,42,44,45,46]; PVLDB 5 [9,18,26,28,50]; ICDE 4 [31,38,41,49]; EDBT 1 [11]; SSDBM 1 [43]; DaWaK 1 [21] |
| Journals / bulletins | 3 | TODS [29], JACM [24], IEEE Data Eng. Bulletin [10] |
| Systems venues | 1 | SoCC [33] |
| Theses | 1 | PhD dissertation (Alluxio) [32] |
| Web / software / datasets / product docs | 19 | [1,3,4,5,6,7,8,12,15,16,22,23,35,36,37,39,40,51,52] |

By year band (publication or "accessed/2021" year for web items): <=2010: 19; 2011-2020: 18; 2021+: 15 (of which only 1 peer-reviewed, Greenplum SIGMOD 2021 [34]; the rest are 2021-dated web pages).

PVLDB + VLDB + SIGMOD + ICDE: 25 (PVLDB-proper 5, VLDB conference 6, SIGMOD 10, ICDE 4).

Observation: a large web share (~37%) reflects a systems paper anchored in industrial products (S3, Azure, Arrow, Parquet, Alluxio, Delta Cache). Detected citation slip: the text cites [22] for NYC Taxi and [39] for stock prices (p.2440), but [22] is the Kaggle stock dataset and [39] is NYC TLC (p.2444) - the two are swapped.

---

## 10. Limitations / discussion / conclusion

- There is no dedicated Limitations or Discussion section. Limitations are front-loaded into the final intro paragraph (p.2433): single-table predicates only (a consequence of the data-source API), cross-table predicates would require revisiting algorithms, read-only workloads (updates via invalidation "easy" / refresh "more challenging" left for future work), storage push-down study deferred because it only supports CSV today.
- Further limitations are stated locally where they arise: DNF blow-up (p.2435), lost optimality guarantee (p.2438), eager-write overhead and future client-side offload (p.2439), ML-based oracle as future work (p.2437), no feedback of regions from connectors (p.2439).
- Conclusion (p.2443, one paragraph, 5 sentences): restates context, motivation, system definition (co-located, unmodified DBMS via connectors, semantic regions, continuous adaptation) and the qualitative result (Spark and Greenplum latency, bandwidth). It reuses abstract wording almost one-to-one, adds no numbers, no limitations, no future work.
- Honesty style: trade-offs are reported inside result paragraphs in neutral language ("only in this extreme scenario", "fail to catch", "slightly worse") and immediately followed by the regime where the method wins.
- Acknowledgments: ERC grant and thanks to reviewers and a named colleague (p.2443).

---

## 11. Transferable rules

DO rules:
1. DO title as `<Name>: A <distinguishing adjective> <artifact type> for <domain>`: because each word maps to a claim and a section (evidence: title p.2432; "Unified" -> 2.2).
2. DO structure the intro as Challenges -> Opportunities -> Introducing X subsections: because it makes gap, enabling trends, and idea separately checkable (evidence: 1.1-1.3, pp.2432-2433).
3. DO write each challenge bullet as status-quo + concrete consequence (cost, wasted bytes, duplicated effort): because reviewers can verify each one independently (evidence: 1.1 bullets, p.2432).
4. DO cite named industrial systems in the motivation (Alluxio, Delta Cache, Snowflake) to prove the problem is real: because it pre-empts "who needs this?" (evidence: p.2432 P2).
5. DO frame an enabling trend as something "we find opens a new opportunity": because it explains why the idea is possible now and not 20 years ago (evidence: 1.2, p.2432).
6. DO attach a section pointer to every technical challenge/contribution bullet: because reviewers can jump from claim to evidence (evidence: p.2433 "(Section 4)" bullets).
7. DO put quantified headline results with section pointers in the intro (up to Nx per query, Mx average, P% bandwidth): because it sets the evaluation contract early (evidence: p.2433).
8. DO state scope restrictions in the intro and argue the restriction is exploited, not merely tolerated: because it converts a limitation into a design lever (evidence: single-table predicate paragraph, p.2433).
9. DO list explicitly deferred aspects (updates, cross-table predicates, storage push-down) with a one-line reason each: because it defuses "what about X" reviews (evidence: p.2433).
10. DO motivate the core abstraction with a tiny conceptual example figure early (semantic vs file cache): because it shows the win before any formalism (evidence: Fig.3, p.2434).
11. DO justify a key design decision with a small preliminary measurement inside the design section: because it turns an assertion into evidence (evidence: 16 rectangles from 3 queries, ~50 ms per region, Fig.5, p.2435-2436).
12. DO use a familiar architectural analogy for a non-obvious split (RR/OR like C-Store write/read stores): because it lowers reviewer cognitive load (evidence: p.2434).
13. DO formulate the optimization as a known problem (0/1 knapsack), then state exactly why the textbook version breaks (overlap double counting, huge W/B): because it shows novelty precisely where the classic fails (evidence: 4.3-4.4, p.2437-2438).
14. DO state complexity for the core algorithms and admit lost guarantees: because it pre-empts theory reviewers (evidence: O(n log n) -> O(n^2 log n); fractional optimality revoked, p.2438).
15. DO quantify integration cost (LOC per connector, no recompilation): because "lightweight/unmodified" claims need numbers (evidence: < 350 Scala, < 150 PXF lines, p.2439).
16. DO give exact hardware, cloud tier, and software versions incl. a commit hash: because reproducibility reviewers check it (evidence: p.2439).
17. DO normalize resource budgets across all competitors (cache size as % of data) and say it is for fairness: because unequal budgets are the first attack on caching papers (evidence: p.2440).
18. DO include at least one production-grade external system as a baseline besides internal variants: because internal-only comparisons look self-serving (evidence: Alluxio, Fig.9, 13b).
19. DO evaluate on a second host system to back a generality claim: because "DBMS-agnostic" needs more than one DBMS (evidence: Greenplum, Fig.12, p.2441).
20. DO design workloads that each stress one property (long-term regions, bursts, shifts, standard benchmark): because each experiment then answers one question (evidence: 6.2-6.7).
21. DO report distributions (violins with quartiles + mean) rather than only means: because caching wins are often skewed per query (evidence: Fig.8 caption, p.2440).
22. DO show learning curves over the query sequence for adaptive caches: because warm-up cost is a real trade-off reviewers will ask about (evidence: Fig.9b, 11).
23. DO report both online (critical-path) and offline (background) cost separately: because an expensive background optimizer is acceptable only if shown not to hurt queries (evidence: Fig.14, p.2442).
24. DO report the regimes where you lose in the same paragraph as wins (cold cache, 110% cache, joins not pushable): because candor raises credibility (evidence: p.2441).
25. DO publish the generated workload queries even if code is not released: because it enables partial reproduction (evidence: [12], p.2440).
26. DO reuse your own measurement in related work to refute a competitor design: because it grounds differentiation in evidence (evidence: Dar et al. vs Sec 3.2, p.2443).

Anti-patterns (do NOT copy blindly):
- No numbers in the abstract (p.2432): current PVLDB reviewers expect at least one quantified result; carry the headline number into the abstract.
- Intro headline numbers (20x, 8x, 41%) are never restated in Section 6 text (p.2433 vs pp.2440-2442): always restate each headline with its figure/table and configuration in the evaluation.
- No statistical treatment (no repetitions, error bars, CIs; pp.2439-2442): add run counts and variability, especially for cloud storage latency, which is noisy.
- No explicit research questions: tolerable here because subsection titles act as RQs, but explicit RQs map better to reviewer checklists.
- Augmentation (a claimed key component) is never ablated (p.2439-2440): every claimed component needs an on/off ablation.
- Cross-DBMS sharing is claimed as a benefit (p.2433) but not evaluated; never claim an architectural benefit without an experiment or an explicit "not evaluated" note.
- Alluxio version/configuration not disclosed (p.2441): always disclose baseline versions and tuning.
- Missing metrics for a caching paper: no hit ratio, no p95/p99 tail latency, no throughput, no monetary cost, no memory/SSD footprint; add the ones your claims depend on.
- Single-node evaluation only; no scale-out (p.2439).
- No dedicated limitations section and a conclusion that merely restates the abstract (p.2443): a short limitations/threats paragraph is cheap insurance.
- Paper-specific assumptions that should not be transplanted: read-only workloads; single-table conjunctive/disjunctive predicates from a data-source API; Parquet/Arrow as the cache format; a bandwidth-saved benefit model; no access control or multi-tenant isolation (so for result reuse with access control, correctness under authorization changes must be added, not assumed).
- Typos and citation slips survived (RR written for OR in 2.3, p.2434; swapped dataset citations [22]/[39], p.2440): run a citation/label check before submission.

---

## 12. Quantified fingerprint

| Metric | Value |
|---|---|
| Body pages (excl. references) | 12 (pp.2432-2443) |
| Reference pages | 1 (p.2444) |
| References | 52 (25 in PVLDB/VLDB/SIGMOD/ICDE; 19 web/software) |
| Figures | 16 (26 panels); 10 with experimental results (Fig.5, 8-16) |
| Tables | 1 |
| Algorithms | 3 (pseudocode, complexity stated for knapsack variants only) |
| Formal definitions/theorems | 0 |
| Baselines | 8 non-proposed configurations (No cache, Alluxio, F-LRU, RR-LRU1, RR-LRU2, OR-LRU1, OR-K_DP, F/RR/OR); 2 external systems (vanilla Spark, Alluxio); 2 proposed (OR-K_G, RR/OR) |
| Metric families | 6 (latency distribution/mean/CDF/time series; online latency breakdown; oracle refresh latency; background compute time; network GB; connector LOC) + 1 preliminary (per-region overhead) |
| Datasets | 4 entries in Table 1 (TPC-H SF50, Lineitem, NYC Taxi, Stocks) from 3 sources |
| Workload patterns | 5 (regions, hot events, changing regions, TPC-H Q6 zipfian, TPC-H 22 queries) |
| Host DBMSs | 2 (Spark 3.0.1, Greenplum 6.16) |
| Explicit RQs | 0 (7 goal-specific subsections 6.2-6.8) |
| Pages on experiments | approx 3.1 (p.2439 last quarter through p.2442 to the start of Sec 7) |
| % of body on experiments | approx 26% (3.1 / 12) |
| Related work | approx 1 page, 5 groups, 26 distinct refs, placed after experiments |
| Statistical treatment | none (no repetitions/error bars) |
| Artifact | workload queries only (aka.ms link [12]); no code |
