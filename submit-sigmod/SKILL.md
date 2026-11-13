---
name: "submit-sigmod"
description: "Pre-submission checklist for ACM SIGMOD (CCF-A). Snapshot of 2026-11-12 PT covering (1) the SIGMOD 2027 Industrial Track, which is the open industrial deadline for our RateQ paper — 12 pages plus unlimited references, not double-blind, non-academic author required, CMT SIGMODIND2027, deadline 2026-11-24 23:59 AoE — and (2) the SIGMOD 2027 Research Track / PACMMOD process for future research submissions (already closed for 2027): 12-page body, double-anonymous, separate appendix PDF, author feedback and revision. Includes official formatting, duplicate-submission, author-list, AI, and CMT rules. Use when preparing a SIGMOD industrial or research submission (投 SIGMOD / SIGMOD 工业轨道 / SIGMODIND / PACMMOD / 工业稿投稿指南)."
---

# Submitting to SIGMOD (投稿 SIGMOD 前须知)

**Re-read that year's official CFP before submission.** This skill is a snapshot; official wording wins. Access date: **2026-11-12 (America/Los_Angeles)**.

## A. SIGMOD 2027 Industrial Track (open; RateQ's target)

Official sources:

- CFP: https://2027.sigmod.org/calls_industrial_track_papers.shtml
- Important dates: https://2027.sigmod.org/calls_papers_important_dates.shtml
- CMT: https://cmt3.research.microsoft.com/SIGMODIND2027
- ACM Proceedings template: https://www.acm.org/publications/proceedings-template
- Industrial Track PC Chairs: Bailu Ding (Stealth Startup) and Divesh Srivastava (AT&T) — https://2027.sigmod.org/org_industrial_pc.shtml
- ACM generative-AI FAQ: https://www.acm.org/publications/policies/frequently-asked-questions

Use with `write-sigmod` (industrial and research writing, including how to state limits and what is or is not in production) and `review-sigmod`. The older shorter skill `write-sigmod-industrial` is superseded by `write-sigmod` for new work; official CFPs still win.

### 1. What the track wants [CFP]

“Innovative commercial or industrial-strength data management systems (including open source) and solutions.” Also welcome: “novel applications of data management systems and experience in applying recent research advances to problems relevant to the database industry.”

**At least one author must have a non-academic affiliation.** This is a hard eligibility condition, not a style preference.

A thinly disguised research paper with no operational evidence is a poor fit. A product brochure with no generalizable lesson and no precise measurement is also a poor fit. When in doubt, the CFP invites authors to email the industrial chairs.

### 2. Dates [CFP]

All deadlines are **23:59 AoE** (Anywhere on Earth, UTC−12), which is **not** midnight Beijing.

| Event | Date | Beijing time |
|---|---|---|
| Paper submission | Tuesday, 24 November 2026, 23:59 AoE | **25 November 2026, 19:59** |
| Reviews released | Tuesday, 26 January 2027 | — |
| Revision (if invited) | Tuesday, 23 February 2027 | — |
| Notification | Thursday, 4 March 2027 | — |
| Camera-ready | Thursday, 18 March 2027 | — |

Conference: 13–18 June 2027, Huntington Beach, CA, USA.

Reviews may invite a **lightweight shepherding** revision; papers not invited to revise receive their decision with the reviews.

### 3. Format, length, anonymity [CFP]

- **Length:** full papers, **up to 12 pages + unlimited references**. The 12 pages are the body. Do not put essential claims only in a post-limit appendix (the industrial CFP does not offer a review-only appendix).
- **Template:** latest **ACM Proceedings Format**, LaTeX `sample-sigconf.tex` (version 2e) or the Word `Interim layout.docx`. Margins, inter-column spacing and line spacing **must** stay unchanged. The ACM template changed in 2017; use the current version. Violations of length, file type or formatting: **rejected without review**.
- **Not double-anonymous (not double-blind).** Every submission **must include all author names and affiliations**. This is the opposite of the research track.
- **Author list:** changes after the deadline are **not permitted**. Exceptional changes go by email to the industrial chairs, who decide.
- The assistant does **not** submit; the author who is allowed to (for RateQ: Dr.Wang) uploads on CMT.

### 4. Duplicate submissions [CFP]

A paper under review for SIGMOD 2027 Industrial cannot be under review anywhere else, including workshops and journals, and cannot be resubmitted elsewhere until rejected or withdrawn. This covers substantial overlap, not only identical text.

A paper **rejected or withdrawn from the SIGMOD 2027 research track may be submitted to the industrial track of the same conference**, if the other industrial conditions hold (including a non-academic author). The converse is governed by the research-track CFP (12-month embargo rules there); do not assume industrial rejection is free to move to research without reading that CFP.

### 5. AI and integrity [ACM] [CFP]

- AI cannot be an author. Authors are responsible for every number and sentence.
- If AI is used to conduct the research, ACM requires a methods-section description. If a venue-required AI acknowledgment is included, it typically sits after the conclusion and, for a 12-page body, **counts toward those 12 pages** unless the CFP explicitly excludes it — the 2027 industrial CFP does **not** exclude it, so keep the body ≤ 12 pages including that section, with only references after.
- Do not invent production metrics, claim that a system has replaced a live engine when it has not, or drop a losing cell. The industrial track punishes overclaim more than it punishes a modest deployment scope (`write-sigmod`).
- Do not use the AI acknowledgment as an internal-audit paragraph (“no number was changed”).

### 6. CMT packet (author submits)

1. Re-open the CFP; record page limit, template, deadline (AoE → Beijing), and anonymity policy.
2. Confirm a non-academic author and the affiliation line (our frozen decision: keep `Loctek Ergonomic Technology Corp.` on the author line unless the author decides otherwise; body prose does not name the company).
3. Confirm the AI declaration with the authors.
4. 12-page body check on the compiled PDF (conclusion ends on or before page 12).
5. Dr.Wang submits on SIGMODIND2027. The assistant does not.

## B. SIGMOD 2027 Research Track / PACMMOD (for future research submissions)

**Status on 2026-11-12:** the SIGMOD 2027 research track is **closed**. This section is for later SIGMOD/PACMMOD cycles. **[CHECK] every number against that year's CFP.** Do not reuse 2027 dates.

Official source read on 2026-11-12: https://2027.sigmod.org/calls_papers_sigmod_research.shtml

Snapshot of 2027 research rules (do not apply them to an industrial submission):

- CMT: https://cmt3.research.microsoft.com/SIGMOD2027
- **12 pages excluding references**, unlimited references. Camera-ready may be 13 pages excluding references, in PACMMOD format (do **not** use PACMMOD format at initial submission).
- A **separate appendix PDF** is allowed for essential review-only details (e.g. extra proofs). The paper must be self-contained; reviewers are not required to read the appendix. A long appendix of extra results is discouraged and will be ignored. The appendix is **not** part of the camera-ready.
- PDF ≤ 10 MB, US letter, 2-column ACM Proceedings (`sample-sigconf.tex`).
- **Double-anonymous** reviewing (Snodgrass 2007 principles: authors should not go to extreme lengths; review quality trumps perfect anonymization). This is the opposite of the industrial track.
- At least three reviews. **Author feedback** before the decision: (1) a revision plan, (2) clarification of factual errors by pointing at the submitted text. Interactive discussion may follow, initiated by reviewers.
- Decisions: Accept / Reject / Minor Revision / Major Revision. Revisions typically have one month. Reviewers are instructed to request revisions only when the requests are specific and constructive (justify an assumption, add a realistic scenario, compare a relevant system, larger or real data, tighten presentation). Revisions are **not** requested to invent a new problem or to fix a fundamental lack of novelty.

**[CHECK]** later PACMMOD cycles for embargo, COI, artifact and AI wording. The research and industrial tracks have **different** anonymity, appendix, and eligibility rules; never mix them.
