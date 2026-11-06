# Stating limitations in AQP / sampling / LLM-query papers with guarantees (ICDE practice)

Third corpus for `limitations-writing.md` (graph algorithms) and `limitations-writing-eab.md` (benchmarks):
regular research papers on approximate query processing with error guarantees, sampling-based estimation,
proxy- or LLM-powered query processing with guarantees, semantic operators and sample maintenance.
Twelve accepted papers were read in full on 2026-11-06 (9 ICDE 2022-2027, 3 PVLDB). Every quote was
checked verbatim against the extracted full text and is under 15 words. Counts are observations, not
venue rules.

**Integrity boundary (same as the other guides).** Change placement, frequency, wording and framing only:
every measured number stays in the tables, no claim becomes false, no competitor is hidden. In this area
reviewers can recompute your losing cells from a public artifact, so a sentence that contradicts a table
is fatal.

## Quick rules (details and evidence below)
1. Abstract gains-first (10/12); a no-gain regime becomes a worst-case bound ("outperforms or matches",
   "never worse than ...") in the body, not a closing negative sentence (1/12 states a loss, and pairs it
   with the gain in one clause).
2. Say "asymptotic" once, precisely, with its validity condition, in the theorem (and title if you like);
   do not repeat the caveat in Discussion. 0/6 CLT-based papers give a finite-sample bound for the main
   estimator, so asymptotic guarantees are the norm, not a weakness to apologise for.
3. Back the asymptotic guarantee with empirical coverage at the sample sizes actually used, including the
   smallest slices (5/6 do). This is the answer to BARGAIN-style (SIGMOD'26) "only asymptotically" attacks.
4. Classify weak regimes as efficiency losses, never correctness losses: "only affect performance, not
   correctness" (ABae), "will still provide accuracy guarantees" (SUPG).
5. Every losing cell gets its cause in the same or the next sentence (11/11): skew, balance, target
   looseness, slice size, parameter range.
6. One compact discussion unit of 80-200 words at most, not a "Limitations" heading (1/12 has one); pair
   each item with a direction.
7. Define correctness relative to the oracle in the problem definition ("with respect to the reference
   algorithm", LOTUS); report a human-truth variant or agreement number (5/6 that use model oracles).
   A few-hundred-row human audit is above the norm (SemiBonsai: 40 pairs; ExSample: ~100 frames).
8. Report real dollars and tokens at list prices (4/12; all LLM-era papers do).
9. Proprietary data: 0/12 depend on it. Let public datasets carry every headline claim, present the
   enterprise workload as external validity, release code + generator + public labels, and give the
   non-release reason in the CMT form (ICDE 2027 CFP).
10. Ablation losses of your own planner/variant are evidence for the next component; look for a second
    metric (latency, blocked queries, certified targets) where the full method wins.

## Worked case: TopUp (ICDE 2027 R2), 23 self-negating statements found, 6 kept
| Before (self-negation) | After (scope / mechanism / evidence) | Rule |
|---|---|---|
| Abstract ends "The savings ... vanish on one public dataset at loose targets." | Delete; the range 0.72-1.00x already shows the 1.00; add certified-target evidence (0.97-0.99 vs 0.63-0.72) | 1 |
| Contribution bullet "We also report where it does not help: ..." | Contribution: a planner-computed rule for when exact labelling is cheaper | 1, R2 |
| RQ title "Where X helps, and where it does not"; Discussion "Limitations." | "When does a synopsis pay off?"; "Scope of the guarantees." (2 sentences) | 6 |
| "A-lazy is within 11% of X's cost ... and cheaper in one" (planner looks useless) | Second metric: without the plan 21-25% of queries block on top-ups vs 3.5-7.0%, and fewer targets are certified | 10 |
| "40 replicates cannot separate such tails from a small bias" | Mechanism (low-rate cells, large weights) + bound (mean bias at most 5% of eps) | 5 |
| "flooring them [ratio intervals] ... is a direct extension" | Run the extension as an incremental experiment, report the coverage | 3 |
| "the guarantee ... is supported only by a consistency argument" (third mention of asymptotic) | Keep in the proposition only | 2 |
| "on par" cell stated in abstract, contributions, takeaway, discussion | Once, in RQ1, with cause and "still meets its targets" | 4, 5 |

`scripts/icde_structure_check.py` flags the wording above ("we also report where", "not evaluated",
"cannot separate", "should not be used", "direct extension", "supported only by", "holds trivially",
"is largest without", "at most N% on", failure headings with nested braces, negatives in the contribution
list).

## 1. Corpus

| ID | Short name | Full title | Venue + year | URL actually read | Topic |
|---|---|---|---|---|---|
| P1 | KG-AQP | Aggregate Queries on Knowledge Graphs: Fast Approximation with Semantic-aware Sampling | ICDE 2022 [V: DOI 10.1109/icde53745.2022.00263] | https://arxiv.org/pdf/2203.03792 | AQP with CLT/bootstrap confidence interval; proxy vs human ground truth |
| P2 | ExSample | ExSample: Efficient Searches on Video Repositories through Adaptive Sampling | ICDE 2022 [V: arXiv journal_ref; DOI ...2022.00266] | https://arxiv.org/pdf/2005.09141 | Adaptive sampling with a DNN detector as oracle |
| P3 | JanusAQP | JanusAQP: Efficient Partition Tree Maintenance for Dynamic Approximate Query Processing | ICDE 2023 [V: DOI 10.1109/icde55515.2023.00050] | https://arxiv.org/pdf/2204.09235 (v2) | Synopsis/sample maintenance under inserts and deletes; CLT CIs |
| P4 | BATCHER | Cost-Effective In-Context Learning for Entity Resolution: A Design Space Exploration | ICDE 2024 [V: DOI 10.1109/icde60146.2024.00284] | https://arxiv.org/pdf/2312.03987 | LLM cost-quality trade-off, real API dollars |
| P5 | ZenDB | Towards Accurate and Efficient Document Analytics with Large Language Models (ICDE title: "Querying Templatized Document Collections with Large Language Models") | ICDE 2025 [V: DOI 10.1109/icde65448.2025.00183; same six authors as the arXiv v1] | https://arxiv.org/pdf/2405.04674 (v1; ICDE camera-ready text **not** read) | LLM SQL over documents, cost vs accuracy |
| P6 | SpatialJoinSampling | Random Sampling over Spatial Range Joins | ICDE 2025 [V: arXiv comment "Accepted version of our ICDE2025 paper"] | https://arxiv.org/pdf/2508.15070 | Exact uniform join sampling |
| P7 | CactusDB | CACTUSDB: Unlock Co-Optimization Opportunities for SQL and AI/ML Inferences | ICDE 2026 [V: title page says accepted to ICDE 2026] | https://arxiv.org/pdf/2602.23469 | SQL + ML/LLM inference co-optimisation |
| P8 | OptiAQP | Index-Assisted Stratified Sampling for Online Aggregation (ICDE list title: "OptiAQP: Index-Assisted Stratified Sampling for Online Aggregation") | ICDE 2027 [V-partial: listed on icde2027.github.io/accepted-papers.html, but that page's heading reads "ICDE 2026"; round not verified] | https://arxiv.org/pdf/2604.28141 | Horvitz–Thompson stratified sampling with (eps, delta) CLT bound |
| P9 | SemiBonsai | Cost-Effective Numerical QA over Semi-Structured Table: Structuring, Resolution, Planning | ICDE 2027 [V-partial: arXiv comment "technical report for the ICDE 2027 paper", and the title is on the same accepted list] | https://arxiv.org/pdf/2610.07749 | LLM QA under a monetary budget; LLM judge validated against humans |
| P10 | SUPG | Approximate Selection with Guarantees using Proxies | PVLDB 13(11) 2020 [V: reference line in PDF] | https://arxiv.org/pdf/2004.00827 | Proxy plus oracle selection with recall/precision guarantees |
| P11 | ABae | Accelerating Approximate Aggregation Queries with Expensive Predicates | PVLDB 14(11) 2021 [V: reference line in PDF] | https://arxiv.org/pdf/2108.06313 | Proxy-stratified sampling for aggregates with expensive predicates |
| P12 | LOTUS | Semantic Operators and Their Optimization: Enabling LLM-Based Data Processing with Accuracy Guarantees in LOTUS | PVLDB 18(11) 2025 [V: reference line in official PDF] | https://www.vldb.org/pvldb/vol18/p4171-patel.pdf (venue and key phrasing); https://arxiv.org/pdf/2407.11418 (v3, full analysis) | LLM semantic operators with proxy/oracle accuracy guarantees |

Used only as reviewer-expectation evidence, outside the corpus counts:
- **BARGAIN**, "Cut Costs, Not Accuracy: LLM-Powered Data Processing with Guarantees". The arXiv comment says "To appear in SIGMOD'26". Read at https://arxiv.org/pdf/2509.02896.

Candidates dropped:
- **HAIDES: Adaptive Approximation of Inference Queries over Unstructured Data** (ICDE 2025; DOI 10.1109/icde65448.2025.00181; Papadopoulos, Simitsis, Pedersen). No open full text was found. **[NR]**
- **BlazeIt, VerdictDB, PS3.** Outside ICDE 2022–2026, and the PVLDB/SIGMOD slots were already used by closer analogues. **[NR]**
- **Unify (ICDE 2025), BOND (ICDE 2026).** No arXiv full text was found. **[NR]**

---

## 2. Per-paper findings, (a)–(g)

Key: (a) does the abstract state a loss, or a regime where gains vanish; (b) how the guarantee and its assumptions are phrased; (c) how losing cells or small gains are phrased; (d) whether there is a dedicated Limitations heading, and how long; (e) how non-released or proprietary data is handled; (f) how oracle or label quality is handled; (g) future-work phrasing in the conclusion.

| ID | (a) Loss in abstract | (b) Guarantee phrasing | (c) Losing cell / small gain phrasing | (d) Limitations heading | (e) Proprietary data | (f) Oracle / label quality | (g) Future work |
|---|---|---|---|---|---|---|---|
| P1 KG-AQP | No: "with an accuracy guarantee in the form of confidence interval" | CLT plus Bag of Little Bootstraps: "The Central Limit Theorem (CLT) is applied to compute the confidence interval". The word "asymptotic" is never used. | "more results have slightly larger relative error than the predefined error bound", then "This is reasonable, since we provide an accuracy guarantee for" the proxy ground truth | None. Scope is fenced in the intro: "As the first step, we mainly focus on non-extreme aggregates". A Remarks paragraph names an open problem. | Public KGs plus attributes crawled from the web | **Closest precedent.** Reports both the proxy ground truth (tau-GT) and a human-annotated one (HA-GT), measures their Jaccard agreement, and reports errors against both. The proxy is "one of the best-efforts to define correct answers". | "In future, we would derive accuracy guarantees for extreme functions" |
| P2 ExSample | No: "reduces processing time by 1.9x on average and up to 6x". The downside bound is in the intro: "In the worst case, ExSample does not perform worse than random sampling". | No formal error guarantee. The bias bound "matches this upper bound in practice", with the qualifier "though only after enough sampling has happened". | "have very low skew, meaning random should do just as well"; "situations where random is competitive with ExSample"; "it never performs significantly worse" | No heading called Limitations. "IV. DETERMINANTS OF EXSAMPLE LIMITS" (about 800–1000 words, with simulations) and "VII. FUTURE WORK" (about 70 words). | Own 10-hour dashcam set; release not stated; no comment | Detector used as ground truth, admitted: "None of the datasets have human-generated object instance labels". About 100 frames per dataset hand-annotated to fine-tune the detector. | "Two areas for future work are automating chunking" (and score integration) |
| P3 JanusAQP | No: "reduces the error of a state-of-the-art baseline by more than 60%" | "Assuming that all partitions are large enough", then "the central limit theorem can be used to asymptotically bound the estimation error". The intro says "theoretical guarantees on the confidence intervals". | "the DP-based algorithm does lead to a lower error", then "provides favorable trade-off between cost and accuracy". Also: "queries close to the beginning of the catch-up phase will have a higher error". A missing baseline is handled in a footnote: "Due to its age, a direct comparison with AQUA was not feasible". | None. arXiv v2 has no Conclusion; limits are scattered through §4.4 and §6. | Public only | N/A (exact ground truth) | Appendix only: "we plan to investigate in a future work" |
| P4 BATCHER | No; it states prior work's limitation instead | No formal guarantee; mean ± std over 3 runs | "improves F1 score by 1.3%-30.6% on all datasets except Beer", with the cause given: "the dataset is very small (with only 91 pairs for testing)". "achieves comparable or even better F1 scores with manual prompting". A failed LLM is dropped: "Thus, we omit the results of L LAMA 2." (pypdf spacing) | None. Results come as six boxed "Finding k" statements. | Public | Benchmark labels used as truth; LLM noise not discussed. Real API dollars plus AMT labelling dollars reported. | None: "We also provided guidance for selecting appropriate design choices" |
| P5 ZenDB | **Yes**, as a trade-off: beats the RAG baselines "at a marginally higher cost" | Deterministic and conditional: "guaranteeing that the results are correct for well-formatted documents" (named assumption) | "ZenDB achieves comparable precision and recall to GPT_single"; "While ZenDB incurs a slightly higher cost", immediately followed by the gains | None | Partly collaborator-sourced civic documents ("from our collaborators at Big Local News"); release not stated | Human-labelled answers for one collection only; for the others, how ground truth was built was not found | Names its own failure regime: "we plan to study the setting where there are no templates" / "or when the templates are very noisy" |
| P6 SpatialJoinSampling | Hedged: "significantly faster than the baselines in most tests" | Exact guarantee (uniform, independent samples) with an expected-time bound; experiments therefore measure only time and space | "BBST can be worse than KDS when l is significantly small" ... "although the difference is small"; "in practice, the difference is slight". Scope by footnote: "small join result size cases are not interesting for our problem". | One footnote of about 35 words: "Limitation remark: Although our technique can be extended" (to higher dimensions) | Public; code on GitHub | N/A | None; the conclusion repeats "outperforms the baselines by a large margin in most tests" |
| P7 CactusDB | No ("up to441× speedup", pypdf spacing) | Exact rewrites, "without accuracy loss" | Mostly baselines' relative standing: "PostgresML is slightly slower"; "MADLib underperform other baselines for these workloads" | **Yes**: inline paragraph "Limitations and Future Works" at the end of the Conclusion, about 150 words, three items (e.g. "CACTUSDB can only apply a subset of co-optimization techniques") | Public | N/A (LLMs treated as black boxes; this is listed as a limitation) | Each limitation is matched to a future-work item, e.g. "representing LLMs as white-box models" |
| P8 OptiAQP | No: "consistently achieve good speedup and, in extreme cases, up to 3x" | Horvitz–Thompson estimation, "Lindeberge-Lévy Central Limit Theorem" (sic), "in order for the Central Limit Theorem to be valid" with at least 30 samples per stratum. A footnote concedes the CI is "an estimation due to the fact that the true estimator variance" is unknown. Target called "(ε,δ) confidence bound". | Scope, then loss, then mitigation: "as our method is designed for that"; "could be less effective or even cause a small slow down"; "However, they are easy to mitigate in practice" (fallback to uniform sampling). On its own variant: "Greedy even performs worse than the naïve" one. | None. "6 Related work and possible extension" (about 400 words); coverage figures moved to supplementary material | Public plus synthetic; anonymous artifact URL given in the abstract | N/A (exact) | "We also discuss multiple possible extensions to handle additional query types in future work" |
| P9 SemiBonsai | No; criticises prior work instead: "they rely on LLMs without considering financial implications" | No formal guarantee; budget enforced with an adaptive Lagrangian penalty | "incurs a modest runtime"; "and comparable EM on COMPLEX-T" (a tie with GPT-5.5); baselines framed as "No single baseline is consistently strong" | None; scope pre-empted: "tables in existing semi-structured table QA benchmarks are generally small" | Public; code on GitHub | LLM judge validated against humans: "This LLM-based equivalence check matches human judgments in 95% of cases" (40 pairs). Adds an oracle upper bound. | None; the conclusion "consistently improves answer accuracy" |
| P10 SUPG | No; reports others' failure ("existing approaches can catastrophically fail") and "up to 30×" | "with high probability" in the abstract. In the body: "Though this bound is an asymptotic result for large s", defended empirically for s > 100. Hoeffding dismissed because it "does not use any property of the data". | "As the data becomes more balanced, our algorithms outperform uniform sampling less"; "the performance of our algorithms degrades with higher noise"; uncorrelated proxies: "but SUPG will still provide accuracy guarantees" | "8. DISCUSSION AND FUTURE WORK", about 164 words, before the Conclusion: "we have analyzed our algorithms in the asymptotic regime" | Industrial use cases appear only as motivation; public stand-ins evaluated | The DNN oracle "may not exactly match the ground truth labels that a human labeler would provide". Human-label oracles used on 3 datasets. Real dollars from Scale API prices. | "Supporting multiple proxies and even more sample efficient algorithms are avenues for future research." |
| P11 ABae | No: "reducing labeling costs by up to 2.3×" | "matches the expected error of the optimal stratified sampling algorithm asymptotically"; "With high probability over the draws made in Stage"; non-parametric bootstrap CIs. §4.6: "our analysis is asymptotic: finite sample bounds with exact constants" are deferred. | "ABae outperforms or matches uniform sampling in all cases."; "proxy correlation will only affect performance, not correctness."; on sensitivity, "but these are outside of our recommended values of" C | None. "4.6 Discussion" (about 78 words) inside the theory section: "However, we defer extensions to future work." | Public; expert-label collaborations appear only as motivation | Oracle (DNN or human labels) treated as truth; noise not analysed. Cost counted in oracle calls. | None in the conclusion; §4.6 only |
| P12 LOTUS | No ("match or exceed", "up to 3.6× faster") | PVLDB text: guarantees "with respect to the reference algorithm", met "with probability 1−δ" (symbol garbled by pypdf). "Using the central limit theorem and the normal approximation". The word "asymptotic" is never used. arXiv v3 says "gold algorithm" instead of "reference algorithm". | "modestly lower execution time despite modestly higher LLM calls" (competitor DocETL faster here); "requires more oracle calls when using the weaker proxy"; observed failure rate "lower than the configured failure probabilities" | None. PVLDB text offloads material: "we exclude an exploration here due to space limitations" plus a pointer to an extended version. | Public; open source | Correctness is defined relative to an LLM reference algorithm (Llama-70B oracle). Task accuracy is reported separately against dataset ground truth. | Arxiv v3 ends on adoption; PVLDB body: "we envision a rich space of future work exploring" |

Notes on (b). None of the 12 papers gives a finite-sample (non-asymptotic) probabilistic bound for its main estimator. P6 and P7 have exact guarantees and P5 a deterministic conditional one. The others either use CLT/bootstrap or give no formal guarantee.

---

## 3. Cross-paper counts (N = 12 unless stated)

| Property | Count | Papers |
|---|---|---|
| Abstract states a loss or a regime where gains vanish | **1/12** | P5 (cost, phrased as "marginally higher cost") |
| Abstract uses a hedged scope qualifier without stating a loss | 1/12 | P6 ("in most tests") |
| Abstract reports gains only (often "up to X") | 10/12 | the rest |
| A worst-case / "never worse than baseline" bound appears in the intro or body | 3/12 | P2, P10 ("still provide accuracy guarantees"), P11 ("outperforms or matches") |
| Probabilistic guarantee based on CLT / normal approximation / bootstrap | 6/12 | P1, P3, P8, P10, P11, P12 |
| ...of those, the word "asymptotic(ally)" is used | 3/6 | P3, P10, P11 |
| ...of those, the validity condition is stated (large partitions, ≥30 per stratum, s > 100) | 3/6 | P3, P8, P10 |
| ...of those, coverage / failure rate is checked empirically | 5/6 confirmed | P1, P8 (in supplementary), P10, P11, P12; P3 not confirmed |
| ...of those, finite-sample bounds are named as future work | 2/6 | P10, P11 |
| Own losing cell or small gain reported in the body | 11/12 | all except P7 (only baselines' standings found) |
| ...cause stated in the same or the next sentence | 11/11 | data property (skew, balance, size), parameter range, or deliberate trade-off |
| Dedicated "Limitations" heading or labelled paragraph | **1/12** | P7 (inline, about 150 words) |
| Limitations under another name (Discussion / Determinants of limits / Possible extension) | 4/12 | P2, P8, P10, P11 |
| Footnote-only limitation | 1/12 | P6 |
| No limitations text found | 6/12 | P1 (scope sentences only), P3, P4, P5, P9, P12 |
| Results depend on proprietary, unreleased data | **0/12** | none; P2 and P5 use self- or collaborator-collected data with release unstated and no comment |
| Model or LLM used as oracle / ground truth (fully or partly) | 6/12 | P1, P2, P9 (judge), P10, P11, P12 |
| ...states the guarantee is relative to that oracle | 3/6 | P1, P10, P12 |
| ...reports a human-truth variant or agreement check | 5/6 | P1, P9, P10, P11 (some human labels), P12 (task ground truth); P2 only fine-tuned on about 100 hand-labelled frames |
| Real dollar costs reported | 4/12 | P4, P5, P9, P10 |
| Future work stated in the conclusion or its own section | 6/12 | P1, P2, P5, P7, P8, P10 |
| ...future work names the paper's own failure regime or limitation | 4/6 | P1 (extreme aggregates), P5 (no or noisy templates), P7 (one-to-one), P10 (finite-sample) |

Venue split: among the 9 ICDE papers, 1 states a loss in the abstract (P5) and 1 has a limitations paragraph (P7). The 3 PVLDB comparators are more explicit about asymptotics: 2 use "asymptotic" and 2 have a Discussion section.

---

## 4. Writing rules (with TopUp examples)

1. **Keep the abstract gains-first. Express the no-gain regime as a worst-case bound, not as a loss.** 10/12 abstracts report gains only. Every corpus paper that has a weak regime moves it out of the abstract, either as a worst-case statement ("does not perform worse than random sampling") or as "outperforms or matches". For TopUp: the abstract gives the savings range with a scope qualifier ("on workloads with ..." or "in most settings"). The 1.00× public-dataset cell becomes, in the intro and evaluation: TopUp never costs more than exact labelling, and it reaches that parity only when the target is so loose that a small sample already suffices. Do not write "savings vanish" or "fails".
   *Supported by: P2, P6, P11, P10.*

2. **If a trade-off goes in the abstract, name both sides in one clause.** ZenDB is the only corpus paper that puts a loss in its abstract, and it pairs the higher cost with the accuracy gain ("at a marginally higher cost"). Use this only if a reviewer is likely to find the regime anyway, for example by pairing the loose-target parity with the gain at tight targets.
   *Supported by: P5.*

3. **Say "asymptotic" once, precisely, with its condition, in the theorem and the setup. Do not hedge it elsewhere.** The PVLDB analogues say it plainly ("asymptotically", "an asymptotic result for large s"). The ICDE papers state the validity condition ("Assuming that all partitions are large enough"; at least 30 samples per stratum). TopUp's title already says "asymptotic", so state the CLT/Lindeberg condition and the minimum effective sample per query or stratum in the theorem. Do not repeat caveats in every section.
   *Supported by: P3, P8, P10, P11.*

4. **Back the asymptotic guarantee with an empirical coverage table at the sample sizes actually used, including a small-sample or adversarial case.** 5 of the 6 CLT-based papers validate coverage or failure rate. This matters more since BARGAIN (SIGMOD'26) attacks SUPG with an adversarial dataset, saying SUPG "meets the quality target only asymptotically as sample size goes to infinity". TopUp should report empirical (eps, delta) coverage per query at its smallest per-query effective sample sizes. Optionally add a finite-sample (Bernstein / Hoeffding) variant as a robustness row, so the reader sees the gap and its cost.
   *Supported by: P10, P11, P12, P8, P1; threat evidence: BARGAIN.*

5. **Frame finite-sample bounds as a research direction, not an admission.** SUPG: "finite-sample complexity bounds will be a fruitful area of future research". ABae puts "finite sample bounds with exact constants" in Discussion. One sentence in Discussion or Conclusion is enough.
   *Supported by: P10, P11.*

6. **Classify weak regimes as efficiency losses, never correctness losses.** ABae: "proxy correlation will only affect performance, not correctness." SUPG: "but SUPG will still provide accuracy guarantees". For TopUp, the 1.00× cell and weak-workload-overlap cases are where the shared PRN sample buys nothing over a per-query plan; the (eps, delta) target is still met. Say that in the same sentence.
   *Supported by: P11, P10, P12.*

7. **Attach a cause to every losing cell, and give a mitigation or fallback where one exists.** All 11 papers that report own losses do this. The pattern is "X when [data property]" plus "although the difference is small" or a fallback (OptiAQP falls back to uniform sampling: "However, they are easy to mitigate in practice"). For TopUp, attribute the 1.00× to a target looseness or label prevalence where exact or uniform sampling is already optimal. If the allocator can detect this, say it then degenerates to the per-query or uniform plan.
   *Supported by: P2, P8, P6, P4, P10.*

8. **Use one compact limitations unit of about 80–200 words, named as discussion and matched item by item to future work.** Only 1/12 has a "Limitations" label (CactusDB, about 150 words, at the end of the Conclusion, each item matched to future work). The PVLDB analogues use "Discussion and Future Work" (about 164 words) or a "Discussion" subsection (about 78 words). For TopUp, one paragraph can cover asymptotic-only, the LLM-as-reference oracle, the enterprise data release, and the audit size, each paired with a direction. Do not spread "we cannot" sentences across the paper.
   *Supported by: P7, P10, P11, P2.*

9. **Define correctness relative to the LLM labeller ("reference algorithm"), then report a human-oracle variant and an agreement number.** LOTUS (PVLDB) gives guarantees "with respect to the reference algorithm". KG-AQP reports proxy and human ground truths side by side, with their agreement, and explains misses against the human truth as expected ("since we provide an accuracy guarantee for" the proxy). TopUp already has this structure. State it in the problem definition, not in a limitations apology.
   *Supported by: P12, P1, P10.*

10. **Present the roughly 600-row audit as validation that is above the corpus norm, with its size and agreement statistic.** The precedents are smaller: SemiBonsai validates its LLM judge on 40 pairs ("matches human judgments in 95% of cases"), and ExSample hand-labels about 100 frames per dataset. Report agreement with a CI, and state that the guarantee transfers to human truth up to the measured disagreement (KG-AQP pattern).
    *Supported by: P9, P2, P1.*

11. **Report real LLM cost in dollars and tokens alongside oracle-call counts.** SUPG converts labels to dollars at public Scale API prices; BATCHER, ZenDB and SemiBonsai report API dollars or tokens. ABae and LOTUS count oracle calls only, which reviewers of LLM papers now treat as weaker. Give a $ column at public list prices per model.
    *Supported by: P10, P4, P5, P9.*

12. **Fence scope in the introduction, not in a late limitations section, and keep proprietary data out of the critical path.** "As the first step, we mainly focus on non-extreme aggregates" (KG-AQP) and "tables in existing ... benchmarks are generally small" (SemiBonsai) set scope early and neutrally. No corpus paper depends on unreleased proprietary data (0/12), so there is no in-paper precedent. TopUp should:
    - make public datasets carry every headline claim;
    - present the enterprise workload as additional external-validity evidence;
    - give the non-release reason in the CMT submission form, as the ICDE 2027 CFP requires ("an explanation should be provided in the submission form");
    - release code, the workload or query templates, and a de-identified or synthetic generator.
    Mark this rule's evidence as CFP-based, not corpus-based.
    *Supported by: P1, P9, P6 (scope); ICDE 2027 CFP and PVLDB Vol. 20 guidelines (data).*

---

## 5. Reviewer expectations and how accepted papers pre-empt them

Sources:
- The ICDE 2027 CFP and submission guidelines (https://icde2027.github.io/cf-research-papers.html, .../submission-guidelines.html). They publish **no** scoring rubric. They say: at least 3 reviewers; accept or reject with no revision; single-blind; rebuttal in Jan 8–15, 2027 for R2; supplemental material "will be considered in the evaluation"; if artifacts cannot be shared, "an explanation should be provided in the submission form"; contributions should "build on previous advances in the data engineering research community"; 12 pages with no appendix.
- The PVLDB Vol. 20 submission page (https://www.vldb.org/pvldb/volumes/20/submission). Reviewers "will have access to the supplemental material". Acceptable reasons for not sharing include that "data/code may contain copyrighted contents" or that artifacts may be a commercialization candidate.
- BARGAIN (SIGMOD'26) as the most recent published critique of the asymptotic-guarantee line. In its quote "meets the quality target only asymptotically", the missing space in the pypdf output ("targetonly") was restored.
- CFP and PVLDB quotes in this section were re-checked verbatim against the live pages on 2026-11-06.
- **Unverified:** no public OpenReview reviews of comparable AQP / LLM-query papers were found, and the SIGMOD reviewer guidelines were not read. The concerns below are inferred from the CFP text, from BARGAIN's critique, and from what the accepted papers visibly pre-empt. They are not quoted reviews.

| Likely reviewer concern | Evidence that it is live | How accepted papers pre-empt it | TopUp action |
|---|---|---|---|
| **Guarantee is asymptotic only** | BARGAIN builds its case on it: prior work has "only marginal cost savings and weak theoretical guarantees", and SUPG "meets the quality target only asymptotically as sample size goes to infinity" | Name it (P3, P10, P11); state the condition (P3, P8); empirical coverage at the sample sizes used (P10 for s > 100, P12 failure rate, P8 in supplementary); finite-sample bounds as future work (P10, P11) | Rules 3–5. Also compare against BARGAIN, or at least discuss it, as the non-asymptotic per-query competitor. |
| **Missing or weak baselines** | CFP requires positioning against ICDE/VLDB/SIGMOD work | Compare against uniform sampling plus the SOTA (P10, P11); explain an omitted baseline in a footnote (P3 on AQUA, P6 on join-then-sample); drop a failing LLM in one line (P4) | Baselines: exact labelling, uniform, SUPG/ABae-style per-query planners, plus BARGAIN and LOTUS (discussion or experiment); footnote any omission |
| **Real LLM cost not reported** | 4/12 report dollars; LLM-era papers (P4, P5, P9) all do | Dollars at public prices (P10, P4); tokens and per-query cost split into one-off and amortised (P5) | Rule 11; amortisation over the workload is TopUp's core argument, so show $ per query vs. per workload (P5 pattern) |
| **LLM labels treated as truth / label noise** | Prediction-powered inference and related debiasing work pair LLM labels with a small human set; reviewers from statistics or ML will ask "why not PPI?" (inferred, not from a review) | Guarantee relative to the reference algorithm (P12); dual ground truth plus agreement (P1); judge-vs-human check (P9); one-sentence oracle-mismatch caveat (P10) | Rules 9–10; one related-work sentence positioning TopUp against PPI-style debiasing (complementary: TopUp can plug the human-oracle variant into it) |
| **Gains vanish in some regimes** | Any 1.00× cell will be found | Worst-case bound (P2); "outperforms or matches" (P11); cause plus mitigation (P8, P6) | Rules 1, 6, 7 |
| **Evolving data / maintenance cost** | Sample maintenance is the "evolving data" half of the title; JanusAQP is the ICDE precedent | P3 reports catch-up-phase error explicitly ("will have a higher error") and frames it as a trade-off | Report error during maintenance or catch-up and the update cost, with P3-style phrasing |
| **Dataset diversity / public data / artifacts** | CFP: supplemental availability "will be considered"; PVLDB requires a reason for any non-release | 0/12 rely on proprietary data; P8 puts an anonymous artifact URL in the abstract; P6 and P9 link code | Rule 12; artifact link in the paper (ICDE is single-blind, so a named GitHub repository is fine; use an anonymous host only for double-blind venues); non-release reason in the CMT form |
| **Scale** | Generic ICDE expectation (not confirmed from a rubric) | P6 up to 323M points; P3 multi-million-row dynamic data | Show TopUp's sample and allocator overhead vs. data size and number of queries |

---

## 6. Things not verified

- OptiAQP and SemiBonsai: whether they are ICDE 2027 R1 papers. Both titles are on icde2027.github.io/accepted-papers.html, but that page's heading says "ICDE 2026".
- ZenDB: the ICDE 2025 camera-ready text was not read; findings come from arXiv v1, which has the same authors and system.
- LOTUS: the detailed findings come from arXiv v3. Only venue, "reference algorithm" wording, CLT phrasing, space-limitation offloading and future-work phrasing were re-checked in the PVLDB 18(11) PDF.
- JanusAQP: whether coverage is checked empirically was not confirmed; arXiv v2 has no Conclusion, and the ICDE version may differ.
- No OpenReview or other public reviews were found for comparable papers; the reviewer concerns are inferred (Section 5).
- HAIDES (ICDE 2025), Unify (ICDE 2025), BOND (ICDE 2026): no open full text; not analysed.
- Word counts for limitations sections are approximate.
