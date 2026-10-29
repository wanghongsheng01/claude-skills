# Writing for *Data Mining and Knowledge Discovery* (DMKD): evidence-based notes

Compiled 2026-10-29 from 30 DMKD papers (2016–2026; 23 of 30 published online 2021 or later) and the journal's public submission guidelines (link.springer.com/journal/10618/submission-guidelines). The per-paper data is in `dmkd_paper_survey.csv`, in the same folder as these notes.

**How to read this file.**
- Each section gives **Observations** (what the sample shows, with counts and DOIs) and then **Recommendations** (my advice for the manuscript "Auditing Data-Repair Benchmarks with Explicit Comparison Contracts"). The two are kept apart.
- Counts are "k/N". N is the set the count could be measured on:
  - 30: all papers;
  - 28: full texts read (26 Springer open-access HTML pages and 2 accepted arXiv versions);
  - 26: Springer full-text HTML pages, when the count concerns publisher end-matter that arXiv versions lack;
  - 20 and 8: the evaluation/benchmark full texts and the method full texts.
- Two required papers (Campos 2016 and Berrar 2022) are paywalled. For them only the abstract, keywords, pagination and reference list could be read.
- Counts based on keywords (for example "Wilcoxon" or "limitation") come from automatic text search, which I then checked by hand for the key cases.

## 0. Sample key (short tag → DOI prefix 10.1007/)

**Evaluation / benchmark / reproducibility / data-quality papers (22)**

| Tag | DOI (10.1007/…) | Paper |
|---|---|---|
| Campos16 | s10618-015-0444-8 | On the evaluation of unsupervised outlier detection (abstract and metadata only) |
| Bagnall17 | s10618-016-0483-9 | The great time series classification bake off |
| IsmailFawaz19 | s10618-019-00619-1 | Deep learning for time series classification: a review (arXiv 1809.04356 accepted version) |
| Ruiz21 | s10618-020-00727-3 | The great multivariate TSC bake off |
| Middlehurst24 | s10618-024-01022-1 | Bake off redux |
| Hewamalage23 | s10618-022-00894-5 | Forecast evaluation for data scientists: common pitfalls and best practices |
| Sorbo24 | s10618-023-00988-8 | Navigating the metric maze (TSAD metrics taxonomy) |
| Marques23 | s10618-023-00931-x | On the evaluation of outlier detection and one-class classification |
| Iglesias25 | s10618-024-01077-0 | What do anomaly scores actually mean? |
| SanchezVinces25 | s10618-024-01086-z | A comparative evaluation of clustering-based outlier detection |
| Rochner24 | s10618-024-01056-5 | Evaluating outlier probabilities |
| Fabris22 | s10618-022-00854-z | Algorithmic fairness datasets: the story so far (dataset audit) |
| Fanourakis23 | s10618-023-00941-9 | KG embedding methods for entity alignment: experimental review (entity-resolution adjacent) |
| Guidotti22 | s10618-022-00831-6 | Counterfactual explanations and how to find them: literature review and benchmarking |
| Bodria23 | s10618-023-00933-9 | Benchmarking and survey of explanation methods for black box models |
| Souza20 | s10618-020-00698-5 | Challenges in benchmarking stream learning algorithms with real-world data (arXiv 2005.00113 accepted version) |
| Grzenda20 | s10618-019-00654-y | Delayed labelling evaluation for data streams |
| Le23 | s10618-022-00866-9 | A methodology for refined evaluation of neural code completion approaches |
| Gonzalez24 | s10618-024-01014-1 | Binary quantification and dataset shift: an experimental investigation |
| Airola19 | s10618-018-00607-x | The spatial leave-pair-out cross-validation method (evaluation bias / leakage) |
| Simpson26 | s10618-026-01195-x | Instance space of clustering validation measures |
| Berrar22 | s10618-022-00828-1 | Using p-values for the comparison of classifiers: pitfalls and alternatives (abstract and metadata only) |

**Ordinary recent method papers (8):** Dempster24 quant (s10618-024-01036-9); Foumani24 Series2vec (s10618-024-01043-w); Nuyts25 TSelect (s10618-025-01132-4); Panayiotou26 MOUFLON (s10618-026-01260-5); Leiber26 3CPO Poisson subspace clustering (s10618-026-01230-x); Zavitsanos26 Focused PU (s10618-026-01264-1); Chatzis25 tPARAFAC2 (s10618-025-01122-6); Gunasekara25 SGBR (s10618-025-01147-x).

**Journal guideline facts (from the submission-guidelines page):**
- Abstract of 150–250 words, with no undefined abbreviations.
- 4–6 keywords.
- Name–year citations.
- A "Statements and Declarations" heading. Submissions without the relevant declarations are returned as incomplete.
- A data availability statement for all original research.
- Decimal headings with no more than three levels.
- LaTeX with the Springer Nature template.

**How DMKD judges a regular paper (from the same page):**
1. Is the main contribution clear "after reading the abstract"?
2. Is there a clearly defined research gap? A new method alone is "typically not enough".
3. Is success shown by experiments that answer "clearly formulated research questions"?

**Other journal facts:**
- The "Survey" paper type explicitly includes "extensive independent experimental comparisons".
- Extended conference papers must say so at submission and include a statement of what changed.
- arXiv preprints are allowed if they link to the official publication.

---

## 1. Title

**Observations**
- Length: 6–18 words, median 10 (30 papers). Evaluation papers have a median of 10 and method papers a median of 8.5.
- Colon titles: 20/30. Among evaluation papers 14/22, among method papers 6/8.
- Question titles: 1/30 (Iglesias25, s10618-024-01077-0, "What do anomaly scores actually mean? …").
- Method papers mostly use "NAME: what it does for which task" (5/8: quant, Series2vec, TSelect, MOUFLON, tPARAFAC2).
- 19/22 evaluation titles contain a genre word: evaluation, benchmark(ing), review, comparative, pitfalls, challenges, investigation, taxonomy, survey or "story". The recurring templates are:
  - "X: a review and experimental evaluation of …" (Bagnall17, Ruiz21, Middlehurst24);
  - "On the evaluation of X: …" (Campos16 s10618-015-0444-8, Marques23 s10618-023-00931-x);
  - "X: experimental review" or "X: an experimental investigation" (Fanourakis23 s10618-023-00941-9, Gonzalez24 s10618-024-01014-1);
  - "X: common pitfalls and best practices" (Hewamalage23 s10618-022-00894-5);
  - "Challenges in benchmarking X with real-world data" (Souza20 s10618-020-00698-5);
  - "A methodology for refined evaluation of X" (Le23 s10618-022-00866-9).
- Playful or metaphorical main titles always come with a literal subtitle: "Navigating the metric maze: a taxonomy of evaluation metrics …" (Sorbo24), "… the story so far" (Fabris22), "… and how to find them: literature review and benchmarking" (Guidotti22).

**Recommendations**
- Keep a colon title of about 9–14 words. Put the evaluated object first and the evaluation genre in the subtitle. Two templates fit the sample well:
  - Campos16/Marques23 style: "On the evaluation of data repair: comparison contracts, benchmark infrastructure, and an empirical audit".
  - Hewamalage23/Souza20 style: "Comparison contracts for data-cleaning evaluation: pitfalls in benchmark infrastructure and how to make them explicit".
- Avoid a pure question title (1/30). Avoid DB-specific product names (BART, Raha/Baran, dbt) in the title; no evaluation-paper title in the sample names a specific tool.
- Put "evaluation" or "benchmark" in the title or keywords: 19/22 evaluation papers signal their genre this way.

## 2. Abstract

**Observations**

*Length*
- 93–292 words, median 206 (30 papers).
- 20/30 fall within the journal's 150–250 range; 6/30 are longer (up to 292, Fabris22) and 4/30 shorter (quant has 93).
- Evaluation papers run longer (median 232, 16/22 at 250 or fewer) than method papers (median 168, 8/8 at 250 or fewer).

*Opening sentence*
- 25/30 open with field context.
- 5/30 open with the authors' action: "We perform an extensive experimental evaluation" (SanchezVinces25, s10618-024-01086-z), "We show that it is possible" (quant), "We argue that" (Series2vec), "In this paper, we propose" (MOUFLON), "We propose" (Focused PU).

*Typical evaluation-paper sequence:* context → gap stated as a list of concrete deficiencies → what we did, with scale numbers → headline finding → implication for future evaluations. Examples:
- Campos16 lists four separate gaps before the study (models, benchmark data, dataset suitability, measure bias).
- Bagnall17 (s10618-016-0483-9) names exactly why earlier comparisons were incomparable: different languages, single train/test splits, normalised versus raw data.
- Le23 (s10618-022-00866-9) says aggregated metrics "blur the differences".
- Airola19 (s10618-018-00607-x) names two specific biases (pooling and spatial autocorrelation).

*Scale numbers.* 12/30 put dataset or method counts in the abstract:
- 18 algorithms × 85 datasets × 100 resamples (Bagnall17);
- 8,730 models on 97 datasets (IsmailFawaz19);
- 14 methods on 46 datasets (SanchezVinces25);
- 18,351 synthetic datasets (Simpson26);
- 200+ datasets (Fabris22);
- 20 metrics (Sorbo24).

*Findings and recommendations*
- Enumerated findings: 4/30 use "First…Second…Finally" or "(1)(2)(3)" (Rochner24, Gonzalez24, Fabris22, TSelect).
- Evaluation abstracts often end with a recommendation to the community:
  - SanchezVinces25: clustering-based methods "should be included as baselines in future benchmarking studies";
  - Sorbo24: metric choice "must be made with care";
  - Bagnall17: closes on reproducibility and a basis for "more robust testing".

*Code URL in the abstract:* 3/30 (Gonzalez24, Series2vec, 3CPO). Bagnall17 claims reproducibility in the abstract without a URL.

**Recommendations**
- Aim for 200–245 words, inside the 150–250 limit. The evaluation-paper median is 232, but the journal limit is binding.
- Use the evaluation-paper sequence:
  1. One context sentence on why data-cleaning systems are compared on benchmark infrastructure.
  2. A gap stated as concrete defects, following the Bagnall17 and Campos16 style. Here these are the comparison choices (row correspondence, value-field orientation, normalization) that are left implicit and can change scores while the native systems are correct.
  3. What you did, with numbers: how many benchmarks, systems, error types and score deltas.
  4. The headline finding, including the largest score swing.
  5. The generality claim: the same contract decomposition applies to other evaluation pipelines, for example the dbt metric-reference check.
  6. A community recommendation, such as declaring comparison contracts alongside benchmark results.
- Make the main contribution identifiable from the abstract alone. This is DMKD's first review criterion.
- Define or avoid abbreviations such as BART, dbt and ER in the abstract, as the guidelines require.

## 3. Keywords

**Observations**
- 2–11 keywords, median 4. 20/30 fall within the journal's 4–6.
- 6/30 have fewer than 4, for example Hewamalage23 with 2 and Fabris22 with 3. 4/30 have more than 6, for example SGBR with 9 and Berrar22 with 11.
- Evaluation papers usually include a literal "Evaluation" keyword, or a close variant, plus the task name:
  - Campos16: "Unsupervised outlier detection; Evaluation; Measures; Datasets";
  - Marques23: "… Evaluation; Model selection …";
  - Sorbo24: "Time series; Anomaly detection; Evaluation; Taxonomy";
  - SanchezVinces25: "Evaluation; Experimental analysis and comparison";
  - Middlehurst24: "Bake off".

**Recommendations**
- Use 5–6 keywords mixing task and evaluation terms, for example: Data cleaning; Error detection and repair; Benchmark validity; Evaluation methodology; Reproducibility; Entity/row alignment.

## 4. Introduction moves and contribution statements

**Observations**
- **Contribution list:** 16/28 full texts have an explicit list, often introduced by "In summary, our main contributions are". This holds for 10/20 evaluation and 6/8 method papers. Examples: Marques23 (9 items), SanchezVinces25 (10 list items with sub-points), Fanourakis23 (7), Grzenda20 (5), Sorbo24 (4), Middlehurst24 (4), and all method papers except quant and Focused PU.
- **Research questions:** 6/20 evaluation papers state explicit research questions or open questions; no method paper does (0/8).
  - IsmailFawaz19 (s10618-019-00619-1) poses a list of open questions.
  - Marques23 adds "we aim to answer the following research questions".
  - Fanourakis23 frames four open questions that the results answer.
  - SanchezVinces25 has a section titled "Research questions and experimental setup".
  - Le23 has 4 RQs.
  - Rochner24 phrases every results subsection as a question.
  - The guidelines' third criterion asks for this.
- **Roadmap paragraph:** at least 21/28 end the introduction with "The rest of the paper is organised as follows". Several method papers end on the contribution list instead (Series2vec, TSelect, MOUFLON, 3CPO).
- **Reproducibility promise in the introduction:**
  - Bagnall17: repository and website in the last paragraphs;
  - SanchezVinces25: subsection 1.3 "Reproducibility";
  - Le23: published dataset and scripts via footnotes;
  - Grzenda20: open-source implementation as a contribution bullet.
- **Intro subsections** are rare (1/28): SanchezVinces25 uses "1.1 Why…? 1.2 Contributions 1.3 Reproducibility".
- **Extensions of earlier publications** are declared in the introduction (2/28): Marques23 ("a major extension of our preliminary publication") and Chatzis25.
- **Selection criteria:** evaluation papers state them early. Middlehurst24 gives three inclusion criteria for algorithms; Fabris22 gives venues and years surveyed.

**Recommendations**
- Structure the introduction as:
  1. Context;
  2. A concrete motivating failure (one paragraph, one number);
  3. The gap, as a list of deficiencies;
  4. The paper's angle, introducing "comparison contract" as a named concept (see §12);
  5. 3–4 explicit research questions (RQ1–RQ4), answered one-to-one in the results, as in SanchezVinces25 and Le23;
  6. A contribution list of 4–6 items, where the last item is the released artifact;
  7. One sentence on reproducibility;
  8. A roadmap.
- If the paper extends the previous IS submission or any conference version, state it here and in the cover letter. DMKD requires a statement of revisions for extended conference papers.

## 5. Related work organisation

**Observations**
- 16/28 have a "Related work" section (variants include "Background and related work" and "Preliminaries and related work"), always as Section 2.
- The other 12/28 replace it with a background or "review of methods" section that does double duty:
  - Bagnall17 §2 "Time series classification algorithms";
  - IsmailFawaz19 "Background";
  - Middlehurst24 "Definitions and terminology" plus an algorithms section organised by taxonomy;
  - Hewamalage23 "Terminology of forecast evaluation";
  - Sorbo24 "Background".
- Inside the section, evaluation papers organise prior work by taxonomy or category rather than chronologically:
  - Middlehurst24 has 8 algorithm families;
  - Guidotti22 and Bodria23 use explanation types;
  - Fabris22 has 2.1 Algorithmic fairness surveys, 2.2 Data studies, 2.3 Documentation frameworks.
- Evaluation papers explicitly separate themselves from earlier surveys or benchmarks:
  - Guidotti22 and Bodria23: "highlights the differences between this work and previous ones";
  - Marques23: "improving on previous comparison studies in several important aspects".

**Recommendations**
- Use Section 2 "Related work" with three subsections:
  1. Data-cleaning benchmarks and error generators: BART, Raha/Baran and similar.
  2. Evaluation methodology and benchmark validity in data mining: Campos16, Bagnall17, Souza20, Hewamalage23, Sorbo24, Berrar22, Marques23. This is the subsection that signals DMKD fit.
  3. Reproducibility and specification of metrics in analytics pipelines (semantic layers).
- End each subsection with one sentence on how this paper differs.

## 6. Problem formulation and notation

**Observations**
- 13 or more of 28 contain a formal problem statement, notation section or numbered Definitions:
  - Middlehurst24: 7 Definitions;
  - Rochner24: §3 "Notation…" and 17 Definitions;
  - Guidotti22: Definitions 1–2;
  - Gonzalez24: "Notation and definitions" plus worked Examples;
  - Iglesias25: "General notation";
  - MOUFLON: "Problem statement" (Problem 1) and Definitions 1–4;
  - 3CPO: Problem 1;
  - Focused PU: Proposition/Lemma/Theorem;
  - tPARAFAC2 and Series2vec: notation / problem definition;
  - Grzenda20: "Problem statement and justification" with formal definitions in the appendix.
- Measure- or protocol-critique papers define **desired properties first** and then test every candidate against them:
  - Sorbo24 §4 "Properties" (10 properties), then §6 "Case studies" and §7 "Categorization";
  - Rochner24 requires probabilities to be "sharp, refined, and calibrated" and then derives measures.

**Recommendations**
- Add a short formal section, "Comparison contracts: definitions". It should cover:
  - the benchmark pair (clean, dirty) and the repaired output;
  - a contract C = (row correspondence, value-field orientation, normalization, …);
  - the score as a function of the contract.
- Then state desiderata, for example "contract-invariance of a correct system" or "explicitness". This mirrors Sorbo24 and Rochner24, and makes "responsibility per analysis step" a formal object rather than prose.

## 7. Method / procedure sections

**Observations**
- Evaluation papers usually put a "procedure" section before the results:
  - Bagnall17 "Data and experimental design";
  - Middlehurst24 "Experimental procedure" with 3.2 "Reproducibility";
  - Marques23 "Experimental setup" with Algorithms; Datasets; Experimental scenarios; Evaluation measures; Model selection; Ensemble;
  - Fanourakis23 "Experimental setting" with Datasets; Statistics and meta-features; Evaluation protocol and metrics; Pre-processing pipelines; Implementation details.
- Protocol papers present the new evaluation procedure as the "method":
  - Grzenda20 "New delayed evaluation methodology";
  - Le23 "Approach" with 3.1 "Methodology for a refined evaluation";
  - Gonzalez24 "Types of dataset shift" with protocols for generating shifted data.
- Method papers have a single method section, sometimes ending with a "Complexity" or "Time complexity" subsection (quant, TSelect, 3CPO, Bagnall17 §2.6).

**Recommendations**
- Present the audit procedure as the method, as Grzenda20 and Le23 do. Cover:
  - (i) how comparison choices are enumerated;
  - (ii) how each choice is varied while the system output is held fixed;
  - (iii) how a native-system "ground truth of correctness" is established;
  - (iv) the reference implementation, including the dbt check.
- Close with a "Pre-processing pipelines / implementation details" subsection, as in Fanourakis23.

## 8. Experimental design and how evaluation papers argue generality

**Observations**

*Datasets.*
- Nearly all papers use multiple datasets. Examples of scale: 85–142 UCR/UEA datasets (Bagnall17, Middlehurst24, quant), 46 (SanchezVinces25), 18,351 synthetic (Simpson26), 11–14 (SGBR, Focused PU), 6 streams (Grzenda20).
- Only Airola19 (18 pages) rests on a single application case study.

*Baselines.*
- Bake-off papers fix "standard benchmark classifiers" (Bagnall17: DTW and Rotation Forest).
- SanchezVinces25 compares against non-clustering baselines. Fanourakis23 adds a non-learning baseline (PARIS).

*Statistical testing.*
- 13/28 full texts use a formal multiple-comparison test: 9/20 evaluation and 4/8 method papers. Tests used: Friedman, Wilcoxon signed-rank, Holm, Nemenyi, Shaffer, or the Wilcoxon-based multiple comparison matrix.
- CD diagrams appear as results figures in 8/28: Bagnall17, IsmailFawaz19, Ruiz21, Middlehurst24, Marques23, SanchezVinces25, Simpson26, TSelect. Hewamalage23 recommends them in its guidance.
- The 11/20 evaluation papers *without* NHST are the measure, protocol and dataset critiques: Hewamalage23, Sorbo24, Iglesias25, Rochner24, Fabris22, Guidotti22, Bodria23, Souza20, Grzenda20, Le23, Airola19. They argue through controlled constructions, defined properties and counter-examples, not leaderboards.
- Berrar22 (s10618-022-00828-1) cautions that p-values from Friedman and Wilcoxon tests overstate evidence and proposes alternatives.

*Ablation and sensitivity.*
- Ablation is a method-paper convention: 3/8 have an ablation subsection (Series2vec, 3CPO, TSelect) against 0/20 evaluation papers.
- Sensitivity or parameter analysis appears in 6/8 method papers and at least 5/20 evaluation papers:
  - Iglesias25: "Sensitivity analysis" with one "Effect of X" subsection per factor;
  - SanchezVinces25: "Resilience to parameter configuration";
  - Grzenda20: "Analysis of hyper-parameters";
  - Le23: "Auxiliary experiments";
  - Marques23: model selection.

*Runtime.*
- Reported in 10/20 evaluation and 6/8 method papers. Examples: SanchezVinces25 "Scalability" with a runtime-versus-size figure; Grzenda20 "Computational cost and memory consumption"; TSelect, where runtime is central.

*How evaluation papers argue generality across domains and datasets.* Seven distinct moves:
1. **Domain breadth of the testbed.**
   - Ruiz21 organises its archive section by domain (biosignals, accelerometer, coordinates, audio, other).
   - Middlehurst24 lists more than ten application domains.
   - Bagnall17 analyses results "by problem type".
2. **Same evaluation template repeated across data modalities.** Bodria23 (s10618-023-00933-9) has a section each for tabular, image and text data, and each ends with a "… quantitative comparison" subsection.
3. **Controlled factor sweeps.**
   - Iglesias25: size, dimensionality, outlier ratio, density, clusters, local outliers;
   - Gonzalez24: one experiment per shift type;
   - Rochner24: controlled calibration;
   - Chatzis25: noise and missingness grids.
4. **Meta-feature or instance-space analysis** linking outcomes to measurable dataset properties.
   - Fanourakis23: "Meta-level analysis";
   - Simpson26: instance-space footprints;
   - Bagnall17 §4.5: characteristics of the problem.
5. **"Extensions" sections** carry the protocol to other task types. Grzenda20 §7 covers regression, evolving instances and weighted bins.
6. **A literature-usage survey** shows the problem is widespread.
   - Fabris22: 500+ articles across 7 venues;
   - Le23: survey of state-of-the-art benchmarks;
   - Sorbo24: review of metric usage;
   - Souza20: "Stream datasets from literature".
7. **A real-world application section** after the controlled experiments: MOUFLON, Focused PU, Souza20 (insect sensor streams), Chatzis25.

**Recommendations**
- The editor's comment ("breakdown of responsibility to different steps … appreciated more where it is extended to other domains") maps directly onto moves 2 and 5. Add a section "Beyond data repair: comparison contracts in other evaluation pipelines". Apply the same contract decomposition, using the same table template, to 2–3 DM evaluation settings where implicit comparison choices are documented in DMKD itself:
  - (a) row/instance correspondence in entity resolution or entity alignment evaluation. Fanourakis23 has a "Pre-processing pipelines" subsection.
  - (b) point-versus-range alignment and label orientation in time-series anomaly detection metrics (Sorbo24).
  - (c) normalisation and scaling choices in forecasting and TSC evaluation. Hewamalage23 shows scale-dependent error measures; Bagnall17 found normalised versus raw data inconsistent across studies.
  - (d) label/score orientation in outlier evaluation (Campos16, Marques23).
  - (e) the dbt metric-reference check, as an analytics-pipeline instance.
  Each needs only a small worked case showing that a contract choice changes the score. A single table that maps contract components to pipeline steps across domains is the "responsibility breakdown" extended.
- Add one controlled factor sweep (move 3): vary each contract component independently over several benchmarks and error types, and report the score delta.
- If you report score changes over many benchmark datasets, add a Wilcoxon signed-rank test (with Holm correction) and effect sizes, or a CD-style summary. DMKD readers in the bake-off tradition (8/28 CD diagrams) expect this. Following Berrar22, emphasise effect sizes and intervals over p-values.
- Report runtime and overhead of the reference checker, as 16/28 papers report runtime.
- Do not invent an ablation. For an audit paper, "contract-component sensitivity" plays that role.

## 9. Results writing

**Observations**
- Results subsections often mirror the research questions or factors one-to-one:
  - SanchezVinces25 "Investigation": Accuracy; Resilience to data variation; Resilience to parameter configuration; Automatized parameter selection; Scalability;
  - Rochner24: question-form headings;
  - Gonzalez24: one subsection per shift type.
- 6/28 add a qualitative "closer look" or lessons subsection after aggregates:
  - Bagnall17 §6 "A closer look at specific problems";
  - Ruiz21 "Explanatory analysis case studies";
  - Fanourakis23 "Lessons learned";
  - Gonzalez24 "A final note about our experiments";
  - Rochner24 "Practical considerations";
  - Fabris22 "Broader relevance to the community".
- Separate "Analysis" or "Discussion" after the results is common in evaluation papers (Middlehurst24 "Analysis"; see §10).

**Recommendations**
- One results subsection per RQ, each opening with a one-sentence answer.
- Then add a "Lessons for benchmark designers and users" subsection with numbered take-aways, in the style of Fanourakis23 and Hewamalage23.

## 10. Discussion and limitations

**Observations**
- A separate Discussion section appears in 8/28: SanchezVinces25, Le23, Airola19, Simpson26, Souza20 ("Evaluation and Discussion"), TSelect, MOUFLON, and 3CPO ("Discussion and conclusions").
- A standalone "Limitations" section appears in only 2/28 (3CPO, SGBR). "Threats to validity" appears in 1/28 (Le23, inside the Discussion).
- Limitations are nonetheless mentioned in the text of 24/28.
- Sorbo24 puts its scope and limitations in a §3 "Method" section, up front.

**Recommendations**
- Add a "Discussion" section with a "Threats to validity" subsection, as in Le23. Cover:
  - which benchmarks and systems were audited;
  - whether the native-system correctness criterion could itself be contract-dependent;
  - how far the cross-domain demonstrations generalise.
- This is uncommon in DMKD but well suited to an audit paper, and it pre-empts reviewer objections.

## 11. Conclusion

**Observations**
- 25/28 use "Conclusion(s)". The variants are "Conclusions and future work" (Fanourakis23), "Conclusions and recommendations" (Fabris22) and "Discussion and conclusions" (3CPO). SanchezVinces25 splits into 7.1 Summary and 7.2 Outlook.
- Evaluation conclusions open by restating the goal or finding:
  - Bagnall17: "The primary goal … is to promote reproducible research", then "We view data mining as a practical area";
  - Airola19: restates the "dangers" shown;
  - Hewamalage23: contrasts forecasting evaluation with established practice elsewhere.

**Recommendations**
- Write "Conclusions and recommendations" in Fabris22 style: three short paragraphs covering what was shown, recommendations for benchmark maintainers and users (a checklist of contract fields to report), and an outlook.

## 12. Naming the problem and repositioning (rhetorical moves specific to audit papers)

**Observations**
- Strong DMKD audit papers name the problem or flaw class:
  - Fabris22 (s10618-022-00854-z): "data documentation debt", with sub-names opacity and sparsity;
  - Souza20 (s10618-020-00698-5): a five-part critique taxonomy, from "uncertainty about changes" and "temporal dependence" to "streaming as an afterthought";
  - Hewamalage23: pitfalls grouped by evaluation step;
  - Airola19: "pooling bias" and "spatial bias".
- They pair the critique with a constructive artifact:
  - a repository (Souza20);
  - standardised documentation (Fabris22);
  - a methodology (Le23 CT3; Grzenda20);
  - a taxonomy (Sorbo24);
  - a companion website (Bodria23 "XAI Live Survey");
  - open code for every experiment (Bagnall17, Middlehurst24).
- They question the suitability of popular benchmarks:
  - Fabris22 on Adult, COMPAS and German Credit;
  - Campos16 on outlier datasets;
  - Simpson26 on the diversity of earlier benchmark collections.

**Recommendations**
- Keep "comparison contract" as the named concept. Give the failure modes names in a short taxonomy, for example correspondence ambiguity, orientation ambiguity and normalization ambiguity, and present it as a figure or table early on.
- Pair the critique with the released checker as the constructive artifact.
- Present "native systems are correct but scores move" as the headline counter-example. It plays the same role as Airola19's near-perfect AUC for near-random classifiers.

## 13. Figures and tables

**Observations**
- Figures: 3–50, median 13.5 (28). Tables: 0–35, median 6 (28). Evaluation papers have a median of 15 figures and 6 tables; method papers 10 and 5.5.
- **First figure is an illustrative toy example** in 12 or more of 28:
  - Sorbo24 Fig. 1: a hypothetical anomaly/label scenario;
  - Iglesias25: a simple dataset with ten inliers and two outliers;
  - Rochner24: sharpness/refinement/calibration example;
  - Le23: aggregated versus refined accuracy on one snippet;
  - Grzenda20: the "flight problem";
  - Fanourakis23: two KGs to align;
  - Gonzalez24: synthetic shift examples;
  - also Bagnall17, Marques23, MOUFLON, 3CPO, TSelect.
- **CD diagrams:** 8/28 (see §8). Captions name the scenario and what bars or cliques mean, for example Marques23's "Critical difference diagrams with average ranks of the methods over all Type I experiments" and IsmailFawaz19's caption explaining the thick horizontal line.
- **Other recurring figure types:**
  - pairwise accuracy scatter plots and multiple comparison matrices (quant, Middlehurst24, Series2vec);
  - flowcharts for guidance (Hewamalage23 decision flowcharts for data partitioning, error measures and test selection; Simpson26 process flowchart);
  - taxonomy trees (Sorbo24, Bodria23);
  - runtime-versus-size curves (SanchezVinces25, MOUFLON, 3CPO).
- Large result tables go to appendices: Middlehurst24 has 23 tables, TSelect 35, mostly in appendices.
- Captions are descriptive, often more than one sentence. The guidelines require "descriptive captions" and colour-blind-safe patterns.

**Recommendations**
- Fig. 1: one toy table pair (clean/dirty/repaired) where two contracts give different F1 for the same correct repair.
- Fig. 2: a contract taxonomy or pipeline diagram showing which step owns which choice. This is where the "responsibility breakdown" appears visually.
- Main results: a heat-map or table of score deltas by contract component × benchmark. If many datasets are involved, add one CD diagram or a Wilcoxon summary.
- Cross-domain section: one compact table with rows for domains and columns for contract components.
- Use self-explanatory captions of two or three sentences. Move per-dataset tables to the appendix or supplementary material.

## 14. References

**Observations**
- **Count:** 25–617, median 65 (30). 25/30 have 40–150. Evaluation papers have a median of 83 and method papers 52. The outliers are surveys: Fabris22 617, Bodria23 177, Guidotti22 151.
- **Style:** author–year in 28/28 full texts. The guidelines mandate name–year, alphabetical lists and Springer basic style. No numbered style appears.
- **Venue mix** (automatic count over Springer reference lists, n=30):
  - ≥1 DMKD reference in 23/30 (median 2, about 3% of references). The TSC bake-offs cite DMKD heavily: 11 in Bagnall17, 13 in Ruiz21, 24 in Middlehurst24.
  - ≥1 KDD reference in 27/30.
  - ≥1 database-venue reference (VLDB, SIGMOD, ICDE, EDBT or CIDR) in 16/30. This is 15/22 evaluation papers against 1/8 method papers. For example, SanchezVinces25 has 15 and Campos16 has 10.
  - ≥1 arXiv reference in 25/30.
  - Share of references from the last 5 years: median 0.445 (0.09–0.84).
- **Self-citation** (approximate surname match): median 12.5% of references (0.3%–38%). It is high in group-driven bake-offs, for example Middlehurst24 with 26 and Campos16 with 27.
- **Software and data citation:**
  - Bagnall17 cites its website as a reference;
  - Iglesias25 cites a DOI-citable TU Wien data repository;
  - Simpson26 gives a figshare DOI;
  - Middlehurst24 links an evaluation-package documentation page;
  - Ismail Fawaz19 gives a GitHub link in a footnote.

**Recommendations**
- Target 60–100 references, author–year, using the Springer Nature LaTeX template (`sn-jnl`, `sn-basic`).
- Keep the VLDB/SIGMOD data-cleaning core. Evaluation papers in DMKD routinely cite DB venues (15/22).
- Add 8–15 data-mining evaluation-methodology references: Demšar 2006 JMLR (cited across the bake-offs), Benavoli et al., Campos16, Bagnall17, Souza20, Hewamalage23, Sorbo24, Marques23, Berrar22, Fabris22, plus relevant KDD and ECML PKDD work.
- Cite the dataset and software versions you audited (BART, Raha/Baran releases, dbt version) as references or with archived DOIs.
- Keep self-citation near or below the median (about 10–15%).

## 15. Length norms

**Observations**
- Journal pages (Springer layout): 18–79, median 45. 25/30 are 25–60 pages. Evaluation papers have a median of 48 and method papers 35.
- Body text (full-text HTML, excluding references): evaluation papers about 11k–22k words, median about 14k; method papers about 6k–13k, median about 8k.
- Top-level numbered sections: 5–11, median 7. The guidelines allow at most three heading levels.

**Recommendations**
- Aim for about 10–13k words of body text, roughly 30–40 journal pages including figures. Use 6–8 top-level sections.
- A suggested outline:
  1. Introduction
  2. Related work
  3. Comparison contracts: definitions and properties
  4. Audit procedure and reference implementation
  5. Experimental setup (RQs, benchmarks, systems, metrics, reproducibility)
  6. Results (one subsection per RQ, then lessons learned)
  7. Beyond data repair: contracts in other evaluation pipelines
  8. Discussion and threats to validity
  9. Conclusions and recommendations
  10. Statements and Declarations

## 16. Reproducibility and code/data statements; Statements & Declarations

**Observations**

*Code and data links*
- 20/28 full texts link code or data publicly (GitHub, Bitbucket, a project site, figshare or a DOI repository).
- Where the link sits:
  - in a dedicated end-matter statement or numbered section in 7 (Middlehurst24, Marques23, Iglesias25, Guidotti22 inside its Ethics declarations, Bodria23, Simpson26, Chatzis25);
  - in the abstract in 3 (Gonzalez24, Series2vec, 3CPO);
  - in the introduction or a contribution footnote in 9 (Bagnall17, Ruiz21, SanchezVinces25 §1.3, Grzenda20, Le23, TSelect, Focused PU, IsmailFawaz19, Souza20);
  - in the method section in 1 (quant).
- Best practice in the sample combines a GitHub link with an archived DOI (Iglesias25 GitHub plus TU Wien DOI; Simpson26 figshare DOI). Middlehurst24 adds a "Reproducibility" subsection in the experimental procedure.

*Statements and declarations*
- Among the 26 Springer full-text HTML pages, an "Ethics declarations" block appears in 16/26, and every one includes Competing or Conflict of interest. For papers from 2023 on, it is 14/18.
- The headings used:
  - 11 have conflict of interest only;
  - 4 use the full Springer set: Conflict of interest, Ethics approval, Consent to participate, Consent for publication (Middlehurst24, Guidotti22, Bodria23, Chatzis25; Guidotti22 also nests "Code availability" there);
  - 1 adds "Ethical approval" for register data (MOUFLON).
- Data availability statements in papers from 2023 on: 10/18. Separate "Code availability" headings: 3/18 (Middlehurst24, Bodria23, Chatzis25).
- 4 of those 10 data statements are the boilerplate "No datasets were generated or analysed during the current study", even though public datasets were analysed (SanchezVinces25, 3CPO, Focused PU, SGBR).
- Three papers disclose that a co-author is a DMKD action editor (Iglesias25, SanchezVinces25, Rochner24).
- Funding is a separate heading in most papers from 2022 on.

**Recommendations**
- Put a "Statements and Declarations" heading before the References. The guidelines use this exact heading and return submissions without it. Include:
  - Competing interests;
  - Funding;
  - Data availability: name every benchmark, its version and source URL or DOI, and how the generated dirty/repaired pairs can be obtained;
  - Code availability: a GitHub link plus a Zenodo DOI for the exact commit;
  - Ethics approval: not applicable;
  - Author contributions.
- Do not use the boilerplate "no datasets were generated or analysed". The guidelines ask for the minimal dataset needed to replicate the results.
- Also add a "Reproducibility" subsection in the experimental setup (Middlehurst24, SanchezVinces25) and one sentence in the introduction.
- If review is anonymised, mask the repository. The guidelines suggest anonymising data authorship.

## 17. Specific lessons for repositioning a database-oriented benchmark-audit paper for DMKD

These are synthesized recommendations; supporting observations are cited inline.

1. **Choose the paper type deliberately.** Submit as a Regular paper: the comparison-contract methodology and checker are new research contributions, as in Grzenda20 and Le23. Make the research gap and RQs explicit, because those are DMKD's stated criteria. The "Survey" type covers independent experimental comparisons, but the manuscript is more than that.
2. **Recast the contribution as evaluation methodology for data mining, not as a database-systems bug report.** The closest DMKD analogues all frame flaws in evaluation infrastructure as threats to scientific conclusions:
   - Campos16 (datasets + measures);
   - Souza20 (benchmark-data critique + repository);
   - Hewamalage23 (pitfalls by pipeline step);
   - Sorbo24 (metric properties);
   - Le23 (refined evaluation reveals hidden differences);
   - Airola19 (biased CV produces misleading AUC).
   Open with the consequence for comparative conclusions ("systems may be ranked differently"), not with an implementation detail of BART or Raha/Baran.
3. **DMKD has almost no data-cleaning papers.** Crossref title/abstract queries over 1573-756X for "data repair", "data cleaning", "deduplication" and "dirty data" in 2015–2026 returned no data-repair benchmark papers, and very few entity-resolution papers (for example "Fast schemes for online record linkage", s10618-018-0563-0, not open access). So:
   - explain the task and benchmark ecosystem in about one page, assuming no DB background (the guidelines expect application background to be explained);
   - translate jargon: row correspondence → instance alignment or record matching; value-field orientation → which attribute/value is scored and in which direction; normalization → canonicalisation before comparison;
   - define every abbreviation.
4. **Answer the editor's comment structurally:** add the cross-domain section (§8 recommendation). Use the same contract decomposition in a single comparative table, following the Bodria23 per-modality template and the Grzenda20 "Extensions" section. Use DMKD-documented settings (entity alignment, anomaly-detection metrics, forecasting normalisation, outlier label orientation) and the dbt semantic layer. This turns "responsibility per analysis step" into a reusable framework.
5. **Give generality evidence the DMKD way:**
   - more benchmarks and error types, with numbers in the abstract;
   - a controlled factor sweep with one "Effect of X" subsection per contract component (Iglesias25, Gonzalez24);
   - optionally, a short literature-usage survey counting how many published data-cleaning evaluations state each contract choice (Fabris22, Le23, Sorbo24).
6. **Use statistics proportionately.** For score deltas over many datasets, use paired Wilcoxon or Holm tests and effect sizes, with a CD diagram if ranking systems. For counter-example demonstrations, use controlled constructions without NHST (11/20 evaluation papers do so), and cite Berrar22 for restraint with p-values.
7. **End with community recommendations:**
   - a short reporting checklist ("comparison-contract card") that benchmark maintainers should publish;
   - recommended defaults;
   - the checker as a released tool.
   SanchezVinces25 and Fabris22 end this way.
8. **Use the journal's formatting:**
   - Springer Nature LaTeX template;
   - author–year citations;
   - at most three heading levels;
   - an abstract of 150–250 words;
   - 4–6 keywords;
   - "Statements and Declarations";
   - a substantive data availability statement;
   - an archived code DOI.
9. **Disclose prior submission history if relevant.** If any part appeared at a conference, declare it with a revisions statement (Marques23 and Chatzis25 do this in the introduction). Rejection history at Information Systems normally goes only in the cover letter, if anywhere.

---

### Caveats
- Campos16 and Berrar22 could not be read in full: they are not open access, and no legitimate full-text copy was found. Their rows contain only abstract, keyword, pagination and reference-list data.
- IsmailFawaz19 and Souza20 were read from accepted arXiv versions. Their figure and table counts and section lists come from the preprints; page counts and reference counts come from Springer metadata.
- Several 2023+ papers (Gonzalez24, quant, Series2vec, TSelect) show no declarations block in the HTML. This may be a rendering difference rather than an absence in the PDF.
- Self-citation counts use surname matching and are approximate. Venue counts use regular expressions over reference strings and may slightly undercount abbreviated venue names.
