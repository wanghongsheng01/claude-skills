# Review-ESWA evidence notes (collected 2026-10-29; the live 2026 guide read directly confirms double-anonymized review, ≤250-word abstracts, 1–7 keywords, EiC Ling Wang and the 5/62/147/7-day timeline)

Expert Systems with Applications (ESWA), Elsevier, ISSN 0957-4174.
Compiled 2026-10-29 from public sources. **All URLs accessed 2026-10-29** unless stated otherwise.

## 0. How to read these notes

Reliability tags used below:

- **[OFFICIAL]**: Elsevier or ESWA page fetched directly.
- **[OFFICIAL-SNIPPET]**: wording from the official ESWA Guide for Authors or Insights page as indexed by the search engine. ScienceDirect returned HTTP 403 to WebFetch for every ESWA page tried (guide-for-authors, insights, aims-and-scope, editorial-board), so the live page itself was not read. Check these against the live page before relying on them.
- **[COMMUNITY]**: self-reported author data (SciRev, LetPub, CSDN or Zhihu posts). The samples are small and self-selected.
- **[VENDOR]**: commercial consultancy blogs (manusights.com, nativeee.com, CSDN "论文辅导"). They are often unsourced, internally inconsistent, or marketing copy. Treat them as opinion.
- **[UNVERIFIED]**: could not be confirmed from any source I could read.

Access limits: ScienceDirect, the oa.upm.es PDF, Zhihu, academia.edu and the web.archive.org copies all refused WebFetch, and dblp served a bot-check page. I did not try to get around any of these blocks. Quotes from those sources come only from search-engine snippets.

---

## 1. Editorial process

### 1.1 Scope (desk-review criterion #1)

- **Official Aims and Scope** [OFFICIAL], https://shop.elsevier.com/journals/expert-systems-with-applications/0957-4174
  - The journal calls itself "a refereed international journal whose focus is on exchanging information" on expert and intelligent systems "applied in industry, government, and universities".
  - It publishes "original papers dealing with the design, development, testing, implementation" and/or management of expert and intelligent systems, and also gives practical guidelines.
  - The page lists a long set of application areas (business and finance, engineering, medicine, science, the public sector and social domains, energy, ...).
  - Listed topics include multi-agent systems, knowledge management, neural networks, knowledge discovery, data and text mining, multimedia mining and genetic algorithms.
  - **Exclusion:** "The journal no longer considers papers that contain applications to military/defense systems."
  - **Metaphor algorithms:** papers that "repurpose existing concepts within the framework of metaphors" are discouraged. New nature-inspired proposals "must provide formal, mathematically grounded explanations" of how they differ from established methods. The page also states "The emphasis is on genuine innovation rather than the renaming of existing concepts" (wording via search snippet of the same page).
  - Authors are invited to turn open-source software into a paper in *Software Impacts*.
- **Implication for an LLM-annotation method paper.** The scope is defined by applied expert and intelligent systems. "Text mining" and "knowledge discovery" are explicitly in scope. ESWA has no stated exclusion for NLP or LLM work, unlike DKE's stated focus. The screening risk at ESWA is a paper that reads as a pure-methods or statistics paper with no applied-system framing; that is a [VENDOR] observation, see §4.

### 1.2 Evidence that ESWA publishes in our area (scope precedent)

OpenAlex API queries restricted to ISSN 0957-4174 [OFFICIAL metadata via OpenAlex]:

- LLM / annotation query: https://api.openalex.org/works?filter=primary_location.source.issn:0957-4174,title_and_abstract.search:large%20language%20model%20annotation,from_publication_date:2024-01-01 (30 hits). Hits include:
  - "Standardizing longitudinal chest X-ray report evaluation via large language model annotation" (2026), https://doi.org/10.1016/j.eswa.2026.134237
  - "KA2L: A knowledge-aware active learning framework for LLMs" (2026), https://doi.org/10.1016/j.eswa.2026.133951
  - "HalluTrigger ... hallucinations in large language models ..." (2026), https://doi.org/10.1016/j.eswa.2026.132644
  - "OpenBioNER-v2 ... zero-shot medical named entity recognition" (2026), https://doi.org/10.1016/j.eswa.2026.131725
- Conformal prediction query: 16 hits since 2023, for example:
  - "Improving conformalized quantile regression through cluster-based feature relevance" (2023), https://doi.org/10.1016/j.eswa.2023.122322
  - "Conformal prediction of option prices" (2024), https://doi.org/10.1016/j.eswa.2023.123087
  - "From prediction to decision support: A transfer-aware and uncertainty-calibrated evaluation framework ..." (2026), https://doi.org/10.1016/j.eswa.2026.134259
- Annotation, crowdsourcing and label-noise query (title search): 190 hits since 2024, for example:
  - "Crowdsourcing truth inference under behavioral uncertainty using Kelly-inspired risk-aware allocation" (2026), https://doi.org/10.1016/j.eswa.2026.134057
  - "Worker and instance similarity-based label completion for crowdsourcing" (2026), https://doi.org/10.1016/j.eswa.2026.133503
  - "Label-wise reliability-aware classifier for robust chest X-ray multi-label classification" (2026), https://doi.org/10.1016/j.eswa.2026.131438
  - "DART: ... pseudo-label Review ..." (2024), https://doi.org/10.1016/j.eswa.2024.125124
- Hierarchical text classification query: 20 hits, for example:
  - "HeteroHTC ..." (2025), https://doi.org/10.1016/j.eswa.2025.126558
  - "Hierarchical text classification utilizing logic rule constraints through message passing" (2026), https://doi.org/10.1016/j.eswa.2026.132834
  - "Medical chief complaint classification with hierarchical structure of label descriptions" (2024), https://doi.org/10.1016/j.eswa.2024.123938
- **Use.** Cite a selection of these in the introduction and related work. This shows fit and engages prior ESWA work, which a simulated reviewer can check. No source says ESWA *requires* citing prior ESWA work [UNVERIFIED]. Several vendor and Chinese guides imply it, without evidence.

### 1.3 Review model (single vs double anonymized)

- **Double anonymized** [OFFICIAL-SNIPPET]. Search-engine renderings of the ESWA Guide for Authors (https://www.sciencedirect.com/journal/expert-systems-with-applications/publish/guide-for-authors) state that the journal follows a double anonymized review process: author identities are concealed from reviewers and vice versa. The title page (with author details) and the anonymized manuscript (without author details) are submitted as separate files. Three independent extended searches returned consistent snippets.
- **Conflicting older sources** say "single anonymized": an undated academia.edu copy of an older guide (https://www.academia.edu/77603820/Expert_Systems_with_Applications) and a template site. These are likely out of date.
- **Practical rule: prepare a double-anonymized package regardless.** Elsevier's double-anonymized requirements [OFFICIAL], https://www.elsevier.com/reviewer/what-is-peer-review/guidelines:
  - "The title page will remain separate from the manuscript throughout the peer review process." It holds the authors, affiliations, acknowledgements and COI statement.
  - "Use third person to refer to work the authors have previously published." For example, "Black and Hart (2015) have demonstrated".
  - "Make sure that figures and tables do not contain any reference to author affiliations."
  - Anonymize file names and document properties.
  - For a paper with public code this also means anonymizing the code and data links, for example with an anonymous repository. This step is my inference, not stated by ESWA.
- Status: **[PARTIALLY VERIFIED]**. Confirm in Editorial Manager, which lists separate "Title page" and "Manuscript (anonymized)" upload types if the journal is double anonymized.

### 1.4 Initial editor screening (desk review)

- [OFFICIAL-SNIPPET] ESWA Guide for Authors: "Your submission will initially be assessed by our editors. The decision as to whether your article is accepted or rejected for publication will be made by our editors."
- Elsevier's generic editor training, "Editor Essentials: Initial submission assessment" [OFFICIAL]. Text was extracted from the PDF at https://researcheracademy.elsevier.com/uploads/2021-02/EE%20Initial%20submission%20Nov2020.pdf (dated Nov 2020).
  - Submission checks include completeness against the Guide for Authors, "a complete declaration of interest statement", "Assessing the iThenticate similarity check results", and conformity to field protocols.
  - Language decision tree:
    - If the scope or impact "does not meet the threshold for peer review", the result is a "Desk reject based on scope or impact".
    - If the language is "too poor for reviewers to assess the merit", the editor requests revisions before review.
    - If the language is "not perfect, but sufficiently understandable", the editor sends the paper for peer review.
  - Similarity check: "Every paper is run through a similarity check". "Peer reviewed conference proceedings are considered prior publication, conference program abstracts are not". "Elsevier encourages authors to share their preprint anywhere at any time".
  - Summary checklist before peer review: all files submitted, "good, readable English", passed the iThenticate check, declaration of interest available, applicable guidelines followed.
- Elsevier plagiarism detection [OFFICIAL], https://www.elsevier.com/editor/perk/plagiarism-complaints/plagiarism-detection. Many Elsevier journals screen all new submissions automatically with Crossref Similarity Check (iThenticate) inside the editorial system. It does not compare against manuscripts still under review.
- Elsevier editors may also use in-house private AI tools for "finding reviewers, matching scope, and detecting duplicate submissions" [OFFICIAL]. Source: https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals (policy updated June 2026).

### 1.5 Number of reviewers

- No official ESWA statement found [UNVERIFIED].
  - A search that matched "minimum of two (2) external referees" turned out to be *Intelligent Systems with Applications*, a different journal. Do not attribute that wording to ESWA.
- [COMMUNITY] SciRev, https://scirev.org/journal/expert-systems-with-applications/ (n = 20): "Average number of review reports (first round)" is 2.2. Per-entry values range from 1 to 4, and 2 is the most common.
- [COMMUNITY, via search snippet; the Zhihu page returned 403] https://www.zhihu.com/question/662933076 says "ESWA的系统默认需要2个审稿人意见，AE处理文章时，可以修改这个数字". The answer adds that the editor may decide on a single report.
- [COMMUNITY] SciRev complaint: "Finalizing a decision based on the comments of a single reviewer based on a few benchmark results".
- [VENDOR] manusights says ESWA "typically invites two to three reviewers" (unsourced). https://manusights.com/blog/expert-systems-with-applications-submission-guide
- **Simulation default:** two reviewers plus a handling editor (Associate Editor), with a possible third reviewer.

### 1.6 Timelines

- **Official journal-insights metrics.** Two sets of values are in circulation:
  - **Set A** [OFFICIAL-SNIPPET plus many secondary copies]: 5 days submission to first decision; 62 days submission to decision after review; 147 days submission to acceptance; 7 days acceptance to online publication.
    - Reproduced by Peeref (https://www.peeref.com/journals/2799), LetPub CN (https://www.letpub.com.cn/index.php?journalid=2799&page=journalapp&view=detail) and manusights ("checked 2026-10-21").
  - **Set B** [OFFICIAL-SNIPPET; search engine described it as the current Insights page]: 7 days to first decision; 101 days review to decision; 187 days submission to acceptance; 5 days acceptance to publication.
    - Insights page: https://www.sciencedirect.com/journal/expert-systems-with-applications/about/insights
  - Status: **[CONFLICTING; live page unreadable]**. Either way, the "first decision" figure includes desk decisions, so a desk decision usually comes within about a week.
- **SciRev** [COMMUNITY] (n = 20, undated entries):
  - First review round: 5.4 months on average. Per-entry median 13.1 weeks; range 5.6 to 73.9 weeks.
  - Total handling time for accepted papers: 7.7 months.
  - Immediate rejection: 13 days (per-entry 3 to 27 days).
  - Review rounds: 1.9 on average.
  - Report quality: 2.6/5. Difficulty: 3.9/5 ("difficult"). Overall rating: 2.1/5.
  - Outcomes: 5 accepted, 8 rejected after review, 6 immediate rejections, 1 withdrawn after 176 days with no review.
  - URL: https://scirev.org/reviews/expert-systems-with-applications/
- **LetPub** [COMMUNITY]: "Average Peer Review: About 13.8 month(s)" and "Competitiveness 16%". The page shows a count of user posts but no definition of these figures. https://www.letpub.com/journal-selector/journal/2799
- **Individual timelines** [COMMUNITY]:
  - CSDN (posted 2024-08-30), https://gitcode.csdn.net/6aa0d9ad1a35784c84206bc9.html
    - Submit 2023-11-05 → Under Review 2023-11-17 → Revise 2024-01-07.
    - Under Review again 2024-01-31 → Revise 2024-04-12 → Revise 2024-06-12.
    - Accepted 2024-06-28.
    - In total: three revision rounds, about 7.7 months.
  - Eastmount blog, https://blog.csdn.net/Eastmount/article/details/143300377 (also mirrored at https://gitcode.csdn.net/6aa0dace1a35784c84207339.html, 2024-12-10)
    - Submit 2024-10-28 → With Editor 10-30 → Under Review 11-04 → Decision in Process 12-25.
    - The paper was still in DIP about two months later.
  - CSDN promo article (2025-07-24), https://damodev.csdn.net/6a431a27662f9a54cb85e7e0.html. One user's record runs from submission on 2025-04-12 to acceptance on 2025-07-21, with two "Revise" rounds. In round 2, one reviewer repeated the round-1 comments ("一个意见和第一轮一样").
- **Planning assumption:** desk decision in about 1 to 2 weeks; first decision after review in roughly 2 to 5 months (high variance); total about 6 to 9 months with 2 or 3 rounds. Multiple revision rounds are common.

### 1.7 Acceptance and desk-rejection rates

- **11% acceptance** [UNVERIFIED-OFFICIAL]. manusights attributes this to the "Elsevier journal catalog" (checked 2026-10-21) and notes the reporting period is unspecified (https://manusights.com/journals/expert-systems-with-applications). I could not load the Journal Finder entry (JS-rendered), so this is unconfirmed.
- **16% "Competitiveness"** [COMMUNITY, LetPub; undefined metric].
- **12–15%** [VENDOR, unsourced]; **about 27%** [VENDOR, nativeee.com 2025-04-27, uncited]. Do not use either.
- **Desk-reject rate:** no official figure exists [UNVERIFIED]. In the SciRev sample, 6 of 20 reports (30%) were immediate rejections, but the sample is self-selected. The nativeee claim that an "AI预审系统" filters about 20% of submissions is uncited.

### 1.8 Editors

- **Editor-in-Chief: Prof. Ling Wang (王凌), Tsinghua University** [SECONDARY]. Source: Beijing University of Chemical Technology news item (URL path dated 2025-12-17), https://english.buct.edu.cn/2025/1217/c9113a215943/page.htm. It refers to "Professor Wang Ling from Tsinghua University ... Editor-in-Chief of the international top journal Expert Systems with Applications", who invited Prof. Yongming Han as Associate Editor.
- **Binshan Lin** (LSU Shreveport) appears as EIC in LSUS pages (https://lsus.edu/binshan-lin-phd), which are probably out of date.
- Status: the official masthead (https://www.sciencedirect.com/journal/expert-systems-with-applications/about/editorial-board) returned 403, so **current EIC and handling-editor list is [UNVERIFIED]**.
- The board uses Associate Editors; several universities announce AE appointments (e.g. Istinye Univ., https://www.istinye.edu.tr/en/mdbf/news/dr-erfan-babaee-tirkolaee-joined-editorial-board-expert-systems-application-eswa). nativeee claims two AEs were added for Chinese-region submissions [VENDOR, UNVERIFIED].

### 1.9 Other journal facts (context only)

- Impact factor: 7.5 is widely reported, for JCR 2024 released in 2025 (BUCT; CSDN). manusights reports 9.4 for JCR 2025 released in 2026 [UNVERIFIED].
- CiteScore: 17 (LetPub).
- About 4,059 articles per year (Peeref) and a large Chinese-author share (CSDN reports 64.43%; [COMMUNITY]).
- Hybrid journal, with a subscription route that has no fee. The OA APC is reported as USD 3,630 by manusights [UNVERIFIED].
- Submission is through Editorial Manager at https://www.editorialmanager.com/eswa (LetPub link).

---

## 2. Reviewer guidelines and questionnaire

### 2.1 Elsevier generic reviewer guidance [OFFICIAL]

Source: https://www.elsevier.com/reviewer/how-to-review

- **Before accepting:** "Only accept if you feel you can provide a high-quality review". Disclose conflicts of interest and keep the content confidential.
- **What to evaluate in an original research article:**
  - Title and abstract: accuracy, including major results and limitations.
  - Introduction: current background and clear objectives.
  - Methods: enough detail to allow replication, including design, sample size and statistical reporting.
  - Results: effective tables and figures, and whether further analyses are needed, such as "confidence intervals, effect sizes, sensitivity analyses".
  - Discussion: conclusions supported by the data, and limitations acknowledged.
  - References: current and relevant.
  - Language: whether professional editing is needed.
  - Overall: novelty, importance, and ethical or integrity concerns.
- **Research-data check:** major flaws include insufficient data points, unclear tables, and claims supported by non-significant variation.
- **Report-writing rules:**
  - Summarize the article and give your main impressions; reference specific sections.
  - Check the abstract, graphical abstract and **highlights**.
  - Raise suspected plagiarism with the editor.
  - Do not comment on spelling or layout (recommend language editing instead).
  - Do not suggest citations to your own work unless scientifically justified.
- **Recommendation categories:** Accept; Revise (minor or major, specifying the changes and whether you will re-review); Reject (with reasons). A reviewer who recommends revision is agreeing to a follow-up review.
- **Comments:** separate confidential comments to the editor and comments to the author(s). The editor decides.

### 2.2 Editorial Manager review form

Editorial Manager lets each journal customize the reviewer form: a recommendation drop-down, comments to author, comments to editor, and optional rating questions (Aries Systems, https://www.ariessys.com/wp-content/uploads/Reviewer_Questions_VS_EMUG-2017.pdf).

**The ESWA-specific reviewer questionnaire (rating questions, "within scope?", etc.) was not found in any public source [UNVERIFIED].**

A simulated ESWA review should use the Elsevier criteria in 2.1 plus the recommendation set Accept / Minor Revision / Major Revision / Reject. The exact ESWA labels are [UNVERIFIED].

### 2.3 Structured peer review

Elsevier states that some journals use structured peer-review forms and that reviewers should check the journal's guide. Whether ESWA uses one is [UNVERIFIED].

---

## 3. Frequent reviewer criticisms on ESWA papers (as publicly reported)

**Direct ESWA reviewer text is scarce.** I found no public collection of real ESWA reviewer reports. ESWA does not publish its reports, and no open peer review was found. The evidence below comes from community complaints, vendor opinion and Elsevier's criteria.

| Criticism | Evidence | Strength |
|---|---|---|
| Benchmark-only, narrow empirical evidence | SciRev: "Finalizing a decision based on the comments of a single reviewer based on a few benchmark results" | [COMMUNITY], 1 report |
| Outdated or unfair baselines; missing ablations; missing significance tests | manusights rebuttal guide says ESWA reviewers grade "benchmarking fairness, reproducibility, and application substance". Its example comments ("The baselines are outdated and the comparison is not fair", "An ablation study is needed...") are **invented illustrations**, not real quotes. https://manusights.com/blog/expert-systems-with-applications-response-to-reviewers | [VENDOR] |
| Reproducibility: "code available on request" | manusights flags "code available on request" as a failure pattern | [VENDOR] |
| Insufficient methodological novelty; not beating SOTA; unclear engineering or application value | nativeee (2025-04-27) gives 42% / 36% / 22% shares for these reasons, **uncited** (https://www.nativeee.com/index.php/news/814.html). The post also says reviewers now focus on industrial deployability and that ablation plus cross-dataset validation are "编辑最新内部要求" | [VENDOR, UNVERIFIED] |
| Unclear motivation | CSDN guide's example comment "The motivation of this work is not clear." is fictional (https://blog.csdn.net/weixin_42523907/article/details/166109868, 2026-09-25) | [VENDOR, illustrative] |
| Repeated or unchanged comments across rounds | CSDN 2025 timeline: "一个意见和第一轮一样" | [COMMUNITY] |
| Limitations, effect sizes, sensitivity analyses, replicable methods, current references | Elsevier how-to-review criteria (§2.1) | [OFFICIAL, generic] |
| Poor English | Elsevier Editor Essentials language decision tree (§1.4) | [OFFICIAL, generic] |

The following items from the brief were **not found as ESWA-specific public evidence [UNVERIFIED]**: complexity/runtime analysis, hyperparameter sensitivity, dataset bias, poor figures, missing recent ESWA citations and excessive self-citation.

They are standard in applied ML venues, so keep them in the simulation checklist as expected rather than evidenced. The Elsevier criterion of "sensitivity analyses" covers hyperparameter sensitivity loosely.

---

## 4. Common desk-reject reasons at ESWA

**Official or explicit:**

1. Military or defense application: "no longer considers" [OFFICIAL].
2. Metaphor-based or renamed algorithms with no formal differentiation: discouraged [OFFICIAL].
3. Scope or impact below the threshold for peer review [OFFICIAL, Elsevier generic].
4. Language too poor to assess [OFFICIAL, Elsevier generic]. The usual action is to return the manuscript for revision before review.
5. Incomplete submission package, missing declaration of interest, or a high or problematic iThenticate overlap. This includes overlap with a prior peer-reviewed conference version, which "is considered prior publication" [OFFICIAL, Elsevier generic].

**Reported by vendors or the community (not ESWA-confirmed):**

6. A "methods paper in an application journal". manusights says the most common desk rejection is an abstract presenting a generic method with Figure 1 showing an architecture schematic and no application substance [VENDOR, based on their "pre-submission reviews"].
7. Application context treated as decoration; outdated or selective baselines [VENDOR].
8. Lack of novelty [COMMUNITY; one Chinese Q&A and generic advice].
9. Transfer: desk rejections "can come with a transfer offer" to Knowledge-Based Systems, Applied Soft Computing, EAAI, Pattern Recognition or Neurocomputing [VENDOR, unsourced list]. SciRev's Applied Soft Computing page records an ESWA editor proposing a transfer to ASC (https://scirev.org/journal/applied-soft-computing/, via search snippet).

**"Too many self-citations" and "salami slicing"** were not found as ESWA-specific reasons [UNVERIFIED]. Elsevier's general integrity and similarity checks would catch redundant publication.

---

## 5. Response-to-reviewers practices reported for ESWA

- **Decision letter format** [OFFICIAL-SNIPPET of a real 2019 ESWA decision letter, ESWA-D-19-04650R1, https://oa.upm.es/78335/1/ESWA-D-19-04650_R1.pdf]. The letter asks for a "Detailed Response to Reviewers" with two labelled sections: (1) the editor's full decision letter with the author's reply, and (2) the entire comments made by the reviewer with "Point-to-Point responses to the Reviewer". This letter is from 2019, so the current template may differ.
- **Upload both a highlighted-changes manuscript and a clean manuscript** [COMMUNITY: CSDN 2024 author]. manusights says the same, without a source.
- **Quote each comment, answer every one, and cite the page and line of the change in the revised manuscript** [VENDOR; CSDN guide].
- **Expect 2 or 3 rounds.** SciRev averages 1.9 rounds; one CSDN author needed 3 rounds before acceptance; another had 2. Late rounds can turn around quickly: in the 2024 timeline, round 3 went from revise to accepted in about 2 weeks.
- **Responding to "lack of novelty"** [COMMUNITY]: Zhihu column https://zhuanlan.zhihu.com/p/687173582 (via snippet).
  - If only one reviewer raises novelty and the others do not, "还是有机会争取的".
  - Compare the work point by point against the specific related work and add experiments.
  - A CSDN author reports turning a "no novelty" view around with added comparison and ablation experiments [COMMUNITY, unverifiable].
- **If an experiment cannot be done,** explain why and offer an alternative, such as a supplementary public-dataset experiment [COMMUNITY].
- **Chasing a slow review:** enquire politely only after more than about 3 months in "Under Review", at most monthly [COMMUNITY]. SciRev shows that very long waits (9 to 17 months) do happen.
- **Proofs:** about 48 hours to confirm [COMMUNITY, UNVERIFIED].

---

## 6. ESWA and Elsevier policies relevant to review

### 6.1 Generative AI [OFFICIAL]

Source: https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals ("Policy updated June 2026").

- **Authors:**
  - Declare AI use "in a separate AI declaration statement", placed at the end of the manuscript immediately before the references.
  - "Basic checks of grammar, spelling and punctuation do not need a declaration statement."
  - Not allowed: "Generating sections of a manuscript without genuine intellectual contribution from the author".
  - The ESWA guide has a "Declaration of generative AI use" section [OFFICIAL-SNIPPET].
- **Reviewers:**
  - "Reviewers should not upload a submitted manuscript or any part of it into an AI tool."
  - Use "only private AI tools" for supportive tasks.
  - Disclose AI use in the comments to authors.
- **Editors:** must not upload manuscripts to external AI tools. They have access to Elsevier-internal AI for reviewer finding, scope matching and duplicate detection.
- **Implication:** a manuscript that uses LLMs as *research objects* (e.g. annotators) is in a different position: That is methodology, not writing assistance, and belongs in Methods. Any LLM use for writing needs the separate declaration.
- **Implication for the skill:** when the future "review ESWA papers" mode is used by a human reviewer, they must not paste the manuscript into a non-private AI tool.

### 6.2 Conflicts of interest

- Reviewers must disclose COI before accepting [OFFICIAL, how-to-review].
- Authors need a declaration of interest statement. Elsevier's Declaration Tool produces a Word file (CSDN 2024) and the Editor Essentials checklist requires it [OFFICIAL].

### 6.3 Suggested reviewers

- **Conflicting [UNVERIFIED].**
  - CSDN authors (2023–2024) say the system *required* suggested reviewers, and recommend 3–5.
  - A related-post snippet on CSDN says the ESWA flow now has "少了一步，推荐审稿人" (one step fewer: no suggested reviewers).
  - The official guide snippet surfaced no "suggesting reviewers" section.
- Check in Editorial Manager at submission time. If the field is offered, prepare 3–5 names with no COI and avoid same-institution names. nativeee also claims the system avoids same-IP reviewers [UNVERIFIED].

### 6.4 APC and open access vs. review

- Elsevier [OFFICIAL], https://www.elsevier.com/about/policies-and-standards/editorial-independence: "the editorial decision making processes of our publications are kept separate from our commercial interests". The page does not explicitly mention APC or OA choice.
- A CSDN author's remark that paid OA is "possibly faster" is [COMMUNITY, UNVERIFIED] and should be disregarded.

### 6.5 Formatting items checked by editors and reviewers

- Abstract ≤ 250 words [OFFICIAL-SNIPPET].
- Highlights: 3–5 bullets, each ≤ 85 characters including spaces, in a separate editable file [OFFICIAL-SNIPPET]. The snippet describes them as optional but encouraged; CSDN authors treat them as required. **Supply them anyway** — reviewers are told to check them.
- Other items reported by CSDN authors [COMMUNITY]:
  - CRediT author statement.
  - 3–5 classifications.
  - ORCID for all authors.
  - Cover letter (not a copy of the abstract).
  - Figure resolution (line art ≥ 1000 dpi; greyscale or colour ≥ 300 dpi).
  - elsarticle-num style.
- Preprints are allowed: "Elsevier encourages authors to share their preprint anywhere at any time" [OFFICIAL, Editor Essentials]. Under double-anonymized review, do not cite the preprint in a way that identifies the authors.

---

## 7. (Removed)
Paper-specific implications were moved to the author's private review log.

---

## 8. Source list (all accessed 2026-10-29)

**Official (fetched directly)**
- ESWA journal page / scope: https://shop.elsevier.com/journals/expert-systems-with-applications/0957-4174
- Elsevier how to review: https://www.elsevier.com/reviewer/how-to-review
- Elsevier generative AI policy: https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals
- Elsevier double-anonymized guidelines: https://www.elsevier.com/reviewer/what-is-peer-review/guidelines
- Elsevier editorial independence: https://www.elsevier.com/about/policies-and-standards/editorial-independence
- Elsevier Editor Essentials, Initial submission assessment (PDF, Nov 2020): https://researcheracademy.elsevier.com/uploads/2021-02/EE%20Initial%20submission%20Nov2020.pdf

**Official, search snippets only (the live pages returned 403)**
- ESWA Guide for Authors: https://www.sciencedirect.com/journal/expert-systems-with-applications/publish/guide-for-authors
- ESWA Insights: https://www.sciencedirect.com/journal/expert-systems-with-applications/about/insights
- Elsevier plagiarism detection: https://www.elsevier.com/editor/perk/plagiarism-complaints/plagiarism-detection
- 2019 ESWA decision letter: https://oa.upm.es/78335/1/ESWA-D-19-04650_R1.pdf

**Bibliographic data**
- OpenAlex API queries (ISSN 0957-4174), as listed in §1.2
- arXiv:2510.14581

**Community**
- SciRev ESWA: https://scirev.org/journal/expert-systems-with-applications/ and https://scirev.org/reviews/expert-systems-with-applications/
- LetPub: https://www.letpub.com/journal-selector/journal/2799 and https://www.letpub.com.cn/index.php?journalid=2799&page=journalapp&view=detail
- Peeref: https://www.peeref.com/journals/2799
- CSDN / gitcode: https://gitcode.csdn.net/6aa0d9ad1a35784c84206bc9.html, https://gitcode.csdn.net/6aa0dace1a35784c84207339.html, https://blog.csdn.net/Eastmount/article/details/143300377, https://damodev.csdn.net/6a431a27662f9a54cb85e7e0.html, https://blog.csdn.net/weixin_42523907/article/details/166109868
- Zhihu (snippets only): https://www.zhihu.com/question/662933076, https://zhuanlan.zhihu.com/p/687173582
- Baidu Zhidao: https://zhidao.baidu.com/question/2023876246702973548.html (generic; no content)

**Editors**
- BUCT news item: https://english.buct.edu.cn/2025/1217/c9113a215943/page.htm
- LSUS biography: https://lsus.edu/binshan-lin-phd

**Vendor (low reliability)**
- https://manusights.com/blog/expert-systems-with-applications-submission-guide
- https://manusights.com/journals/expert-systems-with-applications
- https://manusights.com/blog/expert-systems-with-applications-review-time
- https://manusights.com/blog/expert-systems-with-applications-response-to-reviewers
- https://manusights.com/blog/rejected-from-expert-systems-with-applications-where-next
- https://www.nativeee.com/index.php/news/814.html
