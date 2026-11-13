---
name: "submit-pvldb"
description: "Pre-submission checklist for PVLDB Volume 20 / VLDB 2027 (CCF-A journal, monthly cycles). Built from the official Submission Guidelines, Call for Research Track, Formatting Guidelines and Important Dates, read on 2026-11-12 PT: four paper categories and page limits, mandatory abstract on the 25th and full paper on the 1st at 17:00 Pacific Time, monthly cap of two papers per author and yearly cap of twelve for Volume 20, single-blind, CMT PVLDBv20_2027, COI rules (5-year institution and collaboration, advisor forever), Self-Declaration of Related Submissions, Scope Policy and Self-Assessment of Relevance, EA&B reproducibility package required at the initial submission, artifact URL and ACM badge, 12-month resubmission embargo, Light Load Reviewer nomination, desk-reject categories, AI/ACM authorship policy, and camera-ready. Use when preparing, formatting or packaging a paper for PVLDB / VLDB 2027 (投 PVLDB / 投 VLDB / PVLDB 投稿指南 / 十二月周期 / EA&B 投稿 / 作者上限)."
---

# Submitting to PVLDB Volume 20 (投稿 PVLDB 前须知)

**Re-read the official pages before every cycle.** Rules can change between volumes. This skill is a snapshot; official wording wins. Access date: **2026-11-12 (America/Los_Angeles)**.

Primary sources (all official):

- Submission Guidelines: https://www.vldb.org/2027/submission-guidelines.html
- Call for Research Track: https://vldb.org/2027/call-for-research-track.html
- Formatting Guidelines: https://vldb.org/2027/formatting-guidelines.html
- Important dates (monthly cycle): same Guidelines page; conference dates at https://www.vldb.org/2027/
- CMT: https://cmt3.research.microsoft.com/PVLDBv20_2027/
- Official LaTeX template (GitHub): https://github.com/vldbproceedings/VLDB-Template
- Official Overleaf template: https://www.overleaf.com/latex/templates/official-vldb-template/ptsndjkwxkdr (also linked from the Formatting Guidelines)
- Publication policies: https://vldb.org/pvldb/general-information/publication-policies
- Reproducibility: https://vldb.org/pvldb/reproducibility
- ACM artifact badges: https://www.acm.org/publications/policies/artifact-review-and-badging-current
- ACM generative-AI FAQ (authors remain responsible; AI cannot be an author): https://www.acm.org/publications/policies/frequently-asked-questions

Tags: **[CFP]** = stated on an official PVLDB/VLDB 2027 page; **[ACM]** = ACM policy that applies because the template and badges are ACM's; **[CHECK]** = re-verify for a later volume.

Use with `write-pvldb` (how accepted papers are built, including how to state limits) and `review-pvldb` (simulated review, including a self-negation pass). Official venue pages always override advisor notes and this skill.

## Language convention

Manuscript, CMT form text and revision letters in **English**. Plans and reports to the author in **Chinese (中文)**.

## 1. Dates and monthly cycles [CFP]

PVLDB Volume 20 uses **12 monthly cycles** in the year before VLDB 2027 (Athens, 23–27 August 2027).

- **Abstract (mandatory):** 25th of the **previous** month, **17:00 Pacific Time** (Daylight Saving observed on the US calendar). New in Volume 20, effective April 2026.
- **Full paper:** 1st of the month, **17:00 Pacific Time**. These deadlines are strict; no extensions.
- **CMT opens** on the 20th of the previous month for that cycle.
- **First cycle of Volume 20:** 1 April 2026. **Last new-paper deadline for Volume 20:** 1 March 2027.
- **Initial notification:** usually the 15th of the following month: Accept, Reject, or Revision (one revision only; the reviews state what is expected).
- **Revision window:** up to 2.5 months; submit by the 1st in the next three months (0.5 / 1.5 / 2.5 months after the revision notification). Last three revision deadlines: 1 May, 1 June and 1 July 2027. **1 June 2027** is the last revision deadline for presentation at VLDB 2027; later revisions roll to VLDB 2028.
- Papers accepted to Volume 20 **by 1 July 2027** form the VLDB 2027 Research Track (plus rollover from Volume 19). Later accepts roll to VLDB 2028.
- At least one author of each accepted paper must attend VLDB 2027.
- PVLDB is the **only** research-track submission channel for VLDB 2027.

**December 2026 cycle (in use for several of our regular papers):** abstract **2026-11-25 17:00 PT**, full paper **2026-12-01 17:00 PT**.

**January 2027 cycle:** abstract **2026-12-25 17:00 PT**, full paper **2027-01-01 17:00 PT**.

Convert PT to Beijing when talking to the author: 17:00 PT in late November is 09:00 the next calendar day in Beijing (PST, UTC−8).

## 2. Categories, page limits, template [CFP]

| Category | Body page limit | Title suffix (submission only) |
|---|---|---|
| Regular Research | 12 pages excluding references | none |
| Experiment, Analysis & Benchmark (EA&B) | 12 pages excluding references | `[Experiment, Analysis & Benchmark]` |
| Scalable Data Science (SDS) | 8 pages excluding references | `[Scalable Data Science]` |
| Vision | 6 pages excluding references | `[Vision]` |

Hard rules:

- **Everything except the reference list** counts toward the body limit: appendices, acknowledgements, funding, and the AI-generated-content acknowledgment if present. Only references may run past the limit, with no cap on reference pages.
- Use the **official PVLDB ACM-based template** (`acmart` + current `pvldb.sty`). Any deviation, including omitted mandatory blocks (copyright, reference format, artifact/availability), is liable to **desk rejection**.
- US letter, two-column, no margin or spacing hacks, no content in the margins.
- **Single-blind:** author names and affiliations **must** appear on the first page and **must match CMT** (order and middle names).
- Category suffix goes on **both** the PDF title and the CMT title; it is removed in the camera-ready if accepted.
- No citations in the abstract; the CMT abstract must be the same as the PDF abstract.

Regular research has two flavors in the Call (review expectations differ): *Foundations and Algorithms* (formalism or precise pseudocode; a prototype is encouraged) and *Systems* (principled design, prototype, end-to-end empirical evaluation; novelty may be architecture or combination).

## 3. Author caps [CFP] (new yearly cap in Volume 20)

- **Monthly:** at most **two** research-track papers per author (any category).
- **Yearly:** at most **twelve** papers for the entirety of Volume 20 (not a rolling cap across volumes). Effective April 2026.
- Revisions do **not** count toward the cap.
- Enforcement: for a paper with ID = *k*, if any author already has two submissions with ID < *k* in the same month, the paper is desk-rejected. Cap filtering runs **before** COI, scope and format checks.
- Intentional violations: more severe penalties than mere rejection.
- Every author must use a **single CMT account** and **Latin characters** for names and affiliations.
- Authors can inspect their counter by logging into CMT. Submissions not marked Withdrawn count toward the yearly cap.

For our group: coordinate 09, 13, 14, 15 (and any January papers) so that **no author exceeds two papers in the same month**. Companion papers (e.g. 13 and 15) must not go in the same month.

## 4. Conflicts, authorship, related submissions [CFP]

**COI** — each author enters domain and individual conflicts with the Editorial Board (Reviewers, Associate Editors, Editors-in-Chief) in CMT *Personal Conflicts* before the deadline. Undeclared or spurious conflicts: desk reject. Automated COI detection is also used. X and Y conflict if:

- same university or company in the past **5 years**, or an accepted offer within the next 6 months (different campuses of a system do not count, e.g. UC Berkeley vs UC Santa Barbara);
- collaborators in the past 5 years (joint publication, joint project, co-organizing) or currently, including co-authorship not yet published;
- PhD advisor / advisee, **ever**;
- relative or close personal friend.

**Authorship:** after acceptance, the author set **cannot be changed**.

**Self-Declaration of Related Submissions (required):** cite and discuss every related paper by the same authors that is concurrently under review, in press, or otherwise not yet properly published, marked “under submission” in the reference list, and report it on the CMT form. The Review Board assesses incrementality **assuming the earlier submission is accepted**. Failure to disclose, if discovered, is a policy breach. This is **in addition to** citing prior published work. ICDE 2027 companions and sibling PVLDB submissions belong here.

**Originality and duplicates:** a PVLDB paper must be original and not under review elsewhere. Overlap with a prior refereed publication longer than 4 VLDB-style pages is not allowed; shorter prior work must still be cited. **12-month embargo** after a research-track reject (or a withdrawal after a revision decision). The embargo does **not** apply across tracks (Industrial, Demonstrations). Desk rejects for incomplete abstract, unattested COIs, format, or caps do **not** start the embargo.

## 5. Scope, SAR, and desk reject [CFP]

Scope is judged **only** from the manuscript, on three criteria: (1) core data-management challenges (scalability, efficiency, storage, lifecycle, queryability, …); (2) a non-superficial connection to the DB literature (PVLDB, VLDBJ, SIGMOD, ICDE, EDBT, TODS, TKDE, … — “beyond a syntactic citation”, Call for Contributions); (3) evaluation in a data-management context. Adjacent areas (ML/AI, security, theory, hardware) can be in scope **if** these three are met. Keywords or “there was a PVLDB paper on a nearby topic” do not decide scope.

Authors at the boundary should fill the **Self-Assessment of Relevance (SAR)** box: (i) the data-management challenges, (ii) the principled contributions, with section pointers.

A high fraction of citations to non-peer-reviewed work (e.g. only arXiv) is a known desk-reject risk (EiC letter, PVLDB Vol. 18 No. 5). Cite and compare against DB-venue baselines.

Desk-reject notification states only **one** reason even if several apply.

## 6. Artifacts and EA&B [CFP]

- Regular papers: supplemental material (code, data, scripts) should be in a **public archival** repository (e.g. public GitHub; **not** a personal page). Reviewers see it. If it is absent, a **reasonable explanation** is required (copyright, commercialization, not applicable). “We ran out of time” is not acceptable; the paper can be held until availability is fixed. Accepted papers that meet the availability rubric get an ACM badge. Associate Editors assess availability in the meta-review.
- **EA&B (Volume 20, effective April 2026):** the **initial** submission **must** include a link to the **full** reproducibility package (all experiments, data, artifacts, and meaningful instructions). **No excuses.** EA&B papers are also submitted to the PVLDB Reproducibility Committee. This is stricter than Volume 19.

## 7. Light Load Reviewer nomination [CFP]

Every submission must nominate at least one author who is a qualified reviewer (at least two prior research papers in SIGMOD, VLDB, ICDE, EDBT or CIDR). If none qualifies, nominate the best-qualified author. EiCs may appoint a nominated author as a Light Load Reviewer (at most 1 paper/month, up to 3 papers per submitted paper). If the nominee does not provide information in time or fails to submit a non-superficial review, **all co-authors' yearly caps decrease by one**.

## 8. AI policy [ACM] [CHECK]

- Generative AI **cannot be an author**.
- Authors are responsible for every sentence, number and reference, regardless of tool.
- If AI is used **to conduct the research** (design, code, data, experiments, figures that support conclusions), ACM requires a **methods-section** description of that use.
- ACM's current FAQ (checked 2026-11-12) no longer **requires** disclosure of AI used **only** to assist writing, but PVLDB camera-ready or CMT instructions may still ask for an acknowledgment: **follow the official PVLDB wording of the cycle you submit to**, and never invent a policy. If a declaration is included, it counts toward the 12-page body. Do not delete a declaration the venue requires. Do not use the declaration as a place for internal audit language (“no cell was invented”, “no number was changed”).

## 9. CMT steps (author submits; this skill does not submit)

1. Re-open the official Guidelines and record the access date.
2. Check monthly/yearly caps against every co-author's other papers in that month and in Volume 20.
3. All authors: CMT profile, Latin-character names, domain and PC conflicts.
4. Register the abstract by the 25th (title, abstract identical to the PDF, category, subject areas, SAR if needed).
5. Upload the PDF (official template, names on page 1, page limit) and the artifact URL (or explanation; EA&B: full package) by the 1st at 17:00 PT.
6. Self-declare related submissions on the form **and** in the related-work section.
7. Nominate a Light Load Reviewer.
8. The corresponding author who is allowed to submit (for our papers: Dr.Wang) clicks Submit. The assistant does not.

## 10. Integrity (does not override [CFP])

Do not invent numbers, drop measured cells, claim a result on a fold the method was tuned on as a held-out, or silently delete a fact a reviewer needs to judge validity. How to *word* limits is `write-pvldb`; hiding them is not allowed.
