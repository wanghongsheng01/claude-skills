---
name: "write-sigmod-industrial"
description: "Writing guide for the ACM SIGMOD Industrial track (CCF-A when the authors so treat it; SIGMOD 2027 Industrial). Covers the official deadline 2026-11-24 23:59 AoE (2026-11-25 19:59 Beijing), 12 pages plus unlimited references, single-blind / not double-blind policy, the requirement of a non-academic author, CMT submission, and a style suited to deployed or deployable systems, honest scope (what is and is not in production), and lessons. Presentation follows Deng S01–S11. Not for the SIGMOD research track (already closed for 2027). Use when drafting or polishing a SIGMOD industrial paper (写 SIGMOD 工业稿 / Industrial Track / SIGMODIND)."
---

# Writing for SIGMOD Industrial (Write-SIGMOD-Industrial)

**Re-read the official CFP before submission.** Snapshot date: **2026-11-12**.

- CFP: https://2027.sigmod.org/calls_industrial_track_papers.shtml
- CMT: https://cmt3.research.microsoft.com/SIGMODIND2027
- The SIGMOD **research** track for 2027 is closed; this skill is **only** for the Industrial track.
- Apply `results-presentation-review` (S01–S11) and `academic-latex-polish`. Do not rewrite ICDE skills.

## Language
Manuscript in **English**. Author-facing plans in **Chinese**.

## 1. Official constraints (SIGMOD 2027 Industrial)

- **Deadline.** 2026-11-24 **23:59 AoE** = **2026-11-25 19:59 Beijing time**. AoE is not “midnight Beijing”. Late uploads fail.
- **Length.** **12 pages** of body **plus unlimited references**. Use the official ACM / SIGMOD industrial template stated on the CFP (confirm the class and the year). No margin hacks.
- **Blindness.** **Not** double-blind. Author names and affiliations are on the paper. A **non-academic** author is required (industry affiliation). The RateQ decision was: keep the Loctek affiliation line, anonymize the body so it does not name the company in the prose.
- **Submission.** Through CMT, by the author who is allowed to submit (for RateQ: Dr.Wang personally). This skill does not submit.
- **What the track wants.** Experience with real systems: architecture, design choices, deployment, lessons, and measured impact. A thinly disguised research paper with no operational evidence is a poor fit. Conversely, a pure product brochure with no generalizable lesson and no honest limitation is also a poor fit.

## 2. How an industrial paper differs from a research paper

- **Lead with the operational problem**, then the constraint of the production environment (latency SLO, cost, human process, what cannot be changed), then the design.
- **Say clearly what is in production and what is not.** If the engine has not replaced the live system, write that (RateQ: “not yet replacing the online freight engine” is accurate and must stay). Reviewers punish overclaim more than they punish a modest deployment scope.
- **Lessons** are first-class: what was tried, what failed, what would be done differently. A lesson must be supported by a measurement or a concrete incident type, not a slogan.
- **Anonymization of customer and proprietary data.** No raw rates, no credentials, no customer identifiers. Public or synthetic workloads carry the main tables when the production numbers cannot be released; if a production number is used, it must be aggregated and consistent with what the authors are allowed to publish.
- **Related work** still exists: position against published industrial and research systems. This is not a white paper.

## 3. Structure (suggested)

1. Introduction: the operational problem and why existing practice breaks; one figure or number from a **releasable** measurement; contributions as design + deployment + lessons + evidence.
2. Setting and requirements: workload, constraints, what is out of scope.
3. Architecture and design: components mapped to requirements; algorithms only as deep as the industrial claim needs, with enough precision to be checked.
4. Implementation and deployment: what shipped, what did not, operational cost.
5. Measurements: quality, cost, robustness; comparison with the production baseline or with the obvious alternative. S01–S11 apply **as-is** (bold best, count row, honest losses).
6. Lessons and limitations: specific, evidenced, not a humility paragraph that retracts the claims.
7. Related work and conclusion.

## 4. Integrity

- Do not invent production metrics. Do not hide losing cells. Do not claim SOTA against academic methods unless those methods were actually run under the same protocol.
- AI-content declaration: include as the CFP requires; RateQ’s declaration is to be **confirmed by the authors**, not silently assumed.
- After the deadline, this skill is still useful for camera-ready and for later industrial tracks (re-read that year’s CFP; do not reuse 2027 dates).

## 5. Workflow

1. Open the CFP and CMT; record page limit, template, deadline (AoE → Beijing).
2. Confirm the non-academic author and the affiliation line.
3. Freeze claims that the authors have already frozen (do not “improve” a frozen RateQ body without an explicit request).
4. Presentation lint (S01–S11); English polish without changing numbers.
5. The author submits on CMT. The assistant does not.
