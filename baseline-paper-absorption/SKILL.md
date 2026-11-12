---
name: "baseline-paper-absorption"
description: "Process skill for absorbing how accepted baseline and venue-sample papers write: titles, section outlines, caption claims, table marks, citation placement and limitation phrasing. Produces a reusable notes file in a fixed template, then optionally updates a venue writing skill. It does not invent a census that was not actually read. Use before writing or rewriting a venue skill, or when the user asks to study accepted papers’ writing (吸收已发表写法 / 基线论文结构 / 图题与引用习惯 / 会刊写作样本)."
---

# Baseline-paper absorption (process)

This is a **process**, not a claim that a new sample was already read. The workflow in the Feishu “做顶会文章通用” note is: survey the venue’s preferences → absorb how published papers write → then innovate and experiment → then freeze a venue skill. Plaintext keys that may appear in that note must **never** be copied.

Existing evidence you may reuse, and must not pretend to have redone:

- `write-icde` and `survey-icde`: 1058 ICDE titles, plus deep-reads documented in those skills’ `references/`.
- `results-presentation-review` S01–S11 and the co-author lessons in `review-icde`.
- Official CFPs (always re-read; dates go stale).

If you have **not** deep-read a new set of PDFs this turn, say so in the notes file and in any skill you edit. Do not write “21 VLDB papers were read” unless the list and per-paper notes exist.

## Language
Notes that will feed a venue skill: **English** (so they can be pasted into SKILL.md). Author-facing summaries: **Chinese**.

## 1. Select the sample (before opening PDFs)

1. Name the venue, year range, and track (research, industrial, EA&B, journal regular).
2. Take the list from the **official** proceedings or journal TOC, not from memory. If DBLP or a crawler fails, stop and record the failure; do not invent titles or counts.
3. Decide a budget (for example 8–15 papers): include the closest baselines to **this** manuscript, plus 3–5 recent papers in the same subject area, plus 1–2 EA&B papers if relevant.
4. Record bibkeys, official URLs, and how each PDF was obtained (open HTML, author copy, existing local file). Do not commit copyrighted PDFs to a public repo.

## 2. What to extract (per paper, same template)

Create one notes file `references/absorbed/<venue>-<year>-<shortkey>.md`:

```
# <citation key> — <title>
Venue, year, track, pages (body / refs), official URL. Access date.

## Title pattern
Literal title. Pattern tag (Acronym: claim; Claim: setting; EAB label; …).

## Abstract moves (one line each)
Context / gap / “we present” / insight / components / evidence / artifact.
Headline numbers, copied verbatim. Any loss sentence? (should usually be none)

## Section outline
Numbered section titles only, with approximate pages if visible.

## Figure and table habits
For each figure/table: caption’s first sentence (claim or not?); winner marks (bold / underline / none); count row (yes/no); units; colour-blind usable (yes/no/unknown).

## Citation habits
Where related work sits (after intro vs after experiments). How the paper differs from the closest work (quote the distinguishing sentence). Conference-vs-journal lineage cited?

## Limitations
Where stated (experiments only / discussion / not at all). Does the abstract or conclusion self-negate? Are losing cells kept?

## What we will copy, and what we will not
Copy: concrete habits that match Deng S01–S11 and the official CFP.
Do not copy: topic-specific claims, any number we did not verify, any style that hides losses.
```

## 3. Aggregate only after every paper has a file

Write `references/absorbed/<venue>-summary.md`:

- Counts: median title length, abstract moves, where related work sits, fraction with count rows, fraction with claim-first captions.
- **Mark the sample size and the date.** A summary of 8 papers is not a 1058-paper survey.
- Conflicts with Deng’s rules or with the official CFP: the CFP and Deng win; record the conflict (accepted papers sometimes violate a rule we still want to keep).

## 4. When (and when not) to update a venue skill

- New official dates or page limits: update `references/official-rules.md` and the SKILL.md “official constraints” section, with the access date.
- New writing habits with a real sample: add an “Observations (N papers, date)” subsection. Do not overwrite ICDE observations with VLDB guesses.
- **Never** delete existing skills or rewrite write-icde from this process. **Never** push to `main` of `claude-skills`; open a PR on a new branch.
- If the user asked only for absorption notes, stop at the notes files; do not silently invent a new skill.

## 5. Integrity

- Do not quote substantial copyrighted prose into a public skill; paraphrase habits and keep quotations short (title, a caption’s first sentence, a distinguishing clause).
- Do not absorb “less honest disclosure” even if an older internal prompt said so. It contradicts Deng and the current author instruction.
- Enterprise or personal text from chats and internal docs is **not** a writing baseline for a paper.
