---
name: "information-systems-writing"
description: "Write, restructure or revise a paper for the Elsevier journal Information Systems (data management, CCF B), especially empirical, benchmarking, data-quality, data-cleaning, entity-resolution or reproducibility papers. Covers title, abstract, introduction moves, section plan, results and limitations paragraphs, language register with measured targets, punctuation and parentheses, removing AI-flavored prose, figures and captions, and references. Use together with information-systems-submission (formal requirements) and academic-latex-polish (preservation-safe polishing)."
---

# Writing for Information Systems (IS 专属写作经验)

Use this skill when drafting or rewriting a manuscript for **Information Systems** (Elsevier, ISSN 0306-4379). The norms come from published IS papers in data quality, data cleaning, entity resolution and experimental studies (list and measurements in `references/observed-papers.md`), from the journal's reproducibility guidelines, and from the existing `academic-latex-polish` rules in this repository. Formal requirements (files, declarations, template) live in `information-systems-submission`.

## Language convention (permanent agreement with the author)
- **English** for everything reviewers, editors or the portal will see: manuscript, abstract file, highlights, cover letter, declarations, supplementary descriptions, every text typed into the portal, and responses to reviewers.
- **Chinese (中文)** for every report to the author: progress, check results, step-by-step instructions, decisions needed, and internal notes such as package READMEs and review logs.

## Workflow
1. **Read the paper end to end** and write down, in one line each: the object studied, the question, the evidence, the main findings, and what a reader can reuse. If these five lines are not clear, fix the content plan before polishing sentences.
2. **Snapshot the source** (`cp -r paper paper.orig`) so every number and claim can be checked afterwards with `academic-latex-polish/scripts/check_preserve.py`.
3. **Measure the register** with `scripts/is_style_check.py paper/main.tex` and compare with the targets below.
4. **Restructure** to the section plan below, then rewrite paragraph by paragraph with the rules in "Language" and "Avoid AI-flavored prose".
5. **Redraw or fix figures** with the figure rules; regenerate them from scripts, never edit images by hand.
6. **Rebuild the references** with the reference rules; verify every new entry from a primary source (publisher page, DOI landing page, PVLDB PDF). Never cite from memory.
7. **Re-measure, compile, render pages, and check preservation.** Every number in the old paper must still be present unless the user agreed to remove it. Caveats may be merged but not dropped.

## Title
- 8–14 words. Name the object of study and what was done to it: "The effects of data quality on machine learning performance on tabular data"; "Data Lakehouse: A survey and experimental study"; "SMBench: No-code benchmarking of learning-based entity matching".
- A colon and subtitle are common. A coined system name belongs in the title only when the system is the contribution; study and audit papers use plain nouns.
- Put the community's search terms in the title (data cleaning, data repair, entity resolution, benchmark, data quality). Avoid private vocabulary ("comparison contract", "authority") unless it is defined in the abstract.

## Abstract (one paragraph, at most 250 words)
Order: context (1 sentence) → problem and why it matters (1–2) → what was done, with counts of systems, datasets and runs (2–3) → the two or three findings a reader should remember, with at most a few key numbers (2–3) → what this means for practitioners or evaluators and what is released (1). Published IS empirical abstracts state counts of the things studied and use few result decimals. Do not end on a disclaimer; put scope limits in one clause.

## Section plan for an empirical or audit paper
1. **Introduction** (6–10 paragraphs): context → problem → a concrete example that shows the problem → gap in prior work, naming two or three studies → approach and scope ("We limit the study to ...") → headline findings in plain words → "Contributions." with 3–5 bullets, each a noun phrase or starting "We ..." → one-paragraph outline of the paper.
2. **Background and related work** early when the reader needs it to follow the study; otherwise near the end. Group by research line, not by paper; finish each group with one sentence that positions this work.
3. **Method or procedure**, with defined terms introduced once with `\emph{}` and used consistently.
4. **Experimental setup**: hardware, software versions and commits, datasets with a size table, parameters, repetitions, and how results are scored.
5. **Results**, one subsection per question or system. Open each paragraph with the observation or with what a figure shows; give the number after the claim; close a group with one "Overall, ..." sentence.
6. **Discussion / implications** for people who build or evaluate systems.
7. **Limitations and threats to validity**: one place, concrete, each limit attached to the claim it limits. Do not repeat the same caveat in every section.
8. **Conclusion**: findings in two or three sentences, then a short list of future work.
9. Declarations and data availability, then references, then appendices.

## Language (measured targets)
Published IS papers in this area measure as follows (body text): mean sentence length 20–26 words, 10–20% of sentences above 35 words, 1.0–1.8 parentheses and 0–0.5 semicolons per 100 words, frequent "we", hedges at most about 0.2 per 100 words. A draft at 15 words per sentence reads clipped; one at 32 reads dense. Rules:
1. **One idea per sentence, but not one clause per sentence.** Merge runs of short sentences that share a subject with "and", "because", "so that", "while", "which".
2. **Paragraphs open with their point.** The first sentence states the finding or the purpose; evidence follows; a paragraph does not end with an unrelated caveat.
3. **Claim, then number.** "Positional comparison flags 24 and 31 cells in two configurations that contain no events."
4. **Plain verbs.** show, measure, compare, observe, find, use, report. Prefer "we measure" over "the measurement is performed".
5. **Present tense for results and for what the paper does; past tense for what was run.**
6. **Terms.** Define a new term once and keep it. Do not coin several abstract nouns for related ideas. Prefer the field's words (row correspondence, ground truth, error detection, data repair) over private ones.
7. **Semicolons.** At most one per paragraph; never "X; Y; Z" chains.
8. **Parentheses.** Not more than one per sentence and never nested. Keep them for an abbreviation at first use, a compact statistic after its claim, a short e.g. list, or a pointer to a figure or section. Turn other asides into a clause or a separate sentence. No parentheses in section headings or highlights.
9. **Negation.** State what holds. A sentence that only says what the paper does not claim belongs in Limitations, once. Limit "not X but Y", "rather than" and "instead of" to where the contrast is the point, roughly once per page.
10. **Numbers.** Thousands separators (1,085), en dash for ranges (2016--2020), percent with a number (0.633 percentage points). Spell out one to nine in running text unless they are measurements.
11. **Spelling and punctuation.** Pick American or British spelling and keep it. `e.g.,` and `i.e.,` with a comma; Oxford comma used or not used consistently; `--` for ranges, `---` without spaces for a dash, used sparingly; LaTeX quotes ``like this''.

## Avoid AI-flavored prose
`scripts/is_style_check.py` flags these. Remove or rewrite every hit unless it is a quotation or a defined technical term.
- **Words:** delve, crucial(ly), notably, importantly, it is worth noting, landscape, underscore(s), pivotal, seamless(ly), comprehensive, robust (unless measured), nuanced, shed(s) light, pave(s) the way, in the realm of, testament, leverage (use "use"), harness (except "test harness"), holistic, intricate, multifaceted, meticulous(ly), tapestry, navigate (figurative), unlock, empower, elevate, foster, streamline.
- **Structures:** em-dash chains; habitual triplets ("fast, accurate, and scalable"); "not only ... but also" in every paragraph; meta-commentary ("this section does not claim", "we deliberately", "importantly, we note", "it should be emphasized"); stacked hedges ("may potentially suggest"); sentences that start with "This" plus an abstract noun repeatedly ("This boundary ...", "This distinction ..."); colon-led slogans ("The result: ...").
- **Codes and versions:** internal project codes (P19), file versions (v5, v7), "version-3 certificate", and the name of a previous target journal never appear in text, tables, captions or supplement names. Describe artifacts by function.
- **Over-defence:** a reviewer reads repeated disclaimers as uncertainty. Each limitation appears once in the body where it bites and once in Limitations.

## Figures
- **Every figure earns its place**: a mechanism diagram the text cannot replace, or a plot that shows a comparison or trend faster than a table. Do not draw a figure that repeats a table.
- **Schematics**: flat vector, thin dark-gray lines, white background, one accent colour for the part that matters, no shadows, gradients or 3D. Short labels inside boxes (at most about six words), full explanation in the caption and text. Avoid slash-separated label strings ("agree / disagree / unknown"); use words or a legend.
- **Plots**: sans-serif fonts at 7–9 pt at final size, axis labels with units, colour-blind-safe palette that also prints in grayscale, direct labels instead of legends where possible.
- **Size**: design at final width (single column about 90 mm, full width about 190 mm; in `preprint` layout `\linewidth` is about 140 mm) so that text is never scaled below 7 pt.
- **Format**: vector PDF with embedded fonts; raster at 300 dpi or more. Keep the drawing script in the supplement.
- **Captions**: start with a noun phrase that names what is shown (5–15 words), then at most two sentences that define symbols or say how to read it. Do not put the finding's caveats in the caption. Table captions go above tables, figure captions below figures.
- **Tables**: booktabs three-line style, no vertical rules, units in headers, right-aligned numbers, the same abbreviations as the text.
- `assets/is_figure_style.py` sets matplotlib defaults that follow these rules.

## References
- Numbered style (elsarticle-num) with DOIs; 30–90 references is typical, mostly PVLDB, SIGMOD, ICDE, EDBT, TKDE, VLDB Journal and Information Systems itself.
- Cite the community whose reviewers you want: for data cleaning, the standard evaluation studies and benchmarks; for reproducibility, the journal's own reproducibility editorial (Chirigati et al., Inf. Syst. 59 (2016) 95–97).
- Cite related IS papers only when they are genuinely related; never pad.
- Software and data: cite repository, commit and access date; prefer a DOI from Zenodo or Mendeley Data when available.
- Preprints are labeled as arXiv preprints with identifier and year.
- Verify each entry against a primary source and record where it was verified; keep author order and venue names exact.
- Use "et al." with a name when the citation is the sentence subject ("Ni et al. [12] benchmark twelve repair algorithms"); do not use a bare "[12] shows".

## Highlights (Elsevier)
3–5 bullets, each at most 85 characters with spaces, each a complete finding or contribution in plain words, no parentheses, no undefined abbreviations.

## Reviewer-driven lessons (2026-10, audit paper for IS)
- **Every title term must be defined in the body.** A title phrase such as "comparison contract" that never reappears leaves the reviewer unable to map title to content; define it in the introduction and formalize it in the method section.
- **Join the halves.** If a paper has two case studies from different settings, say in the introduction why both are there and give a short primer on the less familiar setting before its section.
- **Give practitioners something to do.** End the findings paragraph of the introduction with a short list of recommendations, each bounded to the audited versions and each tied to a measured result; never recommend beyond what was measured.
- **Collect provenance in one table.** Protocol dates, amendments, exploratory status and blinding scattered across sections read as defensive; a study-by-study chronology table lets the text stay short.
- **Define overloaded words once.** Terms such as native, adapter, consumer, materialization, endpoint, witness and independent need a terminology paragraph.
- **Disclose AI used in the research process in the method section**, not only in the writing declaration.
- **Cite supplements by number** where the corresponding analysis is described.

## Rewrite pitfalls (caught by an independent check in 2026-10)
Rewriting for flow silently changes claims. After every rewrite, have a separate agent that did not write the text compare old and new section by section. Typical shifts:
- **Modal loss:** "can fail" becomes "fails", "supports changing" becomes "calls for", "do not determine" becomes "cannot determine", "cannot independently certify" loses "independently".
- **Quantifier creep:** "alone cannot decide all four" becomes "cannot decide"; "makes conclusions replayable" becomes "replays every conclusion".
- **Gap overstatement:** "prior studies take X as given" when the original concedes that prior work already audits X. State the narrow gap the paper actually fills.
- **Citation drift:** a paper cited for "effect of cleaning" when it studies data quality; "on these inputs" when the cited study used other datasets; "at a larger scale" or "shows" where "raises a related concern" or "suggests" is accurate.
- **Dropped caveats in captions and abstract:** the closing scope sentence of the abstract and caveats inside captions disappear first; restore them.
- **Causal connectives:** "since" or "so" inserted where the original only juxtaposed two facts.
- **Moved limitations:** a limitation moved from a specific subsection into the conclusion widens its scope; keep it where it applied.

## Checklist before handing back
- [ ] `is_style_check.py` within targets or deviations justified.
- [ ] No AI-tell words, internal codes or previous-journal traces.
- [ ] Every number and claim preserved (`check_preserve.py`), caveats merged not dropped.
- [ ] Independent reviewer agent compared old and new text for meaning shifts; all fixed.
- [ ] Introduction has the eight moves; contributions list present.
- [ ] Figures regenerated from scripts, captions noun-phrase first.
- [ ] New references verified from primary sources.
- [ ] Compiled twice, no undefined references, pages rendered and read.
