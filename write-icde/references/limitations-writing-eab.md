# Stating limitations in EAB papers without self-negation (ICDE practice)

Evidence: five accepted ICDE "Experiment, Analysis & Benchmark" (EAB) papers (ICDE 2026 and ICDE 2027 R1). The full extracted texts were read on 2026-11-06, including the appendices and table captions. Each item below is an observation from those papers. None of it is an official rule of the venue.

This file is the EAB companion to `claude-skills/write-icde/references/limitations-writing.md`, which was built from ten graph-algorithm papers. It uses the same format: corpus, observations with counts, then rules with "Supported by".

**Integrity boundary.** The same boundary applies as in the algorithm guide. The rules below change only wording, placement, frequency and framing:
- every measured number stays in the paper;
- no claim becomes false;
- no evaluated system is hidden;
- facts a reviewer needs to judge validity stay in the paper: sample sizes, number of runs, judge model, hardware, and what was excluded and why.

Some accepted papers leave out some of these facts (see Section 3). That shows the omission was survivable in those cases. It is not a rule to copy.

**Quoting convention.** Verbatim wording is limited to short functional phrases (five words or fewer) needed for the vocabulary analysis. Everything else is paraphrase. Sentence counts are approximate ("≈"), because the PDF-to-text extraction merges some line breaks.

---

## 0. Corpus

| Code | Paper (short name) | Venue | Full text used | What is benchmarked |
|---|---|---|---|---|
| DCO | Distance Comparison Operations Are Not Silver Bullets in Vector Similarity Search | ICDE 2026 EAB | arXiv 2604.02801v1 (12 pp. + appendices A–P; appendices I–P repeat A–H in the extraction) | 8 DCO methods, 10 vector datasets, CPU±SIMD/GPU |
| RLESI | Benchmarking RL-Enhanced Spatial Indices Against Traditional, Advanced, and Learned Counterparts | ICDE 2026 EAB | arXiv 2512.11161v1 | 12 disk-based spatial indices, 6 datasets, 7 workloads |
| XRAG | XRAG: eXamining the Core – Benchmarking Foundational Components in Advanced RAG | ICDE 2026 EAB | arXiv 2412.15529v4 | RAG components and 5 orchestrators, 4 QA datasets, ConG/ConR/LLM-judge metrics |
| TSF | TS-Fault: Benchmarking Time Series Forecasters Against Structural Faults | ICDE 2027 R1 EAB | arXiv 2606.18539v1 | 21 forecasters, 6 datasets, 4 fault modes × 5 difficulties |
| SQLM | SQLMorph: Query Mutation and Fine-Grained Metrics for Text-to-SQL Evaluation | ICDE 2026 EAB | arXiv 2609.08950v1 | 3 Text-to-SQL systems on BIRD dev, generated query variants, new metrics |

A distinction is used throughout the file:
- **Method negatives**: negative findings about the systems being evaluated. These are the contribution of an EAB paper.
- **Benchmark limits**: limits of the authors' own benchmark, protocol, data or metrics.

The algorithm guide only has one category, because there the authors' method is the object being evaluated.

---

## 1. Per-paper records

Columns:
- **Loc**: section.
- **Sent.**: number of sentences.
- **Wording**: a phrase of five words or fewer.
- **Paraphrase**: what the passage says.
- **Device**: how the passage frames the limit.

### 1.1 DCO (ICDE 2026 EAB)

**Statements of benchmark limits**

| Loc | Sent. | Wording | Paraphrase | Device |
|---|---|---|---|---|
| III-A taxonomy | 2 | "not our primary concern" | Hardware-only acceleration methods are excluded as competitors, because recent work focuses on algorithms. Hardware is instead varied as an experimental condition (Sec. V-F). | Scope with a literature reason, then an immediate mitigation |
| IV-B datasets | 3 | "To simulate" | XUltra (12,288-d) is synthetic. It is built by concatenating real MSMARCO token embeddings to match LLM embedding widths. Ground truth comes from an exhaustive scan. | Synthetic data presented as a design choice with real-data provenance; no concession word |
| IV-C implementation | 1 | "recommended in their original papers" | Every method runs with its authors' recommended parameters. | Fairness convention |
| IV-C implementation | 2 | "processed sequentially" | Batch queries run sequentially, SIMD uses SSE, and multithreading is off. Appendix A gives a one-sentence justification: an established protocol, for a fair comparison. | Protocol fact; justified only in the appendix |
| V intro | 2 | "Due to page limits" | Only selected results are shown. The parameter study, AVX2 and cosine results are in the full version on GitHub. | Space constraint plus a pointer |
| V-D index construction | 1 (clause) | — | Classification-based methods are excluded because they need a built index to train. | Exclusion explained by a property of the method |
| V-E dynamic data | 1 | "We focus solely on insertion" | Deletions are not tested, because deletion logic is independent of the DCO. | Scope with a technical reason |
| V-F hardware | 1 | "lacks native GPU support" | The hardware study uses IVF only, because HNSW lacks native GPU support. | Scope with a technical reason |
| V-G summary | 1 | — | The recommendation chart is based on average QPS rank at recall above 95%. | Disclosure of the criterion |
| App. H (parameter study) | ≈4 | — | Tuning the step sizes Δ0/Δd raises QPS of ADSampling, DADE and DDCres by up to 1.5×, 1.8× and 1.8× over the prior-work defaults. The main conclusions (which used the defaults) are not re-examined against this. | Reported as a takeaway about the methods, not as a threat to the benchmark |

**Not stated anywhere:**
- the single machine (one Ryzen 9 5950X CPU and one RTX 3090);
- the number of repetitions or any variance;
- that the CPU results use HNSW and the GPU results use IVF, which mixes index type with hardware.

**Totals.** About 18 sentences on benchmark limits, in roughly 10 places. All are in Sec. III–V or the appendix. None is in the abstract, introduction or conclusion.

**The "Limitations" paragraph (V-G)** has 4 bold bullets and about 9 sentences. Every bullet is about the DCO methods, with numbers: QPS losses of up to 8–42% and 77–79%, and speedups narrowing from 2.0–4.4× to 1.2–3.8× on IVF once SIMD is on. A symmetric "Merits" list (4 bullets) comes first.

**Framing**
- Dedicated section on the benchmark itself: none.
- Devices used: scope with a reason (4), protocol fact (2), pointer to the full version (2), fairness convention (2).
- Adjacent mitigations:
  - the hardware exclusion is followed by "evaluated later as a condition";
  - the page limit is followed by a pointer to the full paper.
- Vocabulary about the authors' own benchmark: "comprehensive", "first", "fill this gap", "from scratch within a unified framework", "for a fair comparison".
- Deficit vocabulary pointed only outward:
  - the four prior-work bullets are titled Narrow, Insufficient, Restricted and Limited;
  - "not silver bullets", "fail to maintain", "in only 4 out of the 14 subfigures".
- Never used about the authors' own benchmark: limitation, threat, limited, small.

**Abstract and conclusion.** Both carry method negatives:
- the methods are sometimes slower than a full scan;
- they are unstable across hardware;
- they are "not yet ready for production".

Neither says anything negative about the benchmark.

### 1.2 RLESI (ICDE 2026 EAB)

**Statements of benchmark limits**

| Loc | Sent. | Wording | Paraphrase | Device |
|---|---|---|---|---|
| I intro | 1 | "prioritize open-source implementations" | Baselines are selected by whether code is available, for reproducibility. | Selection criterion presented as a virtue |
| II | 1 | "we focus on points" | Only point data is used, because RLESIs are optimised for points. | Scope justified by the target methods |
| III-B.1 | 2 | — | LISA and ZM-index get leaf capacity 10,000 instead of 100, because otherwise utilisation falls below 10%. | Deviation with a measured reason |
| III-B.2 | 3 | "we reuse the insertion method" | Qd-tree and GKD-tree have no insertion algorithm of their own, so KD-tree insertion is reused. Mapping-based indices reuse R-tree insertion, because keeping the order during insertion is hard. | Adaptation disclosed with a reason |
| III-C baselines | 3 | "comparing them all unfeasible" | One representative per family. RLR-tree is the only open-source DP option. LMSFC is excluded because it has no public code. | Feasibility and availability reasons, given per family |
| IV-A datasets | 4 | "widely used in recent studies" | Three of the six datasets are synthetic. Each distribution is tied to the prior papers that used it. AUS is new but adds skew. | Precedent citation for each dataset |
| V-A | 1 | "allowing for brevity" | I/O is reported only for range queries, because I/O trends match latency. | Reporting choice with a reason |
| V-A, O1 | 1 | "as indicated by training logs" | Qd-tree's RL model did not converge well. The training logs show it, and [10] reports the same problem. | Process problem turned into a property of the method, with external corroboration |
| V-A O4, V-B O8 | 1 + 1 | "missing implementation" | ZM-index has no dedicated kNN algorithm and reuses R-tree's, which explains its kNN results. | Implementation gap stated as the cause of a result |
| V-D | 1 | "Due to space constraints" | Read-heavy query latency is moved to the supplementary material. | Pointer |
| V-E, O15 | 1 | "is omitted here" | Tuning time (more than 30 h per dataset per index) is left out of the build-time figure, but the number is stated. | Cost disclosed numerically, once |
| V-E, O17 | 1 (clause) | "in the absence of" | LISA stands in as the space-partitioning learned index, because no binary-partitioned learned index exists. | Substitution with a reason |
| V-G tuning | 2 | "search space remains limited" | The grid is small, but the chosen parameters matter most and are enough. Grid search was chosen because it is simple with few parameters. | Concession and justification in the same sentence |
| V-G tuning | 2 | "rather than re-tuned" | Tuning uses range-query latency only, and the result is reused for all workloads. | Design choice. It returns in VI-A as an RLESI property: trained only on range queries, so they lack generalization |
| V-G, O20 | 2 | "likely due to restricting" | BM-tree gained little from tuning, probably because its sample size was capped to bound training cost. | The authors' own budget limit, disclosed where it matters, with a hedged cause |
| VI-B "Challenges" | 3 | "This mismatch means" | Training on samples but building on the full data creates a locality mismatch. | A protocol property presented as a challenge of RLESIs |

**Not stated:**
- a single server with an HDD only (no SSD, no in-memory setting);
- repetitions or variance;
- only 2-D data, beyond the remark about points;
- that the tuning grid (Table III) has 12–20 configurations per index.

**Totals.** About 31 sentences in about 16 places. Two are in the introduction or contribution list. The rest are in Sec. II–VI.

**Section VI "Insights and Limitations"**
- The "Limitations" sub-part (2–3 sentences) is about the training cost of RLESIs.
- An "Opportunities" part follows, with the authors' own fix: BM-tree-Impr cuts build time by 12% on NORM/SKEW and by up to 27% on US.

**Framing**
- No section on the limits of the authors' own benchmark.
- Characteristic move: two benchmark decisions are later presented as properties of the methods:
  - tuning on range queries only;
  - training on samples.
- Vocabulary about the authors' own work: "first unified benchmark", "fair comparison", "representative", "to ensure reproducibility".
- The only deficit word applied to the authors' own work is "limited" (the tuning grid), in a concessive clause.

**Abstract and conclusion.** Both carry method negatives: RLESIs underperform, have high tuning costs, and generalize poorly. Nothing is said about benchmark limits.

### 1.3 XRAG (ICDE 2026 EAB)

**Statements of benchmark limits**

| Loc | Sent. | Wording | Paraphrase | Device |
|---|---|---|---|---|
| III footnote 2 | 1 | "not the focus" | The web demo and the config hook are not part of the experimental analysis. | Scope |
| Table II caption | 1 | "does not currently support" | XRAG cannot fine-tune. The train/validation splits are kept for future use. | Not-done item and future hook in the same sentence |
| III-C datasets | 3 | "while preserving reliability" | Test sets are subsampled to cut token cost (FQA is used in full). Sampling-based averaging is said to keep reliability. | Cost reason and mitigation claim in the same sentence; no sampling variance is given |
| IV setup + footnote 8 | 1 + 1 | "minor variations" | Temperature 0 is used for consistency. The footnote says LLM generation and evaluation still vary slightly, possibly because of MoE randomness or prompt interpretation, with a citation. | Mitigation first; the residual nondeterminism goes in a footnote with a hedged, external cause |
| IV setup | 1 | "pilot study" | Because of OpenAI token cost, the LLM-judge metrics (CogL) are run only as a pilot that shows capability. | Scope reduction presented as a capability demonstration |
| IV setup | 1 | "repeated three times" | LLM-generation experiments are repeated three times, with standard deviations in the tables. | Mitigation. XRAG is the only paper in the corpus that reports repetitions |
| IV computational resource | 5 | "environments ... are distinct" | Different GPUs per dataset (V100, L20, RTX 4090), with times and index sizes. The latency table (XII) uses FQA only, on identical hardware. | Heterogeneity stated as fact, with numbers |
| V-B | 2 | "unsuitable for most non-critical scenarios" | One judge metric (Dp-RMch) scores below 0.5 while the others score above 0.8, so it may reject correct answers. | Metric-reliability finding turned into usage advice |
| V-B | 2 | "particular weakness of LLM testing" | Judge API calls sometimes fail. The success rate Psc is above 85% and is reported per metric in Tables IX–X. | Process problem attributed to LLM testing in general, bounded by a measured rate |
| VII conclusion | 4 | "In the future" | Planned: component training, more dataset types (open, long-form, multiple-choice QA), robustness to dirty or malformed queries. The community is invited to contribute. | Not-done items presented as a roadmap |

**Not stated:**
- the LLM judge is a single model (GPT-3.5 Turbo), run on three 100-item samples of three datasets (FQA is missing from Tables IX–X);
- no judge–human agreement and no human evaluation;
- the orchestrators are compared on HQA and FQA only (Table XI), with no reason given.

**Totals.** About 22 sentences in about 10 places. All are in Sec. III–V, footnotes, captions, or the future-work list in the conclusion.

**Framing**
- No limitations or threats section.
- The paper uses three devices in turn:
  - cost reason plus mitigation ("while preserving reliability", "pilot study");
  - external attribution of nondeterminism (footnote, cited);
  - a roadmap in the conclusion.
- Vocabulary about the authors' own work: "comprehensive", "exhaustive", "thoroughly", "fair comparison", "pilot study".
- Deficit vocabulary is pointed at prior toolkits: "significant limitations", "restricted scalability", "undeveloped evaluation protocols".

**Abstract and conclusion.** Neither has any negative finding. The abstract is purely descriptive.

### 1.4 TS-Fault (ICDE 2027 R1 EAB)

**Statements of benchmark limits**

| Loc | Sent. | Wording | Paraphrase | Device |
|---|---|---|---|---|
| II-B | 1 | — | Pretraining contamination of foundation models is answered by synthesising faulted inputs at evaluation time. | A known threat turned into a design property |
| III-A | 2 | "isolates input robustness" | Only the inputs are faulted; the target stays clean. | Scope stated as a design choice |
| III-A | 1 | — | Tables report the average risk. The worst case appears only through per-dataset maxima. | Reporting choice |
| IV-E | 1 | "to future work" | Single-mode evaluation is the core protocol. Compositional sweeps are postponed, after composability has been defined formally. | Boundary placed right after the capability |
| V-B models | 2 | "strictly zero-shot" | Foundation models are never fine-tuned, so their results reflect pretrained capability. | Design choice with its interpretation |
| V-C protocol | 2 | "to keep comparisons fair" | A shared training recipe (at most 10 epochs, early stopping). Batch size 16 on Electricity. | Fairness convention |
| V-D metrics | ≈6 | "sensitive to the scale" | The ratio r inflates when the clean error is small. So ΔMSE, r and RD are reported together. Rankings use the median RD, because the mean is dominated by a few extreme configurations. | Metric artefact acknowledged, mitigated immediately |
| VI-A | 2 | "the same verdict" | Robustness ranks by mean faulted MSE differ, but they lead to the same conclusion. | Robustness check against another aggregation |
| VI-D | 2 | "not an artifact" | Foundation-model fragility also holds in absolute ΔMSE. | Artefact objection answered in advance |
| VI-D | 1 | "A plausible mechanism" | The learned-prior explanation is offered as a hypothesis. | Hedge on the cause, never on the numbers |
| VI-F + Table IX | 1 + 1 | "impractical" | ARIMA is omitted on the 321-channel Electricity dataset. | Exclusion with a reason |
| VII-B "Guarding Against Goodhart" | ≈8 | "a feature, not a vulnerability" | Objection: the public scenario parameters invite tuning to them. Answer: hold out parameter combinations at release, as ImageNet-C does. | Anticipated objection turned into a design property |
| VII-D "Threats to Validity" | 5 (≈110 words) | "remain untested"; "unlikely to reverse" | Four threats, each with its counter in the same sentence (see list below). | Dedicated section; every threat is countered by evidence from the paper's own results |

The four items of VII-D:
1. The faults are constructed, not taken from incident logs. Counter: each mode is grounded in documented failures, the ImageNet-C precedent applies, and field validation is left to future work.
2. The weights λ and β are fixed per mode. Counter: difficulty is monotone, and ρ≈0.03 makes it implausible that reweighting restores the ranking.
3. Only energy, load and climate data are used. Counter: the ordering is consistent across all six datasets; finance, traffic and clinical domains are untested.
4. The training budget is a shared 10-epoch recipe. Counter: the stratification tracks architecture rather than fit.

**Not stated:**
- the number of seeds or repeated training runs;
- that each of the 120 configurations has only 20 paired windows;
- any uncertainty on per-model ratios. Spearman p-values are given.

**Totals.** About 36 sentences in about 14 places, including the Goodhart paragraph. The only dedicated threats section in the corpus sits at the end of the Discussion, just before the conclusion.

**Framing**
- Every acknowledged limit comes with a measured counter or a bounded scope, in the same or the next sentence.
- Vocabulary about the authors' own work: "core protocol", "to keep comparisons fair", "remain untested", "unlikely to reverse", "plausible", "a feature, not a vulnerability".
- "fail" and "fragile" are used freely about the evaluated forecasters, never about TS-Fault.

**Abstract and conclusion.**
- The abstract gives three method findings that contradict leaderboard intuition; the conclusion gives five.
- Neither mentions a benchmark limit or a threat.
- The conclusion ends with one generic forward-looking sentence.

### 1.5 SQLMorph (ICDE 2026 EAB)

**Statements of benchmark limits**

| Loc | Sent. | Wording | Paraphrase | Device |
|---|---|---|---|---|
| I intro | 1 | "intended for offline development" | The fine-grained metrics are meant for offline development, where gold queries exist. | Scope of applicability, in the introduction |
| III setup | 2 | "cost-conscious choice" | A medium token budget. The defaults are not claimed to be optimal; the right trade-off depends on the user's goals. | Limit presented as a design choice |
| III-1 | 1 | "on the dev set" | Only BIRD dev is used. | Protocol fact, no reason given |
| III-2 | 2 | "unless otherwise specified" | The framework can pin model versions or run local models to control drift. The experiments use GPT-4o and one OpenAI embedding model. | The capability is stated before the single-model choice |
| III-3 | 1 | "For now" | EX is the primary metric until Sec. VI. | Temporal hedge |
| III-4 | 1 | "representative" | Three open-source systems. Table I shows leaderboard numbers from the time each system was submitted. | Selection framing |
| IV-F.1 | 3 | "lightweight human verification" | All 58 expanded NL–SQL pairs were checked: 43 aligned, 8 add noise, 7 lose the intent. Most are faithful; a small fraction need verification. | Defect in the authors' own artefact, given with exact counts, positive count first, plus a remedy |
| IV-F.3 | 1 | "Manual inspection attributes" | Most failures come from join structure; a small share from DISTINCT, projection or GROUP BY. | Qualitative attribution |
| IV-F.3 | ≈10 | "possibly attributable" | The confound between join complexity and prompt-context noise is isolated by a control experiment on DIN-SQL (recovery falls from 54.90% to 24.05%). The remaining confound is presented as inherent to join-heavy queries. | Threat, then control experiment, then a bounded claim |
| IV-F.3 | 1 | "most straightforward system to instrument" | The control experiment uses DIN-SQL only. | Scope with a reason |
| V-C/V-D | 2 | — | TQA analyses are restricted to queries each system originally solved (998, 857 and 904 queries); the rest are discarded. | Protocol fact with counts |
| VI-B | 1 | "may change the result" | Semantic column matching is deterministic for a fixed embedding model; another model may produce different matches. | Dependency disclosed and bounded (the cost is negligible) |
| VI-C.1 | 1 | "only to the outer query" | Mutations skip subqueries to keep the effects interpretable. | Scope with a reason |
| VI-C.2 | 3 | "remains unchanged" | The system ranking is the same under EX and the new metrics. The new metrics add diagnostic resolution on the 410 queries all systems fail. | Null result on the authors' own metric stated plainly, then its value reframed |
| VII | 1 | "may be worth exploring" | The metrics might serve as RL reward signals. | Hedged forward direction, the only one in the paper |

**Not stated:**
- a single benchmark (BIRD) and a single SQL engine;
- a single LLM, and no repetitions;
- the size of the expansion set (58 queries from 30 seeds) as a sample size;
- whether the 7 misaligned pairs were corrected before EX was computed on Q_exp;
- the number of annotators in the human check;
- why the NC-PC cells in Table XI are "N/A".

**Reading note.** The abstract and introduction say TQA lowers accuracy by up to 17%. Table VII as extracted shows −23.4/−23.9 for DIN-SQL under O/L and L/L. The paper does not reconcile the two. So an accepted paper's headline number can disagree with its own table.

**Totals.** About 32 sentences in about 15 places. One is in the introduction; the rest are in Sec. III–VII. There is no limitations section, and the conclusion has no limits and no future work.

**Framing**
- Characteristic moves:
  - measure the authors' own artefact's defect rate and report it;
  - isolate a confound with a control experiment;
  - say plainly that the new metric does not change the ranking, then state what it adds.
- Vocabulary about the authors' own work: "cost-conscious", "representative", "lightweight", "for now", "deterministic", "limited hallucination".

**Abstract and conclusion.** The abstract carries method negatives: EX degradation with more joins, and up to 17% under TQA. Nothing negative is said about SQLMorph itself.

---

## 2. How each paper handles eight kinds of limit

"—" means the issue is absent and not mentioned. "n/a" means it does not apply.

| Kind of limit | DCO | RLESI | XRAG | TSF | SQLM |
|---|---|---|---|---|---|
| Few models, few runs, single repetition | 8 methods; run count not stated | 12 indices; run count not stated | 4 generators; **3 repetitions with std**; temperature 0; residual variance in a footnote | 21 models; run and seed count not stated; the training-budget threat covers tuning, not repetition | 3 systems, one LLM (GPT-4o); run count not stated; model pinning offered as a capability |
| Synthetic or small data | XUltra synthetic, built from real token embeddings, presented as a design choice | 3 of 6 datasets synthetic, justified by prior-work usage; same 100M scale as the real data | Test-set subsampling "while preserving reliability"; LLM judge on 3×100 items, called a pilot | Constructed faults are Threat (i), countered by documented failures and the ImageNet-C precedent; 20 windows per configuration not discussed | Generated queries checked by execution plus a human check of all 58; small expansion set not flagged; balanced 480-query sample for the join study |
| LLM-as-judge or automatic-metric reliability | n/a | n/a | Dp-RMch flagged unsuitable; API success rate reported; no human agreement | Ratio-scale artefact acknowledged; median vs mean; ΔMSE check; p-values | Weakness of EX is the motivation; dependence on the embedding model disclosed; metrics validated on single-error mutants |
| Scale, latency not production-like | Up to 100M vectors; single-threaded sequential queries justified as an established protocol (appendix) | 100M points on an HDD server; cardinality study (O19); testbed not flagged | Latency on FQA only, on identical hardware; GPUs differ elsewhere | n/a (accuracy); generation cost called linear and cheap | "realistic, medium-token-budget"; defaults explicitly not claimed optimal |
| Methods or settings not evaluated | Hardware-only methods; deletions; classification methods in index build; HNSW on GPU; each with a reason | Non-point data; LMSFC (no code); per-family selection; "Not Available" cells in figures not explained in the text | Fine-tuning; demo; FQA missing from the judge tables; orchestrators on 2 datasets, no reason | Compositional faults (future work); ARIMA on Electricity; no fine-tuning of foundation models | Hidden test set; subqueries; NC-PC cells |
| Generalization to other systems, vendors, domains | Hardware and index variety is the study object; AVX2 in the appendix | One library (libspatialindex), 2-D only; not flagged | Generators from three vendors claimed as coverage | Threat (iii): other domains untested; consistency across 6 datasets as evidence | BIRD only; suitability for private evaluation asserted, not tested |
| Bugs, reruns, process problems | — | Qd-tree non-convergence (training logs plus [10]); ZM-index lacks kNN | API failures, success rate above 85% | — | 7/58 intent losses; manual failure attribution |
| Human study not done | n/a | n/a | No human evaluation or judge agreement; not mentioned | n/a | Only a "lightweight" check of 58 pairs; annotator count not given |

---

## 3. Cross-paper observations

| Observation | Count | Papers |
|---|---|---|
| Abstract states a negative finding about the benchmark itself | **0 / 5** | — |
| Conclusion states a limit of the benchmark itself | **0 / 5** | — |
| Abstract states method negatives (the EAB contribution) | 4 / 5 | DCO, RLESI, TSF, SQLM (the XRAG abstract is descriptive only) |
| Conclusion restates method negatives | 3 / 5 | DCO, RLESI, TSF |
| Dedicated "Threats to Validity" or limitations section about the benchmark | **1 / 5**: about 5 sentences (≈110 words), 4 items, at the end of the Discussion | TSF |
| Section heading containing "Limitations" | 2 / 5, **both about the evaluated methods** | DCO (V-G "Merits, and Limitations"), RLESI (VI "Insights and Limitations") |
| The word "limitation(s)" used about the authors' own benchmark | **0 / 5** | — |
| The same word used about prior evaluations or evaluated methods | 4 / 5 | DCO, RLESI, XRAG, SQLM (TSF uses "acknowledged but unmitigated" for prior benchmarks) |
| Deficit words (limited, restricted, insufficient, narrow) about the authors' own benchmark | 1 occurrence in the whole corpus | RLESI: the tuning grid, in a concessive clause |
| Introduction or contribution list states a benchmark limit | 2 / 5, 1 sentence each, both as scope or criterion | RLESI (open-source criterion), SQLM (offline-use scope) |
| Benchmark limits stated in the setup section | 5 / 5 | all |
| Benchmark limits stated in the result section that they affect | 5 / 5 | all |
| Exclusions stated with a one-clause technical reason | 5 / 5 | all (e.g., DCO deletions, RLESI LMSFC, XRAG demo, TSF ARIMA, SQLM subqueries) |
| Reduction driven by cost or space, with the reason stated | 4 / 5 | XRAG (token cost, twice), RLESI (tuning hours, sample cap, space), DCO (page limits), SQLM (cost-conscious defaults) |
| A limit followed by a mitigation or counter-evidence in the same or next sentence | 5 / 5, in at least one place each; TSF in every place | all |
| Headline checked against another metric or aggregation, or a control experiment | 3 / 5 | TSF (median vs mean, ΔMSE vs r), SQLM (context-fixed control), DCO (indexes re-evaluated with a fixed query method) |
| Repetitions or variance reported | 1 / 5 | XRAG |
| Number of runs not stated | 4 / 5 | DCO, RLESI, TSF, SQLM |
| Single testbed, single generator or single judge flagged as a threat | **0 / 5**, although present in DCO, RLESI (single machine), SQLM (single LLM), XRAG (single judge) | — |
| Synthetic or constructed data justified | 4 / 5 | DCO (real provenance), RLESI (precedent), TSF (threat plus precedent), SQLM (execution validity plus human check) |
| Reliability of an automatic metric or LLM judge discussed | 3 / 5 | XRAG, TSF, SQLM |
| Human check of the authors' own generated data | 1 / 5 (58 pairs) | SQLM |
| Absence of a human study mentioned | 0 / 5 | — |
| Process problem disclosed | 3 / 5, each with an evidence source or a bound | RLESI, XRAG, SQLM |
| "bug", "rerun", "mistake", "flaw", "unfortunately" used anywhere | **0 / 5** | — |
| Paragraph anticipating a reviewer objection | 1 / 5 | TSF (Goodhart) |
| Not-done benchmark item turned into future work | 2 / 5 | XRAG (conclusion, 3 items), TSF (compositional sweeps, field validation) |
| Future directions for the evaluated methods | 2 / 5 | DCO (4 items), RLESI (2 plus their own fix) |
| Pointer to a full version or supplementary material for omitted results | 2 / 5 | DCO, RLESI |
| "fail" applied to evaluated methods | 5 / 5 | all |
| "only" applied to evaluated methods' wins | 2 / 5 | DCO ("only 4 out of the 14"), RLESI ("can only outperform ... on AUS") |

**Typical length**
- One benchmark limit takes 1–3 sentences and appears once, at the setup or result passage it affects.
- Per paper, benchmark limits total about 18–36 sentences spread over 10–16 places. That is roughly 1–2% of a 12-page paper per place.
- The single dedicated block (TSF) is about 5 sentences.

**Vocabulary used about the authors' own benchmark choices:**
- for a fair comparison
- representative
- we focus on / not our primary concern / not the focus
- core protocol
- cost-conscious choice
- pilot study
- for brevity
- for now
- remain untested
- unlikely to reverse
- plausible
- likely due to

**Never seen about the authors' own benchmark:**
- limitation (as a noun for their own work)
- weakness
- flaw
- bug
- mistake
- unfortunately
- we could not
- insufficient
- small sample
- "only N" models or datasets

---

## 4. Where EAB papers differ from the algorithm-paper guide

| Dimension | Algorithm papers (10, `limitations-writing.md`) | EAB papers (5, this file) |
|---|---|---|
| Negatives in the abstract | 0/10 state a loss | Method negatives in 4/5; they are the headline. Benchmark negatives in 0/5 |
| "Limitations" or failure heading | 0/10 | 2/5, about the evaluated methods; 1/5 "Threats to Validity" about the benchmark itself |
| "fail" and "only" | Never about the authors' own method | Freely about the evaluated methods (5/5 and 2/5); never about the authors' own benchmark |
| Mechanism after a negative | 9/10 | Every method negative gets a mechanism sentence in all 5 (e.g., O(D²) query pre-processing, packed-leaf splits, learned priors, recall drop in schema retrieval) |
| Conclusion | Folds scope into the headline; no losses | Restates method negatives (3/5); no benchmark limits (0/5) |
| Future work | 1/10, hedged | 4/5 have a forward list. Two lists are for the methods (DCO, RLESI); two are for the benchmark (XRAG, TSF) |
| What has to be defended | The authors' method's losing cells | The benchmark's validity: representative data, fair configuration, metric artefacts, judge reliability, coverage of excluded settings |
| Main presentation risk | Self-negation about the authors' own method | A reviewer applying the paper's own gap criteria (the "Ours" row) to the paper's own setup |

**Consequence.** For an EAB paper, the algorithm guide's rules R1–R4 and R8 (scope qualifiers, state each negative once, the fact → mechanism → regime → bound order, calibrated wording) apply to the **benchmark limits**. They do **not** apply to the method negatives, which an EAB paper states openly in the abstract, the takeaways and the conclusion. The four-step order (R4) still applies to method negatives.

---

## 5. Writing rules for EAB papers

Each rule keeps every measured number and every validity fact. "Supported by" lists the papers that show the pattern.

**E1. Keep two registers apart.**
- Method negatives are the contribution. State them with numbers in the abstract, the introduction's findings list, the takeaways and the conclusion.
- Benchmark limits never go in the abstract or the conclusion.

*Supported by: DCO, RLESI, TSF, SQLM (method negatives in the abstract, 4/5). The 0/5 counts for benchmark limits in the abstract and conclusion hold across all five.*

**E2. Point deficit vocabulary outward; describe your own choices with scope and design vocabulary.**
- "limited", "restricted", "narrow", "insufficient" and the heading "Limitations" are for prior evaluations and evaluated methods.
- For your own choices, write "we focus on X because ...", "not our primary concern", "a cost-conscious choice rather than a universally optimal setting", "the core protocol".
- If a section must be titled "Limitations", give it to the evaluated methods, as DCO and RLESI do. Title the one about your benchmark "Threats to Validity", as TSF does.

*Supported by: all five. "limitation" about the authors' own benchmark appears 0/5 times; "limited" appears once, in a concessive clause (RLESI).*

**E3. Give every exclusion a one-clause technical reason, at the point where it applies.**
- Tie the reason to a property of the evaluated object or the platform rather than to your resources. Examples from the corpus:
  - deletion logic is independent of the operator;
  - an index lacks native GPU support;
  - a method has no public code;
  - per-series fitting is impractical at 321 channels;
  - subqueries are left out to keep mutation effects interpretable.
- Do not collect exclusions in a list at the end.

*Supported by: DCO (V-D, V-E, V-F), RLESI (II, III-C), TSF (VI-F), SQLM (VI-C.1, IV-F.3), XRAG (footnote 2).*

**E4. When resources forced a reduction, state the cost number once and pair it with what preserves validity in the same sentence.**
- Examples:
  - subsampled to save tokens, using sampling-based averaging;
  - LLM-judge metrics as a pilot;
  - repeated three times with standard deviations;
  - tuning time of more than 30 h per index stated, then omitted from the figure;
  - full results in the extended version.
- Do not repeat the reduction in the takeaways or the conclusion.

*Supported by: XRAG (III-C, IV), RLESI (O15, O20), DCO (V intro), SQLM (III).*

**E5. Apply your own gap criteria to yourself.**
- Every deficiency you charge prior evaluations with must be covered by your setup, as in DCO's Table I "Ours" row. Otherwise, name it in a threats item.
- Counter-example in the corpus: DCO criticises prior work for disabling SIMD as not reflecting modern servers. Yet DCO runs single-threaded with sequential batches and justifies this only in one appendix sentence. That is the kind of point a reviewer turns around.

*Supported by:*
- *DCO (Table I covers all four prior-work gaps);*
- *RLESI (tuning answers its own "fixed parameters" criticism);*
- *SQLM (fixed prompts and seeds answer its own reproducibility criticism);*
- *TSF (evaluation-time synthesis answers the contamination problem it raises).*

**E6. If you add a threats section, keep it to about four one-sentence items at the end of the Discussion.**
- Each item reads: threat, then counter-evidence that is already measured in the paper, or a bounded scope.
- Example pattern: "constructed faults → grounded in documented failures; field validation is future work".
- Example pattern: "fixed weights → difficulty is monotone and ρ≈0.03, so reweighting cannot plausibly restore the ranking".
- The section is optional (4/5 accepted papers have none). What every paper does is handle limits in place (E3, E4).

*Supported by: TSF (VII-D, ≈110 words); the absence in DCO, RLESI, XRAG and SQLM.*

**E7. Put a robustness check right next to the headline, and say the verdict does not change.**
- Report an alternative metric or aggregation (median vs mean, absolute vs ratio).
- Or run a control experiment that fixes the suspected confound.
- Then state the result as "both orderings deliver the same verdict" or "not an artifact of dividing by a small clean error".

*Supported by: TSF (VI-A, VI-D), SQLM (IV-F.3 control experiment), DCO (Fig. 10, indexes re-evaluated with a fixed query method).*

**E8. Report the quality of your own generated data, metrics and judges with exact counts, in the section that builds them.**
- Order: positive count first, then the residual, then the remedy.
- Examples: 43/58 aligned, 8/58 add noise, 7/58 lose intent; judge API success above 85% shown per metric; one judge metric flagged as unsuitable for general use.
- Two items are missing in the corpus and a reviewer can ask for them:
  - agreement between the judge and humans (XRAG);
  - the number of annotators (SQLM).
  Report both.

*Supported by: SQLM (IV-F.1), XRAG (V-B, Tables IX–X), TSF (V-D ratio artefact).*

**E9. State process problems as observed facts, with their evidence source and a corroboration or bound.**
- Name where the evidence comes from: training logs, a measured success rate, manual inspection.
- Give a corroboration (another paper reports the same) or a bound.
- Attribute the problem to the evaluated object or the general practice when the evidence supports that, as with non-convergence of a method's RL model or API failures common to LLM testing.
- The corpus never uses "bug", "rerun", "mistake" or "unfortunately".

*Supported by: RLESI (O1), XRAG (V-B, footnote 8), SQLM (IV-F.1, IV-F.3).*

**E10. Turn not-done extensions into a named boundary of the core protocol, or into a short benchmark roadmap.**
- Option 1, in the body, placed right after you show the capability: "single-mode evaluation is the core protocol; compositional sweeps are future work".
- Option 2, at most one short list in the conclusion: training support, more task types, robustness to dirty queries.
- Never present these items as deficits.

*Supported by: TSF (IV-E, VII-D(i)), XRAG (Table II caption, VII), DCO and RLESI (forward lists for the methods).*

**E11. Name the strongest structural objection to the benchmark design in its own Discussion paragraph, and answer it with a design property.**
- Example: exposed parameters invite gaming. Answer: held-out parameter combinations, with the ImageNet-C precedent.
- Example: pretraining contamination. Answer: evaluation-time synthesis.
- Example: LLM-generated variants hallucinate. Answer: deterministic expansion, with the LLM used only for the final rewrite.
- The answer must rest on something the benchmark does, not on rhetoric.

*Supported by: TSF (VII-B, II-B), SQLM (IV-B design principles).*

**E12. Hedge causes, never measurements; state a null result on your own artefact plainly, then say what it adds.**
- Write "a plausible mechanism", "likely due to", "possibly attributable" for explanations.
- Give numbers without hedging.
- If your new metric leaves the leaderboard order unchanged, say so in one sentence, then give the added resolution in numbers. SQLM's example: recovered-cell shares of 15–25% on the 410 queries all three systems fail.

*Supported by: TSF (VI-D), RLESI (O20), XRAG (footnote 8), SQLM (IV-F.3, VI-C.2).*

---

## Checklist before submission (EAB)

- [ ] The abstract and the conclusion contain method negatives with numbers, and no benchmark limits.
- [ ] No sentence calls your own benchmark "limited", "restricted" or "insufficient", or uses "limitation" for it. Scope and design wording is used instead.
- [ ] Every excluded method, setting, dataset or metric has a one-clause technical reason at the point where it applies.
- [ ] Every cost-driven reduction states the cost once and names what preserves validity in the same sentence.
- [ ] Each gap you charge prior work with (your Table I) is either covered by your setup or named in a threats item.
- [ ] Protocol facts a reviewer needs are present once in the setup: number of runs or seeds, sample size per configuration, judge model(s), hardware, model versions. Four of five accepted papers omit the run count; do not copy that.
- [ ] Any generated data or LLM judge has a quality figure with exact counts. If possible, add human agreement and the number of annotators.
- [ ] The headline result carries a robustness check (alternative aggregation or control experiment), placed next to it.
- [ ] Optional threats section: at most about 4 one-sentence items, each paired with counter-evidence already in the paper, at the end of the Discussion.
- [ ] The words "bug", "mistake", "unfortunately", "flaw" and "weakness" do not appear about your own benchmark.
- [ ] Headline numbers in the abstract and introduction match the tables. SQLM's "up to 17%" against −23.9 in Table VII shows that accepted papers can slip here; a reviewer reading a text that contradicts its own table is the most common rejection trigger noted in the algorithm guide.

---

# Part B. Four more accepted papers on LLMs over data (HCT-QA, CITBench, RDL-Bench, Text2VectorSQL)

Read in full on 2026-11-06 from arXiv. Combined with Part A (nine papers): a dedicated threats/limitations section about the benchmark itself appears in 1/9; "limitation" is used for the authors' own benchmark in 0/9; a benchmark limit is stated in the abstract or conclusion in 0/9 (one partial, framed as a finding); a validity threat is turned into a measured RQ, metric, control experiment or finding in 7/9.

Evidence file. It records what four accepted ICDE papers do. It does not give advice for any one submission. All quotes are 12 words or fewer and come from the arXiv versions listed below. Those versions may differ from the camera-ready.

## B.0. Papers

| # | Title | Venue / year | Track evidence | Full text read |
|---|---|---|---|---|
| H | HCT-QA: A Benchmark for Question Answering on Human-Centric Tables | ICDE 2026 | Listed with the "[Experiment, Analysis, and Benchmark]" tag in the local ICDE 2026 list (icde2026_github_io_accepted-papers_html.html.txt, l. 4253). The arXiv v3 title carries the same tag. | https://arxiv.org/abs/2504.20047 (v3, 5 Mar 2026; 34 pp. including appendix A–L) |
| C | CITBench: A Comprehensive Benchmark for Interactive Tabular Data Processing with LLMs | ICDE 2027 | In the local ICDE 2027 list (accepted-papers.html.txt, l. 1678) with no tag there. The arXiv v1 PDF header reads "[Experiment, Analysis, and Benchmark]". | https://arxiv.org/abs/2608.00018 (v1, 29 Jun 2026; 14 pp.) |
| R | RDL-Bench: A Benchmark for Task-Aware Question Answering over Relational Databases | ICDE 2027 | In the local ICDE 2027 list (l. 936) with no tag. The arXiv comment says "accepted by ICDE 2027". The paper is a benchmark by title and content (dataset, two-level protocol, 4 RQs). | https://arxiv.org/abs/2610.21382 (v1, 15 Oct 2026; 13 pp.) |
| T | Text2VectorSQL: Towards a Unified Interface for Vector Search and SQL Queries | ICDE 2026 | In the local ICDE 2026 list (l. 1942) with no tag. Mixed contribution: a task, a training-data pipeline, a benchmark (VectorSQLBench, 2,997 samples, new metrics) and fine-tuned models. **This is the weakest track fit of the four.** | https://arxiv.org/abs/2506.23071 (v2, 6 Nov 2025; 13 pp.) |

**How the papers were selected.**

- The excluded papers named in the brief were skipped: DCOs, RL spatial indices, XRAG, TS-Fault and SQLMorph.
- Several in-scope candidates had no public full text that could be found, either through the arXiv API (title and author search) or through web search. These were SemQueryBench (EAB, 2027), Revisiting Single-Table Retrieval (EAB, 2026), MM2SQL (2026) and Text-to-RLS (2027).
- FusionSQL ("An Efficient and Effective Evaluator for Text2SQL Models...", 2026, arXiv 2603.07841) was downloaded and then rejected, because it proposes a method rather than a benchmark.
- The ICDE 2025 list contains no LLM benchmark paper in scope.
- No paper on LLM security or access control with a public full text was found in the three lists. All four papers chosen are Text-to-SQL or LLM-over-tables benchmarks.

Abbreviations used below: "Sent." is the approximate number of sentences in a statement. "Abs/Intro/Contrib/Setup/Res/Concl/App/FN/TN" mean abstract, introduction, contributions, setup, result sections, conclusion, appendix, footnote and table note.

---

## B.1. HCT-QA (H)

### 1.1 Inventory of limitation, scope and not-done statements

| # | Section | Sent. | Quote (≤12 words) | Paraphrase |
|---|---|---|---|---|
| H1 | Setup (III-A, HCT properties) | 2 | "we focus on common structural patterns and exclude HCTs exhibiting rare" | Nested tables and other irregular layouts are left out, framed as "outliers". |
| H2 | Setup (III-A, extraction) | 2 | "The verified sample demonstrated 100% accuracy." | The extraction tool was checked on a 10% sample only. The claim is phrased as a result. |
| H3 | Setup (III-B) | 1 | "Our focus is on single-HCT questions." | No questions span more than one table. |
| H4 | Setup (III-B) | 1 | "These properties are only provided for the manually-generated questions." | Question metadata covers only 3,248 of 9,835 real QA pairs. |
| H5 | Setup (III-B, model-generated QA) | 2 | "only 4% of model-generated questions were marked as nonsensical" | Of the GPT-generated questions, 24% were ambiguous, and about 50% of the answers needed correction. This sits in a paragraph that calls the pipeline "highly effective and scalable". |
| H6 | Setup (IV-A, generator) | 2 | "The remaining 4 properties are not supported in this version" | The synthetic generator covers 15 of 19 table properties. The reason given is "complex irregularities". |
| H7 | Setup (V intro) | 1 | "our evaluation focus on LLMs and VLMs" | The benchmark is said to suit other engines, but only LLMs and VLMs are tested. |
| H8 | Setup (V-A, prompting) | 2 | "no clear indication that the latter improved model performance" | 1-shot prompting was dropped. App I shows the test used 1,000 queries and 2 small models. |
| H9 | TN (Table IV) | 1 | "ChatGPT-4o Vision was not run on synthetic HCT images" | A cell is missing, attributed to "API constraints". |
| H10 | Res (RQ2) | 2 | "we cannot say that newer versions of models outperform" | The lack of a trend across model generations is reported as a finding. |
| H11 | Concl (Future Work) | ~9 (3 paragraphs) | "Initial experiments with two medium-sized LLMs indicate" | The authors plan cross-HCT joins, CUBE/PIVOT, paraphrase diversity and other systems. A pilot says models cannot handle the OLAP operators yet. |
| H12 | App B | 2 | "we could have captured the properties at a more coarse" | The granularity of the metadata is justified as a design choice. |
| H13 | App H (RQ8) | 3 | "no clear correlation between answer length and recall" | Recall inflation by verbose answers is tested as an RQ and rejected. |
| H14 | App J | 4 | "Since running an LLM-as-a-Judge is expensive" | A Llama-3-70B judge was compared with the CC score on 500 pairs, with agreement shown only as a figure ("closely align"). The judge was not adopted, for cost reasons. |
| H15 | Related work | 1 | "22% of the ground-truth answers were incorrect" | A quality audit of the closest prior benchmark (HiTab, 206 samples). It points outward, not at HCT-QA. |

### 1.2 Handling by threat type

- **Few models or single run.** 25 LLMs and 9 VLMs. Temperature 0, one run, no variance reported, no comment on it.
- **Closed-model version drift.** Not mentioned. Models are named "ChatGPT 4o" and "ChatGPT 4.1" with no snapshot dates. RQ2 compares model generations, which is a different question from API drift.
- **Synthetic or small data.** The synthetic part (67.7K QA pairs) is presented as a contribution. It is validated by fine-tuning on synthetic data and testing on real HCTs and on HiTab, with a +12 pp gain on real data from synthetic training. The lower CC score on synthetic data is explained as a property of the data: answers contain more values.
- **LLM-as-judge or metric reliability.** Rule-based metrics (F1 and CC). The LLM-judge check is in the appendix only, with a qualitative agreement claim. Verbosity inflation is tested (RQ8, appendix).
- **Small scale.** The 1-shot test (1,000 queries, 2 models) and the 10% extraction check are stated as procedures, not as limits.
- **Settings not evaluated.** Single-HCT questions, rare layouts, 4 properties and non-LLM engines are all stated as scope (H1, H3, H6, H7). OLAP operators and joins are routed to future work (H11).
- **Generalization.** One out-of-domain test (HiTab, +8 pp after fine-tuning).
- **Bugs or process problems.** Generator error rates are quantified (H5) and presented as evidence for the verification pipeline. One annotator was replaced after failing hidden checks. Internal mismatch visible in the text: the body fine-tunes Llama-3.1-8B for 2 epochs, while App L lists Meta-Llama-3-8B and FanarC-9B at 1 epoch.
- **No human study.** There is no human-performance baseline and the paper does not raise the point. Human annotation is described in detail (14 annotators, two-way verification, about 1,170 manual work hours), but no inter-annotator agreement statistic is given.

### 1.3 Framing devices

- **Dedicated Limitations or Threats section:** none. A "Future Work" paragraph block inside the Conclusion covers about 9 sentences.
- **Limits written as scope:** "we focus on", "our focus is", "in this version", "only provided for".
- **Limits written as findings or RQs:** RQ2 (no trend across generations) and RQ8 (verbosity).
- **Mitigation placed next to the limit:** model-generated QA is followed by the human-verification pipeline (H5). The 10% extraction check comes with its 100% result (H2).
- **Placement:** two limits sit in a table note and in the appendix (H9, H14).
- **Words used:** "focus", "exclude", "outliers", "not supported in this version", "initial experiments". The word "limitation" is used only for prior systems and benchmarks ("existing limitations of these systems", "suffers from key limitations"). Never used: "threat", "bias" (about its own data), "limitation" (about itself).
- **Absolute wording:** "Guaranteed semantic correctness" (generator property 2), "with 100% accuracy" (synthetic QA). The synthetic case is true by construction: ground truth comes from executing SQL on the relational source.

### 1.4 Negative finding about the benchmark itself in the abstract or conclusion

None. The abstract and conclusion state limits of the models only ("continue to face challenges with complex queries").

---

## B.2. CITBench (C)

### 2.1 Inventory

| # | Section | Sent. | Quote (≤12 words) | Paraphrase |
|---|---|---|---|---|
| C1 | Abs | 1 (clause) | "capturing key potential behavioral characteristics of user-in-the-loop" | The hedge word "potential" quietly marks the simulator as approximate. |
| C2 | Intro / III-C | 1 + ~4 | "Informed by our controlled user study of 10 participants" | The simulator is grounded in a study of n=10. The paper gives qualitative noise profiles but no counts or agreement figures. |
| C3 | IV-A (generation) | 1 | "instantiated via Claude-Sonnet-4.5" | Tasks and reference code are LLM-generated. Claude-Sonnet-4.5 is also the top offline model (overall P̄ 70.33), and the paper does not discuss this. |
| C4 | IV-B a) consensus filter | ~5 | "representativeness bias is completely averted" | A task is kept only if more than 1/3 of 6 solver models agree and at least one fails. The circularity (several of these solvers are also evaluated) is answered with an argument, not data. |
| C5 | IV-B a) / c) | 1 + 1 | "rejections stem entirely from minor instruction-level layout or description ambiguities" | Excluded tasks are said to reflect wording ambiguity, not capability gaps. No counts are given. |
| C6 | IV-B c) | 1 | "to guarantee 100% ground-truth target precision" | Human validation by 3 graduate students in two passes. |
| C7 | IV-C b) | 1 | "uncontrollable, non-reproducible generative user agents" | A rule-based simulator is chosen over LLM user agents, framed as a design choice. |
| C8 | V-A b) | 1 | "from K independent inference trials to mitigate stochasticity" | Run variance becomes a metric (Unreliability U = max − min). K is never given. |
| C9 | V-A c) | 1 | "completely excluded from performance degradation tracking" | API timeouts were retried and excluded. No rate is reported. |
| C10 | V-A c) | 1 | "sequences are configured to 5–8 conversational rounds" | The horizon is capped "to prevent baseline context saturation", framed as a design choice. |
| C11 | V-A c) | 1 | "Due to computational overhead constraints, experiments systematically sample a 50% balanced slice" | Only 50% of offline tasks and 25% of online sequences are evaluated. |
| C12 | V-B | 1 | "ground-truth matrix benchmarks remain mathematically unassailable" | The ground-truth claim rests on the human protocol. |
| C13 | Concl | 1 | "simulating potential user interaction characteristics" | The hedge is repeated in the conclusion. |

### 2.2 Handling by threat type

- **Few models or single run.** 12 base models are listed in the setup and in Table III, plus 5 agent frameworks on 2 backbones. The abstract and introduction say 13. T = 1.0 with K trials; spread is reported as U, which turns variance into a measured dimension.
- **Version drift.** Not mentioned. No snapshot dates.
- **Synthetic or small data.** All tasks are LLM-synthesized over 50 public datasets. Synthesis is defended by consensus filtering and human validation (C4–C6). Absolute wording replaces measured error rates.
- **LLM-as-judge or metric reliability.** No judge. Cell-matrix comparison against locked ground truth; a shape mismatch scores 0.
- **Small scale.** The 50%/25% sampling is stated in one sentence with its reason (C11). n=10 user study.
- **Settings not evaluated.** Round cap and fixed noise profiles, framed as design (C7, C10).
- **Generalization.** Breadth is asserted: 10 domains, 4 table-size regimes.
- **Bugs or process problems.** Excluded tasks and API exceptions are explained away (C5, C9). Visible mismatch: 13 vs 12 models.
- **No human study.** The user study informs the simulator. The simulator itself is not checked against human sessions, and the paper does not say so.

### 2.3 Framing devices

- **Dedicated section:** none. The Discussion (§V-D, four "Challenges") is about model weaknesses, not benchmark weaknesses.
- **Design-choice framing:** every limit is presented as a design rule with its rationale (C7, C10, C4).
- **Threat turned into a metric:** stochasticity becomes U (C8).
- **Hedge words** for realism appear only in the abstract and conclusion ("potential", "simulated", "simulating").
- **Strongest absolute vocabulary** of the four: "completely averted", "guarantee 100%", "mathematically unassailable", "stem entirely from", "eliminate ... bias". "Limitation" is used only for models ("critical limitations in current models").

### 2.4 Negative finding about the benchmark in the abstract or conclusion

None.

---

## B.3. RDL-Bench (R)

### 3.1 Inventory

| # | Section | Sent. | Quote (≤12 words) | Paraphrase |
|---|---|---|---|---|
| R1 | Abs + Contrib (Key Findings) + Concl | 1 each | "binary predictive QA overestimates LLM relational understanding" | A finding about an evaluation format that also covers the paper's own Boolean subset. It is used to justify the scalar-regression tasks. |
| R2 | III-A, IV-E | 1 each | "This separation prevents temporal leakage." | The leakage threat is named and closed by design (a "causal wall" at the reference time). |
| R3 | IV-F | 2 | "One database researcher manually inspects every candidate instance" | Single-reviewer validation, stated plainly. |
| R4 | IV-F | 1 | "Manual verification resulted in the revision or removal of 382 instances." | The curation loss is quantified (382 against 4,040 kept). |
| R5 | FN 1 | 1 | "The hepatitis domain contains no prediction-oriented instances" | A coverage gap, explained by missing timestamps. |
| R6 | V-A (baselines) | 1 | "spanning a wide capability range" | Only 3 LLMs (Claude Sonnet 4.6, Qwen2.5-32B, Llama-3.1-8B), defended as representative. |
| R7 | V-A (baselines) | 1 (clause) | "on Olist, NCAA, Financial, and Hepatitis" | CHESS and XiYanSQL-32B were run on 4 of 7 domains, with no reason given. Table IV nonetheless prints 7 domain values and an average for both. |
| R8 | V-A (implementation) | 1 | "responses that fail to parse default to the Reasoning Track" | A rule for router failures. The rate is not reported. |
| R9 | V-A (environment) | 1 | "All results are averaged over five independent runs with different seeds." | ± is shown only for trained models. LLMs use deterministic decoding. |
| R10 | V-A (metrics) | 2 | "This aggregation summarizes workload performance, while the underlying metrics measure" | A caveat on averaging different metrics. A per-type table (Table V) follows. |
| R11 | V-A (metrics) | 1 | "LLM-based predictors output discrete Yes/No answers without calibrated confidence" | Explains why Accuracy is used instead of AUROC, as a design choice. |
| R12 | V-B (paragraph "Generator sensitivity") | 4 | "This preliminary two-domain comparison provides no evidence of" | Generator bias tested on 100 Qwen-generated questions in 2 domains. The hedge "preliminary" is explicit. |
| R13 | V-E (RQ4) | 1 + 3 | "Annotated difficulty is useful but not monotonic." | A negative finding about the benchmark's own difficulty labels, kept in the result section. |
| R14 | Concl | 5 | "a natural extension that RDL-Bench is designed to support" | Open problems are listed. Multi-turn QA is presented as supported by the design, not as missing. |

### 3.2 Handling by threat type

- **Few models or single run.** Few LLMs, justified by capability range (R6). Deterministic decoding for LLMs; 5 seeds with ± for trained models only (R9).
- **Version drift.** Not mentioned ("Claude Sonnet 4.6", no date).
- **Synthetic or small data.** Real databases, LLM-generated questions (Claude Sonnet 4.6). Validated by automatic checks and one reviewer (R3, R4). A generator-bias test was run (R12).
- **LLM-as-judge or metric reliability.** No judge. Type-aware denotation metrics with an explicit aggregation caveat (R10, R11).
- **Small scale.** The generator test is small and labeled "preliminary" (R12). The 4-domain subset for two baselines is unexplained (R7).
- **Settings not evaluated.** The Hepatitis predictive track (footnote), and multi-turn QA, which is routed to future work as a supported extension (R14).
- **Generalization.** 7 domains. RESDSQL's failure to transfer is reported as a finding.
- **Bugs or process problems.** The curation loss is quantified (R4). The 4-vs-7-domain mismatch between text and Table IV is visible.
- **No human study.** None, and not raised. No inter-annotator agreement (a single reviewer).

### 3.3 Framing devices

- **Dedicated section:** none. "Conclusion and Future Work" holds a 5-sentence open-problems paragraph.
- **Bold-lead paragraphs** ("Generator sensitivity.", "Finding.") make validity checks look like results.
- **The most hedged wording of the four:** "preliminary", "no evidence of", "useful but not monotonic", "far from saturated". "Limitation" is used only for methods ("characterizes their cross-domain limitations").
- **Threats turned into findings:** binary-format overestimation (R1) and the routing gap measured against an Oracle-Router upper bound.

### 3.4 Negative finding about the benchmark in the abstract or conclusion

**Partial (yes).** The abstract and conclusion state that Boolean predictive QA overestimates LLM understanding (R1). This applies to part of the benchmark's own task design, but it is framed as a finding about the format and motivates the paper's scalar tasks. The negative finding about the difficulty labels (R13) appears in the body only.

---

## B.4. Text2VectorSQL (T)

### 4.1 Inventory

| # | Section | Sent. | Quote (≤12 words) | Paraphrase |
|---|---|---|---|---|
| T1 | III-A (DB sourcing) | 2 | "Real-world databases are scarce on the internet" | Synthesized databases are justified by data scarcity. |
| T2 | III-A (augmentation) | 1 | "generate plausible unstructured text conditioned on the existing structured data" | Unstructured content is partly LLM-written. This is not flagged as a threat. |
| T3 | III-B (ground truth) | 2 | "establishes an unbiased and comprehensive ground truth" | Ground truth is pre-filtering execution over the union of 5 SQL variants (RRF). |
| T4 | FN 5 | 2 | "post-filtering can be efficient and acceptable for vague queries" | The ground-truth convention is qualified in a footnote only. |
| T5 | III-B (annotation) | 1 | "annotators with expertise in both database systems and natural language processing" | The number of annotators and their agreement are not given. |
| T6 | III-B (annotation) | 1 | "Any sample that fails to execute is discarded." | The number discarded is not reported. |
| T7 | III-B (metrics) | 2 | "is brittle for vector search where approximate results" | A limit of the standard metric (EX) motivates the new metrics. |
| T8 | III-B (ACC_SQL) | 1 | "We use an LLM-based evaluator to parse the query" | LLM-judged skeleton accuracy. The evaluator model and its validation are not reported. |
| T9 | Fig. 3 caption | 1 (clause) | "while SQLite-vec does not so far" | SQLite has no ANN index, a backend capability gap stated in a caption. |
| T10 | IV-A (implementation) | 1 | "we kept default execution settings but set a 60s execution timeout" | Fixed embedding models and default engine settings. |
| T11 | IV-C a) | 2 | "indicating noticeable catastrophic forgetting of previously acquired SQL skills" | The released configuration (1:0) is the one showing forgetting (BIRD-dev 58.2 vs 63.9). The choice is justified by "our focus on establishing a robust baseline". |
| T12 | IV-C c) | 1 | "we evaluated three representative models" | The recall-degradation analysis uses 3 models on 2 backends. |

### 4.2 Handling by threat type

- **Few models or single run.** About 30 models. One run, decoding not stated, no variance.
- **Version drift.** Not mentioned. Closed models are named by family (Claude-3/4, GPT-4, Gemini-2.5, Grok-3/4).
- **Synthetic or small data.** Training and benchmark data are LLM-synthesized and then human-reviewed. Defended by the pipeline description (majority voting, RRF, expert review), not by error rates.
- **LLM-as-judge or metric reliability.** One LLM-judged metric, unvalidated (T8). A metric limit of prior work is turned into new metrics (T7).
- **Small scale.** The subset analysis (T12) is stated without a reason.
- **Settings not evaluated.** The post-filtering ground-truth convention is qualified in a footnote (T4). Embedding models are fixed.
- **Generalization.** Asserted through breadth: "To ensure robustness and generality", 3 backends × 4 sources.
- **Bugs or process problems.** Catastrophic forgetting is disclosed in an ablation (T11). Visible mismatch: the text gives a "91.8% success rate" for UniVectorSQL-7B, while Table II shows 91.0.
- **No human study.** None, and not raised.

### 4.3 Framing devices

- **Dedicated section:** none. The Conclusion has no future-work statement about the benchmark; only research directions for systems are mentioned.
- **The one benchmark caveat (T4) sits in a footnote.**
- **Limits written as challenges:** the system-level limit (post-filtering recall loss) is promoted to a headline "discovery".
- **Words:** "first", "gold standard", "unbiased", "guarantees", "principled". "Limitation" is used only for traditional Text-to-SQL and prior indexes.

### 4.4 Negative finding about the benchmark in the abstract or conclusion

None. The negative headline (recall degradation) concerns the systems' execution strategy, not the benchmark.

---

## B.5. Cross-paper observations (k/4)

| # | Observation | k/4 | Papers |
|---|---|---|---|
| O1 | Dedicated "Limitations" or "Threats to Validity" section | **0/4** | none |
| O2 | Future-work text about the benchmark's own scope in the conclusion | 2/4 | H (about 9 sentences), R (5 sentences) |
| O3 | The word "limitation(s)" applied to the paper's own work | **0/4** | none (H, C, R and T all apply it only to prior work or to the models tested) |
| O4 | The phrase "threat(s) to validity" | 0/4 | none |
| O5 | Scope stated as a design statement with a number or reason ("we focus on", "in this version", "N of M") | 4/4 | H1/H3/H6, C10, R5/R6, T4/T10 |
| O6 | At least one limit placed only in a footnote, table note, figure caption or appendix | 3/4 | H9 (table note), H14 (appendix); R5 (footnote); T4 (footnote), T9 (caption). C keeps all its limits in body paragraphs |
| O7 | Partial evaluation (subset of tasks, domains or models) disclosed | 4/4 | H8/H9, C11, R7, T12 |
| O7a | ...with a stated reason (compute or API) | 2/4 | H9 (API), C11 (compute) |
| O8 | Decoding setting declared for the LLMs | 3/4 | H (T=0), C (T=1.0), R (deterministic); T not stated |
| O9 | Run-to-run variance reported for the LLMs | 1/4 | C (U metric); R gives ± for trained models only |
| O10 | Closed-model snapshot dates or version drift addressed | **0/4** | none; all 4 name models without dates |
| O11 | Benchmark content generated by an LLM | 4/4 | H (GPT questions), C (Claude tasks), R (Claude questions), T (LLM SQL, questions and text) |
| O11a | Generator error or curation-loss rate quantified | 2/4 | H5 (4/24/72%, about 50% corrections), R4 (382 instances) |
| O11b | Generator bias tested with data | 1/4 | R12 (C4 argues without data) |
| O12 | Number of human validators stated | 3/4 | H (14 plus authors), C (3), R (1); T not stated |
| O13 | Inter-annotator agreement statistic | **0/4** | none |
| O14 | LLM-as-judge: used as a metric without validation / checked and not adopted | 1/4 / 1/4 | T8 / H14 |
| O15 | A validity threat converted into an RQ, metric or finding | **4/4** | H RQ2/RQ8, C U-metric, R generator test and Boolean-format finding, T EX → new metrics |
| O16 | Mitigation or check in the same paragraph as the limit | 4/4 | H2/H5, C4/C6, R2/R12, T3 |
| O17 | Small check explicitly hedged ("preliminary", "initial", n given) | 2/4 | R12, H11 |
| O18 | Absolute guarantee vocabulary about the paper's own data ("guarantee", "100%", "unbiased", "unassailable", "completely") | 3/4 | H, C, T (R uses hedged wording) |
| O19 | Hedge word on how realistic the simulation is ("potential", "simulated") in the abstract or conclusion | 1/4 | C1/C13 |
| O20 | Generality argued by enumerating breadth (domains, backends, sources) | 4/4 | H, C, R, T |
| O21 | Out-of-distribution test of the benchmark's usefulness | 2/4 | H (HiTab), R (cross-generator) |
| O22 | Absence of a human baseline or human study acknowledged | **0/4** | none (C has an n=10 user study, presented as grounding) |
| O23 | Quality audit of a competing benchmark used as motivation | 1/4 | H15 |
| O24 | Negative finding about the paper's own benchmark in the abstract or conclusion | **0/4 strict; 1/4 partial** | R1 (format-level, framed as a finding) |
| O25 | Negative finding about the paper's own benchmark anywhere in the body | 1/4 | R13 (difficulty labels not monotonic) |
| O26 | Visible internal mismatch in counts or configurations (abstract vs setup vs table vs appendix) | 4/4 | H (fine-tune configuration), C (13 vs 12 models), R (4 vs 7 domains), T (91.8 vs 91.0) |

Reading notes on the counts:

1. The four papers carry their limits **inside the method and setup text**, one or two sentences each, usually with the reason and the check in the same place. None groups them into a section.
2. Several items were **silent in all four** (O10, O13, O22). These papers were accepted anyway. That shows only that the silence was not fatal for these four papers; it does not show that reviewers ignore these points.
3. O26 is negative evidence: every paper has a mismatch a careful reviewer could spot. The papers were accepted, but nothing here suggests the mismatches helped.

## B.6. Writing rules (wording, placement and frequency only)

**Integrity boundary for every rule.** A rule may change *how* and *where* a limit is stated. It never removes a fact a reviewer needs to judge validity: subset sizes, single-reviewer validation, unvalidated judges, missing runs, excluded cells, generator identity, curation losses. If a fact affects a headline number, it stays in the main text next to that number. Moving it to an appendix alone does not satisfy the boundary.

1. **State each limit where the affected design decision is introduced, in one or two sentences, with its reason. A separate Limitations section is not needed in this corpus.** In all four papers, limits live in the setup, metric and construction paragraphs (O1 0/4; O5 4/4).
   *Supported by: H, C, R, T.*

2. **Write scope as a bounded design statement with a number, not as a deficiency.** Patterns: "we focus on X", "N of M properties are not supported in this version", "X is evaluated on k of n domains". Keep "limitation" for prior work and for the systems under test, as all four do (O3 0/4; O5 4/4).
   *Supported by: H (H1, H3, H6), R (R5, R6), T (T4), C (C10).*

3. **Put the check or mitigation in the same paragraph as the limit. If the check is small, say so with its size and a hedge word.** Example: "This preliminary two-domain comparison provides no evidence of..." (R12), or the 10% extraction sample reported with its result (H2) (O16 4/4; O17 2/4).
   *Supported by: R, H, T, C.*

4. **Turn a validity threat into something measured: an RQ, a metric or a finding.** Examples: verbosity inflation becomes RQ8 (H); stochasticity becomes the Unreliability metric (C); generator bias becomes a sensitivity test (R); an unsuitable metric (EX) becomes new metrics (T). This is the most frequent device in the corpus (O15 4/4).
   *Supported by: H, C, R, T.*

5. **Disclose every resource-driven subset once, with the fraction and the reason, in the setup or a table note.** Unexplained subsets are where the corpus shows text and table drifting apart: R7's 4-vs-7 domains, and T12 with no reason (O7 4/4; O7a 2/4).
   *Supported by: H (H9), C (C11); counter-examples R, T.*

6. **Report curation losses and generator error rates as quality-control evidence, with numbers.** Examples: "only 4% ... nonsensical", 24% ambiguous, about 50% answers corrected (H5); "revision or removal of 382 instances" (R4). The facts are kept in full and read as rigor rather than weakness (O11a 2/4). C and T give no rates and depend on absolute wording instead.
   *Supported by: H, R; contrast C, T.*

7. **Keep the abstract and conclusion for findings about the systems under test. A caveat about the benchmark itself surfaces there only when it is a finding in its own right.** Example: Boolean-format overestimation (R1). Body-level negatives about the paper's own artifact (R13) stay in the result sections (O24 0/4 strict, 1/4 partial).
   *Supported by: H, C, R, T.*
   *Boundary:* this describes where the four papers placed such statements. If a benchmark defect changes a headline number, that defect still belongs next to the number.

8. **Route unbuilt extensions to a future-work passage naming concrete operations, preferably with a pilot result or a statement that the design already supports them.** Examples: CUBE/PIVOT with "Initial experiments with two medium-sized LLMs..." (H11); "a natural extension that RDL-Bench is designed to support" (R14) (O2 2/4).
   *Supported by: H, R.*

9. **Use absolute wording ("guaranteed", "100%") only where the procedure enforces it by construction, and name that procedure in the same sentence.** H's synthetic ground truth, obtained by SQL execution, is a by-construction case. C's "mathematically unassailable" and T's "unbiased" rest on procedural arguments without measured error. R gets by with hedged wording throughout (O18 3/4 use absolutes; 1/4 does not).
   *Supported by: H (by construction), R (hedged alternative); C, T as the riskier pattern.*

10. **Keep every count and configuration identical across the abstract, setup, tables and appendix.** All four accepted papers contain a visible mismatch (O26 4/4): model count (C), domain coverage (R), fine-tuning configuration (H) and a success rate (T). This is a consistency check, not a framing device. It is listed because it is the cheapest error for a reviewer to find.
    *Supported by: H, C, R, T (negative evidence).*

## B.7. Caveats on this evidence

- The sample is four papers. Two are tagged EAB (H; C in its PDF header). R is an untagged benchmark paper. T is a mixed benchmark-plus-method paper.
- None of the four is about LLM security or access control. No in-scope paper on that topic had a public full text in the three lists.
- Counts refer to the arXiv versions read, which may differ from the camera-ready versions.
- Sentence counts are approximate and were made by reading, not by an automatic tool.
- Downloaded PDFs and extracted text are in /private/tmp/claude-501/-Users-loctek-Desktop-ICDE2027/0578ebb1-8b07-4af4-9a06-2987c25cf67d/scratchpad/eab_new/. That folder also holds the rejected FusionSQL text, 2603.07841.
