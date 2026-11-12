---
name: "write-vldb"
description: "Writing guide for PVLDB / VLDB research papers (CCF-A; PVLDB Vol. 20 and VLDB 2027). Covers official monthly deadlines (abstract on the 25th of the previous month, full paper on the 1st, 17:00 PT), the 12-page body limit including appendix and acknowledgements but excluding references, single-blind policy, the two-papers-per-author-per-month and twelve-per-year caps, and the requirement to submit an EA&B reproducibility package at initial submission when the paper is an experiment, analysis or benchmark contribution. Presentation rules are Deng S01–S11 and results-presentation-review; structural habits (title, abstract, introduction, RQ takeaways) are cross-referenced from write-icde and are not a fresh full-text census of VLDB 2025–2026 PDFs. Use when drafting, restructuring or polishing a paper for PVLDB or VLDB (写 VLDB / 写 PVLDB / Vol. 20 / EA&B 复现包 / 每月截稿)."
---

# Writing for PVLDB / VLDB (Write-VLDB)

**Re-read the official pages immediately before every submission.** The rules below were checked on **2026-11-12**. If a page disagrees with this file, the official page wins.

- Important dates: https://www.vldb.org/2027/important-dates.html
- Research-track CFP: follow the links from that page (call-for-research-track / submission guidelines for the current volume).
- For ICDE-specific wording, page budgets or EAB title tags, use `write-icde`, `submit-icde` and `review-icde`. **Do not rewrite those skills.**
- For tables and figures, always also apply `results-presentation-review` (S01–S11) and, for English, `academic-latex-polish`.

This skill does **not** claim a new deep-read of a VLDB 2025–2026 accepted-paper sample. Paragraph and caption habits below are transferred from write-icde and Deng’s rules, which are consistent with PVLDB practice but are not a fresh frequency table.

## Language
Manuscript, captions and reviews in **English**. Plans and reports to the author in **Chinese**.

## 1. Official constraints (Vol. 20 / VLDB 2027)

- **Monthly research cycle.** Abstract: 25th of the previous month, 17:00 PT. Full paper: 1st of the month, 17:00 PT. Convert to Beijing time when reporting to the author (PT + 16 hours in standard time; check DST). The last cycle that accepts **new** papers for VLDB 2027 was stated as **2027-03-01 17:00 PT** — confirm on the important-dates page, because the conference may stop accepting new work after a stated month.
- **Length.** Regular research papers: at most **12 pages** of body, **including** appendix and acknowledgements, **excluding** references. Use the official PVLDB / acmart template for the current volume (`vldbproceedings` / the volume’s posted class). Do not steal space with margin or spacing hacks.
- **Blindness.** Single-blind: author block is present. Still do not deanonymize **other** co-submissions or confidential enterprise data.
- **Author caps.** At most **two** papers per author per month, and **twelve** per year (confirm the exact wording on the current CFP; do not exceed it). Scheme A already books January and February slots — do not silently add a third paper in those months.
- **EA&B / reproducibility.** For experiment, analysis and benchmark papers, a **reproducibility package is due at initial submission**, not after acceptance. Declare the official EA&B label if the track requires it. The package must run on public data or a documented generator; enterprise dumps do not belong in the package.
- **Dual submission.** A manuscript under review at PVLDB must not also be under review at TKDE or another venue. After a VLDB reject, wait for the venue’s own resubmission rules.

## 2. Framing

PVLDB wants a **data-management** problem: a query or operator, a cost or correctness constraint, a guarantee or a clearly scoped empirical claim. Pure ML methods without a data-system interface are a poor fit. Industrial experience belongs in SIGMOD Industrial (`write-sigmod-industrial`) unless the contribution is a generalizable system or algorithm with public evidence.

## 3. Title, abstract, introduction

Follow `write-icde` §§2–4 as a starting structure (they were measured on ICDE, not VLDB):

- Title: technical paradigm or hard setting first; EA&B papers use the official label, not a homemade synonym.
- Abstract: context → shared false assumption → “We present X” → insight → 2–3 components → evaluation scope → 1–2 headline numbers with the **same wording** as the body. No citations. Do not put a loss sentence at the end of the abstract (Deng / write-icde limitations guide).
- Introduction: scenario with a concrete number; existing work and its shared assumption; Figure 1 as a real measurement that breaks the assumption; challenges C1–C3; mapping from challenges to components; 3 contributions with section numbers; the last contribution holds experiments and headline results plus artifact availability. Answer one obvious reviewer objection in the introduction.

## 4. Method and experiments

- Define inputs, constraints and the objective. If there is a guarantee, state it as a theorem or a checkable certificate; **do not use an LLM’s self-statement as a certificate**.
- Experiments: one subsection per RQ, each ending with a bold **Takeaway**. Required: main quality-and-cost table, where the method helps and where it does not (mechanism from counters, not guesses), ablation, other backbones **including GPT and Claude** when the paper uses LLMs, overhead. Say how many repetitions and report dispersion.
- Public data is the main table. Any conclusion drawn on non-public enterprise data must also hold on public data; say so and show it.
- Presentation: S01–S11 — claim-first captions; bold best / underline second; a count row; colour-blind-safe figures; keep every losing cell; explain losses once, in the experiment that measures them, as fact → mechanism → regime.

## 5. Related work, limitations, integrity

- 3–5 themed paragraphs; end each with how this paper differs. Actively declare relationship to the authors’ already-submitted papers (ICDE 2027 Ladder 2258, AuthZ-Graph 2034, Certify-Join 2052, N1 2066, and sibling PVLDB submissions in other months).
- Limitations: follow write-icde §9. No “where we fail” heading; no self-negation in the abstract or the conclusion; no hiding losses.
- AI-generated-content declaration: include if the volume requires it; state tools honestly.
- Never invent numbers, never drop a measured cell, never claim SOTA on a fixture the method was written against (see BindOrClarify v0.1: 100% on template rules is not a main-table result).

## 6. Workflow

1. Re-open the official important-dates and submission-guidelines pages; record the access date.
2. Check author monthly/yearly caps against other submissions in the same month.
3. Draft against the 12-page body budget; move only references beyond page 12.
4. If EA&B: finish the reproducibility package **before** the full-paper deadline.
5. Run `results-presentation-review` and `academic-latex-polish`; then a compliance pass (page count, template, AI declaration, artifact URL).
6. Enterprise traces stay out of the repo and the artifact; public generators and SHA-pinned downloads stay in.
