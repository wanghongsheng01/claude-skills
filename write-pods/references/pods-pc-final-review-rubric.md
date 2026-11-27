# ACM PODS (PACMMOD) 3-Reviewer Pre-Submission Final Review Rubric & Proof/Visual Hardening Guide

Distilled from official **ACM PODS / PACMMOD** reviewing standards (journal-first multi-cycle review, strict 15-page main body excluding unlimited References and Appendix, double-anonymous policy) and real end-to-end hardening across ten full iterations (`v1 → v10`) of an ACM PODS 2027 Cycle 2 submission.

Use this rubric **after** the manuscript passes structural drafting and baseline linting, as the **final simulated PC meeting** right before uploading to EasyChair / Overleaf.

---

## 1. Reviewer #1 — Complexity & Proof-Soundness Theorist (Zero-Gap Proof Audit)

PODS reviewers read proofs line by line. Never ship a paper with any of these **7 classic PODS proof traps**:

1. **Parsimonious Reductions vs. Non-Empty Solution Spaces**:
   - Whenever the target counting problem's solution set is *always non-empty* (e.g., $|\Pi^*(D, D')| \ge 1$ and $|\mathcal{T}^*(D, D')| \ge 1$ because $S_n \neq \emptyset$), a strict many-one parsimonious reduction from unrestricted `#PM(G)` cannot map `#PM(G) = 0` to `0`.
   - **Fix**: State explicitly that hardness holds under reductions **parsimonious on all positive instances** (i.e., $1$-Turing after an $O(k^{2.5})$ Hopcroft–Karp feasibility pre-check that returns `0` when `#PM(G) = 0`), and verify the Appendix proof never hand-waves the infeasible branch.
2. **Ban `"and similarly..."` Hand-Waving in Hardness Proofs**:
   - Never close a proof with `"(and similarly for ED by comparing single-cell probes on a three-value column)"`. PODS referees treat unverified `"similarly"` clauses as proof gaps.
   - **Fix**: Check whether the *exact same* construction already yields the second metric directly (e.g., in the arity-$2$ `#PM(G)` gadget, slack partners $(x_i, \diamond)$ match $x_i$ in column $1$ while target partner $(\star, y_i)$ differs, giving $\mathrm{TP}_{\mathrm{ED}}(\{(i,1)\},\pi) = \mathbb{I}[\pi(i) = j_{y_i}]$ with zero extra columns) and write the 2-line proof explicitly.
3. **Explicit Multi-Metric Threshold Mapping**:
   - When claiming `NP`- or `coNP`-completeness "for Precision, Recall, and $F_1$", explicitly write the monotone map from combinatorial target $K$ to rational threshold $\tau$ for all three metrics (e.g., $\tau_{\mathrm{Prec}} = K/|E_G|$, $\tau_{\mathrm{Rec}} = K/G_0$, $\tau_{F_1} = 2K/(|E_G| + G_0)$) once the ground-truth denominator $G_0$ is proven invariant across optimal worlds.
4. **Transparent Concentration / Sampling Constants**:
   - For `FPRAS` / `FPAUS` + Hoeffding bounds, explicitly show the triangle-inequality split between TV-distance bias (e.g., $\le \varepsilon/4$) and empirical-mean sampling deviation (e.g., $\le \varepsilon/2$ at $N = \lceil 2\varepsilon^{-2}\ln(2/\delta)\rceil$), confirming total error $\le 3\varepsilon/4 < \varepsilon$.
5. **Corner-Case Denominator & Parameter Hygiene**:
   - Explicitly state non-empty / positive-denominator preconditions (e.g., $|S_R| \ge 1$, $|\mathrm{Err}(\pi)| \ge 1$ for Recall) and verify `data complexity` (fixed schema arity $m$) vs. `combined complexity` (unbounded $m$) are never conflated.
6. **Information-Theoretic Determinacy Anchoring**:
   - When non-identifiability or ambiguity arises from erased witnesses, explicitly frame it as an **information-theoretic determinacy barrier** (citing Nash–Segoufin–Vianu, *ACM TODS 2010*) rather than a mere algorithmic limitation.
7. **Roman Pre-Setup Before Italic Theorems**:
   - Keep every `\begin{theorem}` at `≤ 10` compound inline formulas with **zero** inline `\sum`, `\prod`, `\frac`, or `\binom`. Pre-define auxiliary sets and pairwise counts in upright Roman prose + a centered display equation right before `\begin{theorem}`.

---

## 2. Reviewer #2 — Algorithms, Operating Regimes & Reproducibility Chair

1. **Native-Prose Operating-Regime Crossovers (Venue-Native `C7`)**:
   - **Do NOT** add an engineering-style `Limitations` / `Threats to Validity` section or mechanical bold `Takeaway (RQ1):` badges (0/8 published PODS papers use them).
   - **DO** include a crisp native `\paragraph{Operating Regimes and Algorithmic Crossovers.}` in the evaluation section naming exact regimes where simpler baselines beat asymptotic/MCMC solvers (e.g., small $|\Pi^*| \le 2{,}000$ where burn-in overhead loses to exact enumeration; acyclic $\vec{G}(\pi^*)$ or $\delta(\bar{D}) > 2\Delta_{\max}$ where a single solve suffices) and exact crossover thresholds where polynomial/FPRAS algorithms win by $10^2\times\text{--}10^3\times$.
2. **Cleanroom Anonymous `reviewer_repo/` Verification**:
   - Replace every hardcoded `/Users/...` path with `Path(__file__).resolve().parent.parent`.
   - Include a 1-command `run_all.sh` (fast theorem verification + JSON receipt verification + vector figure regeneration in `<5s`, plus `--full` for end-to-end re-execution).
   - Actually copy `reviewer_repo/` into an isolated `/tmp/cleanroom_test` directory and run `bash run_all.sh` to verify zero missing internal imports, zero hardcoded paths, zero secrets, and zero author/institution leaks.
   - Ensure Appendix C (`Artifact Reproducibility Summary`) names the exact verbatim filenames in `reviewer_repo/`.
3. **Zero-Overlap Concurrent Submission Hygiene (Path B Protocol)**:
   - When a concurrent empirical manuscript is under review at another venue, enforce 100% separation in title, conceptual terminology, theorems, algorithms, tables, figures, and scripts (zero shared CSVs or benchmark audit numbers), keep public author GitHub repos private during review, and prepare a transparent confidential note to the PC Chair(s).
4. **Bibliography `0% arXiv` Published-Venue Rule**:
   - Replace every `arXiv` note for papers already published in *PACMMOD / PODS*, *TODS*, *SIGMOD*, or *VLDB* with their verified official ACM/publisher DOIs.

---

## 3. Reviewer #3 — Visual Geometry, Typography & Page-Budget Chair

1. **Automated Vector Figure Box-Overflow Audit (`scripts/figure_overlap_audit.py`)**:
   - **Never rely solely on zoomed-out page thumbnails!** Rounded-box schematic panels (`FancyBboxPatch` / Matplotlib `bbox`) frequently suffer horizontal text overflow where wide math expressions like `$\Pi^*(\nu(D),\nu(D'))$` cross the left/right border and collide with incoming arrowheads.
   - Run `python3 write-pods/scripts/figure_overlap_audit.py <figures_dir>` on every figure PDF to assert **0 horizontal box overflows (`min(pad_l, pad_r) >= 0`)**, then visually inspect every figure page at **≥ 155 DPI**.
2. **Takeaway-First Captions & Tabular Polish**:
   - Every table and figure caption must open with a concrete claim (`≤ 28–30` words for tables), unify decimal precision per column, mark fastest (**bold**) and second-fastest (**underline**) in comparison tables, and explain in prose why specialized solvers outrun general-purpose ones.
3. **Human PODS Cadence & Zero AI-Smell**:
   - Maintain mean sentence length **`19.9–26.4w` (SD `11.5–15.0w`)**, **`0.00/1K` AI-tics**, **`0` em-dashes**, **`0` Overfull/Underfull `\hbox`**, and **exact `≤ 15.00` main-body pages** (`References` starting on Page 15 or immediately at the top of Page 16 with **0 lines of body text** on Page 16).
4. **Terminology Uniformity**:
   - Scrub stray systems jargon (e.g., `"benchmark pair"` → `"instance pair"`) inside formal theorem statements.
