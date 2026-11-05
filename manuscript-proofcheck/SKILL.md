---
name: manuscript-proofcheck
description: Review and correct the typesetting, rendering, bibliography and mechanical writing of a LaTeX paper before ANY submission (conference or journal, first submission, revision or camera-ready). Use whenever a manuscript is being finalised, a compiled PDF of a submission is shared, the user reports a visual defect in a compiled paper (odd glyph, dash in references, stray box, broken title, overfull line, table past the margin, lower-cased acronyms or mangled names in references, inconsistent names or numbers), or before packaging an Overleaf/zip upload. Runs a source linter and a PDF checker, inspects every rendered page, verifies the bibliography online, fixes the source with minimal edits and reports causes.
---

# Manuscript proofcheck

A compiled paper can be correct in substance and still look careless: a wrong glyph, a dash where an
author list should be, an unfamiliar end-of-proof box, a title broken by hand. Reviewers notice these
first. This skill finds such defects in both the LaTeX source and the compiled PDF, fixes the source,
and explains every cause. It does not change claims, numbers or arguments; content review is the job of
the venue's review skill (e.g. `review-icde`).

## Inputs

- The LaTeX source folder (main file, sections, `.bib`, class/style files).
- The compiled PDF, ideally from the same compiler the venue or Overleaf uses. If no PDF is available,
  run the source checks and say clearly that the visual checks were not done.
- The `.log` and `.blg` files when available (overfull boxes, undefined references, BibTeX warnings).
- The venue's author guidelines (page limit, what counts toward it, review model, template).

## Workflow

1. **Source lint.** Run
   `python3 scripts/tex_lint.py <paper_dir> [--class IEEEtran|acmart|llncs|elsarticle]`. It follows the
   main file's `\input`/`\include` chain and the `.bib` files named by `\bibliography`, so stale copies
   in the folder (such as an exported `overleaf/` directory) do not add noise.
   Every finding has a rule id that points to `references/defect-catalog.md`, which gives the cause and
   the standard fix.
2. **PDF check.** Run `python3 scripts/pdf_check.py <paper.pdf> --out <scratch_dir> [--body-limit N]`
   (needs PyMuPDF). It reports page count and body pages (up to the reference heading), wrong or
   replacement glyphs, unresolved `??` and `[?]`, leftover TODO or coloured draft text, dashes standing
   in for repeated author names, title line breaks, Type 3 or non-embedded fonts. It also renders every
   page to PNG.
3. **Visual pass, every page.** Open every PNG. Do not stop at the pages the user pointed at: the
   defects the user reports are samples of a class. Use the checklist below and write down the page and
   line of each finding.
4. **Bibliography verification.** Check every entry online (DBLP, ACL Anthology, publisher, arXiv).
   This is mandatory, because generated or hand-copied entries often carry a future year, an invented
   DOI or a venue that the paper never appeared in. Delegate to a subagent for long lists. Report
   NOT FOUND entries instead of guessing, and prefer the published venue over arXiv when both exist.
   Self-citations under review must list the full author list, not "et al." or "and others".
5. **Fix.** Make minimal source edits, one defect class at a time. Follow the catalog fix. Keep a backup
   copy of the source before editing. Never use negative `\vspace`, shrunk `\baselinestretch`, changed
   margins or font size to gain space: venues desk-reject for this. Cut text instead.
6. **Re-check.** Re-run both scripts. If a TeX installation is available, recompile, clear warnings and
   re-render the pages. If not, say that the fixes are uncompiled and list what the author must look at
   after compiling (the pages and objects that changed).
7. **Report.** Write the report as a document for the author, in the language the author's standing
   instructions require. For each defect give: where (page/line or file:line), what the reader sees, the
   root cause and the fix applied. Separate it from any submission material.

## Writing-mechanics pass (source and PDF, every submission)

These are mechanical consistency checks, not claims review. Fix them before the visual pass.

- One name per thing: a dataset, configuration, model or method has the same name in the title,
  text, table headers, captions and figure legends (not "Enterprise" in a table and "production
  policy model" in the text; not three spellings of one model).
- Counts stated in words match the enumerations ("two grant styles" lists two; "six placements"
  matches the table). Captions spell small numbers as words ("three models", not "3 models").
- Every symbol is defined before use and no symbol is reused for two things (e.g. `E` as both an
  enforcement point and an identity matrix).
- Numbers in the text come from the same generated source as the tables (macros or a generated
  `numbers.tex`), and every macro used is defined; no hand-typed copy of a table value.
- Statements stay next to their proofs; remarks go after the proof (T19).
- The author block, artifact link and acknowledgements are final (T23) and match the submission
  system.

## Visual checklist (each page)

- Title: no hand-made line break, no orphan word on the last title line, at most three lines.
- Author block: names, affiliations, e-mails and the corresponding-author note match the submission
  system; no TODO left. Anonymous only if the venue is double-blind.
- Glyphs: indicator 𝟙, blackboard letters, script letters, Greek variants (ϵ vs ε used consistently),
  no ⊮, no empty boxes, no "?" in place of a symbol.
- Math: inline radicals, fractions and sums that push into the line above; displays whose second line
  floats far right; equation numbers that collide with the formula; overfull displays in narrow
  columns.
- Theorem-like environments and proofs follow the class style. For example, IEEEtran uses `IEEEproof`
  and its own QED mark, and amsthm's open box looks foreign there.
- Floats: captions readable, tables not overfull (no header or column past the margin, T18/P19), narrow
  cells without word rivers (T24), no float far from its first reference, no column
  that is mostly white, no algorithm or figure placed before the section that introduces it if that
  makes reading hard.
- Text: no overfull lines in the margin, no widow or orphan line at a column top, consistent
  spelling variety (labelling/labeling, -ise/-ize), consistent capitalisation of method names.
- References: no dash for repeated names (unless the venue's style wants it), no "et al." in self
  citations, acronyms keep their capitals (T20), names with non-ASCII initials intact (T21), no
  "ser. ..." labels or chapter records without proceedings titles (T22), consistent venue
  abbreviations, no raw URL breaking the column, no future-dated or unverifiable entries.
- Last pages: body ends within the page limit as counted by the venue (check whether references,
  appendices and acknowledgments count).

## Reporting rules

- Every reported defect must have been seen in the PDF or the source; mark source-only predictions as
  such.
- State plainly what was not checked, such as the result of a recompile or the bibliography items that
  could not be verified.
- Add any new defect class you meet to `references/defect-catalog.md` (cause, detection, fix), so the
  next paper benefits.
