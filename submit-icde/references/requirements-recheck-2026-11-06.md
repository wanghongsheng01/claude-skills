# ICDE 2027 research track: requirements re-check (Round 2) and reviewer-evaluation evidence

Re-check date: 2026-11-06 (Asia/Shanghai). Round 2 deadline: 2026-11-11, 17:00 PST.
Purpose: input for upgrading the `submit-icde` and `review-icde` skills.
Written in English at the explicit request of this task (an exception to the usual Chinese-report convention).

Legend: **[V]** verified on the cited page during this re-check. **[V-hist]** verified in the site's public Git history. **[2nd]** secondary source only. **[UNVERIFIED]** could not be confirmed from a public source. **[INF]** my inference from verified text.

Primary URLs:
- CFP: https://icde2027.github.io/cf-research-papers.html
- Submission guidelines: https://icde2027.github.io/submission-guidelines.html
- Important dates: https://icde2027.github.io/important-dates.html
- Formatting guidelines (linked in menu): https://icde2027.github.io/formatting-guidelines.html (HTTP 404)
- FAQ: https://icde2027.github.io/faq.html (HTTP 404; the menu has only a "Sponsorship FAQ")
- Site source / history: https://github.com/icde2027/icde2027.github.io (commits API: https://api.github.com/repos/icde2027/icde2027.github.io/commits)
- CMT: https://cmt3.research.microsoft.com/ICDE2027 (redirects to the login page; the submission form itself is not public)

---

## 0. Diff against the 2026-11-03 snapshot

**Nothing has changed since the snapshot.** [V]
- I downloaded the live index, cf-research-papers, submission-guidelines, formatting-guidelines (404), important-dates, accepted-papers and cf-future pages on 2026-11-06. Each is **byte-identical** to the copy in `01_guidelines/raw/`.
- The HTTP `last-modified` header for cf-research-papers.html is `Wed, 28 Oct 2026 16:53:49 GMT`. The newest commit in the site repository is `a414777f` (2026-10-28T16:52Z). There have been no commits after the snapshot. [V-hist]
- There is no FAQ page, no CMT-instructions page, no formatting-guidelines page (404) and no reviewer-guidelines page. `cf-research-papers-temp.html` exists in the repo, but it is an empty stub with old dates (May 10-14) and contains no rules. [V]

**Changes before the snapshot that matter (2026-10-28 commit `ee76fd2f` "CFP,AP,PCI")** [V-hist]. That commit rewrote the CFP **but left submission-guidelines.html with older text**. The two official pages now disagree on several points; see §1.14. The CFP is the newer text and should be treated as authoritative. [INF]
- The COI definition in the CFP reverted to calendar anchors ("2023 to the present", "four or more papers 2016 to the present") and added "use Domain Conflicts" for co-workers. The submission guidelines still say "past three years" and "4 or more in the last 10 years".
- Registration: the CFP now says "At least one full author registration… One registration can only count towards a single paper… IEEE reserves the right to exclude a paper… (including removing it from IEEE Xplore)". The submission guidelines still say "presentation at the conference is not required".
- The 1-year wait in the CFP now reads "Papers rejected from ICDE, **including revisions of such papers**, cannot be submitted to ICDE until a year has passed since the rejection".
- The out-of-scope rule now says explicitly that positioning "is typically done by explaining in the paper, as part of its coverage of related work, how the paper builds on and extends contributions published in … ICDE, VLDB, or SIGMOD".
- The page-limit wording changed from "AI-generated content acknowledgement" to "AI-generated content declaration".
- The template rule now reads: "The use of negative spaces, content entering the margins, or similar are considered violations of the format."
- Earlier relevant edits: 2026-05-28 `9a184498` changed the per-author quota from "5 across both rounds" to "**5 per submission round**". 2026-09-23 `2b32d4fa` added the camera-ready section. 2026-04-23 `d6a76ae2` replaced the topic list. [V-hist]

**Error found in the earlier check (`01_guidelines/01_ICDE2027_指南核查.md`).** It gives the Round 2 deadline as Beijing 08:00 on 11-12. US daylight saving time ended on 2026-11-01, so 17:00 on 2026-11-11 is **PST (UTC-8) = 2026-11-12 01:00 UTC = 09:00 Beijing**. The 08:00 figure is only correct for Round 1 (PDT). (Computed with Python zoneinfo.) The rebuttal close (2027-01-15 17:00 PST) and the camera-ready deadline (2027-03-10 17:00 PST) are also 09:00 Beijing on the following day. [V]

---

## 1. ICDE 2027 research-track requirements (Round 2)

### 1.1 Dates and rounds [V] (CFP; important-dates)
| | Round 1 | Round 2 |
|---|---|---|
| Submission due | 2026-06-11 | **2026-11-11** |
| Author rebuttal period | 2026-08-08 to 08-15 | **2027-01-08 to 01-15** |
| Notification (Accept/Reject) | 2026-09-10 | **2027-02-10** |
| Camera-ready due | 2026-10-10 | **2027-03-10** |
- "All deadlines are 5:00PM Pacific Time." "Notification dates are approximate."
- "Each submission round provides an Accept/Reject notification without the option for revision."
- Submission is through CMT, which opens "a week before the submission deadline of each round". The index page says "The Round 2 submission is open with deadline November 11, 2026". [V] https://icde2027.github.io/index.html
- Conference: Copenhagen, 2027-05-17 to 21.

### 1.2 Paper categories [V] (CFP)
- **Regular research papers** present "original contributions related to the topics of interest".
- **Experimental, Analysis, and Benchmark (EAB)** papers cover "extensive evaluation of algorithms, data structures, and systems that are of wide interest, or … benchmarks". Their contribution is "fundamentally new insight into the strengths and weaknesses of existing methods, or new ways to evaluate existing methods". The title must start with `[Experiment, Analysis, and Benchmark]`. The tag is removed in the camera-ready version.

### 1.3 Template, format and PDF
- "Manuscripts must be prepared in accordance with the IEEE format available at https://www.ieee.org/conferences_events/conferences/publishing/templates.html." [V] (CFP)
  - That IEEE URL returns HTTP 202 (a bot challenge) to automated clients, so I could not read its content. [UNVERIFIED content] Secondary copies say the page offers LaTeX and Word conference templates in US Letter and A4, and that the templates are optional for IEEE generally. [2nd] https://cai.ieee.org/2025/manuscript-templates-for-conference-proceedings/
  - Official Overleaf "IEEE Conference Template" (author IEEE): `\documentclass[conference]{IEEEtran}`. Its notes say all template text must be removed before submission; no symbols, special characters, footnotes or math in the title and abstract; no sub-titles. [V] https://www.overleaf.com/latex/templates/ieee-conference-template/grfzhhncsfqn
  - IEEEtran is V1.8b (2015/08/26, Michael Shell). Its default paper size is **letterpaper**, with a4paper as an option. [V] https://ctan.org/pkg/ieeetran ; local `IEEEtran.cls` lines 142 and 374.
  - ICDE itself does **not** state a paper size, font or PDF version for the submission. The Formatting Guidelines page is a 404. [V] US Letter is the IEEEtran default and is safe; A4 is not stated to be forbidden. [INF]
- "The use of negative spaces, content entering the margins, or similar are considered violations of the format." [V] (CFP; the submission guidelines omit this sentence.)
- "Only electronic submissions in PDF format will be considered." [V]

### 1.4 Page limit and appendix [V] (CFP)
- "Research and EAB papers must not exceed **12 pages**, excluding references and the AI-generated content declaration … No appendix is allowed."
- **Only** the references and the AI declaration are excluded. Any other acknowledgment (funding, thanks) and any "supplementary" section inside the PDF counts toward the 12 pages. [INF from the exact wording]
- No cap on reference pages is stated. ICDE 2023 and 2024 stated "12 pages for the main text plus up to 4 pages for the bibliography"; ICDE 2027 has no such cap. [V] https://icde2024.github.io/CFP_research.html ; https://icde2023.ics.uci.edu/research-papers-track/
- Camera-ready: "adheres to the 12-page limit excluding the AI-generated content acknowledgments and the references". [V] (CFP, camera-ready section)

### 1.5 Review model and anonymity [V] (CFP)
- "Submissions are reviewed in a single-blind manner." Author names and affiliations appear on the paper.
- Supplemental-material hosting must not "track back to the reviewers and jeopardize anonymity". Reviewer anonymity is what is protected, so personal web pages are not allowed.

### 1.6 ORCID [V] (CFP and submission guidelines)
- "ORCIDs are required for all authors at the time of paper submission."
- Where the ORCID is entered (CMT profile or submission form) is not stated. [UNVERIFIED]

### 1.7 CMT profile and conflicts of interest
- "each author of a submission must create a CMT profile and complete it with domain and individual conflicts. If a CMT profile is missing even for one author of a submission, the paper will be desk rejected." [V] (CFP)
- "You can mark your conflicts by clicking on your name (upper right-hand side on CMT) and selecting Domain Conflicts and Individual Conflicts. An author's declared conflicts will be automatically applied to all of their submissions." [V] (CFP)
- COI definition (CFP, newest wording). X has a COI with a PC or **senior PC** member Y iff [V]:
  1. X and Y are co-authors of **a submission under review** (any venue, not only ICDE).
  2. X and Y are co-authors of a paper published during **2023 to the present**.
  3. X and Y are co-authors of **four or more papers published during 2016 to the present**.
  4. X and Y were co-workers in the same company or university during 2023 to the present. "(Use **Domain Conflicts** to indicate this type of COI.)"
  5. X and Y were collaborators within the past three years / during 2023 to the present (e.g., a joint grant). Both bullets are present.
  6. X is or was Y's primary thesis advisor or vice versa, no matter how long ago.
  7. X and Y are relatives or close friends.
- "Papers with incorrect or incomplete COI declarations as of the submission closing time are subject to desk rejection." "Failure to report COIs or frivolous declaration of COIs count as violations. All submissions will be checked for violation via automated software." [V] (CFP)
- CMT mechanics (Microsoft CMT documentation) [V] https://cmt3.research.microsoft.com/docs/help/chair/conflicts.html :
  - "An Author must submit a paper before they can see the Individual Conflicts in their name dropdown." Each author therefore has to mark individual conflicts **after** the paper record exists and **before** the deadline.
  - Domain conflicts are entered as semicolon-separated domains, e.g. "washington.edu; mit.edu". Entering an institution name gives an error. Do not enter public e-mail domains (gmail.com etc.). List every domain an institution uses.
  - Whether ICDE enabled per-submission conflict pages is [UNVERIFIED]. The CFP says the profile-level conflicts apply to all submissions.

### 1.8 Per-author quota, duplicates, novelty, 1-year rule [V] (CFP)
- "An author may submit a maximum of **5 papers** to the research track (regular and EAB papers combined) **per submission round**." This changed on 2026-05-28 from "5 across both rounds". [V-hist]
- Duplicate submissions: the paper "cannot be under review for any other conference or journal during the entire time it is under consideration" (for Round 2 this runs through about 2027-02-10). It "must be substantially different from any previously published work".
- Novelty: the work must be "not described in any prior publication that is more than 4 double-column pages". Overlapping prior publications must be cited "even if this prior publication does not exceed the 4-page threshold".
- 1-year wait: "Papers rejected from ICDE, including revisions of such papers, cannot be submitted to ICDE until a year has passed since the rejection." A Round 1 reject cannot go to Round 2; it can go to ICDE 2028 Round 1.
- Re-submission policy: "Submissions that were desk-rejected in Round 1 due to COI violations or failure to follow length and formatting instructions **may** be resubmitted in Round 2. Submissions that were rejected in Round 1 for being out-of-scope … **cannot**."
- No title or author change after acceptance; reviewers may request a title change. The camera-ready section adds: "it is not allowed to change, in the final version, the title/abstract/authors or any of the metadata submitted to the CMT."

### 1.9 Supplemental material [V] (CFP)
- "Authors are expected to submit supplemental material, such as code, data, and other implementation artifacts … Availability of the supplemental material will be considered in the evaluation of the paper."
- If none is provided, "an explanation should be provided in the submission form".
- "EAB papers MUST provide all artifacts necessary to reproduce the results. No exceptions in this paper category are allowed."
- Provide it "through a URL pointing to standard, openly accessible file sharing services with well-understood privacy policies (e.g., a public GitHub repo). Personal webpages … are not acceptable."
- Whether CMT also accepts an uploaded supplementary file is [UNVERIFIED] (the form is behind login).

### 1.10 AI-generated content
- ICDE wording [V] (CFP):
  - "Generative AI tools and technologies, such as ChatGPT, may not be listed as authors."
  - The use of AI-generated content "(including but not limited to, text, figures, images, and code) shall be disclosed in the acknowledgments section".
  - "authors should mention tools (including LLMs) that were used for data processing, filtering, visualisation, and facilitating or running experiments."
  - "The AI system used shall be identified, and specific sections of the article that use AI-generated content shall be identified and accompanied by a brief explanation regarding the level at which the AI system was used."
  - "The use of AI systems for editing and grammar enhancement is … generally outside the intent of the above policy. Authors remain responsible for correctness and originality."
  - The CFP cites the IEEE guideline copy at https://icbc2025.ieee-icbc.org/ai-content-generation-guidelines. That page's TLS certificate fails verification, so it was not read. [UNVERIFIED]
- Camera-ready: "Note that the AI-generated content disclosure acknowledgments are **mandatory**." [V] (CFP). [INF] Include the section in every version, with an explicit statement even if the only use was grammar editing or no AI was used.
- IEEE Author Center policy [V] https://conferences.ieeeauthorcenter.ieee.org/author-ethics/guidelines-and-policies/submission-policies/ :
  - For editing and grammar use, disclosure "is not required, but recommended".
  - "If using an AI system for editing and grammar, exclude the reference section."
- Heading and placement: ICDE 2026 required an "AI-Generated Content Acknowledgement" section "just before References" and said "when unsure, disclose". [V] https://icde2026.github.io/cf-research-papers.html . ICDE 2027 says only "acknowledgments section". Using the ICDE 2026 heading, placed just before the references, satisfies both. [INF]
- The page limit is called "declaration" in the CFP and "acknowledgement" in the submission guidelines. These are the same item. [V]

### 1.11 Scope statement and subject areas
- Topics: 31 listed areas, including "Graph data", "Vector data", and "Foundation models and LLMs for data engineering and vice versa". [V] (CFP)
- "We expect that research contributions build on previous advances … as published in ICDE or other core conferences such as VLDB and SIGMOD." [V]
- Out-of-scope desk reject: the paper must align with at least one topic and position itself, "typically … as part of its coverage of related work", against ICDE/VLDB/SIGMOD work. "Submissions that purely advance data mining or machine learning approaches not relating to data engineering aspects would be considered as out of scope." [V]
- Optional explanation "(in 1000 characters) in the submission form" covering (a) the key data-engineering challenge(s), (b) principled ideas and contributions with section references, (c) ICDE/VLDB/SIGMOD research it builds on. Examples 1-3 count in favour; "a similar paper appeared at ICDE before" (#4) is insufficient. [V]
- The CMT subject-area list (primary/secondary) and the exact form field names are [UNVERIFIED]; the form is behind CMT login.

### 1.12 Review process and rebuttal
- "reviewed by at least 3 reviewers. The reviewing of a paper will be coordinated by a **senior PC member**, who will provide a meta-review based on the discussions about the paper. The outcome is either 'reject' or 'accept.' There will be no revisions." [V] (CFP). The submission guidelines say "coordinated by an area chair".
- Author rebuttal: 2027-01-08 to 01-15. [V] **No rebuttal format, length, file-upload rule or content restriction is published anywhere on the site.** [V that it is absent; format UNVERIFIED]
- Rebuttal is **new for ICDE**. ICDE 2023, 2024, 2025 and 2026 used Accept / Revise / Reject with one revision round of 4-5 weeks and no rebuttal. [V] https://icde2023.ics.uci.edu/research-papers-track/ ; https://icde2024.github.io/CFP_research.html ; https://ieee-icde.org/2025/cfp/ ; https://icde2026.github.io/cf-research-papers.html
- CMT Author Feedback mechanics [V] https://cmt3.research.microsoft.com/docs/help/author/author-feedback.html ; https://cmt3.research.microsoft.com/docs/help/chair/manage-author-feedback.html ; https://cmt3.research.microsoft.com/docs/help/author/author-feedback-author-comments.html :
  - The author uses "Post Author Feedback" with text fields defined by the chair. A rebuttal document upload is possible only "Sometimes … [if] the Chair will allow". Click Submit, or the file is not saved.
  - "Meta-Reviews may not be visible even though the link is present."
  - After feedback closes, reviewers and meta-reviewers may post follow-up comments if the chair enables it ("The number of comments is limited to 5"), and the author replies in the console.
  - CMT documents no default character limit. ICDE's limit is [UNVERIFIED].
- Review Quality Chairs exist for ICDE 2027: Yuchen Li (SMU) and Matteo Lissandrini (Verona). [V] https://icde2027.github.io/officers.html
- PC Chairs: Christian S. Jensen, Guoliang Li, Li Xiong. The site has separate Senior PC and PC lists. [V] https://icde2027.github.io/pc-chairs.html

### 1.13 Desk-reject causes (complete list) [V unless marked]
1. Non-compliance with the instructions for research papers (generic catch-all) (CFP).
2. Formatting or length violations: IEEE format, negative space, margins, more than 12 pages, any appendix.
3. COI violations: missing, incorrect or frivolous declarations; checked by automated software.
4. A missing CMT profile for any author.
5. Out of scope / relevance.
6. EAB without all artifacts. "No exceptions" is stated; that this is a desk reject rather than a review-stage reject is [INF].
7. Quota above 5 per author per round, under review elsewhere, prior-publication overlap, or a 1-year-rule violation. These are stated as eligibility rules, not explicitly in the desk-reject list. [INF: treat as reject without review]

### 1.14 Inconsistencies between the two official pages (all [V])
| Item | CFP (newer, 2026-10-28) | Submission guidelines (older text) |
|---|---|---|
| Coordinator | senior PC member | area chair |
| COI co-authorship | 2023-present; 4+ papers 2016-present; any submission under review | past 3 years; 4+ in last 10 years; paper or grant proposal in submission |
| Registration | ≥1 full author registration, one per paper; Xplore removal if not met | unique full registration; "presentation at the conference is not required" |
| 1-year rule | "including revisions"; "since the rejection" | "from the time of their last submission" |
| Negative-space sentence | present | absent |
| Page-limit exclusion name | "AI-generated content declaration" | "AI-generated content acknowledgement" |
Safe reading: follow the stricter of the two in every row (declare COIs under both definitions; plan for a registered author who presents). [INF]

### 1.15 Inclusion and diversity in writing [V] (CFP)
- Avoid language or examples that marginalize or stereotype. "Reviewers will be empowered to monitor and demand changes if such issues arise."

### 1.16 Camera-ready and IEEE publication rules
- ICDE [V] (CFP, camera-ready section):
  - Use IEEE CPS, not CMT, for the paper and the copyright form: https://ieeecps.org/cps/v2/auth/login?ak=1&pid=2drDUt2CWjOK5NK2Pr75y. The CPS kit contains the PDF eXpress validation instructions.
  - 12-page limit; EAB tag removed; the AI acknowledgment is mandatory; title, abstract, authors and CMT metadata cannot change.
  - Formatting failure means "exclusion of the paper from the proceedings and the conference".
  - Proceedings chairs: Chao Zhang (RUC) and Wei Shen (Nankai).
  - Due 2027-03-10.
- IEEE copyright [V] https://conferences.ieeeauthorcenter.ieee.org/get-published/about-transferring-copyright-to-ieee/ : "You will receive a link to the eCF after your paper is accepted". Signing transfers copyright to IEEE. For mixed government/non-government authorship, a non-government author signs.
- Posting [V] (IEEE submission policies page): authors may post the accepted (submitted) version, not the final IEEE version, with the IEEE notice "© 20xx IEEE. Personal use of this material is permitted…".
- PDF eXpress [V that the service exists, login at https://ieee-pdf-express.org/ ; conference ID supplied by CPS, UNVERIFIED]. Typical Xplore requirements [2nd; older IEEE PDF specs]: all fonts embedded and subset (no Type 3 bitmap fonts), PDF 1.4 or later, no security, US Letter page boxes.
  - Sources: https://scg.unibe.ch/wiki/howtos/howtomakeyourcamerareadypdfpassthroughthepdfcheck ; https://2014.ieeeicassp.org/PaperFormat/Author-PDF-Guide-V32.pdf
  - The current IEEE PDF specification page could not be fetched (the Author Center URL returned 404). [UNVERIFIED]

### 1.17 Other facts useful for planning [V]
- Round 1 accepted list: 127 papers, 4 of them EAB (the listing still shows the tag). The page heading has a typo, "Accepted Research Papers for ICDE 2026". The acceptance rate is not published. https://icde2027.github.io/accepted-papers.html
- Other tracks (important-dates): DEFT due 2026-11-22; Industry and Applications due 2026-12-01; Demos due 2026-11-23; PhD Symposium due 2026-11-11.

---

## 2. How ICDE reviewers evaluate papers: public evidence

- **No ICDE review form, reviewer guideline, PC-chair blog or CMT review-question list is public** for any edition from 2023 to 2027.
  - I searched the ICDE 2023-2027 sites, and the web in general, for "review form", "reviewer guidelines", "meta-review" and "overall rating". [V that none was found]
  - Every scoring dimension in the `review-icde` form is a simulation, not ICDE's form. [UNVERIFIED for any specific field]
- What the official pages do say about evaluation [V]:
  1. At least three reviewers, plus a meta-review by the senior PC member (2027), the area chair (2026) or the meta-reviewer (2023-2025), "based on the discussions about the paper".
  2. Supplemental material "availability … will be considered in the evaluation".
  3. Relevance and positioning against ICDE/VLDB/SIGMOD work, assessed through the related-work section.
  4. EAB criterion: "fundamentally new insight into the strengths and weaknesses of existing methods, or new ways to evaluate existing methods".
  5. Inclusive-writing checks by reviewers.
  6. Earlier editions told reviewers to "request revisions with specific requests" (2023, 2024); this no longer applies in 2027.
- Meta-review content: only "based on the discussions about the paper" is stated. CMT notes that meta-reviews may be hidden from authors during author feedback. [V] Any further structure is [UNVERIFIED].
- Rebuttal format and length: not published (§1.12). [UNVERIFIED]
- Closest public proxy, PVLDB (heavy PC overlap with ICDE; a proxy only, not ICDE rules) [V] https://vldb.org/pvldb/volumes/19/submission :
  - The scope policy has three criteria: Core Data Management Focus; Connection to the Database Research Literature; Evaluation in Data Management Contexts.
  - Reviewers consider the supplemental material, and "We ran out of time" is not an acceptable excuse for missing material.
  - EA&B papers whose authors are not committed to reproducibility are rejected.
  - Undeclared or spurious conflicts are desk-rejected.
- IEEE reviewer-side AI rule: reviewers must not upload manuscripts to public AI platforms. [2nd] https://rams.org/?p=2833 . This is relevant only as context; it does not constrain authors.

---

## 3. Gaps in the existing skills

### 3.1 `submit-icde` (SKILL.md, assets, scripts/check_icde_submission.py)
Correct as far as it goes: dates; 12 pages without appendix; single-blind; ORCID; CMT profile; quota of 5 per round; EAB tag and artifacts; supplemental URL; scope statement with 1000 characters and (a)/(b)/(c); AI disclosure content.

Missing or outdated:
1. **Deadline in Beijing time** (Round 2, PST): 2026-11-12 09:00, not 08:00. The skill gives no local time; the earlier report has it wrong. Add a computed conversion to the checklist.
2. **COI rule details.**
   - Add "co-author of any submission under review" and "collaborators 2023-present".
   - Co-worker COIs go in Domain Conflicts.
   - COIs are against PC **and senior PC** members, and correctness is judged "as of the submission closing time".
   - Note that the submission-guidelines page uses the older "3 years / 10 years" definition; declare under both.
3. **CMT order of operations.** Individual conflicts become visible only after a paper is submitted. Domain format is `a.edu; b.com` with no gmail. Every co-author must log in and attest before the deadline.
4. **Funding or other acknowledgments count toward the 12 pages.** Only references and the AI declaration are excluded. No reference-page cap exists (the 2023/2024 "+4 pages" cap is gone).
5. **Checker page-count logic.**
   - It counts pages up to the "REFERENCES" heading, so an AI acknowledgment placed before the references and spilling onto page 13 is wrongly counted as body.
   - References starting at the top of page 13 give a false ERROR.
   - The `^\s*REFERENCES\s*$` regex may miss IEEEtran's small-caps heading after text extraction ("R EFERENCES"), in which case all pages are counted. [risk; not tested]
   - Fix: find the first page of the AI/Acknowledgment or References heading, test whether body text continues past page 12, and report the reference page count separately.
6. **Checker misses other format violations.**
   - `\linespread`, `\baselinestretch`, `\enlargethispage`, negative `\abovecaptionskip`/`\belowcaptionskip`/`\textfloatsep`, `\titlespacing`, `\addtolength` on geometry, and leftover IEEE template red text ("Ensure that all template text is removed").
   - Math or footnotes in the title or abstract (IEEE Xplore rule).
   - Fonts: run `pdffonts` and reject Type 3 or non-embedded fonts (needed for PDF eXpress later).
7. **Re-submission rules.**
   - The 1-year wait covers "revisions of such papers".
   - Round 1 desk rejects for COI or format **may** go to Round 2; out-of-scope rejects may not.
   - Novelty uses the 4-double-column-page threshold, and overlapping short papers must still be cited.
   - No concurrent submission anywhere until about 2027-02-10.
8. **Metadata freeze.** The title, abstract and author list entered in CMT cannot change at camera-ready. Finalise the author list and make the CMT abstract identical to the PDF abstract at submission.
9. **Rebuttal (new in 2027).** The skill only says "a rebuttal period exists". Add:
   - Window: 2027-01-08 to 01-15, 17:00 PST, 09:00 Beijing on 01-16.
   - CMT "Post Author Feedback" mechanics; a file upload only if the chair allows it; meta-reviews may be hidden.
   - Rebuttal is the only lever because there is no revision.
   - Length limit is unknown; check CMT when the window opens.
   - A rebuttal template asset is missing.
10. **Camera-ready section absent.**
    - IEEE CPS link (not CMT), PDF eXpress validation, eCF copyright after acceptance.
    - Remove the EAB tag; the AI acknowledgment is mandatory; 12 pages.
    - A unique full registration per paper, plus a presenting author (CFP and submission guidelines differ; plan for both).
    - Due 2027-03-10.
11. **AI disclosure details.**
    - Recommend the ICDE 2026 heading "AI-Generated Content Acknowledgement", placed just before the references.
    - Add the IEEE line that grammar-editing disclosure is "recommended" and that AI editing should exclude the reference section.
    - Treat the section as mandatory even when only editing was done; write an explicit statement.
    - The checker's ERROR when no AI keyword appears is consistent with this; keep it.
12. **Unverified items to flag in the skill.** ORCID location; subject-area list; whether CMT takes a supplementary upload; rebuttal length. These are all behind CMT login.
13. **Inclusive-writing clause** (reviewers may demand changes) is not mentioned.
14. The scope-template asset should quote the CFP's sharpened sentence that positioning is "typically done … as part of its coverage of related work".
15. Minor: the quota line should say "per round (Round 1 papers do not count toward Round 2)" [INF from the "per submission round" wording]. The source line "read 2026-11-03" should be updated with the 2026-10-28 commit reference.

### 3.2 `review-icde` (SKILL.md, assets/review_form.md, assets/desk_screen.md, references/reviewer-lens.md)
Correct: three or more reviewers plus a meta-review, Accept/Reject only, scope lens, artifact weight, independence protocol.

Missing or outdated:
1. **Provenance disclaimer.** ICDE publishes no review form. The six score dimensions and the five-level overall scale are a simulation and should be labelled as such. Map them to the only official criteria: relevance and positioning, supplemental availability, EAB insight criterion, inclusive writing. Optionally add the PVLDB three-criterion scope test, marked as a proxy.
2. **Desk screen is incomplete** (`assets/desk_screen.md` has 9 rows). Add:
   - Funding or other acknowledgments counted in the 12 pages; no supplementary section inside the PDF; template text removed.
   - No math in the title or abstract.
   - Stricter COI definition (any submission under review; senior PC); frivolous COIs.
   - Novelty: the 4-page prior-publication threshold and citation of overlapping work. Not under review elsewhere. 1-year rule including revised versions.
   - Supplemental explanation in the form if there are no artifacts.
   - Scope statement present when the paper is borderline.
   - Inclusive language.
   - AI acknowledgment present even when use was minimal.
3. **Meta-reviewer role naming.** Use "senior PC member" (CFP) and note that the submission guidelines say "area chair". The meta-review is "based on the discussions"; add a simulated discussion step (reviewers read each other's reports, then the meta-review).
4. **Rebuttal simulation** (the biggest gap, since 2027 replaces revision with rebuttal):
   - Generate the rebuttal-targeted questions per reviewer.
   - Draft a rebuttal under an assumed length cap (mark the cap as an assumption until CMT shows the real one).
   - Then have each reviewer re-score after reading it, and have the meta-reviewer decide.
   - Rebuttals cannot change the paper (no revision). Weaknesses that need new experiments are fatal unless answered with numbers already in the paper or artifact. [INF]
   - Add `assets/rebuttal_template.md`.
5. **EAB-specific review questions** ("fundamentally new insight / new ways to evaluate", all artifacts, no exceptions) are absent from the form.
6. **Reproducibility row.** "Availability considered in the evaluation" should be its own explicit check: is the URL public, neutral and non-tracking, and does it contain run instructions?
7. **Remove the revision framing.** The final step "revision table" is fine as an internal pre-submission tool, but the skill should state that ICDE 2027 offers no revision after submission. Earlier editions (2023-2026) used Revise, so reviewer habits of asking for revisions may persist, but the outcome can only be accept or reject. [V for the editions; INF for habits]
8. `reviewer-lens.md` is built from 21 accepted papers only, mostly LLM, ANN and graph topics. It cannot show rejection causes. Label it "survivor evidence".

---

## 4. Not verified (consolidated)
- The ICDE CMT submission form: ORCID field, subject areas, scope field label, supplementary upload, author-response length or format.
- The contents of the IEEE templates page (bot-protected) and of the icbc2025 AI-guideline page (TLS failure).
- The current IEEE PDF eXpress specification and the ICDE 2027 conference ID.
- The ICDE review form, rating scale, meta-review template, and any PC-chair guidance for 2023-2027 (none public).
- Acceptance rates for ICDE 2027 Round 1.
