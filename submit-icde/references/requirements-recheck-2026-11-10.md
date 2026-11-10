# ICDE 2027 research track, Round 2: requirements re-check of 2026-11-10

Re-check date: 2026-11-10, 22:10-22:30 Asia/Shanghai (14:10-14:30 UTC). All pages listed were downloaded or
read on that date. Purpose: input for updating the `submit-icde` skill
(`/Users/loctek/.claude/skills/submit-icde/`). Written in English at the explicit request of the task (an
exception to the usual Chinese-report convention, as for the 2026-11-06 file).

Compared against: `SKILL.md` (sources dated 2026-11-03/06/09), `references/requirements-recheck-2026-11-06.md`
and `references/eab.md`.

Status legend:
- **CONFIRMED**: seen today on an official page and matching the skill.
- **UNCHANGED**: not re-readable or not re-stated today, but the evidence (byte-identical page, no new
  commit) shows it still matches the skill.
- **CHANGED/NEW**: differs from the skill or was not in it. Marked with **>>>**.
- **UNVERIFIED**: still not readable from a public source.

Verbatim fragments are short (under 15 words) and in quotation marks.

## Sources read today (2026-11-10)
| Tag | URL | Result |
|---|---|---|
| CFP | https://icde2027.github.io/cf-research-papers.html | 200; byte-identical to `01_guidelines/raw/` snapshot |
| SG | https://icde2027.github.io/submission-guidelines.html | 200; byte-identical to snapshot |
| ID | https://icde2027.github.io/important-dates.html | 200; **2 lines differ** (Demo track only) |
| HOME | https://icde2027.github.io/index.html (also reached via https://ieee-icde.org/2027) | 200; byte-identical |
| AP | https://icde2027.github.io/accepted-papers.html | 200; byte-identical |
| FUT | https://icde2027.github.io/cf-future.html | 200; byte-identical |
| — | https://icde2027.github.io/formatting-guidelines.html, faq.html, camera-ready.html | 404 (no such pages) |
| GIT | https://api.github.com/repos/icde2027/icde2027.github.io/commits | newest commit `eeabdfdc` 2026-11-09T12:59Z "demo-update" |
| ICDE26 | https://icde2026.github.io/cf-research-papers.html | 200 |
| ICBC | https://icbc2025.ieee-icbc.org/ai-content-generation-guidelines (the AI page the CFP cites) | 200, **readable today** (TLS failed on 11-06) |
| IEEE-POL | https://conferences.ieeeauthorcenter.ieee.org/author-ethics/guidelines-and-policies/submission-policies/ | 200 |
| IEEE-XPL | https://conferences.ieeeauthorcenter.ieee.org/write-your-paper/meet-ieee-xplore-requirements/ | 200, **new source** |
| IEEE-CR | https://conferences.ieeeauthorcenter.ieee.org/get-published/about-transferring-copyright-to-ieee/ | 200 |
| IEEE-TPL | https://www.ieee.org/conferences/publishing/templates.html | 202 bot challenge (still unreadable) |
| IEEE-TOOLS | https://conferences.ieeeauthorcenter.ieee.org/write-your-paper/authoring-tools-and-templates/ | 200 (only points to Word/LaTeX templates and Overleaf) |
| OVL | https://www.overleaf.com/latex/templates/ieee-conference-template/grfzhhncsfqn | 200 |
| CMT-COI | https://cmt3.research.microsoft.com/docs/help/chair/conflicts.html | 200 |
| CMT-SUB | https://cmt3.research.microsoft.com/docs/help/author/author-submission-form.html | read via WebFetch, **new source** |
| CMT-FB | https://cmt3.research.microsoft.com/docs/help/author/author-feedback.html | 200 |
| CMT | https://cmt3.research.microsoft.com/ICDE2027 | redirects to login; form not public |
| PDFX | https://ieee-pdf-express.org/ | redirects to login |
| Search | web search "ICDE 2027 research papers round 2 deadline ... extension" | no extension found anywhere |

---

## 0. What changed since the skill was written

**>>> CHANGED/NEW 0.1: the site changed on 2026-11-09, but not for the research track.**
- Commit `eeabdfdc` (2026-11-09T12:59Z, "demo-update") touched only `cf-demonstrations.html` and
  `important-dates.html` [GIT]. Every page now reports `last-modified: Mon, 09 Nov 2026 13:00:16 GMT`.
- The only content change: Demonstrations due **2026-12-07** (was 11-23), notification **2027-02-19**
  (was 02-10) [ID].
- CFP and SG are byte-identical to the snapshot, so every research-track rule is unchanged.
- Skill action: the `SKILL.md` source line says "site last updated 2026-10-28". Change it to "re-checked
  2026-11-10; last site commit 2026-11-09 (demo dates only); research-track text last changed 2026-10-28".

**>>> CHANGED/NEW 0.2: the IEEE AI-guideline page cited by the CFP is now readable, and it is stricter
than the CFP's own wording** [ICBC, read 2026-11-10].
- The CFP points to it with "As per IEEE guidelines" [CFP]. The skill had it as UNVERIFIED (TLS failure).
- It repeats the CFP's disclosure text, and adds three sentences that the CFP does not copy:
  1. For editing and grammar use, "disclosure as noted above is recommended".
  2. LLM-generated text is "prohibited unless the produced text is presented as a part of the paper's
     experimental analysis".
  3. LLMs may be used for editing "text solely written by the authors"; authors remain responsible
     for plagiarism and veracity checks.
- Skill action: in section 3 (AI disclosure) add: the AI acknowledgment should say that the prose was
  written by the authors and that AI was used only for editing (or name exactly where generated content
  appears, e.g. code, figures, experiment outputs); LLM outputs quoted in the paper must be presented as
  experimental results. Treat grammar-editing disclosure as recommended (already the skill's advice).

**>>> CHANGED/NEW 0.3: IEEE Xplore PDF requirements now read from the official IEEE page** [IEEE-XPL,
read via WebFetch 2026-11-10]. Camera-ready only, not a submission rule.
- PDF version 1.4 or later, but "not Acrobat 9, X, or XI" output.
- "All fonts are embedded or subset." The page does not mention Type 3 fonts (the skill's "no Type 3"
  came from older secondary IEEE guides; keep it as safe practice, label it [2nd]).
- No passwords or security settings; no scanned pages.
- No bookmarks, **links**, crop or registration marks, date stamps or PDF attachments; no PDF Package
  or merged PDF.
- PDF eXpress is used only by some conferences; such conferences send an invitation e-mail with a custom
  link. Otherwise use the IEEE PDF Checker. ICDE says its PDF eXpress instructions are inside the CPS kit
  [CFP], so expect the CPS link to lead to it.
- Paper size is not stated on this page.
- Skill action: in section 3b add "no hyperlinks/bookmarks in the camera-ready PDF unless PDF eXpress
  accepts them (load `hyperref` with `draft` or remove it if eXpress complains)", and source it.

**>>> CHANGED/NEW 0.4: CMT submission mechanics (from the CMT author help page)** [CMT-SUB, CMT-COI].
- If the chair enabled it, an "Edit Conflicts of Interest" page appears right after clicking Submit
  [CMT-SUB]. This complements the skill's rule that individual conflicts become visible only after a
  paper exists [CMT-COI, CONFIRMED today: "An Author must submit a paper before they can see the
  Individual Conflicts"].
- Authors "may be asked to enter domain conflicts in two ways": for themselves and per submission
  [CMT-COI]. Fill both if the ICDE form shows both.
- A title and abstract can be submitted without files and edited later, if the chair's Edit Submission
  phase is enabled; files are saved only when Submit is clicked [CMT-SUB].
- CMT e-mails a confirmation to all authors, but co-authors who never registered their e-mail with CMT
  get no mail from chairs [CMT-SUB]. Every co-author's CMT e-mail must match the address entered in the
  author list.
- Skill action: add these four lines to section 2a.

**>>> CHANGED/NEW 0.5: IEEE-level duty to disclose prior publications and concurrent submissions**
[IEEE-POL, read 2026-11-10].
- IEEE policy says authors "must disclose all prior publication(s) and current submissions" when
  submitting. ICDE's own rule is the "cite the prior publication" requirement [CFP].
- Skill action: in the Overlap row, add that any overlapping prior paper (including workshop or
  ≤4-page versions) must be cited and mentioned; if CMT asks about related submissions, answer it.

Nothing else changed. In particular the page-limit rule, dates, COI definition, quota, single-blind
review, desk-reject list, scope statement and re-submission policy are identical to the skill.

---

## 1. Checklist (Round 2)

### 1.1 Dates [CFP, ID, HOME; read 2026-11-10]
| Item | Status | Detail |
|---|---|---|
| Submission due 2026-11-11, "5:00PM Pacific Time" | CONFIRMED | PST in November: **2026-11-12 01:00 UTC = 09:00 Beijing** (zoneinfo, computed 2026-11-10) |
| Rebuttal 2027-01-08 to 01-15 | CONFIRMED | ends 01-16 09:00 Beijing |
| Notification 2027-02-10, "Notification dates are approximate" | CONFIRMED | |
| Camera-ready 2027-03-10 | CONFIRMED | |
| CMT opens "a week before the submission deadline" | CONFIRMED | HOME: "The Round 2 submission is open" |
| No deadline extension | CONFIRMED | none on official pages or in a web search, 2026-11-10 |
| Other tracks | >>> CHANGED (Demo only) | Demos 2026-12-07 / notif. 2027-02-19; Tutorials 11-20; Industry 12-01; PhD 11-11; DEFT 11-22 [ID] |
| Conference | CONFIRMED | Copenhagen, 2027-05-17 to 21 [HOME] |

### 1.2 Page limit and what counts [CFP; read 2026-11-10]
| Item | Status | Detail |
|---|---|---|
| Limit | CONFIRMED | "must not exceed 12 pages", for research and EAB papers |
| Excluded | CONFIRMED | only "references and the AI-generated content declaration" |
| Appendix | CONFIRMED | "No appendix is allowed." |
| Funding / other acknowledgments | UNCHANGED (inference) | not excluded by the wording, so they count toward 12 |
| Reference pages | CONFIRMED | no cap stated (ICDE 2023/2024 had "+4 pages"; gone) |
| Format | CONFIRMED | "Only electronic submissions in PDF format" |
| SG wording | CONFIRMED | SG says "AI-generated content acknowledgement" instead of "declaration"; same item |
| Camera-ready | CONFIRMED | 12 pages "excluding the AI-generated content acknowledgments and the references" |
| ICDE 2026 | CONFIRMED | same rule, "AI-generated content acknowledgement" [ICDE26] |

### 1.3 Template, fonts, margins [CFP, OVL, IEEE-TOOLS; read 2026-11-10]
| Item | Status | Detail |
|---|---|---|
| IEEE format (conference template) | CONFIRMED | CFP links the IEEE templates page |
| Negative space / margins | CONFIRMED | "negative spaces, content entering the margins, or similar" are violations (CFP; absent from SG) |
| Remove template text | CONFIRMED | Overleaf official template: "ensure that all template text is removed" |
| No symbols, special characters, footnotes or math in title/abstract | CONFIRMED | Overleaf template abstract text |
| Sub-titles not captured in Xplore | CONFIRMED | Overleaf template |
| Paper size, font, PDF version for submission | UNVERIFIED | ICDE states none; IEEE templates page is still bot-protected (HTTP 202); IEEEtran default is US Letter |
| Camera-ready PDF rules | >>> NEW | see 0.3 (PDF ≥1.4, fonts embedded/subset, no security, no links/bookmarks) |

### 1.4 Review model [CFP, SG; read 2026-11-10]
| Item | Status | Detail |
|---|---|---|
| Single-blind | CONFIRMED | "reviewed in a single-blind manner" |
| ≥3 reviewers, senior PC meta-review | CONFIRMED | SG still says "area chair" |
| Accept/Reject only | CONFIRMED | "There will be no revisions." |
| ORCID for all authors at submission | CONFIRMED | where it is entered: UNVERIFIED (CMT form; not in CMT-SUB help) |

### 1.5 Supplemental material / artifacts [CFP; read 2026-11-10]
| Item | Status | Detail |
|---|---|---|
| Expected for all papers | CONFIRMED | availability "will be considered in the evaluation" |
| If none | CONFIRMED | explanation "in the submission form" |
| EAB | CONFIRMED | "MUST provide all artifacts"; "No exceptions" |
| Hosting | CONFIRMED | public URL, e.g. "a public GitHub repo"; no personal web pages / tracking |
| CMT file upload for supplements | UNVERIFIED | CMT allows files only per chair settings [CMT-SUB] |

### 1.6 AI-generated content [CFP, ICBC, IEEE-POL, ICDE26; read 2026-11-10]
| Item | Status | Detail |
|---|---|---|
| AI not an author | CONFIRMED | |
| Disclose in acknowledgments: system, sections, level | CONFIRMED | incl. LLMs for "data processing, filtering, visualisation" and running experiments |
| Grammar editing outside the policy's intent | CONFIRMED | CFP |
| Editing disclosure "recommended"; generated prose prohibited unless experimental | >>> NEW | from the cited IEEE page, see 0.2 |
| AI editing should exclude the reference section | CONFIRMED | IEEE-POL |
| Heading "AI-Generated Content Acknowledgement" just before References; "err on the side of caution" | CONFIRMED | ICDE 2026 rule [ICDE26]; 2027 silent, so keep it |
| Mandatory at camera-ready | CONFIRMED | "disclosure acknowledgments are mandatory" |

### 1.7 Conflicts of interest [CFP, SG, CMT-COI; read 2026-11-10]
| Item | Status | Detail |
|---|---|---|
| Against PC and senior PC | CONFIRMED | |
| Definition (CFP) | CONFIRMED | co-authors of a submission under review; co-author 2023–present; ≥4 papers 2016–present; co-workers 2023–present (Domain Conflicts); collaborators past 3 years / 2023–present; thesis advisor ever; relatives or close friends |
| SG older wording | CONFIRMED | e.g. "4 or more publications in the last 10 years" — declare under both |
| Judged at closing time; automated check; frivolous COIs are violations | CONFIRMED | |
| CMT profile for every author, else desk reject | CONFIRMED | |
| Individual conflicts visible only after a submission exists | CONFIRMED | CMT-COI |
| Domain format `a.edu; b.com`, no gmail etc. | CONFIRMED | CMT-COI |
| Edit-COI page after Submit; per-submission domain conflicts; e-mail registration of co-authors | >>> NEW | see 0.4 |

### 1.8 Eligibility, quota, re-submission [CFP, SG; read 2026-11-10]
| Item | Status | Detail |
|---|---|---|
| Max 5 research-track papers per author "per submission round" (regular + EAB) | CONFIRMED | same in SG |
| Not under review elsewhere until decision | CONFIRMED | resubmit elsewhere only "after it is rejected or withdrawn" |
| Novelty: prior publication > 4 double-column pages; cite overlaps | CONFIRMED | |
| IEEE: disclose prior publications and current submissions | >>> NEW | see 0.5 |
| 1-year wait "including revisions"; Round 1 reject ineligible for Round 2; may go to ICDE 2028 Round 1 | CONFIRMED | SG counts the year "from the time of their last submission" |
| Round 1 desk rejects for COI / length / format may go to Round 2; out-of-scope may not | CONFIRMED | |

### 1.9 Desk-reject criteria [CFP; read 2026-11-10]
| Item | Status |
|---|---|
| Non-compliance with instructions | CONFIRMED |
| Formatting and length violations | CONFIRMED |
| COI violations (missing, incorrect, frivolous) | CONFIRMED |
| Missing CMT profile for any author | CONFIRMED |
| Out of scope; positioning "typically" in related work vs ICDE/VLDB/SIGMOD | CONFIRMED |
| Scope explanation "(in 1000 characters)", (a)/(b)/(c); example #4 "insufficient" | CONFIRMED |
| "The responsibility rests with the authors" | CONFIRMED |

### 1.10 Rebuttal [CFP, CMT-FB; read 2026-11-10]
| Item | Status | Detail |
|---|---|---|
| Rebuttal period Jan 8–15, no revision | CONFIRMED | |
| Format / length | UNVERIFIED | still unpublished by ICDE |
| CMT: meta-reviews "may not be visible"; uploads only per chair; click Submit | CONFIRMED | CMT-FB |

### 1.11 Camera-ready, registration, copyright [CFP, SG, IEEE-CR, IEEE-XPL; read 2026-11-10]
| Item | Status | Detail |
|---|---|---|
| Upload via IEEE CPS, not CMT; PDF eXpress instructions in CPS kit | CONFIRMED | |
| EAB tag removed; title/abstract/authors/CMT metadata frozen | CONFIRMED | |
| Registration: ≥1 full author registration, one per paper; Xplore removal if not met | CONFIRMED | SG still says "presentation at the conference is not required"; CFP assumes an author presents |
| eCF link "after your paper is accepted" | CONFIRMED | IEEE-CR |
| Xplore PDF rules | >>> NEW | see 0.3 |

### 1.12 EAB (`references/eab.md`) [CFP; read 2026-11-10]
| Item | Status |
|---|---|
| Prefix `[Experiment, Analysis, and Benchmark]`, removed at camera-ready | CONFIRMED |
| All artifacts, "No exceptions" | CONFIRMED |
| Same 12 pages, no appendix | CONFIRMED |
| PVLDB/SIGMOD tag forms | UNCHANGED (not re-read today) |

### 1.13 Still unverified (unchanged list)
CMT form fields (ORCID location, subject areas, scope field label, supplementary upload), rebuttal length,
IEEE templates page content (bot challenge), ICDE 2027 PDF eXpress conference ID, any ICDE review form.

## 2. Edits suggested for `submit-icde`
1. `SKILL.md` source line: add "re-checked 2026-11-10: research-track text unchanged; site commit
   2026-11-09 changed only demo dates".
2. Section 3 (AI disclosure): add 0.2 (prose written by authors; generated text only as experimental
   output; editing disclosure recommended), citing the ICBC URL.
3. Section 3b (camera-ready): add 0.3 (IEEE Xplore PDF rules, links/bookmarks), citing IEEE-XPL; label
   the Type 3 rule as secondary.
4. Section 2a (CMT): add 0.4 items.
5. Section 2 Overlap row: add 0.5.
6. Section 1 "other tracks" is not in the skill; no change needed unless the skill lists demo dates.
