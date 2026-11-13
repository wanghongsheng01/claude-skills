---
name: pvldb-paper-craft
description: "Use when drafting, polishing, layout-checking, or doing a pre-delivery review of a PVLDB or SIGMOD paper: the end-to-end production pipeline (problem selection, SOTA positioning, method, experiments, figures/tables, writing, self-review) and how each step is done; the reviewer's 10–20 minute skim in the order tables → figures → experiment analysis tied to each figure/table → title/abstract/intro, and how to optimise for that skim; full paper anatomy, paragraph organisation, writing conventions, and a grounded what-NOT-to-write list; formula/figure/table/reference checklists; Volume 20 mandatory blocks; and a PDF layout lint (overlap, margin overflow, unreadable tables). Complements write-pvldb (limitation wording, W/T/L, section prose) and submit-pvldb (official calendar, caps, CMT). Use for 论文工艺 / 版式检查 / 审稿人速读 / 交付前自审 / 正文重叠 / 公式溢出 / 表格字号 / paper craft."
---

# PVLDB paper craft (production pipeline, reviewer skim, layout)

This skill is about **how a formally published PVLDB / SIGMOD paper is produced, skimmed, and visually finished**. It does not replace:

- `write-pvldb` — limitation wording without self-negation, W/T/L tables, section-level prose patterns;
- `submit-pvldb` — official Volume 20 rules, deadlines, author caps, CMT, COI (official pages always win);
- `review-pvldb` — simulated review on official dimensions.

Manuscript, captions and revision letters are in **English**. Author-facing checklists may be in Chinese.

**Integrity.** This skill changes placement, wording, layout and what is emphasised. It does **not** change measured numbers, hide losing cells, or invent citations. A sentence that contradicts its own tables is a rejection reason.

Evidence below is from formally published PVLDB 2023–2026 papers (and two SIGMOD papers on the same scientific neighbourhood: SQL equivalence, query rewrite, NL2SQL, EA&B). Treat arXiv-only or placeholder-template PDFs as facts-only, never as layout exemplars.

---

## 1. Paper production pipeline

Produce the paper in this order. Writing (step F) comes after the tables can already survive a reviewer skim (steps D–E). Skipping G is how a complete scientific draft is delivered looking unfinished.

### A. Problem selection and bounding

- Pick a scientific problem the venue already recognises, or (EA&B) a clearly named evaluation object (a full pipeline, a system class, a leaderboard protocol).
- Bound the fragment / setting in a sentence that later becomes a theorem hypothesis or a protocol premise (QED: a parameterised query fragment plus “assuming a complete first-order theory solver”; LLM-R2: Executability / Equivalence / Efficiency).
- Prove the gap with a **concrete failure**, not a slogan: a real Calcite rule that prior checkers cannot prove (QED §2); a U-expression with unbounded summation that prior provers handle only heuristically (SQLSolver); a 50-query sample in which existing engines fail 54% (WeTune). If the inherited benchmark is contaminated (identical pairs, annotation errors), say so and rebuild or re-annotate before claiming SOTA.
- Deliverable of this step: one paragraph that states input, output, correctness, and the exact prior failure.

### B. SOTA and benchmark positioning (before writing, honoured in the tables)

- List **living** strongest systems in the same problem (for SQL equivalence: UDP, EQUITAS, SPES, WeTune, SQLSolver, QED — whichever applies), not retired proxies.
- For every omitted baseline, write one clause of reason in Setup (“limited support for …”, “fine-tuning is out of scope because …”).
- Fix the comparison protocol in writing: SQLSolver compares any two provers only on pairs **both** can attempt; QED rebuilds Calcite-New after dropping trivial identical pairs. Fairness sentences belong in Setup, not in a rebuttal.
- EA&B: freeze the protocol (datasets, metrics, hardware, selection rationale). Rankings may be **conditional** (“on PostgreSQL/JOB/HIV rewriter at 1 GB”). A single-stage ranking that is “locally valid but globally misleading” is a finding (MV Rewrite Bench).
- Deliverable: a skeleton of the main table (rows = living baselines + this method; columns = headline metrics) with empty cells to fill.

### C. Method design (example → formalism → algorithm → scope in the theorem)

- Start from one end-to-end example that will become Figure 1 or §Overview (QED’s Calcite pushdown; SQLSolver Figure 1: an equivalent pair existing solvers cannot prove).
- Name every component with a stable noun that will recur as (i) a method subsection title, (ii) a column of the ablation table, (iii) the subject of a “This is because…” sentence (Sphinteract: Simple / CQs / CQs & ES; QED: Normalization / Linearization / Unification; LLM-R2: Demonstration Selection / Curriculum).
- Define symbols at first use. Put the range of a completeness or complexity claim **inside the theorem statement**, not in a later paragraph that retracts it.
- Deliverable: component list + example + the claims each component is responsible for (the quantity it is allowed to move).

### D. Experiment design (attributable by component)

Required Setup, written once: datasets and why; living baselines and omission reasons; metric definitions; hardware; fairness protocol; seeds / temperature; cost units and date if money is reported; repetitions and dispersion.

Then one subsection per RQ / Exp, built so a reader can answer “which **component** moves which **metric**”:

1. The question names the component.
2. “Table k and Figure n report the results.”
3. Read the table: who wins, on which dataset, by which delta — numbers identical to the cells.
4. Mechanism: “This is because…” (Sphinteract, ParSEval), wall-clock split onto algorithm numbers (QED Table 2: 0.83s on Alg. 5, 0.03s on Alg. 6), “Takeaways. (RQ1/RQ3)” (MV), boxed Finding (Dawn), “In summary,” (DAIL-SQL). The component name must match step C.

Own failures and costs sit **in this section**, next to the number, with a mechanism and a bound (“the slowdown is within one order of magnitude”; “higher rewrite latency … offset by the larger reduction in execution time”). They are not a first-level “Limitations” section in 2023–2026 PVLDB method papers (0/10 in the craft corpus). Plugin-style claims (REDSQL) use a host ± method table and a “consistently helps” sentence, not a single champion row.

EA&B: Insights / Lessons are operating guidance about **systems under test** or about the protocol; they may refuse a blanket winner (Dawn Finding 1). That is a finding, not self-negation.

Deliverable: filled main table, ablation / failure table, and a one-sentence mechanism per table.

### E. Figures and tables, built for the skim in §2

Design the visual centre of the evaluation section **before** polishing prose:

- Main table: `booktabs`; best in **bold** (or a declared colour, as Dawn’s orange/blue SOTA); optional underline for second; this method in a stable place (rightmost column or bottom row); living baselines present; deltas or multiplicative factors visible in the cell (`71.63% (+42.30%)`, `67.3% (+8.8%)`); failures / timeouts as cells or as their own table (QED Table 3, SQLSolver Table 5); **type ≥ 8 pt, never ≤ 6 pt**. Too many columns: split, go full-width, or drop a secondary metric — do not `\resizebox` into unreadability.
- Figure 1 by page 3: a real example or a pipeline that already carries the insight, not an empty architecture box. Later result figures should make “ours is best” or “the finding holds” intuitive without the caption (and the caption should still be self-contained). Dual-encode colour and line type.
- Place the main table at the visual centre of the first results subsection (right column or full-width top), with the Finding / Takeaway boxed immediately under it (Dawn).

### F. Writing, skeleton first

Draft in section order of §3, filling the paragraph patterns there. Abstract 150–250 words, 1–4 headline numbers identical to the main table (median 2–3 in the corpus; a zero-number abstract is legal, as in LLM-R2 / MV / SemBench, but any number that is written must match). Contributions: 3–5 bullets with section pointers; last bullet is the experiment or the finding. Conclusion: short, same numbers, no failure laundry list. Related work: every paragraph ends on “how we differ.” See §4 for what not to write.

### G. Self-review (mandatory; errors must be zero)

Run the four-layer protocol in §6 **before** a coauthor or Overleaf / CMT drop. Layer 0 (compile log + layout lint) and Layer 1 (150 dpi visual pass on **every** page) must be clean. Do not change numbers to “fix” a narrative.

---

## 2. Reviewer-skim checklist (10–20 minutes)

Reviewers do not start at the title. Optimise and self-review in **this order**. Time boxes are typical, not official.

### Pass 1 — Tables only (3–6 min)

For the main table and the ablation / failure table, answer:

- [ ] Do the headline metrics **reach or beat living SOTA**, on a named dataset, against a named system?
- [ ] Is that obvious **from the table itself**: bold or declared colour, stable position of this method, deltas in the cell, consistent decimals and units, type ≥ 8 pt?
- [ ] Are the baselines the **living strongest**, and is every absence reasoned in Setup?
- [ ] Are **losing, timeout, and cannot-prove** cells visible (own failure table or explicit categories), not deleted?
- [ ] For a plugin claim: does every host appear with and without the plugin?
- [ ] For EA&B: is a blanket ranking refused when the data refuse it, and is the condition (engine, workload, metric) in the takeaway?

If a reviewer needs the prose to discover who won, the table is not finished.

### Pass 2 — Figures only (3–5 min)

- [ ] Figure 1, in the first three pages, makes the problem or the insight visible (example or worked pipeline).
- [ ] The main result figure intuitively supports the claim (ours above the others; or the finding’s crossing lines).
- [ ] Caption is self-contained and may carry a one-line takeaway.
- [ ] Axis labels and legends are near body size (≥ 8 pt); colour-blind-safe; nothing clipped or colliding with column text.

If the figure does not work silently, redraw it; do not only rewrite the paragraph.

### Pass 3 — Analysis tied to each table and figure (5–8 min)

Standing on each table/figure, read only the adjacent text:

- [ ] It **names the method component** responsible for the gain, with the **same name** as in the method section and the ablation columns.
- [ ] It uses a mechanism sentence (“This is because…”, time split onto algorithm numbers, Takeaway (RQk), Finding, “In summary,”) rather than “our method is significantly better.”
- [ ] Numbers are copied from the table with the same rounding and dataset name.
- [ ] A loss or cost, if any, sits here, once, with mechanism and bound — not in the abstract or the conclusion.

### Pass 4 — Title, abstract, introduction (3–5 min), last

- [ ] Title: method papers default to `Acronym: … for/of X` or a factual sentence; EA&B may be a question or a finding. No limitation and no number in the title. Volume 20 EA&B submissions append `[Experiment, Analysis & Benchmark]` (removed in camera-ready as the guidelines say).
- [ ] Abstract: about 150–250 words; context → concrete gap → “we present” + “Our key insight is…” → **1–4** numbers with dataset and comparator (or zero numbers, but then no slogans). **No** own-failure list, **no** “first or tied … with no loss.”
- [ ] Introduction: prior failures with examples or measurements; one insight paragraph; 3–5 contribution bullets with section numbers; last bullet honours the experiment or finding. Figure 1 is already on these pages.
- [ ] Every number in the abstract, the last contribution bullet, and the conclusion is the **same** number as in the main table.

### How exemplars optimise this skim (patterns to copy)

- Dawn (PVLDB 17): Tables 3–4 in the right column of the first results page; orange/blue SOTA; SuperSQL at the bottom with `(+0.3↑)`; Finding 1 boxed under the table and **refuses** a blanket win.
- Sphinteract (PVLDB 18): Table 2 full-width at the top of the results page; caption names the SOTA hosts and the DAIL-SQL baseline; every cell is `accuracy (+delta)`; columns are interaction rounds; rows are the method-section components.
- QED (PVLDB 17): Table 1 lists every living checker, this method rightmost and largest; Table 2 splits runtime onto algorithms; Table 3 is **own** unproven cases.
- SQLSolver (PACMMOD 1(4) / SIGMOD 2024): Table 5 “Reasons of verification failure for each prover” attributes wins to a supported-feature component and to the LIA* algorithm; fairness protocol is explicit.
- REDSQL: abstract and last contribution already use `host + absolute + (delta)`; the table is host ± method, so consistency is visible in one glance.

---

## 3. Full paper anatomy

### 3.1 Sections that almost every method paper contains

1. Title; authors; corresponding-author footnote (two marks are allowed; they must **not** collide with the mandatory block).
2. Abstract (its own visual block).
3. **Mandatory PVLDB block**, produced only by `\vldbtopmatter`: Reference Format, CC BY-NC-ND license footnote, Artifact Availability. Set `\vldbdoi`, `\vldbpages`, `\vldbavailabilityurl`, `\vldbshorttitle` (a complete phrase). Do not hand-typeset these. (SIGMOD / PACMMOD use the ACM copyright block instead.)
4. Optional CCS / keywords.
5. **§1 Introduction** — §3.2 pattern; Figure 1 in the first three pages.
6. **§2** in exactly one primary form: (i) Overview + running example, (ii) Background / Preliminaries / Problem, or (iii) Related Work placed early, each paragraph ending on a difference.
7. **Method** (two to four sections): representation, algorithms, theorems. Subsection titles = later ablation names.
8. **Evaluation / Experiments** — Setup once, then one subsection per RQ, takeaway under each main table. Typically 20–40% of a method paper’s body; 25–55% or more for EA&B. Never so short that the only table is unreadable.
9. Related Work if not already in §2.
10. Optional Discussion (practical recommendations).
11. **Conclusion**, one or two short paragraphs; optional one or two testable future directions. Recent PVLDB method papers do **not** use a first-level “Limitations” heading about their own method (see `write-pvldb` for how to state a loss when you must).
12. Acknowledgments; References (**excluded** from the 12-page body). Appendices **count** toward the 12 pages.

**EA&B variants.** The title may be a question, a finding, or “Benchmarking / A Benchmark for …”. Contributions may be followed by a “Summary of findings.” A traditional method section is optional (experiment design can follow the introduction, organised by Q1–Q3). Lessons target systems under test or operating guidance, not “our benchmark is weak.”

### 3.2 Paragraph organisation and language

**Abstract (6–10 sentences, four beats):** (1) why the task matters — do not spend three sentences on “with the rise of LLMs”; (2) a **concrete** prior gap; (3) “we present X” and “Our key insight is…” with one or two mechanism nouns (Q-expressions, LIA*, SRA), no pseudocode; (4) 1–4 numbers aligned with the main table.

**Introduction (about 1.5–2.5 pages):** stakes (industry numbers only with a citation); two to three paragraphs that each take one prior system and one concrete failure; a standalone insight paragraph; 3–5 contribution bullets (“In sum:” / “Our contributions are…”), last bullet = results; optional roadmap sentence. Do not finish the whole Related Work twice.

**Each method subsection (about three paragraphs):** the slice of the problem this component owns; definitions and algorithms; a forward pointer to the quantity the experiments will move.

**Each experiment subsection (four beats):** question names a component; pointer to Table/Figure; read the numbers; mechanism sentence that calls back to the method section. Setup is not repeated.

**Related Work paragraph:** topic → representative systems → “However / In contrast” → what this paper adds. Not an annotated bibliography.

**Conclusion:** what was done + the same 1–3 numbers as the abstract. A future-work sentence is optional and short. Do not re-list failures (even WeTune, which has a 2022 SIGMOD Limitations section before the conclusion, keeps the conclusion short and positive).

**Sentence craft.** Topic sentence first, number in the middle, mechanism last. Prefer “successfully optimizes 247 queries … resulting in substantial …” over “substantial” alone. Present tense for what the paper proposes; past tense for runs performed. “First” and “SOTA” only when a public table or leaderboard can be checked. Plugin claims use “consistently helps all evaluated approaches.” `\vldbshorttitle` must be a publishable phrase, never a truncated mid-word.

### 3.3 What NOT to write (grounded)

These are not style preferences. They are patterns **absent** from the formally published corpus, or present only as cautionary formally-published flaws, or observed as pre-delivery defects.

**Abstract and introduction**

1. Do not pack 20+ numbers, a second dataset’s full metric suite, or “first or tied … with no loss” into the abstract. Corpus abstracts are ~156–239 words with a median of 2–3 result numbers; **0/12** put an own-failure list or “with no loss” in the abstract.
2. Do not put own-failure categories in the abstract, the contribution list, or the conclusion. They belong in an evaluation table (QED Table 3).
3. Do not use “we carefully / we make a first attempt / we preliminarily explore” as the insight. The insight is a mechanism noun.
4. Do not put “our limitations are…” in the contribution bullets. Dawn’s “there is no clear winner” is a finding about **compared** methods.
5. Do not write a slogan the main table cannot verify (“fully solves”, “no loss on any dataset”, “always best”).
6. Do not paste the same long number list in abstract, introduction and conclusion; keep the **wording** consistent and let the conclusion be shorter (SQLSolver’s conclusion does not even repeat 346/359).

**Method and theory**

7. Do not open a display formula with undefined symbols.
8. Do not let a display formula or a broken `cost(p).` run into the gutter or past the right margin.
9. Do not crush an algorithm box into the neighbouring column.
10. Do not preview “experiments will show we comprehensively outperform” inside the method section.

**Tables, figures, analysis**

11. Do not shrink the main table to 6 pt, or stack four unreadable tables on one late page. One main table (or a pair) per results page, near body type, is the published habit.
12. Do not make the best cell a treasure hunt: bold, declared colour, underline, or a rightmost maximum, and **say the rule** in the caption (“Best results are bold.”).
13. Do not use a dead or quietly dropped baseline as the SOTA foil.
14. Do not show only winning cells.
15. Do not write “significantly better” without naming the component.
16. Do not use a decorative architecture diagram with no input/output as Figure 1.
17. Do not allow column text to collide (two-column overlap is a first-minute reject cue).
18. Do not paraphrase a table’s numbers with a different rounding or dataset name.

**Related work, conclusion, limitations**

19. Do not write Related Work as a commented bibliography; end every paragraph on a difference. Do not write the same survey twice.
20. Do not add a first-level “§ Limitations” about **your own** method in a 2023–2026 PVLDB paper (0/10 in the craft corpus). Place the loss in the experiment that measures it. Older SIGMOD / early PVLDB independent Limitations sections are not a Volume 20 requirement. How to word a loss: `write-pvldb`.
21. Do not self-evaluate (“would not survive review”) and do not generalise from the rare conclusion that uses the word “limitation” about itself (one paper in twelve, and it immediately offsets the cost with a measured gain).
22. Do not close with a five-item wish list. At most one or two testable directions; many excellent conclusions have none.
23. Do not apologise for the benchmark’s leftover capacity; state the scope once and, if true, that the leftover is headroom (SemBench).

**Format and delivery**

24. Do not hand-write the PVLDB Reference Format, the license footnote, or Artifact Availability. Omitting `\vldbtopmatter` is a desk-reject risk.
25. Do not let corresponding-author footnotes collide with that mandatory block. Two corresponding authors are legal; overlap is not.
26. Do not truncate `\vldbshorttitle` or leave half-words (“Path ill”).
27. Do not treat the appendix as free pages — it counts toward 12.
28. Do not change experimental numbers to avoid a limitation sentence.
29. Do not copy layout from a placeholder PVLDB template or an arXiv manuscript.
30. Do not deliver a PDF that has not been read at 150 dpi on every page and whose `.log` has not been read.

---

## 4. Section-by-section writing skeleton

- **Title.** Method: `{Acronym}: {mechanism} for/of {task}` or a factual sentence. EA&B: benchmarking phrase, question, or finding; submission suffix as in `submit-pvldb`. One or two lines; no limits, no numbers.
- **Abstract.** Four beats of §3.2; then check word count, at most four numbers, every number sits in the main table, no own-failure list. Print abstract, last contribution bullet, conclusion, and the main table side by side.
- **Introduction.** Six slots: task and stakes; prior failures with examples; insight; contributions; optional roadmap; Figure 1. Do not finish the method here.
- **Preliminaries / Overview / Problem.** Symbols; one worked example; inputs, outputs, correctness.
- **Method.** Subsection titles = ablation columns. Algorithm boxes numbered, with Input/Output. Theorem hypotheses include scope.
- **Experiments.** Setup → RQ1…RQk (four beats) → optional failure table → optional case study. Main table at the visual centre of RQ1. Plugin work uses host ± method. EA&B freezes protocol and conditions every ranking.
- **Related work.** Three to six classified paragraphs, each ending on a difference. Actively declare related submissions as `submit-pvldb` requires.
- **Conclusion.** Five to eight sentences, numbers aligned, optional one or two future directions.
- **References.** ACM Reference Format via the official template: authors, year, title, In Proceedings or journal, pages, DOI. In-file consistency of venue names. Zero undefined or multiply-defined labels.

---

## 5. Formula, figure, table, and reference checklists

### Formula

- [ ] Every symbol is defined at first use and keeps one meaning.
- [ ] Displayed equations use `equation`/`align`; number only those you cite. Inline math does not break across a margin (`cost(p).` must stay inside the column).
- [ ] After compile: no formula in the gutter or past the right edge; accents and subscripts do not collide with the next line.
- [ ] Algorithms: numbered, Input/Output, readable line numbers, type at least ~80% of body size, no column collision.
- [ ] Theorems, lemmas, definitions numbered via `\label`/`\ref`, never by hand.

### Figure

- [ ] Figure 1 by page 3 is an example or a pipeline that carries the insight.
- [ ] Caption is self-contained; optional one-line takeaway.
- [ ] Labels ≥ 8 pt (below 6 pt is a warning at most, and only inside dense diagrams).
- [ ] Colour and line type dual-encoded; this method’s curve is the most visible.
- [ ] Vector preferred; rasters ≥ 300 dpi; no collision with body text; subfigures labelled (a)(b) in both art and caption.
- [ ] A silent look at the figure supports the claim; if not, redraw.

### Table

- [ ] `booktabs`; clear multi-level headers.
- [ ] Best in bold (or declared colour); second optionally underlined; rule stated in the caption or text.
- [ ] This method in a stable place; all living baselines present; absences justified.
- [ ] Deltas or factors in the cell; units and decimal places consistent; dispersion in parentheses or a note.
- [ ] Failures / timeouts visible.
- [ ] **Type ≥ 8 pt (never below 7 pt; 6 pt is an error).** Split rather than `\resizebox{\linewidth}{!}{...}`.
- [ ] Main table at the visual centre of the first results subsection, not only on the penultimate page.

### References and cross-references

- [ ] `.log` has zero undefined citations, undefined references, multiply-defined labels.
- [ ] Each entry has year, pages or volume(issue), and a DOI when published.
- [ ] Every table citation is a real `\cite`.
- [ ] The PVLDB Reference Format short title is a complete phrase (check the macro arguments, not a hand-copied block).

---

## 6. Pre-delivery self-review protocol

Run on every draft that leaves the machine, including “internal” PDFs. Layers 0 and 1 must report **zero errors** before Layer 2.

### Layer 0 — Source and compile

1. Compile with the official Volume 20 kit (`acmart` v2.19 or the current official pin, plus the matching `pvldb.sty`). Do not mix a stale sty.
2. Set `\vldbdoi`, `\vldbpages`, `\vldbavailabilityurl`, a complete `\vldbshorttitle`, author notes.
3. Read the **entire** `.log`: Overfull/Underfull `\hbox`/`\vbox`, undefined/multiply-defined, font warnings. Clear Overfull; do not hide it with `\sloppy`.
4. Run the lint in this skill directory:

```bash
# from the skill folder; prefers a local .venv with pymupdf
./check_pdf_layout.sh paper.pdf --log main.log --out lint.txt
# equivalent:
python check_pdf_layout.py paper.pdf --log main.log --out lint.txt --render-dir pages/
```

Exit code 0 means no errors (warnings allowed). **Every error must be fixed.** Every warning is inspected by eye. The tool is calibrated for **letter, acmart two-column, 612×792 pt**. PACMMOD’s smaller page (e.g. 486×720) floods `RIGHT_MARGIN` — do not judge those PDFs with the same threshold. Dense plots in otherwise clean published papers may still false-positive; the visual pass decides.

The script is read-only. It never edits the PDF and never invents numbers from the paper.

### Layer 1 — 150 dpi, every page (not optional, not replaceable by the script)

Render every page at ≥ 150 dpi (`--render-dir` or `pdftoppm -r 150`) and inspect at near-print size:

- column-to-column text collision;
- formulas, algorithms, tables in the gutter or past the margin;
- tables and figures readable without zoom;
- page-1 foot: license, Reference Format, Artifact Availability, and corresponding-author notes are separated;
- running heads, page numbers, short title complete, no half-words;
- captions and figure art not clipped.

Any failed page goes back to LaTeX. There is no “fix in the next version” for overlap or 6 pt tables.

### Layer 2 — The 10–20 minute skim of §2

Do Passes 1–4 in that order, preferably on a different day or by a different person. Write down any table that is not obvious in 30 seconds and any analysis sentence that does not name a component.

### Layer 3 — Consistency and the “what not to write” list

Walk §3.3 items 1–30. Align abstract / contribution / conclusion / main table numbers. Related Work ends on differences. The conclusion is short and does not open a self-limitation section. Citations and mandatory blocks are present. **Numbers are not edited to improve the story.**

Only then send the PDF to coauthors or to the submission system.

---

## 7. Low-level errors that make a paper look unpublished

These are independent of scientific contribution and appear in the first minutes of the skim:

1. Two-column body text overlapping.
2. Formulas or text past the page edge.
3. Main tables at 6 pt or smaller.
4. Figure type below 6–7 pt, or figure text colliding with the body.
5. Footnotes colliding with the mandatory PVLDB block on page 1.
6. Missing `\vldbtopmatter` or a hand-copied licence / Artifact / Reference Format (desk-reject risk).
7. Truncated short titles, half-words, broken font encodings.
8. `?` citations, centimetre-wide Overfull `\hbox`, wrong DOI or page macros.
9. Numbers that disagree across abstract, introduction, tables, and conclusion.
10. Section headings that fight `pvldb.sty` (Volume 20 restores **ALL-CAPS** section heads on `acmart` v2.19).
11. An appendix treated as pages “outside the 12.”
12. A PDF nobody opened at 150 dpi — the usual common cause of 1–11.

---

## 8. Volume 20 format facts that change the PDF

Confirm against the live official pages and `submit-pvldb`. As of the 2026-11 official template (`acmart` v2.19, 2026/06/27; `pvldb.sty` 2026/07/06 v1.0, https://github.com/vldbproceedings/VLDB-Template):

- Body at most **12 pages**, including figures, tables and appendices; **references excluded**.
- `\vldbtopmatter` is mandatory (Reference Format, CC BY-NC-ND footnote, Artifact Availability). Omitting it risks a desk reject.
- Section headings are ALL-CAPS via `pvldb.sty`.
- PVLDB is **single-blind** (names are on the submitted PDF). SIGMOD research is a different process — see `submit-sigmod`.
- EA&B contributions are protocol, insights and a reproducibility package; the abstract need not claim “our method wins X%.”
- Page 1 foot is a collision zone: inspect it every compile.

---

## 9. Helper: `check_pdf_layout.py`

| Item | Detail |
|---|---|
| Files | `check_pdf_layout.py`, wrapper `check_pdf_layout.sh` (uses a sibling `.venv` if present) |
| Requires | `pymupdf` (`pip install pymupdf`); optional `requirements.txt` in this folder |
| Flags | `TEXT_OVERLAP`, `RIGHT_MARGIN`, `TINY_TABLE_FONT` (< 6 pt in a table = error), `TINY_FIGURE_LABEL` (warning), `FOOTNOTE_COLLISION`, `TWO_CORR_AUTHOR_NOTES` (warning), plus `.log` Overfull / undefined refs when `--log` is given |
| Filters already in place | math accents and 1–2 character stems; thin math brushing body text is a warning; labels mostly inside a figure are not `TEXT_OVER_FIGURE` errors |
| Exit | 0 no errors; 1 errors; 2 usage or IO |
| Not a judge | False positives remain on dense published plots and on non-letter page sizes. A clean published paper may still warn. An error on a letter acmart draft (overflow, true overlap, 6 pt tables) is real and must be fixed. The 150 dpi pass is authoritative. |

Usage is in §6 Layer 0. Do not close a delivery on the lint summary alone.

---

## Companion skills

- `write-pvldb` — how to word limitations, losses and W/T/L without self-negation; section prose.
- `submit-pvldb` — official rules, calendar, caps, CMT; wins over any memory of this file.
- `review-pvldb` — simulated Volume 20 review.
- `ccf-a` — when to use the strongest reasoning tier for paper work.
