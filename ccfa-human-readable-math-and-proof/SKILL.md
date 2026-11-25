---
name: ccfa-human-readable-math-and-proof
description: "Mandatory mathematical readability, proof QED typography, and figure-to-text formula consistency skill for SIGMOD, PVLDB, ICDE, and TKDE papers. Reverse-engineered from published AlayaDB (SIGMOD '25), WAIR (SIGMOD '26), Cortex AISQL (SIGMOD '26), LOTUS (PVLDB '25), and DBSP (PVLDB '23). Eliminates dense walls of inline symbols in narrow two-column paragraphs, enforces baseline-aligned geometric QED squares without orphan lines or stretched leading, and verifies 100% symbol/formula exactness between every figure and the paper body."
---

# Human-Readable Mathematical Writing, Proof Typography & Figure Formula Consistency

**CORE PRINCIPLE:** Academic database papers are read by busy human reviewers in narrow `3.3-inch` two-column layouts—not by compilers. A paragraph stuffed with 12 inline formulas, a 19-line italic theorem block, a floating/misaligned QED square `□`, or a figure formula using an undefined symbol immediately degrades reviewer trust.

---

## 1. Five Golden Laws of Human-Pleasant Database Math (From Published SIGMOD & PVLDB Exemplars)

1. **Law 1 — Pre-Define Setup Before `\begin{theorem}` (`AlayaDB` SIGMOD '25 p. 7; `WAIR` SIGMOD '26 p. 8)**:
   - Never dump 10 lines of notation definitions *inside* an italic `\begin{theorem}` block.
   - Define the domain, projection, and estimator in normal Roman prose (plus one clean centered display equation if it contains a `\sum` or ratio) **before** the theorem.
   - Keep every `\begin{theorem}` / `\begin{proposition}` / `\begin{lemma}` concise (**4–9 lines**), so a reviewer grasps the scientific guarantee in one glance.
2. **Law 2 — Display Equations Over Inline Symbol Soup**:
   - Any expression containing `\sum`, `\prod`, `\bigcup`, `\bigsqcup`, `\arg\max`, a multi-term fraction, or an `=`/`\le` derivation chain of $\ge 2$ steps **MUST be placed in a centered display environment** (`equation` or `align*`), **never** jammed inline inside justified two-column prose.
3. **Law 3 — Paragraph Inline-Math Density Budget ($\le 26\%$ Math Characters, $\le 3$ Math Spans/Sentence)**:
   - Never chain parameter assignments inline like `set den(g_1)=M, r(g_1)=\varepsilon (num(g_1)=M\varepsilon), and for all g \in F_u \setminus \{g_1\} set den(g)=1, r(g)=1 (num(g)=1)`.
   - State the construction in clear English (*"Assigning volume $M \gg 1$ with rate $\varepsilon$ to a minimum-weight cell $g_1$ and unit volume with unit rate elsewhere gives..."*) followed by a single clean display line.
   - In experimental prose, prefer natural English (`ADS hit rates of 0%, 50%, and 100%`; `two-row rollup groups`) over gratuitous inline set notation (`\rho \in \{0\%, 50\%, 100\%\}`).
4. **Law 4 — Baseline-Aligned Geometric QED Square & Clean Proof Closing (`Cortex AISQL` p. 4; `WAIR` p. 8)**:
   - **Font Trap in `acmart` (`txsya`):** Default `acmart` + `newtxmath` maps `\qedsymbol` (`\openbox`) to a tiny `3.5 pt` elevated box floating in the upper half of the line—which looks vertically misaligned next to lowercase text and resembles a missing-glyph tofu box `□` when stranded across a wide blank gap.
   - **Mandatory Fix in Preamble:** Define an exact baseline-aligned `0.50em × 0.50em` hollow Halmos square sitting at `0.00 pt` depth on the baseline:
     ```latex
     \renewcommand{\qedsymbol}{\leavevmode\hbox{\vrule height 0.50em width 0.45pt\vbox to 0.50em{\hrule width 0.41em height 0.45pt\vss\hrule width 0.41em height 0.45pt}\vrule height 0.50em width 0.45pt}}
     ```
   - **Proof Closing Line Geometry:**
     - Zero `\sum`, `\prod`, `\frac`, `\bigl`, or tall math in the **last 2 lines** of any `\begin{proof}`.
     - The final text line before `\qedsymbol` must occupy **42%–88% of the column width** (never an orphan `□` alone on a blank line, and never a `<35%` 2-word widow tail leaving a giant blank chasm before `□`).
5. **Law 5 — 100% Figure-to-Body Formula & Symbol Consistency (Mandatory on Every Version!)**:
   - Every mathematical symbol, complexity bound, parameter tuple, and `(Thm. X)` / `(Alg. Y)` / `(Eq. Z)` badge inside every figure **must be 100% identical** to the notation and numbering in `main.tex`, and **must match the plotted axis variable**!
   - **Matplotlib STIX Glyph Ban:** Never use `\setminus` in Matplotlib `stix` mathtext—it renders as a tiny half-height floating tick `∖` (`U+2216`) that looks broken. Either write complexity directly in terms of the plotted axis variable (e.g., `$O(1)$ vs. $|T|$` when the x-axis is `Warehouse Tables $|T|$`) or use explicit clean notation defined on the figure axes.
   - Never leave stale parameter symbols from earlier drafts in architecture boxes (e.g., writing `(\tau_0, N^*)` in a figure when Equation (5) in the text uses `(\alpha, n_{\min})`, or mixing `|H_k|` in figures with `|H_c|` in theorems).

---

## 2. Mandatory Automated Gates (Run on Every Build!)

```bash
python3 scripts/proof_and_math_audit.py path/to/main.tex path/to/main.pdf
python3 scripts/figure_formula_consistency_audit.py path/to/main.tex path/to/figure_script.py
```
Both scripts must exit with **`0 FAIL(s)`** before any PDF is synced to Overleaf, GitHub, or cloud storage.
