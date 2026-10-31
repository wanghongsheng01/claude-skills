# How papers in Information Processing & Management (IPM) are written: survey notes

ISSN 0306-4573. Prepared 2026-10-30. Companion data: `ipm_paper_survey.csv` (same folder, 219 papers).

## 0. Evidence base and how far to trust it

| Tier | Papers | What it means |
|---|---|---|
| Full text, read by me | **9** | Body prose read end to end from extracted PDF text. Numeric table rows were stripped from 6 of them before reading (104136, 105151 and 104123 were read with tables). |
| Full text, machine counts only | 25 | Regex counts and headings. Not read. One of them (104723 DataFactory) also had its RQ, contribution and implication passages read as excerpts. |
| Abstract only | 129 in the CSV | Abstract metrics, no body. |
| Metadata only | 56 in the CSV, 1,497 overall | Crossref title and reference list. |

Labels used below: **[FT]** read full text, **[FT-auto]** machine counts on full text, **[ABS]** abstract only, **[META]** Crossref/OpenAlex metadata.

Limits that affect the conclusions:

- **Sampling is not random.** Full texts exist only where a legal open copy was reachable, which favours arXiv-posting and European-repository authors. Only 8 of the 34 full texts are the published version (VoR). The other 26 are preprints or accepted manuscripts, and can differ from what IPM printed. For example, 105030's arXiv v3 has no limitations section; the published version may have one. Proportions from the 34 are indicative, not estimates for the journal.
- **Regex counts are crude.** They count words, not meaning. A mention of "baseline" or a *p*-value can be incidental. Headings are missed where PDF extraction merged lines (three papers returned no top-level headings). Where I read a paper, my manual reading overrides the regex.
- **Three of the four named Text-to-SQL DOIs could not be read.** 103978, 104560 and 104607 are closed, with no copy found through OpenAlex, Semantic Scholar, the arXiv API or web search. No abstract was found either. Only 104136 was read. Do not cite anything about the other three beyond their titles and reference lists.
- **Not reached:** ScienceDirect (403), the IPM Guide for Authors (403), and many repositories (403 to scripted requests, including Durham, Open Access Milano-Bicocca, Open University, Aalto, Torino). So **no journal rule is confirmed here**; everything is observed behaviour. Check the Guide for Authors before submission, especially highlight limits and the AI declaration wording.
- Three PDFs (103672, 103792, 104951) downloaded but could not be parsed, and are not counted.
- The arXiv title search was stopped after 181 of its 268 target titles, so more preprints may exist.
- **No journal version of the abstract is guaranteed.** Of 158 abstracts analysed, 119 are from OpenAlex (mostly CC-licensed VoR records); 39 are from Semantic Scholar or the arXiv API and may be preprint wording.
- All DOIs in the CSV (219 of 219) were individually re-checked against Crossref: DOI matches and ISSN 0306-4573 is present.
- "2027" issue years are Crossref's assigned future issues for papers already online.

## 1. Most useful findings

1. **IPM accepts evaluation-only LLM papers, and they can carry bad news in the abstract.** 105151, 104128, 105131 and 105047 all state limits of LLMs as main findings. The convention is that bad news arrives with a usable recommendation: where the tool can and cannot be used. [FT, ABS]
2. **The strongest template for an audit paper is two-level measurement:** item-level disagreement, then the downstream effect on the decision people actually make. 105151 (LLM relevance judges) does this: Cohen's κ only 0.32–0.53 at pair level, yet Kendall's τ ≥ 0.90 on some system rankings, and not on others. [FT]
3. **The only published IPM Text-to-SQL paper I could read is weak on evaluation and leaves a clear opening.** 104136 uses one sample database and about 200 partly GPT-4-generated test questions. Its Execution Accuracy exceeds its Test-Suite Accuracy by 6.5 to 13.5 points in all six configurations, but the paper treats these as three views of capability and does not examine the gap as a measurement problem. [FT] An inference, not a finding of the paper: the gap is a citable foothold from inside the journal for work on evaluation measures.
4. **"Implications" is the clearest IPM signature.** Headed implications sections appear in 7 of 8 published versions, but 9 of 26 preprint or accepted copies. This difference may reflect version, field, or author habit; I cannot separate these with this sample. Treat a theoretical-and-practical implications section as expected. [FT-auto]
5. **Limitations are normal and fairly long, but rarely called threats to validity.** Manually measured spans in 8 read papers run from 70 to 946 words, median about 409. The phrase "threats to validity" appears in 2 of 34. [FT, FT-auto]
6. **Inferential statistics are not required for acceptance, but they are a differentiator.** Some inferential statistic was found in 19 of 34 papers: 6 of 9 evaluation papers and 8 of 18 method papers. 104262 reports 17 models with no test or interval. Its evaluation design was still accepted. [FT, FT-auto]
7. **Method papers and evaluation papers follow different conventions.** Method papers rely on baselines and ablation (11 of 18 mention ablation). Evaluation papers rely on agreement or correlation measures, and on error analysis. Only 1 of 9 evaluation papers mentions ablation. Do not imitate DataFactory's format for an audit paper. [FT-auto]
8. **Self-citation is modest and not uniform.** Pooled, 5.99% of references point to IPM; the median paper has 5.8%. 158 of 1,496 papers have none. 509 have five or more. Text-to-SQL papers run lower (median 4.1%, 3 of 10 have none). [META]
9. **NL-query reference lists are very recent.** Median 80% of references from the last three years, against 54% for the whole journal. Reference counts: median 50.5 for NL-query, 58 overall. [META]
10. **"Audit" is almost absent from titles:** 1 of 1,497 (105174). The closer vocabulary is evaluate, assess, benchmark, empirical or comparative, which appears in 32 of 61 LLM-evaluation titles. [META] Papers 105225, 105154 (accuracy versus reliability) and 105174 (reproducible failure plus label-free audit) are close relatives for audit papers.

## 2. Corpus

- Crossref journal query, published from 2024-01-01, type journal-article: 1,530 records. After removing editorials, corrigenda and similar by title: **1,497**. [META]
- OpenAlex: 1,424 records. OA status: 1,211 closed, 127 hybrid, 55 green, 31 bronze. CC licence recorded in Crossref: 135 of 1,497.
- Title-based groups (regex on title; see the `focus_category` column; inspect before relying on it):
  - **A, NL-to-query:** 10 papers (103802, 103978, 104136, 104280, 104560, 104607, 104723, 104836, 105042, 105092)
  - **B, LLM evaluation/reliability:** 61
  - **C, LLM as annotator or human-AI comparison:** 11
  - any LLM term in title: 241

## 3. Title patterns [META, n = 1,497; computed]

| Feature | All (1,497) | LLM-any (241) | A (10) | B (61) | C (11) |
|---|---|---|---|---|---|
| Median words | 11 | 13 | 10 | 13 | 13 |
| Contains a colon | 735 (49%) | 135 (56%) | 7 | 38 (62%) | 6 |
| Question | 33 (2%) | 8 (3%) | 0 | 4 | 2 |
| Acronym or system name first | 349 (23%) | 62 (26%) | 4 | 16 | 2 |
| "Towards" first | 16 (1%) | 5 | 0 | 4 | 1 |
| "framework" | 156 (10%) | 32 | 3 | 8 | 0 |
| evaluate/assess/benchmark/empirical/comparative | 78 (5%) | 34 | 0 | 32 (52%) | 6 |
| "novel" | 29 (2%) | 4 | 0 | 1 | 0 |

Other title counts, all 1,497: "audit" 1, "reliab-" 8, "benchmark" 12, "hallucin-" 8, "bias" 17.

Patterns by paper type:

- **Method paper:** `Name: what it does, via how`. Examples: 104560, 104836, 105042.
- **Evaluation paper:** a claim or question, then scope after a colon. Examples: 103973, 104437, 105225; also long descriptive forms such as 105047 and 105131.
- **Question titles** are rare overall but over-represented among LLM-capability papers (4 of 61 in B against 2% overall).

## 4. Abstracts

Computed on 158 abstracts of at least 100 words, with highlights removed. [ABS, 119 OpenAlex + 39 other]

| Measure | All 158 | OpenAlex 119 | LLM title 43 | B or C 15 |
|---|---|---|---|---|
| Median words (IQR) | 208 (184–233) | 215 (184–235) | 221 (189–240) | 221 (189–234) |
| Median sentences | 9 | 9 | 9 | 9 |
| Contains a number | 129 (82%) | 97 (82%) | 37 (86%) | 14 (93%) |
| Contains a percentage | 66 (42%) | 48 (40%) | 19 (44%) | 4 (27%) |
| "we/our" | 133 (84%) | 99 (83%) | 35 (81%) | 13 (87%) |
| "this paper/study/article" | 104 (66%) | 79 (66%) | 28 (65%) | 13 (87%) |
| Gap or contrast word | 109 (69%) | 82 (69%) | 33 (77%) | 10 (67%) |
| "novel" | 40 (25%) | 29 (24%) | 5 (12%) | 2 (13%) |
| outperform/superior | 42 (27%) | 29 (24%) | 8 (19%) | 0 |
| Hedge word | 41 (26%) | 32 (27%) | 11 (26%) | 7 (47%) |
| Explicit negative phrase | 23 (15%) | 15 (13%) | 9 (21%) | 3 (20%) |
| Implication word | 31 (20%) | 24 (20%) | 7 (16%) | 3 (20%) |
| Structured labels (Background:, etc.) | 0 | 0 | 0 | 0 |

Observations:

- **Always one unstructured paragraph.** No structured abstracts were found.
- **Usual move order, seen in the abstracts I inspected:** context (1–2 sentences), contrast or gap (1), what this paper does (1), data and design with counts (1–3), results with numbers (2–4), one closing sentence on meaning or use.
- **Results are stated with values, including sample sizes.** Examples: 105151 gives κ and τ ranges; 104128 gives precision and recall; 105131 gives cosine ranges; 104280 and 104836 give point gains in accuracy.
- **Evaluation abstracts avoid "outperform" and hedge more.** In the small B or C group, 0 of 15 used outperform/superior and 7 of 15 hedged. Small sample; treat as a tendency.
- **The most careful abstract I found is 105179.** It reports a clustered bootstrap interval, reports an interval that crosses zero, and states what that does not show: "this interval does not establish equivalence" (105179, abstract). It also confines the claim to the studied domain. This is a model for how to report a non-result in one clause.
- **Other negative-framing devices in abstracts:** no single approach wins (105047); the claim is restricted to a tested setting (105047, 105179); an explicit avoid recommendation (105151); a direct need for human oversight (104128).

## 5. Highlights [ABS, indirect]

Highlights are not in the VoR PDFs I could read (0 of 8 VoR copies carry them on the first page). They are visible indirectly because 34 of 125 OpenAlex abstract records have them merged in: 3 bullets in 10 records, 4 in 14, 5 in 10. Measured on 125 bullets: median 81 characters, maximum 148, 44 above 85 characters. Parsing bullet boundaries is imperfect. Bullets are short noun-led or verb-led fragments, one finding or element per bullet (see 104616). I could not read the current rule; confirm the limit in the Guide for Authors.

## 6. Section structure

Top-level headings [FT-auto, 34; 3 not extractable].

- **Method-paper default:** Introduction, Related work, (Preliminaries), Method, Experiments, (Ablation), (Discussion and implications), Conclusion. Examples: 103920, 104028, 104052, 104580.
- **Evaluation-paper default:** Introduction, Related work, Data or gold standard, Method/Experiments, Results, Error analysis, Implications and limitations, Conclusion. Example: 104262.
- **Information-science or survey variant** pushes each element to the top level: Limitations, Theoretical contribution, Practical implications, Future research direction. Examples: 104350, 104882.
- **Dedicated "Research objectives" heading** appears in 6 of 34 (103796, 103900, 104136, 104299, 104723, 105124). This is more common than I would expect at database venues, and it spans both method and evaluation papers.
- **Dedicated "Error analysis" sections or subsections** appear in the evaluation and verification papers I read (104128, 104262).
- **A "distinction from existing work" subsection** explicitly compares against nearest neighbours (105151, Sec 2.1, with a comparison table).
- **Median body length** about 10,500 words (includes tables as extracted). Published PDFs ran 13–31 pages among the 8 VoR copies (one includes a repository cover page).

## 7. Research questions and contributions

Counts [FT-auto, 34]: labelled RQ1, RQ2 and so on in 10; "research question" phrase in 13; labelled hypotheses in 3; labelled research objectives in 1; regex-detected contribution list in 20.

Forms seen [FT]:

- **Labelled RQs after the gap, one sentence each, answered in result headings.** 104123 places four RQs at the end of the introduction, then headings RQ1 to RQ4 in Results. DataFactory (104723, excerpt) uses five RQs mapped to Sections 5.2 onward. This mapping is the cleanest pattern.
- **Research objectives instead of RQs.** 105151 lists RO1–RO3 and cites them inside section openings and result headings.
- **RQs plus hypotheses.** 104882 has RQ1–2 and H1–2, and revisits them by name in discussion, while saying they are not definitively answered.
- **Unlabelled numbered questions.** 104350.
- **Contribution bullets with bold lead-ins.** 105030 and 104262 each list about four. 105151 lists two.
- **No RQ and no bullets at all.** 104493 poses questions in prose and 104128 uses a road-map paragraph. So labels are common but not mandatory.

Observed habit: RQs are justified individually before being listed (104123 and 104350 explain why each comparison level matters to a named user).

## 8. How the gap is argued [FT]

Common order: domain matters → current practice costs or fails → recent LLM work offers a route → **but** something specific remains open → this paper's response.

Types of gap seen:

- **Coverage gap, then a generalisation question:** evidence is mostly on one language or domain, so does it transfer? (105151)
- **Metric gap:** earlier work relies on one metric, so test whether the result depends on it. (105151)
- **Anomaly gap:** a prior result does not fit the pattern, so investigate it with more data. (104123, which revises the first author's own earlier finding)
- **Benchmark flaws gap:** existing benchmarks have three named faults. (105030)
- **Integration gap:** parts exist separately, but no unified pipeline. (104882)
- **Practical bridge gap:** technical people versus non-technical users. (104136; thin literature review, still accepted)

Evidence for the gap is often a short list of named systems and their faults. An explicit "to the best of our knowledge" claim appears (105151), and is immediately bounded by citing the one prior study and what it did not cover. Strong "first" claims also appear (105030, 104123).

Note also how contrast is carried by words such as however or nevertheless rather than by polemic. Criticism of prior work is usually about scope, not error.

## 9. Experiment design and reporting

### Counts [FT-auto; regex]

| Item | All 34 | Evaluation 9 | Method 18 | VoR 8 |
|---|---|---|---|---|
| "baseline" at least 3 times | 18 | 2 | 15 | 4 |
| Mentions ablation | 12 | 1 | 11 | 2 |
| Any inferential statistic (test, *p*, CI, bootstrap, effect size) | 19 | 6 | 8 | 5 |
| *p*-value pattern | 10 | 4 | 2 | 2 |
| Confidence interval | 9 | 4 | 3 | 3 |
| Effect size | 6 | 3 | 2 | 0 |
| Chi-square | 6 | 2 | 2 | 2 |
| Bootstrap | 4 | 1 | 1 | 2 |
| Bonferroni/Holm/Benjamini | 4 | 2 | 1 | 1 |
| *t*-test | 3 | 0 | 2 | 2 |
| ANOVA | 3 | 0 | 1 | 2 |
| Wilcoxon | 1 | 1 | 0 | 0 |
| Friedman | 1 | 1 | 0 | 0 |
| McNemar | 1 | 1 | 0 | 1 |
| Agreement (κ, Krippendorff, Fleiss) | 5 | 2 | 2 | 0 |
| Correlation (Kendall, Spearman, Pearson) | 9 | 5 | 3 | 1 |
| Link to GitHub, HF, Zenodo, OSF or figshare | 25 | 7 | 15 | 4 |

### Practices worth copying [FT]

- **Reference standard and its own uncertainty.** 105151 measures human-human disagreement first, then compares LLMs against it. 104123 computes a theoretical maximum correlation for a proxy (0.226), so an r of 0.134 can be read against what the proxy could possibly show. **This is directly transferable** to auditing accuracy when the reference is imperfect.
- **Human comparator on the downstream task.** 105151 compares LLM-based rankings with those from individual human annotators, a fairer baseline than the aggregate.
- **Interpretive thresholds with a citation.** 105151 adopts Voorhees' τ bands; it also tabulates κ interpretation.
- **Uncertainty over queries.** 105151: BCa bootstrap with 10,000 resamples over queries, 90% CIs, and an explicit remark that intervals do not always clear the threshold. It also discloses that 8 of 15 systems are BM25 variants, which could inflate correlation.
- **Paired test for paired outcomes.** 104136 reports McNemar for model comparison on the same 200 questions.
- **Effect sizes reported alongside tests, including small ones.** 104493 gives Cramér's V and labels some effects small; it also reports non-significant comparisons (for example, *p* = 0.179).
- **Repeat stochastic runs.** 104123 runs five per article and quantifies the gain from averaging; 104493 ran 10–20 per condition; 105030 discloses single-pass inference and gives cost as the reason.
- **Version and date pinning.** 105151 gives dated model IDs and generation dates; 104123 too. 104128 has a Replicability section listing seed and parameters, plus raw LLM outputs.
- **Error analysis with cases.** 104128 groups false positives, false negatives and low recall. 104262 uses confusion matrices for the best model per category.
- **Multi-model, multi-prompt grids.** 105151 uses 3 × 2; 104262 uses 17 × 4; 105030 uses 19 models and three input modes.
- **Cost as a stated design constraint.** 104123 gives about $500; 105151 and 105030 cite API cost to justify scope.

### Weak practice that was still published, so not a safe bar

- 104262: no statistical tests or intervals, despite fine ranking differences among models.
- 104136: single database, synthetic test items, no intervals, and "significantly" used for the overall pattern while testing only two comparisons. Reported as observed; do not copy.
- 104882: comparison uses metrics taken from other papers and explicitly calls them circumstantial and not directly comparable. It states the goal is feasibility, not superiority.

## 10. How limitations are written

### Measured [FT; manual span, words]

| Paper | Words | Where | Items | Tone |
|---|---|---|---|---|
| 104350 | 70 | own top-level section | 2 | Each named, one justified as pragmatic |
| 104136 | 159 | run-in, inside implications | about 4 | Plain concession, then items ordered from first to last |
| 104123 | 329 | opening of Discussion, no heading | several | Starts with sample scope; hedged forecasts about other models |
| 105151 | 392 | Sec 5.3 of Discussion | 4 | Ordered; several items defended by reference to comparable collections |
| 104262 | 426 | second half of Sec 7 | 5 | Each paired with planned work |
| 104128 | 542 | Sec 7.5, joined with future work | several | States untested assumptions; next step named |
| 104882 | 934 | Sec 4.4 Threats (452) + end of Sec 5.4 (482) | many | Includes conditions under which the framework would do poorly |
| 104493 | 946 | run-in paragraph in Sec 4 | many | Discloses a model-version confound and failed effects |
| 105030 | 0 | none in arXiv v3 | 0 | Published version not seen |

Median across the 8 non-zero values: about 409 words. Heading-based heuristic across 16 papers with detectable sections: median 425 (range 70–1,776, inflated by whole-section capture). [FT-auto]

Position [FT-auto]: the final mention of limitations or threats sits at a median of about 92% through the body. Limitations usually come after results and before the conclusion, in or next to the Discussion. 4 of 8 VoR copies give them a heading; 8 of 8 mention them.

### Wording habits (my paraphrase, not quotes)

- An opening sentence concedes limits while affirming value; then ordinal items.
- Content order: dataset size and scope; single-collection generalisation; limited model and prompt subset; provider and version drift; reproducibility.
- **Defending a limitation is accepted practice.** 105151 notes its 46 queries are comparable to established TREC tracks, then still concedes that some metrics are volatile with so few queries.
- **Pairing each limitation with future work is routine.**
- **Stating a limit on the claim itself:** the observed metric-level divergence could be caused by collection size rather than by the metric (105151). This is rare and valuable.
- "Threats to validity" is the exception, not the norm (2 of 34). Internal/external/construct validity taxonomies were not seen in the papers I read, apart from 104882's unstructured use of the heading. Use "Limitations" unless there is a reason not to. If you keep a validity structure, it would be distinctive, not expected.

## 11. Null and negative results

Negative-phrase regex (did not, no significant, underperform, and similar): median 9 per paper, range visible in the CSV (for instance 2 in 104136, 44 in 104212). [FT-auto] Counts include incidental uses.

Read examples [FT]:

- **105151:** the rationale prompt shows no clear pair-level advantage; LLMs are unsuited to P@10 and R@10 rankings; lower pair-level error does not imply better ranking preservation. Stated in abstract, results, discussion and implications.
- **104123:** a stricter prompt reduced correlation (0.134 to 0.117) and was dropped from further analysis; journal-level correlation with citation rate is negative; ChatGPT underrates some prestigious clinical journals. Negative correlations are explored rather than hidden.
- **104493:** hashing did not lower hallucinations in Experiment 2, and increased them for Llama 3.1; some comparisons are not significant; some models do not benefit. Note the conclusion still leads with the positive overall message.
- **104350:** repeatedly says which factors showed no significant difference.
- **105030:** modest performance on a benchmark is treated as a finding; a human-designed prompt harms some reasoning models.
- **104128:** 44% recall is reported up front, then framed as acceptable for its use, while 12% false positives are said to require human oversight.
- **104262:** larger proprietary models decline under chain-of-thought prompting, and this is reported and explained speculatively.

Pattern: **negative results are published when they answer a usable question** (when to trust, which metric, which model). I did not find any paper positioned purely as a null-result report. Authors typically pair a null with an explanation or a positive adjacent result. A non-result is often the conclusion only for one model or metric.

## 12. Hedging

Hedge terms per 1,000 words: may, might, could, suggest, appear, seem, possibly, perhaps, potentially, likely, arguably, tend. Boosters: significantly, clearly, demonstrate, novel, outperform, superior, substantially, robust, remarkable, impressive, first, strongly, effectively, comprehensive. [FT-auto; includes methods prose]

| Group | Median hedge | Median booster |
|---|---|---|
| All 34 | 2.84 | 3.50 |
| VoR 8 | 3.09 | 3.35 |
| Evaluation 9 | 3.20 | 5.08 |
| Method 18 | 2.12 | 3.33 |
| Read 9 | 3.70 | 3.19 |

Read papers, hedge rate: 105030 0.44; 104882 2.94; 104136 2.98; 104128 3.06; 104262 3.70; 105151 5.20; 104493 6.97; 104350 9.38; 104123 10.88.

Reading impressions [FT]:

- **Register varies widely, by author tradition more than topic.** Information scientists hedge most (Thelwall-coauthored 104123 and 104350: 10.88 and 9.38).
- **Boosterism is tolerated.** 104262 and 104136 use words like outstanding, impressive, revolutionize, transformative. High booster rates here do not mean editors reward it. Avoid copying, particularly for an audit paper, where credibility rests on restraint.
- **Causal explanations are usually marked** by likely, may be due to, or perhaps, as in 104262 and 104123. Findings themselves tend to be flat statements.
- **A careful claim-scoping device:** an explicit qualifier limiting the finding to the tested settings. See 105047 [ABS] and 105151.
- **Hedged response to one's own hypotheses:** results are described as consistent with an expectation, while further analysis is called for (104882).

## 13. Figures and tables

Highest figure and table numbers cited [FT-auto]:

| Group | Median figures | Median tables |
|---|---|---|
| All 34 | 5.5 | 5.5 |
| VoR 8 | 6 | 4.5 |
| Evaluation 9 | 5 | 4 |
| Method 18 | 7 | 8 |

Habits [FT]:

- Figure 1 is often a framework or pipeline schematic (104136, 105030, 104128, 104882).
- Results tables have model rows and metric columns, with the best value in bold (104262).
- Comparison table against sibling datasets or studies (105151 Table 1, 104882 Tables 1–2).
- Heatmaps for pairwise agreement or rank displacement; interval plots with a threshold line (105151 Figures 3, 5, 6, 7).
- Long descriptive figure captions stating the takeaway (104136, 105151).
- Graphical abstract is sometimes included as a figure in preprints (104128, 104493).
- Prompts appear in figures or appendices (105151, 104128, 104493).
- Screenshots of systems occur (104136, 105151), though 104136's five prototype screenshots add little evidence.

## 14. References [META; Crossref deposited lists; computed]

| Group | n | Median refs (IQR) | Median share ≤ 3 yrs before online year | Median mean age, yrs | Median IPM share | Pooled IPM share | Zero IPM refs | ≥ 5 IPM refs |
|---|---|---|---|---|---|---|---|---|
| All | 1,496 | 58 (48–71) | 53.6% | 4.9 | 5.8% | 5.99% | 158 | 509 |
| LLM title | 241 | 60 (49–75) | 61.4% | 4.4 | 5.2% | 5.45% | 40 | 75 |
| A NL-to-query | 10 | 50.5 (43–55) | 80.5% | 2.5 | 4.1% | 3.65% | 3 | 0 |
| B LLM evaluation | 61 | 58 (44–77) | 65.6% | 4.7 | 5.1% | 5.16% | 13 | 19 |
| C LLM annotator | 11 | 57 (42–91) | 53.6% | 5.4 | 4.4% | 4.88% | 4 | 4 |

Method: "online year" is Crossref's created year. IPM references are matched by IPM DOI prefix or by journal title in the deposited reference; references without either are not counted, so the share is a lower bound. Crossref records for recent items may be incomplete. Reviews inflate the upper tail (maximum 577).

Reference counts for group A: 103802 51; 103978 74; 104136 33; 104280 43; 104560 43; 104607 50; 104723 51; 104836 56; 105042 55; 105092 37.
IPM references in those: 3, 0, 0, 4, 2, 1, 3, 2, 3, 0.

Practical target from the data (a suggestion, not a rule): 50–70 references, roughly half or more from the last three years, and about 3–6 from IPM where honestly relevant. Zero IPM citations is common, so there is no sign of a required quota. Citing the IPM neighbours in Section 17 is still sensible since they are on topic.

## 15. Implications sections

Counts [FT-auto]: heading containing "implication": 16 of 34, VoR 7 of 8. Phrase "theoretical implications/contributions": 13 of 34, VoR 5 of 8. Phrase "practical implications/contributions" or "managerial": 16 of 34, VoR 6 of 8. Future work mentioned: 29 of 34.

Forms [FT]:

- Combined subsection under Results and discussion (104136 Sec 5.3).
- Subsections under a closing section (104128: 7.3 Theoretical contributions, 7.4 Practical implications, 7.5 Limitations and future work).
- Separate top-level sections (104350, 104882; DataFactory 104723 has a top-level combined section).
- Practical implications only, as a bullet list (105151 Sec 5.2). Each bullet is finding → recommendation; this was the clearest version I read.
- Combined with limitations (104262 Sec 7).

"Theoretical" is treated loosely. In the computing-leaning papers it often just restates what was learned about models and methods (104136, 104128). In information-science papers it ties to named theories (104350 sociotechnical; 104882 Marchionini and human-information interaction). A theory-free statement is acceptable if it names what understanding has changed.

## 16. AI-use, CRediT, data statements

- **AI declaration:** present in 5 of 34 by regex, including preprints: 103704, 104244, 104262, 104493, 105151. Only 1 of 8 VoR copies has it; absence probably means no AI use was declared, but I cannot confirm that. Wording I read describes language or readability help, says authors reviewed and edited, and that they take responsibility. Check Elsevier's current required wording.
- **CRediT:** 8 of 8 VoR copies. 16 of 34 overall, since preprints often omit it.
- **Data availability statement:** 8 of 8 VoR. 12 of 34 overall.
- **Openness varies, even in published papers.** 104136 says on request plus a code link; 104882 on request; 104350 confidential; 105151 and 104262 release data; 104128 and 104493 release raw LLM outputs. A public repository link was found in 25 of 34, 4 of 8 VoR.
- **Competing-interest statement and funding sections** are standard in VoR copies.

## 17. NL-to-query cluster

| DOI | Title (short) | Evidence | What is known |
|---|---|---|---|
| 10.1016/j.ipm.2025.104136 | Ojuri et al., text-to-SQL, agents and LLMs | **[FT, VoR]** | See below |
| 10.1016/j.ipm.2026.104723 | DataFactory, multi-agent table QA | [FT-auto + excerpts, preprint] | Five RQs mapped to Sec 5; ten baselines in five categories; ablation; Research Objectives section; theoretical-practical section |
| 10.1016/j.ipm.2025.104280 | Text-to-Cypher pipeline | [ABS] | 240 queries over three complexity levels on one biomedical KG; reports vanilla-prompt baseline and execution accuracy; closes on scalable and robust |
| 10.1016/j.ipm.2026.104836 | CyVerACT agentic Cypher | [ABS] | Two public datasets, 2,180 entries; correctness and execution success; syntax and schema gains |
| 10.1016/j.ipm.2024.103978 | Multi-pattern RAG for Text-to-SQL | [META] | 74 refs, no IPM refs in Crossref match |
| 10.1016/j.ipm.2025.104560 | EMLC multi-level correction | [META] | 43 refs |
| 10.1016/j.ipm.2025.104607 | Q-value guided Text-to-SQL | [META] | 50 refs |
| 10.1016/j.ipm.2026.105042 | PostGISer, GeoSQL | [META] | 55 refs; bronze per OpenAlex; not reachable |
| 10.1016/j.ipm.2026.105092 | Agentic table QA | [META] | 37 refs |
| 10.1016/j.ipm.2024.103802 | SPARQL generation for KBQA | [META] | 51 refs |

From titles, most of this cluster proposes methods. Apart from 104136's comparison, I found **no IPM paper evaluating Text-to-SQL evaluation itself**, but I could read only one fully, and 103978, 104560, 104607 might discuss metric weaknesses. Check before claiming a gap in the journal.

**104136 in detail [FT].** Objectives have their own section. Compares fine-tuning versus few-shot on GPT-3.5 and Llama-3-8B, plus GPT-4 and Llama-3.3-70B as benchmarks. Database: MySQL classicmodels, chosen because it can be rebuilt. Test set of about 200 questions drawn from a pool of curated and GPT-4-generated pairs. Metrics: Valid SQL, Execution Accuracy, Test-Suite Accuracy.

| Configuration | VA | EX | TS | EX − TS (my subtraction) |
|---|---|---|---|---|
| Fine-tuned GPT-3.5 | 97.0 | 91.5 | 79.5 | 12.0 |
| GPT-3.5 few-shot | 94.5 | 87.0 | 74.0 | 13.0 |
| GPT-4 | 99.0 | 95.5 | 82.0 | 13.5 |
| Fine-tuned Llama-3-8B | 82.5 | 79.0 | 72.5 | 6.5 |
| Llama-3-8B few-shot | 69.5 | 62.5 | 56.0 | 6.5 |
| Llama-3.3-70B | 99.0 | 95.0 | 81.5 | 13.5 |

McNemar is reported only for two EX comparisons: 4.26, *p* ≈ 0.039 for the GPT-3.5 pair, and 25.33 for the Llama pair. The paper names the gold-query-based test suite but does not discuss errors in gold SQL or EX false positives. Limitations mention a small domain dataset, biases of pretrained models, and prompt sensitivity. Its abstract is non-technical and has no numbers, which is unusual in my sample (18% lack numbers).

## 18. LLM-as-annotator and human-AI agreement cluster

- **105151 NormasTCU [FT, preprint]:** described above. Best single template.
- **105030 MSLR [FT, preprint]:** 2+1 annotation with Krippendorff's α = 0.832; human-LLM pipeline; LLM judge validated through correlation with a recall metric and 87.96% agreement on 380 expert-rated items.
- **104145 KG validation [ABS]:** nine workflows from automated to hybrid. Precision up, recall and F1 down for LLM alone; hybrid yields best F1 with little human effort.
- **104128 [FT, accepted]:** LLM verification without internal knowledge, with human oversight recommended.
- **104486 crowdworkers [ABS]:** LLM contexts compared with expert contexts; new metric validated by two human referees.
- **105131 [ABS]:** Krippendorff's α and cosine; inter-LLM agreement exceeds LLM-taxonomy agreement; competing explanations are tested.
- **Titles only [META]:** 103973, 104365, 104437, 104567, 105154, 105174, 105225.

Recurring claim structure: LLM disagrees with humans at item level, but the result can still be useful at an aggregate level, provided a human stays involved for specific conditions. A result that contradicts this comfort (for example, aggregate rankings also move) would stand out; state it precisely.

## 19. Evaluation, benchmark and reliability cluster

- **104123 [FT, accepted]:** large-scale correlation study; RQs; CI; proxy ceiling; negative results; own earlier finding revised.
- **104262 [FT, preprint]:** new gold standard; 17 × 4 grid; error analysis; no tests.
- **104493 [FT, accepted]:** debiasing via prompts; chi-square plus Cramér's V; many stated failures.
- **104350 [FT, VoR]:** survey in 20 countries; tests and null differences; short limitations.
- **105047, 104616, 104554, 104476, 105179, 105173 [ABS]:** benchmarks and fairness or trust evaluations, all giving figures in abstracts. 104476 includes output stability; 105179 includes article-clustered bootstrap and ablation; 105173 includes a robustness check.
- **105124, 104840, 104299, 103900 [FT-auto]:** evaluation-leaning. 105124 uses Wilcoxon, correction, CI. 104840 discusses deviations from preregistration in its limitations (1,170-word heuristic span), the only such mention I noticed.
- **Re-evaluation or reproducibility language in titles:** 104611 and 105174 only.

## 20. Draft rules for a Write-IPM skill

Evidence-based defaults. Items marked *(rule unconfirmed)* require checking the Guide for Authors.

**Framing**

1. State the problem as an information-use problem: who relies on the score, and what decision changes. Keep database detail in service of that.
2. Do not frame it as a method contest. Frame it as an evaluation of a measure that people act on.
3. Use two levels: item-level error, then effect on comparison, ranking, or deployment decisions.
4. Include a recommendation about when to trust, avoid, or check. Evaluation papers are read for this.

**Title.** Claim or question plus scope, about 11–15 words, colon acceptable. Prefer evaluate, measure, reliability or similar; "audit" is rare but has one precedent (105174).

**Abstract.** One paragraph, about 190–240 words, 8–10 sentences, no labels. Include corpus sizes, and at least two results with values and uncertainty if available. Close on scope and recommendation. Use first person. Avoid "novel" and "outperform" for an evaluation paper.

**Highlights.** 3–5 fragments, one point each; aim for under 85 characters *(rule unconfirmed)*.

**Introduction.** Domain and stakes, current practice, what is known, specific open question, RQs or ROs with one-line rationale, numbered contributions, optional road map.

**Related work.** Close with an explicit comparison subsection or table against nearest neighbours. Cite IPM neighbours (104136, 105151, 105225, 105154, 105174) where honestly relevant, and only after reading them.

**Design.** Name the reference standard and measure its uncertainty. Pin model IDs, dates and parameters. Report repeated runs or justify single runs. Give cost constraints. Publish data, prompts, and raw outputs.

**Statistics.** Paired tests for paired outcomes, intervals over the right sampling unit, effect sizes, and multiple-comparison control. A cited interpretive threshold where one exists. Not universal in IPM, so this adds credibility rather than meeting a bar.

**Results.** Headings map one-to-one to RQs or ROs. Follow with error analysis using cases.

**Discussion.** Interpretation; comparison with prior work; **Theoretical implications**; **Practical implications** as finding → recommendation; **Limitations** at about 300–500 words, ordered items, each stating the effect on claims and, where possible, its remedy.

**Negative results.** Report them in the abstract if central. Give a likely reason marked as such, and say what they mean for practice. Use exact scope, such as a non-significant comparison or an interval that does not establish equivalence.

**Hedging.** Plain statements for measured findings. Hedge explanations and generalisations. Avoid revolutionize, outstanding and impressive even though published examples exist.

**End matter.** CRediT, competing interests, data availability, and the AI declaration *(wording unconfirmed)*.

**References.** 50–70, majority recent. Keep foundational items for evaluation theory.

## 21. Unverified and open

- Current Guide for Authors: not seen.
- Whether IPM's scope statement or editors favour particular framing: not investigated.
- Whether "implications" sections are required, or just common: unknown.
- Acceptance rates and rejected-paper patterns: no evidence here, since this sample is only of published work.
- Priority papers to obtain through library access: 105225, 105154, 105174, 103978, 104560, 104607, 105042, 104611, 104437.

## 22. Fully read papers

| DOI | Copy used | Type |
|---|---|---|
| 10.1016/j.ipm.2025.104136 | VoR, CC BY, University of New England repository | Evaluation and prototype |
| 10.1016/j.ipm.2025.104350 | VoR, CC BY, White Rose | Survey |
| 10.1016/j.ipm.2026.104882 | VoR, CC BY, University of Jyväskylä | Framework, literature-based validation |
| 10.1016/j.ipm.2025.104123 | Accepted-status preprint, arXiv 2411.01952 | Evaluation |
| 10.1016/j.ipm.2025.104128 | Accepted version, arXiv 2409.07507 | Method and evaluation |
| 10.1016/j.ipm.2025.104262 | Preprint, arXiv 2412.08258 | Evaluation |
| 10.1016/j.ipm.2025.104493 | Preprint, arXiv 2411.17304 | Method and evaluation |
| 10.1016/j.ipm.2026.105030 | Preprint v3, arXiv 2511.07979 | Benchmark |
| 10.1016/j.ipm.2026.105151 | Preprint, arXiv 2608.27746 | Dataset and evaluation |
