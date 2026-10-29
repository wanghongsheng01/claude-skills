# How DMKD reviews manuscripts: evidence notes for a `review-dmkd` skill

Compiled 2026-10-29 from public sources only. Nothing was signed into. All URLs were accessed on **2026-10-29** unless a row says otherwise.

**Tags**
- **[VERIFIED official]**: text read on a DMKD/Springer/ECML PKDD page or a DMKD article page.
- **[PUBLIC FIRST-HAND]**: an editor's, action editor's or reviewer's own slides, paper or self-report, read directly.
- **[INFERRED]**: my reasoning from the evidence, not stated by any source.

Short quoted phrases are in quotation marks. Everything else is paraphrase.

Companion file: `research/submit-dmkd-notes.md` covers portal, template and declarations. This file covers **how a paper is judged**.

---

## Part A. Evidence

### A1. Official DMKD process and criteria

Source G: DMKD submission guidelines, https://link.springer.com/journal/10618/submission-guidelines [VERIFIED official].

**Process**
- **Two stages.** A first evaluation by the editor-in-chief (EiC), "typically done within 2 weeks or so". Regular review then "will usually take 1-3 months, sometimes more".
- **Revisions are the norm.** It is "very rare that a paper is accepted after the first submission". Accepted papers "often undergo two or three iterations".
- **Who assigns reviewers.** "We have a hierarchical system, where action editors invite reviewers". The chain is EiC → action editor (AE, printed as "Responsible editor") → reviewers.
- **Number of reviewers.** Not stated for regular papers.
  - Springer's generic tutorial says "two or more experts" (source SNT) [VERIFIED official, generic].
  - The ECML PKDD journal track aims for three (A2).
  - For a regular paper, plan for 2–3 reviewers [INFERRED].
- **Review model.** "Research content published in this journal is peer reviewed (single-anonymous)" (source E, https://link.springer.com/journal/10618/ethics-and-disclosures) [VERIFIED official].
  - The required title page carries the author names and affiliations [VERIFIED official, G].
  - Reviewers therefore know who the authors are.
- **Speed.** The journal homepage reports a median of "3 days" from submission to first decision (source H, https://link.springer.com/journal/10618) [VERIFIED official].
  - This median almost certainly includes the many desk decisions [INFERRED].
- **Decision categories.** DMKD does not publish them.
  - Springer's generic tutorial names three outcomes: reject, accept, or revise and resubmit, with possible re-review by the same reviewers (SNT) [VERIFIED official, generic].
  - Snapp/Editorial Manager forms normally offer Accept / Minor revision / Major revision / Reject [INFERRED; not visible without login].
  - A "reject and resubmit" option is unconfirmed [INFERRED].

**Regular-paper criteria** [VERIFIED official, G]. These are the closest thing DMKD publishes to a reviewer form.
1. What is the main contribution to data mining and knowledge discovery? It "should already be clear after reading the abstract".
2. What is the motivation? It is "typically not enough that a paper presents a new method". There must be "a clearly defined research gap" that alternative methods cannot currently address.
3. How is success demonstrated? Usually by "experiments that answer clearly formulated research questions", or by formal proofs.

**Survey-paper type** [VERIFIED official, G]. This explicitly includes papers that "report on extensive independent experimental comparisons" of competing approaches. Such papers "typically do not have to contain a new research contribution". The criteria are:
- Is the material "comprehensive and balanced"? Is the line between accepted views and personal perspectives clear?
- Does it give novel insight that goes "beyond the knowledge contained in the discussed papers"? "A mere concatenation of summaries" is not of interest.

**Application-paper type** [VERIFIED official, G].
- Comparing well-known algorithms on a new dataset and declaring a winner is "not sufficiently interesting".
- The criteria are:
  - the quality of the solution, including that simpler methods would not do as well
  - whether it extends the state of the art
  - its demonstrated impact in the domain

**Conference extensions** [VERIFIED official, G].
- Accepted, but the paper must give "a mature and in a way final view" and "enough new material to provide a significant contribution beyond the conference paper".
- The prior publication must be acknowledged and the extension explained at submission.

**Scope** [VERIFIED official]. Source S, https://link.springer.com/journal/10618/aims-and-scope.
- KDD includes "the multi-step knowledge discovery process ... (including data cleaning and noise modelling)".
- Listed topics include "Data pre-processing for data mining, including data cleaning".
- Also listed: "data mining systems and tools" and "details of successes and failures of KDD".

**Hard requirements that cause return or rejection** [VERIFIED official, G]:
- An incomplete set of editable sources means "not being considered for review".
- The abstract must be 150–250 words.
- 4–6 keywords.
- A "Statements and Declarations" section. Submissions without it "will be returned as incomplete".
- A mandatory Data Availability Statement for original research.
- LLM use must be documented. Pure "AI assisted copy editing" is exempt.

### A2. ECML PKDD journal track (DMKD + Machine Learning journal)

This is used as a **proxy** for DMKD reviewing. Sources: JT26, https://ecmlpkdd.org/2026/submissions-journal-track/ (read in the browser), and JT25, https://ecmlpkdd.org/2025/submissions-journal-track/ [VERIFIED official, for the track only].

**Review mechanics**
- "we aim to obtain three reviews from experienced reviewers", including Guest Editorial Board members.
- The initial decision comes about 10 weeks after each cutoff.
- Papers not rejected "normally require (sometimes substantial) revisions", and the revised paper is re-reviewed.
- Review is single-blind.

**Eligibility**
- Papers must meet journal quality and "lend themselves to conference talks".
- No journal versions of conference papers and no surveys.
- A paper rejected by the Machine Learning journal may not go to DMKD, and vice versa.

**Desk-reject rules**
- Incomplete or double submission.
- Wrong format.
- More than 23 pages. Pages 21–22 are "scrutinized".
- No qualified reviewer nominated among the authors.

**Reproducibility**
- Reviewers "will be instructed to pay close attention to reproducibility of results where appropriate".
- Code and data should go in as supplementary material whenever feasible.
- Links to web supplements are not allowed (JT26).

**The DMKD cover letter (≤2 pages) is the de facto reviewer frame.** It must answer:
- "What is the main claim of the paper? Why is this an important contribution...?"
- "What is the evidence provided to support claims? Be precise."
- 3–5 most closely related contributions from the past 7 years, by researchers outside the authors' group, with how the paper relates to each.
- Keywords, conflicts of interest, and suggested reviewers.

**Proxy criteria from the ECML PKDD 2026 research track** (not the journal track; source RT26, https://ecmlpkdd.org/2026/submissions-research-track/) [VERIFIED official, for the conference track only]: "novelty, technical quality, potential impact, and clarity", judged by three reviewers.

[INFERRED] Treat claim, evidence and the closest recent related work as the AE's mental checklist for any DMKD submission, not only for the journal track. The same people (DMKD AEs, Fürnkranz as EiC 2015–2023) designed both.

### A3. Generic Springer reviewer guidance

Source SNT: https://www.springernature.com/gp/authors/campaigns/how-to-peer-review [VERIFIED official, generic].
- Editors find comments on "importance and novelty" most useful, as well as whether the paper will interest the audience.
- The reasoning matters more than "a simple recommendation".
- Reviewers flag errors in methods or analysis, and unclear sections.
- Peer review should improve "clarity, robustness and reproducibility".

### A4. Writings by DMKD editors and action editors on reviewing standards

DMKD editors-in-chief:
- Fayyad, founding EiC.
- Geoff Webb, 2005–2014.
- Johannes Fürnkranz, 2015–2023 (the Wikipedia list agrees with the DMKD responsible-editor records below).
- Eyke Hüllermeier, current. The board page lists him as EiC [VERIFIED official, https://link.springer.com/journal/10618/editorial-board].

The current AEs include several authors of benchmark-critique work: **Eamonn Keogh, John Paparrizos, Arthur Zimek, Panagiotis Papapetrou, Albert Bifet, Heiko Paulheim and Toon Calders**. Anthony Bagnall sits on the editorial board [VERIFIED official].

**Eamonn Keogh, "How to do good research, get it published in SIGKDD and get it cited!" (SIGKDD 2009 tutorial, 173 slides).** Source K09, https://www.cs.ucr.edu/~eamonn/Keogh_SIGKDD09_tutorial.pdf [PUBLIC FIRST-HAND]. Keogh is a current DMKD AE. Points relevant to journal reviewing:
- **Problem statement.** If a reviewer cannot write a one-sentence research statement after the abstract, the paper "is usually doomed" (slide 23).
- **The introduction is an anchor.** By its end the reviewer must know what the problem is and why it matters (slides 78–79).
- **Top ten avoidable reasons for rejection** (slides 157–168):
  - out of scope. Did you cite and read KDD papers, frame the problem as KDD, use KDD datasets and metrics?
  - experiments not reproducible. The test: could you recreate every experiment from your webpage alone?
  - too similar to your last paper
  - a weakness you did not acknowledge
  - you unfairly diminish others' work
  - there is an easier way, or you did not compare to algorithm X. Include simple strawmen.
  - missing related work, or the idea is already known
  - too many parameters, magic numbers or arbitrary choices
  - not an important problem ("Why do we care?")
  - careless writing
- **Choices and parameters.** Unjustified choices are bad: explain every choice, and say so when a choice was arbitrary (slide 94). Parameters must be settable or shown to be insensitive (slide 166).
- **Wording.** Separate "significantly" from "statistically significantly ... at a confidence level of" (slide 95). Do not say "proved" for experiments.
- **Data scale.** Small datasets are increasingly hard to excuse (slide 38).
- **Reproducibility.** Explicit reproducibility efforts "instill confidence in the reviewers" (slides 80–88).

**Keogh, "Irrational Exuberance: Why we should not believe 95% of papers on Time Series Anomaly Detection" (MiLeTS@KDD 2021, 66 slides).** Source K21, https://kdd-milets.github.io/milets2021/slides/Irrational%20Exuberance_Eammon_Keogh.pdf [PUBLIC FIRST-HAND]. It lists the flaws a benchmark-literate reviewer looks for:
- flawed benchmark datasets: trivial, mislabeled, unrealistic anomaly density, run-to-failure bias
- inappropriate measures of success
- non-reproducible experiments, including public data without public labels
- ignoring older competitive baselines
- "unjustified complexity"
- spurious precision: four significant digits when the ground truth is uncertain, and counting non-independent events as many successes (slides 33–37)

The constructive half proposes a better archive and a binary scoring protocol (slides 51–53). A critique paired with a remedy is the model to follow [INFERRED].

**Wu & Keogh, "Current Time Series Anomaly Detection Benchmarks are Flawed and are Creating the Illusion of Progress."** arXiv 2009.13807 (v1 2020, v5 2022), https://arxiv.org/abs/2009.13807 [PUBLIC FIRST-HAND, abstract and search snippets only].
- It names four flaws (triviality, unrealistic density, mislabeled ground truth, run-to-failure bias).
- It operationalises "trivial" as solvable by a single line of standard library code.
- It releases the UCR anomaly archive.
- A public Reddit thread criticised it as reading "like an editorial" with vague definitions [PUBLIC FIRST-HAND, but third-party and informal]. Reviewers of critique papers may raise the same objection.

**Keogh & Kasetty, "On the need for time series data mining benchmarks: a survey and empirical demonstration," DMKD 7(4), 2003.** https://doi.org/10.1023/A:1024988512476 [VERIFIED official article page; content from the abstract].
- The extended journal version of KDD 2002, and the earliest DMKD precedent for a benchmark-critique paper.
- It surveyed 57 papers and re-implemented more than two dozen contributions on 50 datasets.
- It found the number of datasets used "astonishingly low", and improvements dwarfed by variance across data or implementation details.

**Statistical comparison expectations**:
- **Demšar (2006, JMLR 7)**, https://www.jmlr.org/papers/v7/demsar06a.html [PUBLIC FIRST-HAND, abstract]. Use the Wilcoxon signed-rank test for two classifiers, and Friedman with post-hoc tests for several. Critical difference (CD) diagrams are proposed.
- **Benavoli, Corani & Mangili (2016, JMLR 17)**, https://jmlr.org/papers/v17/benavoli16a.html [PUBLIC FIRST-HAND, abstract]. Mean-rank post-hoc tests are inconsistent. Use pairwise tests whose outcome "only depends on the two algorithms being compared", such as the sign test or Wilcoxon with a correction.
- **Benavoli, Corani, Demšar & Zaffalon (2017, JMLR 18)**, https://jmlr.org/papers/v18/16-305.html [PUBLIC FIRST-HAND, abstract]. Abandon NHST in favour of Bayesian tests. The ROPE / practical-equivalence idea is from the paper body; I did not verify it here.
- [INFERRED] DMKD reviewers expect one of these for any "method A beats method B over many datasets" claim. Bagnall et al. 2017 (A6) followed Demšar.

**Fürnkranz.** I found no public editorial by him on reviewing standards. However:
- He was the responsible editor for Campos 2016, Bagnall 2017, Ruiz 2021, Guidotti 2023 and van den Burg 2019 (A6) [VERIFIED official].
- The paper-type criteria in G were very likely written under his editorship [INFERRED].

**Webb.** I found no public editorial on reviewing standards. His 2007 tenth-anniversary editorial introduced position papers "without the usual emphasis on theoretical and empirical evidence" (search snippet only; [PUBLIC FIRST-HAND, unverified full text]). The ODBMS interview contains nothing on reviewing [checked].

**Hüllermeier.** I found no editorial on reviewing standards.

### A5. Public DMKD or ECML PKDD journal-track reviews

- **None found.**
  - DMKD is single-anonymous, closed review. Springer does not publish pre-publication history under that model (companion notes).
  - ECML PKDD journal-track reviews run inside Snapp, not OpenReview (JT26).
  - Searches for public rebuttal or response letters on GitHub or arXiv turned up only generic templates.
- **SciRev self-reports.** Source SR, https://scirev.org/reviews/data-mining-and-knowledge-discovery/ [PUBLIC FIRST-HAND, n=2].
  - One immediate rejection after 14 days, "out of scope".
  - One acceptance with 3 reports and 13.7 weeks of total handling.
  - Too sparse to generalise.
- **Nearest public analogue.** The OpenReview forum of Liu & Paparrizos, "The Elephant in the Room" (TSB-AD, NeurIPS 2024 Datasets & Benchmarks), https://openreview.net/forum?id=R6kJtWsTGy.
  - Paparrizos is a DMKD AE.
  - **Not read.** OpenReview showed a browser-verification check, which I did not attempt to bypass.
  - The user can open it manually to harvest real benchmark-paper criticisms.

### A6. Precedents: DMKD papers with no new algorithm (audit, evaluation or benchmark)

Responsible editor and dates come from each Springer article page [VERIFIED official].

| Paper | Type | Responsible editor | Received → Accepted |
|---|---|---|---|
| Keogh & Kasetty 2003, time-series benchmarks (10.1023/A:1024988512476) | critique + re-implementation | n/a (old record) | journal version of KDD'02 |
| Campos et al. 2016, outlier-detection evaluation (10.1007/s10618-015-0444-8) | measures + datasets + empirical study | J. Fürnkranz | 17 Jul 2015 → 18 Nov 2015 |
| Bagnall et al. 2017, TSC bake off (10.1007/s10618-016-0483-9) | re-implementation + comparison | J. Fürnkranz | 7 Jun 2016 → 1 Nov 2016 |
| Ismail Fawaz et al. 2019, DL for TSC review (10.1007/s10618-019-00619-1) | review + empirical study | E. Keogh | 12 Sep 2018 → 25 Feb 2019 |
| van den Burg et al. 2019, messy CSV dialects (10.1007/s10618-019-00646-y) | data-wrangling method (data-prep precedent) | J. Fürnkranz | 26 Nov 2018 → 19 Jul 2019 |
| Ruiz et al. 2021, multivariate TSC bake off (10.1007/s10618-020-00727-3) | comparison | J. Fürnkranz | 24 Aug 2020 → 25 Nov 2020 |
| Hewamalage, Ackermann & Bergmeir 2023, forecast-evaluation pitfalls (10.1007/s10618-022-00894-5) | evaluation-practice critique + tutorial | E. Keogh | 4 Apr 2022 → 7 Nov 2022 |
| Guidotti et al. 2023, benchmarking explainers (10.1007/s10618-023-00933-9) | survey + benchmark | J. Fürnkranz | 24 Nov 2021 → 10 Mar 2023 |
| Sørbø & Ruocco 2024, metric maze for TSAD (10.1007/s10618-023-00988-8) | metric taxonomy + analysis | E. Keogh | 20 Feb 2023 → 24 Oct 2023 |
| Middlehurst, Schäfer & Bagnall 2024, bake off redux (10.1007/s10618-024-01022-1) | comparison | E. Keogh | 16 Jan 2024 → 29 Mar 2024 |
| Fischer et al. 2024, STREP reporting framework (10.1007/s10618-024-01020-3) | reporting/reproducibility framework | P. Papapetrou | 6 Dec 2023 → 25 Mar 2024 |
| Clustering-based outlier detection comparative evaluation 2025 (10.1007/s10618-024-01086-z) | empirical evaluation | E. Hüllermeier | 15 Dec 2024 → 28 Dec 2024 (the "Received" date probably reflects a late revision) |
| "How robust is your fair model?" 2025 (10.1007/s10618-025-01112-8) | robustness criterion + experiments | T. Calders | 17 May 2023 → 6 May 2025 |

**What these precedents share.** Each feature below is visible in the abstracts or full text read: Bagnall via ar5iv 1602.01711, the others via their abstracts.
1. **A named, community-level problem.** Examples:
   - unclear progress in outlier detection because benchmarks and measures are not understood (Campos)
   - incomparable evaluations from single splits, mixed languages and test-set tuning (Bagnall, from ar5iv)
   - "flawed evaluation practices which results in spurious conclusions" (Hewamalage abstract)
2. **Breadth.**
   - Campos: many detectors on "a wide variety of datasets prepared for this purpose".
   - Bagnall: 18 algorithms on 85 datasets with 100 resamples.
   - Keogh & Kasetty: 50 datasets.
   - Clustering-OD 2025: 14 methods on 46 datasets.
3. **Consequences shown, not just defects listed.**
   - Bagnall: only nine algorithms significantly beat the benchmarks.
   - Campos: datasets characterised by suitability, plus improved measures.
   - Keogh & Kasetty: claimed gains dwarfed by variance.
4. **A constructive artefact.** Examples:
   - the repository of datasets and results (Campos; https://www.dbs.ifi.lmu.de/research/outlier-evaluation/ [VERIFIED])
   - a common code framework and results website (Bagnall)
   - a new archive (Keogh)
   - best-practice guidelines (Hewamalage)
   - a taxonomy (Sørbø)
5. **Sound statistics where rankings are claimed.** Bagnall used Friedman + Nemenyi CD diagrams, following Demšar, and reported reproduction failures.
6. **Fair treatment of prior work.**
   - Bagnall says it is the designers' responsibility to "demonstrate its worth" and calls the authors' own COTE "by no means the final solution" (ar5iv).

[INFERRED] The editors who accepted these papers are exactly the AEs a benchmark-audit paper is likely to be assigned to: Keogh, Hüllermeier, Papapetrou, Zimek, Paparrizos. Their stated values in K09/K21 should be weighted heavily.

### A7. Adjacent data-cleaning evaluation literature

This literature is the "database" framing risk. Most data-cleaning evaluation studies appear at DB venues, for example:
- Abedjan et al., PVLDB 2016
- Ni et al., "Automatic Data Repair: Are We Ready to Deploy?", PVLDB 17(10) 2024, https://vldb.org/pvldb/vol17/p2617-miao.pdf (12 repair algorithms × 12 datasets × 4 downstream tasks) [VERIFIED via search result and PVLDB listing]
- REIN, EDBT 2023

The DMKD searches for "data cleaning", "data repair" and "error detection" returned almost no DMKD papers on relational data repair. van den Burg 2019 (CSV wrangling) is the nearest DMKD precedent [VERIFIED official, Springer search].

[INFERRED] The AE will ask why this is a DMKD paper rather than a PVLDB, Information Systems or SIGMOD one. Scope text (A1) supports data cleaning as KDD process. The paper must still be framed through KDD consequences: evaluation validity, leakage of wrong labels into reported progress, and KDD-process reproducibility.

---

## Part B. Derived instruments (all [INFERRED] from Part A; source keys in brackets)

### B1. DMKD-style review form

Each criterion is scored 1–5 (1 = fatal, 3 = acceptable with revision, 5 = exemplary). Weights reflect how often the evidence stresses each criterion. The paper type, chosen first, changes which criteria dominate.

**0. Paper type and desk gate** (not scored)
- Is it a Regular, Survey (including "extensive independent experimental comparison") or Application paper? [G]
- Does it pass every desk-screen item in B3?

**C1. Contribution and claim** (weight 20%) [G, JT26, K09]
- Is the main contribution clear after the abstract alone?
- Can the reviewer write "X is good for Y in the context of Z" in one sentence?
- Is the claim specific, falsifiable and matched by the evidence?

**C2. Motivation, research gap and significance** (15%) [G, SNT, RT26, K09]
- Is there "a clearly defined research gap" that existing approaches cannot address?
- Why should KDD researchers care?
- What changes in practice or in the published literature if the paper is right?

**C3. Novelty and relation to the literature** (10%) [G-survey, JT26, K09]
- Does it go beyond what the cited papers already establish?
- Are the 3–5 closest recent works by other groups identified and contrasted?
- Is the KDD literature cited, not only DB literature?
- Is prior work treated fairly?

**C4. Technical soundness** (15%) [SNT, K09, K21]
- Are definitions precise?
- Are design choices and parameters justified?
- Is the reference or ground truth itself validated?
- Are there hidden assumptions?
- Is there a simpler way?

**C5. Experimental and evaluation methodology** (20%) [G, K03, Bagnall, Campos, Demšar/Benavoli, K21, Sørbø]
- Do the experiments answer clearly formulated RQs?
- Breadth: are there enough datasets, generators, systems and versions?
- Are the baselines appropriate, including simple ones?
- Are the metrics justified?
- Are variance and uncertainty reported, and statistical tests used where comparisons are claimed?
- Does the precision of reported numbers match the uncertainty?

**C6. Reproducibility and artefacts** (10%) [JT26, G-data policy, K09, Bagnall]
- Is the code, data, configuration, version pinning and scripts available as supplement or archived DOI?
- Is there a data availability statement?
- Could a third party regenerate every table?

**C7. Clarity and presentation** (10%) [RT26, K09, SNT]
- Structure, terminology load, figures, abstract readability.
- Is the length justified?
- Is the paper written for a DM reader?

**Overall recommendation:** Accept / Minor revision / Major revision / Reject (state whether resubmission would be welcome).
- Each recommendation needs 3–5 numbered major issues and minor issues.
- Add confidential comments to the AE, which must not contradict the report [SNT].

**AE synthesis rule** [G, INFERRED]
- Reject if any reviewer finds a fatal C1, C2 or C5 flaw that no revision can fix.
- Otherwise the default is major revision, since first-round acceptance is "very rare".
- Expect 2–3 rounds.

### B2. The 25 most likely reviewer objections, ranked by evidence

**Evidence score (E):**
- **3**: stated in official DMKD or ECML-JT text and in first-hand AE writings.
- **2**: one of those sources, or a strong precedent pattern.
- **1**: inference only.

**"Here"** gives how likely each objection is for the current manuscript ("Auditing Data-Repair Benchmarks with Explicit Comparison Contracts"), based on its abstract, section list and references (`overleaf-is/main.tex`, read 2026-10-29).

| # | Objection a DMKD reviewer or AE would write | E | Sources | Here |
|---|---|---|---|---|
| 1 | "The main contribution is not clear from the abstract; I cannot state the claim in one sentence." | 3 | G crit.1; JT26 "main claim"; K09 sl.23 | High: the 246-word abstract is number-dense with many defined terms |
| 2 | "What research gap does this fill that existing evaluation studies cannot? Why does it matter to KDD?" | 3 | G crit.2; SNT; K09 sl.167 | High |
| 3 | "The paper explicitly offers no new algorithm and no re-ranking. So what changes? Show that the defects alter published conclusions." | 3 | G crit.2–3; A6 pattern 3; K03; Wu&Keogh | High: the abstract says "not ... a re-ranking" |
| 4 | "Out of scope / a database or software-engineering paper not framed for data mining." | 3 | K09 sl.159; SR desk-reject case; S (scope) | High: 0 of 23 references are KDD/DMKD/ECML/JMLR |
| 5 | "Experiments are not fully reproducible, or the artefacts are hard to use (versions, scripts, data)." | 3 | JT26; G data policy; K09 sl.160; Bagnall | Medium: a Zenodo deposit exists; must check it actually regenerates every table |
| 6 | "Breadth is too narrow: one generator (BART) and one consumer release (Raha/Baran). Findings may not generalise." | 3 | K03 "astonishingly low"; Bagnall; Campos; K09 sl.38 | High |
| 7 | "Related work is incomplete: benchmark-critique and evaluation-methodology literature in DM/ML is missing (Keogh & Kasetty, Campos, Bagnall, Wu & Keogh, Hewamalage, Demšar)." | 3 | K09 sl.165; JT26 3–5 recent works | High |
| 8 | "The weaknesses are not acknowledged up front." Or the reverse: "so many caveats that the claim is empty" ("deployment utility remains unmeasured"). | 3 | K09 sl.162; JT26 "Be precise" | Medium |
| 9 | "There is an easier way. A simple key-based diff, or sorting before comparison, would catch this. Why is a whole procedure needed?" | 3 | K09 sl.164; K21 Ockham | High |
| 10 | "Unjustified complexity or terminology (comparison contract, supplied authority, ledger); hard to follow." | 2 | K21 "unjustified complexity"; K09 "don't make the reviewer think" | High |
| 11 | "Unjustified design choices and magic numbers (why 94 runs, a 50-row table, 696 mutations, 158 inputs?)." | 2 | K09 sl.94, 166 | Medium |
| 12 | "Survey/comparison paper judged on balance: is it comprehensive and balanced, does it give novel insight beyond the cited papers?" (applies if typed as Survey) | 3 | G survey criteria | Depends on the article type chosen |
| 13 | "Who audits the auditor? How is your own reference, verifier or ground truth validated?" | 2 | K21 mislabeled ground truth; Campos dataset suitability | High |
| 14 | "Spurious precision or overclaiming: counts like 942/948 imply fine distinctions. Are events independent?" | 2 | K21 sl.33–37; K09 sl.95 wording | Medium |
| 15 | "No statistical treatment or variance where comparisons are made (e.g., patching vs rebuilding speed)." | 2 | Demšar; Benavoli; Bagnall | Medium (mostly deterministic; say why tests do not apply) |
| 16 | "Metrics are not justified; why these detection/correction precision-recall definitions?" | 2 | Sørbø & Ruocco; Campos; Hewamalage | Medium |
| 17 | "Tone toward the audited tools (BART, Raha/Baran) is unfair; were the original authors consulted?" | 2 | K09 sl.163 | Medium: audit papers are prone to this |
| 18 | "Synthetic or controlled mutations are not representative of real errors." | 2 | K21 sl.4; K09 sl.38 | Medium |
| 19 | "Two loosely coupled contributions (benchmark audit + dbt semantic-layer verifier); the paper lacks focus." | 1 | G crit.1 (single main contribution) | High |
| 20 | "Version-specific findings for pinned releases have short shelf-life. What is the general lesson?" | 1 | G "mature ... final view"; A6 pattern 4 | High |
| 21 | "No constructive artefact the community will adopt (a corrected benchmark, a tool, guidelines)." | 2 | A6 pattern 4 (Campos repo, Bagnall code, UCR archive, Hewamalage guidelines) | Medium: four recommendations exist; make them an artefact |
| 22 | "Prior or overlapping publication (earlier synthetic benchmark; previous journal submission). What is new?" | 2 | G extensions FAQ; K09 sl.161 | Medium (Appendix history; declare) |
| 23 | "Practical impact or deployment utility is not demonstrated." | 2 | G application criteria; RT26 "potential impact" | Medium (stated as unmeasured) |
| 24 | "Writing and presentation: dense, number-heavy prose; tables and figures carry the argument poorly." | 2 | K09 sl.168; RT26 clarity | Medium |
| 25 | "Efficiency claims ('patching is slower') lack runtime methodology (implementation effects, hardware, repetitions)." | 1 | Bagnall "efficiency also matters"; INFERRED | Low–medium |

### B3. Action-editor desk-screen checklist (EiC/AE first pass, about 2 weeks)

Hard gates (fail any one → return or desk reject) [VERIFIED official unless marked]:
- [ ] Complete editable source set (LaTeX + figures + PDF) [G]
- [ ] Abstract 150–250 words without undefined abbreviations; 4–6 keywords [G]
- [ ] "Statements and Declarations" present: competing interests, funding, contributions, and so on [G]
- [ ] Data Availability Statement for original research [G]
- [ ] LLM use documented, if beyond copy editing [G]
- [ ] Not under review elsewhere; any prior conference/journal version declared, with a statement of the extension [G]
- [ ] Article type chosen correctly: Regular, Survey or Application [G]
- [ ] Journal track only: ≤23 pages (aim ≤20); DMKD cover letter ≤2 pages; CMT + Snapp; qualified author-reviewer; no journal versions of conference papers or surveys [JT26]

Substantive screen [INFERRED from G, K09, A6]:
- [ ] **Scope**: framed as a KDD problem (data cleaning / evaluation validity in the KDD process); cites DMKD/KDD/ECML/JMLR literature; not merely a DB-systems or software-testing contribution
- [ ] **Contribution visible in the abstract**: one-sentence claim; contribution type stated
- [ ] **Gap**: why existing evaluation studies (Abedjan 2016, CleanML, Ni et al. 2024, REIN) do not already answer this
- [ ] **Consequence**: at least one demonstration that the defect changes a reported result, ranking or conclusion
- [ ] **Breadth**: more than one generator, benchmark or consumer, or a convincing argument why one suffices
- [ ] **Evidence quality**: RQs stated; methods replicable; reproducibility artefact archived (DOI)
- [ ] **Fairness and tone** toward audited systems
- [ ] **Presentation**: readable by a DM generalist; jargon defined once; length proportionate
- [ ] **Suitable reviewers exist** among the AEs/board (e.g., Keogh, Paparrizos, Zimek, Papapetrou, Paulheim) → the paper should cite and engage their evaluation-methodology work [INFERRED]

### B4. What made non-algorithm papers acceptable, as a recipe [INFERRED from A6]

1. Name a field-level problem and show it matters (the "illusion of progress" style), with at least one concrete case where a published or plausible conclusion flips.
2. Cover enough breadth for the conclusion to be general: several systems, datasets, generators and versions.
3. Deliver a reusable artefact: a validated benchmark variant, an open tool, guidelines or a checklist.
4. Use correct statistics wherever rankings or differences are claimed, and justify their absence for deterministic checks.
5. Treat the audited work fairly and include its authors' perspective.
6. Choose the article type deliberately. "Extensive independent experimental comparisons" are DMKD Survey papers [G]. An audit with a new procedure fits the Regular type better, but then the procedure itself must be the contribution.

---

## Part C. Sources

| Key | Source | URL | Accessed | Tag |
|---|---|---|---|---|
| G | DMKD submission guidelines (FAQ, paper types and criteria, data policy) | https://link.springer.com/journal/10618/submission-guidelines | 2026-10-29 | [VERIFIED official] |
| S | DMKD aims and scope | https://link.springer.com/journal/10618/aims-and-scope | 2026-10-29 | [VERIFIED official] |
| E | DMKD ethics & disclosures ("single-anonymous") | https://link.springer.com/journal/10618/ethics-and-disclosures | 2026-10-29 | [VERIFIED official] |
| B | DMKD editorial board | https://link.springer.com/journal/10618/editorial-board | 2026-10-29 | [VERIFIED official] |
| H | DMKD homepage (median 3 days to first decision) | https://link.springer.com/journal/10618 | 2026-10-29 | [VERIFIED official] |
| JT26 | ECML PKDD 2026 journal track | https://ecmlpkdd.org/2026/submissions-journal-track/ | 2026-10-29 | [VERIFIED official] (proxy) |
| JT25 | ECML PKDD 2025 journal track | https://ecmlpkdd.org/2025/submissions-journal-track/ | 2026-10-29 | [VERIFIED official] (proxy) |
| RT26 | ECML PKDD 2026 research track (criteria) | https://ecmlpkdd.org/2026/submissions-research-track/ | 2026-10-29 | [VERIFIED official] (proxy, conference) |
| SNT | Springer Nature "How to peer review" | https://www.springernature.com/gp/authors/campaigns/how-to-peer-review | 2026-10-29 | [VERIFIED official] (generic) |
| A6 | DMKD article pages (responsible editor, dates) for the 13 papers in A6 | https://link.springer.com/article/{DOI} | 2026-10-29 | [VERIFIED official] |
| K09 | Keogh, SIGKDD 2009 tutorial | https://www.cs.ucr.edu/~eamonn/Keogh_SIGKDD09_tutorial.pdf | 2026-10-29 | [PUBLIC FIRST-HAND] |
| K21 | Keogh, "Irrational Exuberance", MiLeTS 2021 | https://kdd-milets.github.io/milets2021/slides/Irrational%20Exuberance_Eammon_Keogh.pdf | 2026-10-29 | [PUBLIC FIRST-HAND] |
| WK | Wu & Keogh, TSAD benchmarks flawed (arXiv 2009.13807) | https://arxiv.org/abs/2009.13807 | 2026-10-29 | [PUBLIC FIRST-HAND] (abstract/snippets) |
| K03 | Keogh & Kasetty, DMKD 2003 | https://doi.org/10.1023/A:1024988512476 | 2026-10-29 | [VERIFIED official] (abstract) |
| BAG | Bagnall et al. 2017 full text (arXiv) | https://ar5iv.arxiv.org/html/1602.01711 | 2026-10-29 | [PUBLIC FIRST-HAND] |
| CAM | Campos et al. 2016 abstract + repository | https://doi.org/10.1007/s10618-015-0444-8 ; https://www.dbs.ifi.lmu.de/research/outlier-evaluation/ | 2026-10-29 | [VERIFIED official] / [PUBLIC FIRST-HAND] |
| HEW | Hewamalage et al. 2023 abstract | https://link.springer.com/article/10.1007/s10618-022-00894-5 | 2026-10-29 | [VERIFIED official] |
| DEM | Demšar 2006, JMLR | https://www.jmlr.org/papers/v7/demsar06a.html | 2026-10-29 | [PUBLIC FIRST-HAND] (abstract) |
| BEN16 | Benavoli, Corani, Mangili 2016, JMLR | https://jmlr.org/papers/v17/benavoli16a.html | 2026-10-29 | [PUBLIC FIRST-HAND] (abstract) |
| BEN17 | Benavoli et al. 2017, JMLR | https://jmlr.org/papers/v18/16-305.html | 2026-10-29 | [PUBLIC FIRST-HAND] (abstract) |
| NI24 | Ni et al., PVLDB 17(10) 2024 | https://vldb.org/pvldb/vol17/p2617-miao.pdf | 2026-10-29 | [VERIFIED official] (search listing) |
| SR | SciRev DMKD reviews (n=2) | https://scirev.org/reviews/data-mining-and-knowledge-discovery/ | 2026-10-29 | [PUBLIC FIRST-HAND] (self-reports) |
| WIKI | Wikipedia DMKD (EiC list) | https://en.wikipedia.org/wiki/Data_Mining_and_Knowledge_Discovery | 2026-10-29 (search snippet) | [INFERRED]-grade, corroborated by A6 editor records |
| OR | OpenReview TSB-AD forum (blocked by browser check; not read) | https://openreview.net/forum?id=R6kJtWsTGy | 2026-10-29 | not read |

**Searched with nothing usable found:** a Webb editorial on reviewing; a Hüllermeier editorial; the Fürnkranz reviewing editorial; public DMKD reviews or rebuttals on GitHub or arXiv; Keogh's 2012 "Acceptance Rate to 80%" slides.
