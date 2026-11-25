---
name: "write-pods"
description: "Deep formal-theory architecture, visual/tabular craft, and human writing guide for ACM PODS (Symposium on Principles of Database Systems, PACMMOD acmsmall single-column, <= 15.0 body pages excluding unlimited references and unlimited appendix, strict double-anonymous). Empirically distilled from full-text and page-level visual dissection of 8 officially accepted PODS 2024–2027 papers (Karmakar et al. PODS '24, Kolaitis et al. PODS '25, Esmailpour et al. PODS '25, Fan-Koutris-Roy PODS '25, Lin-Nguyen-Woodruff PODS '26, Surianarayanan-Kumar-Sintos PODS '26, Liu-Zhang PODS '26, Nakos-Ngo-Panayi PODS '27 C1). Enforces framed PROBLEM/INPUT/OUTPUT boxes, Data-vs-Combined Complexity dichotomies, CQA-style Certain/Possible semantics, numbered Example & Lemma scaffolding, Fan-Koutris-Roy concrete mathematical schematics, dedicated single-topic booktabs tables, 14.5–15.0p body completeness, and zero AI-smell/self-negation."
---

# Writing for ACM PODS: Deep Theoretical Craft, Visual/Tabular Rigor & Human Voice (`write-pods`)

Grounded in direct full-text and visual page dissection of **8 officially accepted PODS 2024–2027 papers** (`references/absorbed-pods-papers.md` and `references/pods-visual-and-depth-anatomy.md`) plus the live **PODS 2027 Call for Research Papers**.

## Language Convention
- Everything reviewers see (manuscript prose, problem boxes, theorems, proofs, captions, appendix): **formal academic English**.
- Strategy memos, deep review reports, and revision closure tables for the author: **Simplified Chinese (简体中文)**.

## 1. Official PODS 2027 Hard Constraints
- **Document Class**: `\documentclass[acmsmall,review,anonymous]{acmart}` + `\acmJournal{PACMMOD}`.
- **Length**: **Strictly ≤ 15.0 pages main body** (aim for **14.5–15.0 pages** — neither spilling onto Page 16 nor under-filling at ≤ 13.5 pages), plus **unlimited References** and **unlimited clearly marked Appendix**.
- **Strict Double-Anonymous**: Omit author names/institutions; third-person self-citations; zero acknowledgements, grants, or author-linked public repository URLs; empty PDF `/Author` metadata.

## 2. Seven Mandatory Pillars of Genuine PODS Depth (Eliminating "Thin / Superficial Draft" Smell)

1. **Framed Computational Problem Boxes (`PROBLEM / INPUT / OUTPUT`)**:
   - Follow `Karmakar et al. (PODS '24, pp. 3, 5)` and `Kolaitis et al. (PODS '25, p. 6)`: showcase every core decision, certification, extremal-evaluation, and counting problem in a bordered `\fbox` / `problembox` with explicit `PROBLEM`, `INPUT`, and `OUTPUT` fields (at least **2–4 problem boxes** per paper).
2. **Data Complexity vs. Combined Complexity & Complete Dichotomies / Trichotomies**:
   - Follow `Kolaitis et al. (PODS '25, §4)`: explicitly distinguish **data complexity** (fixed schema arity $m = O(1)$) from **combined complexity** (unbounded $m$), and classify tractability across all parameter regimes (`m = 1` vs. `m >= 2`, bounded vs. unbounded domain $|\mathcal{V}|$, exact vs. $\varepsilon$-perturbed). Never leave obvious parameter corners unanalyzed!
3. **Certain vs. Possible Semantics over Repair / Alignment Worlds**:
   - Connect directly to PODS CQA heritage (`Arenas–Bertossi–Chomicki '99`, `Kolaitis et al. '25`): when multiple optimal worlds exist (e.g., $\Pi^*(D, D')$), formalize and characterize **certain ($\min$)** and **possible ($\max$)** evaluation scores alongside world-counting complexity!
4. **Numbered `\begin{example}` Thread & `\begin{lemma}` Scaffolding**:
   - Include **≥ 3–5 numbered `\begin{example}` environments** tracing concrete relational instances step-by-step and **≥ 3–6 `\begin{lemma}` environments** isolating reusable structural invariants (LP complementary slackness, degree-constrained orientation gadgets, perturbation Lipschitz bounds) rather than jumping abruptly from `Definition` to `Theorem`.
5. **Concrete Mathematical Schematics (`Fan–Koutris–Roy PODS '25 Fig. 1` Style)**:
   - Never draw generic pastel PowerPoint flowcharts! Figure 1 must depict **actual concrete relational tuple grids, cost matrices with dual potentials $(u_i, v_j)$, tight residual digraphs with SCCs, and exact algebraic values** that a reader can check by hand.
6. **Dedicated, Single-Purpose `booktabs` Tables (`Karmakar et al. '24`, `Surianarayanan et al. '26`)**:
   - Never cram two unrelated topics side-by-side into one hybrid table! Give each conceptual or experimental family its own clean, self-contained table with unified precision, explicit regime/complexity columns, and numbered analytical observations `(1)–(5)` in the prose (`Karmakar et al. PODS '24 p. 16`).
7. **Human PODS Cadence & Zero Self-Sabotage (`0/8` `Threats to Validity` / `Limitations`)**:
   - Mean sentence length **20–26 words** (SD 11–15), em-dashes **≤ 0.6/1K**, AI clichés **≤ 0.35/1K**, zero trailing `□` tofu glyphs, and complete line-by-line proofs in the body + Appendix.

## 3. Automated Audit Script
```bash
python3 write-pods/scripts/pods_human_craft_audit.py <paper_dir_or_main.tex> --pdf <main.pdf>
```
Verifies format, double-anonymous hygiene, 14.2–15.0p body completeness, presence of framed `PROBLEM` boxes, `\begin{example}` & `\begin{lemma}` scaffolding, zero hybrid crammed tables, and human PODS stylometrics (`0 FAIL, 0 WARN`).
