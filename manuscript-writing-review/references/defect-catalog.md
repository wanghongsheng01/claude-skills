# Defect catalog

Each entry gives what the reader sees, the cause, how it is detected and the fix.

- R* rules come from `scripts/review_lint.py` (source).
- F* rules come from `scripts/fig_check.py` (figure files).
- L* rules come from `scripts/layout_check.py` (compiled PDF).

*Observed* marks a defect that reached an author.

## Process failure behind all of them (*observed*, CertKP, ICDE 2027, 2026-11-06)

- **Seen.** The author compiled the "final" Overleaf package and found:
  - a cut-off legend;
  - black boxes at the end of proofs;
  - lemmas written as walls of inline symbols;
  - a legend over bars;
  - a table printed over the next column.
- **Cause.**
  - No TeX was installed, and the package was sent with "please check the pages on Overleaf".
  - Source lints cannot see figure geometry or table width.
- **Fix.** Hard rule 1 of SKILL.md: compile, or get the author's PDF and check it, before any handover.

## Math readability

### R01 Heavy inline formula (*observed*)
- **Seen.** Set-builder definitions, sums and long conditions inside running text, e.g.
  `$F\cup\{x\notin F: |N(x)\cap F|\ge\omega-k-1,\ c(x)\ge\omega-k\}$` or a sum with two index sets
  in a theorem. The line spacing breaks apart and the formula is hard to parse.
- **Detect.** Inline math with `\sum`, `\prod`, `\bigcup`, a set-builder `\{…:…\}`, `cases`, more
  than 55 characters, or five or more relations or operators.
  - `\frac` and `\binom` are reported as WARN (tall inline).
- **Fix.** Use a display `\[ … \]`. For a case distinction ("≥ a if (x,y)∈E and ≥ b otherwise"), use
  `\begin{cases}`. Number it only if it is referenced (`\eqref`).

### R02 Too many formulas in one sentence (*observed*)
- **Seen.** Lemmas and theorems whose statement is a sequence of (i), (ii), (iii) with inline
  formulas; reviewers call them "dense characters".
- **Detect.** Seven or more inline formulas with relations or operators in one sentence.
- **Fix.**
  - Define auxiliary symbols first (e.g. `Let $H_t=…$.`).
  - Put each condition's formula in a display.
  - Split the sentence.

### R03 Formula broken by an editing remnant (*observed*)
- **Seen.** "… + s, +i, where" — a sum split as `$…+ s$,\n$+\,i$`.
- **Detect.** A comma followed by inline math that starts with `+`, `-` or `=`.
- **Fix.** Join the formula, preferably as a display.

### R08 Numbered equation never referenced
- **Seen.** Equation numbers that nothing refers to. This is not wrong, but it is noise.
- **Detect.** An `equation` whose label is never referenced, or an `equation` without a label.
- **Fix.** Use `\[ \]`, or reference the equation where it is used.

## Proofs

### R04 / L05 End-of-proof box read as a garbled glyph (*observed* twice)
- **Seen.**
  - With amsthm under IEEEtran, an open square □.
  - After switching to `IEEEproof`, IEEEtran's default closed box ■.
  - Authors flagged both as "乱码" (garbled characters).
- **Cause.** The two box styles look like missing-glyph boxes at the end of a line. The earlier fix
  (amsthm → IEEEproof) changed the box but did not remove it.
- **Detect.**
  - Source: IEEEtran with a proof environment and no `\renewcommand{\IEEEQED}{}`.
  - PDF: IEEEtran draws the mark as a small filled square (≈5.8 pt), and layout_check L05 finds it.
- **Fix.** Use IEEEproof and drop amsthm, then add `\renewcommand{\IEEEQED}{}` after the packages.
  Keep a mark only if the venue template mandates one.

## Figures

### F01 / L07 Legend or label cut off at the canvas edge (*observed*)
- **Seen.** "Cer" instead of "CertKP" at the right end of the legend.
- **Cause.** A matplotlib legend with `ncol=5` in a 3.4-inch figure, placed in the axes with `loc="upper
  left"`. The legend was wider than the canvas, and `tight_layout` does not shrink legends.
- **Detect.**
  - fig_check F01 compares clipped and unclipped text extraction.
  - layout_check L07 finds words that end at the figure's outer panel.
- **Fix.** Put the legend above the axes (`loc="lower center", bbox_to_anchor=(0.5, 1.0)`) with at
  most three columns in a one-column figure, raise the figure height, and regenerate.

### F02 / L03 Annotation over a data label (*observed*)
- **Seen.** "bar labels in ms" printed over the value label "148".
- **Cause.** `ax.text(…, transform=ax.transAxes)` at a fixed position, with data-dependent labels
  under it.
- **Fix.** Move such notes to the caption ("Bar labels give the time in ms.").

### F03 / L04 Legend over bars (*observed*)
- **Seen.** In the ablation figure, the legend entry "BasicX+" was drawn over the tallest bars.
- **Cause.** `loc="upper right"` inside the axes, while the tallest bars sit in the middle and on the
  right.
- **Fix.** Place the legend above the axes; never rely on `loc="best"` for bar charts.

### R11 / R12 Figure-script risks
- **Detect.**
  - R11: a legend inside the axes without `bbox_to_anchor`; free text in axes coordinates.
  - R12: a legend with five or more columns.
- **Fix.** As in F01–F03. Verify with fig_check.

## Tables

### L01 / L03 Single-column table running into the other column (*observed*)
- **Seen.** The last column ("Glob (L/C)") of an 8-column table was printed over the body text of
  the right column.
- **Cause.** Column count, a long header and two-decimal ratios at `\footnotesize` with
  `\tabcolsep=2.4pt` gave 267 pt for a 252 pt column. Floats do not warn about this in the PDF
  (only "Overfull \hbox" in the log).
- **Detect.**
  - R09: seven or more columns at `\small`, or eight or more at `\footnotesize`.
  - L01: a word enters the gutter while the other column has text on the same line.
  - L03: text over text.
- **Fix.** In the generating script, shorten the header (move "L/C" to the caption), use one
  decimal for values ≥ 10, use `L/C` without spaces, and reduce `\tabcolsep`. Otherwise use
  `table*`.

### L02 Table past the page margin (*observed*)
- **Seen.** A 7-column dataset table in the right column, about 22 pt past the margin.
- **Cause.** `\small`, `\tabcolsep=4pt` and a long text cell ("Q&A, temporal").
- **Fix.** Use `\footnotesize`, `\tabcolsep=3pt`, and a short cell with a footnote mark ("Q&A$^\dagger$",
  with "$^\dagger$: temporal" in the caption).

### R05 Justified narrow cells with word gaps (*observed*)
- **Seen.** "two-seed region", "reused, credited" spread across the cell with big gaps.
- **Cause.** `p{}` columns are justified.
- **Fix.** Use `>{\raggedright\arraybackslash}p{…}` and `\usepackage{array}`.

## Algorithms

### R06 Wrapped algorithm comments and one-line statements (*observed*)
- **Seen.** A comment like `// order-based, Sec. V-C` broken over two lines; the comment of a
  one-line `\lIf` on its own line; a fallback statement whose comment wrapped twice.
- **Detect.** A `\tcp` text longer than 18 characters; a one-line algorithm statement with a comment
  longer than 110 characters.
- **Fix.** Keep comments to a reference (`Thm. 2`) or drop them. Use the block form `\If{…}{…}` for
  long statements.

### R07 enumerate options without a package
- **Seen.** A compile error or a literal "[(a)]".
- **Fix.** Inside theorems, write `(a)~ … (b)~ …` inline. Do not load enumitem with IEEEtran.

## Bibliography

### R10 Internal remark in a bib note (*observed*)
- **Seen.** "accepted to ICDE 2027 (according to the arXiv comments)" printed in the references.
- **Fix.** Use a neutral note ("To appear in ICDE 2027") or none. Use the published version once it
  exists.

## Page flow

### L08 Last page with only a few lines (*observed*)
- **Seen.** After the math was set as displays, the paper ran to 13 pages, and page 13 held only the
  last two lines of reference [60].
- **Fix.** Remove redundant bib fields (for example, `publisher = {Springer}` in LNCS entries whose
  series already identifies the publisher) or trim text. Never shrink the spacing.
