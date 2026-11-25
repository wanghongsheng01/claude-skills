---
name: "review-dasfaa"
description: "Simulated DASFAA 2027 Program Committee review and deep pre-submission improvement protocol. Absorbs review-icde, review-pvldb, results-presentation-review (Deng S01-S11), paper-presubmission-review (A-H), sigmod-human-writing-craft, and manuscript-writing-review, calibrated against 8 real published DASFAA 2024-2026 papers (including DASFAA 2026 Best Paper DynamicPO). Runs a strict desk screen, three independent human-reviewer personas (DB Systems/Formal, Empirical/SOTA, Generalist Human-Craft & AI-Smell Skeptic), a mandatory Self-Negation & Over-Honest AI Disclosure Audit Appendix, a Senior PC Meta-Review, and a concrete Revision Closure Table. Use before submitting any DASFAA paper."
---

# Simulated DASFAA PC Review & Deep Revision Protocol (`review-dasfaa`)

Use after `write-dasfaa` and before `submit-dasfaa`. This skill replaces shallow surface checks with a **rigorous, human-reviewer-perspective simulation** anchored in our 8-paper DASFAA 2024–2026 corpus (`write-dasfaa/references/absorbed-dasfaa-papers.md`) and historical `review-icde` + `review-pvldb` + `results-presentation-review` (S01–S11) + `paper-presubmission-review` lessons.

## Language Convention
- Simulated reviewer reports and meta-review: **English** (matching actual DASFAA CMT reviews), accompanied by an **author-facing executive summary, Self-Negation Audit Appendix, and Revision Closure Table in Simplified Chinese (简体中文)**.

## 1. Mandatory 5-Stage Review Procedure

### Stage 1 — Desk-Reject Screen (`assets/desk_screen.md`)
Verify hard DASFAA 2027 CFP requirements before reading science:
1. Springer LNCS A4 format (`llncs`), `splncs04` references.
2. **Strictly ≤ 16 pages total INCLUDING references and appendices.**
3. **Abstract ≤ 200 words.**
4. **Strict double-blind anonymity**: zero author names, affiliations, personal GitHub handles (`wanghongsheng01`), identifying acknowledgments, or non-empty PDF `/Author` metadata.
5. **Core DASFAA database/data-management scope**: problem framed as a data-management / query / contract / data-quality / integration challenge with solid DB-venue lineage (SIGMOD/VLDB/ICDE/DASFAA/TKDE).

### Stage 2 — First-Two-Minutes Presentation & SOTA-at-a-Glance Pass (`results-presentation-review` S01–S11 + `paper-presubmission-review`)
Evaluate what a busy DASFAA PC member sees in the first 2 minutes:
- **Title & Fig. 1**: Does Fig. 1 appear on pp. 1–3 (`8/8` of published DASFAA papers) and visually convey the exact gap vs. prior work + core mechanism?
- **Tables (S01–S06, A1–A5)**:
  - **Bold best** + **underline second-best** on comparison tables (ties share the mark, even when a baseline wins).
  - **Best/2nd count row** or visually separated **Avg./Summary row** (`\midrule`) where ups/downs exist across rows.
  - **Claim-first, short captions** (table captions ~2 lines, ≤ 35–40 words; figure captions ≤ 60 words opening with the takeaway).
  - Unified decimal precision per metric; one unit per column; pure `booktabs` + `\cmidrule(lr)` (zero vertical rules `|`); no empty "experiment-log" tables.
- **Win/Loss Analysis (S07, S10)**: Every cell where a baseline ties or wins has a **one-time, data-backed 4-step explanation** (`fact → mechanism → regime → practical choice rule`) right next to its table.

### Stage 3 — Mandatory Over-Honest AI Disclosure & Self-Negation Pass (反 AI 过度诚实自我否定专审)
Run `python3 ../write-dasfaa/scripts/dasfaa_human_craft_audit.py <paper_dir> --pdf <paper.pdf>` AND manually audit every paragraph of Abstract, Introduction, Method, Evaluation, Discussion, and Conclusion against `write-dasfaa` §4:
- **Flag every suicidal / over-honest AI confession**, including:
  - Any `Threats to Validity` or `Limitations` or `Where we fail` heading (`0/8` in DASFAA method/system papers!).
  - Any sentence undermining your own evaluation (`"only confirms the implementation"`, `"validates the implementation, not the contract"`, `"written with the live export in view"`, `"built after the current rules, so they test documented behaviour rather than generalization"`, `"remain the weakest parts"`, `"is a single small pilot"`, `"neither measures end-user utility"`, `"inviting G4 claims"`, `"on a smaller sample"`).
  - Any negative concession in the Abstract or Conclusion (`0/8` in DASFAA), e.g., `"at the cost of repairing about half as many tasks"`.
  - Any self-inflicted objection (`"A natural objection is..."`) or apologized-for design cost (`"is a real burden"`).
  - Any AI prose tells (`crucially`, `notably`, `importantly`, `comprehensive`, em-dash chains, bullet walls, robotic uniform sentence length).
- **Produce the Self-Negation Audit Appendix** (Chinese, for the author — NEVER written into the manuscript!):
  - Every flagged sentence gets an exact tag: `删去冗余` / `重新框定为范围或取舍` / `移位置` / `补强机理分析` / `保留（附隐瞒风险说明）`.

### Stage 4 — Independent 3-Reviewer Simulation + Meta-Review (`assets/review_form.md`)
Simulate three distinct, tough, realistic human DASFAA PC members (each writing independently without author excuses):
- **Reviewer 1 (Database Systems & Formal Rigor):** Attacks problem novelty, formal definitions/theorems, soundness boundaries, complexity, and positioning vs. SIGMOD/VLDB/ICDE/DASFAA work.
- **Reviewer 2 (Experimental Methodology & SOTA Skeptic):** Attacks baselines, dataset breadth/public-data sufficiency, ablation attribution, cost/overhead accounting, and any unexplained non-first cells or perceived evaluation circularity.
- **Reviewer 3 (Human Craft, Narrative & AI-Smell Skeptic):** Reads like a seasoned human researcher comparing the draft directly against accepted human DASFAA papers (`DynamicPO`, `OLLA`, `Trans-RAG`, `MAKGED`). Flags AI-smell, robotic pacing, over-honest self-sabotage, thin causal insight, and Conclusion weakness.
- **Senior PC Meta-Reviewer:** Synthesizes the 3 consensus strengths, top 3–5 rejection risks, separates **writing/framing fixes** from **evidence/analysis fixes**, and issues a pre-revision verdict (`Accept / Weak Accept / Borderline / Weak Reject`).

### Stage 5 — Deep Revision Closure & Re-Verification
1. Apply ALL feasible revisions directly to the LaTeX source (and regenerate any modified figures/tables cleanly) — preserving **100% of verified numbers, losing table cells, citations, and algorithms**.
2. Compile cleanly (`0` errors, `0` Overfull > 1pt, strict `≤ 16` pages A4, `0` `□` QED boxes, `0` double-blind leaks).
3. Re-run `dasfaa_human_craft_audit.py` + `manuscript-writing-review` + `ccfa-visual-table-ref-mastery` linters AND inspect rendered PNGs of every modified page.
4. Close with a **Revision Closure Table** (`审稿意见编号 → 原文问题与行号 → 具体修改方案 → 修改后验证结果`).
