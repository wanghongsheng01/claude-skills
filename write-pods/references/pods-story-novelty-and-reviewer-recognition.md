# PODS Story Novelty & Reviewer Recognition: How Accepted Evaluation/Measure Papers Win Over Skeptical PC Members

> **Distilled from 15 Officially Accepted PODS & Joint DB-Theory Papers (2018–2027)**:
> - **Repairs & Inconsistency Measures**: Livshits, Kimelfeld, Roy (*PODS '18 / TODS '20*, `1712.07705`); Livshits, Ilyas, Kimelfeld, Roy (*SIGMOD '21*, `1904.06492`); Calautti, Livshits, Pieris, Schneider (*PODS '22*, `2204.10592` & `2112.09617`); Kolaitis, Pardal, Virtema, Wijsen (*PODS '25*, `2412.11661`).
> - **Quantitative Responsibility & Evaluation Scores**: Bienvenu, Figueira, Lafourcade (*PODS '25*, `2503.22358` & *PODS '24*, `2312.14529`); Karmakar, Monet, Senellart, Bressan (*PODS '24*, `2401.06493`).
> - **Incomplete Databases & Numerical Intervals**: Arenas, Barceló, Monet (*PODS '20*, `1912.11064`); Console, Libkin, Peterfreund (*PODS '23*, `2210.15395`).
> - **Noisy/Mismatched Data & Discovery Foundations**: Liu & Zhang (*PODS '26*, `2603.11216`); Esmailpour, Galhotra, Raychaudhury, Sintos (*PODS '25*, `2503.21235`); Surianarayanan, Kumar, Sintos (*PODS '26*, `2509.16194`); Lin, Nguyen, Woodruff (*PODS '26*, `2506.07342`); Fan, Koutris, Roy (*PODS '25*, `2504.08914`).

---

## 1. The Two Deadly Novelty Objections at PODS (Even When Proofs Are Correct!)

When a paper studies **evaluation, scoring, data quality, or inconsistency measurement**, technical correctness and CQA terminology alone are **not enough** to secure a champion (`+2` Strong Accept) on the PODS Program Committee. Skeptical senior reviewers routinely raise two fatal novelty objections:

1. **The "Folklore Subroutine" Objection**:
   > *"The authors use Hungarian matching, Tarjan's SCCs, Valiant's permanent, Jerrum–Sinclair–Vigoda, Mann–Whitney rank sums, and min-max scaling. Each subroutine is classical; where is the non-obvious database-theoretic insight?"*
2. **The "Four Mini-Notes in One Envelope" (Module-Stacking) Objection**:
   > *"The framework defines a tuple $\mathcal{C} = (\mathcal{I}, \nu, \sigma, \mu)$ of four pipeline stages, but each section analyzes its own stage independently. Why is this one unified theory rather than four small observations bundled together?"*

---

## 2. Five Story-Novelty Engines Used by Accepted PODS Papers

Reverse-engineering how accepted PODS papers preempt both objections reveals **five concrete story-construction engines**:

### Engine 1 — The Explicit Broken-Premise Hook (打破经典隐含公理)
Every memorable PODS paper opens by naming **one foundational assumption silently shared by 20+ years of database theory**—and showing what happens the moment that assumption is removed:
- *Exemplar (`Livshits–Kimelfeld–Roy PODS '18`, p. 2)*: Classical optimal repair theory explicitly states: *"Table records have identifiers, as we wish to be able to determine easily which cells are updated in a repair."*
- *Exemplar (`Console–Libkin–Peterfreund PODS '23`, p. 1)*: Classical CQA returns Boolean certain/possible answers, which collapse to trivial `(-\infty, +\infty)` or empty answers on incomplete numerical aggregates.
- *Exemplar (`Bienvenu et al. PODS '25`, p. 1)*: Drastic `0/1` Shapley encoding makes even trivial conjunctive queries `FP^{#P}`-complete and sensitive to unrelated facts.
- **Actionable Rule**: In `Abstract` Sentence 1–2 and `§1` Paragraph 1, explicitly contrast classical repair/CQA's **witnessed-state premise** (persistent tuple IDs, canonical value equality, strict total orders) against the **quotiented artifact reality** where serialization erases those witnesses.

### Engine 2 — The Counter-Intuitive Complexity Inversion ("The PODS Paradox")
PODS reviewers champion papers whose headline theorem **reverses naive complexity intuition**:
- *Exemplar (`Karmakar et al. PODS '24`)*: Combining probabilistic uncertainty (`#P`-hard) with Shapley coalitions (`#P`-hard) seems doubly intractable, yet expected Shapley reduces in polynomial time to plain probabilistic query evaluation (`EScore ==_P EV`)!
- *Exemplar (`Arenas–Barceló–Monet PODS '20`)*: Counting completions looks simpler than counting valuations, yet `#Val` is always in `#P` with an `FPRAS`, whereas `#Comp` leaves `#P` (`SpanP`-complete) and loses approximability!
- **Actionable Rule**: Elevate **Complexity Inversion** to the centerpiece of your Introduction:
  - In classical keyed repairs, CQA (`min` over repairs) is `coNP`-complete.
  - When tuple IDs are erased, exact world counting (`#OptAlign`, parsimonious `#OptTarget`) and exact average-case evaluation (`ExpEval`) become `#P`-hard already at fixed schema arity $m = 2$—**yet worst-case/best-case CQA evaluation (`CertEval`/`PossEval`) for cell-repair Precision/Recall/$F_1$ becomes deterministically polynomial** ($O(n^2 m + n^3)$ unit Hamming; $O(n^2 m + n^3 \log(nm))$ weighted costs), while `ExpEval` admits an `FPRAS`!

### Engine 3 — The Anti-Folklore Shield: Proving the Exact Structural Frontier Where Polynomial Time Breaks!
Why does a PODS reviewer respect a polynomial-time algorithm built from matching/LP? **Only when you prove the exact syntactic/structural dichotomy explaining WHY it works and WHERE `NP`/`coNP`-hardness immediately returns!**
- *Exemplar (`Livshits–Kimelfeld–Roy PODS '18`)*: `OptSRepair` uses simple greedy/matching simplifications—what made it a landmark PODS paper was proving **soundness AND completeness of the frontier**: the exact moment simplification stops, the problem becomes `APX`-complete (`NP`-hard)!
- *Exemplar (`Kolaitis et al. PODS '25`)*: Semiring minimization rewrites cleanly when the attack graph is acyclic, and becomes `NP`-hard to even approximate on strong cycles!
- **Actionable Rule**: Never state a cubic/polynomial evaluation theorem (`CertEval` $\in \mathsf{P}$) in isolation! Pair it immediately with its **Matching Intractability Boundary**:
  - Prove that polynomial tractability of `CertEval`/`PossEval` hinges on **row-separability (unary tuple decomposition)** over the Birkhoff face $G_{\mathrm{tight}}$;
  - The instant an evaluation metric couples **pairs of rows** (e.g., pairwise entity co-reference $F_1$ or a 2-atom self-join query over target completions $\mathcal{T}^*(D, D')$), `PossEval` becomes **`NP`-complete** and `CertEval` becomes **`coNP`-complete in data complexity already at fixed arity $m = 2$** (even when $G_{\mathrm{tight}}$ is a disjoint union of $2 \times 2$ blocks)!

### Engine 4 — Cross-Operator Non-Commutativity (代数耦合铁证，彻底击碎“四模块拼盘感”)
To prove that a multi-component abstraction $\mathcal{C} = (\mathcal{I}, \nu, \sigma, \mu)$ is **one indivisible mathematical object** rather than four independent chapters (`ccfa-track-novelty-and-anti-stacking` Move 2–4):
- Prove an explicit **Cross-Axis Non-Commutativity Theorem** showing that two axes interact destructively when composed in different orders!
- Specifically, between minimum-change correspondence ($\mathcal{I}_{\mathrm{min}}$) and value normalization ($\nu$):
  - Even when $\nu$ is globally idempotent ($\nu^2 = \nu$) and preserves every diagonal error coordinate ($E_\nu = E$), **$\mathcal{I}_{\mathrm{min}}$ and $\nu$ fail to commute**: $\Pi^*(\nu(D), \nu(D'))$ can strictly enlarge a unique optimum $\Pi^*(D, D') = \{\pi_1\}$ (shattering correction $F_1$ from $[1, 1]$ to $[0, 1]$) **or flip a unique optimum to a completely disjoint bijection** ($\Pi^*(D, D') \cap \Pi^*(\nu(D), \nu(D')) = \emptyset$)!
  - Then characterize the exact condition (**cross-row disequality invariance** on $\mathrm{adom}(D') \times \mathrm{adom}(D)$) under which $\Pi^*(\nu(D), \nu(D')) = \Pi^*(D, D')$.

### Engine 5 — Structural Invariant Replacement ("Why the Naive Quantity Is Wrong")
Show that the quantity practitioners naturally worry about is the **wrong mathematical invariant**, and replace it with the exact structural invariant:
- *Naive belief*: "Ambiguity grows with $|\Pi^*(D, D')|$." $\to$ *Truth*: $|\Pi^*| = 256$ under duplicate-tuple quotients has $|\mathcal{T}^*| = 1$ and **zero** score spread, whereas $|\Pi^*| = 2$ on one alternating cycle splits detection $[1, 1]$ from correction $[0, 1]$; the exact invariant is **Tarjan SCC projection onto cell targets**.
- *Naive belief*: "Idempotent string normalization on load is harmless." $\to$ *Truth*: Direct scoring fails by $|K_\nu|/|E|$ on $E$, while materialized round-trip scoring depends strictly on idempotence over the **untouched complement $E^c$**.
- *Naive belief*: "Tie-breaking jitter in ROC-AUC is random numerical noise." $\to$ *Truth*: Exact closed interval of width $(n_+ n_-)^{-1}\sum_j p_j q_j$, vanishing iff every score level is **label-pure**.

---

## 3. Pre-Submission Story-Novelty Checklist for PODS Authors & Reviewers

1. **First-Paragraph Litmus Test**: Does Paragraph 1 name the exact classical premise (e.g., persistent tuple IDs in repair theory) that breaks, rather than listing benchmark filenames?
2. **Headline Paradox Test**: Can a PC member state the paper's central counter-intuitive theorem in **one memorable sentence** at the PC meeting?
3. **Anti-Folklore Boundary Test**: For every polynomial-time algorithm using classical combinatorial primitives, is there a matching **hardness frontier** showing where polynomial time breaks (e.g., row-separable $\in \mathsf{P}$ vs. pairwise-coupled $\mathsf{NP}/\mathsf{coNP}$-complete at $m = 2$)?
4. **Anti-Collage Coupling Test**: Is there an explicit **cross-axis interaction / non-commutativity theorem** proving that the axes of the model cannot be analyzed in isolation?
