---
name: "icde-cmt-submission"
description: "Prepare everything the ICDE CMT 'Create New Submission' page asks for, from the paper itself, and check it before the author presses Submit: title, plain-text abstract (CMT limit 2,000 characters, rebuilt from LaTeX with macros expanded and compared word for word with the PDF), authors table (email, first/last name, organization, country, primary contact, ORCID), subject areas (via icde-subject-areas), the single PDF (<= 20 MB), Toronto Paper Matching consent, and the ten additional questions of the ICDE 2027 research track, including the Relevance text (<= 1,000 characters, (a)(b)(c)) and the Availability text (artifact URL plus the reason for anything withheld). Field list taken from the ICDE 2027 Research Second Round form on 2026-11-11. Use whenever a paper is submitted to ICDE through CMT (投 ICDE / ICDE 投稿 / CMT 投稿 / 投稿窗口 / 投稿表单 / 准备投稿材料 / Create New Submission)."
---

# Filling the ICDE CMT submission form (投稿窗口材料)

Use with `submit-icde` (rules and checks of the call), `icde-subject-areas` (Primary/Secondary areas) and
`manuscript-writing-review` / `manuscript-proofcheck` (the PDF itself). This skill turns the final paper into the exact
text and ticks the CMT page needs, and checks that every pasted field matches the uploaded PDF.

## Language convention
All text pasted into CMT is reviewer-facing: formal academic English, copied from the generated file, never retyped.
The walkthrough for the author (which box, which tick, what only the author can do) is in Chinese (中文), as a
document.

## 1. The form (ICDE 2027, track "ICDE 2027 Research Second Round", seen 2026-11-11)
| Section | Field | What to enter | Limit / rule |
|---|---|---|---|
| Title and abstract | Title* | paper title, identical to the PDF | |
| | Abstract* | plain text of the PDF abstract (no LaTeX; × and – as Unicode) | 2,000 characters (CMT counter) |
| Authors* | one row per author, in PDF order | Email, First Name, Last Name, Organization (one text field; join two affiliations with a comma), Country/Region; "Primary Contact" radio for one author; reorder with the arrows | every author needs a CMT account with the same e-mail; ORCID is entered in each author's CMT profile and is required at submission |
| Subject Areas* | one Primary, 2-3 Secondary | see `icde-subject-areas` | "None Of Above" only if nothing fits |
| Files | exactly one file | the final PDF | 1 file, <= 20 MB, doc/docx/pdf |
| Toronto Paper Matching System* | consent | tick "I agree" | |
| Additional questions | 1 Desk Rejection Policy* | tick "I agree" | read the policy: format, COI, scope, re-submission |
| | 2 Maximum number of submissions per author* | tick "I agree" | at most 5 papers per author per round |
| | 3 Relevance (text box) | see section 2a: Topics line, (a) challenge, (b) contributions with section numbers, (c) ICDE/VLDB/SIGMOD work it builds on and how it extends it | CFP: 1,000 characters (box shows "8000 characters left"); recommended for every paper, required if scope could be questioned |
| | 4 Duplicate Submissions* | tick "I agree" | no parallel submission until the decision |
| | 5 Conflicts of Interest* | tick "I agree" | only after every author has entered domain and individual conflicts in the CMT profile (name, top right) |
| | 6 Integrity of the review process* | tick "I agree" | no contact with PC/SPC about the paper |
| | 7 Authorship* | tick "I agree" | author list frozen after acceptance |
| | 8 Availability* (text box) | public artifact URL (e.g. GitHub), then one paragraph on what is in it and why anything is withheld | no personal web pages; EAB papers must release everything |
| | 9 Registration for accepted papers* | tick "I agree" | one full registration per accepted paper |
| | 10 Presentation for accepted papers* | tick "I agree" | an author must present in person |
[CHECK] the form for later editions: CMT pages change every year; refresh this table from a screenshot.

## 2a. Writing the Relevance text (what the form itself asks, ICDE 2027 R2)
The form says a submission must align with at least one ICDE topic area and position itself in the state of the art
of the data-engineering community; authors explain in 1,000 characters (a) the key data-engineering challenge(s),
(b) principled ideas and contributions, with reference to specific sections, and (c) research published in ICDE or
other core outlets such as VLDB and SIGMOD that it builds on. Its examples favour "We propose X ... in Section Z we
..." and "builds substantially on the following papers in ICDE, SIGMOD and VLDB"; "a similar problem was once
published at ICDE" is called insufficient. Hence:
1. First line `Topics:` with the chosen CMT subject areas (same names as the ticked boxes).
2. (a) the challenge in data-engineering terms (what breaks in a data system, under which budget or update regime).
3. (b) "We formalize/prove/give/evaluate ... (Sec. II/III/IV/V)", using the section numbers of the final PDF.
4. (c) only papers that are in the bibliography and appeared in ICDE, PVLDB/VLDB Journal, SIGMOD/PODS or TODS, cited as
   NAME, VENUE'YY, and one clause on how the paper extends them ("from profiling all data to certifying what queries
   need"). Workshop, CIDR, SSDBM, arXiv or ML-venue papers do not count for (c) even if they are the closest work.
5. At most 1,000 characters, counting line breaks (aim for <= 995 in case CMT counts a break as two).
6. Unicode for symbols (ε, δ, ×, –), no LaTeX.
`prepare_cmt.py` checks 1-6 (topic named, (a)(b)(c), sections exist in the PDF, core venues only, each venue/year in
the .bib, an "extends/builds on" clause, length).

## 2. Workflow
1. Make sure the PDF is final: same as the last compiled version and as Overleaf, all gates of `submit-icde` and
   `manuscript-writing-review` clean, body <= 12 pages.
2. Choose the subject areas with `icde-subject-areas` and record them.
3. Write `authors.json` (author order, e-mail, first/last name, organization, country, ORCID, primary contact) and the
   relevance text (<= 1,000 characters, (a)(b)(c), section numbers of the final PDF).
4. Run
   `python3 scripts/prepare_cmt.py <paper_dir> --pdf <final.pdf> --artifact-url <url> --authors authors.json --relevance relevance.txt --withheld "<what is not released and why>" --areas "<Primary>; <Secondary 1>; <Secondary 2>" --out cmt_form_EN.md`
   It writes every field and a check list; it exits non-zero if any check fails (title or abstract differ from the
   PDF, abstract > 2,000 characters, PDF > 20 MB or not US Letter, Type 3 fonts, body > 12 pages, no AI declaration,
   relevance text too long or missing (a)/(b)/(c), artifact URL not reachable without login).
5. Give the author a Chinese walkthrough: for each CMT section, what to paste (from `cmt_form_EN.md`) and what to tick,
   then the author-only items of section 3. When the author sends screenshots, compare every filled field with the
   file (title, abstract end, author rows, uploaded file name, size and time, ticks) before Submit.
6. After Submit, read the Submission Summary page (the author's screenshot) row by row: title, abstract end, author
   rows, areas, file name/size/time, every question "Agreement accepted", both text boxes. Check the column
   **"Individual Conflicts / Attested?"**: every author must show "Yes" (a co-author who never attested shows
   "(0) No" even with zero conflicts; this is a desk-reject risk until the deadline). In the Availability box put the
   URL alone on the first line: "https://…/repo. The repository …" makes the trailing period part of the link.
   Then: the author keeps the CMT confirmation e-mail; record submission ID, PDF hash and Overleaf/artifact
   commits in the project notes. Do not change the artifact repository after the deadline except to fix a broken
   link.

## 3. Only the author can do these (desk-reject risks)
- Every author has a CMT account with the e-mail used in the author row, a complete profile with ORCID, and domain
  plus individual conflicts entered before the deadline ("If a CMT profile is missing even for one author of a
  submission, the paper will be desk rejected"). The COI helper https://opencoi.greatji.com/icde2027 is advisory only.
- Log in to CMT and press Submit; never type or store credentials for the author.
- Count the papers per author in the round (<= 5).

## 4. Pitfalls seen
- Pasting the LaTeX abstract (macros, `\xx`, `{,}`) instead of the plain text: the generator expands macros and checks
  the result against the PDF. Greek letters and relations (`\epsilon`, `\delta`, `\le`) are now converted to Unicode;
  before 2026-11-11 they leaked into the plain abstract and the check failed with no hint. A failed check now prints
  the differing words.
- Body page count: the heading test once matched any line starting with "references" and reported 5 body pages for
  an 11-page body; it now matches only the whole-line REFERENCES / AI-GENERATED CONTENT ACKNOWLEDGMENT heading.
- Relevance text citing the closest work from CIDR or SSDBM in (c), or listing papers without saying how the
  submission extends them: the form asks for ICDE/VLDB/SIGMOD work the paper builds on.
- Subject areas taken from the scorer's first guess: apply the rules of icde-subject-areas (Certify-Join: the scorer
  first proposed Query processing and Graph data from generic words; the right primary was Data quality).
- Uploading an older PDF with a similar name: compare the file name, size (CMT shows Kb) and upload time with the final
  file.
- Two affiliations: CMT has one Organization field; write both, separated by a comma, as in the PDF.
- Relevance text written for a different version of the paper: section numbers must match the final PDF.
- Availability text that only says "code on GitHub" when enterprise data is withheld: say what is released, what is
  not, and why; keep the headline claims on public data.

## 5. Worked example (AuthZ-Graph, ICDE 2027 R2, 2026-11-11)
All twelve checks passed: title and abstract identical to the PDF (1,787 characters), PDF 0.53 MB, US Letter, no
Type 3 fonts, body 12 pages, AI declaration present, relevance 959 characters with (a)(b)(c), artifact URL public.
Subject areas: Primary Graph data; Secondary Data security and privacy; Storage, indexing, and physical database
design; Query processing and optimization.

## 6. Worked example (Certify-Join, ICDE 2027 R2, 2026-11-11)
Eighteen checks passed: title and abstract identical to the PDF (1,636 characters), PDF 0.46 MB, US Letter, body on
11 pages, AI declaration present, relevance 995 characters (Topics line, (a)(b)(c), Sec. II-V exist, SPIDER ICDE'07,
BINDER PVLDB'15, SWAN ICDE'14, Auto-BI PVLDB'23, SIGMOD'17 all in the .bib, "extends ... from ... to"), artifact URL
public, areas verbatim. The first relevance draft failed three of the new checks (no topic named; CIDR and SSDBM in
(c); no "extends" clause), which is what the author had noticed.

Post-submit check of the same paper (CMT Paper ID 2052): all fields matched, but the second author's "Individual
Conflicts / Attested?" showed "(0) No", and the Availability box had been pasted as "URL. The repository …" on one
line; both were sent back to the author before the deadline.
