---
name: "submit-icde"
description: "Pre-submission checklist and checker for the IEEE International Conference on Data Engineering (ICDE, CCF A) research track, built from the ICDE 2027 call for research papers (read 2026-11-03): two rounds, 12-page IEEE limit without appendix, single-blind, CMT conflicts, AI-content disclosure, artifacts, scope/desk-reject rules, EAB category. Use when preparing, formatting or packaging a paper for ICDE (投 ICDE / ICDE 投稿 / 投稿前检查), or when deciding Round 1 vs Round 2. Includes a LaTeX/PDF checker."
---

# Submitting to ICDE (投稿 ICDE 前须知)

Source: ICDE 2027 CFP https://icde2027.github.io/cf-research-papers.html and submission-guidelines.html, read on 2026-11-03 and re-checked on 2026-11-06 (no change; site last updated 2026-10-28). Microsoft CMT documentation for conflicts and author feedback; IEEE Author Center for copyright and posting. Tags: [CFP] = stated in the call; [OBS] = observed in published ICDE papers; [CHECK] = re-verify for a later edition (rules change each year).

Use with `write-icde` (how accepted papers are built) and `review-icde` (simulated PC review).

## Language convention
Manuscript, CMT form text and rebuttal in **English**; plans and reports to the author in **Chinese (中文)**.

## 1. Dates and rounds [CFP]
ICDE 2027: Round 1 due 2026-06-11, Round 2 due 2026-11-11, 5:00 PM Pacific Time (PST in November = **2026-11-12 09:00 Beijing**); rebuttal Aug 8-15 / Jan 8-15; notification Sep 10 / Feb 10; camera-ready Oct 10 / Mar 10. CMT opens one week before each deadline.
- Outcome is Accept or Reject only; there is no revision. A rebuttal period exists.
- A paper rejected in Round 1 cannot go to Round 2. A rejection blocks ICDE for one year, and this includes revised versions of the paper. Round 1 desk rejects for COI or format may come back in Round 2; out-of-scope rejects may not.
- After submitting, do not submit the paper anywhere else until the decision (about 2027-02-10). Pick the round you can be ready for, and do not submit a draft. [CHECK] dates for later editions.

## 2. Hard rules (desk reject if violated) [CFP]
| Item | Rule |
|---|---|
| Template | IEEE conference template (IEEEtran `conference`); no negative spaces or content in margins |
| Length | at most 12 pages, excluding **only** the references and the AI-content acknowledgment. Funding and other acknowledgments count toward the 12. **No appendix** and no supplementary section inside the PDF. There is no cap on reference pages. |
| Review | **single-blind**: names and affiliations on the paper |
| ORCID | required for all authors at submission |
| CMT | every author needs a CMT profile with domain and individual conflicts; one missing profile = desk reject |
| COI | Conflicts are declared against PC **and senior PC** members. A conflict exists for: co-authors of any submission under review; co-authors of a paper since 2023; co-authors of 4+ papers since 2016; same institution since 2023 (declare as Domain Conflicts); collaborators since 2023; thesis advisor ever; relatives and close friends. The older submission-guidelines page uses a 3-year/10-year wording, so declare under both. Declarations are checked by software as of the deadline; missing or frivolous COIs mean desk reject. |
| Quota | at most 5 research-track submissions (regular + EAB) per author per round |
| Overlap | not under review elsewhere; cite any prior publication it overlaps with |
| Scope | must fit a CFP topic and position itself against ICDE/VLDB/SIGMOD work; pure ML/DM without a data-engineering angle is out of scope |
| EAB | title begins with `[Experiment, Analysis, and Benchmark]` (removed at camera-ready); all artifacts mandatory |

## 2a. CMT order of operations [CMT docs, CFP]
1. Every author creates a CMT profile, adds ORCID, and enters **Domain Conflicts** as semicolon-separated
   domains (`zju.edu.cn; loctek.com`). Do not enter institution names or public mail domains such as
   gmail.com.
2. The corresponding author creates the paper record early. **Individual Conflicts become visible only
   after a paper has been submitted**, so every author must log in again and mark individual conflicts
   before the deadline.
3. The title, abstract and author list entered in CMT are **frozen at camera-ready**. Make the CMT
   abstract identical to the PDF abstract, and finalise the author list now.
4. Upload the PDF. Fill the subject areas, the supplemental URL and, if needed, the scope statement.
   Keep the confirmation e-mail.
5. Not verifiable without logging in to CMT: where the ORCID field is, the subject-area list, whether a
   supplementary upload exists, and the rebuttal length. Check them in the form.

## 2b. Official pages disagree (follow the stricter reading)
The CFP was updated on 2026-10-28; the submission-guidelines page still has older text. They differ on:
- who coordinates reviewing: senior PC member vs. area chair;
- the COI periods;
- registration (one full registration per paper, plus a presenting author);
- the wording of the one-year rule.
Plan for the stricter version in every case.

## 3. Things that are scored but not desk-reject [CFP]
- **Supplemental material** (code, data) via a public URL such as a public GitHub repository; availability is considered in evaluation. If you cannot share, explain in the submission form. No personal web pages that could track reviewers.
- **AI-generated content disclosure** in the acknowledgments: name the system, the sections, and the level of use, including LLMs used to run experiments or process data. Grammar editing alone need not be disclosed. The acknowledgment does not count toward the 12 pages. [OBS] All three ICDE 2026 papers we checked carry an "AI-Generated Content Acknowledgement".
- **Scope statement** (optional form field, at most 1000 characters) when the paper might look out of scope: (a) the data-engineering challenge, (b) the principled contributions with section numbers, (c) the ICDE/VLDB/SIGMOD papers it builds on. "A similar paper appeared at ICDE before" is not accepted as a reason.
- At least three reviewers plus a senior PC meta-review.
- Inclusive writing: reviewers may demand changes to language or examples that marginalise or
  stereotype.
- AI disclosure details:
  - use the heading "AI-Generated Content Acknowledgement" placed just before the references;
  - write it even if use was minimal; IEEE recommends disclosing grammar editing;
  - it is mandatory at camera-ready.

## 3a. Rebuttal (new in ICDE 2027; 2023–2026 used revisions)
- Window: 2027-01-08 to 01-15, 17:00 PST (01-16 09:00 Beijing). The outcome is accept or reject; there
  is no revision.
- Use CMT "Post Author Feedback", which offers text fields defined by the chair. A file upload is
  possible only if the chair allows it, and meta-reviews may be hidden. Click Submit, or nothing is
  saved.
- ICDE publishes no length limit or format; check CMT when the window opens.
- The rebuttal cannot change the paper. Answer with numbers that are already in the paper or the public
  artifact. Template: `assets/rebuttal_template.md`.

## 3b. Camera-ready (if accepted; due 2027-03-10)
- Upload the paper and the copyright form through **IEEE CPS**, not CMT. The CPS kit contains the IEEE
  PDF eXpress instructions: all fonts embedded, no Type 3 fonts, no security, US Letter.
- Sign the IEEE eCF copyright form after acceptance.
- Keep the 12-page limit, remove the EAB tag, keep the AI acknowledgment.
- The title, abstract and authors must not change.
- One unique full registration per paper, plus a presenting author.
- Posting: you may post the accepted, not the IEEE-final, version, with the IEEE copyright notice.

## 4. Workflow
1. Decide category (regular or EAB) and round; check the author quota and the one-year rule.
2. Build with IEEEtran; keep the body within 12 pages; move proofs or extra results to a public technical report, not an appendix.
3. Write the AI disclosure as an unnumbered acknowledgment before the references (template in `assets/ai_disclosure_template.tex`).
4. Prepare the artifact repository; make it public before the deadline; cite its URL in the paper.
5. Compile and run the layout gate `manuscript-writing-review`: 0 layout errors, every page seen. If the
   paper lives in an Overleaf project with git access, push through its git bridge, then compare the
   Overleaf PDF with the local one.
6. Run the checker: `python3 scripts/check_icde_submission.py paper/ --pdf paper/main.pdf [--eab] [--scope scope.txt]`.
7. Every author: ORCID, CMT profile, conflicts (section 2a). The corresponding author fills the subject areas and, if needed, the scope statement (`assets/scope_statement_template.md`).
8. Submit the PDF and the supplemental link on CMT before 5:00 PM PT; keep the CMT confirmation.

## 5. Checker
`scripts/check_icde_submission.py` inlines `\input` files and checks:
- spacing hacks: `\linespread`, `\enlargethispage`, negative float or caption skips, `\titlespacing`;
- math or footnotes in the title or abstract;
- leftover IEEE template text;
- fonts, with PyMuPDF: embedded, no Type 3;
- the body end, which it finds at the AI acknowledgment or the References heading (including
  IEEEtran's "R EFERENCES" extraction).

It also checks: IEEEtran conference class; no negative `\vspace`, geometry changes or appendix; author block filled; EAB title tag; AI disclosure in the acknowledgments; abstract length and no citations; citation keys resolved in the `.bib`; number of VLDB/SIGMOD/ICDE references; leftover TODO or placeholder macros; artifact link; scope text length; and, if a PDF exists, page count before the references and US Letter size. It reads files only.

## 6. Final checklist
- [ ] Round and category chosen; quota and one-year rule checked.
- [ ] IEEEtran, at most 12 body pages, no appendix, no negative spacing.
- [ ] Authors and affiliations shown (single-blind); ORCIDs collected.
- [ ] AI disclosure acknowledgment written.
- [ ] Related work positions the paper against ICDE/VLDB/SIGMOD papers.
- [ ] Public artifact repository with code, data and run instructions.
- [ ] CMT profiles and conflicts for every author.
- [ ] Checker passes with no ERROR; `manuscript-writing-review` shows 0 layout errors.
- [ ] CMT abstract identical to the PDF abstract; author list final (frozen at camera-ready).
- [ ] Every author marked individual conflicts after the paper record was created.
- [ ] Deadline in local time noted (Round 2: 2026-11-12 09:00 Beijing).
