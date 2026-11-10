# Data profiling, dependency discovery and join inference: how accepted papers state weaknesses

Read in full on 2026-11-10 for the Certify-Join submission (ICDE 2027 R2): SPIDER (ICDE 2007, author version), SWAN (ICDE 2014), Aurum (ICDE 2018), Ver (ICDE 2023), AutoFeat (ICDE 2024), Auto-BI (PVLDB 2023), BINDER (PVLDB 2015), Lazy discovery (CIDR 2022); 527 concessions catalogued, every quote machine-checked and at most 15 words. Section 4 is the worked mapping for Certify-Join (budgeted join certification) and doubles as an example of mapping a paper's weaknesses to patterns.

Prepared 2026-11-10 for the ICDE 2027 R2 submission "Certify-Join". This is an internal working document, not submission material.

## 0. Scope and method

**Papers read in full.** Eight accepted papers on inclusion and key dependencies, data profiling, join discovery or inference, and dependency maintenance. Each was read as an open-access full text, extracted from its PDF:

| ID | Paper | Venue | Source read |
|---|---|---|---|
| SPIDER | Bauckmann, Leser, Naumann, Tietz, *Efficiently Detecting Inclusion Dependencies* | ICDE 2007 | 10-page author version hosted by HPI (`2007_bauckmann_efficiently.pdf`). The proceedings version is a 3-page short paper (pp. 1448–1450). |
| SWAN | Abedjan, Quiané-Ruiz, Naumann, *Detecting Unique Column Combinations on Dynamic Data* | ICDE 2014 | HPI author copy (12 pp.) |
| AURUM | Castro Fernandez et al., *Aurum: A Data Discovery System* | ICDE 2018 | Author manuscript (12 pp.) |
| VER | Gong, Zhu, Galhotra, Castro Fernandez, *Ver: View Discovery in the Wild* | ICDE 2023 | arXiv 2106.01543, latest version (16 pp. with appendix) |
| AUTOFEAT | Ionescu, Vasilev, Buse, Hai, Katsifodimos, *AutoFeat: Transitive Feature Discovery over Join Paths* | ICDE 2024 | Project-page PDF (13 pp.) |
| AUTOBI | Lin, He, Chaudhuri, *Auto-BI: Automatically Build BI-Models Leveraging Local Join Prediction and Global Schema Graph* | PVLDB 16(10), 2023 | arXiv 2306.12515 (18 pp. with appendix) |
| LAZY | Kossmann, Lindner, Naumann, Papenbrock, *Workload-driven, Lazy Discovery of Data Dependencies for Query Optimization* | CIDR 2022 | CIDR PDF (7 pp.) |
| BINDER | Papenbrock, Kruse, Quiané-Ruiz, Naumann, *Divide & Conquer-based Inclusion Dependency Discovery* | PVLDB 8(7), 2015 | VLDB PDF (12 pp.) |

The optional ICDE 2024–2026 data-validation paper was not added because of the time budget. AUTOFEAT (ICDE 2024) and VER (ICDE 2023) are the most recent ICDE papers in the set.

**What counts as a statement.** Every place where a paper concedes any of the following:
- a limitation;
- a loss or tie against a baseline;
- a weaker regime;
- a heuristic without a guarantee;
- an approximation;
- a simulated or synthetic part of the evaluation;
- a one-off or overhead cost;
- an assumption that restricts scope;
- deferred work.

In total, 527 statements were catalogued, about 60–86 per paper.

**Quotes.** The quotes below (at most 15 words each) were all checked by machine against the extracted text. The checker normalised ligatures and joined words hyphenated across lines. Section numbers follow each paper's own numbering. Page numbers ("p") are PDF page indices of the version read.

**Abbreviations used below:**
- Rhetorical devices: SQ = scope qualifier inside a positive claim; DCR = design choice with a reason.
- Location columns: Abs = abstract; Intro = introduction; Meth = method; Exp = experiments; RW = related work; Concl = conclusion.

---

## 1. Per-paper findings

### 1.1 SPIDER (ICDE 2007)

**Contribution.** A single pass over DBMS-sorted value lists that tests all unary IND candidates in parallel, with extensions to composite and partial INDs.

**Counts (65 statements).** Abs 2 · Intro 8 · Meth 22 · Exp 25 · RW 2 · Concl 6.

**Abstract and conclusion.**
- The abstract contains no self-negation. It only states the cost plainly ("a 21 GB database in ∼4 h") and that the problem is difficult.
- The conclusion contains three negative findings, each turned into a lesson or future work.

| Sec. | Quote (≤15 words) | What it concedes | Device |
|---|---|---|---|
| Abstract | "It uses the efficient sorting facilities of a DBMS" | Depends on the DBMS for sorting | DCR |
| §1 | "can only be verified by a human expert" | An IND is a foreign-key candidate, not a verified foreign key | Semantic-vs-syntactic separation |
| §1.3 | "our algorithm either surpasses those in runtime or makes less assumptions" | Not faster than every competitor | Trade-off framing |
| §2.2 | "this worst case complexity is grossly misleading on average" | Quadratic or worse worst case | Worst case vs typical case |
| §2.2 | "We cannot eliminate this quadratic operations" | Inherent quadratic term | Hardness inherent to the problem |
| §3.2 | "we expect good performance at least on other biological data sources" | Parameter defaults are tuned on one domain | Scope qualifier |
| §4 | "there is just a small difference between the Brute Force and the SPIDER algorithm" | Near-tie on small schemas | Regime analysis |
| §4.2 | "does not save much time for testing" | Own pruning filters are net-negative | Honest negative result |
| §4.3 | "As the SRSW phase dominates the overall time" | The test phase is small; DBMS sorting dominates | Dominated by another cost |
| §8 | "database-external pruning does not speed up the computation" | Own component brings no gain | Negative result turned into a lesson, placed in the conclusion |
| §8 | "which increases the runtime heavily when many IND candidates are satisfied" | Composite IND cost | Regime analysis |
| §8 | "compute the sensitivity and specificity of foreign key detection using gold standards" | No quality evaluation | Concrete future work |

**Other statements.**
- §3.2 is a parameter study that concedes the following:
  - the Bloom filter only rejects and cannot confirm an IND;
  - it costs about 20 MB per 1,000 attributes;
  - longer filter arrays help "only marginally";
  - the optimal setting cannot be found without costly analysis.
- §4 and §4.1 contain fairness notes:
  - competitors were reimplemented;
  - all attributes were given the same data types.
- §5 states that composite INDs were not run on PDB, with a reason.
- §6 tests only one threshold (5%) for partial INDs.

### 1.2 SWAN (ICDE 2014)

**Contribution.** Incremental maintenance of minimal uniques and maximal non-uniques under inserts and deletes. It uses a greedily chosen set of single-column indexes and position-list indexes (PLIs).

**Counts (62 statements).** Abs 1 · Intro 3 · Meth 19 · Exp 37 · RW 0 · Concl 2.

**Abstract and conclusion.**
- The abstract contains only the hedge "up to 1 order of magnitude faster than DUCC".
- The conclusion contains only problem hardness and the qualifier "mainly".
- Caution: the conclusion and the §V-E summary are stronger than the body ("always outperforms"), even though the body reports losses (see §3, practices to avoid).

| Sec. | Quote (≤15 words) | What it concedes | Device |
|---|---|---|---|
| §I | "it is NP-hard in the number of columns and sub-quadratic in the number of rows" | Exponential worst case | Hardness first |
| §I | "an initial dataset is typically several orders of magnitude bigger than the size" | Assumes small increments | Assumption stated up front |
| §III-A | "The sets MUCS and MNUCS can be obtained by any holistic approach" | Needs a one-off full profiling run | One-off cost delegated to an orthogonal method |
| §III-B | "Nevertheless, in the worst case, we have to do a fullscan on the initial dataset" | Worst-case full scan | Worst case stated, used to motivate the design |
| §III-C | "creating such a large number of indexes is expensive (computational- and storage-wise)" | Index cost | DCR (rejected alternative) |
| §III-C | "SWAN follows a greedy approach based on the frequency of columns among minimal uniques" | Greedy index selection with no guarantee (none claimed) | Heuristic labelled as greedy plus an intuition |
| §III-D | "However, choosing more columns to index is not always beneficial." | Index budget trade-off | Trade-off framing |
| §V-A | "We made a best-effort java implementation of GORDIAN" | Baseline was reimplemented | Fairness note |
| §V-B | "the Uniprot dataset has more duplicates resulting into much more index look-ups for SWAN" | Weaker on duplicate-heavy data | Loss explained by the data |
| §V-B | "This time indexing all columns leads to drastic performance boosts." | A naive "Index All" alternative beats SWAN's own selection | Honest loss, scoped to "this specific case" |
| §V-B | "On larger datasets the update could easily be taken offline though." | Index maintenance cost | Amortization (move the cost offline) |
| §V-C | "such a design would lose against a holistic approach" | Incremental method used as a static method should lose | Expectations lowered, then measured |
| §V-C | "SWAN with the 100k sample was slightly slower than DUCC" | Loss | Minimiser plus crossover |
| §V-D | "except for 20% deletes where SWAN is slightly slower than DUCC-INC" | Loss at a high delete ratio | Loss in an "except" clause |
| §V-D | "In practice, one typically finds less than 1% of deletes." | The losing regime is called atypical | "In practice" (uncited, which is a weakness) |
| §V-E | "superior to previous baseline systems in realistic scenarios with up to 5% deleted rows" | Wins only up to 5% deletes | Regime bound written into the positive claim |
| §VII | "SWAN is the first approach to mainly depend on the incremental data size" | Still partly depends on the initial data | One-word qualifier ("mainly") |

**Other statements.**
- §III mentions false positives from partial index coverage twice, each followed by a remedy.
- §V-A says one dataset is synthetic (TPC-H) and gives fairness reasons for shrinking the evaluation to 100k rows and 40 columns.
- §V-B gives honest numbers: about 10 s to update all indexes, and the speed-up falling from 15× to 5×.
- §V-C admits that earlier experiments excluded the initial profiling and index-build cost.

### 1.3 AURUM (ICDE 2018)

**Contribution.** An enterprise knowledge graph of syntactic column relationships:
- built in O(n) with MinHash/HyperLogLog sketches and LSH;
- maintained with the sampling-based RESS change detector;
- queried with SRQL over a G-Index.

**Counts (80 statements).** Abs 1 · Intro 3 · Meth 29 · Exp 41 · RW 4 · Concl 2.

**Abstract and conclusion.**
- The abstract contains no negative. It discloses only that part of the evaluation is deployment experience.
- The conclusion contains one future-work clause and the modest "stepping stone" framing.

| Sec. | Quote (≤15 words) | What it concedes | Device |
|---|---|---|---|
| §I | "finds syntactic relationships such as similarities, PK/FK candidates in O(n)" | Syntactic candidates only, not semantics | SQ (the words "syntactic" and "candidates") |
| §III-A | "configured to balance the probability of false positives and negatives" | LSH errors in both directions | Trade-off framing |
| §III-A | "works well in practice, as shown in the evaluation" | PK/FK heuristic has no guarantee | "In practice", backed by an experiment pointer |
| §III-C | "computed with approximate methods, such as the ones explained above, will contain false positives" | Approximate edges are wrong sometimes | Plain admission plus an immediate remedy (an offline exact check) |
| §IV-A2 | "Semantic ambiguity is a fact of life in data discovery and integration applications." | Results are semantically ambiguous | Ambiguity normalised and handed to the user |
| §IV-A3 | "in theory the provenance graph could be as large as the EKG, in practice" | Worst-case memory | Worst case vs typical case, with a measured figure |
| §V-A3 | "most time is spent during the profiling stage" | One-off profiling dominates | Dominated by another cost |
| §V-B | "we spent time tuning it until we achieved the best results" | Risk of an unfair baseline comparison | Fairness note |
| §V-B | "On the synthetic EKGs, G-Index performs better, but on-par with Virtuoso and Neo4J." | Tie | Regime (real vs synthetic) |
| §V-B | "PostgreSQL is competitive with Neo4J and even with Virtuoso" | A plain baseline is strong | Baseline-strength acknowledgement |
| §V-C1 | "the profiler took only slightly above 1.5 hours to build signatures" | One-off build cost for 250 GB | Honest number |
| §V-C2 | "for DWH and CHEMBL we achieved a precision of around 50%" | Low precision | Honest number, then explained by threshold artefacts |
| §V-C2 | "some of the candidate PK/FKs found by AURUM are in fact semantically reasonable joins" | False positives against the declared schema | Errors reframed as findings (expert-checked) |
| §V-D | "therefore simulating data evolution" | Simulated change | Simulation disclosed, alongside real ChEMBL versions |
| §V-D | "with a maximum error of less than 15%" | Estimation error of the sampling detector | Honest number |
| §VI | "which is orthogonal to the problem we solve" | No lineage support | Orthogonal |
| §VII | "We see AURUM as a stepping stone towards addressing the substantial challenges" | Not a complete solution | Modest framing |

**Other statements.**
- The user survey has N = 4, and users were assisted in a 1.5-hour session.
- The G-Index is not persistent (20 s rebuild) and uses about 200 MB.
- Scale-up data is replicated DWH.
- Some low PK/FK numbers appear only in Fig. 7 and Table III (see §3, practices to avoid).

### 1.4 VER (ICDE 2023)

**Contribution.** Discovery of project-join views over collections with no PK/FK information, from noisy query-by-example input. It contributes 4C view distillation and bandit-based view presentation, and reuses Aurum for indexing.

**Counts (86 statements).** Abs 2 · Intro 8 · Meth 25 · Exp 47 · RW 4 · Concl 0.

**Abstract and conclusion.**
- The abstract contains only scope qualifiers.
- The conclusion contains no negative and no future work.
- Forward-looking lessons sit in Appendix D.

| Sec. | Quote (≤15 words) | What it concedes | Device |
|---|---|---|---|
| §I | "Identifying true join paths automatically is impossible." | No ground truth for join paths | Weakness turned into a property of the problem |
| §I | "a join path implies an inclusion dependency but not the other way around" | The IND proxy over-generates | States which way the proxy errs |
| §I | "Only users know the right context" | Semantics cannot be automated | Semantic-vs-syntactic separation |
| §I | "While challenges 1-3 are addressed by existing work" | Novelty limited to challenges 4–5 | Contribution boundary |
| §II | "Formalizing these requirements is outside the scope of this work." | User intent not formalised | Explicit out-of-scope |
| §V | "In the worst case, it may compare hashes of all pairs of non-compatible views" | Quadratic worst case | Worst case, then a measured typical reduction |
| §VI | "we ignore the schema information to simulate pathless scenario" | The pathless setting is simulated | "Simulate" verb plus purpose (it yields ground truth) |
| §VI-A | "They take 93 seconds (median) when using FASTTOPK." | Ver's median is 101 s, slower than the baseline | Honest number without adjectives |
| §VI-B3 | "Given a contradiction, we do not have an automated way of choosing a view." | No automatic resolution | Plain admission; best and worst bounds reported instead |
| §VI-B3 | "The contradictions in candidate views are mainly due to wrong join paths." | Errors in upstream inference | Loss explained by an upstream component |
| §VI-C1 | "We simulated the user to answer questions correctly." | Oracle user | Simulation disclosed in one sentence |
| §VI-C1 | "Every query runs within 11 minutes" | Minutes-scale latency (about 27K views) | Honest bound plus input size |
| §VI-C2 | "The bottleneck is the MATERIALIZER and the time taken to read views" | I/O dominates | Dominated by another cost |
| §VI-C2 | "73 seconds but it takes less than 0.5 millisecond per question" | One-off initialisation cost | Amortization (one-off vs per-use) |
| §VI-C3 | "When there is no noise in the input query, then all baselines perform well" | Ties with baselines at zero noise | Regime analysis (the advantage needs noise) |
| §VI-D | "employ it as a downstream component to Ver" | The competitor (SQuID) is not beaten head-on | Complementary |
| App. D1 | "investment in better join path discovery algorithms would highly benefit this problem" | Weak upstream inference | Weakness turned into a lesson for the community |

**Other statements.**
- The user study has N = 18 students; 5 of 18 preferred the baseline.
- The noisy workload is generated (150 queries).
- Scale points are random table subsamples.
- Table V shows a 0.96 vs 1.0 hit ratio that is never verbalised.

### 1.5 AUTOFEAT (ICDE 2024)

**Contribution.** Feature discovery over multi-hop join paths, ranked by relevance and redundancy without training a model during the search.

**Counts (60 statements).** Abs 0 · Intro 1 · Meth 22 · Exp 33 · RW 0 · Concl 4 (in the "Future Work" paragraph).

**Abstract and conclusion.**
- The abstract contains no negative, although its "noisy, uncurated data lakes" are simulated.
- The conclusion's future-work paragraph is the only place that admits there is no evaluation on a real organisational data lake.

| Sec. | Quote (≤15 words) | What it concedes | Device |
|---|---|---|---|
| §I | "AutoFeat applies heuristic-based feature selection techniques on the augmented table to prune out" | Heuristic selection | Heuristic named in the introduction |
| §III-B | "relationships discovered by dataset discovery algorithms, which can be spurious" | Noisy input join graph | Assumption stated up front |
| §III-C | "process for feature selection follows an empirical approach" | No theory behind the component choice | Design choice backed by an empirical study |
| §V-C | "In feature selection, relevance is measured using heuristics." | Relevance metric has no guarantee | Heuristic presented as the field's norm |
| §V-D | "JMI achieves the highest accuracy but at the cost of the longest runtime" | The chosen metric is not the most accurate | Trade-off framing |
| §VII-A | "we aim to simulate a data lake scenario where the connections between datasets are unknown" | The data lake is simulated by splitting tables | "Simulate" verb plus purpose |
| §VII-B | "Since the source code was unavailable, we implemented the feature selection part of the system" | Baseline (ARDA) reimplemented | Reproducibility note |
| §VII-C1 | "we expected that MAB would be more effective than the results show" | Baseline result left unexplained | Honest surprise, with no explanation (a risk) |
| §VII-C1 | "Compared to the JoinAll and JoinAll+F baselines, AutoFeat results in similar accuracy" | Tie with exhaustive baselines | Tie reframed as validation |
| §VII-C1 | "with ARDA surpassing on the school dataset" | Loss | Honest concession |
| §VII-C3 | "AutoFeat is an approach best suited to tree-based ML models" | Weaker for other model classes | Regime written into the summary claim |
| §VII-E | "is the most efficient version with minimal accuracy loss" | The default loses some accuracy | Trade-off framing |
| §VIII | "after evaluating our approach on real data lake scenarios within organisations" | No real-lake evaluation | Future work |

**Other statements.**
- §III-B calls the heuristic output "the optimal subset" without proof (see §3, practices to avoid).
- The data-lake gain over MAB is only 2%.
- The τ sensitivity study shows an accuracy drop of up to 4%.
- No complexity bound is given for the traversal.

### 1.6 AUTOBI (PVLDB 2023)

**Contribution.** Join prediction for BI models:
- a calibrated local classifier;
- a global k-MCA / k-MCA-CC optimisation, with k-MCA-CC NP-hard and EXP-APX-complete, solved exactly by branch-and-bound;
- a greedy recall mode for EMS, which is NP-hard and 1/2-inapproximable.

**Counts (70 statements).** Abs 3 · Intro 4 · RW 2 · Meth 25 · Exp 28 · Concl 1 · Appendix 7.

**Abstract and conclusion.**
- The abstract contains a hardness statement, but about the problem, not the method. It is paired with "efficient in practice" and an explicit scale bound.
- The conclusion contains only "improving the end-to-end efficiency" as future work.

| Sec. | Quote (≤15 words) | What it concedes | Device |
|---|---|---|---|
| Abstract | "While we prove k-MCA is intractable and inapproximate in general" | Hardness | Hardness as a contribution, followed by an exact algorithm |
| Abstract | "which is shown to be efficient in practice with sub-second latency" | No polynomial bound | "In practice" |
| Abstract | "can scale to the largest BI-models we encounter (with close to 100 tables)" | Scale shown only up to the observed maximum | Scale bound inside the positive claim |
| §3.2 | "synthetic TPC benchmarks used in prior work that tend to be clean and simple" | Synthetic benchmarks are weak evidence | Synthetic data framed as the easier case |
| §3.3 | "is restricted to equi-joins for now" | Equi-joins only | Scope plus "for now" |
| §4.1 | "we do not regard this as our key contribution in Auto-BI" | The local classifier is not novel | Honest narrowing of novelty |
| §4.2 | "the scores so produced are still heuristic in nature" | Uncalibrated scores | Concede, then fix (calibration) |
| §4.3.2 | "making it inapproximable in polynomial time" | Hardness theorem | Hardness stated plainly |
| §4.3.2 | "we clearly cannot hope Algorithm 3 to solve" | Exponential worst case | Worst case conceded plainly |
| §4.3.2 | "with the max being 11 seconds on a case with 88 data-tables" | Worst observed latency | Mean, median and max reported |
| §4.3.2 | "intractable in theory but reliably solvable in practice" | Same | Analogy to TSP and Knapsack |
| §4.3.3 | "The EMS problem is NP-hard, and is 1/2-inapproximable" | Hardness of the recall mode | Hardness justifies the greedy heuristic |
| §4.3.3 | "We find different solutions have very similar results" | Greedy without a guarantee | Empirically near-optimal instead of a bound |
| §5.1 | "While Auto-BI is not designed for general OLTP databases, we perform the tests nevertheless" | Out-of-design regime | Stress test, then insight |
| §5.2 | "causing data leakage and inflated results" | Validity threat for the GPT baseline | Threat stated against the baseline |
| §5.3 | "Auto-BI works reasonably well on the most challenging slice of the test cases" | F1 drops to 0.79 at 21+ tables | Regime slice (but euphemistic) |
| §5.4 | "Auto-BI is 2-3x slower but the latency is still acceptable" | Slower than the fast variants | Honest ratio plus acceptability |
| §5.4 | "IND-generation is also expensive for all methods, but it is a standard step" | Preprocessing cost | Cost shared by all methods |
| §5.4 | "which we argue is acceptable considering the size of the data" | Runtime above 1 s for more than 40 tables | Runtime normalised by input size |
| §5.5 | "The drop in quality is apparent but not too significant" | Ablation loss | Trade-off framing |
| App. C | "This leads to stronger baselines" | The original baselines were weak, so they were strengthened | Baseline strengthening |

**Other statements.**
- Held-out test cases, the anonymised System-X and semantic-equivalence scoring that is "fair for all methods" are all fairness notes.
- Several ties and losses appear only in Tables 5, 6, 9 and 10 (see §3, practices to avoid).

### 1.7 LAZY (CIDR 2022)

**Contribution.** A vision paper. Dependency candidates are mined from the plan cache, validated in Hyrise and used by three rewrites, giving 27% lower execution time on JOB.

**Counts (64 statements).** Abs 3 · Intro 2 · Meth 26 · Exp 28 · RW 1 · Concl 4.

**Abstract and conclusion.**
- The abstract contains only scope words: "vision", "feasibility", "potential", "prototypical", "exemplary".
- The conclusion states the worst overhead ratio plainly (up to 1.3× of the saving).

| Sec. | Quote (≤15 words) | What it concedes | Device |
|---|---|---|---|
| Abstract | "This paper presents our vision of a workload-driven, lazy dependency discovery system" | Prototype status | Scope by genre |
| §3.1 | "not considering all possible attribute combinations as potential data dependency candidates" | Incomplete by design | DCR |
| §3.1 | "it depends on the user-defined rules whether or not the dependency selection promotes useful dependencies" | No usefulness guarantee | Plain admission |
| §3.2 | "inefficient query plans and, in the worst case, faulty results" | Invalid dependencies can give wrong answers | Risk stated explicitly |
| §3.2 | "we propose the use of efficient incremental validation and maintenance approaches that exist for FDs" | Maintenance not implemented | Orthogonal (delegated to prior work) |
| §4.1 | "no (foreign) keys or constraints are defined for the benchmarks" | Simulated "no constraints" setting ("To simulate a scenario") | Simulation disclosed |
| §4.2 | "the observed performance benefits do not represent a formal verification of our approach" | Empirical evidence only | Explicit disclaimer of a guarantee |
| §4.2 | "the number of improved queries clearly outweighs the degraded ones" | Some queries get slower | Net-effect framing |
| §4.2 | "the star schema-like data model of the TPC-DS and JOB is more suitable" | Weaker on TPC-H | Regime explained by schema shape |
| §4.3 | "Using dependencies for query optimization introduces a tradeoff" | Discovery overhead | Trade-off framing |
| §4.3 | "For the TPC-H, all queries must be executed more than once." | Break-even needs more than one run | Honest break-even |
| §4.3 | "the candidate generation consumed never more than 10 % of the total dependency discovery time" | Validation dominates the cost | Cost decomposition |
| §4.3 | "the effort for dependency discovery is usually amortized quickly in most scenarios" | Not always amortized | Amortization (hedged) |
| §4.3 | "it can be executed as asynchronous background task whose runtime is significantly less relevant" | Overhead exists | Cost decoupled from the critical path |
| §6 | "between 0.05 × and 1.3 × of the observed execution time reduction" | Overhead can exceed one run's saving | Honest range in the conclusion |

### 1.8 BINDER (PVLDB 2015)

**Contribution.** Hash-partitioned, divide-and-conquer discovery of unary and n-ary INDs, with lazy partition refinement. Up to 26× faster than SPIDER.

**Counts (80 statements).** Abs 1 · Intro 3 · Meth 26 · Exp 44 · RW 3 · Concl 3.

**Abstract and conclusion.**
- The abstract contains only the hedge "up to".
- The conclusion contains two limitations (I/O-bound; result size exponential), each phrased as the motivation for future work.
- Caution: the conclusion drops "up to" and omits the losses (see §3, practices to avoid).

| Sec. | Quote (≤15 words) | What it concedes | Device |
|---|---|---|---|
| Abstract | "Binder is up to 26x faster than Spider and more than 2500x faster than Mind" | Non-uniform speed-up | "Up to" |
| §2 | "in terms of performance, the preprocessing step is negligible" | Preprocessing cost | Dominated by another cost; every system pays it |
| §2 | "an entire partition needs to fit in main memory" | Memory assumption | Assumption stated up front, with a remedy |
| §3.3 | "unfortunately, this does not indicate an optimal checking order" | Ordering heuristic is uninformative | "Unfortunately" used only for a heuristic detail |
| §4.3 | "the bucketing process dominates the entire IND discovery process by taking up 95%" | I/O-bound | Cost decomposition |
| §6.1 | "which to date is the fastest algorithm for unary INDs discovery" | Strong baseline | Baseline-strength acknowledgement |
| §6.1 | "we reduce the server's memory to 8 GB" | Simulated low-memory setting | Simulation with a purpose |
| §6.2 | "Binder performs worse on database inputs than on file inputs" | Slower on database inputs | Loss explained by DBMS overhead |
| §6.2 | "Spider, on the other hand, profits from a database" | The competitor has an advantage | Baseline-strength, then "Despite these advantages" |
| §6.4 | "Binder is slower than Spider if the datasets are very small" | Loss regime | Regime analysis |
| §6.4 | "Spider has an advantage over Binder if the input dataset contains many duplicate values" | Loss regime | Regime analysis |
| §6.4 | "Binder could simply keep its buckets in main memory" | Fix not implemented | Easy-fix sentence |
| §6.5 | "Thus, this approach would be clearly faster than the original Spider algorithm" | Part of the gain comes from bucketing alone | Pre-empting an objection, then an ablation |
| §6.6 | "which is the default in practice" | The losing regime is atypical | "In practice" |
| §6.6 | "but also exceeds seven days for PDB and PLISTA" | Fails to finish on two datasets | Honest statement, then explained by the data |
| §6.6 | "we tried different validation queries based on LEFT OUTER JOIN, NOT IN, and EXCEPT statements" | Baseline might be under-tuned | Fairness note |
| §7 | "In general, this is an orthogonal task" | No foreign-key selection | Orthogonal |
| §8 | "because the result sizes can grow exponentially with the number of attributes" | Output explosion | Limitation as the motivation for future work |

### 1.9 Cross-paper statistics

| Paper | Abs | Intro | Meth | Exp | RW | Concl | Total | Negative in abstract? | Negative in conclusion? |
|---|---|---|---|---|---|---|---|---|---|
| SPIDER | 2 | 8 | 22 | 25 | 2 | 6 | 65 | No (honest cost only) | Yes (negative findings recast as lessons) |
| SWAN | 1 | 3 | 19 | 37 | 0 | 2 | 62 | No ("up to") | No (hardness, "mainly") |
| AURUM | 1 | 3 | 29 | 41 | 4 | 2 | 80 | No | Future work only |
| VER | 2 | 8 | 25 | 47 | 4 | 0 | 86 | No | No |
| AUTOFEAT | 0 | 1 | 22 | 33 | 0 | 4 | 60 | No | Future-work paragraph |
| AUTOBI | 3 | 4 | 25 | 28 | 2 | 1 | 70 (+7 App.)* | Problem hardness only | Future work only |
| LAZY | 3 | 2 | 26 | 28 | 1 | 4 | 64 | No (scope words) | Overhead range stated |
| BINDER | 1 | 3 | 26 | 44 | 3 | 3 | 80 | No ("up to") | Yes (as future-work motivation) |

\* AUTOBI's appendix statements (7) are not in the location columns or the total. The other papers' appendix statements are already inside their Meth/Exp counts.

**Summary of the counts:**
- About 90% of concessions sit in the method and experiment sections.
- No abstract contains a negative statement about the authors' own method.
- Words used across the 8 papers:
  - The word "limitation" is never applied to the authors' own method; it appears 3 times, always about a baseline.
  - "Unfortunately" appears 4 times. It is used only about a rejected design alternative, a heuristic detail or a baseline, never about a headline result.
  - "Threats to validity" never appears.

---

## 2. Writing patterns (15)

Each pattern lists the papers that use it, an example and how to apply it.

**P1. Hardness first, then say what the algorithm does and does not guarantee.**
- Used by: AUTOBI, SWAN, BINDER, SPIDER.
- How it works: state the hardness result as a contribution. Then say plainly whether the algorithm is exact or heuristic. For a heuristic, give empirical closeness instead of a bound.
- Example (AUTOBI): "The EMS problem is NP-hard, and is 1/2-inapproximable", followed by "We find different solutions have very similar results".
- Example (SWAN): "SWAN follows a greedy approach based on the frequency of columns ...", with no guarantee claimed.

**P2. Worst case vs typical case, with a measured number.**
- Used by: SPIDER ("grossly misleading on average"), AURUM ("in theory ... in practice"), VER (worst case, then median reduction), AUTOBI (mean/median/max: "with the max being 11 seconds ...").
- How it works: the worst case is always stated first and never hidden. The typical case is then backed by a distribution (median and max), not an adjective.

**P3. Regime analysis: say exactly when the baseline wins, inside the experiments.**
- Used by: BINDER ("Binder is slower than Spider if the datasets are very small"), SWAN ("except for 20% deletes ..."), VER ("When there is no noise ... all baselines perform well"), AUTOFEAT ("best suited to tree-based ML models"), LAZY ("star schema-like ... more suitable").

**P4. Explain the loss by a mechanism in the data or setting, in the next sentence.**
- Used by: SWAN (Uniprot duplicates), BINDER (file-creation overhead; almost-duplicate tables), VER ("mainly due to wrong join paths"), AUTOFEAT (star-shaped schema), SPIDER (SRSW phase).
- How it works: no loss is left without a "because".

**P5. Acknowledge the baseline's strength and document fairness.**
- Used by: BINDER ("which to date is the fastest ..."; "Spider, on the other hand, profits from a database"; three SQL formulations tried for MIND), AUTOBI ("This leads to stronger baselines"; same training data for ML-FK), SWAN ("best-effort ... GORDIAN"), AURUM ("we spent time tuning it ...").
- Effect: a conceded advantage makes the remaining wins harder to dispute.

**P6. Write the regime bound into the positive claim itself.**
- Used by: SWAN ("superior ... in realistic scenarios with up to 5% deleted rows"; "mainly depend on"), AUTOBI ("the largest BI-models we encounter (with close to 100 tables)"), BINDER ("up to 26x"), AURUM ("syntactic ... PK/FK candidates").
- How it works: this is how a limitation reaches the abstract without being a negative sentence.

**P7. Decompose the cost so the conceded cost sits next to a dominant or shared cost.**
- Used by: SPIDER ("As the SRSW phase dominates ..."), BINDER ("bucketing ... 95%"), LAZY ("candidate generation ... never more than 10 %"), VER ("The bottleneck is the MATERIALIZER ..."), AUTOBI ("IND-generation is also expensive for all methods, but it is a standard step").

**P8. One-off cost: amortization, break-even and off-critical-path, each with a number.**
- Used by: LAZY ("between 0.05 × and 1.3 × ..."; "all queries must be executed more than once"; "asynchronous background task"), VER ("73 seconds ... less than 0.5 millisecond per question"), SWAN ("could easily be taken offline"), AURUM ("only slightly above 1.5 hours ..."), BINDER ("every IND detection system requires such a preprocessing phase").

**P9. Design choice with a reason, naming the rejected alternative.**
- Used by: SWAN (indexing everything "is expensive"), LAZY ("not considering all possible attribute combinations ..."), BINDER (statistics "more expensive than their pruning effect"), AUTOFEAT (left joins only), AURUM (value-level granularity rejected).
- Effect: the scope restriction reads as an engineering decision, not an omission.

**P10. Separate syntactic or structural correctness from semantic correctness, and hand semantics to a human or a downstream step.**
- Used by: SPIDER ("can only be verified by a human expert"), AURUM ("Semantic ambiguity is a fact of life ..."), VER ("Only users know the right context"), LAZY ("in the worst case, faulty results").

**P11. Name the proxy and the direction of its error, then give the remedy.**
- Used by: VER ("a join path implies an inclusion dependency but not the other way around"), AURUM ("will contain false positives", then an offline exact check), AUTOBI ("still heuristic in nature", then calibration), SWAN (partial-duplicate false positives, then verification).

**P12. Disclose simulated parts in the setup with the verb "simulate", a purpose and a real-data anchor.**
- Used by:
  - VER: "to simulate pathless scenario"; "We simulated the user to answer questions correctly."
  - AURUM: "therefore simulating data evolution", plus a real ChEMBL version swap.
  - AUTOFEAT: "we aim to simulate a data lake scenario ...".
  - LAZY: "To simulate a scenario"; "no (foreign) keys ...".
  - BINDER: "we reduce the server's memory to 8 GB".
- How it works: one sentence, no apology. The purpose is usually ground truth or control.

**P13. Turn a negative or neutral result into a finding or lesson, and report it, even in the conclusion.**
- Used by: SPIDER (pruning "does not speed up the computation", explained and placed in the conclusion), VER App. D1 ("investment in better join path discovery ..."), AUTOBI (OLTP: "somewhat surprising"), AURUM (false positives as "semantically reasonable joins"), LAZY (valuable dependencies are cheap to validate).

**P14. Orthogonal or complementary, plus narrow, concrete future work (1–3 items, never a list of wishes).**
- Used by: BINDER ("In general, this is an orthogonal task"), AURUM ("which is orthogonal to the problem we solve"), VER ("outside the scope of this work"; competitor as "downstream component"), AUTOBI ("restricted to equi-joins for now"), LAZY (maintenance delegated to existing FD techniques), SPIDER (gold-standard sensitivity and specificity).

**P15. State honest numbers plainly, without evaluative adjectives, including small losses.**
- Used by: VER ("They take 93 seconds (median) when using FASTTOPK."), AURUM ("precision of around 50%"; "maximum error of less than 15%"), BINDER ("In fact, its execution time almost doubles."), AUTOBI ("2-3x slower but the latency is still acceptable"), LAZY ("0.05 × and 1.3 ×").

---

## 3. Anti-patterns and practices to avoid

### 3.1 Things none of the eight papers do

1. **No abstract states a negative about the authors' own method.**
   - Abstracts carry only scope bounds (P6), genre words ("vision"), honest cost figures or problem hardness (AUTOBI).
2. **No paper has a section titled "Limitations" or "Threats to validity".**
   - Concessions are distributed: method about 40%, experiments about 50%.
   - This describes how these papers are written, not a rule. Recent ICDE EAB papers do use such sections.
3. **No paper calls its own result a "failure".**
   - "Unfortunately" and "limitation" are never applied to a headline result of the authors' own method.
4. **No paper claims an approximation or performance guarantee it does not prove.**
   - Heuristics are labelled "heuristic", "greedy" or "empirical".
   - LAZY explicitly says its results "do not represent a formal verification".
   - The one exception is AUTOFEAT's unproved "optimal subset" wording, listed in §3.2 below.
5. **No paper reports a loss in the text without a regime or a cause.** (Losses that appear only in tables are a separate problem; see §3.2.)
6. **No paper apologises for a simulation or hides one.** Each discloses it once, in the setup.
7. **No paper defers more than two or three concrete items to future work, and none turns future work into a list of missing features.**
8. **No paper compares against an unattainable oracle and calls the gap a weakness.** Where optimal solutions are discussed (AUTOBI), the exact optimum is part of the method, not a rival. This item is inferred by us; see the mapping for W2.
9. **No paper puts a self-undermining sentence where the claim is made.** Concessions appear where the evidence is, not next to the claim.

### 3.2 Things some of them do, which we should not copy

These are reviewer-risk items for a 2027 submission.
- **Conclusion stronger than the body.** SWAN ("always outperforms") and BINDER (drops "up to", omits the 7-day timeouts). Our conclusion must keep the same qualifiers as the experiments.
- **Losses left only in tables or figures.**
  - AUTOBI: Tables 5, 6, 9 and 10.
  - AURUM: Fig. 7 (35% precision on ChEMBL), and DWH recall at K=128 in Table III.
  - VER: the hit ratio of 0.96 vs 1.0 in Table V.
  - Our numbers 5.3 and 34 must each be stated in the prose.
- **Inconsistent numbers across sections.**
  - VER: 17.5% vs 18%.
  - AUTOBI: 10K+ vs 100K+ models.
  - AUTOBI: the abstract says "k-MCA is intractable", while the theorem shows only k-MCA-CC is.
- **"In practice" claims with no citation.** SWAN: "less than 1% of deletes". Every "in practice" needs a measurement or a citation.
- **Unexplained baseline results.** AUTOFEAT: MAB "more effective than the results show".
- **Unproved "optimal" wording for a heuristic output.** AUTOFEAT §III-B.

---

## 4. Mapping: our weaknesses → patterns

The model sentences below show register only. Numbers are those given in the brief; check them against the paper before use.

**W1. Greedy bundle rule; no approximation guarantee (NP-hard, no PTAS).**
- Patterns: P1, P9, P2, P15.
- Precedents: AUTOBI (EMS 1/2-inapproximable, then greedy, then "very similar results"); SWAN (greedy index choice, no bound claimed).
- Model: *"Budgeted certification is NP-hard and admits no PTAS (Thm. X); we therefore use a greedy bundle rule, which carries no approximation guarantee. Section Y measures its distance to an exact ILP."*
- Never write "near-optimal" without the measured gap.

**W2. Average coverage gap of 5.3 points to a clairvoyant ILP; 34 points in one small TPC-H cell, where a naive baseline also reaches 100%.**
- Patterns: P3, P4, P5, P6, P15. Also avoid the §3.2 practices "losses left only in tables" and "conclusion stronger than the body".
- Steps:
  - Call the ILP an upper bound that sees the probe outcomes in advance, not a deployable baseline. This is our inference, consistent with P5/P8 wording.
  - Give the average and the worst cell in the prose.
  - Explain the cell by its mechanism, as in BINDER's small-dataset loss: a small instance, coarse budget granularity, a budget large enough that even naive ordering covers everything.
  - State that the naive baseline also reaches 100% there, as a regime fact, as in VER's "all baselines perform well" at zero noise.
- Model: *"Averaged over all cells, the greedy rule is 5.3 points below the clairvoyant ILP bound. The largest gap (34 points) occurs on the smallest TPC-H cell, where the budget suffices for naive ordering to certify every edge."*

**W3. Inference rules and probe ordering do not change coverage on star or snowflake benchmarks.**
- Patterns: P13, P3, P4.
- Precedents: SPIDER (its own pruning "does not speed up the computation", explained, and reported in the conclusion as a finding); BINDER ("pruning capabilities ... have no effect for the LOD and PDB datasets", explained by the data); LAZY (schema shape decides benefit).
- Write it as a finding with a mechanism: on star or snowflake schemas every edge touches the fact table, so the rules have nothing to derive. Then give the regime where they help, or the cost they add (none, or X).

**W4. Under a shared-scan cost model, exact one-pass profiling reads fewer rows than our exact method; our advantage there comes only from sampling.**
- Patterns: P5, P6, P7, P3.
- Precedent: BINDER ("Spider, on the other hand, profits from a database ... Despite these advantages ...").
- Model: *"Under a shared-scan cost model, exact one-pass profiling (SPIDER/BINDER-style) reads fewer rows than exact certification; in that model our advantage comes from sampled certificates."*
- Put this in the experiments, with the row counts. Scope the abstract claim to the cost model it holds under (P6).

**W5. Certificates guarantee cardinality safety, not semantic correctness.**
- Patterns: P10, P11, P6.
- Precedents: SPIDER ("can only be verified by a human expert"), VER (proxy direction; "Only users know the right context"), AURUM ("PK/FK candidates"), LAZY ("in the worst case, faulty results").
- How to apply:
  - Define the guarantee precisely, with the word "cardinality" in the claim.
  - State the direction of the error: a certified edge can still be semantically wrong.
  - Name who resolves it: the LLM prior or a human.

**W6. Sampled-probe outcomes in the budget experiments are simulated from exact detection probabilities; real samples appear only in the calibration study.**
- Patterns: P12, P15.
- Precedents: VER ("We simulated the user to answer questions correctly."), AURUM (simulated change plus a real ChEMBL version), BINDER (8 GB memory cap), AUTOFEAT.
- How to apply: one sentence in the setup, using the verb "simulate". Then:
  - give the purpose: label once and replay many times, with a controlled variance;
  - give the real-data anchor: the calibration study and its measured agreement.
- Do not repeat the caveat in later sections.

**W7. The sampled certificate is per atom; the tree-level bound needs fact-row sampling.**
- Patterns: P6, P9, P14.
- Precedents: SWAN ("mainly"), AUTOBI ("restricted to equi-joins for now"), LAZY (delegating to existing techniques).
- How to apply:
  - Write "per-atom" into the theorem and the claim.
  - Present fact-row sampling as the stated condition for the tree-level bound: a design choice with a reason.
  - Do not present it as a gap.

**W8. Incremental maintenance needs a one-off build costing about one full verification.**
- Patterns: P8, P7.
- Precedents: LAZY (break-even "more than once"; 0.05–1.3×), VER (73 s once vs 0.5 ms each), SWAN (offline), BINDER (every system pays preprocessing).
- Model: *"Maintenance requires a one-off build costing about one full verification; it breaks even after the first update batch and runs off the query path."*
- Give the break-even point as a number.

**W9. Planning time grows with workload size (36 min for 26k queries over 10k tables).**
- Patterns: P2, P7, P8, P15.
- Precedents: AUTOBI ("acceptable considering the size of the data"; max 11 s at 88 tables), VER ("Every query runs within 11 minutes"), AURUM ("1.5 hours" for 250 GB).
- How to apply:
  - Report the median and the maximum, normalised per query or per table.
  - Say that planning runs offline or once per workload.
  - Give the dominant sub-cost.

**W10. Under a weaker LLM prior (GLM), 18–26% of results have semantic errors.**
- Patterns: P10, P3, P13, P15.
- Precedents: VER App. D1 (index quality treated as a regime: "spurious join paths"; "investment in better join path discovery ..."), AURUM ("around 50%" precision, then explained), AUTOBI (variants as a trade-off).
- How to apply:
  - Report it as prior-quality regime analysis.
  - Note that cardinality safety is unaffected.
  - Draw the lesson: certification quality tracks the semantic prior.

**W11. Route-equivalence certification is left to future work.**
- Pattern: P14.
- Precedents: AUTOBI ("for now"; "which we will leave as future work"), BINDER ("orthogonal task"), VER ("outside the scope of this work").
- How to apply: one concrete sentence in the conclusion, at most two future-work items in total.

### 4.1 Placement summary

Taken from the counts in §1.9.

| Location | What goes there |
|---|---|
| Abstract | Only scope-bounded positives: per-atom; cardinality safety; the cost model; tested scale |
| Introduction | Problem hardness (W1) and the guarantee's scope (W5, W7) |
| Method | W1, W5, W7, W8, each as a design choice with a reason |
| Experiments | W2, W3, W4, W6, W9, W10, as regimes with numbers and causes |
| Conclusion | One W3-style finding and W11 as future work; the same qualifiers as the body |

---

## Sources

- SPIDER: https://hpi.de/oldsite/fileadmin/user_upload/fachgebiete/naumann/publications/PDFs/2007_bauckmann_efficiently.pdf
- SWAN: https://hpi.de/oldsite/fileadmin/user_upload/fachgebiete/naumann/publications/PDFs/2014_abedjan_detecting.pdf
- AURUM: https://rutgers-db.github.io/cs541-fall19/paper/discovery-1.pdf (author manuscript; also https://dspace.mit.edu/handle/1721.1/137860)
- VER: https://arxiv.org/abs/2106.01543
- AUTOFEAT: https://delftdata.github.io/autofeat/assets/papers/ICDE_FeatureDiscovery.pdf
- AUTOBI: https://arxiv.org/abs/2306.12515
- LAZY: https://mail.vldb.org/cidrdb/papers/2022/p70-kossmann.pdf
- BINDER: https://www.vldb.org/pvldb/vol8/p774-papenbrock.pdf
