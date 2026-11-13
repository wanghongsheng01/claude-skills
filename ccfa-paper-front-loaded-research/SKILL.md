---
name: ccfa-paper-front-loaded-research
description: >-
  Use before starting any new CCF-A database paper (PVLDB, ICDE, SIGMOD and
  siblings). Runs a front-loaded research process—venue fit, problem definition,
  SOTA and dataset maps, novelty storyline, type-specific reading, and an
  experiment plan—and treats the coauthor briefing PDF as a product of that
  process, not a post-hoc wrap-up. Do not use after a manuscript is already
  frozen merely to dress it up, and do not use it as a substitute for official
  venue guidelines.
---

# Front-loaded research before writing a CCF-A paper

Official venue guidelines (current-cycle CFP, page limits, identity policy, artifact rules) always take precedence over this skill and over advisor advice. Do not encode a calendar-year deadline in this skill; look up the live official page and record the access date.

## When to use

- A new CCF-A article is about to be started: an idea, an enterprise need, or a candidate topic exists, but the method, the official experiments, and the manuscript are not yet underway.
- A paper is already in progress but stages 1–6 were skipped or are incomplete: stop expanding experiments, complete the research document, then continue.
- A finished manuscript needs a **catch-up** research document (补课) before a coauthor briefing: write honest conclusions; list storyline or baseline gaps as recommendations; do not silently rewrite the paper.

## When not to use

- The task is only a pre-submission compliance pass (use the pre-submission-hardening note).
- The task is only compiling a coauthor PDF for a paper whose stages 1–6 document already exists and is current: follow the briefing template, do not redo the literature from scratch.
- The user has not approved execution of a research programme that would spend money, contact coauthors, or submit to a conference. This skill never sends messages, never submits, and never merges a `claude-skills` PR.

## Inputs

- Reference briefing sample (default: the N1 coauthor PDF, read-only), or a statement that the already-extracted template should be reused.
- Materials: idea, draft, enterprise need, code, existing experiments—paths or links, or "none".
- Target venue: name, year, track, deadline if known; otherwise recommend candidates and wait for confirmation before a directed analysis.
- Tentative research type (B1-method / B1-benchmark / B2) or "undecided".
- Constraints: time, compute, data, budget, confidentiality.

Do not invent missing inputs. Mark them "to be supplied".

## Outputs

1. A Chinese front-loaded research document (Feishu + the paper's private repo) with the eleven-part structure below.
2. A written type decision (B1-method, B1-benchmark, or B2) with literature evidence.
3. A research and experiment plan in which every experiment maps to a claim.
4. Only after (1)–(3) pass the gates: method implementation, experiments, manuscript, and then the coauthor briefing PDF.
5. Updates to type-specific skills when reusable lessons are found.

## Process (stages 1–6 are a gate)

**Gate for a new paper.** Do not write the method, run main experiments, or draft the submission manuscript until stages 1–6 are written and the quality gates pass.

**Catch-up for a finished paper.** Produce the same document honestly. If the storyline does not stand, a strong baseline is missing, venue fit was overstated, or the type is wrong, record recommendations and risks. Do not change the manuscript or rerun an official test fold without the author's confirmation.

### Stage 1 — Briefing template

Reuse the already-checked N1 structure (cover; optional reply to prior comments; venue fit; scientific problem and type; existing methods and SOTA; datasets; why they fall short; opportunity and novelty storyline; our method; experiments with bold / underline / W-T-L and 95% CI; questions for the coauthor; consistency declaration). Extract tone and evidence placement; do not copy old facts from the sample into the new paper.

### Stage 2 — Venue fit

1. Verify the venue is currently CCF-A and read **this cycle's** official guidelines (pages, anonymity, artifacts, author caps, concurrent-submission rules). Record the URL and the access date.
2. Survey formally published papers of the last three years (extend to five if the sample is thin or the topic shifted, and say why). Build a list with title, year, track, problem, method type, datasets, contribution, and a formal source (official proceedings or DOI). Preprints are leads only.
3. Classify by scientific problem, area, and method family. State inclusion rules, the denominator, and how labels were checked.
4. Report **share among accepted papers** and, separately, **acceptance rate of the direction**. If the submission denominator is unavailable, do not invent an acceptance rate and do not call a share an acceptance rate.
5. Say whether the direction is aligned with recent accepted work, whether its share ranks near the top, and whether the trend is stable or a short spike. Present contrary evidence. Never show only a favourable trend.

### Stage 3 — Problem, SOTA, datasets

Define the scientific problem as object—input/output—constraints—core tension—evaluation goal—scope. Separate an enterprise need, an engineering task, a technical difficulty, and a researchable problem. Decide, with sources, whether the problem is already defined in the literature or first defined here. A renamed known problem is not B2.

For each strong method: formal citation, mechanism, assumptions, public code, datasets, metrics, protocol, reported result, reproduction status, limits. Tag evidence as "from the original paper", "official leaderboard", "third-party reproduction", or "local reproduction". List mandatory baselines, optional baselines, and ablations, with reasons. A constructed control that reimplements our mechanism under an existing paradigm can be the strongest baseline; say that it is not a vendor binary.

For datasets and benchmarks: scale, domain, labels, splits, metrics, licence, realism, leakage, saturation, and representative papers. Explain inclusions and exclusions. A new dataset requires a proof that existing ones are insufficient. Formal claims must stand on public data; enterprise evidence is complementary and de-identified.

### Stage 4 — Opportunity and novelty storyline

Do not declare novelty before stages 2–3. Build the storyline as: established consensus; precise failure condition; why it fails; unused mechanism or constraint; executable method or protocol; falsifiable claim and what would refute it; value and non-goals. Check the storyline against recent accepted papers at the target venue, with examples and counterexamples. "Reviewers will like this" is not evidence.

### Stage 5 — Learn from published papers of the same type

Load the matching branch skill (`ccfa-b1-method-writing`, `ccfa-b1-benchmark-writing`, or `ccfa-b2-first-problem-definition`). Read full official PDFs, not abstracts. This round's floor is five representative papers per type, each with a DOI or official proceedings URL; later expand to 15–25. Extract thinking (how they found the opportunity, compressed claims, and persuaded with evidence), not a second related-work paragraph.

### Stage 6 — Research and experiment plan

Write: one-sentence problem; primary and auxiliary contributions; difference from the nearest neighbour; venue fit; storyline; method and data path; baseline and dataset matrix; main experiment, ablation, robustness, efficiency, cases, failure conditions, statistical tests, reproducibility, resources, risks, and stop conditions. Delete decorative experiments. For a catch-up paper, compare the completed work against this list and record gaps as recommendations.

### Stage 7 — Skills, then the coauthor briefing

Deposit reusable lessons into this skill or a branch skill. The coauthor briefing PDF is written only after stages 1–6 (or an honest catch-up) and uses numbers identical to the current submission PDF. It is delivered to the corresponding author only; the agent does not forward it.

## Eleven-part research document

1. Executive summary. 2. Scientific problem and type decision. 3. Target venue, share (not rate), match and contrary evidence. 4. SOTA, baselines, datasets. 5. Opportunity. 6. Novelty storyline and venue-preference evidence. 7. Lessons from same-type papers. 8. Experiment plan or a review of completed experiments. 9. Evidence chain and uncertainties. 10. Recommend continue / adjust / stop. 11. Skill updates.

## Evidence standard

- Formal publications first: official TOC, DOI, publisher page. Record title, venue, year, and publication status.
- Statistics carry a denominator, a labelling rule, and an access date. Share ≠ acceptance rate.
- Comparisons use the same task, split, metric, and protocol.
- Facts, inferences, and recommendations are labelled separately. If evidence is missing, write "insufficient".
- Do not fabricate papers, DOIs, deadlines, results, or skill completion.

## Checklists

**Before methods or experiments (new paper).** [ ] Official guidelines read this cycle. [ ] Venue share computed with a denominator; no invented acceptance rate. [ ] Problem defined; type decided with citations. [ ] Strongest fair baselines and datasets listed. [ ] Storyline is falsifiable and has a boundary. [ ] Same-type papers actually read. [ ] Every planned experiment supports a claim. [ ] Confidentiality: no raw enterprise data, secrets, or business formulas in the document or repo.

**Catch-up.** [ ] Gaps stated as recommendations, not silently patched. [ ] Official folds not rerun. [ ] Numbers in any briefing match the submission macros.

## Quality gates

| Gate | Must hold |
|---|---|
| Venue | Sources verifiable; share and rate distinguished; contrary trends shown |
| Problem and SOTA | Clear definition; consistent comparison; no obvious missing strong baseline |
| Storyline | Increment over the nearest neighbour holds; not a renamed old problem |
| Plan | Experiments cover every claim; stop conditions stated |
| Briefing | Written only after the above; numbers match the submission PDF |

## Failure handling

- Official pages or proceedings unavailable: record the attempt, do not fill from memory, and do not proceed as if the fact were known.
- The closest neighbour already defines an equivalent problem: reclassify as B1 and rewrite the increment; do not keep a B2 claim.
- The strongest baseline cannot be run: say so, give the reason, and do not invent a row.
- A catch-up finds a broken storyline: report it; do not quietly weaken the baseline or retune on an official fold.

## Version

- 0.1 (2026-11-12, America/Los_Angeles): first draft from the approved v2 prompt (Feishu https://loctek.feishu.cn/docx/SAX8dvbjNo7ZaZxx5v9c5r8InFg, `ccfa-00-control` `a1345ce`) and the attached CCF-A execution prompt. Not yet validated on a new paper started from a blank page; validated as a catch-up on ScopeCache (paper 09) in the same round.
