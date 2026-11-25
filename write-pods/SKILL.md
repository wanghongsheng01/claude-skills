---
name: "write-pods"
description: "Human-craft writing, formal-theory architecture, and anti-AI-smell guide for ACM PODS (Symposium on Principles of Database Systems, published in PACMMOD, ACM acmsmall single-column, <= 15 body pages excluding references and unlimited appendix, strict double-anonymous). Empirically distilled from 8 officially accepted PODS 2024–2027 papers (Karmakar et al. PODS '24, Kolaitis et al. PODS '25, Esmailpour/Distribution-Aware Dataset Search PODS '25, Fan et al. PODS '25, Lin-Nguyen-Woodruff PODS '26, Surianarayanan-Kumar-Sintos PODS '26, Mismatch Ambiguity PODS '26, Nakos-Ngo-Panayi PODS '27 C1) and unified with historical claude-skills (ccfa-human-readable-math-and-proof, ccfa-track-novelty-and-anti-stacking, sigmod-human-writing-craft, write-dasfaa). Use when framing, drafting, proving, or polishing any PODS submission."
---

# Writing for ACM PODS: Formal Craft, Theory-Plus-Evidence Architecture & Anti-AI-Smell (`write-pods`)

Grounded in direct empirical measurement of **8 officially accepted PODS 2024–2027 papers** (`references/absorbed-pods-papers.md`) and the live **PODS 2027 Call for Research Papers** (verified 2026-11-25).

## Language Convention
- Everything reviewers see (manuscript prose, theorems, proofs, captions, appendix): **formal academic English**.
- Reports, theory plans, mock reviews, and checklists for the author: **Simplified Chinese (简体中文)**.

## 1. Official PODS 2027 Hard Constraints (Verified 2026-11-25)
- **Document Class**: `\documentclass[acmsmall,review,anonymous]{acmart}` (single-column PACMMOD format).
- **Length**: **≤ 15 pages main body**, excluding references (unlimited) and a clearly marked **Appendix** (unlimited, incorporated at submission time, read at PC discretion).
- **Double-Anonymous**: Omit author names and affiliations; cite authors' own prior work in third person; **no acknowledgements, grant numbers, or links to submitted papers in public repositories**; strip PDF `/Author` metadata.
- **Submission Portal**: EasyChair (`https://easychair.org/conferences/?conf=pods2027`).

## 2. How Real Human PODS Authors Architect a Paper (From 8 Accepted Papers)
1. **Unify under ONE crisp mathematical model before proving anything (`§2 Preliminaries / Model`).**
   - `Kolaitis et al. (PODS '25)` defines semiring-annotated repairs and consistent answers cleanly before the main dichotomy.
   - `Karmakar et al. (PODS '24)` introduces expected Shapley-like scores and d-D circuits in §2, proves complexity equivalence in §3, gives the tractable algorithm in §4, and validates in ProvSQL in §6.
2. **Every main theorem must be genuinely non-trivial — NEVER restate an `if`-branch.**
   - PODS reviewers prize four theorem archetypes:
     1. **Exact Characterizations (`if and only if`)**: e.g., attack-graph acyclicity, tight-edge SCC identifiability, exact commutativity criteria;
     2. **Complexity Separations / Dichotomies**: e.g., $\mathsf{P}$ vs. $\mathsf{NP}$-hard or $\#\mathsf{P}$-complete (with full self-contained reductions);
     3. **Tight Upper & Lower Bounds / Separation Thresholds**: matching constructive witnesses proving bounds cannot be improved;
     4. **Constructive Polynomial-Time Algorithms**: strictly improving asymptotic complexity over naive baselines (e.g., $O(n^3)$ vs. $O(n^5)$ or $O(n^2 2^n)$), with complete correctness and complexity proofs.
3. **15-Page Body + Unlimited Appendix Proof Discipline**:
   - State every Definition, Theorem, Proposition, and Corollary completely in the 15-page body.
   - Keep **short, insightful proofs and crisp proof sketches (highlighting the key gadget, potential, or invariant)** in the main body; place full case-exhaustive proofs and auxiliary lemmas in a cleanly hyperlinked Appendix (`Proof in Appendix~\ref{app:...}`).
4. **Empirical Validation in a PODS Paper (`Karmakar et al. PODS '24 §6`, `Lin–Nguyen–Woodruff PODS '26 §9`)**:
   - PODS explicitly welcomes *"experimental work that sheds light on the scientific foundations"* and *"rigorous analysis of important industry artifacts"*.
   - Structure experiments as **verification of theoretical boundaries, tightness witnesses, and algorithmic scalability** — NOT as a sprawling systems benchmark dump. Aim for ~2–3 pages (15–20% of the 15-page body).
5. **Human PODS Stylometric Baseline (Measured Across 8 Papers)**:
   - **Sentence length**: Mean **19.9–26.4 words**, SD **11.5–15.0 words** (natural burstiness).
   - **Em-dashes**: **≤ 0.8 / 1K words** (5/8 papers have `≤ 0.21/1K`).
   - **AI clichés**: **≤ 0.35 / 1K words** (median `0.20/1K`).
   - **`Threats to Validity` / `Limitations` headings**: **0 / 8 (0%)**! Express assumptions cleanly inside Definitions and Theorem hypotheses; close Conclusion with 1–2 crisp open theoretical problems.
   - **Formal readability (`ccfa-human-readable-math-and-proof`)**: Pre-define notation before `\begin{theorem}`; keep theorem statements `≤ 9` lines; place `\sum`, `\frac`, and multi-step chains in centered display equations; use clean proof endings without awkward floating tofu QED boxes.

## 3. Automated Audit
Run on every PODS draft before compilation delivery:
```bash
python3 write-pods/scripts/pods_human_craft_audit.py <paper_dir_or_main.tex> [--pdf <main.pdf>]
```
Must exit with **`0 FAIL`**.
