---
name: "review-pvldb"
description: "Simulated PVLDB Volume 20 review for pre-submission improvement, built from the official PVLDB review process (Associate Editor, at least three reviewers, three-week discussion, meta-review, Accept / Reject / one Revision; desk-reject for format, caps, COI, scope), EiC guidance on out-of-scope and citation practice (Volume 18–19 front matter), common revision requests, and a self-negation / limitation-writing pass from accepted PVLDB, SIGMOD and ICDE papers. The simulated reviewer may request adding, dropping or shrinking experiments; the authors may run those increments in revision. Use when self-reviewing a PVLDB draft (审 PVLDB / 模拟审稿 / 投稿前自审 / 自我否定检查 / 要不要补实验)."
---

# Reviewing for PVLDB (Review-PVLDB 审稿指南)

This skill is for **pre-submission self-review** and for reading official reviews, not for producing a real PVLDB review of someone else's paper under a PC assignment. Official process sources, accessed **2026-11-12 PT**:

- Submission Guidelines (process, caps, scope, COI, artifacts, embargo): https://www.vldb.org/2027/submission-guidelines.html
- Call for Research Track (categories, evaluation expectations): https://vldb.org/2027/call-for-research-track.html
- EiC letters on desk-rejects and scope (PVLDB Vol. 18 No. 5 Front Matter): https://www.vldb.org/pvldb/vol18/FrontMatterVol18No5.pdf
- EiC letters on the Volume 19 process (at least three reviewers, AE, three-week discussion, meta-review; SAR; related-submission policy): e.g. https://www.vldb.org/pvldb/vol19/FrontMatterVol19No1.pdf and No. 3
- Limitation-writing evidence: `write-pvldb` §7 and `write-icde/references/limitations-writing*.md`

Use with `submit-pvldb` and `write-pvldb`. Official pages win. Reports to the author are in **Chinese**; a simulated review that mimics a PC review is in **English**, with a Chinese meta-summary.

## 1. Official process (what a real review looks like) [CFP]

- Plagiarism and COI screening, then assignment.
- At least **three** experienced reviewers, coordinated by an **Associate Editor**. A fourth reviewer may be added for specialized expertise.
- A structured **three-week discussion**, then a consensus **meta-review**.
- Outcomes on the first pass: **Accept**, **Reject**, or **Revision** (only one revision; up to 2.5 months; reviews are specific about what is expected).
- Tools: CMT, TPMS, CLOSET (COI), iThenticate. Associate Editors assess artifact availability on a standard rubric for accepted papers (ACM badge).
- Desk rejects (format, missing names, page limit, caps, unattested COI, incomplete abstract, out of scope) may state only one reason. Format/caps/COI/abstract desk rejects do **not** start the 12-month embargo; a content reject does.

Volume 19+ also uses a **Self-Assessment of Relevance** for papers at the boundary, and requires **Self-Declaration of Related Submissions**. A Shadow PC exists and is independent of official decisions.

PVLDB does **not** publish its reviewer form on OpenReview (the venue is not on OpenReview). Do not invent scores. Simulate with the dimensions in §2, which are those the Guidelines, the Call and the EiC letters actually use.

## 2. Review dimensions

Score each qualitatively (Strong Accept / Accept / Weak Accept / Borderline / Weak Reject / Reject) and write a short paragraph, then a meta-recommendation.

1. **Scope and data-management contribution.** Does the manuscript itself address DM challenges, engage the DB literature beyond syntactic citation, and evaluate in a DM context? (`submit-pvldb` §5.) Out-of-scope is a desk-reject risk.
2. **Novelty and incrementality**, including declared related submissions (assume those are accepted). A companion paper that shares a fold or a headline table is a problem.
3. **Technical depth.** For Foundations/Algorithms: soundness of theorems, tightness of scope statements. For Systems: principled architecture, working prototype. For EA&B: new insight, a new way to evaluate, or a real-workload characterization; not “our method wins.”
4. **Experimental evidence.** Strongest published baselines actually run (not estimated); held-out protocol; W/T/L and losing cells explained once with a mechanism; public-data confirmation of any enterprise claim; EA&B package complete at submission. The simulated reviewer **may request** an added baseline, a larger scale, a missing official-TEST row, an ablation, or the *dropping* of a low-information table that blows the 12-page budget.
5. **Presentation and 12-page budget.** Official template, names on page 1, body ≤ 12 including appendix and acknowledgements, S01–S11 tables, English clarity.
6. **Integrity and limitation writing (§3).** Numbers match the repo; no claim the tables contradict; mandatory disclosures present; **self-negation is not mistaken for honesty.**

## 3. Self-negation and limitation pass (required on every draft)

Run this pass **in addition to** a scientific review. It uses accepted-paper practice (`write-pvldb` §7), not a request to hide facts.

**Flag and propose a rewrite (do not apply it until the author approves, if a plan-only task):**

- Abstract or conclusion lists losses of the authors' method, a laundry list of “remaining limits,” or “future work” that names a gap (0/10 algorithm abstracts and conclusions do this; 0/9 EAB papers put *benchmark* limits there). Findings about *systems under test* in an EA&B paper are allowed and expected.
- A heading “where we fail”, “honest residual,” “the honest generalization gap,” “we report rather than paper over,” “would not survive a PVLDB review,” “we do not claim December readiness,” “no cell was invented,” “no number was changed.”
- The same weak cell or “we did not do X” is repeated in the abstract, introduction, experiments, discussion, threats **and** conclusion. State it once.
- Process language: visible `\todo`, “this experiment is open and is not estimated,” a first-pass gold-bug percentage told three times, “we will not retune” as a refrain.
- The word “limitation” applied to the authors' own method or benchmark; “fail” applied to themselves; “honest” as a self-congratulatory adverb.

**Keep, and say so (deleting these would be concealment):**

- Every losing cell and its mechanism, once, next to the table.
- A confidence interval that includes zero, once, next to that comparison.
- A standard baseline that was not run, if the paper would otherwise be read as having run it; worded as a protocol fact, not a confession, or finished as an increment.
- “The system has not replaced the live engine,” if that is true (more often a SIGMOD industrial issue).
- PVLDB-required related-submission declarations, the honest-annotation (or equivalent) premise of a certificate, “we do not report numbers against a system we could not faithfully run, and we do not claim a win.”
- The AI acknowledgment if the cycle requires it, shortened to the venue form.

**Revision-style experiment requests the simulated reviewer is allowed to make:**

- Add a missing strongest baseline on a frozen held-out (or label a DEV-only profile clearly).
- Add a public-data confirmation of an enterprise-only claim.
- Add an ablation that attributes a first-place metric to a named component.
- Move a post-hoc rule that would improve a held-out onto a **new** pre-registered fold; do **not** request retuning on the same held-out.
- Drop a table or a repeated paragraph to recover page budget.
- Authors may run these increments in a PVLDB revision (2.5-month window) or, if cheap and clean, before initial submission. The simulated review must estimate cost and must not request a change that would invalidate a frozen official number.

## 4. Common rejection and revision reasons (from official text and accepted-paper practice)

From the Call, the Guidelines and EiC letters:

- Out of scope; DB literature only cited syntactically; too many non-peer-reviewed citations (Vol. 18 No. 5 EiC letter: desk-rejects rose, majority out of scope, some format).
- Over the page limit; wrong template; authors missing or not matching CMT.
- Cap or COI violations.
- Incremental relative to a **declared or undeclared** related submission.
- Evaluation on a fixture designed with the method, without an independently inspectable test (a revision request, not automatically a reject, if the authors already have such a test and present it as the inspectable one).
- Missing strongest baselines; estimated rows; official numbers rescored after tuning.

From how revisions are described historically in PVLDB/SIGMOD policy text (also PACMMOD reviewer guidelines, which PVLDB-style revisions resemble): “justify a crucial assumption,” “present a realistic scenario,” “compare against a relevant previous system,” “show results at larger scale or from a real system,” “tighten presentation.” Revisions are **not** requested to invent a new problem or to repair a fundamental lack of novelty.

**Writing that hurts acceptance even when the method is strong:** a conclusion that agrees the work is incomplete; an introduction that tells the reviewer the result would not survive review; a threats section that reads as an internal audit. Accepted papers do not do this (`write-pvldb` §7.1). The cure is reframing and shortening, not deleting the underlying facts.

## 5. Output of a simulated review

For each paper:

1. A one-paragraph **meta-review** in Chinese (recommendation, the two or three issues that would move it, which issues are writing and which are evidence).
2. Two or three simulated reviewers in English, each with a score, a summary, strengths, weaknesses, and **concrete experiment requests** with estimated cost, or an explicit “no further experiment needed.”
3. A **self-negation appendix**: a list of flagged sentences, each labelled `删去冗余` / `重新框定为范围或取舍` / `移位置` / `通过补实验解决` / `保留` (with a concealment-risk note). This appendix is for the author. It is **not** written into the manuscript.
4. A reminder: this is a simulation. Do not treat a Weak Accept here as a prediction of the real AE.

## 6. Workflow

1. Re-read `submit-pvldb` official pages (access date).
2. Check caps, related submissions, template, page count, artifact (EA&B: full package).
3. Scientific review on the dimensions of §2.
4. Self-negation pass of §3.
5. If the task is plan-only, **stop**: deliver the review and the rewrite plan; do not edit the manuscript until the author approves.
