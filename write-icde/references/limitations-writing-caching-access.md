# Writing the limits of a caching / access-control method without self-negation

Reference for revising **ScopeCache** (permission- and version-safe result reuse for multi-principal LLM data agents, ICDE 2027 R2). Built from eight accepted papers on result caching, computation reuse, and fine-grained access control, read on 2026-11-10. Every quotation below was checked verbatim against the extracted full text and is shorter than 15 words; section numbers refer to the version listed in Section 1.

Contents: 1. Papers read; 2. Per-paper extraction (six questions); 3. Cross-paper patterns; 4. Rewrite rules with before/after examples for ScopeCache; 5. Phrases to avoid; 6. Checklist for the ScopeCache revision.

---

## 1. Papers read

| # | Paper | Venue, year | DOI / URL used | Full text read? |
|---|---|---|---|---|
| P1 | Pappachan, Yus, Mehrotra, Freytag. *Sieve: A Middleware Approach to Scalable Access Control for Database Management Systems* | PVLDB 13(11), 2020 | doi:10.14778/3407790.3407835; PDF: https://par.nsf.gov/servlets/purl/10384098 (published PVLDB version) | Yes (body, all sections; algorithm internals of Sec. 4 skimmed) |
| P2 | Tran, Vasudevan, Desai, et al. *Data Guard: A Fine-grained Purpose-based Access Control System for Large Data Warehouses* | Given in the brief as ICDE 2026; read arXiv:2502.01998v2 (IEEE conference format, 21 Oct 2025) | https://arxiv.org/abs/2502.01998v2 | Yes. The ICDE 2026 acceptance could not be checked independently: dblp was unreachable from this machine, and the arXiv page shows no venue |
| P3 | Nagel, Boncz, Viglas. *Recycling in Pipelined Query Evaluation* | ICDE 2013 | doi:10.1109/ICDE.2013.6544837; PDF: https://ir.cwi.nl/pub/21352/21352A.pdf | Yes |
| P4 | Durner, Chandramouli, Li. *Crystal: A Unified Cache Storage System for Analytical Databases* | PVLDB 14(11), 2021 | doi:10.14778/3476249.3476292; https://www.vldb.org/pvldb/vol14/p2432-durner.pdf | Yes |
| P5 | Schmidt, Kipf, Horn, Saxena, Kraska. *Predicate Caching: Query-Driven Secondary Indexing for Cloud Data Warehouses* | SIGMOD Companion 2024 (industry) | doi:10.1145/3626246.3653395; PDF via amazon.science | Yes |
| P6 | Bindschaedler. *Semantic Caching for OLAP via LLM-Based Query Canonicalization (Extended Version)* | Short version: DOLAP 2026 workshop (EDBT/ICDT 2026); read the extended arXiv:2602.19811 | https://arxiv.org/abs/2602.19811 | Yes. It is a workshop paper, so it serves partly as a **contrast case** (see P6 item 6) |
| P7 | Bruno, Debrodt, Song, Zheng. *Computation Reuse via Fusion in Amazon Athena* | ICDE 2022 | PDF: https://cdn.amazon.science/24/f4/bd95d35b4a02bea58fb588d80f84/computation-reuse-via-fusion-in-amazon-athena.pdf | Yes (replacement for LBSC) |
| P8 | Zhang, Sheng, Chang, Panda, Sagiv, Shenker. *Blockaid: Data Access Policy Enforcement for Web Applications* | OSDI 2022 | https://www.usenix.org/system/files/osdi22-zhang.pdf | Yes (replacement for Dynamic Materialized Views). Not a DB venue, but it is the closest accepted work on **caching access-control decisions** and has a model threat-model paragraph |

**Not accessible, so replaced:**
- *LBSC: A Cost-Aware Caching Framework for Cloud Databases* (Ji, Xie, Wu, Zhang; ICDE 2024, pp. 4911-4924). No open-access full text was found (only abstract listings); replaced by P7 (ICDE 2022, computation reuse).
- *Dynamic Materialized Views* (Zhou, Larson, Goldstein, Ding; ICDE 2007, doi:10.1109/ICDE.2007.367898). Only IEEE Xplore and academia.edu listings were found, with no open PDF; replaced by P8. No statement in this file is attributed to these two papers.
- No further ICDE 2024-2026 paper on semantic/result caching or row-level security with open full text turned up within this search. The Sieve follow-up (Shakya et al., arXiv:2511.14629) is a journal-format preprint with no acceptance record, so it is not used.

---

## 2. Per-paper extraction

Format of each entry: (1) abstract qualifiers, (2) losses and weak regimes, (3) threat model and assumptions, (4) side channels, scale, synthetic data, missing real workloads, (5) how the experiments present "where it helps less", (6) what the paper never writes.

### P1 Sieve (PVLDB 2020): middleware FGAC with guarded expressions

1. **Abstract.** The scope sits in the problem statement: existing FGAC does not scale "when the number of access control policies are in the order of thousands". The paper's claim is then positive and bounded by that setting. The abstract contains no sentence about what Sieve cannot do.
2. **Losses and weak regimes.** Losses appear as **crossover thresholds inside the method's own design**, not as defeats. The UDF operator is worth its invocation cost only above a partition size (Sec. 5.2): “the usage of the Guard&∆strategy is beneﬁcial if |PGi| > 120”. Exp. 2.2: “at low query cardinality it is better to utilize IndexQuery”, followed by a numeric boundary (> 0.07). A baseline's odd behaviour gets a mechanism: “the optimizer is able to use the low cardinality join condition”. Pattern: regime, then the cost-model choice that exploits it.
3. **Assumptions.** Each simplification is stated once in the model section as a focus: “we focus on the object conditions with values as constants” (Sec. 3.1), and “We therefore restrict our discussions to allow policies” (Sec. 3.1), after showing that deny policies can be translated into allow policies. The guarantee is named by borrowing an established criterion: “satisﬁes the sound and secure properties of the correctness criterion” (Sec. 3.1).
4. **Synthetic data and scale.** Real data (3.9M WiFi events) is paired with **synthetic policies**, and the paper gives the reason directly: the dataset “does not include user-deﬁned policies. We therefore generated a set of synthetic policies” (Sec. 6.1). It calibrates them with fieldwork: “we conducted several town hall meetings and online surveys”. A second, fully synthetic dataset (Mall) is used only for the stress test with more policies. A missing DBMS feature becomes an experiment: PostgreSQL does “not support index usage hints explicitly”, so Exp. 4 measures exactly that case and finds “the speedup factor w.r.t. the baseline is even higher than in MySQL”. Timeouts are encoded in the table: “those time values are denoted as t+”. A cost estimate is flagged honestly as one-sided: “Note that this is an upper bound of the cost” (Sec. 5.3).
5. **Experiment presentation.** Numbered experiments, each opening with "The goal of this experiment is ...". Design-choice experiments (Exp. 2.1, 2.2) present the regimes where each alternative wins. The extended version is pointed to without apology: “Due to space limitations, we could not describe several technical details” (Sec. 1).
6. **Never writes.** No "limitation" of Sieve itself (the word appears only for prior work and for space), no threat-model caveat, and no statement that the results may not generalize. Future work is a plan, not a gap: “We plan to leverage the experience gained while developing Sieve” (Sec. 7).

### P2 Data Guard (ICDE 2026 per brief; arXiv v2): purpose-based masking views

1. **Abstract.** It is entirely positive and scoped by setting ("for large data warehouses", "purpose of the access"). The evaluation claim is qualitative ("identify the key factors that influence the data masking overhead"), and deployment scale (20,000 table accesses a day) stands in for breadth. No negative sentence.
2. **Losses and weak regimes.** Overhead is reported together with **the regime that drives it and the regime that removes it** (Sec. VI-B): heavier views are those that target multiple fields or deep structures, “consistent with our micro-benchmark results”, while “In some cases, row-level masking can even reduce query cost”. Every micro-benchmark curve is explained mechanistically (traversal and reconstruction of immutable structs make overhead linear in depth). Boundary case: “A consent rate of 1.0 reduces the masking query to the baseline query”.
3. **Assumptions.** Restrictions are introduced with a reason and an extension path. “For simplicity, we only consider a specific form of data redaction”; “Note that the same model can be extended to define and support other types” (Sec. IV-A3). “We further restrict the policy conditions to be based on data subject consents only”, with the motivation that “data subject consents are the most common basis for data access policies” at the company. A deployment artifact is explicitly decoupled from the model: the model “does not require an ontologybased organization of policy labels” (Sec. VII).
4. **Benchmark, data, scale.** The missing benchmark is turned into a contribution: “Since there has been no prior standard benchmark”, they build their own micro-benchmark (Sec. VI-A). Format generality is stated as an expectation: “we expect similar trends for other widely used formats such as Parquet”. Excluded operations are justified as orthogonal: “as these operations are application-specific and orthogonal to the data-masking operation”. Bypass and staleness are handled by a mechanism, not a disclaimer: continuous log monitoring “detects potential bypasses or accesses to stale views” (Sec. VII). Versioning is a design feature: “each data-masking view is versioned according to the semantic versioning scheme” (Sec. V-A4).
5. **Experiment presentation.** One subsection per factor ("Impact of Data Type", "Impact of Field Depth", "Impact of number of policies applied", "Impact of consent rates"), then production statistics. The average 13.2% CPU overhead is framed against the value protected: “which we consider acceptable given the importance of access control”.
6. **Never writes.** The single own-method "limitation" (UDF masking blocks predicate pushdown) sits in a "Practical Considerations" section and is followed at once by priority and outlook: “we recognize opportunities for further optimizations”. Heuristics are acknowledged as heuristics with a plan: “While these optimizations are presented as heuristics in this paper”. The missing theory is called “an important future direction”, not a weakness.

### P3 Recycling in Pipelined Query Evaluation (ICDE 2013)

1. **Abstract.** The novelty is scoped by the execution model ("in pipelined query executors"), and the comparison point (MonetDB materializes everything) is set up as a different design space rather than a competitor to beat. No negative sentence.
2. **Losses and weak regimes.** This is the clearest **fact, then mechanism, then regime** sequence in the set. Fact: “MonetDB beneﬁts the most with an unlimited recycler cache size”. Mechanism: (a) its operator-at-a-time paradigm materializes intermediates for free, (b) its matching is lighter. Regime where the paper wins: in the limited recycler cache scenario, “our approach shows a greater improvement”. Internal mode losses follow the same pattern: speculation beats proactive at 4 and 16 streams because there were “not enough reuse possibilities in the workload to amortize the extra execution cost”. A known blind spot is stated as a property of a mode: history mode “performs badly for results that only occur twice in the workload”, and the next mode is introduced to fix it.
3. **Assumptions.** Prior work's assumption is named and contrasted (“This assumption is shared with most prior work on recycling”). A trade-off is labelled as a decision: “This reduced complexity comes at the price of missing sharing opportunities”, followed by “This was a design choice: doing so allows us to handle more queries”. Updates are scoped out in one line: “In this work, we focus on materialization strategies and leave maintenance out of scope” (Sec. II), after sketching eviction-on-commit and view maintenance as the known options.
4. **Simulation and missing features.** Missing engine support is stated, and the result is shown to hold without it: “Vectorwise’s optimizer does not support materialized views so we could not explore this direction”, then “there is substantial performance to be gained even without optimizer integration”. Simulations are named as simulations, with the method: “To simulate the effect of updates invalidating cached results” (flushing every 25 or 50 queries), and for unimplemented rules, “we simulate their beneﬁt by manually altering query plans”. The robustness claim follows: “Even with a refresh every 25 queries, recycling is still quite beneﬁcial”. Production truncation is mentioned and dismissed with evidence: “In our testing, there was no need for truncation”.
5. **Experiment presentation.** Paragraph headings name questions ("Throughput Scaling", "Per-Query Breakdown", "Detailed Trace", "Matching Cost"). Overhead is bounded relative to the benefit: “even the highest matching cost is orders of magnitude lower than the evaluation cost”.
6. **Never writes.** No "limitations" paragraph, no "unfortunately", and no claim about MonetDB being worse in general. Future work is a named variant: “A subsumption variant we leave to future work is dimension subsumption”.

### P4 Crystal (PVLDB 2021): unified semantic cache storage

1. **Abstract.** The claim is qualified by integration conditions ("with a small DBMS-specific data source connector", "on unmodified Spark and Greenplum"). Numbers carry "up to" and "on average" (introduction: up to 20x per query, 8x on average, up to 41% bandwidth). No negative sentence.
2. **Losses and weak regimes.** Baselines are allowed to tie in a precisely bounded regime: “Only in this extreme scenario, Alluxio is able to match” (cache size of 110% of the data, Sec. 6.3). The warm-up cost is said plainly with its cause: “The traditional caches directly reach the maximum performance whereas RR / OR learns”. Own components fail on named workloads, and the combined design is the answer: “Long-term caches (OR) fail to catch the events due to their latency constraints” (Sec. 6.4). The weak benchmark is explained by its structure before the number is given: “Most restrictions come from join conditions which currently cannot be pushed down”, then “the OR approaches are able to improve the mean performance by up to 20%” (Sec. 6.7).
3. **Assumptions.** A restriction is turned into a lever. Cached regions are restricted in that “they are strictly the result of single-table predicates”, and “This restriction is exploited in our solutions to the technical challenges” (Sec. 1.3). The extension is described as engineering: future cross-table push-down means “Such developments will require a revisit of our algorithms in future”. Updates: “We focus on readonly workloads in this paper”; “updates can be handled by view invalidation (easy) or refresh (more challenging)”. An immature dependency: “a detailed study is deferred until the technology matures”.
4. **Synthetic data.** Workload synthesis is anchored in precedent and released: “Following prior work [18], we synthesize queries”; “We have made the queries available at [12]”. Generality across engines: “the relative beneﬁts of using Crystal stay similar” on Greenplum.
5. **Experiment presentation.** Subsections are named by scenario ("Regions of Query Accesses", "Benefit of RR/OR", "Changing Regions", "TPC-H", "Microbenchmarks"). Each weak case is a dedicated scenario that motivates a component.
6. **Never writes.** "Unfortunately" occurs once, for a rejected design alternative (exponential knapsack search), never for the final system. "Preliminary" is used once, for an experiment that rules out an alternative.

### P5 Predicate Caching (SIGMOD Companion 2024)

1. **Abstract.** The bound is in the number: “up to 10x on selected queries”. The motivation names the failure mode of the alternatives (result caches are stale under updates), not of the method.
2. **Losses and weak regimes.** This paper shows best how to **state a small or null effect without self-negation**. (a) Small effect plus a secondary metric: “While this performance improvement is not as significant, the number of scanned rows shrinks” by almost 4x (Sec. 5.5). (b) Mechanism for the small effect: “the data is still too evenly distributed”, then a stated expectation: “We expect real-world data sets to be more skewed”. (c) Null result stated plainly: on standard TPC-H “the predicate cache does not impact the runtime”, followed by the regime rule “predicate caching performs better on data sets with a more uneven distribution” (Sec. 5.5.2). (d) A baseline wins slightly and is reframed as complementary: “Sorting techniques achieve similar gains as predicate caching”, and “the overall runtime improvements are slightly larger”; then “We expect sorting to perform better on other workloads with more selective queries” (Sec. 5.6), followed by a combination experiment and a "bridges this gap" positioning.
3. **Assumptions.** The workload premise is stated as the premise of all caches: “Caches operate on the assumption that the system’s workload repeats over time” (Sec. 2.1), then measured on the fleet. Applicability is a **list of positive requirements**: “predicate caching can be applied to any data format that fulfills the following requirements” (row identity, infrequent renumbering, detectable changes; Sec. 4.5). Safety under approximation: merged ranges introduce false positives, so “the system must re-evaluate the predicate on the cached rows to eliminate false positives” (Sec. 4.1.1). Invalidation is stated as an event: “vacuum changes the row ranges in the predicate cache, and we invalidate the cache” (Sec. 4.3.2). The trade-off of an extension: “Combining the predicate cache with semi-join filters also has disadvantages”, ending with “Hence, we must weigh the benefits of including the join”.
4. **Scale and real workloads.** Real fleet statistics motivate the problem (Sec. 2). The evaluation uses synthetic benchmarks plus two internal workloads that "simulate customer clusters". Overhead is bounded: “average runtime degrades by less than 0.5 % for both TPC-H and TPC-DS”.
5. **Experiment presentation.** Sections on memory, hit rate, build overhead, query performance, and "Predicate Caching vs. Sorting". Table 1 grades result caching, MVs, sorting, and predicate caching on four criteria with ++/+/−/−−, and **gives the proposed method a lower "Gain" than result caching**: an honest trade-off table that still shows the method as the only one without a "−".
6. **Never writes.** No "limitation" or "threat" section. Competitors are treated generously: “Despite the low hit rate, it is still worthwhile to install the result cache”. The design promise is phrased as a goal achieved: “while rigorously avoiding slowdowns”.

### P6 Semantic Caching for OLAP via LLM canonicalization (DOLAP 2026, extended arXiv)

1. **Abstract.** It is scoped positively ("dashboard-style OLAP over star schemas"), and safety is a feature ("Reuse requires exact intent matches under strict schema validation"). The abstract reports "zero false hits" without hedging.
2. **Losses and weak regimes.** Out-of-scope queries take a named safe path: “queries outside this subset bypass the cache and execute directly on the backend” (Sec. 1). Coverage is quantified rather than hidden: “In TPC-DS, 14 of 99 query templates (14%) qualify” (Sec. 3.1), with the safety consequence “ensuring the system never returns incorrect results for unsupported query patterns”. A weak regime is scoped "by design": TPC-DS and NYC TLC lack hierarchy traversal, “so derivations provide limited benefit on those workloads by design” (Sec. 5.5). Capacity: “Interleaved requires larger caches” (Sec. 5.4), with a 0.0% cell reported in the table.
3. **Assumptions.** Section 3.1, "Scope and Assumptions", lists the deliberate exclusions (window functions, set operations, ...) and the join-path assumption, each with its bypass. It separates two kinds of correctness: “cache correctness (a hit returns the same result as backend execution)” versus user-intent correctness (Sec. 5.3). This is directly reusable for ScopeCache (data-level soundness versus whether the agent asked the right question). The rule is “prioritize misses over incorrect reuse” (Sec. 3.5). Multi-tenant isolation is an optional signature field, and the paper says “our evaluation uses ungoverned single-tenant schemas” (Sec. 3.3).
4. **Synthetic data and missing real workloads.** These are discussed in an explicit "Limitations" subsection (Sec. 6.3) and in Sec. 6.2: “Our evaluation uses static snapshots, but production systems must link entries to data freshness”.
5. **Experiment presentation.** RQ-shaped subsections ("RQ2: Does Intent-Signature Caching Preserve Correctness?"), a coverage-precision trade-off table, and "Deployment Knobs" profiles (Conservative / Balanced / Aggressive).
6. **What a full research paper should not copy (contrast case).** Some sentences in this workshop paper weaken its own evidence in a way the seven full papers avoid: “Controlled variants may overstate hit rates vs. production traffic” (Sec. 6.3), and in the conclusion, “Robust invalidation under data updates is the key gap for production deployment”. The confidence score is called “an uncalibrated heuristic used for coarse gating” (Sec. 3.4). Each is true, but stated without a bound, a mitigation, or a measured counter-check, so it reads as self-negation. The full papers instead either measure the gap (Sieve's Exp. 4, Recycling's flush simulation) or scope it to a precedent (Crystal's read-only scope, Recycling's maintenance scope).

### P7 Computation Reuse via Fusion in Amazon Athena (ICDE 2022)

1. **Abstract.** It names the class of queries ("query patterns that have common expressions"; "handle some common expression scenarios"). The conclusion repeats the scope: the techniques “improve performance of a class of queries containing common subexpressions”.
2. **Losses and weak regimes.** It reports **both the whole workload and the applicable subset**: 14% on all 99 TPC-DS queries, and “improves almost 60% for the subset of applicable queries” (Sec. I). In Sec. V: “However, not all queries trigger our optimization rules”; then “our techniques are not applicable to all possible queries but instead target specific patterns”, immediately balanced by “those patterns are not uncommon in complex analytical queries” and backed by customer-data analysis. A small latency gain is given a mechanism and a second metric: “modest improvements in latency (below 10%, as the data scans are in parallel)”, but 20-40% less data read and lower CPU (Sec. V-A).
3. **Assumptions.** Generality is bounded by a general fallback: “not all queries with common expressions can be rewritten”, so “the general case should be handled by spooling intermediate results”, which “is part of Athena’s future roadmap” (Sec. I).
4. **Scale.** The scale factor is justified by real customers: 3 TB, “which is consistent with the 99th percentile of data sizes” (Sec. V).
5. **Experiment presentation.** A short quantitative overview, then one subsection per rewrite pattern, with the gain range per pattern (moderate to 6x).
6. **Never writes.** No threat-to-validity section and no statement that TPC-DS is unrepresentative. The fallback (spooling) is presented as the system's roadmap, not as a weakness of the paper.

### P8 Blockaid (OSDI 2022): access-policy enforcement with a decision cache

1. **Abstract.** It is positive, with "modest overheads" and "minimal code changes". The limits are stated **in the introduction, in three sentences**: “Blockaid has some important limitations”. It assumes all information flows through SQL visible to Blockaid (or mediated caches and files), and it “supports only a subset of SQL and is at the mercy of solver performance” (Sec. 1).
2. **Losses and weak regimes.** The cost without the paper's cache is given plainly: “With caching disabled, Blockaid incurs up to 236× higher median PLT” (Sec. 8.4); on a cold cache 7x-422x (Sec. 8.5), with the mechanism “due to the extra template-generation step”. The measurement condition is flagged: “these experiments reflect the best-case PLT” (client co-located). Porting effort is admitted with amortization: “writing the Spree policy took one of us roughly a month”, then "this process would be easier for the developer of a new application".
3. **Threat model.** This is the model paragraph for the set (Sec. 3.1, "Application Assumptions and Threat Model"). The application authenticates correctly; “We treat the database schema and the policy itself as public knowledge”; “assume that the user cannot use side channels to circumvent policies”. Writes are out of scope with precedent: “Ensuring the integrity of updates, while important, is orthogonal to our goal”. Workload assumption: “We assume noncompliant queries are rare in production”. Cache safety: “It does not cache noncompliance results”. Generalized cache entries keep soundness because they are “assumptions on the query and trace that alone would guarantee compliance”.
4. **Side channels and false outcomes.** Side channels are covered by the assumption above; no attack analysis is attempted. False rejections are handled with the pattern **observed fact, then why it remains possible, then mitigation**: “false rejections of compliant queries never occurred in our evaluation”, yet “they remain a possibility for several reasons” (three listed). Then: developers can reduce the chance by running end-to-end tests, and an off-path mode is offered, in which “we can modify Blockaid to log potential violations instead of blocking” (Sec. 9).
5. **Experiment presentation.** Four settings (original, modified, cached, no cache) and a cold-cache variant, so that the cost of every layer is visible. A "Template Generalization" subsection works through a template that does **not** fully generalize and explains three reasons.
6. **Never writes.** No "we cannot guarantee"; the theoretical non-optimality is phrased as "general enough in practice" plus its root cause: “our template generation algorithm is limited by its black-box access to the policy”. A rejected alternative gets a reasoned paragraph: “We decided against this design alternative for two reasons”.

---

## 3. Cross-paper patterns

1. **Abstracts never contain a negative sentence about the method.** All eight scope the claim through the setting, the query class, or the integration condition ("for large data warehouses", "a class of queries", "dashboard-style OLAP", "on unmodified Spark and Greenplum"). Numbers carry "up to", "on average", or "on selected queries".
2. **Limits live in three predictable places**: (a) the model or assumptions section, as a focus with a reason (P1, P2, P6); (b) a short, named paragraph near the end ("Practical Considerations", "Additional Issues", "Discussion"), or three sentences in the introduction (P8); (c) inside the experiment that measures the regime. None of the seven full papers has a "Threats to validity" or "Weaknesses" heading.
3. **Losses follow a fixed four-step sentence pattern: fact, then mechanism, then regime, then bound.** P3 (MonetDB with unlimited cache), P4 (Alluxio at 110%), P5 (uniform TPC-H; sorting), P7 (modest latency, parallel scans). The mechanism always names a property of the workload or the competitor's paradigm, never a defect in the method.
4. **A small effect is paired with a second metric that moved** (rows, bytes, CPU, executions), and with the regime in which the first metric would move (P5, P7).
5. **Out-of-scope inputs take a safe path that the paper names**: bypass (P6), a general fallback (P7 spooling), recheck (P5 false positives), no caching of negative decisions (P8). The limit then reads as a safety property.
6. **Restrictions are turned into levers** (P4 single-table predicates; P3 AND-DAG design choice; P1 deny-to-allow translation).
7. **Updates and maintenance are scoped by precedent, in one sentence**, with the known options named (P3, P4, P8). Where the method handles updates, invalidation is described as an event with a trigger (P5 vacuum; P2 view versioning).
8. **Synthetic data is justified, not apologized for**: field calibration (P1), no existing benchmark (P2), following prior work plus released queries (P4), a real-customer percentile for scale (P7). No paper says its synthetic data "may not reflect" reality; the contrast case P6 does, and it reads weaker for it.
9. **Overheads are quantified and then weighed against the protected value or the saved cost** (P2 13.2% "acceptable given the importance of access control"; P5 < 0.5%; P3 matching cost orders of magnitude below query cost; P8 cached versus uncached).
10. **Zero-error claims are separated from guarantees.** "Never occurred in our evaluation" (evidence) is kept apart from "would guarantee" (theorem or construction), and residual possibilities are listed with mitigations (P8).
11. **Negative vocabulary targets rejected alternatives and prior work, not the final system** (P4 "Unfortunately" for the DP search; P1 and P2 "limitations" for prior approaches).
12. **Future work is a constructive extension tied to an existing component** ("dimension subsumption", "spooling roadmap", "formalize heuristics"), never a "gap that blocks deployment".

---

## 4. Rewrite rules for a caching + access-control paper (with ScopeCache examples)

The "Before" sentences show typical self-negating drafts; they are illustrative, not quotations from the current ScopeCache manuscript. The "After" sentences use the paper's macros and facts as they appear in `overleaf_git/main.tex` (version of 2026-11-10). Check every number against `numbers.tex` before use.

**R1. Put the scope into the claim; do not add a negative sentence to the abstract.** (P2, P4, P6, P7)
- Before: "ScopeCache does not support non-distributive aggregates, multi-table policies, or data updates."
- After: "For distributive metrics over a governed fact table, ScopeCache shares results across principals with different row and column scopes and never returns data outside the requester's view."

**R2. State each guarantee with its domain in one sentence, and say which real systems the domain covers.** (P5 requirement list, P6 "under the schema conditions", P1 named criterion)
- Before: "Our theorems only hold under restrictive assumptions."
- After: "Theorems 1-3 hold for distributive aggregates over one fact table between data loads and for row predicates that are DNFs over that table's attributes; the grant models of the metric platform and of the ERP system are of this form."

**R3. Give every out-of-domain input a named safe path, so that the limit reads as a safety property.** (P6 bypass, P5 recheck, P8 negative decisions not cached, P7 spooling fallback)
- Before: "COUNT DISTINCT cannot be shared across scopes, which limits our approach."
- After: "Distinct counts take the scope-keyed path: they remain sound and are reused within a scope, and mergeable sketches would let them share across scopes approximately."

**R4. Present a structural restriction as the lever that makes the method work.** (P4 "This restriction is exploited")
- Before: "A limitation is that policies must be expressed over attributes of the fact table."
- After: "Because grants are predicates over policy attributes of the fact table, an aggregate grouped by those attributes is principal-independent; this is what lets one execution serve every scope. Policies on other tables are first resolved to value sets of a policy attribute, as the platforms do when they compile grants."

**R5. Label trade-offs as design choices: the cost, then the reason, then what the choice buys.** (P3 "This was a design choice"; P8 "decided against ... for two reasons")
- Before: "Our cell granularity is not optimal and wastes space."
- After: "ScopeCache keys cells on raw policy values. Coarsening cells to grant-literal classes changes warehouse executions by only X to Y% and, on the ERP grants, would reduce the number of cells by a factor of Z; raw values also make grant edits that introduce new value sets free."

**R6. Write the threat model as named assumptions plus what the principal observes; name each channel together with its mitigation and the exact price of that mitigation.** (P8 Sec. 3.1; ScopeCache already follows this; keep it)
- Before: "ScopeCache is vulnerable to timing side channels, which we leave to future work."
- After: "A principal observes the returned values and the response time. Response time reveals whether a call hit; a deployment that must close this channel can answer every call at the latency of a miss, which keeps all savings of warehouse work, the cost the problem minimizes, and gives up only the latency gain."
- Keep the assumptions in one place (trust domain, authenticated principal, public schema and policy, reads only), as P8 does. Do not scatter them across Discussion and Related Work.

**R7. Report a loss to a baseline as fact, then mechanism, then regime, then bound.** (P3 MonetDB, P4 Alluxio, P5 sorting)
- Before: "On BIRD and ENT, ScopeCache brings no improvement over PerScope+V."
- After: "On BIRD and ENT, PerScope+V performs as well as ScopeCache: their calls concentrate on few groupings, so the shared pinned views already answer the calls that online entries could share. The gap opens with the spread of the workload and the size of the policy domain: \psvTpchLo--\psvTpchHi\% on TPC-H, and it is largest at 3,000 policy values (Fig. X)." (Use the real macro values.)

**R8. Report the whole workload and the subset where the mechanism applies.** (P7: 14% overall, 60% on affected queries)
- Before: "Cross-scope sharing helps only a minority of calls."
- After: "ScopeCache served A-B% of agent data calls from entries created under another scope; on these calls it saved C% of warehouse executions, and over all calls D%."

**R9. When the headline metric moves little, name the mechanism and report the metric that did move.** (P5 rows scanned; P7 bytes and CPU)
- Before: "Latency gains are small."
- After: "Latency improves by only X% when warehouse scans run in parallel, but warehouse executions drop by Y% and scanned bytes by Z%, which is the cost a metered warehouse bills."

**R10. State a weak or null regime as a rule about the workload, and support the expectation with a measurement, not hope.** (P5 "performs better on data sets with a more uneven distribution")
- Before: "If principals do not share questions, ScopeCache may provide little benefit."
- After: "With a single principal per question (k = 1), every cross-scope hit reuses an entry created for a different question, and ScopeCache still serves A-B% of data calls from other scopes; at k = 2 the share rises to C-D%. In the ERP system, an aggregation endpoint is called by a median of E accounts per hour."

**R11. Justify synthetic components by provenance and calibration, and release them; do not attach "may not reflect reality".** (P1 field calibration, P2 no benchmark exists, P4 prior work plus released queries, P7 customer percentile)
- Before: "Our fact tables are synthetic, so results may not generalize to real deployments."
- After: "ERP uses the real account-to-shop grants of a production ERP system (N active accounts, M distinct scopes) over a synthetic fact table on the same 287 shops, with the permission-event rate measured in that system; ENT reconstructs an enterprise metric platform whose organization tree, grant modes, metric types, and query format follow the platform's code. Code, traces, and generators are released."

**R12. Name simulations as simulations, give the method, and draw the robustness conclusion from them.** (P3 flushing every 25 queries; manual plan edits)
- Before: "We could not observe real permission changes at scale."
- After: "To stress permission events beyond the measured rate, we raise the event rate up to 16 times the rate measured in the ERP system; ScopeCache keeps its hit rate because grant changes require no invalidation (Theorem 2)." (Match the wording to the actual RQ4 protocol.)

**R13. Quantify overhead, then weigh it against the saved cost or the protected value.** (P2 13.2% "acceptable given the importance of access control"; P3 matching cost; P5 < 0.5%)
- Before: "Lookup adds non-negligible overhead."
- After: "Lookup and scope application add a median of X ms per call, compared with the Y-second warehouse execution that a hit avoids." (Fill X and Y from the overhead table; state the ratio only after computing it.)

**R14. Separate the guarantee from the evidence, and list residual risks with their mitigation.** (P8 false rejections; P6 cache correctness versus intent correctness)
- Before: "Although we found no errors, we cannot guarantee correctness in all cases."
- After: "Theorem 1 guarantees that every answer equals a fresh execution under the current policy and semantic layer. Independently, differential testing of N data calls per cache found no wrong answer. Whether an agent asked the right question is a separate property that ScopeCache neither changes nor relies on."

**R15. Scope updates and maintenance by precedent, in one sentence, and state the event that invalidates.** (P3, P4, P5 vacuum, P2 versioned views)
- Before: "ScopeCache does not handle data updates."
- After: "The base data changes in loads; as for materialized views, a load of a fact table invalidates its entries, and we consider reuse between loads. Republished metric definitions invalidate only the measures whose definition hash changed (Theorem 3)."

**R16. Turn a missing platform feature into an experiment or a measured variant, not a disclaimer.** (P1 PostgreSQL without hints, P3 "even without optimizer integration")
- Before: "We could not integrate ScopeCache into the warehouse optimizer."
- After: "ScopeCache runs as a component between the metric tool and the warehouse and needs only three platform interfaces: grant evaluation as a DNF, base-measure definition hashes, and the tool's request format. All results above are obtained without optimizer integration."

**R17. Offer deployment knobs for the conservative operator.** (P8 log-only and off-path modes; P6 configuration profiles)
- After (ScopeCache): "Operators can run ScopeCache in shadow mode, answering from the warehouse while logging what the cache would have returned, to audit equality before enabling it; and in constant-latency mode (R6)." Add only if implemented or trivially implementable, and never invent a measured result for it.

**R18. Be generous to baselines and say when each is the right choice.** (P5 "still worthwhile to install the result cache"; P2 "effective in their original settings")
- Before: "PerScope is a naive baseline."
- After: "PerScope is the right design when principals rarely differ in scope; ScopeCache targets platforms where principals map to many distinct scopes, as in all five setups (Table~\ref{tab:setups})."

**R19. Give the experiments question-shaped headings and a one-sentence takeaway that names the regime.** (P3 paragraph headings, P4 scenario subsections, P6 RQ titles)
- Pattern: "**When do principals share questions?** ... Takeaway: cross-scope sharing does not require identical questions; derivation (roll-up, filtering, sub-ranging) supplies most cross-scope hits at k = 1."

**R20. Phrase future work as an extension of an existing component, placed after a result, in one sentence.** (P3 dimension subsumption; P7 spooling roadmap; P2 formalize heuristics)
- Before: "Supporting sketches remains a key open problem for deployment."
- After: "Mergeable distinct-count sketches would extend cross-scope sharing to COUNT DISTINCT, with the approximation bound of the sketch."

---

## 5. Phrases to avoid, with replacements

| Avoid | Why | Use instead |
|---|---|---|
| "Our method fails to ..." / "does not work when ..." | Self-negation; not used by any full paper for the final system | "In regime R, baseline B performs as well because M" (R7) |
| "Unfortunately, ..." | Used in P4 only for a rejected alternative | State the fact and the mechanism |
| "A major / important limitation of our approach is ..." (as a standalone admission) | P8 uses "important limitations" only once, as a 3-sentence factual scope, each item concrete | "ScopeCache assumes ..." followed by the concrete condition and its safe path (R2, R3) |
| "Results may not generalize" / "may overstate" / "may not reflect real workloads" | Unbounded doubt; appears only in the workshop contrast case P6 | Provenance plus calibration plus release (R11); a measured counter-check (R10) |
| "We cannot guarantee ..." | Confuses guarantee with evidence | Theorem plus differential testing, kept separate (R14) |
| "vulnerable to side channels" / "we do not address side channels" | Names a threat without scope or mitigation | Name the channel, the observer, the mitigation, and its price (R6) |
| "We leave X to future work" as the only treatment of X | Reads as a gap | Precedent scope plus invalidation event (R15) or a constructive extension (R20) |
| "is the key gap for production deployment" | Self-disqualifying (P6 contrast) | Deployment interfaces required plus what has been validated (R16) |
| "naive baseline", "simple baseline" (for a fair competitor) | Invites reviewers to doubt the comparison | Name the baseline's design point and when it is right (R18) |
| "only marginal / negligible improvement" without a second metric | Hides the mechanism | Mechanism plus the metric that moved (R9) |
| "toy", "preliminary", "proof of concept" (for the main evaluation) | Absent from all eight papers for their own main results | "prototype in X, evaluated on N setups" |
| "Note that our assumptions are strong" | Undefined value judgement | List the assumptions and the systems that satisfy them (R2) |
| "heuristic" without a bound or a plan | P6 "uncalibrated heuristic" contrast | P2 pattern: "presented as heuristics; we plan to formalize" only when true, or give the bound |
| "always" / "never" for measured (not proven) properties | Over-claim that reviewers can falsify | "in all N runs" for evidence; "never" only for what a theorem proves |
| "ScopeCache cannot ..." stacked in a list in the Conclusion | The conclusion is read last | Keep the conclusion positive; put scope in the Discussion (pattern 2) |

---

## 6. Checklist for the ScopeCache revision

1. Abstract: no negative sentence; the scope sits in the claim (R1); numbers carry ranges and setups.
2. Threat model: one paragraph containing trust domain, observer, public items, the timing channel with its mitigation and price, and the load boundary. Already present; check that nothing about channels is repeated elsewhere with weaker wording (R6).
3. Guarantees: "Scope of the guarantees" paragraph = domain + the systems it covers + safe path for the rest (R2, R3). Already present; keep it in the Discussion, not in the Conclusion.
4. Every baseline tie or loss (for example PerScope+V on BIRD and ENT) uses fact, mechanism, regime, bound, and points to the sweep that shows where the gap opens (R7).
5. Every "agent calls served from another scope" number is paired with the all-calls number (R8).
6. Synthetic setups: provenance and calibration sentence, released generators, no "may not generalize" (R11). Real ERP grants and the measured event rate are stated in Setup and in the abstract.
7. Overheads: per-call lookup cost against the execution a hit avoids (R13).
8. Soundness: theorem and differential testing in separate sentences; agent-intent correctness named as orthogonal (R14).
9. Future work: at most 2-3 constructive one-sentence extensions (sketches for COUNT DISTINCT, finer latency padding with its own analysis), none phrased as a gap (R20).
10. Final pass: search the source for the phrases in Section 5 (for example: `grep -n -i -E "unfortunately|limitation|may not|cannot guarantee|naive|preliminary|fail" main.tex`) and rewrite each hit with the matching rule.
