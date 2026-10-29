---
name: "review-eswa"
description: "Review a manuscript the way Expert Systems with Applications (ESWA, Elsevier) screens and reviews it: editor desk check (scope as an applied expert/intelligent system, novelty beyond renaming, language, package completeness, similarity, double-anonymization), then two or three independent reviewer reports with Elsevier's criteria and ESWA's recurring criticisms (baselines, significance, ablation, sensitivity, cost, practical value, reproducibility, limitations), ending in Accept / Minor / Major / Reject. Two modes: (1) pre-submission self-review of the author's own ESWA manuscript, (2) helping a human reviewer draft an ESWA review report within Elsevier's confidentiality and AI rules. Also covers responding to ESWA reviewers (审稿 ESWA / 模拟 ESWA 审稿 / 回复审稿意见)."
---

# Review-ESWA: how ESWA screens and reviews (ESWA 审稿指南)

Evidence: the live ESWA Guide for Authors (2026-10-29), Elsevier reviewer guidance (how-to-review, double-anonymized guidelines, GenAI policy updated June 2026), Elsevier *Editor Essentials: Initial submission assessment* (2020), SciRev (n=20 ESWA reports), LetPub, CSDN/Zhihu author timelines, a 2019 ESWA decision letter, and vendor blogs (low reliability). Each item carries a tag: **[OFFICIAL]**, **[COMMUNITY]**, **[VENDOR]** or **[INFERENCE]**. Details and URLs: `references/evidence.md`.

Public ESWA reviewer reports are not available. The criticism list below combines Elsevier's official criteria, author-reported experiences and the journal's stated aims; treat it as a checklist, not as quotations.

## Language convention (permanent agreement with the author)
Review reports, editor letters and responses to reviewers in English; reports to the author in Chinese (中文).

## Process facts
- **Desk screen** by editors [OFFICIAL]; first decision in ~5 days on the journal's insights page (2026) [OFFICIAL]; SciRev immediate rejections took 3–27 days [COMMUNITY].
- **Double-anonymized**, at least two reviewers [OFFICIAL, 2026 guide]; SciRev averages 2.2 reports per first round [COMMUNITY]; an AE may decide on fewer reports [COMMUNITY].
- Decision after review ~62 days (insights page); acceptance ~147 days; typically 2–3 revision rounds [OFFICIAL/COMMUNITY].
- Recommendations: Accept, Minor revision, Major revision, Reject, with separate confidential comments to the editor [OFFICIAL, Elsevier].
- Reviewers and editors must not upload the manuscript to generative-AI tools; only private tools may support language or literature search, and use must be disclosed [OFFICIAL].
- Older ESWA guides (2024) stated that a rejected paper is not reconsidered unless >70% is rewritten [OFFICIAL, archived]; the 2026 guide no longer shows this, but plan for one shot.

## Mode 1 — pre-submission self-review (run before `submit-eswa`)
Use agents that did not write the text. Give each the compiled PDF or the `.tex` and this file; ask for line-numbered findings.

### Step A: editor desk screen (one agent, verdict in five lines)
Answer each with PASS / RISK / FAIL and a one-line reason:
1. **Scope**: is it an expert or intelligent system designed, tested, implemented or managed for a real application, with practical guidelines? Would the first page convince an ESWA editor, or does it read as a pure NLP/statistics/theory paper? (The "methods paper in an application journal" pattern is the most cited desk-reject risk [VENDOR]; in 2026 a sister Elsevier journal desk-rejected an LLM-annotation method paper as out of scope.)
2. **Novelty**: a genuine contribution, not a renamed or metaphor-dressed combination of existing techniques [OFFICIAL]?
3. **Language**: understandable enough for reviewers [OFFICIAL decision tree]?
4. **Package**: separate title page, anonymized manuscript, declarations-tool file, highlights, figures as files, AI statement, data statement [OFFICIAL].
5. **Integrity**: anonymity leaks, overlap with a prior peer-reviewed version (counts as prior publication; preprints do not) [OFFICIAL], unverifiable references, citation padding.
Verdict: send to review / desk reject / return for revision.

### Step B: two or three reviewer reports (independent agents)
Give the reviewers different profiles, e.g. (R1) application/intelligent-systems reviewer, (R2) methods/statistics reviewer, (R3) experimental-rigour and reproducibility reviewer. Each writes:
1. Summary of the paper in 3–5 sentences (proves they understood it).
2. Major issues (numbered, each with location, why it matters and what would fix it).
3. Minor issues (wording, figures, references; no spelling nitpicks — recommend editing instead [OFFICIAL]).
4. Answers to the checklist below.
5. Recommendation with a one-paragraph justification and confidential comments to the editor.

**Reviewer checklist** (Elsevier criteria [OFFICIAL] + recurring ESWA criticisms [COMMUNITY/VENDOR/INFERENCE]):
- Title and abstract accurate, with main results and limitations; significance reported for main findings.
- Introduction: application stakes, clear gap, explicit contributions that the experiments actually support.
- Related work current (last 2–3 years), includes the closest competitor and relevant ESWA work; differences stated precisely (a comparison table helps).
- Method replicable: notation, algorithm, hyperparameters, data splits, how choices were fixed.
- Theory: assumptions stated, proofs complete, guarantees match what is evaluated.
- Baselines: recent and strong, fairly tuned, same inputs; oracle advantages disclosed.
- Statistics: repeated runs, CIs/effect sizes, appropriate tests (corrected for dependence), no claims from non-significant differences.
- Ablation, sensitivity to key parameters, robustness to another dataset/model.
- Computational cost / complexity / API cost; scalability.
- Practical value: who deploys it, what it saves, guidelines, failure modes ("where it does not help").
- Limitations section honest and specific.
- Reproducibility: code and data deposited (not "on request"); anonymized during review.
- Figures/tables readable, captions self-contained, no duplication.
- References real, complete, APA style; no self-citation coercion; no padding.
- Highlights and abstract consistent with the paper [OFFICIAL: reviewers check highlights].

### Step C: editor decision and fix plan
Merge the reports into an editor letter (decision + numbered required changes). Then turn every point into a fix: text edit, new analysis from existing results, or an explicit "out of scope, stated in Limitations". Do not add new experiments without the author's approval; never invent results. After fixes, a fourth agent compares the revised text with the original for meaning drift and verifies that every number still comes from the results files.

Log everything in `review_log.md` (Chinese summary for the author, English findings verbatim).

## Mode 2 — helping a human reviewer review an ESWA paper
- Work only from what the reviewer pastes or describes; **never upload the confidential manuscript into a public or non-private AI tool** — if the session is not a private, approved tool, give structure and criteria only [OFFICIAL GenAI policy].
- Produce: summary, major/minor issues, checklist answers, recommendation, confidential note; neutral and specific tone; no demands to cite the reviewer's own work unless scientifically needed [OFFICIAL].
- Remind the reviewer to disclose AI assistance in the comments if the journal requires it, and to declare conflicts before accepting.

## Responding to ESWA reviewers
- The decision letter asks for a point-by-point "Detailed Response to Reviewers" covering the editor's letter and every reviewer comment [OFFICIAL, 2019 letter].
- Upload a clean revised manuscript and one with changes highlighted [COMMUNITY]; cite page and line of every change (keep `lineno`).
- Quote each comment, answer it, show the new text; when an experiment is infeasible, explain why and offer the closest alternative [COMMUNITY].
- Novelty objections: compare point by point with the cited competitor and add the comparison to the paper [COMMUNITY].
- Keep the anonymity of the revised files; the title page stays separate.
- Template: `references/response_template.md`.

## Files
- `references/evidence.md` — the source notes (process, timelines, criteria, criticisms, desk-reject reasons, response practices) with URLs and tags.
- `references/response_template.md` — point-by-point response skeleton.
- `scripts/review_packet.py` — builds a reviewer packet (plain-text manuscript with line numbers, section map, claims-with-numbers list, figure/table captions) from a `.tex` file, so reviewer agents cite exact lines.
