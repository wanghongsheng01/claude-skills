---
name: "review-ipm"
description: "Simulate how Information Processing & Management (IPM, Elsevier) screens and reviews a manuscript: editor desk screen (intersection of computing and information science, manuscript type, transferable insight, anonymity including public preprints, package), independent reviewer personas (contribution, methods and statistics, annotation reliability, open science), likely reviewer questions, decision letter and fix plan; also helps a human reviewer and structures responses to reviewers. Use before submitting to IPM or when revising after IPM reviews (审稿 IPM / Review-IPM / 模拟 IPM 审稿)."
---

# Review-IPM: how to simulate IPM's screen and review (IPM 审稿指南)

Evidence: IPM Guide for Authors (read 2026-10-31), Elsevier reviewer guidance and rejection material, editor statements, published IPM papers, small crowd reports, and methods literature on evaluation, annotation and preregistration. **No public IPM reviewer form, report or desk-rejection letter was found**, so this is a checklist assembled from those sources, not a description of IPM's form. Tags: [IPM], [ELSEVIER], [GENERAL], [3RD-anecdote], and +inferred. Sources are in `references/evidence.md`.

## Language convention
Review reports and responses to reviewers in English; reports to the author in Chinese (中文).

## Process facts
- Double anonymized; editor screen, then typically at least two reviewers; editors decide [IPM].
- First decision 2–5 days, decision after review about 61–66 days, acceptance about 145–154 days, depending on the snapshot [IPM]. Crowd reports are slower and dominated by rejected authors [3RD-anecdote]. Plan for 2–3 months to a first review decision [+inferred].
- Acceptance rate: no official figure. Plan for a selective journal.
- Editor in Chief Bernard (Jim) Jansen, since 2016. He describes IPM as a flagship information-science journal with a broad remit [IPM]. His 2026 tutorial outline names fit, cover letters, desk review and revising without overcorrecting [IPM].
- Recommendations: accept, minor or major revision, reject, with separate comments to the editor [ELSEVIER].
- A desk-rejected paper resubmitted as new can be desk rejected again [3RD-anecdote].

## Mode 1: pre-submission self-review
Use agents that did not write the text. Give each the compiled PDF or `.tex` and this file, and ask for line-numbered findings.

### Step A: editor desk screen
PASS / RISK / FAIL with a one-line reason each:
1. **Fit:** does page 1 show the computing and information-science intersection? Which of research, methods, review or critical application is it?
2. **Insight:** does the abstract state a transferable finding and a recommendation, or a benchmark report? [+inferred]
3. **Novelty:** is it already known from the closest work? [ELSEVIER]
4. **Anonymity:** can a reviewer identify the authors through a tool name, repository, preprint or self-citation? The guide says submissions should not be preprints before a final decision [IPM].
5. **Package and language:** guide followed; structure clear [ELSEVIER].
6. **Integrity:** undisclosed overlap, public copies, AI use, unverifiable references.

Verdict: send to review, desk reject, or return.

### Step B: independent reviewer reports
Personas: (R1) information-science contribution reviewer; (R2) methods and statistics reviewer with access to released results; (R3) annotation and LLM-evaluation reviewer; optionally (R4) open-science reviewer. Each writes a summary in 3–5 sentences, numbered major issues (location, why, fix, whether new experiments are needed), minor issues, answers to the questions below, a recommendation and confidential comments.

**Elsevier criteria** [ELSEVIER]: title accurate; abstract with major results and limitations; rationale and objectives; replicable methods; suitable tables, intervals and effect sizes; conclusions supported, limitations acknowledged; references current; novelty; insufficient data and non-significant variation presented as meaningful count as major flaws.

**Contribution** [+inferred]
- What does this tell information-science readers that they did not know?
- Why does the error or effect matter to users, data stewards or organisations?
- Which construct is extended: relevance, data quality, trust, measurement validity?
- Would the conclusions hold for another benchmark, domain or model generation?
- Who changes what practice? Is every implication traceable to a specific result?
- Is there a "theoretical and practical implications" section? (Pattern in recent papers, not a rule.)

**Methods and statistics** [GENERAL]
- How was the sample chosen; is its size justified; is it weighted to the population generalised to?
- Are items clustered by database, question or template? Do intervals respect that? Is the test paired?
- Effect size or only significance? Multiple comparisons?
- Does the gold standard have error, and how does that bias the result?
- Sensitivity to another metric, prompt, seed or model version?

**Annotation** [GENERAL]
- Who are the annotators; training and codebook; blind to model and to each other?
- Which coefficient and why? Fleiss assumes randomly sampled raters per item; fixed raters may call for Conger's κ (confirm in Fleiss 1971 or Gwet before citing).
- Per-class values, prevalence, raw agreement, interval? κ falls under skewed marginals; AC1 is a debated alternative. Report rather than swap.
- Thresholds: McHugh treats κ below 0.60 as inadequate for health research; state which scale is used.
- Was adjudication before or after agreement? Prompt frozen before validation? LLM-human compared with human-human on the same items? Version, temperature, repeat stability?

**Open science** [GENERAL]
- Is the preregistration time-stamped before data access, and readable anonymously? Is it external or internal?
- Every deviation listed? Exploratory analyses labelled? Undisclosed deviations are common and draw scrutiny (Claesen et al. 2021).
- Data and code available during review without exposing identity?
- AI in research in Methods; AI in writing in the declaration [IPM, ELSEVIER].

### Step C: editor decision and fix plan
Merge the reports into a decision letter. Turn every point into a text edit, a new analysis from existing results, or an explicit limitation. List experiments that require new data for the author's decision instead of running them unasked. Re-run the desk screen; fit should move from RISK to PASS.

**Integrity pass.** Have one agent check every claim in the abstract, highlights, results and conclusion against macro files and released results. When a limitation has been shortened, check that the headline claim is still read correctly without it.

## Mode 2: helping a human reviewer
Work only from what the reviewer describes. Never upload a confidential manuscript to a public AI tool [IPM]; the July 2026 Elsevier policy is stricter than its undated how-to page, so follow the stricter one. Give structure, neutral tone, no coercive self-citation. Declare conflicts before accepting.

## Responding to IPM reviewers
Point-by-point response in `references/response_template.md`; quote each comment, answer it, cite page and line; keep files anonymous; avoid overcorrecting.

## Files
- `references/evidence.md`: sources, tags, kappa bands, timing data, unverified items.
- `references/response_template.md`: response skeleton.
- `scripts/review_packet.py`: builds a reviewer packet (numbered plain text, section map, claims with numbers, captions) from a `.tex` file.
