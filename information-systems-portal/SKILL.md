---
name: information-systems-portal
description: "Use when a manuscript is about to be uploaded to, or is being entered in, the Elsevier Information Systems (ISSN 0306-4379) submission portal at submit.elsevier.com/INFOSYS (投稿 Information Systems 投稿窗口/投递). Prepares every upload file and page-by-page answers for all ten portal steps from the elsarticle main.tex, checks the final Overleaf PDF, and lists the portal traps, so no portal screenshots need to be parsed."
---

# Information Systems submission portal (投递 Information Systems 投稿窗口)

This skill covers the **portal step**: what to upload and what to type on each page of the new Elsevier submission service for *Information Systems*. Manuscript preparation (scope, formatting, declarations, Option C data, review protocol) is in the companion skill `information-systems-submission`; run that first. Writing style is in `information-systems-writing`.

Recorded from a complete submission on 2026-10-22 (research paper, LaTeX, Zenodo deposit). If a page differs from this description, the portal has changed: follow the page, then update this file.

## Language convention (permanent agreement with the author)
- **English** for everything reviewers, editors or the portal will see: manuscript, abstract file, highlights, cover letter, declarations, supplementary descriptions, every text typed into the portal, and responses to reviewers.
- **Chinese (中文)** for every report to the author: progress, check results, step-by-step instructions, decisions needed, and internal notes such as package READMEs and review logs.

## Workflow
1. **Finish the manuscript** with `information-systems-submission` (checker clean, Zenodo DOI filled in, final `main.tex`).
2. **Build the portal kit** (generates the required Abstract file and every page's answers from `main.tex`):
   ```bash
   python3 scripts/build_portal_kit.py --tex main.tex --out upload_ready --highlights highlights.txt
   ```
   Fix every WARN. Read `upload_ready/PORTAL_ANSWERS.md` and give the author the per-page values from it; do not ask for portal screenshots.
3. **Lay out the upload folder** exactly as below and put a copy on the author's computer (Downloads) when the session is linked. After copying, **read every file back and compare checksums**: a bridge write once reported success while the old file stayed on disk.
4. **Author compiles on Overleaf** from `02_LaTeX_source/LaTeX_source.zip` (new project → Upload Project, or replace `main.tex` in the existing project). Then verify:
   ```bash
   python3 scripts/verify_final_pdf.py --pdf Manuscript.pdf \
     --expect "<sentence from the latest edit>" --expect "<dataset DOI>" \
     --forbid "<old journal or project code>" --previous <earlier Overleaf PDF> \
     --zip 02_LaTeX_source/LaTeX_source.zip --tex main.tex
   ```
   `RESULT PASS` is required. "identical text to the previous build" or a MISS means a stale `main.tex` was compiled.
5. **Walk the author through the ten steps** below using `PORTAL_ANSWERS.md`. The author clicks every Confirm/Save/Submit; never tick declarations, choose open access, accept terms or submit for them.
6. **After submission**: record date, article type and manuscript number in the package README; remind the author to sign in or set the journal-account password from the confirmation e-mail.

## Upload folder
```
upload_ready/
  00_Abstract/Abstract.docx                 required (generated)
  01_Manuscript/Manuscript.pdf              required (Overleaf build, verified)
  02_LaTeX_source/LaTeX_source.zip          main.tex + elsarticle.cls + figure files
  03_Figures/Figure_1.pdf ...               one file per figure, vector, fonts embedded
  04_Highlights/Highlights.docx             3-5 bullets, each at most 85 characters
  05_Cover_letter/Cover_Letter.docx
  06_Declaration_of_interest/declarationStatement.docx   from Elsevier's Declarations tool
  07_Supplementary/*.zip                    optional when deposited with a DOI
  PORTAL_ANSWERS.md                         generated answers for every page
```

## The ten portal steps
| # | Page | What to do |
|---|---|---|
| 1 | Choose your article type | **Research paper** for a regular article. |
| 2 | Upload your submission files | Upper box (required): **Abstract**, **Manuscript**, **Declaration of competing interests**. Lower box (optional): LaTeX source files, Figure (one upload per figure), Highlights, Cover letter, Supplementary material. Choose the file type, then Upload. |
| 3 | Check or add your title and abstract | Not extracted from the PDF. Paste plain ASCII title and abstract from `PORTAL_ANSWERS.md`; check the abstract's last words. |
| 4 | Check or add your author details | Per author: First name, Last name, Institution (search box, **one** institution per author; pick the university), Email, Contributor roles (CRediT multi-select; the portal spells it "Writing – review & editing"), corresponding-author tick on one author. **Confirm** each, **Add another author** for the next, manuscript order. |
| 5 | Add your funder details | "Did you receive any funding...?" Answer **Yes** whenever the manuscript has a funding statement, including institutional resources without a grant number; name the funder; leave the grant number empty rather than inventing one. **No** only for "did not receive any specific grant". |
| 6 | Decide if you want to publish open access | Author's decision: subscription (free) or gold OA (APC USD 3150 excl. tax in 2026). |
| 7 | Oppose reviewers | Optional; only real conflicts. |
| 8 | Select your classifications | **3–5** from a fixed list; see `references/classifications.md`. No "Data Quality/Cleaning" entry exists. |
| 9 | Provide additional information | Research data: Yes; link `https://doi.org/10.5281/zenodo.<id>` (must start with https://, printed verbatim in the article, so use the DOI); Repository name: Zenodo; Source: Original data for the authors' own protocols, code and results; Title of the data set (max 200 characters) = deposit title. Then the SSRN free-preprint choice: author's decision (YES makes the manuscript public after desk review, permanently). |
| 10 | Review and submit | Author checks and submits. Confirmation page lists date, journal, article type, title and authors. |

## Traps seen in the portal
- **Abstract is a required upload.** The new service lists Abstract, Manuscript and Declaration of competing interests as required. Generate `Abstract.docx` (title + abstract) with the kit script.
- **"I confirm that no authors ... have any competing ... interests" must stay unticked** whenever the manuscript declares any interest (employment, consulting, directorship). Ticking it shows a green "Confirmed" badge and removes the declaration upload, which contradicts the paper. Upload the Declarations-tool file instead; the box then greys out.
- **Declarations tool categories must match the manuscript.** The tool turns relationships into categories (employment; consulting or advisory; ...). If the author confirms a category that the manuscript text does not mention, add it to the manuscript's competing-interest section and the cover letter, rebuild the zip and recompile, so the three agree.
- **Supplementary zips with many files fail.** A 1.4 MB zip holding about 1,700 files returned "Something went wrong – try again" twice, while zips with up to 201 files uploaded. When the supplements are deposited with a DOI and cited, skip the portal upload; keep the portal set all or nothing. Do not split or repack the deposit, or the copies diverge.
- **Stale Overleaf compiles.** Twice an Overleaf PDF came from the previous `main.tex` (the project still held the old file, and once the zip on the author's disk had not been replaced). Always run `verify_final_pdf.py` with `--expect` on the newest sentence and `--previous` on the last build.
- **Do not accept "Confirmed" or pre-filled values blindly.** Re-check every auto-filled field against `PORTAL_ANSWERS.md`.
- **Classification choice drives reviewer matching.** A desk rejection at a sister journal came from a reviewer-pool mismatch; choose classifications whose reviewers publish on the paper's systems, not the broad "Information Systems" entry.
- **Text boxes:** paste ASCII (the kit converts dashes and quotes) and verify nothing is truncated.

## Consistency checks before step 10
- Author names, order, e-mails and corresponding author identical in portal, manuscript title page and cover letter.
- Funding answer (Yes/No) matches the manuscript's Funding section.
- Competing-interest checkbox unticked when the manuscript declares interests; declaration file uploaded.
- Data link equals the `[dataset]` DOI in the reference list and the data statement.
- Highlights file name contains "highlights"; figure files named Figure_N.
- No earlier journal, project code or version label in any uploaded file name or text (`verify_final_pdf.py --forbid`).

## Scripts
- `scripts/build_portal_kit.py`: parses an elsarticle `main.tex` (title, abstract, keywords, `\author[...]`/`\ead`/`\corref`, `\affiliation[...]{organization=...}`, CRediT, Funding, competing interests, data statement, AI declaration, `[dataset]` bibitem, `\includegraphics`) and writes `00_Abstract/Abstract.docx` plus `PORTAL_ANSWERS.md`. Exits non-zero if the dataset DOI is still a placeholder.
- `scripts/verify_final_pdf.py`: fonts (no Type 3, all embedded), `??` and placeholders, required and forbidden text, word diff against an earlier build, and whether the uploaded zip holds the current `main.tex`. Needs poppler (`pdfinfo`, `pdffonts`, `pdftotext`).
