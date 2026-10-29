# Observed ESWA papers and statistics (collected 2026-10-29)

Extracted from the evidence notes behind this skill. Sources: OpenAlex and Crossref APIs (ISSN 0957-4174), arXiv HTML full texts of ESWA papers, archived 2023/2024 and live 2026 Guide for Authors. Items tagged [UNVERIFIED] could not be confirmed. Where the 2023/2024 guide differs from the live 2026 guide (single vs double anonymized review, keyword limit, abstract limit), the 2026 guide wins (see submit-eswa).

## 1. Titles

### 1.1 Statistics (from `eswa_title_abstract_ref_stats.csv`)

| Sample | n | Words: median (IQR; range) | Has colon | "Name/ACRONYM:" prefix | Contains an acronym | Contains "for" | Starts with "A/An" | Contains "framework" | Mentions LLM |
|---|---|---|---|---|---|---|---|---|---|
| Relevant (all 4 groups) | 51 | **12** (10–15; 5–19) | 41% | 22% | 37% | 63% | 6% | 14% | 41% |
| LLM group | 23 | 12 (10–16; 8–19) | 48% | 26% | 52% | 70% | 0% | 22% | 87% |
| UQ/conformal/selective | 11 | 12 (8–14; 5–18) | 45% | 9% | 18% | 55% | 9% | 9% | 0% |
| Hierarchical text classification | 7 | 10 (10–12; 9–12) | 14% | 14% | 29% | 57% | 14% | 14% | 0% |
| AL/HITL/noisy labels | 10 | 10.5 (9–15.5; 7–17) | 40% | 30% | 30% | 60% | 10% | 0% | 10% |
| **Random ESWA 2024–26** | 200 | **12** (10–14; 5–25) | 45% | 29% | 48% | 60% | 10% | 8% | 4% |

### 1.2 Patterns (with examples)

1. **"NAME: what it does + for/in + application" (about 25–30%).** Examples:
   - "KA2L: A knowledge-aware active learning framework for LLMs" (2026, 10.1016/j.eswa.2026.133951)
   - "NoiseLLM: JoT-guided LLM reasoning for label noise-robust cybersecurity event detection" (2026, 10.1016/j.eswa.2026.132572)
   - "HeteroHTC: Enhancing Hierarchical Text Classification via Heterogeneity Encoding of Label Hierarchy" (2025, 10.1016/j.eswa.2025.126558)
   - "LLD-OSN: An effective method for text classification in open-set noisy data" (2025, 10.1016/j.eswa.2025.128339)
   - "MMAP-Net: Missing-aware multimodal fusion for multi-label retinal disease classification with score-calibrated deferral" (2026, 10.1016/j.eswa.2026.133628)
2. **Descriptive noun phrase with "for <application/task>" and no colon (the most common form).** Examples:
   - "Enhancing food safety review classification with large language models and label embedding" (2025, 10.1016/j.eswa.2025.127550)
   - "Contrastive learning with large language models for medical code prediction" (2025, 10.1016/j.eswa.2025.127241)
   - "Adaptive micro- and macro-knowledge incorporation for hierarchical text classification" (2024, 10.1016/j.eswa.2024.123374)
   - "Risk-aware classification via uncertainty quantification" (2025, 10.1016/j.eswa.2024.125906)
3. **"Problem/claim: An application of / A ... framework for ..." (two parts).** Examples:
   - "Carbonation depth assessment of recycled aggregate concrete: An application of conformal prediction intervals" (2024, 10.1016/j.eswa.2024.126231)
   - "From prediction to decision support: A transfer-aware and uncertainty-calibrated evaluation framework for short-horizon electric-vehicle energy and range forecasting" (2026, 10.1016/j.eswa.2026.134259)
   - "Beyond scaling: Capability and evidence boundaries of large language models for trustworthy misinformation verification" (2026, 10.1016/j.eswa.2026.134061)
4. **Claim-style or empirical-study titles (rarer).** Examples:
   - "Stylometry recognizes human and LLM-generated texts in short samples" (2026, 10.1016/j.eswa.2025.129001)
   - "Possibilities and limitations of using large language models (LLMs) for alert classification and prioritisation in security operations centers (SOCs)" (2026, 10.1016/j.eswa.2026.133194)
5. **An application or domain term appears in the title of most LLM papers.** In my manual coding of the 23 LLM-group titles, 15 of 23 (about 65%) name a concrete domain: chest X-ray reports, aircraft fault maintenance, food safety, power-system inspection, medical codes, SOC alerts, cybersecurity events, IT job postings, crisis tweets, spear phishing, and others. The other 8 name only an ML task, for example KA2L or "Topic modeling and alignment with large language models for multi-labeled text corpora" (10.1016/j.eswa.2025.130958).
6. **Capitalisation.** ESWA's published metadata (Crossref and OpenAlex) is mostly in **sentence case**, with a capital letter after the colon. Example: Crossref gives "Calibrated explanations: With uncertainty information and counterfactuals" where the arXiv title is "Calibrated Explanations: with Uncertainty Information and Counterfactuals". A few titles keep Title Case (HeteroHTC, CELLMEA).
7. **Guide rule.** The guide says the title should be "Concise and informative … Avoid abbreviations and formulae where possible" (Guide for Authors, Wayback 2023-10-10 and 2024-02-10). In practice about 29% of random titles start with a coined acronym, so acronym-name titles are tolerated.
8. **"Hierarchical" and "LLM" titles relevant to LLM-annotation quality control**:
   - "Standardizing longitudinal chest X-ray report evaluation via large language model annotation" (2026, 10.1016/j.eswa.2026.134237)
   - "Crowdsourcing truth inference under behavioral uncertainty using Kelly-inspired risk-aware allocation" (2026, 10.1016/j.eswa.2026.134057)
   - "Confidence-aware semantic–numerical fusion via selective prediction for mutual fund style classification" (2026, 10.1016/j.eswa.2026.134442)
   - "Label-wise reliability-aware classifier for robust chest X-ray multi-label classification" (2026, 10.1016/j.eswa.2026.131438)
   - "A transformer based framework for hierarchical enterprise data classification with empirical validation" (2026, 10.1016/j.eswa.2026.132729)

## 3. Section structure (10 arXiv full texts of ESWA papers)

### 3.1 Surveyed papers

| # | arXiv | DOI (ESWA) | Year (vol) | Topic | Top-level sections | Intro words | Contribution bullets | Figs | Tables | Refs (published, Crossref) | Body words (approx) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2603.17566 | 10.1016/j.eswa.2026.133951 | 2027 (333) | KA2L: LLM active learning / annotation cost | Intro · Related Work · Method · Experimental Setup · Experimental Results · Analysis and Discussion (…6.5 Computational cost, 6.6 Limitations) · Conclusion and Future Works · Declarations | 887 | 3 numbered | 3 | 14 | 54 | 10.7k |
| 2 | 2305.02305 | 10.1016/j.eswa.2024.123154 | 2024 | Calibrated Explanations (Venn-Abers, UQ) | Intro · Background · Definition · Presentation · Experiments · Discussion · Conclusion · Declarations | 1095 | 5 numbered ("key characteristics") | 6 | 3 | 50 | 8.0k |
| 3 | 2602.13571 | 10.1016/j.eswa.2026.131627 | 2026 | LLM-confidence reranker (LLM UQ for RAG) | Intro · Related Work · Methodology · Evaluation and Discussion (8 subsections: retrievers, thresholds, sensitivity, LMs, UQ methods, mechanism) · Conclusion | 698 | 4 numbered | 7 | 3 | 63 (arXiv: 81) | 8.0k |
| 4 | 2507.00838 | 10.1016/j.eswa.2025.129001 | 2026 (296) | Stylometry: human vs LLM text | Intro · Related works (7 subsections) · Methodology · Results · Discussion (Limitations; Commercial applications) · Further works · Source code | 821 | 6 bold-labelled | 6 | 11 | 87 | 11.7k |
| 5 | 2512.06694 | 10.1016/j.eswa.2026.133996 | 2027 (333) | TopiCLEAR: topic discovery for short texts | Intro · Related Work · Proposed Framework · Experimental Setup · Quantitative Eval (incl. Ablation) · Qualitative Eval · Conclusion · Appendices A–E | 553 | 2 ("twofold") | 4 | 18 | 45 | 7.3k |
| 6 | 2512.16189 | 10.1016/j.eswa.2026.132966 | 2026 | Healthcare LLM hallucination fact-checking | Intro · Related Work · Methodology · Experiments (incl. clinical expert evaluation) · Results · Discussion and Future Work · Conclusion | 1035 | 3 bullets | 6 | 9 | 65 | 13.1k |
| 7 | 2610.13207 | 10.1016/j.eswa.2026.131178 | 2026 (309) | SharP: LLM augmentation + uncertainty-based selection | Intro · Related Work · Method · Experiments (setup, baselines, ablation, sensitivity) · Conclusion and Future Work · Appendix | 1074 | 3 numbered + code sentence | 7 | 8 | 39 | 9.2k |
| 8 | 2303.04548 | 10.1016/j.eswa.2022.119496 | 2023 | MONITOR: crowdsourced annotation quality | Intro · Belief functions · Related work · MONITOR · Crowdsourcing campaigns · Results · Conclusion | 1340 | none (3 research questions) | 14 | 14 | 43 (arXiv) | 13.6k |
| 9 | 2410.08814 | 10.1016/j.eswa.2024.125337 | 2025 (262) | CrisisSpot: disaster content classification + new dataset | Intro (run-in headed paragraphs) · Related Work · Problem Definition · Methodology · Experimental Evaluations · Discussion (Advantages; Limitations and Future Work; Computational Efficiency and Scalability) · Conclusion | 1540 | 6 numbered | 5 | 9 | 64 | 19.1k |
| 10 | 2412.03391 | 10.1016/j.eswa.2024.125906 | 2025 | Risk-aware classification via UQ | Intro · Motivation and Desiderata · EDL Revisited · Risk-aware Classification · Evaluation · Discussion and Related Work · Conclusions | 536 | none (section roadmap) | 7 | 1 | 67 | 10.0k |

Medians across the 10 papers: intro about 960 words (range 536–1540), body about 10.4k words (range 7.3k–19.1k), 6 figures (range 3–14), 9 tables (range 1–18) and 58.5 references (range 39–87).
The manusights.com claim of "8,000 to 12,000 words across 25 to 35 pages … 6 to 12 figures" is broadly in line with these numbers, but that site is a commercial source and the claim is [UNVERIFIED].

### 3.2 Introduction: paragraph-level organisation

The typical sequence, seen in KA2L, LCR, SharP, the healthcare paper and CrisisSpot, runs as follows:
1. **P1 – Domain importance.** Real-world stakes come first (fake news, clinical safety, disaster response, LLM fine-tuning cost).
2. **P2–P3 – Existing approaches and their limits**, with dense author–year citations.
3. **P4 – The gap or central question.** SharP states it explicitly: "This paper addresses a central question: How can LLMs be guided to …".
4. **P5 – "To address this, we propose NAME"**, with a one-paragraph sketch of the mechanism.
5. **Contribution list.** It is introduced by "The main contributions of this paper/work/study are (summarized) as follows:" and appears in 8 of 10 papers, with 2–6 items (median 3.5). Items begin with verbs ("We propose…", "We innovatively bridge…", "Through extensive experiments on nine open-source LLMs and three datasets, we demonstrate…"). The last item is usually an empirical claim with numbers.
6. **Roadmap paragraph** ("The remainder/rest of this paper is organized as follows: Section 2…"), present in 7 of 10 papers.

Variants:
- CrisisSpot uses bold run-in paragraph heads: "Role of Social Media during Disaster Events", "Challenges in Leveraging …", "Existing Multimodal Paradigms and Limitations", "Addressing Research Gaps: Our Solution at a Glance" and "Key Contributions".
- MONITOR poses research questions as a dashed list.
- KA2L adds a separate "4.4 Research Questions" subsection in the experimental setup.

The guide itself says the introduction should "State the objectives of the work and provide an adequate background, avoiding a detailed literature survey or a summary of the results" (Guide 2023/2024). In practice, most papers still preview their headline results in the contribution bullets.

### 3.3 Other sections

- **Related Work** is its own Section 2 in 7 of 10 papers, usually with 2–4 thematic subsections that end in the gap (KA2L: "Active Learning for LLMs / LLM Hallucination Detection / Hidden State Decoding").
  - Four papers put a **comparison table of prior work** in Related Work or Evaluation: the healthcare paper's Table 1, SharP's Tables 1–2, LCR's Table 1 and CE's Table 3.
- **Method** is titled "Method", "Methodology", "Proposed Framework: NAME" or by the system name ("MONITOR"). It often opens with "Problem Formulation/Definition" (KA2L 3.1, SharP 3.1, CrisisSpot §3) and a notation table (SharP Table 3).
- **Experimental Setup** is often separate from Results (KA2L, TopiCLEAR, and CE 5.1). Typical subsections: datasets, baselines, metrics, implementation details, research questions.
- **Results and Analysis** has subsections named by findings, for example KA2L 5.1 "KA2L-Guided Fine-tuning Achieves Superior Cost-Efficiency and Effectiveness". Analyses are titled "Impact of …" (LCR 4.3–4.7) or "Robustness of …".
- **Discussion** appears as (part of) a section title in 7 of 10 papers: "Analysis and Discussion", "Evaluation and Discussion", "Discussion and Future Work", "Discussion and Related Work" or plain "Discussion". It often contains **Limitations** (explicit subsection in KA2L 6.6, Stylometry 5.1 and CrisisSpot 6.2), "Commercial applications" (Stylometry 5.2), "Advantages over Existing Works" or "Computational Efficiency and Scalability" (CrisisSpot 6.1/6.3).
- **Managerial implications** sections are **not typical** for CS-style ESWA papers: 0 of 10 in the full-text sample. In the OpenAlex full-text subset, "managerial implications" occurs in 0.6% of papers and "practical implications" in 5.3%. Practical value is instead woven into the Introduction, Discussion and Conclusion.
- **Conclusion** is often "Conclusion and Future Work(s)": 1–3 paragraphs that summarise the method, the quantified results and future directions.
- **Back matter** includes a CRediT author statement, a declaration of competing interests, a data-availability statement, Acknowledgements and the "Declaration of generative AI and AI-assisted technologies in the writing process". The generative-AI declaration appears as its own section in 5 of 10 arXiv versions; the guide gives the exact template wording. ESWA uses numbered sections and subsections (1, 1.1, 1.1.1), as the guide requires.
- **Appendices** are used for prompt templates (SharP Appendix A), extra metrics or robustness checks (TopiCLEAR A–E) and case material.

## 4. Experiment conventions

- **Datasets.** Usually 2–6 public benchmarks, plus a new dataset when one is contributed:
  - KA2L: 3 QA sets × 9 open LLMs.
  - LCR: 6 BEIR sets + TREC DL19/20 × 2 retrievers.
  - TopiCLEAR: 4.
  - SharP: PHEME, LIAR and Twitter15/16.
  - CrisisSpot: CrisisMMD plus the new TSEqD (10,352 samples, with inter-annotator kappa).
  - CE: 25 datasets.
  - Healthcare: MIMIC-III.
- **Baselines.** 3–11 in the papers I read:
  - KA2L: Entropy, Coreset and BADGE, adapted to LLMs, plus data-setting baselines.
  - TopiCLEAR: 5. SharP: 5 (HAN, dEFEND, HMCAN, DDT, DeepSeek).
  - CrisisSpot: about 11. LCR: several LLM and fine-tuned rerankers.
  - Baselines are each described in a short paragraph with citation and year (SharP lists "HAN (2016) : …").
- **Statistical tests are uncommon.** None of the 10 papers runs Friedman, Nemenyi or Wilcoxon tests. Variability is reported as mean ± SD over runs: TopiCLEAR uses "five runs", CE uses 30 repetitions and Stylometry uses 10-fold CV. Across the OpenAlex full-text subset of 526 ESWA articles since 2024, the share mentioning each term is:

  | Term | Share |
  |---|---|
  | "Friedman test" | 1.5% |
  | "Nemenyi" | 1.1% |
  | "Wilcoxon" | 6.5% |
  | "t-test" | 8.4% |
  | "ablation study" | 31.7% |
  | "sensitivity analysis" | 16.7% |
  | "computational complexity" | 24.0% |
  | "github.com" | 40.7% |
  | "limitations" | 76.8% |
  | "main contributions" | 33.3% |

  For a method that claims a guarantee, reporting the empirical FDR and violation frequency over repeated random calibration/test splits does the same job as a significance test.
- **Ablation.** Present in 5 of 10 papers (TopiCLEAR 5.2, SharP 4.3, Healthcare Table 6, CrisisSpot Table 8, LCR).
- **Sensitivity and hyperparameter analysis.** Present in 4 of 10 (SharP 4.4, LCR 4.4–4.5, KA2L 6.2, TopiCLEAR).
- **Runtime, complexity or cost.** A dedicated subsection or table appears in 3 of 10 papers: KA2L 6.5 "Computational Cost-Efficiency Analysis", the TopiCLEAR runtime table (Table 3) and the CrisisSpot 6.3 "Computational Efficiency and Scalability" subsection. Brief runtime or complexity remarks appear in most of the others (CE, Stylometry, LCR, the healthcare paper, Risk-aware EDL). **Cost framing is common in annotation papers.** KA2L headlines "reduces 50% annotation and computation costs".
- **Human or expert evaluation** appears when outputs are user-facing: clinicians rated 104 summaries with a rubric table in the healthcare paper, and CrisisSpot reports inter-annotator kappa.
- **Reproducibility and code.** 5 of 10 link their own GitHub repository (KA2L, CE, Stylometry, SharP, CrisisSpot), and KA2L puts the URL in the abstract.
  - The guide (2023 snapshot) describes the **Reproducibility Badge Initiative with Code Ocean** and asks for a data statement.
  - manusights.com (commercial, low reliability) warns that "code available on request" is a desk-reject risk.

## 5. Figures and tables

- **Overview or pipeline figure.** Present in 6 of 10 papers: KA2L "KA2L Workflow", the MONITOR scheme, the CrisisSpot "System Architecture", the LCR illustration, the healthcare paper's comparison of an "LLM-only" pipeline against "LLM + Fact-Checker", and SharP's "Model Architecture".
  - It is usually placed at the start of the method section, as Figure 1.
  - It sits in the **Introduction in 2 of 10** papers (LCR and the healthcare paper). manusights.com advises that "Figure 1" should show application context rather than only an architecture [UNVERIFIED advice].
- **Captions** are descriptive and often several sentences long, and state how to read the table or figure. Examples:
  - "Results are reported as mean ± standard deviation over five runs. The highest mean value is shown in bold" (TopiCLEAR Tables 2–7).
  - "Bold values indicate the best performance" (KA2L Tables 3–9).
  - Figure captions that explain sub-panels (a)/(b) (TopiCLEAR, Stylometry).
- **Table rules from the guide.** Submit tables "as editable text and not as images", place notes below the table, "Be sparing in the use of tables and ensure that the data presented in them do not duplicate results described elsewhere", and "Please avoid using vertical rules and shading in table cells". Booktabs-style tables meet this.
- **Common table types:** dataset statistics (in nearly all papers), a notation table, a hyperparameter or training-configuration table (KA2L Table 2, healthcare Table 3), a main comparison table per dataset group, an ablation table and a runtime table.
- **Colour use:** [UNVERIFIED]. It could not be measured from HTML. Elsevier publishes figures in colour online at no charge (general Elsevier policy, not re-verified for 2026).

## 6. References

- **Style.** The guide (2023 and 2024 snapshots) says: "Citations in the text should follow the referencing style used by the American Psychological Association … Seventh Edition", with the list "arranged first alphabetically and then further sorted chronologically". **ESWA is author–year (APA 7).**
  - A CSDN author reports choosing the elsarticle **harv** option (gitcode.csdn.net/6aa0d9ad1a35784c84206bc9.html). In LaTeX that means `elsarticle` with `\biboptions{authoryear}` or `elsarticle-harv.bst`.
  - 7 of 10 arXiv versions already use author–year citations.
- **Number of references** (Crossref deposits of published versions):

  | Sample | n | Median | IQR | Range |
  |---|---|---|---|---|
  | Relevant | 51 | 50 | 39–63 | 24–120 |
  | LLM subgroup | 23 | 57 | 42–69 | 28–120 |
  | Random ESWA 2024–26 | 200 | 52 | 43–62 | 3–382 (outliers are surveys) |
  | Full-text 10 | 10 | 58.5 | — | 39–87 |

  **Target: about 50–65.**
- **Recency.** The share of references with a year inside the 5-year window (publication year minus 4 through publication year) has a median of 0.57 for the relevant set, **0.64 for LLM papers**, 0.43 for UQ papers and 0.55 for the random set.
- **ESWA self-citation** (lower bound, from DOIs and journal names in the deposited references):

  | Sample | Median ESWA references per paper | Mean | Median share |
  |---|---|---|---|
  | Random | 2 | 2.35 | 3.1% |
  | Relevant | 1 | 1.9 | — |
  | HTC subgroup | 4 | — | — |

  Citing about 3–6 prior ESWA papers is typical and helps signal scope fit.
- **arXiv references.** LLM papers cite arXiv preprints often (median 4, mean 6.4 per paper). Random papers have a median of 0.

## 7. Editorial guidance and scope signals

1. **Aims and scope** (guide 2023/2024): "a refereed international journal whose focus is on exchanging information relating to expert and intelligent systems applied in industry, government, and universities worldwide. The thrust … is to publish papers dealing with the design, development, testing, implementation, and/or management of expert and intelligent systems, and also to provide practical guidelines…".
   - The listed application areas include **information management, information retrieval, risk assessment, crisis management, intelligent database management systems**, medicine and business.
   - It also lists "knowledge management, neural networks, knowledge discovery, **data and text mining**".
   - So LLM annotation for text corpora fits through "intelligent systems for information management / text mining" as long as it is framed as a system with practical value.
2. **2024 additions** (sciencedirect snapshot 2024-02-10):
   - "The journal no longer considers papers that contain applications to military/defense systems."
   - Metaphor-inspired optimisation algorithms are "discouraged".
   - "The Editorial decision for a paper is final … the journal cannot therefore consider manuscripts that have previously been rejected" unless the paper has been "substantially re-written (over 70% changed content)" and the cover letter justifies the resubmission. **Never send the same paper to ESWA twice.**
   - All authors must give an institutional e-mail address; any exception must be explained in the cover letter.
3. **Review model.** The 2023 and 2024 guides say "single anonymized review", with the paper "initially assessed by the editor for suitability" and then "a minimum of two independent expert reviewers". manusights.com (2026) says **double-anonymized**. The current policy is **[UNVERIFIED]**: check the live guide before submitting and, if it says double-anonymized, anonymise the manuscript.
4. **Editor-in-Chief.** Binshan Lin (Louisiana State University Shreveport; lsus.edu/binshan-lin-phd) also edits *Machine Learning with Applications*.
   - **I found no recent editorial by him stating "what ESWA looks for".** OpenAlex lists no ESWA editorial after 2013 (it lists 66 editorial-type works, mostly 1990s "Software survey section" items).
   - Any claim about his preferences is [UNVERIFIED].
5. **Secondary advice** (manusights.com, 2026; commercial, low reliability, use only as heuristics):
   - ESWA wants "substantive real-world application" rather than method novelty alone.
   - Desk-reject patterns include a method-first framing with a thin application, stale baselines ("add at least two baselines from sister venues published in the last 18 months"), benchmark-only validation with no decision setting, "no quantified error cost", and "code available on request".
   - The site also quotes an acceptance rate of about 11% and about 5 days to first (desk) decision from the "Elsevier catalog" [UNVERIFIED].
6. **Chinese community posts** (CSDN):
   - Required uploads: Author Agreement, cover letter (not a copy of the abstract), ORCID, Highlights (3–5), CRediT statement and a Declaration-tool file.
   - A LaTeX template with the harv option is recommended.
   - One timeline ran 2023-11-05 submitted → 2024-06-28 accepted after **three** revision rounds.
   - CSDN also cites an average review cycle of 13.8 months [UNVERIFIED, inconsistent with other reports].
7. **SciRev anecdote.** An ESWA editor redirected a paper to Applied Soft Computing, which then desk-rejected it as out of scope (scirev.org). Scope framing matters.
