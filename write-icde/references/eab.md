# Writing an ICDE "Experiment, Analysis, and Benchmark" (EAB) paper

## Scope of this guide
This is the hub for EAB writing. It covers:
- titles and abstracts;
- how gaps, findings and lessons are framed;
- experiment design and reporting;
- figures, tables and references;
- above all, how accepted papers state the limits of their own study without undermining it.

## Evidence
Sixteen accepted papers, all read in full from public versions (arXiv HTML/LaTeX or PVLDB PDF) on
2026-11-06 or earlier.
- **Nine** are documented paper by paper in `limitations-writing-eab.md` (rules E1–E12 and B.1–B.10).
- **Seven** are added here (section 0). This file summarises only their per-paper records.

Counts such as "3/7" are observations, not venue rules. Wording in quotation marks is limited to short
functional phrases. Everything else is paraphrased.

Integrity boundary, the same as in `limitations-writing.md`:
- every measured number stays;
- no evaluated system is hidden;
- every fact a reviewer needs to judge validity stays in the paper, next to the number it affects: runs,
  models, judges, subsets, exclusions.

The patterns below change wording, placement and framing only.

## 0. Corpus

| Code | Paper | Venue / category as printed | Topic | Full text read |
|---|---|---|---|---|
| DCO, RLESI, XRAG, SQLM | Distance Comparison Operations Are Not Silver Bullets…; Benchmarking RL-Enhanced Spatial Indices…; XRAG; SQLMorph | ICDE 2026 EAB | vector search, spatial indexes, RAG, Text-to-SQL evaluation | `limitations-writing-eab.md` |
| TSF | TS-Fault: Benchmarking Time Series Forecasters Against Structural Faults | ICDE 2027 R1 EAB | forecasting robustness | idem |
| HCT, CIT, RDL, T2V | HCT-QA, CITBench, RDL-Bench, Text2VectorSQL | ICDE 2026–2027 (benchmark papers; HCT and CIT tagged) | LLMs over tables and databases | idem, Part B |
| **CDC** | Benchmarking Content-Defined Chunking Algorithms for Data Deduplication | ICDE 2027 R1, `[Experiment, Analysis, and Benchmark]` | storage, dedup | arXiv 2610.13704 (LaTeX); artifact github.com/mrd0ll4r/cdc-bench |
| **WPB** | WPBench: A Comprehensive Benchmark for Wind Power Forecasting | ICDE 2027 R1, untagged (regular track) | ML-for-data benchmark | arXiv 2609.24444 |
| **ER** | A Critical Re-evaluation of Benchmark Datasets for (Deep) Learning-Based Matching Algorithms | ICDE 2024 (no EAB category that year) | entity matching, ML-for-data | arXiv 2307.01231; Docker artifact |
| **SEM** | SemBench: A Benchmark for Semantic Query Processing Engines | PVLDB 19 (VLDB 2026), EA&B (tag on arXiv) | LLM semantic operators in SQL | arXiv 2511.01716 + PVLDB PDF; sembench.org |
| **UDA** | Unstructured Data Analysis Using LLMs: A Comprehensive Benchmark | PVLDB 19, "[Experiments & Analysis]" on arXiv v1 | LLM document analytics systems | PVLDB PDF + arXiv 2510.27119 v1 (pre-revision) |
| **N360** | The Dawn of Natural Language to SQL: Are We Fully Ready? (NL2SQL360) | PVLDB 17 (VLDB 2024); category tag not printed | Text-to-SQL evaluation | arXiv 2406.01265 |
| **LQO** | Is Your Learned Query Optimizer Behaving As You Expect? A Machine Learning Perspective | PVLDB 17, EA&B (VLDB 2024 programme) | learned query optimisers | arXiv 2309.01551; github.com/edualc/lqo_ml_perspective |

The 2027 R1 tagged papers "SemQueryBench" and "Pitfalls in Learned Indexes" had no public full text on
2026-11-06.

## 1. Titles

The seven new papers range from 8 to 13 words. Five patterns cover the sixteen papers:

| Pattern | Examples |
|---|---|
| `Name: A (Comprehensive) Benchmark for <object>` | SEM, WPB, UDA (no name), HCT, CIT, RDL |
| `Benchmarking <methods> (Against \| for) <condition>` | CDC, RLESI, TSF |
| Claim title that states the finding | DCO ("… Are Not Silver Bullets"), ER ("A Critical Re-evaluation of …") |
| Question title | LQO ("Is Your … Behaving As You Expect?"), N360 ("… Are We Fully Ready?") |
| `Name: <new evaluation method> for <task>` | SQLM ("Query Mutation and Fine-Grained Metrics …") |

- At ICDE the tag goes in front: `[Experiment, Analysis, and Benchmark] Benchmarking X for Y`. See
  `submit-icde/references/eab.md`.
- Choose a claim or question title when the headline finding overturns a belief. Choose
  `Benchmarking X for Y` or `Name: A Benchmark for Y` when the artefact itself is the contribution.
- Avoid superlatives in the title ("most comprehensive", "first"). WPB's "first/most comprehensive"
  claims sit in its contribution list. They are the claims a reviewer tests first.

## 2. Abstract (156–219 words in the new seven)

What the new seven do:
- context → gap → "we present / we build" → scale: 7/7.
- A numeric headline finding: 2/7 (CDC's parameter error of 13–39%; N360's accuracy numbers).
- Findings without numbers: SEM, UDA, LQO, ER. No finding at all: WPB.
- An availability sentence: 1/7. A limit of their own study: 1/7 (SEM's "snapshot" sentence).

The older nine are more assertive. 4/5 of the first five put method negatives with numbers in the
abstract.

Recommended moves (8–10 sentences):
1. The data-engineering object and why its evaluation matters, in one sentence.
2. The blind spot shared by existing evaluations, as one concrete assumption (DCO: SIMD off; ER: easy
   negatives; LQO: ML pipeline stages ignored; CDC: base algorithms conflated with techniques).
3. What you built, in numbers: methods × datasets × workloads × metrics (CDC: 8 × 4 × 4).
4. The design property that makes it different, such as controlled isolation, a new metric, fault
   injection, or interface-agnostic ground truth.
5–7. Two or three findings with numbers. Negatives about the evaluated methods belong here; they are
   the contribution. At least one finding should overturn or qualify a published claim.
8. One actionable recommendation or a decision rule.
9. Artifact availability (public URL).

What does not belong in the abstract:
- limits of your own benchmark (0/15 papers, except SEM);
- a "we also propose a new method" clause that turns the paper into a regular paper (N360's SuperSQL
  blurs the category).

## 3. Introduction: showing the gap

Devices seen:
- **A table of prior evaluations against criteria, with an "Ours" row**: DCO Table I, XRAG. WPB
  puts its check-mark matrix in Related Work.
  - Every criterion you charge prior work with must be met by your own setup (E5). Reviewers apply the
    table to you.
- **A subsection that lists the shortcomings of existing experiments**: N360 §2.2, three numbered
  shortcomings.
- **Stage-structured problem paragraphs.** LQO has five bold paragraphs, one per ML-pipeline stage,
  each ending in "Contribution: … Section X". WPB has four "Issue k" paragraphs, mapped one to one onto
  four contributions.
- **Figure 1 types**:
  - a measurement that breaks a belief (DCO, TSF);
  - a conceptual decomposition (CDC, which splits algorithms into building blocks; LQO, which shows
    the pipeline stages);
  - an issue diagram (WPB);
  - three early figures (N360).
- **A concrete failure example**: SEM's running SQL example; UDA's medical example; N360's
  "one size does not fit all" example.
- **Contributions**: 3–4 items (7/7), usually tied to sections. One item states the headline findings.

Recommended:
- Write the gap as a measured fact, not as an opinion. Prefer a Figure 1 that shows a ranking
  flipping when the missing factor is switched on.
- Then give RQ1–RQ4, and a findings list (F1–F5) that previews the answers with numbers.

## 4. Research questions, findings, takeaways and lessons

| Format | Papers | Count |
|---|---|---|
| Numbered, boxed "Finding n" right after each experiment | N360 (12 findings over Exp-1…Exp-9) | 1/7 |
| Labelled inline takeaways (Insight / Observation / Opportunity) | UDA (9, after 3 RQs) | 1/7 |
| "Key Takeaways" subsection closing each result section, plus a summary table | CDC | 1/7 |
| "Recommendation:" paragraphs, prescriptive and sometimes addressed to the reader | LQO (8) | 1/7 |
| A "lessons learned" paragraph with ordinal lessons for system builders | SEM (5) | 1/7 |
| Numbered observations in the conclusion plus numeric decision thresholds | ER | 1/7 |
| "Overall, …" synthesis sentence closing each subsection | WPB | 1/7 |
| RQs answered first, then evidence; boxed takeaways | TSF, DCO, XRAG, RLESI (older nine) | 4/9 |

How a good finding is written (paraphrased examples):
- **Claim + regime + number + mechanism.** CDC: raw dedup ratios reward algorithms that quietly emit
  tiny chunks; once metadata is charged, one algorithm gives the best and most stable trade-off.
- **Rule of thumb + cost.** N360: the cheaper model gives the best accuracy per dollar; self-consistency
  raises accuracy but lowers cost-effectiveness.
- **Prescription to builders.** SEM: engines should stop invoking semantic operators once a LIMIT is
  satisfied. LQO: future papers should include a simple covariate-shift experiment.
- **Decision threshold stated in advance.** ER: below a stated linearity or complexity score, a dataset
  counts as easy.

Recommended structure for ICDE (12 pages):
- RQ1–RQ4 in the introduction.
- One experiment subsection per RQ, each ending in a boxed finding of 1–2 sentences with a number.
- A final "Lessons and Recommendations" section, about 0.5 page, containing:
  - a decision figure or table: which method under which regime (DCO's recommendation figure; CDC's
    summary table with best and second best);
  - 3–5 research opportunities for the evaluated methods.

## 5. Experiment design and reporting

| Item | Seen in the new seven | Older nine | Recommended (exceed the norm; reviewers ask for it) |
|---|---|---|---|
| Hardware and software environment | 7/7 | most | CPU/GPU model, RAM, OS, compiler or framework versions, VM vs bare metal, NUMA and affinity (CDC discloses that there was no affinity control) |
| Repetitions stated | 3/7 (CDC n=10 + warm-up; SEM 5; LQO 3, the third run used) | 1/5 (XRAG 3) | ≥3 runs for timings, ≥3–5 for LLM outputs; state warm-up and cache state |
| Dispersion reported | 3/7 (CDC median+IQR with a skew rationale; SEM mean±std; LQO CIs) | 2/9 | std or IQR per cell, or error bars; say why median or mean |
| Claim rule or significance | SEM (a gap must exceed 3 std); LQO (Mann–Whitney U, with a footnote on why non-parametric) | TSF p-values | One stated rule for when a difference counts, e.g. non-overlapping 95% bootstrap CIs, or a paired test with Holm correction |
| Seeds | 0/7 | 1/9 (SQLM) | List the seeds in the artifact |
| Protocol validated by an experiment | LQO (a 50-repetition study justifies "3 runs, keep the 3rd"); ER (own vs published F1 per method) | DCO (control) | One small experiment that justifies each non-obvious protocol choice |
| Same backbone and pinned versions | SEM (one LLM for all systems; system versions pinned); N360 (similar-size LLMs) | XRAG T=0 | One shared backbone LLM; model identifier, access date, temperature, max tokens; prompts released |
| Temperature or decoding stated (LLM papers) | 1/3 (SEM) | 4/7 | Always |
| Cost | time 7/7; memory 4/7; $ in 2/3 LLM papers (SEM per query plus the total budget; N360 $ per query with dated prices); tokens 2/3 | most LLM papers | Report $ at list price with the price date, tokens in and out, latency, and the total experiment budget |
| Timeouts | SEM (1 h; a system that times out is not run at larger scales); LQO (counted, threshold not stated) | — | State the threshold and how timeouts enter the aggregates |
| Ground truth | UDA (30 annotators, 4,110 h, agreement on 191 documents of 0.88–0.98); others reuse labels | SQLM (58 checked) | When you create labels, report annotators, hours and agreement. When an LLM judge is used, report its agreement with humans on a sample |
| Fairness of configuration | 6/7: one framework (CDC, LQO, ER Docker); one tuning protocol (CDC calibrate-then-freeze; WPB Optuna then freeze); stated deviations from the original papers (LQO) | 5/5 | Use the same tuning budget for every method; report how the defaults were chosen; check against published numbers |
| Aggregation | WPB normalises scores by a naive baseline, then takes geometric means | — | Use the geometric mean for ratios; report absolute numbers as well as relative ones, and per-workload results (benchmarking-crimes B5, F3, F4) |

Inclusion criteria:
- Use explicit numbered criteria and name the well-known methods they exclude, with the reason: ER (4
  criteria, plus "despite contacting" the authors); LQO (RTOS, Lero and LOGER excluded, with reasons);
  N360 (unavailable code).
- Reimplemented closed systems carry one caveat sentence (UDA).

## 6. Figures and tables
- **Typical counts**: 7–15 figures and 2–9 tables (new seven).
- **Types that carry findings**:
  - multi-panel line plots with error bars (SEM scalability: time, cost, quality and memory per scenario);
  - Pareto scatters with non-dominated points ringed (CDC);
  - stacked bars that split planning, inference and execution (LQO);
  - dumbbells for low/high-quality groups (WPB);
  - per-feature grids (N360);
  - radar charts for coverage (WPB).
- **Summary table** with best in bold and second best underlined (CDC, WPB). Use one compact table per
  RQ rather than one giant per-query table. SEM's two-page per-query table works in PVLDB's 14 pages, but
  it is costly in ICDE's 12 pages, where no appendix is allowed.
- **Recommendation artefact**: a decision table or flowchart (DCO; CDC's summary table; ER's thresholds).
  None of the new seven has a decision tree. Adding one is a cheap way to show "usefulness".
- **Unsupported or inapplicable cells**: use "–" or "✗" with a legend (SEM, WPB, ER). Explain each kind
  once in the caption; the older corpus shows unexplained "Not Available" cells (RLESI).
- **IEEE layout**: one-column figures at 252 pt; legends never over data; captions self-contained. Run
  `manuscript-writing-review`.

## 7. References
- **Totals**: 31–104 in the new seven (CDC 57, LQO 44, WPB 104, ER 71, SEM 57, UDA about 31, N360 62).
- **Share of DB-venue references** (VLDB/SIGMOD/ICDE/CIDR): about 5–34%. arXiv share: 0–55% (UDA v1 is
  the extreme case).
- **ICDE desk-rejects papers that do not build on core-venue work.** Aim for at least 10 VLDB, SIGMOD or
  ICDE references:
  - prior benchmarks and evaluations in the same area;
  - the evaluated systems' own papers;
  - classical DB benchmarking work: TPC, and the DBTest paper on fair benchmarking pitfalls by
    Raasveldt et al., 2018.
- Replace arXiv entries with their published versions.
- Datasets and system versions may be cited as URLs with access dates.

## 8. Limitations and threats to validity without self-negation (the core of this guide)

### 8.1 What the sixteen accepted papers do

| Observation | Count |
|---|---|
| A limit of their own study in the abstract | **1/16** (SEM: results are a snapshot of fast-moving systems, paired with a living website) |
| A concession about their own study in the conclusion | **0/16**. A scope qualifier folded into the claim, or future work: CDC (claims scoped to the evaluated workloads and target range), ER (2 future-work sentences), SEM (a durability argument), TSF, XRAG, HCT, RDL |
| A dedicated, labelled block about their own study | **2/16**: TSF "Threats to Validity" (about 110 words, 4 items, end of Discussion); UDA run-in "Scope and Limitations" (about 105 words, end of Evaluation, added in the PVLDB revision) |
| The word "limitation" used about their own study | 1/16, and only as UDA's run-in heading. "Limitation(s)" is used about prior work or evaluated systems in nearly all papers |
| "flaw", "bug", "unfortunately", "mistake", "rerun" about their own study (final versions) | **0/16**. UDA's arXiv v1 had "Unfortunately"; the PVLDB version removed it |
| A validity threat answered by a measurement instead of a sentence (control experiment, sensitivity check, agreement study, reproduction check, new RQ or metric) | **12/16** |
| Limits stated where they apply, as one or two sentences with a reason | 16/16 |
| Total volume of self-limits | 6–15 sentences over 4–6 places (new seven); 18–36 sentences over 10–16 places (first five) |
| Exclusions with a one-clause technical reason | 16/16 |

### 8.2 Ten placement-and-wording patterns (paraphrased; with the papers that use them)

1. **Design choice with a reason, at the start of the methodology** (CDC, LQO, SEM).
   - State the isolating choice as the control that makes the comparison valid. Example: CDC compares
     base algorithms alone and tunes all of them to the same target on random data before freezing
     them.
   - Point forward to the Discussion for its consequences.
   - Shape: "To isolate X, we fix Y; Section Z discusses what this implies for W."
2. **Domain of validity, not deficiency** (CDC, ER, N360, WPB). Write the claim with its range: rankings
   hold for this hardware class and these implementations; chunk statistics do not depend on execution
   speed. Pair a threat with an **invariance argument** that shields the other metrics from it.
3. **"We do not claim X"** (CDC). Bound the headline discovery explicitly. CDC measures a size deviation
   and says it is not a bound on dedup gains. It states that it does not claim that earlier rankings
   reverse, because re-running those studies is outside its scope. This is the strongest
   self-limitation in the corpus, and it pre-empts the "over-generalisation" reviewer.
4. **Inclusion criteria with named exclusions** (ER, LQO, N360, DCO, RLESI). Use a numbered list of
   criteria, including a "Scope" item. Then name the famous methods that fail it and give the reason:
   no code, would require disabling parallelism, a service that is unavailable.
5. **Concede, then neutralise, in the same sentence** (LQO). Example: a training-time cap may
   disadvantage one optimiser, but its inference time dominates its end-to-end cost anyway.
6. **Reimplementation caveat that re-scopes the claim** (UDA). Results for re-implemented closed-source
   systems reflect their algorithmic design, not a final verdict on the original products.
7. **Snapshot with a versioned or living release** (SEM). Fast-moving systems are evaluated at pinned
   versions, and the artifact or leaderboard will be refreshed. This turns obsolescence into a feature.
   Use it once, in the setup or the introduction. At ICDE, keep it out of the abstract, because the
   conclusion and abstract carry findings.
8. **"Not a universal ranking"** (UDA). Results depend on the LLM and on prompting. The benchmark is a
   platform for comparing designs under controlled settings. Pair it with the controls that make the
   comparison valid.
9. **Threat turned into a measurement** (12/16). Examples:
   - a 50-repetition study of measurement noise (LQO);
   - your F1 against the published F1 for every reproduced method (ER);
   - an I/O-bound sanity baseline (CDC);
   - inter-annotator agreement on a sample (UDA);
   - an LLM-judge audit (XRAG and SQLM partly);
   - a median-vs-mean check (TSF).
   Then write the result, not the worry: "the verdict is unchanged under …".
10. **Small scale turned into a headroom or durability argument** (SEM, ER).
    - SEM: a few thousand rows are enough to separate today's systems, and larger scales stay available
      for future ones.
    - ER: the construction method gives tunable difficulty, so harder variants can be generated.

### 8.3 One compact scope paragraph (recommended for ICDE, because there is no revision round)
UDA added its "Scope and Limitations" paragraph in the PVLDB revision, most likely because a reviewer
asked for it [inference from the v1 → PVLDB changes]. ICDE 2027 has no revision round, so pre-empt the
request.
- Write one paragraph of 80–150 words at the end of the setup or in the Discussion, titled
  **"Scope of the findings"** or **"Threats to validity"**, not "Limitations".
- Use 3–4 sentences, each in the form "threat → what the paper already does about it → bounded claim".
- Keep the one-clause local scopes (patterns 1, 2, 4) where they apply. The paragraph collects them; it
  does not repeat them.
- End with a positive statement of what the findings are valid for. Do not end with what they are not
  valid for.

### 8.4 What accepted EAB papers never say about their own study
- **Deficit adjectives**: incomplete, elementary, insufficient, preliminary as a self-label, indicative
  only, narrow.
- **Apologies and process stories**: "unfortunately", "we found a bug and re-ran", "due to an error",
  "in review we noticed".
- **Bare non-generalisation**: "results may not generalise" without the range they do hold for.
- **"Only N models / datasets"**, "small sample", "we could not", "we did not have time or budget".
  The exception is a cost stated once, together with the validity-preserving device (E4).
- **A "Limitations" heading for the benchmark.** Headings with "Limitations" are given to the evaluated
  methods (DCO, RLESI).
- **Any self-limit repeated** across the abstract, contributions, takeaways and conclusion.

### 8.5 The opposite failure: hiding (a rejection reason)
Do not overclaim.
- Avoid universal rankings from one hardware class.
- Avoid "first / most comprehensive" claims without a coverage table.
- Avoid a missing Ours-row criterion, or text that contradicts a table.
- Keep every subset, exclusion, single-run or unvalidated judge visible next to the number it affects.

The accepted pattern is **visible but bounded**, not invisible.

## 9. Page budget for a 12-page ICDE EAB paper (observed shape, adapted)

| Part | Pages | Content |
|---|---|---|
| Introduction | 1.3–1.6 | gap figure, RQs, findings preview, 3–4 contributions |
| Background and taxonomy | 1–1.5 | methods under test, decomposed into components |
| Benchmark design | 1.5–2 | data, workloads, metrics, ground truth, protocol, inclusion criteria, controls |
| Experiments by RQ | 5–6 | one subsection per RQ, each ending with a boxed finding |
| Lessons, recommendations, scope | 0.7–1 | decision table or figure, research opportunities, scope paragraph |
| Related work and conclusion | 0.8–1 | positioning against prior benchmarks in core venues; a conclusion that restates findings with numbers |

After the conclusion: the AI-Generated Content Acknowledgement (outside the 12 pages), then the references.

## 10. EAB writing checklist
- [ ] The title follows one of the five patterns and carries the ICDE tag as a prefix.
- [ ] The abstract has scale numbers, 2–3 numeric findings about the evaluated methods, one
      recommendation, the artifact URL, and no limits of your own study.
- [ ] The gap is shown by a measurement (Figure 1) or a criteria table. Your own setup meets every
      criterion in that table.
- [ ] RQs are in the introduction. Each experiment subsection ends with a boxed finding with a number.
- [ ] A lessons section has a decision table or figure.
- [ ] The reporting includes:
  - runs and their dispersion;
  - a claim rule or test;
  - seeds;
  - pinned versions and temperature;
  - $ and tokens with price dates;
  - timeouts;
  - ground-truth quality, and judge agreement where a judge is used.
- [ ] Inclusion criteria are listed with named exclusions. Reimplementations carry a caveat.
- [ ] Each self-limit appears once, where it applies, with its reason and a counter-measure.
- [ ] There is at most one scope paragraph of 80–150 words. No "Limitations" heading for the benchmark.
- [ ] No deficit or apology words about your own study (`scripts/icde_structure_check.py --eab`).
- [ ] At least 10 VLDB/SIGMOD/ICDE references. Prior benchmarks are positioned against.
- [ ] Every count is identical across the abstract, setup, tables and artifact. All four Part-B papers
      had a mismatch (`limitations-writing-eab.md` B.5 O26).
