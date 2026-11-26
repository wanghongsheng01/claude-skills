# PODS Evaluation, Measures & Data-Quality Foundations: Author Mindset, Mother-Tongue Positioning, and Acceptance Bar

> **Empirical Corpus Base (13 Officially Accepted ACM PODS Papers, 2020–2027)**:
> - **Responsibility, Scoring & Quantitative Evaluation Measures**: Bienvenu, Figueira, Lafourcade (*PODS '25*, `2503.22358`); Bienvenu, Figueira, Lafourcade (*PODS '24*, `2312.14529`); Karmakar, Monet, Senellart, Bressan (*PODS '24*, `2401.06493`).
> - **Incomplete Databases, Valuations vs. Completions & Numerical Intervals**: Arenas, Barceló, Monet (*PODS '20*, `1912.11064`); Console, Libkin, Peterfreund (*PODS '23*, `2210.15395`).
> - **Consistent, Operational & Counting Repairs**: Kolaitis, Pardal, Virtema, Wijsen (*PODS '25*, `2412.11661`); Calautti, Livshits, Pieris, Schneider (*PODS '22*, `2204.10592` & `2112.09617`).
> - **Data Quality, Mismatch Ambiguity & Discovery Foundations**: Liu & Zhang (*PODS '26*, `2603.11216`); Esmailpour, Galhotra, Raychaudhury, Sintos (*PODS '25*, `2503.21235`); Surianarayanan, Kumar, Sintos (*PODS '26*, `2509.16194`); Lin, Nguyen, Woodruff (*PODS '26*, `2506.07342`); Fan, Koutris, Roy (*PODS '25*, `2504.08914`); Nakos, Ngo, Panayi (*PODS '27 C1*, `2605.30564`).

---

## 1. Why "Evaluation" Papers Fail at PODS — And How Accepted Authors Conceive Them

A recurring rejection mode at PODS occurs when authors submit a paper about **benchmarking, scoring, or data-quality evaluation** written in the narrative dialect of **machine-learning reproducibility or software-engineering pipeline auditing** ("Script A swaps columns; Library B strips whitespace; Repository C changes `k-NN` AUC"). Even if the paper contains correct proofs, a PODS Program Committee member immediately asks:

> *"Is this a foundational principle of database systems, or is it a collection of engineering hygiene bugs in Python benchmark scripts?"*

Reverse-engineering accepted PODS papers in evaluation, inconsistency measurement, noisy/mismatched data, and data discovery reveals **six decisive differences in author mindset, starting point, and scientific completeness**:

### Law 1 — Community Mother-Tongue Alignment (审稿人建议 0.1)
Accepted PODS authors **never** frame their core object as a "Python evaluation wrapper" or "ML benchmark leaderboard." They map the real-world evaluation phenomenon directly onto **canonical database-theory objects** in the very first paragraph:

| Engineering / ML-Evaluation Dialect (Avoid as Primary Framing) | Native PODS Mother-Tongue Dialect (Mandatory Primary Anchor) | Canonical PODS Lineage |
|---|---|---|
| "CSV files exported without row-ID sidecars" | **Incomplete relational representations with unmarked tuple identities** | Imieliński–Lipski (*JACM '84*); Arenas–Barceló–Monet (*PODS '20*) |
| "Different row permutations vs. different clean cell values" | **Valuations** ($\pi \in \Pi^*$) vs. **Completions** ($\tau_\pi \in \mathcal{V}^{n\times m}$) | Arenas–Barceló–Monet (*PODS '20*); Console–Libkin–Peterfreund (*PODS '23*) |
| "Minimum / maximum / average F1 across ambiguous row matchings" | **Consistent (Certain), Possible, and Uniform Probabilistic/Expected Evaluation** ($\underline{\mu}, \overline{\mu}, \mathbb{E}_{\Pi^*}[\mu]$) | Arenas–Bertossi–Chomicki (*PODS '99*); Calautti–Livshits–Pieris (*PODS '22*); Karmakar et al. (*PODS '24*) |
| "String loader normalization vs. repair dictionary lookup" | **Endomorphism commutativity & materialized round-trip idempotence** ($\nu \circ \mathsf{Mat}$ vs. direct lookup) | Fagin–Kolaitis–Popa–Tan (*TCS '05*); Fagin–Kolaitis–Nash–Popa (*PODS '08*) |
| "Event-log column order swap `(cell, clean, dirty)`" | **Operational repairing sequences vs. state-based repairs** | Calautti–Livshits–Pieris–Schneider (*PODS '22*, Operational CQA) |
| "Different `sort` implementations changing ROC-AUC on tied scores" | **Consistent / possible Mann–Whitney functionals over linear extensions of a weak order** | Fagin et al. (*PODS '04*); Kimelfeld / Soliman–Ilyas uncertain rankings |
| "Rescaled / rounded duplicate outlier datasets across repos" | **Relational instance isomorphism modulo column-affine automorphisms & $\varepsilon$-imprecision** | Console–Libkin–Peterfreund (*PODS '23*); Liu–Zhang (*PODS '26*) |

### Law 2 — Single Unified Mathematical Ontology (Zero Collage / Zero Orphan Artifacts)
In `Esmailpour et al. (PODS '25)`, `Bienvenu et al. (PODS '25)`, and `Liu & Zhang (PODS '26)`, **100% of the paper** flows from **one unified formal model** introduced in Section 2:
- Every subsequent section studies a mathematically natural projection or complexity question of that single object.
- **Zero Orphan Empirical Artifacts**: Never include a side experiment in the evaluation section (e.g., an unformalized SQL/YAML patching benchmark) that has no formal definition or theorem in Sections 2–5. Every experimental table row must test a specific proved theorem or complexity frontier of the paper.

### Law 3 — The PODS Four-Way Complexity Separation (Certain vs. Possible vs. Exact Counting/Expected vs. Approximate `FPRAS`)
Look at `Arenas–Barceló–Monet (PODS '20)`, `Calautti–Livshits–Pieris–Schneider (PODS '22, '24)`, and `Bienvenu et al. (PODS '25)`:
- Showing that exact world-counting (`#OptAlign`) is `#P`-complete is only **half** of a PODS story.
- A genuine PODS contribution reveals a **structural complexity separation** over the *same* uncertain/inconsistent object, and **closes the approximability question**:
  1. **Support & Identifiability** ($\mathsf{CertIdent}$): Polynomial time ($O(n^2 m + n^3)$).
  2. **Consistent & Possible Evaluation** ($\mathsf{CertEval}_\mu, \mathsf{PossEval}_\mu$): Polynomial time ($O(n^2 m + n^3)$ for unweighted Hamming; $O(n^2 m + n^3 \log(nm))$ fractional matching for arbitrary weighted/additive tuple costs!).
  3. **Exact Counting & Exact Uniform Expected Evaluation** ($\#\mathsf{OptAlign}$, $\#\mathsf{OptTarget}$, $\mathsf{ExpEval}_\mu$): **`#P`-complete / `#P`-hard in data complexity** already at fixed schema arity $m = 2$ (with `#OptTarget` **parsimoniously** `#P`-complete!).
  4. **Approximate Counting & Approximate Expected Evaluation**: Because optimal alignments equal perfect matchings of the unweighted tight bipartite graph $G_{\mathrm{tight}}$ (LP complementary slackness), **Jerrum–Sinclair–Vigoda (*JACM '04*)** yields a **Fully Polynomial-Time Randomized Approximation Scheme (FPRAS / FPAUS)** for $|\Pi^*(D, D')|$ and an $(\varepsilon, \delta)$-approximation scheme for $\mathbb{E}_{\Pi^*}[\mu(R, \pi)]$ across **all** $(m, \mathcal{V})$!

> **Fatal Anti-Pattern Alert**: Never ask in `Conclusion` *"Does $|\Pi^*|$ admit an FPRAS via Markov chains on $G_{\mathrm{tight}}$?"* when complementary slackness already reduces $|\Pi^*|$ to bipartite `{0,1}`-permanent (solved by Jerrum–Sinclair–Vigoda 2004)! PODS reviewers know JSV cold and will penalize leaving a direct corollary as an "open problem."

### Law 4 — Valuations vs. Completions (`Arenas–Barceló–Monet PODS '20` Principle)
In incomplete databases, two distinct valuations of unknowns can produce the **exact same completed relation**. In sidecar-free evaluation:
- A row bijection $\pi \in \Pi^*(D, D')$ is a **valuation** of missing tuple identities.
- The induced clean target table $\tau_\pi \in \mathcal{V}^{n \times m}$ (where $\tau_\pi[i, a] = t_{\pi(i)}[a]$) is the **completion**.
- Separating `#OptAlign` (counting valuations) from `#OptTarget` (counting distinct completions) explains why duplicate clean tuples cause factorial blowup in `#OptAlign` (`\prod |C_p|!`) while `#OptTarget = 1` (exact cell identifiability!), AND yields **parsimonious** `#P`-completeness of `#OptTarget` at fixed arity $m = 2$!

### Law 5 — Pushing Algorithmic Frontiers Beyond Unit Weights ("What If Costs Are Weighted?")
PODS reviewers instinctively test whether a polynomial-time theorem is an artifact of unit weights:
- Under unit-weight cell-Hamming distance, $|\mathrm{Err}(\pi)| = c^*(D, D')$ is constant across $\Pi^*(D, D')$, making $F_1(R, \pi)$ affine in $\mathrm{TP}(R, \pi)$ (`2` Hungarian solves).
- Under **attribute-weighted or general additive row-pair edit costs** $C_{ij}$, $|\mathrm{Err}(\pi)|$ varies across $\Pi^*_C(D, D')$, turning $F_1(R, \pi) = \frac{2\,\mathrm{TP}(R, \pi)}{|S_R| + |\mathrm{Err}(\pi)|}$ into a **linear-fractional objective** over perfect matchings of $G_{\mathrm{tight}}$.
- Rather than punting this to Future Work, prove that Newton–Dinkelbach parametric assignment over $G_{\mathrm{tight}}$ still solves $\mathsf{CertEval}_{F_1}$ and $\mathsf{PossEval}_{F_1}$ exactly in **$O(n^2 m + n^3 \log(nm))$** strongly polynomial time!

### Law 6 — High-Taste Open Problems in Conclusion
Open problems in an accepted PODS paper (`Kolaitis et al. '25`, `Bienvenu et al. '25`, `Arenas et al. '20`) point to **genuinely deep, non-trivial theoretical frontiers**:
1. **Joint Integrity Constraints + Missing Identities**: Certifying consistent repair evaluation when $D$ is constrained by functional or denial dependencies rather than a materialized clean snapshot, or when alignment costs couple multiple rows simultaneously.
2. **Rich Relational Query Evaluation over Alignment Fibers**: Classifying data complexity (`P` vs. `coNP`-complete) of evaluating conjunctive queries $Q(\tau_\pi)$ across optimal alignments $\pi \in \Pi^*(D, D')$.
3. **Beyond Column-Affine Gauge Groups**: Decidability and $\varepsilon$-stability of representation equivalence under general linear, orthogonal, or coordinate-monotone transformations.
