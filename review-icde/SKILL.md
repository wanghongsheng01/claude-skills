---
name: "review-icde"
description: "Simulated IEEE ICDE program-committee review of a manuscript before submission: desk-reject screen (format, scope, COI, AI disclosure), three independent reviewer reports on an ICDE-style form (novelty, technical depth and soundness, experiments, presentation, reproducibility, relevance), reviewers may request added/supplemented/re-run/removed experiments that the authors then run, a limitations-presentation lens (contradiction vs self-negation), discussion, rebuttal and re-scoring, a senior-PC meta-review with Accept/Reject (ICDE 2027 has a rebuttal but no revision), an adversarial check of numbers, proofs and references, and a revision table. Built from the ICDE 2027 CFP and the strengths/weaknesses of 21 deep-read accepted papers. Has an Experiment, Analysis and Benchmark (EAB) mode (references/eab.md): an EAB review form (novelty of insights, soundness of methodology, coverage, reproducibility as a hard requirement, usefulness), a 40-item EAB checklist from the ICDE/PVLDB/SIGMOD calls, the PVLDB reproducibility criteria, DB fair-benchmarking pitfalls and benchmarking crimes, 15 common rejection reasons for benchmark papers, a three-column limitations lens (acceptable scope vs self-negation vs hiding), and add/supplement/re-run/remove experiment requests that the authors run before submission. Use for 模拟审稿 / 独立审阅 / 预审 of an ICDE paper (including EAB / benchmark / experimental-survey papers) or rebuttal preparation."
---

# Simulated ICDE review (模拟 ICDE 审稿)

Use after `write-icde`, before `submit-icde`. Forms in `assets/`; evidence in `references/reviewer-lens.md`.

**Provenance.** ICDE publishes no review form, scale or meta-review template (checked 2026-11-06). The
form in `assets/` is a simulation. Its only official anchors are relevance and positioning against
ICDE/VLDB/SIGMOD work, availability of supplemental material, the EAB "new insight / new way to evaluate"
criterion, and inclusive writing. `references/reviewer-lens.md` is survivor evidence from 21 accepted
papers: it shows what was accepted, not why papers were rejected.

**Process in ICDE 2027.** A senior PC member (called "area chair" on the older guidelines page)
coordinates at least three reviewers and writes a meta-review based on their discussion. Authors get one
rebuttal (2027-01-08 to 01-15). The outcome is accept or reject; there is no revision (ICDE 2023–2026 had
revisions, so reviewers may still ask for changes).

## Language convention
Reviews, meta-review and rebuttal drafts in **English**; the summary for the author and the revision table in **Chinese (中文)**.

## 1. Independence
The reviewer must not be the author of the text. When using sub-agents, give each reviewer only the PDF/LaTeX, the CFP rules and the review form, not the author's own assessment, and ask for the three most likely rejection reasons. Use three reviewers with different lenses (method/theory, systems/experiments, outside-area generalist) and one meta-reviewer who reads the three reports.

## 2. Desk screen (`assets/desk_screen.md`)
Template and 12-page limit without appendix; author block (single-blind); AI disclosure; scope: a data-engineering challenge and ICDE/VLDB/SIGMOD lineage in related work; EAB title tag and complete artifacts if EAB.

## 3. Reviewer report (`assets/review_form.md`)
Summary; 3 strengths; 3 weaknesses (each actionable); detailed comments by section; scores for novelty, technical depth/soundness, experiments, presentation, reproducibility, relevance; overall (Strong Accept / Accept / Weak Accept / Weak Reject / Reject); confidence; questions for the rebuttal.

What ICDE reviewers look for (from accepted papers, `references/reviewer-lens.md`):
- A gap shown with evidence (Figure 1 measurement), not asserted.
- One clear insight with a provable property; known methods as special cases.
- Baselines that include the strongest recent methods and core-venue work; fair tuning; same pilot/budget.
- Real costs (dollars/tokens/latency) for LLM papers; scalability for systems and graph papers.
- Validity of any guarantee measured (e.g. coverage vs nominal), dispersion over repetitions.
- Limits stated once each, with a mechanism, in the experiment that measures them (neither hidden from the tables nor repeated in abstract and conclusion).
Typical rejection reasons: incremental over a named prior paper; guarantee assumed but not checked; toy scale; missing a key baseline; out of scope (pure ML); claims in abstract not matched by tables.

## 3a. Pre-submission mode: reviewers may ask for experiments, authors may run them
This review improves a manuscript before submission, so it is not limited to judging the
experiments that exist.
- **Reviewers**: may request experiments that are added (a missing baseline, dataset, k, metric),
  supplemented (more seeds, a dedicated machine, a larger graph, a sensitivity sweep), re-run (with the
  current build, under fair tuning) or removed (results that are redundant, unfair or misleading).
  - Each request names the weakness it answers, a rough cost and the result that would change the
    score (form item 9).
  - Prefer requests that remove a weakness outright over requests that only add a caveat sentence.
    For example, re-running a baseline with the current build lets the paper delete its "measured with
    an earlier build" sentence.
- **Meta-reviewer**: merges the requests into one prioritised list that fits the time left before the
  deadline.
- **Authors (the revising agent)**: run the accepted requests as incremental experiments, regenerate the
  tables and figures from the raw results, and update the text and the revision table.
  - Experiments that are dropped are answered in the revision table, with the reason.
- **Iterate**: re-review the revised version with fresh reviewers until no blocking weakness remains or
  the deadline forces a stop.

## 3b. Presentation of limitations (lens for every reviewer)
Accepted ICDE/VLDB/SIGMOD papers keep every losing number in the tables and state each loss once, with a
mechanism, in the experiment that measures it. They put no loss in the abstract or conclusion and use no
failure headings (see `write-icde/references/limitations-writing.md`).

Flag two opposite defects:
- **Contradiction**: text that overclaims against its own tables. This is a rejection reason.
- **Self-negation**: the same loss repeated across the abstract, contributions, takeaways and
  conclusion, or self-negating wording. This is a presentation weakness that hands reviewers rejection
  reasons.

**Area lens: AQP / sampling / LLM queries with guarantees** (`write-icde/references/limitations-writing-aqp.md`).
Ask the questions these reviewers ask, and check the paper answers each with evidence already in it:
- asymptotic only? -> is the condition stated once, and is coverage measured at the smallest slices and
  out of sample (BARGAIN, SIGMOD'26, attacks "only asymptotically" guarantees)?
- is the strongest per-query competitor (shared pilot, cache, ideal moments) in the comparison, at equal
  targets, and are the competitors' certified targets reported (a cheaper method that certifies fewer
  targets is not cheaper)?
- LLM as truth? -> oracle-relative definition, human audit size and agreement with an interval.
- real dollars and tokens at list prices?
- does each component (planner, lazy rule, floor) win on some metric, or does one look dispensable?
- proprietary data: do the public datasets carry the headline claims?
A reviewer may request the incremental experiment that closes a gap (e.g., flooring a ratio interval that
under-covers); prefer that to an admission in the text.

## 3c. Discussion, rebuttal and re-scoring (simulates the 2027 process)
1. **Discussion.** Each reviewer reads the other reports and may change scores, with one sentence of
   reason.
2. **Rebuttal.**
   - Draft the author feedback with `submit-icde/assets/rebuttal_template.md`, under an assumed cap of
     about 4,000 characters until CMT shows the real one.
   - It may use only numbers already in the paper or the artifact.
3. **Re-score.** Each reviewer states whether the rebuttal resolved each weakness and gives a final
   score.
4. **Meta-review.** The meta-reviewer decides accept or reject.
5. **Pre-submission rule.** A weakness that only a new experiment could answer is fatal after
   submission, because there is no revision. Fix it now (section 3a); the rebuttal cannot.

## 3d. Extra questions for EAB papers
**For an EAB paper, use `references/eab.md`.** It contains:
- §1, an EAB review form with seven scored criteria: novelty of insights, soundness, coverage,
  reproducibility (a hard requirement), usefulness, presentation, relevance;
- §2, a checklist (A contribution … I positioning). Each fail becomes a weakness or a requested
  experiment;
- §3, common rejection reasons for benchmark papers, labelled by evidence type;
- §4, the limitations lens with three columns: an acceptable scope statement, self-negation (a
  presentation weakness) and hiding (a soundness weakness). Negatives about the evaluated methods are
  not classified; they are the contribution;
- §5, add / supplement / re-run / remove requests with EAB examples. The authors run them before the
  Round 2 deadline, because ICDE has no revision.

Summary questions:
- Limitations lens for EAB (`write-icde/references/limitations-writing-eab.md`): negatives about the
  evaluated methods are the contribution and are not self-negation. Flag limits of the benchmark itself
  that appear in the abstract or conclusion, are repeated, use deficit words ("incomplete", "elementary",
  "indicative", "found in review"), or sit in a threats list longer than about four items. Check whether
  the paper meets its own Table I criteria; a reviewer will turn any gap it charges prior work with
  against it. Ask for the control experiment or second metric that would turn an admission into a result.
- Does the paper give a fundamentally new insight, or a new way to evaluate?
- Are all artifacts public, with no exceptions?
- Are the benchmark choices justified and reproducible?

## 3e. Reproducibility check (an explicit row)
- The supplemental URL is public, neutral and non-tracking (not a personal page).
- The repository contains run instructions, the raw results behind every table, and the scripts that
  regenerate the tables and figures.

## 4. Adversarial checks
- Every number in the abstract/introduction appears in a table or figure and matches the result files.
- Each proof step is checked; assumptions are stated in the theorem.
- Every reference exists with the stated venue/year (Crossref/OpenAlex/arXiv); no citation supports a claim it does not make.
- Figures readable at column width; captions self-contained.
- **Compiled PDF checked** with `manuscript-writing-review`: no legend over data or cut off, no table in
  the other column, no end-of-proof boxes, theorem conditions in displays, every page looked at.

## 5. Meta-review and revision
Meta-review: consensus strengths/weaknesses and a decision. Then a revision table: weakness -> change made -> location; re-run the checkers of `submit-icde` and `write-icde`.

## Final checklist
- [ ] Desk screen passed.
- [ ] Three independent reports and a meta-review.
- [ ] Numbers, proofs and references verified.
- [ ] Requested experiments merged, run (or answered) and reflected in the tables.
- [ ] Limitations presented once each, with mechanism; no contradiction between text and tables.
- [ ] Revision table completed and changes applied.
