---
name: "review-sigmod"
description: "Simulated SIGMOD review for pre-submission improvement. Covers the SIGMOD 2027 Industrial Track (industrial PC, reviews on 2026-01-26 / wait 2027-01-26, optional lightweight shepherding revision, not double-blind, non-academic author, experience and industrial-strength evidence) and, for future cycles, the SIGMOD research / PACMMOD process (double-anonymous, at least three reviews, author feedback, Accept / Reject / Minor / Major revision, official revision-request examples). Includes common industrial and research rejection reasons and a self-negation pass. The simulated reviewer may request adding, dropping or shrinking experiments. Use when self-reviewing a SIGMOD draft (审 SIGMOD / 工业轨道模拟审稿 / SIGMODIND 自审 / 自我否定检查)."
---

# Reviewing for SIGMOD (Review-SIGMOD 审稿指南)

For **pre-submission self-review**, not for a real PC assignment. Official sources, accessed **2026-11-12 PT**:

- Industrial CFP and process: https://2027.sigmod.org/calls_industrial_track_papers.shtml
- Research CFP and process (2027 research track closed; use for later cycles): https://2027.sigmod.org/calls_papers_sigmod_research.shtml
- PACMMOD / SIGMOD reviewer-process description (two-phase review, author feedback, what revisions may request): ACM PACMMOD journal page, reviewer guidelines, https://dlnext.acm.org/journal/pacmmod/sigmod
- Limitation-writing evidence: `write-sigmod` and `write-pvldb` §7

SIGMOD research and industrial tracks are **not** on OpenReview; do not invent an OpenReview form. Use the dimensions below, which come from the CFPs and from the published PACMMOD reviewer guidance. Reports to the author in **Chinese**; simulated PC-style reviews in **English** plus a Chinese meta-summary.

## A. Industrial track (SIGMOD 2027)

### A1. Official process [CFP]

Each submission is reviewed by the industrial-track PC. Reviews are released **26 January 2027**. Some papers are invited to a **lightweight shepherding** revision due **23 February 2027**; others receive the decision with the reviews. Final notification **4 March 2027**. Eligibility: at least one non-academic author; names and affiliations on the paper; 12 pages + references; ACM proceedings template.

### A2. Industrial review dimensions

1. **Fit.** Is this an industrial-strength system, a novel application, or experience applying research to an industrial problem — or a research paper with a company logo? Conversely, is it a brochure without a generalizable lesson or a precise measurement?
2. **Operational exactness of the claim.** What is in production and what is not? Reviewers punish overclaim (a “deployment” that is only an evaluation on production traces) more than they punish a modest scope. A single factual sentence is enough and should stay.
3. **Technical substance.** Is the design precise enough to check (indexes, maintenance, exactness proofs)? Are academic neighbours (PQO, IVM, envelopes, rule indexes, …) positioned and, where claimed, actually run?
4. **Evidence.** Production workload **and** public or official data; every production conclusion also shown on public data; losing cells kept and explained as a regime (e.g. small portfolios: payoff in maintenance). Compiled vs interpreter, same-machine comparisons.
5. **Lessons.** Numbered, grounded, actionable; not a second results section and not a confession.
6. **Presentation, 12-page body, integrity.** Including the self-negation pass (§C).

### A3. Common industrial objections

- “Not yet in the live path” — valid scope; **keep** the factual sentence; do not invent a rollout. A Weak Accept with this objection is a realistic ceiling until there is verified operational evidence.
- A weak cell at production size (e.g. Q1 at 0.9×) used as a reject: the accepted-paper response is operating guidance, stated once, with public-data consistency, not five repetitions and not a deletion of the 0.9×.
- Domain-specific (freight, one company): the 2027 CFP explicitly welcomes novel applications; the paper should abstract the query (rule-defined cost functions, CFS) and confirm conclusions on public official data.
- Missing academic baselines that were promised: finish them on a held-out, or do not promise them. Estimating is a reject-level integrity issue.

The simulated reviewer **may request** a same-machine remeasurement, a public-data confirmation, a missing exact baseline, a one-paragraph deployment-path fact (only if the authors have it), or the deletion of a repeated weak-cell paragraph to recover space. The reviewer must not request a fake deployment claim.

## B. Research track / PACMMOD (future cycles)

**[CHECK]** that year's CFP. Snapshot of 2027 research / PACMMOD guidance:

- Desk reject for format or broken double-anonymity (early notification).
- At least three reviews. Author feedback **before** the decision: a revision plan, and clarifications of factual errors by **pointers into the submitted text** (example from the official guidance: “We compare to the method suggested by reviewer #3 in Section 2.4, paragraph 3”).
- Decisions: Accept / Reject / Minor Revision / Major Revision. About one month for a revision. One extra content page may be allowed after the first review (PACMMOD wording); a cover letter (up to 4 pages) and highlighted edits are expected.
- Official examples of **allowed** revision requests: “justify a crucial assumption,” “present a real(istic) scenario where the defined problem occurs,” “clean up notation,” “tighten presentation,” “compare against some relevant previous system,” “show experimental results with better data, such as at larger scale or from a real system.”
- Official **non-requests**: a revision will not be invited to address a fundamental lack of technical depth or novelty, or to have the paper address a substantially different problem.

Simulated research reviews use the same scientific dimensions as `review-pvldb` §2 (novelty, depth, evidence, presentation, integrity), plus double-anonymity and the appendix rule. Experiment increments are allowed in the same sense: add, drop, or shrink, with cost, without invalidating a frozen official number.

## C. Self-negation pass (both tracks)

Identical in spirit to `review-pvldb` §3 and `write-pvldb` §7. Industrial-specific flags:

- “Where the gains actually are — **and are not**” (drop the second clause; keep the factual regime).
- The weak production cell repeated in abstract, contributions, experiments, lessons and conclusion. Keep it **once** as operating guidance.
- “No number in the tables was changed” in the AI acknowledgment: delete; keep the acknowledgment itself.
- “Reconstruction is not a 100% match” is **good** industrial writing if it is a fidelity ceiling with a mechanism, stated once. Do not delete it.
- “We do not claim the system has replaced the live engine”: **保留**. Deleting it is concealment and, if the paper is then read as a deployment report, a worse integrity failure than humility.

Label every flagged sentence `删去冗余` / `重新框定为范围或取舍` / `移位置` / `通过补实验解决` / `保留`. Do not apply edits in a plan-only task.

## D. Output and workflow

Same shape as `review-pvldb` §5–§6: Chinese meta-review, English simulated reviews with experiment requests and costs, a self-negation appendix for the author, and a plan-only stop. This is a simulation, not a prediction of the industrial chairs' decision.
