# Human-Pleasant Mathematical Typography & Prose Craft for PODS

> **Why This Reference Exists**: A formally correct paper can still be rejected if its pages look like an impenetrable wall of inline subscripts, set-builders, and 20-line unbroken proof bricks. Editors and PC members are human readers. Dissecting **Karmakar et al. (PODS '24)**, **Kolaitis et al. (PODS '25)**, **Fan–Koutris–Roy (PODS '25)**, and **Surianarayanan et al. (PODS '26)** alongside our SIGMOD/PVLDB readability skills (`ccfa-human-readable-math-and-proof`, `sigmod-human-writing-craft`, `academic-latex-polish`) reveals eight concrete rules that make heavy database theory genuinely pleasant to read.

---

## Rule 1 — English Intuition First, Displayed Equation Second ("Never Define Set-Builders Inline")

- **Anti-Pattern (Symbol-Soup Paragraph, >50% inline math)**:
  > Each $\pi \in \Pi^*(D, D')$ assigns dirty cell $(i, a)$ a binary change label $\chi_\pi(i, a) = \mathbb{I}[t'_i[a] \neq t_{\pi(i)}[a]]$ and a clean target $\tau_\pi(i, a) = t_{\pi(i)}[a]$, inducing $\mathrm{Err}(\pi) = \{(i, a) : t'_i[a] \neq t_{\pi(i)}[a]\}$, $\mathrm{TP}_{\mathrm{EC}}(R, \pi) = |\{(i, a) \in S_R \cap \mathrm{Err}(\pi) : \Delta_R(i, a) = t_{\pi(i)}[a]\}|$, and $F_{1,z}(R, \pi) = 2\,\mathrm{TP}_z(R, \pi)/(|S_R| + |\mathrm{Err}(\pi)|)$.
- **Published PODS Craft (`Kolaitis et al. PODS '25 p. 4 & p. 8`; `Fan–Koutris–Roy PODS '25 p. 3`)**:
  1. Introduce the conceptual meaning in calm, plain English with at most **1–2 atomic symbols** per clause.
  2. Put **every set-builder `\{ ... : ... \}`, indicator, fraction, summation, or multi-part score** into a clean centered display (`align*` or `equation`) with generous `\qquad` separation:
  ```latex
  Under an alignment $\pi$, a dirty coordinate $(i, a)$ is corrupted whenever its observed entry disagrees with the matched clean value $t_{\pi(i)}[a]$. Writing $\mathrm{Err}(\pi)$ for the set of corrupted coordinates under $\pi$, a candidate repair $\Delta_R$ on $S_R \subseteq [n] \times [m]$ yields detection and correction true-positive counts
  \[
    \mathrm{TP}_{\mathrm{ED}}(R, \pi) = |S_R \cap \mathrm{Err}(\pi)|, \qquad
    \mathrm{TP}_{\mathrm{EC}}(R, \pi) = \bigl|\{(i, a) \in S_R \cap \mathrm{Err}(\pi) : \Delta_R(i, a) = t_{\pi(i)}[a]\}\bigr|,
  \]
  with Precision, Recall, and $F_1$ defined in the standard way from $\mathrm{TP}_z(R, \pi)$, $|S_R|$, and $|\mathrm{Err}(\pi)|$.
  ```

---

## Rule 2 — Pre-Define Auxiliary Quantities Before `\begin{theorem}` / `\begin{lemma}` (`Karmakar et al. PODS '24 p. 4, p. 9`)

- **Why**: Inside `acmart`, `\begin{theorem}`, `\begin{lemma}`, and `\begin{proposition}` render in *italics*. Packing inline definitions like `$c_v = |\{j : t_j[1] = v\}|$` or `$\tilde{\varepsilon} := \max_{j \in J_{\mathrm{var}}} \frac{2\varepsilon}{\mathrm{range}_j(\widetilde{X}_2) - 2\varepsilon}$` inside an italic theorem block creates visual clutter and stretches line leading.
- **How PODS Exemplars Do It**:
  - Define auxiliary multiplicities, weights, or perturbation radii in **upright Roman prose (or a centered display)** *immediately before* `\begin{theorem}` or `\begin{lemma}`.
  - Keep every theorem, lemma, and proposition statement **concise (2–7 lines)**, free of inline `\sum`, `\prod`, `\frac`, `\binom`, and free of inline set-builders (`\le 32%` inline math characters).

---

## Rule 3 — Reductions & Constructions Use Structured Bullets + Displayed Piecewise Formulas (`Kolaitis et al. PODS '25 p. 16`)

- **Anti-Pattern (19-Line Reduction Brick)**: Cramming input graph $G$, fresh symbols, dirty relation $D'$, clean relation $D$, row-count check, pairwise Hamming case analysis, forward direction, and converse direction into **one continuous 250-word paragraph**.
- **Published PODS Craft (`Kolaitis et al. p. 16`, Proposition 5.1; `Fan–Koutris–Roy p. 17`, Theorem 6.2)**:
  1. **Paragraph 1 (Setup)**: State the source `#P`-complete / `NP`-hard problem in 2 sentences.
  2. **Bulleted Construction**: Present the target database instance $(D, D')$ in **2–3 short bullet items** (`• Dirty snapshot D': ...`, `• Clean snapshot D: ...`).
  3. **Displayed Key Invariant**: Display the piecewise distance or cost identity (`equation` / `cases`) on its own line.
  4. **Paragraph 2 (Bijection / Correctness Idea)**: Explain in 4–6 clean sentences why optimal solutions correspond to valid structures in the source instance. Defer routine case-checking algebra to the Appendix when space is tight!

---

## Rule 4 — Concrete Examples Show Visual Mini-Displays, Not Inline Tuple Dumps (`Fan–Koutris–Roy PODS '25 p. 3`, Example 2.1)

- Never list 4–8 tuples inline as `D stores (x_1, \diamond), (x_2, \diamond), (\star, y_1), and (\star, y_2); pairing (x_1, y_1) with (\star, y_1) and (x_2, y_2) with (\star, y_2) forces...`.
- Either point directly to the visual table in Figure 1 (summarizing its takeaway in plain words), or display the two tiny relations / matchings side-by-side on a centered display line so the reader's eye grasps the symmetry at a glance!

---

## Rule 5 — Main-Body Pacing: Intuitive Proof Sketches vs. Full Proofs (`Karmakar et al. PODS '24 p. 9` vs. `p. 21`)

- Within PODS's strict **15-page main-body limit**, trying to squeeze 10 full algebraic proofs into the body forces you to delete display equations and jam formulas inline—destroying readability!
- **Optimal PODS Division of Labor**:
  - Give **short, self-contained 3–6 line full proofs** in the body when the proof is genuinely conceptual and clean (e.g., LP complementary slackness, denominator invariance, Mann–Whitney tie decomposition).
  - For multi-case or multi-equation proofs (e.g., 4-regime `#OptAlign` dichotomy, perturbed Hungarian gap inequalities + singleton probes, cross-multiplied Lipschitz perturbation bounds), write a **lucid, spacious 6–10 line `Proof Idea` / `Proof Sketch` in the body** (featuring the single central displayed identity and plain-English intuition) and place the **complete, spacious, step-by-step proof in the Appendix**!

---

## Rule 6 — Never Compress the Unlimited Appendix into Inline Symbol Bricks (`Karmakar et al. PODS '24 p. 21`; `Kolaitis et al. PODS '25 p. 22`)

- **Crucial PODS Rule**: The Appendix in PODS has **NO page limit**.
- Never collapse `equation`, `align*`, `cases`, or paragraph breaks into inline formulas in the Appendix!
- Every Appendix proof must:
  1. Break into **clear labeled paragraphs** (`Setup`, `Forward direction (\Rightarrow)`, `Converse (\Leftarrow)`, `Time complexity`), each **4–7 lines long**;
  2. Put **every summation, product, multinomial count, piecewise matrix, and multi-step inequality chain on its own centered display line** (`align*` or `equation`);
  3. Keep inline math character share **$\le 30\%$** per paragraph so checking the appendix is effortless for a diligent reviewer.

---

## Rule 7 — De-Symbolize Experimental & Connective Prose (`sigmod-human-writing-craft` + `academic-latex-polish`)

- In Section 1 (Introduction), Section 6 (Experiments), Section 7 (Related Work), and Section 8 (Conclusion):
  - **Words first, compact numbers in parentheses**: Write *"Across all $8{,}038$ BART cells, change detection is uniquely determined everywhere, while clean targets remain ambiguous on four salary cells in two runs"* rather than `All 8,038 cells had |L^*|=1 (0 ambig.), while 8,034/8,038 had |T^*|=1`.
  - **One idea per sentence (18–26 words average)**: Split semicolon chains (`X; Y; Z`) into separate sentences. Use at most one short parenthetical per sentence, never nested.

---

## Rule 8 — Quantitative Readability Targets (Enforced by `pods_human_craft_audit.py`)

| Readability Dimension | Symbol-Wall Red Flag | Published PODS Target |
|---|---:|---:|
| Prose / Proof Paragraph Inline Math Share ($\ge 180$ chars) | $> 33\%$ | **$8\% \text{–} 28\%$** (max $\le 32\%$) |
| Inline Math Spans (`$...$`) in One Paragraph | $> 16$ spans | **$\le 14$ spans** (split paragraph or display!) |
| Inline Set-Builders `\{ ... : ... \}` in Prose ($\ge 28$ chars) | $\ge 1$ | **$0$** (always display or pre-name) |
| Inline `\sum`, `\prod`, `\frac`, `\binom` in Theorems/Defs | $\ge 1$ | **$0$** (always display or pre-define) |
| Mean Sentence Length | $> 28$ words | **$19 \text{–} 25$ words** |
