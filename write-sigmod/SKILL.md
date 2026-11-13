---
name: "write-sigmod"
description: "Writing guide for ACM SIGMOD (CCF-A), covering the Industrial Track (SIGMOD 2027 Industrial: deployed or deployable systems, lessons, honest production scope) and, for future cycles, the Research Track / PACMMOD. Built from the official 2027 CFPs (read 2026-11-12 PT) and from accepted SIGMOD, PVLDB and ICDE papers on how to title, structure, evaluate, present tables, cite, and state limitations without self-negation. Use when drafting or polishing a SIGMOD industrial or research paper (写 SIGMOD / 工业轨道写法 / SIGMODIND / 局限怎么写 / 不要自我否定 / lessons learned)."
---

# Writing for SIGMOD (Write-SIGMOD 写作指南)

**Re-read the official CFP of the track you are writing for.** Industrial and research tracks differ in anonymity, appendix rules, and what “contribution” means. Access date for the 2027 CFPs: **2026-11-12 (America/Los_Angeles)**. Official pages: `submit-sigmod`. This skill **supersedes** the shorter `write-sigmod-industrial` for new drafts.

Use with `submit-sigmod` and `review-sigmod`. Apply `results-presentation-review` (S01–S11). Official CFPs always win.

## Language convention

Manuscript in **English**. Author-facing plans in **Chinese (中文)**.

## Integrity boundary

Same as `write-pvldb`: change placement, frequency and wording only; never numbers, never hide a losing cell, never claim a production deployment that has not happened, never delete a venue-mandatory statement. “Do not self-negate” is not “do not disclose.”

---

## A. Industrial track

### A1. Official constraints (SIGMOD 2027 Industrial)

See `submit-sigmod` §A: 12 pages + unlimited references; **not** double-blind; non-academic author required; deadline 2026-11-24 23:59 AoE; ACM `sample-sigconf.tex`; CMT SIGMODIND2027. The AI acknowledgment, if included, is **not** excluded from the 12 pages by the 2027 industrial CFP.

### A2. How an industrial paper differs from a research paper

- **Lead with the operational problem**, then the constraint of the production environment (latency SLO, billing exactness, what cannot be changed), then the design.
- **Say clearly what is in production and what is not.** If the engine has not replaced the live system, write that **once**, factually, in the introduction or in a table caption about the production workload. The 2027 industrial CFP asks for “experience” and “industrial-strength” systems; reviewers punish **overclaim** more than they punish a modest deployment scope. Do not add “and where the gains are not” as a second confession, and do not repeat the 0.9× (or equivalent) fact in the abstract, the contribution list, the experiments, the lessons **and** the conclusion.
- **Lessons are first-class.** What was tried, what failed as an *engineering choice*, what another team should do, each grounded in a measurement. A lesson is operating guidance (R6 in `write-pvldb`), not a humility paragraph that retracts the claims.
- **Anonymize customer and proprietary data** in the prose even though the track is single-blind: no raw rates, no credentials, no customer identifiers. Public or official workloads carry the main tables when production numbers cannot be released. Every conclusion drawn on company data should also be shown on public data (L5 pattern).
- **Related work still exists.** Position against published industrial and research systems. This is not a white paper.

### A3. Suggested structure

1. Introduction: operational problem; one releasable figure or number; “we evaluate on the production workload; the system has not replaced the live engine” as one factual sentence if that is the truth; contributions as design + evidence + lessons, with the production payoff named as a regime (maintenance vs single-query, warehouse-scale vs contract-scale), not as a loss.
2. Setting and requirements: workload, constraints, what is out of scope (as a design boundary).
3. Architecture and design: components mapped to requirements; algorithms as deep as the industrial claim needs, with enough precision to be checked; theorems welcome when they are the reason the system is exact.
4. Implementation and deployment: what shipped, what did not, operational cost — only facts the authors can verify.
5. Measurements: quality, cost, robustness; comparison with the production baseline and with the obvious alternatives. S01–S11 apply as-is. A single weak cell (e.g. Q1 at a 10-service portfolio) is explained once, by the instance property (few eligible services, little to prune), then turned into guidance.
6. Lessons: numbered, each with a measurement; do not repeat every table number.
7. Related work and a short conclusion that restates the operational payoff and the public-data confirmation, **without** a future-work laundry list.

### A4. Limits and losses in an industrial paper

The algorithm-corpus rules of `write-pvldb` §7 apply, with two industrial specialisations:

- **Production fidelity that is not 100%** is reported as a *fidelity ceiling of the reconstruction and of the export*, with the mechanism (e.g. a de-identified field that the export omits) — not as “the model cannot price every parcel.” State it once, in the production RQ or in a lesson.
- **A speedup below 1× at a small portfolio** is a regime: “at *n* services the compiled query is within *p*% of brute force; adopt the system first for audit and re-quote maintenance.” This may appear in the abstract as a **qualifier of where the payoff is**, which is the industrial analogue of R1 (scope qualifier on the positive claim). It should not appear five times, and it should not be worded “the method is not faster.”

Star (Sun et al., *SIGMOD* 2023, PACMMOD 1(2)) shows the research-track version of the same move: name the target workload, explain the outlier with a mechanism, give guidance. HCM (Lin et al., *PVLDB* 14(5), 2021) recommends rebuilding for very large batches rather than saying the method fails on large batches.

### A5. Integrity

Do not invent production metrics. Do not hide losing cells. Do not claim SOTA against academic methods unless those methods were actually run under the same protocol. Do not silently upgrade “evaluated on the production workload” to “deployed in the live engine.” The AI declaration is confirmed by the authors and is shortened to the venue form — no “no number in the tables was changed.”

---

## B. Research track (for future SIGMOD/PACMMOD cycles)

**[CHECK]** that year's CFP. For SIGMOD 2027 research (already closed; snapshot in `submit-sigmod` §B): 12-page body, unlimited references, **double-anonymous**, optional short review-only appendix, author feedback and possible minor/major revision, camera-ready in PACMMOD format (13 pages excluding references).

Writing follows `write-pvldb` §§1–10 almost as-is (title, abstract, introduction, theorems, RQ-structured experiments, W/T/L, fact–mechanism–regime–bound, no self-negation in abstract or conclusion), with these differences:

- **Anonymity:** no author names, no GitHub URLs that identify the authors, no “our previous paper [X]” that breaks anonymity. Artifact links use an anonymized snapshot if required by that CFP.
- **Appendix:** essential proofs may go to a separate review-only PDF; the body must still be self-contained. Do not park a second evaluation in the appendix and rely on reviewers to read it.
- **Revision culture:** SIGMOD research often invites a revision with specific requests (add a baseline, a larger or real dataset, a clarification). Write the initial paper so that a one-month revision is feasible; do not leave visible `\todo` or “this experiment is open and is not estimated” in a submitted body. Either finish the run or omit the paragraph.

The limitation-writing rules (R1–R11) are the same. They were measured in part on a SIGMOD 2023 paper (Star) and on PVLDB papers; they are venue-practice, not ICDE-only.

---

## C. Title, figures, tables, references (both tracks)

- Industrial titles name the operational problem or the system and the setting (`RateQ: Exact Cheapest-Service Queries over Rule-Defined Freight Tariffs` is the pattern: acronym + exactness + the industrial object). Research titles follow `write-pvldb` §1.
- Figures and tables: S01–S11; claim-first captions; bold best / underline second; count row; every losing cell kept; one mechanism paragraph per loss.
- References: ACM Reference Format; industrial papers still cite the research line (PQO, IVM, envelope structures, rule indexes) and the industrial line, “beyond a syntactic citation.”
- Conclusion: industrial — operational payoff and public confirmation; research — headline result with scope folded in. Neither ends with a remaining-limits list.

## D. Workflow

1. Open the CFP of the **correct track**; record anonymity, page limit, appendix rule, deadline.
2. Industrial: confirm the non-academic author and what is or is not in production.
3. Self-negation pass (`write-pvldb` §7 and `review-sigmod`): one factual production-scope sentence; each weak cell once with a regime; no process language in the AI acknowledgment; no five-times repetition of the weak cell.
4. Presentation lint; English polish without changing numbers.
5. The author submits. The assistant does not.
