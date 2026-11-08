# Stating limitations in reachability-index, IVM and access-control papers (ICDE / PVLDB / SIGMOD practice)

Fourth corpus for `limitations-writing.md` (cohesive subgraphs), `limitations-writing-eab.md` (benchmarks) and
`limitations-writing-aqp.md` (AQP / LLM queries): accepted papers on (dynamic) reachability indexing, 2-hop
labeling and its maintenance, label-constrained reachability, transitive closure, incremental view maintenance
and database access-control enforcement. Eleven accepted papers were read on 2026-11-08 from open full text
(abstract, introduction, model/assumption paragraphs, full experimental section, related work, conclusion);
one non-DB paper is used only as background evidence. Every quote was checked against the extracted text and
is under 15 words; at most one quote per paper. Counts are observations from these papers, not venue rules.

Target paper used for all before/after examples: *No Stale Allows: Maintaining Effective Permissions over
Dynamic Authorization Graphs with Conditions and Deny* (FLIX + polarity-aware deferral, ICDE 2027 R2).
Its weak spots are labelled (a)-(g) throughout:
(a) shallow graphs: online BFS is as fast or faster (ERP graph, closure about 5 subjects, FLIX at 0.85x the speed
    of BFS; 0.64-1.94x on the eight shallow graphs, slower on 2 of 8); FLIX wins on deep nesting (41x on DEEP-16);
(b) the reverse `who` query is 1.38-3.20x slower than one reverse search;
(c) deny edges and conditions are synthetic on most public graphs (real only on the ERP graph);
(d) baselines other than BFS are reimplementations;
(e) the model omits intersection and tuple-to-userset rewrites;
(f) the safe deferral rule causes false denies (1.8% of checks in the main runs, 4.6% on the ERP graph);
(g) no concurrency, no general Datalog/IVM engine benchmarked.

**Integrity boundary (same as the other guides).** Change placement, frequency, framing and wording only:
every measured number stays in the tables, every losing cell is named once in the text, no claim becomes
false, no competitor is hidden. In this area reviewers can rerun BFS in an afternoon, so a sentence that
contradicts a table (see the P2H+ conclusion in Section 1) is the fastest way to lose a reviewer.

## Quick rules (details and evidence below)
1. Put the regime in the positive claim (title, abstract, contribution) instead of a separate negative
   sentence: "on deeply nested graphs", "small-world", "at most k labels" (4/11 qualify the claim; 0/11 state a
   loss in the abstract).
2. Treat "simple traversal is strong on easy instances" as a known, citable finding, not a confession; one
   accepted ICDE paper states it as its own finding in the introduction (IFCA).
3. Every losing cell gets its cause in the same or next sentence (7/8 papers with losses), using a measured
   property of the instance: tree-shaped input, inverted-index overhead, no index to prune, relaxed structure.
4. Turn a latency loss into a workload crossover: queries per update, break-even workload size, number of
   policies at which a component pays off (5/11 quantify a crossover).
5. Pair a loss on one metric with the metric the design targets, using "trade-off" or "at the cost of"
   (6/8 papers with losses).
6. Synthetic labels / updates / policies: one or two sentences in the setup, a tick column in the dataset table,
   a precedent citation; never an apology (8/11 use synthetic labels, updates or policies; 0/8 apologise).
7. Baselines: state provenance plus the fairness control (same runtime, same store, single thread); 0/11 write a
   sentence suggesting their own baseline code may be weak.
8. Model restrictions are definitions, assumptions or reductions in the preliminaries, with a precedent or an
   extension pointer (6/11); never "we do not support X" in the abstract or introduction.
9. "Limitation(s)", "drawback", "weakness" describe prior work or your own basic variant that motivates the
   next component; 0/11 apply them to the final method, 0/11 have a Limitations or Threats heading.
10. Conclusion: restate the scoped claim, then at most two future-work sentences framed as extensions
    (6/11 have them: external memory, parallelism, constrained queries, road networks, optimizer integration,
    new tasks). 0/11 list losing cases in the conclusion.

---

## 0. Corpus and how it was read

| ID | Paper (short name) | Venue + year [verification] | Full text actually read | Topic |
|---|---|---|---|---|
| P1 | Reachability Queries on Large Dynamic Graphs: A Total Order Approach (**TOL**, Zhu, Lin, Wang, Xiao) | SIGMOD 2014 [V: SIGMOD'14 copyright block in PDF; DOI 10.1145/2588555.2612181] | https://edwlin.github.io/pubs/sigmod2014-tol.pdf (author-hosted) | dynamic 2-hop reachability labels |
| P2 | Answering Billion-Scale Label-Constrained Reachability Queries within Microsecond (**P2H+**, Peng et al.) | PVLDB 13(6), 2020 [V: reference line in PDF] | https://www.vldb.org/pvldb/vol13/p812-peng.pdf | static LCR 2-hop index |
| P3 | DLCR: Efficient Indexing for Label-Constrained Reachability Queries on Large Dynamic Graphs (**DLCR**, Chen, Peng, Wang, Yu) | PVLDB 15(8), 2022 [V: reference line in PDF] | https://www.vldb.org/pvldb/vol15/p1645-chen.pdf | dynamic LCR 2-hop index |
| P4 | IFCA: Index-Free Community-Aware Reachability Processing Over Large Dynamic Graphs (**IFCA**, Pang, Zou, Liu) | ICDE 2023 [V-partial: DOI 10.1109/icde55515.2023.00172 from the project's Crossref-checked reference table; PDF is the authors' lab copy, camera-ready identity not verified] | https://mod.wict.pku.edu.cn/docs/20230620091531176236.pdf | index-free dynamic reachability vs. TOL/IP/DAGGER |
| P5 | A Reachability Index for Recursive Label-Concatenated Graph Queries (**RLC**, Zhang, Bonifati et al.) | ICDE 2023 [V-partial: DOI 10.1109/icde55515.2023.00013 from the project's reference table; arXiv text read] | https://arxiv.org/pdf/2203.08606 | static RLC reachability index, vs. graph engines |
| P6 | HL-index: Fast Reachability Query in Hypergraphs (**HL-index**, Xie et al.) | ICDE 2026 [V-partial: DOI 10.1109/icde65706.2026.00090 from the project's reference table; arXiv text carries the ICDE-style AI-content acknowledgment] | https://arxiv.org/pdf/2512.23345 (v1) | static hypergraph reachability labels |
| P7 | BatchHL: Answering Distance Queries on Batch-Dynamic Networks at Scale (**BatchHL**, Farhan, Wang, Koehler) | SIGMOD 2022 [V: ACM reference format in arXiv text; DOI 10.1145/3514221.3517883] | https://arxiv.org/pdf/2204.11012 | batch-dynamic 2-hop / highway labelling maintenance |
| P8 | Efficient Maintenance of 2-Hop Labeling Index on Dynamic Small-World Graphs (**M2HL**, Zeng, Fang et al.) | PVLDB 18(7), 2025 [V: reference line in PDF] | https://www.vldb.org/pvldb/vol18/p2005-zeng.pdf | parallel 2-hop label maintenance |
| P9 | Sieve: A Middleware Approach to Scalable Access Control for Database Management Systems (**Sieve**, Pappachan, Yus, Mehrotra, Freytag) | PVLDB 13(12), 2020, pp. 2424-2437 [V: Crossref record of DOI 10.14778/3407790.3407835 gives volume 13, issue 12; the PDF header was read as No. 11 by the reader, Crossref is authoritative] | https://www.vldb.org/pvldb/vol13/p2424-pappachan.pdf | fine-grained access-control enforcement in a DBMS |
| P10 | DBSP: Automatic Incremental View Maintenance for Rich Query Languages (**DBSP**, Budiu et al.) | PVLDB 16(7), 2023 [V: reference line in PDF] | https://www.vldb.org/pvldb/vol16/p1601-budiu.pdf | general IVM incl. recursive Datalog / transitive closure |
| P11 | Incremental View Maintenance with Triple Lock Factorization Benefits (**F-IVM**, Nikolic, Olteanu) | SIGMOD 2018 [V-partial: a footnote of arXiv v2 states that a short version appeared at SIGMOD 2018; the SIGMOD text itself was **not** read] | https://arxiv.org/pdf/1703.07484 (v2, full version) | higher-order factorized IVM |

Background only, outside the counts:
- **Hanauer, Henzinger, Schulz**, Faster Fully Dynamic Transitive Closure in Practice, SEA 2020 (algorithm
  engineering, not a DB venue). Read at https://arxiv.org/pdf/2002.00813. Used because it documents that
  plain BFS/DFS was competitive with dynamic TC algorithms in earlier studies, except on dense random graphs or
  very query-heavy mixes; its own new algorithms beat BFS/DFS by orders of magnitude.

Candidates not read **[NR]**:
- **Valstar, Fletcher, Yoshida**, Landmark indexing for LCR, SIGMOD 2017: no open full text found (ACM DL only;
  slides and code exist). Not counted.
- **Wang et al.**, Lightweight 2-Hop Labels for Reachability Queries on Large-Scale Graphs, ICDE 2026: only a
  faculty-page listing found, no open text. Not counted.
- **O'Reach** (Hanauer et al.), D'Angelo et al. fully dynamic 2-hop cover, Akiba et al. dynamic PLL: not DB
  venues or not attempted; replaced by BatchHL (SIGMOD 2022) and M2HL (PVLDB 2025).
- **Data Guard** (ICDE 2026, purpose-based access control) and **Zhou et al.** dynamic distance labelling
  (ICDE 2024): no open full text checked.
- The arXiv API was rate-limited during this session, so no systematic arXiv sweep for further ICDE 2024-2026
  reachability papers was possible.

---

## 1. Per-paper notes

Format per paper: where each weakness appears (A = abstract, I = introduction, M = model/method, E =
experiments, C = conclusion), length in sentences, vocabulary, mechanism yes/no, losing cells in tables
yes/no, and how the paper handles the seven questions of the brief (small/shallow regime, slower query type,
synthetic data, reimplemented baselines, unsupported features, future work).

### P1 TOL (SIGMOD 2014), dynamic 2-hop reachability
- **A/I.** Gains only. The scope is folded into the claim: the update algorithms handle vertex insertions and
  deletions. The introduction uses BFS as a yardstick against a *competitor*: it says Dagger's queries are
  hardly better than a plain BFS. The method's own weak regimes are not mentioned in A or I.
- **M.** DAG restriction stated as an assumption with precedent, twice, one sentence each (SCCs are contracted,
  as in existing work; updated graphs are assumed to stay acyclic, following two cited papers).
- **E, losses (2 units, 1-2 sentences each).** (i) Insertion: Dagger is considerably faster on three uniprot
  graphs; the next clause gives the mechanism (those graphs are trees, and Dagger is efficient on trees).
  (ii) Deletion: described as generally comparable to Dagger, with the two exceptions (RG40, wiki) named,
  followed by one trade-off sentence.
  Losing cells stay in Figs. 2 and 4.
- **E, BFS baseline.** A bidirectional BFS is included in the query figure, and the text notes that BFS has zero
  update cost; this is used to argue that Dagger is not worth its update cost, i.e. BFS is the bar every index
  must clear, stated openly.
- **Synthetic.** Four synthetic DAGs generated with the generator of an earlier paper (cited); updates are 10^4 random vertex
  deletions followed by re-insertions. Stated as protocol, no hedging.
- **Baselines.** Authors' C++ code for all competitors.
- **C.** Restates gains; one future-work sentence (graphs that do not fit in memory).
- Quote: "slightly inferior performance of BU on deletion is justified by its superior efficiency".

### P2 P2H+ (PVLDB 2020), static label-constrained 2-hop index
- **A.** Gains only (up to five orders of magnitude, microsecond queries on billion-scale graphs).
- **M.** The known weakness (index growth with many labels) gets its own subsection, *Dealing With Large Number of
  Labels*: one sentence concedes that the basic technique cannot be applied directly, and the rest of the
  subsection is an extension (primary/secondary index on frequent labels). A limitation is turned into a feature.
- **Synthetic.** The dataset table has a "Synthetic Labels" tick column (15 of 22 graphs ticked); one sentence
  in the setup says unlabelled graphs get labels generated as for the synthetic data, following the
  baseline's paper.
- **Baselines.** LI+ code and query generator provided by its authors (acknowledged in the text).
- **E, losses.** Index time and size: better than LI+ on most datasets, with the exceptions named in the same
  sentence (ZH, CT, AX for indexing time; YT for index size). The next sentence pivots to the metric the design targets (queries are one or two orders faster on
  those datasets). No mechanism is given; the counter-metric replaces it.
- **C, counter-example.** The conclusion claims dominance over the state of the art in query time,
  index size **and index construction time**, which its own Table 4 contradicts (LI+ builds faster on AX, CT,
  ZH). This is the over-claim to avoid: the experiments are honest, the summary is not.
- Quote: "However, in these datasets, our query performance is about one or two orders faster".

### P3 DLCR (PVLDB 2022), dynamic LCR 2-hop index
- **A.** Gains only; frames a counter-intuitive design choice (query-friendly, update-unfriendly arrays)
  positively as a surprisingly strong result.
- **E, losses.** Index size is about 4x that of P2H+, one sentence with its cause (inverted indices and
  per-entry extra information). Deletion is 5-10x slower than insertion, stated as a neutral characterisation.
  All cells stay in Tables 6-7.
- **Synthetic.** Tick column for synthetic labels; one sentence in the setup; uniform random edge deletions,
  then the same edges re-inserted.
- **Baselines.** P2H+ code from its inventors; ARRIVAL (approximate) is compared on accuracy as well, so a
  faster competitor is shown with its error rate.
- **Deferred regime analysis.** The question of when an update beats rebuilding the index is
  answered in the technical report, announced in one sentence in the setup.
- **C.** Two sentences of claims; one future-work sentence (parallel construction and update).
- Quote: "we synthesize edge labels in exponential distribution following the setting in [21]".

### P4 IFCA (ICDE 2023), index-free dynamic reachability (closest analogue for weak spots a and b)
- **A.** Gains only, scoped to realistic query workloads on large real dynamic graphs.
- **I.** One scope sentence, positively framed: designed for graphs with communities, still efficient on graphs
  without them. Then a striking move: the authors present as their own *finding* that BiBFS beats indexed
  state of the art when query and update time are counted together, and that their method is at least
  comparable to BiBFS when no communities exist because it falls back to BiBFS.
- **E, pre-registered expectations.** A "Goals" list before the results says what should happen, including
  parity (not a win) on graphs without communities. Weak regimes are therefore hypotheses that are confirmed,
  not surprises.
- **E, loss on queries.** TOL and IP answer queries much faster than IFCA; the same sentence calls this expected
  because IFCA builds no index (mechanism inside). Negative queries are slower when the neighbourhood has
  cycles or high-degree vertices (1 sentence, mechanism).
- **E, crossover.** A full paragraph and Fig. 6 plot total time against queries per update (QpU) to find where
  the advantage reverses; the lines do not cross below QpU 1,000 except on named datasets. The paragraph ends
  with real update rates of production graphs to argue that high QpU is unlikely in their target setting.
- **Synthetic workload.** Random timestamps on four static graphs; the paper argues its temporal-replay workload is
  closer to reality than the random updates used by almost all earlier dynamic-reachability work. A data
  weakness becomes a methodological point.
- **Baselines.** Authors' code for all competitors.
- **C.** Gains; one future-work sentence (constrained reachability).
- Quote: "which is expected because IFCA does not build any index to prune its search".

### P5 RLC index (ICDE 2023), static recursive-label-concatenated reachability
- **A/C.** Gains; the conclusion positions the index as a balance between online traversal and a materialised
  closure. This is scope phrased as a design point.
- **Synthetic.** Tick column; labels generated for unlabelled graphs; query generation justified as common
  practice in the literature, with three citations.
- **Baselines.** BFS, BiBFS and an extended transitive closure (ETC) the authors define themselves; ETC cannot be
  built within 24 h except on the smallest graph, which is reported plainly.
- **Systems comparison.** Two commercial engines are anonymised (one sentence with the reason); all systems run
  single-threaded, explicitly for fairness. Table V reports speed-ups **and break-even points**: the workload
  size at which building the index pays off against each engine. A cost (index build) is thereby quantified as an
  amortisation threshold.
- **Static only.** No update support and no sentence about it; silence, not concession.
- Quote: "We do not reveal the identity of all the systems as some are proprietary".

### P6 HL-index (ICDE 2026), static hypergraph reachability labels
- **A/C.** Gains only. The conclusion sizes the neighbour index's memory with the adjective *slight* (cost named
  once; the number is in the table).
- **M.** The word "Limitation" appears as a numbered list (Limitation 1-3) for the authors' own *basic*
  construction algorithm, each solved by the next subsection. The limitation vocabulary motivates components.
- **Baselines.** All implemented by the authors in one C++ code base; the adaptation of the approximate
  competitor is disclosed in one clause, without a hedge.
- **Synthetic.** 3 of 20 hypergraphs synthetic; stated in one sentence.
- **No losses, no future work.** Static only, not mentioned as a limitation.
- Quote: "we have modified it to adapt to our problem".

### P7 BatchHL (SIGMOD 2022), batch-dynamic distance labelling
- **M.** Model mapping in one sentence: weight increases are handled like deletions, decreases like insertions.
- **E, loss to a static method.** A static parallel labelling (PSL*) has better query time on some datasets
  (not named in the sentence; the table shows them); the same sentence adds that it handles only static graphs, then two numbered reasons why it is unsuitable for
  dynamic graphs (rebuild cost, label size), then a three-factor verdict: BHL+ has the best trade-off.
- **E, own-variant loss.** The optimised BHL+ under-performs BHL on LiveJournal; mechanism in the same sentence
  (same affected vertices, extra cost of extended landmark lengths).
- **Baselines.** Authors' code for FulFD, FulPLL, PSL*. Updates: random batches of 1,000 edges.
- **C.** Gains; two future-work items (road networks, separate insertion/deletion algorithms). The road-network
  item quietly marks an unevaluated graph class as future work.
- Quote: "BHL+ stands out in claiming the best trade-off between these factors".

### P8 M2HL (PVLDB 2025), parallel 2-hop label maintenance
- **Title/A.** The regime is in the title ("Dynamic Small-World Graphs"), so a reviewer cannot hold road networks
  or deep hierarchies against the paper.
- **M.** Defined on undirected graphs; directed inputs were converted to undirected for the main runs; a short
  section sketches extensions to directed and weighted graphs and a small experiment checks them. The conclusion
  closes by calling the approach easy to extend to both.
- **E, loss (3 sentences).** With 50 landmarks BatchHL+ updates up to two orders of magnitude faster; mechanism
  (more relaxed index structure); regime (the gap narrows as landmarks grow, comparable above 500); then
  the targeted metric (M2HL queries up to four orders faster, with mechanism).
- **Baselines.** One competitor omitted from tables because it cannot finish on most datasets (stated).
- **C.** Gains plus the extension sentence; no losses.
- Quote: "the performance gap narrows significantly as the number of landmarks increases".

### P9 Sieve (PVLDB 2020), access-control enforcement in DBMSs (closest analogue for weak spots c, d, e)
- **A.** Gains only.
- **I.** One sentence defers technical details (including dynamic policy updates) to the extended version.
- **M, model reduction.** Deny policies are not first-class: one sentence says a deny can be translated into
  explicitly listed allow policies, with an example. The restriction is stated as a reduction, not as a
  missing feature.
- **Synthetic policies (one paragraph).** Reason first (the real WiFi dataset has no user-defined policies),
  then grounding (town-hall meetings and surveys of privacy preferences), then a profile-based generator with
  stated proportions. A second, fully synthetic dataset is used for scalability.
- **Baselines.** Three baselines built by the authors, including a carefully hand-rewritten one (BaselineI)
  that is stronger than the other two; the paper shows it beats its own weaker baselines before beating it.
- **Crossovers as design facts.** The per-tuple UDF operator pays off from about 120 policies; index-query vs
  index-guard choice switches at a query cardinality around 0.07; both are introduced as expected outcomes and
  fed into the cost model.
- **C.** Gains; two future directions (tighter optimizer integration, co-optimising with pre-processing).
- Quote: "we can translate it into the explicitly listed allow policies".

### P10 DBSP (PVLDB 2023), general IVM incl. recursion (reference point for weak spot g)
- **Evaluation scope.** The paper contains no benchmark section. One sentence defers the system description
  and evaluation to a future paper; another says benchmark results are in the repository.
- **Comparison with specialised systems.** One sentence leaves open whether custom DBSP operators can match
  systems specialised for narrow query classes. A general IVM engine is therefore not presented, by its own
  authors, as a performance baseline for specialised indexes.
- **Verification scope.** One sentence: the theorems are machine-checked, the implementation is not.
- **M.** Non-termination over unbounded domains is stated as a property of the construction, not a defect.
- Quote: "We defer a full description and evaluation of the system to a future paper".

### P11 F-IVM (SIGMOD 2018; full arXiv version read)
- **E, near-tie.** On Retailer, F-IVM and first-order IVM have almost the same throughput (2.955M vs 2.926M
  tuples/s, about 1%). The text calls F-IVM the highest on both datasets and gives the mechanism for the
  competitor's strength (updates hit the fact table and the other relations are small). The near-tie is visible
  in the table but not named as such; weaker than naming it.
- **E, cost wording.** A faster variant is described as two orders of magnitude faster, with its 23x memory cost
  in the same sentence (cost named once, next to the gain).
- **Baselines.** All approaches run in the same modified DBToaster runtime; the paper states this as the fairness
  control and adds that algorithms and record types differ.
- **Data.** One real dataset from an industrial collaborator, alongside public ones.
- **C.** Gains; one future-work sentence (further tasks).
- Quote: "at the cost of using 23x more memory".

### Background: Hanauer, Henzinger, Schulz (SEA 2020)
- The abstract reports that earlier studies found simple traversal competitive or superior except on dense random
  graphs or very query-heavy mixes. In the target paper, this citation supports the shallow-graph result
  (weak spot a) as a finding consistent with the literature.

---

## 2. Cross-paper observations

Denominators: 11 corpus papers; 10 with an experimental section (DBSP has none); 8 papers report at least one
cell where a competitor or a simpler variant wins (TOL, P2H+, DLCR, IFCA, BatchHL, M2HL, F-IVM, Sieve).

| Observation | Count | Papers |
|---|---|---|
| Abstract states a loss against a baseline | **0 / 11** | none |
| Title or abstract carries a regime/scope qualifier on the positive claim | 4 / 11 | M2HL (small-world, title), IFCA (real dynamic graphs, communities), RLC (at most k labels), TOL (vertex updates on large dynamic graphs) |
| Introduction states a scope of the own method | 1 / 11, one sentence, positive form | IFCA (designed for graphs with communities, still efficient without them) |
| Introduction presents "simple search is strong" as a finding | 1 / 11 (plus TOL, which uses BFS as the yardstick for a competitor) | IFCA |
| Model restriction stated as definition/assumption/reduction with precedent or extension pointer | 6 / 11 | TOL (DAG, precedent), Sieve (deny to allow), M2HL (undirected + extension section), BatchHL (weight mapping), P2H+ (large-label subsection), DBSP (termination) |
| Pre-registered expectation before results | 2 / 11 | IFCA (Goals list), Sieve (crossovers introduced as expected) |
| Losing cells kept in tables/figures | **8 / 8** | all with losses |
| Losing cells named in text | 7 / 8 | all except F-IVM (near-tie visible only in the table) |
| Loss followed by a mechanism within 1-2 sentences | 7 / 8 | all except P2H+ (counter-metric instead) |
| Loss paired with a win on another metric or workload | 6 / 8 | TOL, P2H+, DLCR, IFCA, BatchHL, M2HL |
| Crossover or break-even quantified | 5 / 11 | IFCA (QpU), RLC (break-even workload), Sieve (~120 policies; cardinality ~0.07), M2HL (landmarks > 500), DLCR (update vs rebuild, in tech report) |
| Plain BFS/online search included as a baseline | 4 / 11 | TOL, IFCA, RLC, HL-index |
| Synthetic labels, updates or policies used | 8 / 11 | TOL, P2H+, DLCR, IFCA, RLC, HL-index, BatchHL, Sieve |
| ... stated in at most 2 sentences in the setup (Sieve: 1 paragraph) | 8 / 8 | |
| ... with a precedent citation or real-data grounding | 6 / 8 | P2H+, DLCR, RLC, TOL (precedent); IFCA (real timestamps argument); Sieve (surveys) |
| ... marked by a "synthetic labels" column in the dataset table | 3 / 8 | P2H+, DLCR, RLC |
| ... with an apology ("may not reflect", "a threat") | **0 / 8** | |
| A non-trivial competitor is the authors' own implementation (BFS/BiBFS baselines not counted) | 4 / 11 | HL-index (adapted HypED, ETE-reach), Sieve (three baselines), F-IVM (1-IVM/DBT in a modified DBToaster), RLC (ETC); TOL, P2H+, DLCR, IFCA, BatchHL use the competitors' authors' code; M2HL does not say |
| ... with a sentence casting doubt on those implementations | **0 / 4** | fairness stated positively instead (F-IVM same runtime, RLC single-thread) |
| "Limitation(s)/drawback/weakness" applied to the final method | **0 / 11** | applied to prior work (DLCR, IFCA, RLC, BatchHL, M2HL, Sieve) or to own basic variants (HL-index, IFCA) |
| Dedicated Limitations / Threats-to-validity heading | **0 / 11** | |
| Conclusion lists losing cases | **0 / 11** | |
| Conclusion over-claims against its own table | 1 / 11 | P2H+ (claims dominance incl. construction time) |
| Future-work sentences in the conclusion | 6 / 11, 1-2 sentences, extensions only | TOL, DLCR, IFCA, BatchHL, Sieve, F-IVM |
| Evaluation or comparison explicitly deferred (tech report / future paper) | 3 / 11 | DLCR, Sieve, DBSP |

Typical length: one loss takes 1-3 sentences and appears **once**. The longest treatment is IFCA's
queries-per-update paragraph (about 8 sentences), and most of it is analysis that ends with a scope verdict, not a
concession.

Typical vocabulary: *except on, generally comparable, slightly, on some datasets, which is expected,
at the cost of, trade-off, the gap narrows, at least comparably, as expected, break-even, in most datasets*.

---

## 3. Writing rules with before/after for the AuthZ paper

Each rule keeps every number. "Before" is either the current Overleaf text (marked *current*) or a typical
self-negating draft (marked *draft*). Numbers are from `numbers.tex` as of 2026-11-08; keep the macros in LaTeX.

**R1. Put the regime in the claim; never a separate negative sentence in the abstract.** (a)
*Supported by: M2HL (title), IFCA, RLC, TOL; 0/11 abstracts state a loss.*
- Before (*draft*): "On shallow graphs, such as a production ERP graph, online BFS is as fast or faster
  (0.85x), so the index helps only on deep hierarchies."
- After: keep the current abstract sentence "On deeply nested graphs, FLIX answers checks 41.0x faster than
  online evaluation, ... and 19.6x on the English Wikipedia category hierarchy", and say nothing about the
  shallow regime in the abstract. The ERP sentence in the abstract already carries the paper's actual ERP
  claim (no false allow, while grant lagging has them); do not add its latency ratio there.
- Optional title or contribution qualifier: "... over Deeply Nested Authorization Graphs" only if the
  freshness claim (no stale allows on every graph) is not weakened by it. The freshness claim holds on shallow
  graphs too, so the qualifier belongs on the speed claim, not the title.

**R2. Present "online search is strong on shallow graphs" as a finding consistent with the literature, and
pre-register it.** (a)
*Supported by: IFCA (finding in I, Goals list in E), TOL (BFS as the bar), Hanauer et al. (background).*
- Before (*current*, intro): "A natural objection is that online breadth-first evaluation is already fast in
  memory. On shallow graphs it is, and we report this regime explicitly."
- After (intro, one sentence + pointer): "Consistent with earlier studies of dynamic transitive closure
  [hanauer2020fdtc], online search is competitive when a user's closure has a few dozen subjects; the index
  targets the deep hierarchies where closures reach thousands, and Section~\ref{sec:exp-latency} measures where
  the two meet."
- After (start of RQ2, one sentence): "We expect FLIX to be within a small constant of BFS when closures are
  small and to gain with closure size; Fig. X tests both."

**R3. State each losing cell once, then the mechanism with a measured statistic, then the bound.** (a)
*Supported by: TOL (trees), DLCR (inverted indices), IFCA (no index), M2HL (relaxed structure), BatchHL (LJ),
F-IVM (small relations).*
- Before (*current*, ERP): "Closures are small (5.1 subjects on average), so FLIX runs at 0.85x the speed of BFS:
  on this deployment online evaluation suffices for latency, but stale allows still arise."
- After: "Closures are small (5.1 subjects on average), so a check costs about as much as visiting the closure
  itself [the shallow-graph mechanism of RQ2; confirm it holds on ERP] and FLIX runs at 0.85x the speed of BFS. Freshness, not latency, is what this deployment needs from
  the index: grant lagging returned 10-18 false allows, FLIX none."
  (Deletes "suffices", keeps 0.85x, adds the mechanism and puts the targeted metric second.)
- Shallow graphs (*current* already follows R3: "faster on 6 graphs and slower on AMZN, YouTube ... this fixed
  work is comparable to visiting the closure itself"). Keep it; add the absolute bound once: "all exact methods
  answer within 2.42 us".

**R4. Turn a latency loss into a workload crossover.** (a), (b)
*Supported by: IFCA (QpU plot + real update rates), RLC (break-even workload), Sieve (~120 policies), M2HL
(landmarks > 500).*
- Before (*draft*): "Because BFS needs no index, FLIX is not worthwhile when updates are frequent."
- After (*current* text already has q*): "Since BFS maintains no index, it does less total work below q* checks
  per update (q* = 4.65 on DEEP-16); at 100 checks per update, close to the 99:1 production mix [varuni2026icact],
  FLIX does 14.3x less work." Put q* in the table caption as well, so the crossover is a column, not a confession.
- For (b): "who" can be framed the same way only if you have measured it; otherwise use R5.

**R5. Pair a loss on a secondary query or metric with the primary one, using "trade-off" / "at the cost of".** (b), (f)
*Supported by: TOL (deletion vs insertion/query), P2H+ (index time vs query), DLCR (size vs query), BatchHL
(three-factor trade-off), M2HL (update vs query), F-IVM ("at the cost of").*
- Before (*current*, threats paragraph): "Our who and what queries reuse the per-hub labels without a dedicated
  index. They agree with the oracle on all graphs, but who is 1.38-3.20x slower than one reverse search, while
  what is 1.76-3.75x faster on the deep graphs."
- After (move from "Threats" to the RQ2 latency section, one unit): "Reverse queries reuse the per-hub labels
  without a dedicated index and agree with the oracle on all graphs. `what` is 1.76-3.75x faster than a forward
  search on the deep graphs; `who` is 1.38-3.20x slower than one reverse search, because [state the measured
  cause in one clause; do not guess it]. The index is designed for checks; an output-sensitive `who` is left
  to future work (Section~\ref{sec:conclusion})."
- Before (*current*, f): "The price is false denies for buffered grants, 1.8% of all checks in the main runs."
- After: "Deferral trades the visibility of new grants for safety: buffered grants appear as false denies in
  1.8% of the checks in the main runs (4.6% on the ERP graph), and no check returns a false allow." Keep both
  numbers; state the ERP 4.6% in the ERP subsection with its cause (the share of grants in the real stream),
  and do not repeat it in the conclusion.

**R6. Synthetic labels: state once in the setup, mark in the dataset table, cite precedent, add the real case.** (c)
*Supported by: P2H+, DLCR, RLC (tick column + precedent), Sieve (grounding paragraph), IFCA (realism argument);
0/8 apologise.*
- Before (*current*, threats): "Conditions and deny edges are synthetic on the SNAP, AMZN and real-hierarchy
  graphs (real on the ERP graph), and the deep layers of Section VI-C are synthetic; we know of no published
  statistics on closure sizes in production directories."
- After (setup, two sentences): "Public graphs carry no conditions or deny edges, so we add them as in [Zanzibar /
  Cedar-style generator citation, or the LCR practice of P2H+/DLCR] (column 'syn.' in Table II); the ERP graph
  carries its real 9,420 conditions, 5,549 deny edges and its 2026 change stream." Then drop the sentence from the
  threats paragraph. Keep "we know of no published statistics on closure sizes" only if you turn it into a
  reason for the depth sweep ("closure size is therefore varied from 2 to 16 levels").

**R7. Baselines: give provenance plus the fairness control, never doubt.** (d)
*Supported by: F-IVM (same runtime), RLC (single-threaded for fairness, anonymised engines), HL-index (adaptation
disclosed in one clause), Sieve (built a strong hand-rewritten baseline); 0/4 cast doubt on their own baseline code.*
- Before (*current*): "Baselines other than BFS are our reimplementations." and, in threats: "Baselines are
  reimplementations that follow the published algorithms and share our graph store, which favours them on
  memory locality."
- After (setup, once): "[Verify before use:] Because the published implementations do not evaluate conditions and
  deny, we implemented TC, 2-hop, LCR and SV from their papers in our code base; all methods share the same graph
  store and run single-threaded in the same binary, which gives the baselines the same memory locality as FLIX." Delete the threats-paragraph duplicate.
  The second clause is the F-IVM/RLC move: the shared store is a fairness control, so state it as one.

**R8. Model scope as a definition or reduction in the preliminaries, plus an extension pointer.** (e)
*Supported by: TOL (DAG assumption + precedent), Sieve (deny reduced to allow), M2HL (undirected + extension
section), BatchHL (weight mapping), P2H+ (extension subsection).*
- Before (*draft*): "We do not support intersection or tuple-to-userset rewrites."
- After (*current* prelim is close; tighten): "Union rewrites become parallel edges, top-level exclusion becomes
  deny, and caveats become conditions; this covers the [N] relation types of the ERP model [state if true].
  Intersection and tuple-to-userset rewrites are outside the model; nested exclusion is handled as described in
  [the section the current prelim already points to]." Add a one-clause reason for the exclusion only if it is
  stated and proved elsewhere in the paper. Do not mention (e) again in the threats paragraph or the
  conclusion. If you have a count of how many real policies use intersection or tuple-to-userset, give it here
  (Sieve/P3-style grounding); if not, do not guess.

**R9. Out-of-scope systems aspects: one sentence each, as orthogonal or future work, and use the DBSP precedent
for general engines.** (g)
*Supported by: DBSP (evaluation deferred; parity with specialised systems left open), DLCR (parallelism as future
work), TOL (external memory), Sieve (optimizer integration).*
- Before (*draft*): "We did not evaluate concurrency, and we did not benchmark a general Datalog or IVM engine,
  which might be competitive."
- After (related work, one sentence): "Definition 2 is a two-stratum Datalog program, so general IVM engines
  [DBSP, F-IVM, DDlog] can maintain it; whether such engines match specialised indexes is open even for their
  authors [DBSP]. A recursive-SQL formulation on SQLite, included in the artifact, agreed with our oracle on all
  35,000 pilot checks." (The current setup paragraph reports 0 mismatches in 35,000 checks; this turns the
  existing pilot into the general-engine reference point instead of an unanswered omission.)
- After (conclusion, one sentence): "Future work includes output-sensitive `who` queries, concurrent updates and
  integration with a distributed tuple store." (The current conclusion already does this; keep it at one
  sentence.)

**R10. Reserve "limitation" vocabulary for prior work and your own basic variants; replace the Threats heading
with a scope unit.** (all)
*Supported by: 0/11 Limitations/Threats headings; HL-index and IFCA use "limitations" for their own basic
algorithm to motivate the next component.*
- Before (*current*): `\subsection{Threats to Validity and Scope}` with (c), (e), (d), cache semantics and (b)
  in one block.
- After: dissolve it. (c) and (d) go to the setup (R6, R7), (e) to the preliminaries (R8), (b) to RQ2 (R5).
  If a residual unit remains (e.g. the cache baselines model documented semantics, not a full service), keep a
  two- or three-sentence paragraph titled "Scope of the comparison" at the end of the setup. For an EAB-style
  review lens this is still visible, but it no longer reads as a list of weaknesses.

**R11. Conclusion: scoped claim, no losses, at most two future-work sentences; never over-claim.** (a)-(g)
*Supported by: TOL, DLCR, IFCA, BatchHL, Sieve, F-IVM (future work as extension); P2H+ as the counter-example.*
- Before (*draft*): "FLIX is faster than BFS only on deep graphs and its who query is slower; deferral causes
  false denies; we did not support intersection."
- After (*current* conclusion is already close): "FLIX returned no false allow on any graph, including a production
  ERP graph, and was 41.0x faster than online evaluation on deeply nested graphs (19.6x on the Wikipedia
  categories). Future work includes output-sensitive `who` queries, concurrency and integration with a tuple
  store." Do not write "outperforms on all graphs" or "dominates": P2H+'s dominance sentence is
  contradicted by its own table, and a reviewer who reruns BFS on the shallow graphs will find the same here.

**R12. Name small losses with the measured range and an absolute bound; use "comparable/parity" only with the
number.** (a)
*Supported by: TOL (comparable, two exceptions named), BatchHL (losing datasets left to the table), M2HL
(comparable above 500 landmarks), P2H+ (datasets named).*
- Before (*draft*): "On LJ-full and Friendster the index brings no benefit."
- After (*current* is right; keep it): "On LJ-full and Friendster, whose closures are shallow, the two methods
  are at parity (1.21x and 0.98x)." Add nothing else; do not use "no benefit", "does not help" or "only 1.2x".
- Same for SV: "slower than BFS on 9 of 15 graphs" is a competitor's loss, so state it plainly with the fallback
  mechanism, as the current text does.

---

## 4. Phrases never seen, and what the corpus uses instead

Never applied to the authors' final method in the 11 papers (checked by text search over all extracted texts):

| Never seen (own method) | Seen instead | Where |
|---|---|---|
| "Limitations" / "Threats to validity" heading | scope in the claim; one-sentence assumption; extension subsection | all 11 |
| "our method fails", "does not help" (as a result) | *except on X*, *generally comparable*, *expected* + the mechanism | TOL, IFCA. ("will not help" occurs once, in DLCR, inside a rule that decides when batching is used, not as a result) |
| "only N x faster" for the own speedup | *only* is used for competitors (a competitor barely better than BFS) and for a competitor's scope (static graphs only) | TOL, BatchHL |
| "the advantage vanishes / disappears" | *the gap narrows*, *the advantage reverses at* + a crossover number | M2HL, IFCA |
| "BFS suffices", "no index is needed" | BiBFS's strength stated as the authors' own finding (query plus update time), plus fallback and crossover | IFCA |
| "synthetic data may not reflect real deployments" | labels synthesized following a cited setting; tick column; grounding in surveys | P2H+, DLCR, RLC, Sieve |
| "our reimplementations may be suboptimal / may favour us" | *same runtime*, *single-threaded for fairness*, adaptation disclosed in one clause | F-IVM, RLC, HL-index |
| "we do not support Z" in abstract or introduction | *we assume, as in [x]*; a reduction (*can be translated into*); *can be extended* + an extension subsection | TOL, Sieve, M2HL, P2H+ |
| A list of losing datasets in the conclusion | scoped claim + 1-2 future-work sentences | 0/11 list losses |
| "unfortunately", "disappointingly", "a weakness of our approach" | not used at all | 0/11 |

Current AuthZ text items that match the left column and should be rewritten:
"online evaluation suffices for latency" (ERP subsection) -> R3; `\subsection{Threats to Validity and Scope}` ->
R10; "Baselines are reimplementations ... which favours them" -> R7; the duplicated synthetic-data sentence in
threats -> R6.

---

## Checklist before submission
- [ ] The abstract carries the deep-nesting qualifier on the speed claim and no shallow-graph sentence.
- [ ] The introduction has one sentence that frames the shallow regime as an expected, literature-consistent
      finding, with a pointer to RQ2. The contribution list has contributions only.
- [ ] Each losing cell (shallow 0.64-1.94x with AMZN and YouTube named; ERP 0.85x; `who` 1.38-3.20x; LJ-full and
      Friendster parity; LCR cheaper updates on 7 graphs) is named once, in the subsection that measures it,
      with its mechanism and, where possible, the targeted metric or a crossover (q*).
- [ ] Synthetic conditions and deny edges: two sentences in the setup and a column in the dataset table; the
      ERP graph is named as the real case. No apology.
- [ ] Baseline provenance and the shared-store fairness control appear once, in the setup.
- [ ] Intersection and tuple-to-userset appear once, in the preliminaries, as outside the model.
- [ ] False denies (1.8% main runs; 4.6% ERP) appear once each, with "trades ... for safety" and zero false allows.
- [ ] No "Threats" heading; at most a 2-3 sentence "Scope of the comparison" paragraph.
- [ ] The conclusion has the scoped claim and one future-work sentence; nothing in it is contradicted by a table.
- [ ] Every number above still appears in a table or figure.
