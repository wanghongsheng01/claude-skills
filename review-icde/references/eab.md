# Reviewing an ICDE "Experiment, Analysis, and Benchmark" (EAB) paper: form, checklist, lenses

Use this file in place of the generic criteria when the paper carries the EAB tag or is a benchmark or
experimental-survey paper. The process is in `../SKILL.md`: independence, desk screen, three reviewers,
discussion, rebuttal and meta-review. Writing-side evidence is in
`write-icde/references/eab.md` (16 accepted papers) and `write-icde/references/limitations-writing-eab.md`.

**Provenance (read 2026-11-06).** ICDE publishes no review form. The form below is a simulation. It is
anchored on these public statements:

| Anchor | Source |
|---|---|
| EAB contribution = "fundamentally new insight into the strengths and weaknesses of existing methods, or new ways to evaluate existing methods"; topic must be of wide interest | ICDE 2027 CFP, https://icde2027.github.io/cf-research-papers.html |
| EAB papers "MUST provide all artifacts necessary to reproduce the results. No exceptions"; supplemental availability "will be considered in the evaluation" | same |
| At least 3 reviewers; senior-PC meta-review; accept or reject, no revision; rebuttal Jan 8–15 2027 for Round 2 | same |
| Relevance: must position against ICDE/VLDB/SIGMOD work, or desk reject | same |
| PVLDB EA&B adds a third contribution type, "characterization of workloads in real-world deployments", and two flavours. Experimental surveys: the core contribution is the gathered insights and reusable artifacts. Workload characterisation: insights into workloads plus reusable benchmark suites or traces | https://vldb.org/pvldb/volumes/20/contributions ; https://vldb.org/2027/call-for-research-track.html |
| PVLDB EA&B must make all data and software available, "there are no excuses". From Vol. 20, the initial submission must link the full reproducibility package. Associate editors use a standard rubric for supplemental availability | https://vldb.org/pvldb/volumes/20/submission |
| The PVLDB reproducibility package has four items: system (white box or fully specified black box); input data or its generator; experiments (configuration, scripts, workload, measurement protocol); scripts that turn raw data into the paper's graphs. Central claims must be supported; an independent team must be able to recreate data and graphs; identical numbers are not expected without identical hardware | https://vldb.org/pvldb/reproducibility |
| SIGMOD 2027 E&A types: experimental survey; experimental analysis of a phenomenon; benchmarks and datasets (all artifacts for review, public release if accepted); reproducibility papers that verify or refute past results; user studies | https://2027.sigmodconf.hosting.acm.org/calls_papers_sigmod_research.shtml |
| Fair-benchmarking pitfalls in DB performance testing: non-reproducibility, failure to optimise, apples vs oranges, over-specific tuning, cold/warm/hot runs, ignoring preprocessing time, incorrect code | Raasveldt et al., DBTest 2018, DOI 10.1145/3209950.3209955, author copy https://pdet.github.io/assets/papers/benchmarking.pdf |
| "Benchmarking crimes" (22 items in six groups: selective benchmarking, improper handling of results, wrong benchmarks, improper comparison, omissions, missing information) | van der Kouwe et al., arXiv 1801.02381, https://ar5iv.labs.arxiv.org/html/1801.02381 |

Evidence types used below:
- **[OFF]**: an official venue text.
- **[PUB]**: a public methodological paper.
- **[OBS]**: observed in accepted papers. This is survivor evidence.
- **[INF]**: inferred, for example from arXiv v1 → camera-ready changes. Label it as an inference.

## 1. EAB review form (simulation; extends `assets/review_form.md`)

**0. Paper type.** Choose one: experimental survey / new benchmark or dataset / workload
characterisation / reproducibility study / new evaluation method (metric, protocol). A paper whose main
contribution is a new method belongs in the regular track; say so.

**1. Summary.** In 3–5 sentences: the object evaluated, the blind spot claimed, the design, the main
findings.

**2. Scores** (1 = poor … 5 = excellent), each with one sentence of justification:

| Criterion | 5 means | 1 means |
|---|---|---|
| **Novelty of insights** [OFF] | Findings overturn or sharply qualify published claims, or reveal a regime nobody tested, and they are explained by a mechanism | A leaderboard that confirms what the evaluated papers already report |
| **Soundness of methodology** [OFF/PUB] | Fair, equally tuned configurations; a control isolates the factor under study; repetitions and dispersion; a claim rule; validated metrics and ground truth | Untuned or misconfigured baselines; one run; metrics or LLM judges unvalidated; confounded factors |
| **Coverage and representativeness** | Strongest and most recent methods with stated inclusion criteria; workloads that span the regimes practitioners meet; real plus controlled synthetic data | Missing the obvious state-of-the-art method; one dataset; toy scale; arbitrary selection |
| **Reproducibility (artifacts)** [OFF] | All four PVLDB package items public now; per-table commands; pinned versions; cached LLM outputs | Anything "upon acceptance", private data, missing scripts. **For ICDE EAB this is a hard requirement, not a score** |
| **Usefulness** [OFF: "wide interest"] | Actionable guidance (decision table, thresholds, recommendations); a reusable benchmark that others can extend; lasting value beyond today's versions | Descriptive results with no guidance; a tool tied to one version |
| **Presentation** | RQ → experiment → boxed finding traceable to a figure; limits visible but bounded (section 4) | Findings buried; text contradicts tables; self-negating or hidden limits |
| **Relevance to data engineering** [OFF] | Systems, queries, indexes, data quality, or cost; builds on VLDB/SIGMOD/ICDE work | Pure ML-model benchmark with no data-engineering angle |

**3.** Strengths S1–S3. Weaknesses W1–W3, each with what would fix it.

**4.** The EAB checklist (section 2): mark every **fail**.

**5.** Limitations-presentation lens (section 4): classify every self-limit statement.

**6.** Requested experiments (section 5): fill in the table.

**7.** Overall: Strong Accept / Accept / Weak Accept / Weak Reject / Reject. Confidence 1–5. The three
most likely reasons for rejection. Questions for the rebuttal.

## 2. EAB review checklist
Mark each item pass / fail / n.a. Each **fail** must appear as a weakness or a requested experiment.

**A. Contribution and insight**
- A1 The blind spot of prior evaluations is shown by evidence: a measurement or a criteria table, not
  an assertion.
- A2 At least one finding is new: it contradicts, qualifies or extends published claims.
- A3 Each major finding has a mechanism explanation; hedging is allowed for causes, not for numbers.
- A4 The findings generalise beyond one configuration, or their range is stated.
- A5 There are recommendations or a decision aid, which carries the usefulness score.
- A6 The paper's own "Ours" row satisfies every criterion it uses against prior work.

**B. Selection** (benchmarking crimes A1–A3, C1–C2)
- B1 Inclusion criteria are explicit. Famous excluded methods are named, with a reason.
- B2 The strongest and most recent methods are included, including commercial systems where they
  matter (SemBench includes BigQuery).
- B3 Workloads and datasets span the relevant regimes. Synthetic data are justified and controlled.
- B4 No benchmark or dataset is dropped from a suite without a reason, and no variable range is cut to
  hide weaknesses.

**C. Fair comparison** (Raasveldt pitfalls; crimes D1–D3)
- C1 Every method has the same tuning budget and protocol: calibrate, then freeze; the same hardware;
  the same backbone LLM.
- C2 Baselines are not unoptimised, misconfigured or modified without saying so. Deviations from the
  original papers are listed.
- C3 Configuration fidelity is checked: reproduced numbers are compared with the published ones.
- C4 Implementations are correct. There is a sanity baseline (CDC uses fixed-size chunking as an I/O
  check) and output checks.
- C5 Reimplemented closed systems carry a caveat, so their results reflect the design, not the product.

**D. Measurement and statistics** (crimes B1–B5, F1–F4)
- D1 The number of runs, warm-up, and cold/warm/hot cache state are stated and justified.
- D2 Dispersion is reported (std, IQR or CI). There is a claim rule or a significance test.
- D3 Preprocessing, training, index-build and tuning costs are reported, not only query time.
- D4 Absolute numbers are given as well as ratios. Ratios are aggregated with the geometric mean.
  Per-workload results are available.
- D5 Hardware and software versions are given. Timeouts and out-of-memory cases are handled explicitly
  in the aggregates.

**E. Metrics and ground truth**
- E1 Metrics measure what the claims are about, and their artefacts are discussed (ratio blow-up, metric
  gaming).
- E2 Human labels report the number of annotators, the effort, and agreement.
- E3 An LLM judge is validated against humans on a sample, with agreement. The judge model is pinned.
- E4 Generated benchmark content reports curation losses and error rates.

**F. LLM-specific**
- F1 Model identifiers, access dates, temperature and max tokens are given. Prompts are released.
- F2 Nondeterminism is handled: repetitions or cached outputs; API failures and retries are reported.
- F3 Contamination: could the test data be in pretraining? Mitigations: evaluation-time synthesis,
  post-cutoff data, or a perturbation test.
- F4 Prompt sensitivity: at least one alternative prompt or strategy, or the claim is scoped to the
  defaults.
- F5 Cost is given in $ at dated list prices and in tokens, plus latency, plus the total budget.

**G. Reproducibility package** [OFF]
- G1 Code, configurations, data or generators, raw results and plotting scripts are all public at a
  neutral host.
- G2 The README maps commands to tables and figures. There is an environment specification and a
  licence.
- G3 Nothing is withheld ("upon acceptance", "on request" or private data means an ICDE EAB violation).

**H. Presentation**
- H1 Each finding is traceable to a figure or table. Counts are identical across the abstract, setup,
  tables and artifact.
- H2 The limitations lens (section 4) passes.
- H3 The paper fits in 12 pages without appendix. Key evidence is not deferred to a website or
  technical report.

**I. Positioning and scope**
- I1 Prior benchmarks are compared explicitly, including concurrent ones (UDA positions against
  SemBench).
- I2 The core-venue lineage is in Related Work. The AI acknowledgement names the LLMs used in the
  experiments.

## 3. Common rejection reasons for benchmark papers
Public sources do not publish rejected reviews. This list combines official criteria [OFF],
methodological literature [PUB], what accepted papers visibly defend against [OBS], and changes between
the submitted and the published versions [INF].

1. **"A leaderboard, not insight"**: results are tabulated without mechanisms or new claims [OFF:
   "fundamentally new insight"].
2. **Findings already known or obvious**: they only confirm what the evaluated papers report.
3. **Unfair or misconfigured baselines**: unequal tuning, default settings for some methods and tuned
   ones for others [PUB: failure to optimise; crimes D3]. Accepted papers defend against this with
   calibrate-then-freeze (CDC) and stated deviations (LQO) [OBS].
4. **The strongest or most recent system is missing**, or an inclusion criterion looks arbitrary [OBS:
   ER, LQO and N360 all name their exclusions].
5. **Workloads that are not representative**: toy scale, a single dataset, synthetic data only
   [PUB: crimes C1–C2].
6. **Single runs, no variance, no claim rule** [PUB: crimes B4]. Most accepted papers are weak here, so
   reviewers who check this find easy targets.
7. **LLM results not reproducible**: unpinned models, no prompts, no cached outputs, no temperature.
8. **Metric or judge validity unverified**: an LLM-as-judge with no human agreement, or ground truth of
   unknown quality [INF: UDA added an agreement study between arXiv v1 and PVLDB].
9. **Artifacts missing or incomplete**. For ICDE EAB this is non-compliance [OFF].
10. **Category confusion**: a new method mixed into the benchmark (N360's SuperSQL), or a benchmark with
    no evaluation insight.
11. **Out of scope**: a pure ML-model benchmark with no data-engineering angle [OFF].
12. **Over-generalisation**: universal rankings from one hardware class or one LLM. CDC's "we do not
    claim reversal" sentence is the counter [OBS].
13. **Self-negating limitations** that hand reviewers the rejection reasons, or limits hidden so that
    the text contradicts the tables (section 4).
14. **Key evidence deferred** to a website or technical report. ICDE allows no appendix [OFF], and
    reviewers are not obliged to read the external material.
15. **Inconsistent counts** across the abstract, setup, tables and appendix [OBS: in all four Part-B
    papers].

## 4. Limitations-presentation lens for EAB papers
Classify every sentence in which the authors concede something about **their own study**. Do not
classify negatives about the **evaluated methods**: those are the contribution, and they are welcome in
the abstract, findings and conclusion.

| Acceptable scope statement (does not lower the score) | Self-negation (a presentation weakness that invites rejection) | Hiding (a soundness weakness; possible rejection) |
|---|---|---|
| A design choice with its reason, at the point of use ("to isolate X we fix Y") | Deficit adjectives about one's own study: incomplete, elementary, insufficient, narrow, indicative only | A subset, exclusion, single run or unvalidated judge not stated next to the number it affects |
| The domain of validity attached to the claim (this hardware class, these versions), plus an invariance argument for the other metrics | A bare "may not generalise" with no range | A universal ranking claimed from one setup |
| "We do not claim X", which bounds a headline | Apologies and process stories: unfortunately, a bug, a re-run, an error found in review | Text contradicting a table; a criterion charged against prior work but not met |
| Inclusion criteria with named exclusions and reasons | Limits of one's own study in the abstract or conclusion, or repeated across sections | "First / most comprehensive" without a coverage table |
| Concede-then-neutralise in one sentence | A long threats list (more than about 5 items, more than about 180 words), with unanswered items | Evidence deferred to an unreviewed website |
| A threat answered by a measurement (control, agreement study, reproduction check) | "Only N models", "small sample", "we could not afford", stated without a validity-preserving device | |
| One scope paragraph (80–150 words; "Scope of the findings" or "Threats to validity") | A "Limitations" heading for one's own benchmark | |
| A versioned snapshot with a refresh plan; "not a universal ranking, a platform for controlled comparison" | Hedging every finding, including measured numbers | |

How the lens enters the review:
- **Each self-negation item** is a presentation weakness. Propose the rewrite pattern from
  `write-icde/references/eab.md` §8.2.
  - If the conceded issue is real and fixable, request the experiment that removes it (section 5)
    rather than a better sentence.
- **Each hiding item** is a soundness weakness. Ask for the fact to be stated next to the number, or
  for the claim to be narrowed.
- **Score effect.**
  - Self-negation lowers Presentation by 1. It lowers Overall only if it makes a finding look unsupported.
  - Hiding lowers Soundness, and may be a reason to reject.
  - Never penalise visible-but-bounded statements.

## 5. Requested experiments: reviewers may ask; authors run them
This is a pre-submission review. ICDE 2027 has no revision, so every request must be settled before the
deadline (Round 2: 2026-11-11, 17:00 PT).
- **Reviewers.** Each reviewer may request experiments of four kinds (below). Each request names the
  weakness it answers, a rough cost, and the result that would change the score.
- **Meta-reviewer.** Merges the requests and ranks them by impact per hour of compute and calendar time.
- **Authors (the revising agent).**
  - Run the accepted requests as incremental experiments with the existing harness.
  - Regenerate the tables and figures from the raw results, and update the text and the artifact.
  - Record each request in the revision table: done / answered with existing evidence / declined with a
    reason.
- **Re-review.** Fresh reviewers re-review until no blocking weakness remains or the deadline stops
  the loop.

| Type | EAB examples |
|---|---|
| **Add** | The missing strongest or commercial system; a real-world workload next to synthetic ones; a second LLM backbone or judge; a decision-table experiment; a human audit of the LLM judge (≥100 items, agreement with CI); a contamination probe; cost at list price |
| **Supplement** | More repetitions with dispersion and a claim rule; a sensitivity sweep over the frozen parameter (target size, temperature, prompt); larger scale on one dataset; per-workload breakdowns |
| **Re-run** | Baselines with equal tuning budgets; all systems on the current pinned versions; measurements on a dedicated idle machine with a stated cache state; any cell produced by an earlier build, so the "earlier build" sentence can be deleted |
| **Remove** | Redundant panels; a comparison that is unfair and cannot be fixed in time (state the exclusion as an inclusion criterion instead); a mixed-in new method that blurs the EAB category; claims that no table supports |

**Prefer a request that turns an admission into a result over one that adds a caveat.** Examples:
- a control experiment instead of "may be confounded";
- an agreement study instead of "the judge may be biased";
- a reproduction check against published numbers instead of "our configuration may differ".

## 6. Meta-review additions for EAB
- Is the paper a genuine EAB contribution (insight or a new evaluation method), or should it be a
  regular paper?
- Would it be desk-rejected? Check the tag prefix, artifacts with no exceptions, and the core-venue
  lineage.
- List the consensus fails from checklist sections A–I, the merged experiment list with owners and
  costs, and the lens findings.
- After the rebuttal: which fails remain, and which of them only a new experiment could fix. Those
  are fatal at ICDE, so fix them before submitting.
