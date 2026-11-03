---
name: "submit-icde"
description: "Pre-submission checklist and checker for the IEEE International Conference on Data Engineering (ICDE, CCF A) research track, built from the ICDE 2027 call for research papers (read 2026-11-03): two rounds, 12-page IEEE limit without appendix, single-blind, CMT conflicts, AI-content disclosure, artifacts, scope/desk-reject rules, EAB category. Use when preparing, formatting or packaging a paper for ICDE (投 ICDE / ICDE 投稿 / 投稿前检查), or when deciding Round 1 vs Round 2. Includes a LaTeX/PDF checker."
---

# Submitting to ICDE (投稿 ICDE 前须知)

Source: ICDE 2027 CFP https://icde2027.github.io/cf-research-papers.html and submission-guidelines.html, read on 2026-11-03. Tags: [CFP] = stated in the call; [OBS] = observed in published ICDE papers; [CHECK] = re-verify for a later edition (rules change each year).

Use with `write-icde` (how accepted papers are built) and `review-icde` (simulated PC review).

## Language convention
Manuscript, CMT form text and rebuttal in **English**; plans and reports to the author in **Chinese (中文)**.

## 1. Dates and rounds [CFP]
ICDE 2027: Round 1 due 2026-06-11, Round 2 due 2026-11-11, 5:00 PM Pacific Time; rebuttal Aug 8-15 / Jan 8-15; notification Sep 10 / Feb 10; camera-ready Oct 10 / Mar 10. CMT opens one week before each deadline.
- Outcome is Accept or Reject only; there is no revision. A rebuttal period exists.
- A paper rejected in Round 1 cannot go to Round 2; a rejection blocks ICDE for one year. Pick the round you can be ready for, and do not submit a draft. [CHECK] dates for later editions.

## 2. Hard rules (desk reject if violated) [CFP]
| Item | Rule |
|---|---|
| Template | IEEE conference template (IEEEtran `conference`); no negative spaces or content in margins |
| Length | at most 12 pages, excluding references and the AI-content acknowledgment; **no appendix** |
| Review | **single-blind**: names and affiliations on the paper |
| ORCID | required for all authors at submission |
| CMT | every author needs a CMT profile with domain and individual conflicts; one missing profile = desk reject |
| COI | co-authors since 2023 (or 4+ papers since 2016), same institution since 2023, collaborators, advisor/advisee ever, relatives/friends. Missing or frivolous COIs = desk reject |
| Quota | at most 5 research-track submissions (regular + EAB) per author per round |
| Overlap | not under review elsewhere; cite any prior publication it overlaps with |
| Scope | must fit a CFP topic and position itself against ICDE/VLDB/SIGMOD work; pure ML/DM without a data-engineering angle is out of scope |
| EAB | title begins with `[Experiment, Analysis, and Benchmark]` (removed at camera-ready); all artifacts mandatory |

## 3. Things that are scored but not desk-reject [CFP]
- **Supplemental material** (code, data) via a public URL such as a public GitHub repository; availability is considered in evaluation. If you cannot share, explain in the submission form. No personal web pages that could track reviewers.
- **AI-generated content disclosure** in the acknowledgments: name the system, the sections, and the level of use, including LLMs used to run experiments or process data. Grammar editing alone need not be disclosed. The acknowledgment does not count toward the 12 pages. [OBS] All three ICDE 2026 papers we checked carry an "AI-Generated Content Acknowledgement".
- **Scope statement** (optional form field, at most 1000 characters) when the paper might look out of scope: (a) the data-engineering challenge, (b) the principled contributions with section numbers, (c) the ICDE/VLDB/SIGMOD papers it builds on. "A similar paper appeared at ICDE before" is not accepted as a reason.
- At least three reviewers plus a senior PC meta-review.

## 4. Workflow
1. Decide category (regular or EAB) and round; check the author quota and the one-year rule.
2. Build with IEEEtran; keep the body within 12 pages; move proofs or extra results to a public technical report, not an appendix.
3. Write the AI disclosure as an unnumbered acknowledgment before the references (template in `assets/ai_disclosure_template.tex`).
4. Prepare the artifact repository; make it public before the deadline; cite its URL in the paper.
5. Run the checker: `python3 scripts/check_icde_submission.py paper/ --pdf paper/main.pdf [--eab] [--scope scope.txt]`.
6. Every author: ORCID, CMT profile, conflicts. The corresponding author fills the subject areas and, if needed, the scope statement (`assets/scope_statement_template.md`).
7. Submit the PDF and the supplemental link on CMT before 5:00 PM PT; keep the CMT confirmation.

## 5. Checker
`scripts/check_icde_submission.py` inlines `\input` files and checks: IEEEtran conference class; no negative `\vspace`, geometry changes or appendix; author block filled; EAB title tag; AI disclosure in the acknowledgments; abstract length and no citations; citation keys resolved in the `.bib`; number of VLDB/SIGMOD/ICDE references; leftover TODO or placeholder macros; artifact link; scope text length; and, if a PDF exists, page count before the references and US Letter size. It reads files only.

## 6. Final checklist
- [ ] Round and category chosen; quota and one-year rule checked.
- [ ] IEEEtran, at most 12 body pages, no appendix, no negative spacing.
- [ ] Authors and affiliations shown (single-blind); ORCIDs collected.
- [ ] AI disclosure acknowledgment written.
- [ ] Related work positions the paper against ICDE/VLDB/SIGMOD papers.
- [ ] Public artifact repository with code, data and run instructions.
- [ ] CMT profiles and conflicts for every author.
- [ ] Checker passes with no ERROR.
