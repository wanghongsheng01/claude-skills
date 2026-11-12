---
name: "write-tkde"
description: "Writing guide for IEEE Transactions on Knowledge and Data Engineering (TKDE, CCF-A journal, rolling submissions). Covers journal-length completeness, ScholarOne submission, the need to re-read current page limits (commonly 12 double-column pages including references and biographies, with longer submissions subject to official overlength policy — verify on the IEEE Computer Society author page), single-blind review, and the prohibition on dual submission with PVLDB / VLDB. Presentation follows Deng S01–S11; structure extends write-icde with the extra room a journal expects (full proofs, complete ablations, discussion). Use when extending a conference idea or a March-after paper (CertMetric, NL2View) into a TKDE manuscript (写 TKDE / IEEE TKDE / 期刊扩写)."
---

# Writing for IEEE TKDE (Write-TKDE)

**Re-read the official IEEE Computer Society TKDE author / submission-guidelines page before every submission.** Page limits and charges change. Snapshot date: **2026-11-12**.

- Journal home and author instructions: start from https://www.computer.org/csdl/journal/tk and the “Author Information” / Journal Peer Review pages linked there. Submission is via ScholarOne.
- **Do not dual-submit** a manuscript that is under review at PVLDB / VLDB, SIGMOD, ICDE, or another venue. After a conference reject, follow both venues’ resubmission embargoes (TKDE has stated waiting periods for “revise as new” and for rejected papers — confirm the current months on the official page).
- Apply `results-presentation-review` (S01–S11) and `academic-latex-polish`. ICDE skills remain the conference reference; this skill is the journal increment.

## Language
Manuscript in **English**. Author-facing plans in **Chinese**.

## 1. Official constraints (verify)

As commonly posted for TKDE regular papers (re-check):

- Regular paper: a **12** double-column-page target **including references and author biographies**; submissions may be allowed up to **14** pages subject to mandatory overlength page charges (MOPC); longer than that has required EIC approval, with a stated maximum (often 18). Concise, comments and survey papers have **different** limits — do not use the regular-paper budget for those types.
- Template: IEEE Computer Society / `IEEEtran` journal option, as given on the official template page. No highlighting or unofficial colour in the review PDF if the journal forbids it.
- Review: single-blind, at least two reviewers, plagiarism screening.
- Rolling: there is no conference-style hard deadline. Use this for papers that **miss or intentionally avoid** the VLDB 2027 March cap (CertMetric, NL2View, a delayed BindOrClarify).
- Supplemental material is typically a **separate** file, not stuffed into the main PDF. There is usually no page cap on supplements; the main claims must still stand in the main file.

If the official page disagrees, follow the official page and update `references/official-rules.md`.

## 2. What a journal version must add

A TKDE paper is not a conference paper with a longer related-work section.

- **Complete** experiments: all promised baselines actually run (including GPT and Claude for LLM papers); factor sweeps; ablation; failure regimes; sensitivity; cost. “Left for a journal version” is not acceptable **in** the journal version.
- **Complete** reasoning: proofs or certificates in the main file or a self-contained supplement that reviewers can check. Still no LLM-as-certificate.
- **Related work** is a map, not a list: include journal and conference lineages (TKDE, VLDB, SIGMOD, ICDE, TODS). End each theme with a precise difference.
- **Discussion**: scope, threats to validity, when a practitioner should prefer a baseline — honest, mechanism-based, without a self-negating abstract (write-icde §9 still applies).
- **Reproducibility**: public data or a generator; artifact URL; enough detail to rerun. Enterprise data only as a supporting case, with the same conclusions shown on public data.

## 3. Structure (suggested)

Use write-icde §§2–7 as the skeleton, then spend the extra pages on:

- a fuller problem definition and notation;
- proofs or worked certificates;
- additional workloads and a “where it loses” section that already exists in the conference draft’s tables;
- a discussion section that does **not** retract the claims.

Title and abstract still follow Deng: no closing negative sentence in the abstract; headline numbers match the body.

## 4. Integrity and overlap

- Same authors’ ICDE 2027 papers and PVLDB submissions must be cited and distinguished. A journal extension of a conference paper must follow IEEE’s extension policy (substantial new material — confirm the current percentage or qualitative rule on the official page; never submit a verbatim conference text).
- Do not inflat page count with unreduced screenshots or leftover appendix dumps that belong in the supplement.
- Presentation: S01–S11 without exception.

## 5. Workflow

1. Open the current TKDE author page; record page limit, template, extension policy, embargo, access date.
2. If the idea is also a VLDB candidate, **choose one venue**.
3. Plan the extra experiments before rewriting prose.
4. Lint presentation and English; ScholarOne submission is done by the author.
