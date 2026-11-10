---
name: "submit-icde"
description: "Pre-submission checklist and checker for the IEEE International Conference on Data Engineering (ICDE, CCF A) research track, built from the ICDE 2027 call for research papers (read 2026-11-03, re-checked 2026-11-06, 2026-11-09 and 2026-11-10): two rounds, 12-page IEEE limit without appendix (only references and AI acknowledgment excluded), single-blind, stricter COI reading and CMT order of operations, AI-content disclosure, artifacts, scope/desk-reject rules, EAB category, rebuttal (new in 2027) and camera-ready (IEEE CPS, PDF eXpress). Includes a dedicated Experiment, Analysis and Benchmark (EAB) guide for Round 2 (references/eab.md): the exact [Experiment, Analysis, and Benchmark] title prefix (not the PVLDB/SIGMOD suffixes), all artifacts mandatory with no exceptions, LLM-experiment disclosure, withheld/enterprise data, regular-vs-EAB choice and an EAB countdown. Use when preparing, formatting or packaging a paper for ICDE (投 ICDE / ICDE 投稿 / 投稿前检查 / 投 ICDE EAB / benchmark paper / experimental survey), or when deciding Round 1 vs Round 2 or regular vs EAB. Includes a LaTeX/PDF/artifact checker with an EAB mode."
---

# Submitting to ICDE (投稿 ICDE 前须知)

Source: ICDE 2027 CFP https://icde2027.github.io/cf-research-papers.html and submission-guidelines.html, read on 2026-11-03 and re-checked on 2026-11-06, 2026-11-09 and 2026-11-10 (research rules unchanged; the site's last commit on 2026-11-09 changed only the demonstration dates; `references/requirements-recheck-2026-11-10.md` has every URL and status; the research text was last changed on 2026-10-28, which renamed the excluded item in the page-limit sentence to "AI-generated content declaration"; the guidelines page still says "acknowledgement", so either heading is accepted). Microsoft CMT documentation for conflicts and author feedback; IEEE Author Center for copyright and posting. Tags: [CFP] = stated in the call; [OBS] = observed in published ICDE papers; [CHECK] = re-verify for a later edition (rules change each year).

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
| Overlap | not under review elsewhere; cite any prior publication it overlaps with; IEEE policy also asks authors to disclose prior publications and current submissions when submitting |
| Scope | must fit a CFP topic and position itself against ICDE/VLDB/SIGMOD work; pure ML/DM without a data-engineering angle is out of scope |
| EAB | title begins with `[Experiment, Analysis, and Benchmark]` (removed at camera-ready); all artifacts mandatory, no exceptions. Full EAB rules with URLs: `references/eab.md` |

## 2a. CMT order of operations [CMT docs, CFP]
CMT help (re-read 2026-11-10): an "Edit Conflicts of Interest" page may appear right after Submit; domain
conflicts may also be requested per submission; co-authors whose e-mail is not registered in CMT receive no
mail from the chairs, so register every co-author's e-mail before submitting.
1. Every author creates a CMT profile, adds ORCID, and enters **Domain Conflicts** as semicolon-separated
   domains (`tudelft.nl; example.com`). Do not enter institution names or public mail domains such as
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
- **AI guideline cited by the CFP is stricter than the CFP text** [IEEE AI-content guideline page linked from the
  CFP, readable since 2026-11-10; see `references/requirements-recheck-2026-11-10.md` item 0.2]: LLM-generated
  text is prohibited unless it is presented as part of the paper's experimental analysis; LLMs may only edit
  text written by the authors; disclosure of editing use is recommended. Check the acknowledgment wording
  against this before submission. If an assistant drafted prose, the authors must rewrite it themselves before
  they may describe the AI use as editing; never change the disclosure to something that did not happen.
  Treat a disclosure that says an LLM "drafted" sections as a desk-reject risk and raise it with the authors.
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
  IEEE Xplore requirements (Author Center, camera-ready): PDF 1.4 or later, fonts embedded or subset, no
  security, no bookmarks, links or attachments; the Type 3 rule comes from PDF eXpress practice, not that page.
- Sign the IEEE eCF copyright form after acceptance.
- Keep the 12-page limit, remove the EAB tag, keep the AI acknowledgment.
- The title, abstract and authors must not change.
- One unique full registration per paper, plus a presenting author.
- Posting: you may post the accepted, not the IEEE-final, version, with the IEEE copyright notice.

## 3c. EAB papers (`references/eab.md`, rules read 2026-11-06 with URLs)
- Tag: the prefix `[Experiment, Analysis, and Benchmark]`, spelled exactly like this. PVLDB's
  `[Experiment, Analysis & Benchmark]` suffix and SIGMOD's `: [Experiments & Analysis]` suffix are wrong
  for ICDE. Remove the tag at camera-ready.
- Artifacts: every artifact needed to reproduce every result is public at submission. "Upon
  acceptance", "on request" and withheld enterprise data are incompatible with "no exceptions". Either
  release de-identified data or a generator, drop the dataset from the EAB claims, or submit as a regular
  paper.
- LLM benchmarks:
  - release the prompts, model identifiers with access dates and parameters, and the cached raw outputs;
  - name the evaluated LLMs, the judges and the labelling models in the AI acknowledgement as tools used
    to run experiments.
- Same 12 pages and no appendix. Extended tables go into the artifact, but every claim must be
  supported inside the paper.
- Choose regular instead of EAB when the main contribution is a new method, or when some data cannot
  be released.
- Countdown T−7 … T−1 and the checker's EAB mode: `references/eab.md` sections 9–10.

## 4. Workflow
1. Decide category (regular or EAB) and round; check the author quota and the one-year rule.
2. Build with IEEEtran; keep the body within 12 pages; move proofs or extra results to a public technical report, not an appendix.
3. Write the AI disclosure as an unnumbered acknowledgment before the references (template in `assets/ai_disclosure_template.tex`).
4. Prepare the artifact repository; make it public before the deadline; cite its URL in the paper.
5. Compile and run the layout gate `manuscript-writing-review`: 0 layout errors, every page seen. If the
   paper lives in an Overleaf project with git access, push through its git bridge, then compare the
   Overleaf PDF with the local one.
6. Run the checker: `python3 scripts/check_icde_submission.py paper/ --pdf paper/main.pdf [--eab] [--artifact ../artifact] [--scope scope.txt]` (`--camera-ready` after acceptance).
7. Every author: ORCID, CMT profile, conflicts (section 2a). The corresponding author fills the subject areas and, if needed, the scope statement (`assets/scope_statement_template.md`).
8. Submit the PDF and the supplemental link on CMT before 5:00 PM PT; keep the CMT confirmation.
9. **Page-count answer for the author.** A 14-page PDF is normal: count body pages up to the page that
   holds the end of the Conclusion and the AI acknowledgment (must be <= 12); references after it are
   free. Funding acknowledgments count toward the 12. Report the split ("12 body + 2 references").
10. **Same PDF as checked.** When the author recompiles on Overleaf, compare its text page by page with
    the locally checked PDF (PyMuPDF `get_text`, whitespace-normalised) before calling it final.
11. **Withheld data.** If any dataset cannot be released, write the reason (personal data, contract,
    commercial) in the CMT supplemental-material field, and release code, generators and the public
    datasets' labels/costs; make sure public datasets carry every headline claim.
12. **Before submitting, run the self-negation pass** of `write-icde` (section 9, `icde_structure_check.py`):
    no loss in the abstract, contributions or conclusion; no "Limitations" or "where it does not" heading.
    Sentences added to satisfy a mock review ("say plainly that ...") need this pass too: on AuthZ-Graph
    they had become 17 concessions ("offers no benefit", "a natural objection", "we know of no"), which the
    extended checker now flags (write-icde section 9d).
13. **Disclosure texts agree with the paper and the artifact** (found on Ladder, ICDE 2027 R2):
    - the AI acknowledgment and the data-availability sentence must not say "all outputs are released"
      when enterprise outputs are withheld; say "all outputs on the public datasets";
    - the CMT scope statement must use the paper's own claim level: if the paper calls a restated
      classical result a Proposition, the scope text must not call it a "theorem" or a contribution;
    - the CMT author list, ORCIDs and title must match the PDF character for character;
    - before pushing a public artifact, regenerate the paper's tables from the artifact copy in a fresh
      folder and diff them with the submitted tables (byte-identical is the target).

14. **Re-check approved limitation rewrites after every page compression** (found on AuthZ-Graph v5/v6,
    ICDE 2027 R2): squeezing the body back to 12 pages removed the mechanism and purpose clauses of three
    approved rewrites (a case study again ended on "0.78x the speed of", "shared the server" came back, the
    primary-source motivation of a synthetic sweep was cut and left "statistics are not published"). After
    each compression round, `git diff` the paper against the last approved version, list every sentence
    that lost a clause, and re-run `icde_structure_check.py`. Cut elsewhere, not the clause that turns a
    loss into a scope statement.

## 5. Checker
`scripts/check_icde_submission.py` inlines `\input` files and checks:
- spacing hacks: `\linespread`, `\enlargethispage`, negative float or caption skips, `\titlespacing`;
- math or footnotes in the title or abstract;
- leftover IEEE template text;
- fonts, with PyMuPDF: embedded, no Type 3;
- the body end, which it finds at the AI acknowledgment or the References heading (including
  IEEEtran's "R EFERENCES" extraction).

EAB mode (`--eab`, or automatic when the title starts with the tag) adds:
- an exact-prefix tag check that catches PVLDB/SIGMOD variants, and tag removal with `--camera-ready`;
- an ERROR for deferred-artifact wording ("upon acceptance", "will be released", "on request"), and a
  WARN for proprietary or internal data;
- WARNs for missing reproducibility facts: hardware, runs, dispersion, versions, and for LLM papers
  temperature and cost;
- a WARN when LLMs named in the body are missing from the AI acknowledgement;
- with `--artifact DIR`, a repository audit: README with commands mapped to tables, licence,
  environment, scripts, raw results, plotting scripts, and no secrets or private-network URLs.

It also checks: IEEEtran conference class; no negative `\vspace`, geometry changes or appendix; author block filled; EAB title tag; AI disclosure in the acknowledgments; abstract length and no citations; citation keys resolved in the `.bib`; number of VLDB/SIGMOD/ICDE references; leftover TODO or placeholder macros; artifact link; scope text length; and, if a PDF exists, page count before the references and US Letter size. It reads files only.

## 6. Final checklist
- [ ] Round and category chosen; quota and one-year rule checked.
- [ ] IEEEtran, at most 12 body pages, no appendix, no negative spacing.
- [ ] Authors and affiliations shown (single-blind); ORCIDs collected.
- [ ] AI disclosure acknowledgment written.
- [ ] Related work positions the paper against ICDE/VLDB/SIGMOD papers.
- [ ] Public artifact repository with code, data and run instructions.
- [ ] EAB only: exact title prefix; every artifact public now (no "upon acceptance"); no unreleasable
      data behind any claim; LLMs used in experiments named in the AI acknowledgement; `--eab --artifact`
      run gives 0 ERROR.
- [ ] CMT profiles and conflicts for every author.
- [ ] Checker passes with no ERROR; `manuscript-writing-review` shows 0 layout errors.
- [ ] CMT abstract identical to the PDF abstract; author list final (frozen at camera-ready).
- [ ] Every author marked individual conflicts after the paper record was created.
- [ ] Body ends on page <= 12 (references free); Overleaf PDF text-identical to the checked PDF.
- [ ] Self-negation pass of write-icde: 0 warnings in abstract, contributions, conclusion.
- [ ] Deadline in local time noted (Round 2: 2026-11-12 09:00 Beijing).
