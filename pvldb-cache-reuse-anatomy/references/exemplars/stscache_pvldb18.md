# Exemplar deconstruction: STsCache (PVLDB 18(9), 2025, pp. 2964-2977)

Source: official PDF `p2964-li.pdf` (14 pages, letter size, PDF/A-2b) plus a `pdftotext -layout` dump. Every page cited below uses the **printed page number** (2964-2977). Mapping: PDF page N = printed page 2963+N. Everything here is paraphrased. Quoted fragments are 15 words or fewer.

---

## 1. Bibliographic facts

| Item | Value (evidence) |
|---|---|
| Title | STsCache: An Efficient Semantic Caching Scheme for Time-series Data Workloads Based on Hybrid Storage (p.2964) |
| Authors | 7: Tao Kong, Hui Li* (corresponding), Yuxuan Zhao, Liping Li, Xiyue Gao, Qilong Wu, Jiangtao Cui (p.2964) |
| Affiliation types | All 7 list Xidian University (academia). Hui Li also lists Yunxi Technology Co., Ltd (industry). So the paper is academic with one industry co-affiliation (p.2964) |
| Venue | PVLDB Vol. 18, No. 9, pp. 2964-2977, 2025 (p.2964 reference block and footer) |
| DOI | 10.14778/3746405.3746421 (p.2964) |
| Total pages | 14 (pdfinfo) |
| References start | p.2976 (PDF p13), the top of the left column |
| Body pages | 12 (pp.2964-2975, including the conclusion and acknowledgments, which end p.2975). References take 2 pages (pp.2976-2977) |
| Reference count | **80** (counted entries [1]-[80], pp.2976-2977) |
| Figures | **25** (Fig. 1-25). 9 are conceptual (Figs 1-9) and 16 report results (Figs 10-25) |
| Tables | **2** (Table 1 Notations, p.2967; Table 2 dataset statistics, p.2972) |
| Algorithms | **4** pseudocode boxes (Alg. 1 SetByIndex and Alg. 2 GetByIndex on p.2970; Alg. 3 BatchEviction and Alg. 4 DeduplicationInsertion on p.2971) |
| Definitions / theorems / lemmas | **5 definitions** (Def. 1-3 p.2967, Def. 4-5 pp.2967-2968), **2 worked examples** (Ex. 1 p.2967, Ex. 2 p.2968), **0** theorems, lemmas or proofs |
| Equations | About 6 displayed expressions, all unnumbered: Meta(q) in Def. 1, the Example 1 tuple, Series(q,M) in Def. 2, the Meta-as-set-of-Series identity, Metric in Def. 3, and the complexity bound O(Σ(1+log N_i)) vs O(N·σ) (pp.2967, 2970). Def. 4-5 add about 10 inline formal conditions (p.2967) |
| Footnotes | 0 content footnotes. There is only the standard CC BY-NC-ND licence block (p.2964), and the asterisk on Hui Li has no footnote text |
| Query listings | 5 SQL-like example queries (Q1, Q2-1, Q2-2, Q3, Q4), p.2966 |
| Artifact | A "PVLDB Artifact Availability" paragraph points to github.com/ts-lab1024/ts-semantic-caching (p.2964). An ACM "Artifacts Available v1.1" badge sits top-right on p.2964 |
| Funding | MIIT special task project + 2 NSFC grants (p.2975) |
| Length | About 13.4k words in total (pdftotext). The abstract is about 178 words |

---

## 2. Title anatomy

Pattern: `SystemName: An <Quality> <Mechanism-class> for <Workload domain> Based on <Enabling substrate>`

| Component | Text | Function |
|---|---|---|
| System name | "STsCache" | The acronym packs the three ideas: **S**emantic + **T**ime-**s**eries + **Cache**. It is easy to remember and compare across the paper (p.2964) |
| Quality claim | "An Efficient" | The performance promise. The evaluation pays it off with throughput and latency (Sec. 5) |
| Mechanism class | "Semantic Caching Scheme" | Names the technique family (semantic caching, refs [31,61]) instead of a single trick |
| Domain | "for Time-series Data Workloads" | Scopes the claim. It deliberately echoes the main baseline's title: [53] is "TSCache: an efficient flash-based caching scheme for time-series data workloads" (p.2976) |
| Substrate | "Based on Hybrid Storage" | Names the hardware assumption (memory + NVMe SSD), which drives the eviction and compaction design (Sec. 4.5-4.6) |

Why it works: the title reads as a direct successor to TSCache, with "flash-based" replaced by "semantic ... hybrid storage". A reviewer can infer the delta from the title alone. The cost is that the title says nothing about the formal contribution (the definition of semantic time-series caching), even though the paper lists that as contribution 1 (p.2965).

---

## 3. Abstract (p.2964): 8 sentences in 2 paragraphs, about 178 words

| # | Rhetorical function | Concrete object / number carried |
|---|---|---|
| S1 | Context and need: extreme-scale time-series workloads in data centers need a high-performance semantic cache that reuses past queries' semantics and results | "data centers"; the cache's job is reusing historical semantics and results |
| S2 | Gap as a two-horned dichotomy: existing caches either ignore query semantics (poor performance) or serve only narrow scenarios (small capacity, limited functions) | Two failure classes. These later map to TSCache and BSCache (p.2964) |
| S3 | Conceptual contribution plus priority claim: they summarize time-series query patterns and define semantic time-series caching "for the first time" | The formal definition (Sec. 3) |
| S4 | Artifact: they present the STsCache system on a memory + NVMe SSD hybrid store | System name; storage model |
| S5 | Mechanism inventory: a list of 5 named strategies | slab-based semantic data management; semantic index; semantic-value batch eviction; time-aware deduplication insertion; lazy compaction |
| S6 | Evaluation scope: benchmarks plus "production environments" | Two evaluation modes |
| S7 | Headline 1, vs. databases: 4.8-10.8× throughput and 79.9%-93.5% lower latency over InfluxDB and TimescaleDB | Named baselines and ranges |
| S8 | Headline 2, vs. the most recent caches: 1.5-4.5× throughput, 59.4%-81.9% lower latency and 22.5%-82.4% higher hit ratio over TSCache and BSCache | Named baselines and three metrics |

Observations:
- The abstract has no separate "challenge" sentence. It goes straight from gap to contribution.
- Every result sentence names its baselines in parentheses.
- The abstract ranges are unions of separate experiments. Throughput vs caches (1.5-4.5×) merges the BSCache range 1.5-3.4× (p.2972) with the TSCache range 2.9-4.5× (p.2973). Hit ratio (22.5-82.4%) merges 22.5-38.8% and 46.9-82.4%.
- The lower bound of the latency claim vs TSDBs, **79.9%**, does not appear in any Section 5 sentence. Sec. 5.3 reports 84.1-92.4% vs a single TSDB (p.2972), and the production study reaches 93.5% (p.2975). Treat this as a traceability gap.
- "Increase hit ratios by x%" does not say whether it means percentage points or a relative increase. Sec. 5.7 does say "percentage points" (p.2975).

---

## 4. Introduction (pp.2964-2965, about 1.4 pages)

| ¶ | Page | Function | Key moves |
|---|---|---|---|
| I-1 | p.2964 (left col bottom to right col top) | **Problem / context** | Defines time-series data, then lists application domains with 3 citation clusters each (IoT, meteorology, finance, manufacturing, monitoring). Says TSDBs are now essential. Then gives the workload insight: queries skew toward recent data, so they overlap more than other queries [22,53], and they involve time ranges, tags and aggregations. It ends by naming a large cache that reuses past semantics and results as "a potent solution" |
| I-2 | p.2964 to p.2965 top | **Gap** (prior-work critique by named system) | (a) Memcached-style KV caches cannot handle varying time ranges. (b) TSCache [53] hashes the non-time part of the query into a key, which loses the metadata-data relationship. This gives 2 numbered drawbacks: no tag-based interface, and a low hit ratio from exact-key matching. (c) BSCache [77] (Zhang et al.) is semantic but built into one monitoring system, in-memory only, not general, and ignores relationships between queries. The paragraph ends with a synthesis sentence, then "challenging for the following reasons" |
| I-3 | p.2965 | **Challenges** (3 bullets with bold run-in titles) | (1) Costly semantic matching. (2) Memory overhead vs performance trade-off: TSCache's flash limits speed, and memory alone is expensive. (3) Cache penetration: queries for non-existent data always hit the backend |
| I-4 | p.2965 | **Idea** | They characterize query patterns and give the first formal definition, introducing the terms *semantic meta* and *semantic series*. STsCache sits on memory + NVMe SSD. Unlike BSCache, it serves general TSDBs |
| I-5 | p.2965 | **Mechanisms → challenges** (4 numbered items) | (1) Slabs for sequential I/O. (2) A semantic index (graph + skip lists) that cuts matching cost and also stores empty-query semantics against penetration. (3) Hotness quantified as "semantic values" plus batch eviction. (4) Deduplicated insertion plus compaction against fragmentation. Each item says which challenge it addresses |
| I-6 | p.2965 | **Implementation + results** | Built on Fatcache and gomemcache, with modified Go clients for InfluxDB and TimescaleDB. Repeats the abstract numbers verbatim (4.8-10.8×, 79.9-93.5%, 1.5-4.5×, 59.4-81.9%, 22.5-82.4%) |
| I-7 | p.2965 | **Contributions** (4 bullets) | See below |
| I-8 | p.2965 | **Roadmap** | One sentence per section (Sec. 2-6) |

**Contribution list** (p.2965). There are 4 bullets, and every one opens with "We propose":
1. **Formal definition** of semantic caching for time-series workloads, "for the first time". It is framed as a foundation for general TSDBs.
2. **Large-capacity hybrid cache** (memory + NVMe SSD) plus **semantic-value batch eviction**. The stated benefit is keeping hotter data in memory to balance performance against memory.
3. **Semantic index** (stores query semantics and the relations between queries). The stated benefits are avoiding expensive matching and preventing penetration via empty-query semantics.
4. **Low-cost compaction** (deduplicated insertion + lazy compaction) to improve space utilization.

No bullet claims the evaluation or the artifact, and none carries a number. Challenge 1 maps to bullet 3, challenge 2 to bullet 2, and challenge 3 also to bullet 3. Bullet 4 has no matching stated challenge. Its motivation (fragmentation) first appears in Sec. 4.6 (p.2971).

**First figure/table**: the intro has none. The first figure is Fig. 1 (p.2966, Sec. 2.1), a toy table of points and series from the TSBS IoT truck use case. It sets up the running example. There is no motivating measurement in the intro.

---

## 5. Remaining sections in order

### Sec. 2 Preliminaries and Related Work (pp.2965-2966, about 0.7 page)
- **2.1 Preliminaries of TSDBs** (p.2965). The first paragraph lists well-known TSDBs, citing product URLs. The second introduces the vocabulary (point, measurement, tag set, field set, timestamp) on the InfluxDB/TSBS IoT example in Fig. 1. The third defines "series" with a pointer to series1 in Fig. 1. The vocabulary is taught on a concrete instance before Sec. 3 formalizes it.
- **2.2 Related Work**: 2.2.1 Semantic Caching, 2.2.2 Query Containment, 2.2.3 Materialized View. **2.3 Time-series Caching** is a separate subsection placed as the closest-competitor block (see §8 below).

### Sec. 3 Formal Definition of Semantic Caching in TSDBs (pp.2966-2968, about 1.75 pages)
- **Opening ¶** (p.2966): anchors on the classic semantic-cache notion [31,61] (query meaning = projected columns plus predicates), then says they take it "one step further". Query patterns come from benchmarks [8,14,15,17,54] and prior work. This gives 4 pattern families: time ranges, aggregations, threshold filtering and tags. Then come **5 SQL-like example queries Q1-Q4** (p.2966). These are the running examples, and they appear *before* any symbol.
- **3.1 Query Semantics** (pp.2966-2967). Symbols are introduced one at a time, each paired with an instance from Fig. 1 or Q3 (M1 and M2 are spelled out; P, P_F and T are spelled out for Q3). **Table 1 Notations** (p.2967) collects the symbols. Then come **Def. 1 Semantic Meta** (a 5-tuple), **Example 1** instantiating it on Q4, **Def. 2 Semantic Series** (per data source), the identity Meta = set of Series plus T, and **Def. 3 Semantic Metric** (a group of series sharing F, P, G). The order is: example query, then symbol, then definition, then worked example.
- **3.2 Semantic Relationships between Queries** (p.2967). The three answer paths are first described informally as numbered items (direct, filtered, aggregated). They are illustrated with **Fig. 2** (aligned aggregation intervals: query A can be answered and query B cannot), and *then* formalized in **Def. 4 Cache Answerable**. A bridging sentence separates "Whether" (Def. 4) from "How" (Def. 5). **Def. 5** defines full hit and partial hit, followed by the terms probe query and remainder query. **Example 2** with **Fig. 3** (p.2968) applies them to Q2-1/Q2-2.
- Claim scoping: the conditions are stated inside the definitions (e.g., overlapping time ranges are required, and the aggregation interval must be an integer multiple with aligned boundaries, p.2967). There is **no theorem or proof** that answerability is sound. Correctness rests on the definitions.

### Sec. 4 STsCache Design (pp.2968-2971, about 3.5 pages)
- **Intro ¶** (p.2968): positions the system as standalone like Memcached, with a cache-aside architecture (**Fig. 4**). The client falls back to the TSDB on anything less than a full hit, then writes the semantics and results back. This decouples the cache from the TSDB.
- **4.1 Architecture Overview** (p.2968, **Fig. 5**): 5 modules with bold run-in heads (interface, data management, semantic index, eviction, compaction). Each gets one or two sentences, and the list doubles as a mini-roadmap for 4.2-4.6.
- **4.2 Semantic-based Interface** (p.2968). 4.2.1 is a custom binary serialization, justified against Protobuf and JSON (re-encoding overhead, size). 4.2.2 is the API: Set and Get with a SemanticKey string plus begin and end time. Empty queries store the value NULL. The design note: parsing only SemanticKey avoids TSDB-dialect compatibility issues. 4.2.3 covers the clients (STsCache Client and STsCache-Aside Client, which merges results).
- **4.3 Slab-based Semantic Data Management** (pp.2968-2969, **Fig. 6**). **Key scoping assumption**: time-series data is append-only and write-once, so the paper says cache consistency need not be considered (p.2968). Then 3 numbered benefits. 4.3.1 covers slab structure (header + data). It argues against row and column layouts, and the 16KB slab size is justified by a forward reference to Sec. 5.4. 4.3.2 covers parallel slab I/O through a thread pool on NVMe [38,75].
- **4.4 Semantic Index** (pp.2969-2970, **Fig. 7**). 4.4.1 is the semantic graph. Its pattern: state the intuitive design, then a "However" (node blow-up), then the refinement (one node per semantic metric plus a mapping list). Edge weights encode the answer path from Def. 4. 4.4.2 is the time-range skip list. Again an intuitive design comes first, then the flaw (it cannot represent empty queries, which causes penetration), then the fix (query-driven key construction), then 3 numbered benefits. 4.4.3 covers operations: **Alg. 1 SetByIndex**, Query Trimming with **Fig. 8** (3 panels a-c; trimming happens only when the cache covers the query's begin or end), and **Alg. 2 GetByIndex**. **Complexity is given only for Alg. 2**: O(Σ_{i=1}^{n_v}(1+log N_i)), compared with O(N·σ) for a scan without the index (p.2970).
- **4.5 Batch Eviction Based on Semantic Value** (pp.2970-2971). 4.5.1: semantic value = the slab's cumulative read/write volume, sorted only at eviction time. 4.5.2: aging by bit-shifts hidden inside the eviction pass. 4.5.3: **Alg. 3**, with 3 numbered benefits. The batch size k = 1/16 of memory slabs is justified by a forward reference to Sec. 5.5.
- **4.6 Compaction Module** (p.2971). It opens with 2 numbered problems (duplicate insertion, fragmentation). 4.6.1 is time-aware deduplicated insertion (**Alg. 4**, **Fig. 9**), with the constraint that the target slab must be in memory. 4.6.2 is lazy compaction, triggered only when an insertion raises a node's slab count and compaction can remove at least one slab.
- Recurring micro-structure in every subsection: motivation or problem sentence, then the naive design, then "However" plus the flaw, then the chosen design, then 2-3 numbered benefits, then a forward reference to the experiment that tunes the parameter.
- Algorithm presentation: 4 boxed pseudocode listings with Input/Output headers and named helper calls. There is one complexity bound and no cost model for eviction or compaction. The listings contain typos (e.g., "DeduplicationInertion" in Alg. 1 and MHead/MHeap mixed in Alg. 3, pp.2970-2971; "Evicton" p.2971; "Compatcion" p.2974).

### Sec. 5 Experiment (pp.2971-2975, about 4.0 pages)
See §6. The subsections are 5.1 Implementation, 5.2 Setting, 5.3 Overall Comparison, 5.4 Slab Management, 5.5 Cache Replacement Policy, 5.6 Compaction Module, 5.7 Alleviate Performance Bottlenecks, and 5.8 Production Environment Evaluation. Sections 5.4-5.7 mirror the design modules of Sec. 4.3-4.6 one to one.

### Sec. 6 Conclusion (p.2975), then Acknowledgments
See §10.

---

## 6. Experiments in depth

**Goals.** There are no explicit research questions. The goals are implied by the subsection titles. Overall comparison against TSDBs and caches, scalability, cache size and semantic overlap (5.3). Per-module parameter justification and ablations (5.4-5.7). Production-style validation (5.8).

**Implementation** (p.2971-2972): a prototype on Fatcache that replaces Fatcache's FIFO with batch eviction. Aggregation and filter operators are integrated. Get/Set clients are built on gomemcache, and the InfluxDB and TimescaleDB Go clients are modified to merge results. The code is about 10,000 lines of C/C++/Go.

**Hardware/software** (p.2972): 3 DELL T7920 workstations (TSDB server, cache server, client), each with a 2.9 GHz 16-core Xeon Gold 6226R, 128 GB RAM (the paper says "DDR5"), 1 TB SSD, 16 TB HDD, Ubuntu 20.04. TSDB data lives on HDD. Cache-server SSD I/O uses direct_io, bypassing the OS page cache. Versions: **InfluxDB 1.8.10, TimescaleDB 2.6.0**. Not disclosed: network bandwidth or topology, the SSD model, and the TSCache code version. Production software (Prometheus, Node Exporter, Docker, Grafana) is cited without versions.

**Datasets** (Table 2, p.2972): 2 TSBS use cases × 3 scales, 10-second sampling over all of 2022.
- IoT (16 fields): Small, 100 devices, 5.05 B points, 42.29 GB. Medium, 500 devices, 25.2 B points, 211.47 GB. Large, 1,000 devices, 50.5 B points, 422.93 GB.
- DevOps (10 fields): Small 3.15 B points, 25.85 GB. Medium 15.8 B points, 129.23 GB. Large 31.5 B points, 258.46 GB.
- After the overall comparison, only the Medium scale is reported, "for ease of discussion and space limit" (p.2972).

**Workloads** (p.2972): TSBS query patterns (aggregation, threshold filtering, tag grouping). Time-range placement follows a Latest distribution (borrowed from YCSB-TS). Range length is Zipfian between 3 hours and 1 month. Mean request sizes: IoT 124.75 KB / 620.53 KB / 1.21 MB, and DevOps 82.34 / 413.96 / 819.69 KB. There are 64 client threads (chosen to saturate the system without overloading the server). Cache capacity is 4% of the dataset with memory:disk = 1:3.

**Baselines**:

| Baseline | What it is | Binary vs reimplementation | Fairness / disclosure |
|---|---|---|---|
| Single-TSDB (InfluxDB, TimescaleDB) | One TSDB server, data on HDD | Original binaries, versions pinned (p.2972) | Shares the testbed |
| Single-TSDB-SSD | Same, data on SSD | Original | Isolates the SSD effect. Shows SSDs give TSDBs little gain because they are CPU-bound (p.2972) |
| Dual-TSDB | Two replicated TSDB servers on SSD, queries split round-robin | Original | **Explicit #servers fairness**: STsCache uses an extra machine, so the database also gets one (p.2972) |
| TSCache [53] | Flash-based time-series cache | Not stated whether this is the original code. The text notes TSCache's default 128 keys per slab and hash matching (p.2972) | It cannot run the benchmark, so it gets a **separate simplified workload** (at most 128 hashed keys) with the same 4% capacity and 1:3 ratio (pp.2972-2973). It is absent from Fig. 10 |
| BSCache [77] | In-memory semantic cache built into a monitoring system | **Reimplemented** on Fatcache, "strictly" following [77], because the original is an internal component (p.2972) | Same base code as STsCache, deployed as a standalone cache server with identical settings (p.2972) |
| FIFO, LRU | Replacement policies | Implemented inside STsCache (p.2974) | Same system. Only the policy changes |

**Metrics** (p.2972):
1. Throughput (queries/s).
2. End-to-end latency (ms), from request send to receipt of the client result object. Only the **mean** is reported, with no percentiles.
3. Hit ratio, split into **full** and **partial** (Def. 5), shown stacked.
4. Derived or ad hoc: memory overhead reduction (75% at a 1:3 ratio, p.2974), and per-slab metadata (8 bytes vs >50% of the slab for TSCache's key and bit arrays, p.2973), stated analytically rather than measured.
- There is no CPU, I/O-volume, network-bytes, $-cost, write-amplification or SSD-wear measurement, even though slab writes are said to extend flash lifespan (p.2969).

**Per-figure results**:

| Fig. | Varied | Measured | Headline the text draws (page) |
|---|---|---|---|
| 10 | 5 systems × 2 TSDBs × 6 datasets (3 scales, 2 use cases) | Throughput, latency | STsCache is best everywhere. 4.8-10.8× throughput and 84.1-92.4% lower latency vs a single TSDB. 1.8-4.0× and 65.6-83.5% vs Dual (p.2972) |
| 10+11 | Same; hit ratio vs BSCache | Throughput, latency, full/partial hit | vs BSCache: 1.5-3.4× throughput, 59.4-77.1% lower latency, 22.5-38.8% higher hit ratio. Explained by query-relationship reuse and BSCache's costly distance-based eviction (p.2972) |
| 12 | TSCache vs STsCache (simplified workload) | 3 metrics | 2.9-4.5× throughput, 76.4-81.9% lower latency, 46.9-82.4% higher hit ratio. 3 reasons: the index, metadata efficiency, and filter/aggregate reuse (p.2973) |
| 13 | Clients 1-128 | Throughput, latency | TimescaleDB plateaus at 16 clients and InfluxDB at 32. STsCache reaches 16.7-36.8× throughput at 128 clients vs 1, with 3.4-7.4× higher latency (p.2973) |
| 14 | Cache size 1-5% of data | 3 metrics | Performance improves with size. At 5%: 0.9-1.9× higher throughput, 45.2-65.7% lower latency, 14.12-16.5% higher hit ratio. The comparison reference is not stated. Even at 1% it beats the TSDBs (p.2973) |
| 15 | Semantic overlap 0-100% (via preloading), all systems | Latency | STsCache has the lowest latency. At zero overlap its miss penalty is small (p.2973) |
| 16 | Request size 16KB-4MB × overlap 0-100% | Latency | Larger queries benefit more (4MB at 20% overlap: −24.3%). At 16KB only full hits help (p.2973) |
| 17 | Slab size 4-1024 KB | 3 metrics | Performance improves as slabs shrink toward 16KB, then plateaus. 16KB is chosen (pp.2973-2974) |
| 18 | Mem:disk 1:0 to 1:9 | Throughput, latency | Performance drops as the disk share grows. 1:3 costs 6.1-14.9% throughput and adds 7.2-19.3% latency vs all-memory, for 75% less memory (p.2974) |
| 19 | FIFO / LRU / batch eviction | 3 metrics | 1.2-2.1× FIFO and 1.1-1.5× LRU throughput. Hit ratio is "slightly higher or on par" with LRU. Full hit +20.9-59.7% and total +6.1-10.7% vs FIFO (p.2974) |
| 20 | Batch size : memory slabs, 1:1 to 1:64 | Throughput, latency | 1/16 is best. Smaller batches mean frequent sorting; larger ones mean random-I/O stalls (p.2974) |
| 21 | Dedup insertion on/off | 3 metrics | +27.1-36.8% throughput, −23.6-25.9% latency, similar hit ratio (p.2974) |
| 22 | Compaction disabled / real-time / lazy | 3 metrics | Compaction vs none: +8.6-48.4% throughput, −5.1-33.2% latency, +4.5-8.6% hit. Lazy vs real-time adds another +3.2-15.9% throughput and −4.1-13.7% latency (p.2974) |
| 23 | Single- vs multi-threaded I/O | Throughput, latency | +12.6-42.2% throughput, −11.7-29.8% latency (p.2975) |
| 24 | Empty-query share 12.5-100%, empty-semantics storage on/off | 3 metrics | The gap widens with the empty share. In the "1:1" case: 31.5× throughput, −96.8% latency, +97.1 pp hit (p.2975) |
| 25 | 3 production-style workloads × 4 systems × 2 TSDBs | Latency | WL.1: up to −82.8/−71.8/−65.3% vs TSDB/TSCache/BSCache. WL.2: −93.5/−57.2/−65.5%. WL.3: −84.1/−68.3/−63.3% (p.2975) |

**Negative results, trade-offs, and regimes with smaller gains** (all are framed mildly, inside the result paragraphs):
- p.2972: putting baseline TSDBs on SSD barely helps them, because they are CPU-bound. This finding constrains the baseline, not STsCache.
- p.2973: with 128 clients, latency grows 3.4-7.4×. This is reported, but alongside the throughput gain.
- p.2973: at zero overlap there is a small miss penalty. For small (16KB) requests, partial hits give no meaningful benefit because network overhead cancels it. This is the clearest regime where the method's advantage disappears.
- p.2974: the hybrid ratio is an explicit cost trade-off (6.1-14.9% throughput lost for 75% memory saved).
- p.2974: the hit ratio vs LRU is only on par or slightly higher. The gain comes from throughput and latency, not hits.
- p.2974: smaller slabs carry metadata and semantic-value-array overhead, and batch size has a U-shaped optimum.
- p.2975: in WL.1 and WL.3 the gain over the TSDB is smaller than in WL.2, because frequent queries for fresh data must go to the TSDB.
- p.2972: the TSCache comparison is limited to a simplified 128-key workload. This is disclosed, but it means the strongest prior flash cache never runs on the main benchmark.

**Ablations** (5): eviction policy (Fig. 19), dedup insertion (Fig. 21), compaction mode (Fig. 22), parallel I/O (Fig. 23), empty-query semantics storage (Fig. 24). Missing: an ablation of the semantic index itself (index vs linear semantic matching is argued only through complexity, p.2970), and of the individual answer paths (filtered/aggregated reuse turned off). The latter is needed to substantiate the "semantic relationships" claim.

**Sensitivity sweeps** (8): clients, cache size, semantic overlap, request size × overlap, slab size, memory:disk ratio, batch size, empty-query share.

**End-to-end / production** (5.8, p.2975). (1) DevOps monitoring that reproduces BSCache's production setup: 100 Docker containers running Node Exporter, scraped by Prometheus every 5 s. WL.1 is latency-sensitive (latest 10-minute and 5-minute windows of 10 key metrics). WL.2 is historical (12-hour windows over half the series in the last 72 hours). Both run each minute. (2) Smart factory: 200 devices (100 machine tools + 100 meters) sampled every 15 s. WL.3 is hourly real-time plus daily weekly queries. The runs start after 1 week of collection and last 48 h, with a 512 MB cache at 1:3. The client is integrated into Grafana. These are realistic deployments, but they are built by the authors and small-scale. They are not a long-running industrial deployment.

**Statistics** (p.2972): every experiment regenerates and runs the workload **5 times and reports the average**. There are no error bars, variance, CIs or significance tests, and latency is the mean only.

---

## 7. Figure and table inventory

| # | Page | Type | Purpose | What a reviewer can recover | Caption style |
|---|---|---|---|---|---|
| Fig 1 | 2966 | Example table-as-figure | Teaches point, series, tag and field vocabulary | The data model and the running example | Descriptive |
| Fig 2 | 2967 | Timeline illustration | Aggregated-answer alignment (Q_A can be answered, Q_B cannot) | The interval-alignment condition of Def. 4 | Descriptive |
| Table 1 | 2967 | Notation table | Symbol glossary | All symbols in one place | Descriptive |
| Fig 3 | 2968 | Worked example diagram | Q2-2 trimmed by cached Q2-1 into probe and remainder queries | How partial hits decompose | Descriptive |
| Fig 4 | 2969 | Data-flow sketch | Cache-aside deployment | Who talks to whom | Descriptive |
| Fig 5 | 2969 | Architecture | 5 modules over memory/SSD slabs | Module inventory, matching Sec. 4.1 | Descriptive |
| Fig 6 | 2969 | Data-structure layout | Slab = header + timestamped field rows | Storage format | Descriptive |
| Fig 7 | 2970 | Index structure | Semantic graph, mapping list and time-range skip list | Index composition and lookup path | Descriptive |
| Fig 8 | 2970 | 3-panel illustration (a-c) | Query trimming in series × time space | The trimming rule | Descriptive |
| Fig 9 | 2971 | Example + mini table | Finding insert points for dedup insertion | The Alg. 4 mechanics | Descriptive |
| Table 2 | 2972 | Dataset statistics | Scale of the 6 dataset configurations | Points, GB, devices, fields | Descriptive, with sampling and duration in the caption |
| Fig 10 | 2973 | Grouped bars, 6 panels (3 scales × throughput/latency) | Main comparison | Ranking at each scale | Descriptive |
| Fig 11 | 2973 | Stacked bars (full + partial hit), 2 panels | Hit ratio vs BSCache | Hit decomposition | Descriptive |
| Fig 12 | 2973 | Bars, 3 panels | vs TSCache | 3 metrics on the simplified workload | Descriptive |
| Fig 13 | 2973 | Lines, 2 panels, log2 x-axis | Client scalability | Saturation points | Descriptive ("Effect of …") |
| Fig 14 | 2973 | Lines, 3 panels | Cache-size sensitivity | Diminishing returns | Descriptive |
| Fig 15 | 2974 | Lines | Latency vs overlap, all systems | Crossovers and the zero-overlap penalty | Descriptive |
| Fig 16 | 2974 | Grouped bars (11 overlap levels × 5 request sizes) | Overlap × request size | The regime where the benefit vanishes (small requests) | Descriptive |
| Fig 17 | 2974 | Lines, 3 panels | Slab size | Parameter optimum | Descriptive |
| Fig 18 | 2974 | Lines, 2 panels | Memory:disk ratio | The cost/performance curve | Descriptive |
| Fig 19 | 2974 | Bars, 3 panels | Eviction policy ablation | Policy ranking, hit split | Descriptive |
| Fig 20 | 2974 | Lines, 2 panels | Batch size | U-shaped optimum | Descriptive |
| Fig 21 | 2974 | Bars, 3 panels | Dedup on/off | Ablation delta | Descriptive |
| Fig 22 | 2975 | Bars, 3 panels | Compaction mode | Ablation delta | Descriptive |
| Fig 23 | 2975 | Bars, 2 panels | Parallel I/O | Ablation delta | Descriptive |
| Fig 24 | 2975 | Bars, 3 panels | Penetration robustness | Gap vs empty-query share | Descriptive |
| Fig 25 | 2975 | Bars, 3 panels (WL.1-3) | Production latency | End-to-end gain per workload | Descriptive |

Every caption is short and descriptive ("Effect of X", "Comparison between …"). **None is claim-first.** The take-away lives only in the body text. The result figures are packed densely: 5 on p.2973, 7 on p.2974, 4 on p.2975. Most use multiple small panels sharing one legend.

---

## 8. Related work

- **Position**: early. It is merged with the preliminaries as Sec. 2, right after the intro (pp.2965-2966), and takes about 0.7 page.
- **Groups and reference counts** (unique refs):
  - 2.2.1 Semantic Caching: 18 refs (traditional KV [2,4,34]; foundations [31,61]; surveys and variants [24,43,72,73,76]; domains: mobile [50,59,60], web [28,29], LLM [23,32], monitoring [77]).
  - 2.2.2 Query Containment: 6 refs ([45,48,56,62], XCache [26], Luo & Naughton [55]).
  - 2.2.3 Materialized View: 7 refs ([25,36,69,71], views [33,65], TimescaleDB continuous aggregates [12]).
  - 2.3 Time-series Caching: 2 refs (TSCache [53], MinMaxCache [57]). This is the closest-competitor block, and it gets its own numbered subsection.
- **Positioning sentence pattern**: each group follows the same template: describe the line of work, then "However" plus a specific mismatch with time-series semantics, then a sentence linking that mismatch to this paper's design. Examples, paraphrased: semantic caching overlooks query-to-query relations and is too memory-costly, and these limitations motivate STsCache (p.2966). Query containment work does not fit because time-series predicates, thresholds, aggregations and ranges differ, which motivates formal definitions (p.2966). Materialized views need DBA-predefined logic and load the server, whereas semantic caching is flexible and independent (p.2966). TSCache hashes away semantics, so hit rates are low (p.2966). MinMaxCache is the reverse case: its success is cited as *inspiration* (p.2966).
- The differentiation against the two main baselines is stated three times: in the intro (pp.2964-2965), in related work (p.2966) and in the result explanations (pp.2972-2973).

---

## 9. References (80 entries, pp.2976-2977)

**By type** (counted):

| Type | Count | Entries |
|---|---|---|
| Web / software / benchmark URLs (no venue) | 20 | [1]-[20] (Redis, InfluxDB, TSBS, Fatcache, Grafana, Docker, …) |
| Core DB venues | 29 | PVLDB 13 [21,37,38,47,53,57,66,67,69,75,78,79,80]; VLDB conf. proceedings 4 [25,31,55,71]; VLDB Journal 1 [28]; SIGMOD conf. 3 [26,36,62]; PACMMOD 2 [44,56]; PODS 1 [48]; ICDE 1 [39]; TODS 2 [45,65]; TKDE 2 [41,61] |
| Systems / networking / distributed venues | 10 | SOSP 2 [22,51], NSDI [46], FAST [49], ICPP [77], IPDPS [70], ICDCS [76], MobiCom [60], MobiDE [59], ICWS [68] |
| ML / AI / signal / other conferences | 10 | NeurIPS 2 [35,42], IJCAI 2 [52,74], ICPR [32], ICASSP [58], ICCBR [63], NLP-OSS [23], WIC [24], SOCA [40] |
| Other journals / magazines | 10 | Pattern Recognition [27], Computer Networks [29], IEEE IoT J. [30], TSE [33], Linux Journal [34], TOIT [43], MC2R [50], Applied Soft Computing [64], CCPE [72], plus the CISIS conf. [73] grouped here as a minor venue |
| arXiv | 1 | [54] |

(Sum = 80. CISIS is counted in the "other" row to keep the total exact.)

**By year band** (using the year printed in each entry): ≤2010: **21**; 2011-2020: **23**; 2021+: **36** (12 of which are software URLs dated 2021-2025).

**PVLDB/SIGMOD/ICDE**: PVLDB 13 (17 if the 4 pre-2008 VLDB proceedings are included); SIGMOD 3 conference + 1 PACMMOD SIGMOD-track [44] (+1 PACMMOD PODS-track [56]); ICDE 1. That gives **17-18** strictly, or about 22-23 including VLDB proceedings and both PACMMOD entries.

Notable: a quarter of the list (20/80) is URLs. Many application-domain refs (IoT, finance, meteorology, NeurIPS forecasting) exist only to pad the motivation in I-1 (p.2964).

---

## 10. Limitations, discussion, conclusion

- There is **no limitations or discussion section and no threats-to-validity paragraph**.
- **Conclusion** (p.2975): one paragraph of 3 sentences. It restates the definition and system, lists the 5 components, and claims "exhaustive experiments" show better efficiency than "a series of baselines". It has no numbers, no limitations and no future work.
- Honest trade-offs appear only in the experiment prose (see §6), each phrased as a design justification rather than an admitted weakness: the memory/disk cost trade-off (p.2974), the small-request regime where partial hits do not pay off (p.2973), the smaller gains on fresh-data workloads (p.2975), and only on-par hit ratio vs LRU (p.2974).
- The main scoping assumptions are stated once each in the design section and never revisited: append-only/write-once data means no consistency handling (p.2968); a cache-aside, client-side merge (p.2968); trimming only when one boundary is covered (p.2970).

---

## 11. Transferable rules and anti-patterns

### DO (rules)

1. **DO name the system so the acronym encodes the idea, and pattern the title on your closest baseline's title**: this lets reviewers read the delta from the title alone (evidence: title p.2964 vs [53] p.2976).
2. **DO write the abstract gap as a two-horned dichotomy that maps onto your two main baselines**: it sets up both comparisons before they are named (evidence: S2 p.2964, then TSCache/BSCache in I-2 p.2964).
3. **DO end the abstract with two headline sentences, one vs. the systems being accelerated and one vs. the state-of-the-art caches, with baselines named in parentheses**: separate baseline families need separate claims (evidence: S7-S8 p.2964).
4. **DO make every abstract number traceable to a sentence in the evaluation**: STsCache's 79.9% lower bound cannot be found in Sec. 5, which is an easy reviewer catch (evidence: p.2964 vs pp.2972, 2975).
5. **DO critique prior work by named system, with numbered concrete drawbacks**: specific mechanism-level critique (e.g., hashing loses the tag-data relationship) is more convincing than "existing work is limited" (evidence: I-2 p.2964).
6. **DO turn the gap into 2-4 bolded challenge bullets, then map each design mechanism back to a challenge**: it creates a checkable problem-to-solution contract (evidence: I-3 to I-5 p.2965).
7. **DO separate "conceptual contribution" (a formal definition) from "system contributions" in the contribution list**: PVLDB values a reusable formalization on top of engineering (evidence: bullet 1 p.2965).
8. **DO introduce formalism after concrete example queries, then instantiate each definition immediately**: example query, then symbol, then definition, then worked example keeps the formal section readable (evidence: Q1-Q4 p.2966, Def. 1 then Example 1 p.2967).
9. **DO describe the semantic cases informally with a figure before the formal definition, and add a "Whether vs How" bridge between definitions**: it shows the reader why each condition exists (evidence: 3.2 prose + Fig. 2, then Def. 4, bridge, Def. 5 p.2967).
10. **DO provide a notation table once symbols exceed about 8**: reviewers flip back to it constantly (evidence: Table 1 p.2967).
11. **DO open the design section with an architecture figure whose modules map one to one onto subsections, and later onto experiment subsections**: it gives the paper a single spine (evidence: Fig. 5 p.2969, Sec. 4.2-4.6, Sec. 5.4-5.7).
12. **DO present each component as naive design, then "However" plus the flaw, then the refined design, then numbered benefits**: it preempts the reviewer's "why not the obvious approach?" (evidence: 4.4.1-4.4.2 pp.2969-2970).
13. **DO forward-reference the experiment that justifies each magic constant at the point where it is introduced**: it defuses "arbitrary parameter" critiques (evidence: 16KB slab to Sec. 5.4, p.2969; k=1/16 to Sec. 5.5, p.2971).
14. **DO give a complexity bound for the hot-path lookup, with and without your index**: it substitutes for, but should not replace, an index ablation (evidence: Alg. 2 complexity p.2970).
15. **DO add a resource-matched baseline when your system adds hardware**: Dual-TSDB equalizes the server count and blocks the "you just added a machine" objection (evidence: p.2972).
16. **DO, when a prior system cannot run your benchmark, disclose why and give it a tailored but equal-resource workload**: it is transparent and keeps the comparison (evidence: TSCache 128-key limit, same 4% and 1:3, pp.2972-2973).
17. **DO reimplement unavailable baselines on the same code base as your system and say "strictly following [ref]"**: it holds the engineering substrate constant (evidence: BSCache on Fatcache p.2972).
18. **DO split hit ratio into its semantic categories (full vs partial) in stacked bars**: it shows *where* reuse comes from, which matters for result-reuse papers (evidence: Figs 11, 12, 19, 21, 22, 24; metric definition p.2972).
19. **DO sweep the workload property that drives reuse (overlap) and the one that drives overhead (request size) jointly**: it exposes the regime where the method stops paying off (evidence: Figs 15-16 p.2974, text p.2973).
20. **DO state the cost side of a trade-off with numbers next to the gain**: e.g., −6.1-14.9% throughput for −75% memory, which reads as honest engineering (evidence: p.2974).
21. **DO include a robustness experiment for the adversarial or pathological workload your design targets (here cache penetration), sweeping its intensity**: it validates a named challenge (evidence: Fig. 24 p.2975).
22. **DO end the evaluation with a production-style deployment that reuses a baseline paper's own production setup**: it makes the comparison hard to dismiss as tuned to your benchmark (evidence: "followed the production environment of BSCache" p.2975).
23. **DO explain each headline win with 2-3 mechanism-level reasons tied back to design sections**: reviewers want causal attribution, not just numbers (evidence: vs BSCache p.2972; vs TSCache p.2973).
24. **DO state the repetition count and aggregation rule in the setup**: it is the minimal statistical disclosure (evidence: 5 runs, average, p.2972).
25. **DO put the artifact URL in the PVLDB Artifact Availability block on page 1**: it earned the badge and signals reproducibility (evidence: p.2964).

### Anti-patterns (do NOT copy blindly)

- **Assuming consistency away.** STsCache skips invalidation entirely because time-series data is append-only (p.2968). For caches with updates, revocation, or access-control policy changes, invalidation and staleness are the core problem and must be modelled, evaluated and proven.
- **Definitions without soundness theorems.** Answerability (Def. 4) has no correctness proof (pp.2967-2968). A result-reuse or access-control cache must prove that it never returns data outside the new query's or user's scope. Reviewers will demand a theorem.
- **No ablation of the headline mechanism.** The semantic index and the reuse of query-to-query relationships are never switched off in isolation. Only the complexity argument (p.2970) and cross-system comparisons support them. Ablate your central idea directly.
- **Mean-only latency, no variance.** There are no percentiles, error bars or CIs (p.2972). For caching papers, p95/p99 tail latency and run-to-run variance are expected.
- **Missing environment details.** No network bandwidth (despite network overhead being used to explain Fig. 16, p.2973), no SSD model, no TSCache version (p.2972). Disclose everything that affects a cache-aside round trip.
- **Ambiguous relative metrics.** "x% higher hit ratio" without saying points or relative (pp.2964, 2973). Fig. 14's "0.9-1.9× higher throughput" has no stated reference (p.2973). Always name the unit and the comparator.
- **Abstract ranges merged across experiments.** Unioning BSCache and TSCache ranges, and benchmark with production numbers, makes ranges wide and partly untraceable (p.2964 vs pp.2972-2975).
- **Repeating "for the first time" three times** (abstract, intro, contribution 1; pp.2964-2965). Priority claims invite counterexamples. Make one claim, carefully scoped.
- **A conclusion with no limitations or future work** (p.2975). PVLDB reviewers increasingly expect explicit limitations. Put trade-offs in a dedicated paragraph, not only scattered through the results.
- **Calling a 48-hour self-built testbed a "production environment"** (pp.2964, 2975). Label it as a production-style or realistic deployment unless it is a real operator deployment.
- **Descriptive-only captions** ("Effect of X") for 16 result figures. Claim-first captions help skimming reviewers.
- **Padding the motivation with domain citations** (NeurIPS forecasting, IJCAI and so on in I-1, p.2964) and 20 URL references. This inflates the reference count without strengthening the positioning.
- **Typos in pseudocode and headings** ("DeduplicationInertion", "Evicton", "Compatcion"; pp.2970-2974). Proofread algorithm boxes.
- **No figure or measurement in the intro.** STsCache gets away with this, but a motivating measurement (e.g., the hit-ratio loss of key-hash caching on a real workload) would strengthen the gap.

---

## 12. Quantified fingerprint

| Metric | Value |
|---|---|
| Total pages / body pages / reference pages | 14 / 12 / 2 |
| References | 80 (20 URLs; 29 core-DB; PVLDB 13) |
| Figures (all / results) | 25 / 16 |
| Tables | 2 |
| Algorithms | 4 |
| Definitions / examples / theorems | 5 / 2 / 0 |
| Displayed equations | about 6 (unnumbered) |
| External system baselines | 4 (InfluxDB, TimescaleDB, TSCache, BSCache). TSDB variants: Single-HDD, Single-SSD, Dual. Policy baselines: 2 (FIFO, LRU). Self-ablation variants: 5 |
| Metrics | 3 primary (throughput, mean end-to-end latency, hit ratio), or 4 counting full/partial hit separately. Plus 1 derived (memory saved) |
| Datasets / workloads | 2 TSBS use cases × 3 scales = 6 benchmark configurations (25.85-422.93 GB, 3.15-50.5 B points), plus 3 production-style workloads in 2 environments |
| Explicit RQs | 0 (6 experiment subsections 5.3-5.8, organized by design module) |
| Sensitivity sweeps / ablations | 8 / 5 |
| Repetitions / error bars | 5 runs averaged / none |
| Pages on experiments | about 4.0 (p.2971 lower right to p.2975 upper right) |
| % of body on experiments | about 33% |
| Approximate page budget | Title + abstract 0.4; Intro 1.4; Prelims + RW 0.7; Formal def. 1.75; Design 3.55; Experiments 4.0; Conclusion + ack 0.2 |
| Abstract | 8 sentences, about 178 words, 7 numeric ranges |
| Contributions | 4 bullets, all "We propose", no numbers |
