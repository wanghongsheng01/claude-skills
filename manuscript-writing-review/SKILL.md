---
name: manuscript-writing-review
description: Mandatory compile-and-review gate for every LaTeX manuscript before it is handed to the author, uploaded to Overleaf or submitted (any venue, first submission, revision, camera-ready). Compiles the paper, checks every figure and every page for readability and layout defects (heavy inline math that should be displayed, legends or labels cut off or covering bars, tables running into the other column or past the margin, wrapped algorithm comments, justified table cells with gaps, end-of-proof boxes read as garbled glyphs, internal remarks in the bibliography), fixes the source and recompiles until the checks are clean. Use it whenever a paper, an Overleaf zip or a compiled PDF is produced or changed, and whenever the author reports a visual defect.
---

# Manuscript writing review

A reviewer judges a paper by its pages, not by its source. Each defect below has been sent to an
author in a "ready" package because the package was never compiled and looked at. This skill makes
compile, check and fix one loop that ends only when the PDF is clean. It does not change claims or
numbers. For content review use the venue's review skill. For glyphs and bibliography verification it
works together with `manuscript-proofcheck`.

## Hard rules

1. **Never hand over an uncompiled package.** "Ready", "packaged" or "please check the pages on
   Overleaf" are not allowed as a substitute for compiling. If no TeX is installed:
   - ask the user once for permission to install and run a TeX distribution in a scratch or tools
     folder (for example TinyTeX, which runs `pdflatex` without root). Automatic permission
     classifiers block downloaded binaries, so the user's explicit OK is needed;
   - otherwise ask the author to compile on Overleaf and send the PDF, then run steps 4–6 on that
     PDF before saying anything is done.
   State plainly in the report which checks ran on a real PDF.
2. **Every figure and every page is looked at** (PNG), not only the pages someone pointed at. A
   defect the author reports is a sample of a class: search the whole paper for the class.
3. **Fix causes in the generator.** If a table or figure is produced by a script, fix the script and
   regenerate it; never hand-edit the generated `.tex`/`.pdf`.
4. **No space hacks.** No negative `\vspace`, smaller fonts in body text, changed margins or
   `\resizebox` on text tables. Make tables narrower by content (shorter headers, fewer decimals, a
   footnote mark instead of a long cell, `\tabcolsep`), or move them to `table*`.
5. **Readability over compactness for math.** Conditions, set definitions, case distinctions, sums
   and chains of inequalities go in displays (`\[ \]`, `cases`, numbered `equation` only when
   referenced). Prose keeps only short symbols ($k$, $S$, $c(v)\ge t-k$).

## Workflow

Scripts live in `scripts/` of this skill. They need Python 3; the PDF scripts need PyMuPDF
(`python3 -m venv venv && venv/bin/pip install pymupdf`).

1. **Source lint.**
   - `python3 scripts/review_lint.py <paper_dir> --figscripts <scripts that draw figures/tables>`
     (rules R01–R12).
   - Also run `manuscript-proofcheck/scripts/tex_lint.py` if that skill is installed.
   - Fix every ERROR. Check every WARN in the compiled PDF.
2. **Figure check before compiling.**
   - Run `python3 scripts/fig_check.py figs/*.pdf --png <dir>` (F01 text cut off, F02 text over
     text, F03 text over bars).
   - Open every PNG.
   - Legends go above the axes (`loc="lower center", bbox_to_anchor=(0.5, 1.0)`), with at most three
     columns in a one-column figure. Notes such as "labels in ms" go in the caption.
3. **Compile** with the venue's engine (pdfLaTeX for IEEE/ACM unless stated). Run
   `pdflatex, bibtex, pdflatex, pdflatex`.
   - TinyTeX setup that worked (macOS, no root): unpack `TinyTeX-1-darwin-*.tar.xz` from the
     rstudio/tinytex-releases GitHub release into a scratch folder, then run `tlmgr update --self`.
     For IEEEtran papers install `ieeetran algorithm2e ifoddpage relsize cite courier times helvetic
     psnfss symbol zapfding`.
   - For any other missing file, look up its package with `tlmgr search --global --file /<file>`.
   - Read the log for `Overfull \hbox` larger than 1pt, undefined references and missing
     characters.
4. **Layout check.** `python3 scripts/layout_check.py main.pdf --out <dir>`:
   - L01: text runs into the other column;
   - L02: text past the margin;
   - L03: text over text;
   - L04: figure text over bars;
   - L05: end-of-proof boxes;
   - L06: missing glyphs or `??`;
   - L07: figure text cut off.
   Also run `manuscript-proofcheck/scripts/pdf_check.py` if available.
5. **Visual pass, every page**, with the checklist below. Write down page and object for each finding.
6. **Fix, regenerate, recompile, re-run 1–5** until there are 0 errors and the visual pass is clean.
7. **Report** to the author in the language their standing instructions require, as a document:
   - each defect with page, what the reader sees, root cause and fix;
   - what was not checked.
   Keep submission files and the report apart.

## Visual checklist (each page)

- **Math readability**:
  - no theorem, lemma, definition or proof whose statement is a run of inline formulas;
  - case distinctions are set as `cases`;
  - set-builder definitions and sums are displayed;
  - a line does not hold more than about three formulas;
  - no formula split across `$…$, $+…$`.
- **Proofs**: no end-of-proof box (filled or open) unless the venue template mandates it. In IEEEtran
  use `IEEEproof` with `\renewcommand{\IEEEQED}{}`.
- **Figures**:
  - legend fully visible and not over data;
  - no label over another label;
  - axis labels and tick labels inside the canvas;
  - fonts readable at print size (≥ 6 pt).
- **Tables**:
  - inside their column, nothing in the gutter, nothing over body text;
  - text cells left-aligned (`>{\raggedright\arraybackslash}p{}`), so there are no stretched word
    gaps;
  - headers short; numbers at sensible precision.
- **Algorithms**:
  - comments fit on their line or are dropped;
  - long statements use the block form, not `\lIf`;
  - every symbol used is defined in the text before or right after the algorithm.
- **Text**: no overfull lines, no stray characters, no editing remnants, no internal remarks.
- **References**: no notes such as "according to …", "TODO", "?"; no dash for repeated authors.
- **Length**: body within the venue limit after all fixes (displays add height: re-count pages).
- **Last page**: not just the tail of one reference (L08). Trim redundant bib fields (e.g. the publisher
  of LNCS volumes) or text instead of using spacing hacks.

## Reporting rules

- Only report what was seen in the PDF or the source; mark source-only findings as such.
- Add every new defect class to `references/defect-catalog.md`: what the reader sees, the cause,
  automatic detection and the fix. Where possible, add a detection rule to a script.
