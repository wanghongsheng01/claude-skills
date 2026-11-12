---
name: "paper-presubmission-review"
description: "Advisor-guided presubmission self-check for CCF-A data-management papers (VLDB/PVLDB, SIGMOD Industrial, ICDE, TKDE, KDD). Distills 邓老师 and 梁老师 review comments plus 邓老师's writing-method notes and six meeting records (problem→gap→insight→method→evidence; SOTA-at-a-glance tables; decimals/units/fonts; no experiment-log tables; title and related-work placement; public-data confirmation; international LLM baselines; novelty story) into a concrete checklist. Every item is tagged with its source and checked against the venue's official author guidelines; where advice conflicts with or does not apply to a venue, the official page wins. Use automatically before submitting, before a co-author review, or when applying advisor feedback (投稿前自审 / 导师意见落地 / SOTA一眼可见 / 加粗下划线 / 实验记录表 / EAB标题标签 / 附录位置 / 邓老师开会记录 / 投稿总指挥)."
---

# Paper presubmission review (advisor-guided self-check)

Reviewers of CCF-A papers look first at two things: **performance** (is the method SOTA, or at least second, and can that be seen in two minutes?) and **novelty** (is the story a clear problem → gap → insight, not a pile of modules?). This skill turns that bar, plus written advice from two advisors, into a checklist that is run **against the target venue's official author guidelines**. Advisor comments are experience. They are not a substitute for the CFP. If the two disagree, **the official page wins**, and the conflict is recorded in the report.

This skill does **not** replace `results-presentation-review` (S01–S11), `manuscript-writing-review`, `manuscript-proofcheck`, the venue writing skills (`write-vldb`, `write-sigmod-industrial`, `write-tkde`, `write-icde`, `write-kdd` if present), or the commander `ccfa-submission-workflow` (CMT/portal packet, Overleaf vs local PDF, second-author briefing, what only the author submits). It is the gate that decides whether advisor-style presentation and official rules are both satisfied. For a full submission run, `ccfa-submission-workflow` calls this skill. **Do not edit those other skills from here** except when a later request explicitly asks to add a cross-link.

## Language

- Fixes to the manuscript are in formal academic English.
- The report to the author is in Chinese, as a document, with a per-paper SOTA standing and a list of checklist findings.

## Sources (tag every checklist item)

| Tag | Source |
|---|---|
| 邓-扫读 | 邓老师: result tables are dense; without bold marks a reader cannot tell whether the method is good. Need SOTA or SOTA on most metrics; second-best is acceptable; it must be clear which papers are best. |
| 邓-骨架 | 附件《邓老师第二次指导文章进化》: one line `problem → gap → insight → method → evidence`; at most two method names and three contributions; each table answers one question that tests the insight. |
| 邓-写法 | 附件《做顶会文章的方法论》and the AutoLink craft notes: disciplined bold (method name, headline numbers, one scan sentence per paragraph); best bold / second underlined, including when a baseline wins; claim-first captions; Figure 1 carries a real example; honest losses recovered on another dimension. |
| 邓-叙事 | 附件中的五级叙事升级: challenge a hidden assumption; problem-driven not method-driven; mechanism not a score dump; open a research connection in the conclusion. Narrative upgrades must rest on real results. |
| 梁-LLM | 梁老师 on Ladder: only Chinese LLMs (Kimi, DeepSeek, GLM) may be called insufficient at an international venue. |
| 梁-小数 | Ladder Tables 4/5, TopUp, k-Plexes Table 7: decimals not unified. |
| 梁-图优势 | Ladder Fig. 3 and Fig. 1(a) do not show the method's advantage. |
| 梁-图表 | TopUp: only line and bar charts, tiring; learn modern palettes. |
| 梁-题目 | TopUp: title is not too long but does not convey what the name means. |
| 梁-RW同伴 | TopUp: no need to mention a companion paper (Ladder) in related work. |
| 梁-数据 | TopUp: the biggest attack is a non-public production dataset; do not add experiments for their own sake — reorganise what is already there, and make conclusions stand on public data. |
| 梁-单位字体 | k-Plexes: Table 5 mixed units, Table 7 mixed decimals, figure fonts not unified. |
| 梁-记录表 | k-Plexes Table 6 looks like an experiment log; EAB Tables 1 and 9 are mostly "–" and most tables look like logs. |
| 梁-附录 | k-Plexes: "Table 1 and Algorithms 1–2 usually go in the appendix." |
| 梁-EAB题 | EAB: should "[Experiment, Analysis, and Benchmark]" be in the title? Does ICDE always put related work last? Presentation is far from A-venue standard. |
| 邓-会议 | Six meeting records (read 2026-11-12 in full): 10–15 min LLM-assisted review; same-venue data-overlap; average row; empty plot regions and box plots; Figure 1 gap/contribution/LLM marks; “model-generated” whitespace; dataset-only tables; problem-necessity figures; one Overleaf+Git. Quotes in `references/deng-meeting-lessons.md`. |
| 官方 | The venue CFP / author guide, with URL and access date. This tag **overrides** an advisor tag when they conflict. See `references/venue-conflicts.md`. |

A historical prompt that asked to "reduce honest disclosure" is **not** adopted (already rejected in the 2026-11-06 transcription of 做顶会文章通用, and by 邓 S07/S10). Losses stay visible and are explained.

## Official-page rule (non-negotiable)

1. Re-open the official pages for the **target venue** and record the access date. The snapshot in `references/venue-conflicts.md` was checked on **2026-11-12**. If a live page disagrees, the live page wins.
2. Apply every checklist item only as far as that venue allows (appendix, EAB title tag, page budget, blindness, related-work placement).
3. In the report, mark each item `适用` / `适用但改写` / `与官方冲突，已按官方执行` / `该会刊不适用`.

## The checklist

Run in this order. Tick in the report. Details and venue conflicts are in `references/venue-conflicts.md` and `references/checklist-recipes.md`.

### A. Performance at a glance (邓-扫读, 邓-写法, S03–S04)

- [ ] **A1.** Every results table bolds the **best** printed value and underlines the **second** best, ranked on the *printed* string so ties share the mark. A baseline that wins is bolded honestly. (邓-扫读, 邓-写法)
- [ ] **A2.** Every comparison table has a **Best/2nd** (or win/tie/lose) **count row**, and each RQ has one standing sentence ("best in X of Y, second in Z, worse in W"). (邓-扫读)
- [ ] **A3.** A one-page **SOTA 总表** across the portfolio states, for each paper, counts against the **strongest actually-run** baseline, whether losses have a precise mechanism, and a verdict: 可投 / 需改进 / 尚不可投. Individual metrics may be second; the paper may not be submitted if it is not SOTA (or clearly second with a mechanism) on **most** metrics. (邓-扫读; Dr.Wang's SOTA gate)
- [ ] **A4.** Every loss has a mechanism from run counters or instance properties, not a guess, in the experiment that measures it, plus a takeaway on the regime where the baseline wins. "All best is not realistic" and is not required. No self-negation in the abstract or conclusion. (邓-写法, 邓-会议, S07/S10)
- [ ] **A5.** When a table goes up on some datasets and down on others, add an **average (or geometric-mean) summary row** so a first glance sees the overall effect. This is in addition to the Best/2nd count row. Do not average incomparable units. (邓-会议)

### B. Typography of numbers and figures (梁-小数, 梁-单位字体, 梁-图表, 梁-图优势, S01–S02, S05)

- [ ] **B1.** One precision per metric inside each table (e.g. all percentages to 1 decimal). Fix in the generator; then verify that only rounding changed. (梁-小数)
- [ ] **B2.** One unit per **column**, in the header (not only the caption). Do not mix ms and s in the same column; do not use "k"/"M" suffixes that look like a unit change. (梁-单位字体)
- [ ] **B3.** All figures share the body typeface (Times-like) at 8–9 pt; tick, axis and legend sizes match. matplotlib `font.family: serif` alone is not Times — set the serif list and `mathtext.fontset`. (梁-单位字体)
- [ ] **B4.** Colour-blind-safe palette; **our method** has one fixed highlight colour, a solid line and markers; baselines use dashed or dotted lines without competing markers. Chart type matches the claim (Pareto, heatmap, CDF, small multiples — not only lines and bars). (梁-图表, 邓-写法)
- [ ] **B5.** Every figure carries a claim a two-minute reader can see. The caption's first sentence is the takeaway (about 1–2 lines; do not repeat the body). If a figure does not show an advantage (or a deliberate non-advantage with a lesson), redraw or drop it. (梁-图优势, 邓-写法, 邓-会议, S02)
- [ ] **B6.** Empty regions in a scatter or cost plot get a one-sentence explanation. A mean curve that looks wrong is checked against the data, or replaced with a box plot. 95% CI bands are acceptable. (邓-会议)
- [ ] **B7.** Large whitespace, overflow, or text–graphics overlap looks "model-generated" and unprofessional. Tighten the layout; if code cannot fix the corners, redraw by hand. Prefer one compact row of panels over several large low-information figures, within the *venue* page limit (a "7 页" remark is not a universal cap). (邓-会议)

### C. Tables that belong in a paper (梁-记录表, S06, S11)

- [ ] **C1.** No table that reads as an experiment log (a two-column "Experiment / Result" dump, a raw run sheet, or mostly "–" cells). Turn it into a standing summary (faster / on par / slower, or a ✓/✗/partial matrix), or move it to the artifact. (梁-记录表)
- [ ] **C2.** Ablation tables have a visually separated summary row (geometric mean for ratios). (S06, 邓-骨架: each component is tested)
- [ ] **C3.** Dataset tables are trimmed to columns the method uses; a constant column in a *results* table can be a finding and may stay. (S11)
- [ ] **C4.** Drop a body table that **only lists other people's datasets** and does not show this method (index size, cost, accuracy, build time). Keep it if the method's structure is in the same table. (邓-会议)

### D. Title, related work, appendix (梁-题目, 梁-EAB题, 梁-附录, 梁-RW同伴, 邓-骨架) — **venue-dependent**

- [ ] **D1.** The title explains the method name's mechanism ("Name: what it does over what"). (梁-题目, 邓-骨架)
- [ ] **D2. EAB / EA&B title tag — follow the official wording and placement, which differ by venue.** (梁-EAB题, 官方)
  - **ICDE:** the title **starts** with `[Experiment, Analysis, and Benchmark]` (with "and"). Drop the tag in the camera-ready. Official: https://icde2027.github.io/cf-research-papers.html
  - **PVLDB / VLDB:** **append** the suffix `[Experiment, Analysis & Benchmark]` (with "&") to the title in the PDF **and** in CMT. Drop it in the camera-ready. Official: https://vldb.org/2027/submission-guidelines.html
  - **SIGMOD Industrial, TKDE, KDD research:** no such tag. KDD has a separate Datasets & Benchmarks track — do not invent an ICDE/VLDB tag there.
- [ ] **D3. Appendix — advisor "put Table 1 and Algorithms 1–2 in the appendix" often conflicts with the CFP.** (梁-附录, 官方)
  - **ICDE:** "**No appendix is allowed.**" Compress or move long proofs to a public technical report; keep the algorithms that are the method in the body. Official: https://icde2027.github.io/submission-guidelines.html
  - **PVLDB:** appendices are allowed **but count toward the 12-page body** (only references may exceed 12). Put an algorithm in the appendix only if the body still makes the method checkable. Official: https://vldb.org/2027/submission-guidelines.html
  - **SIGMOD Industrial:** CFP is "12 pages + references" and does **not** mention a separate appendix (unlike SIGMOD **Research**, which allows a short separate-PDF appendix that reviewers need not read and that is not in the camera-ready). Do **not** assume extra appendix pages for the Industrial track. Official: https://2027.sigmod.org/calls_industrial_track_papers.shtml
  - **KDD research:** submission is 8 content pages, then unlimited references and an optional appendix; the first 8 pages must be self-contained. Camera-ready is 12 pages, of which 9 are content and 3 are references+appendix. Official: https://kdd2027.kdd.org/research-track-call-for-papers/
  - **TKDE:** supporting material is **separate supplemental files**, not a body appendix; the journal page limit **includes** references and biographies. Confirm on the IEEE CS TKDE author page: https://www.computer.org/csdl/journal/tk
- [ ] **D4. Related-work placement — no official venue requires "always last" or "always after the introduction."** (梁-EAB题, 官方). Empirically, EAB/benchmark papers often place it as Section II; problem-driven and theory papers often place it last. Either is acceptable. Choose the placement that serves the story. Do not move a section only because an advisor recalled a habit.
- [ ] **D5. Companion / concurrent papers.** (梁-RW同伴, 官方). 梁's "no need to mention Ladder" applies when there is no scientific overlap. **Official overrides:** PVLDB Volume 20 requires authors to **self-declare related concurrent submissions** and to cite them as "under submission" (https://vldb.org/2027/submission-guidelines.html). ICDE requires citation of overlapping *published* work. Practice: cite a concurrent submission **once** where the overlap must be declared; do not give it a dedicated paragraph.

### E. Evidence integrity (梁-LLM, 梁-数据, 邓-骨架)

- [ ] **E1. International LLM baselines.** (梁-LLM). No CFP names GPT or Claude. The item is still required for LLM papers because "the strongest system is missing" is a common rejection reason, not a desk-reject rule. Include at least GPT and Claude, each in its own column, with model ID, channel and date. Chinese models (Kimi, DeepSeek, GLM) may stay as additional columns. Send only public or de-identified data through third-party APIs. Non-LLM papers: **该会刊/该文不适用**.
- [ ] **E2. Non-public production data.** (梁-数据, 邓-骨架). The **main conclusions must stand on public data alone**; say so and show it. Enterprise numbers are supplementary. EA&B at PVLDB requires a full reproducibility package **at initial submission**, with no excuses. ICDE EAB: artifacts are mandatory. Regular papers that cannot release an artifact must explain why on the form. Reorganise existing results before adding experiments.
- [ ] **E3.** Never invent a number, drop a measured cell, or call a result SOTA when the method was fitted to the test fixtures (a 100% score on template rules is not a main-table result).

### F. Novelty story (邓-骨架, 邓-叙事, 邓-写法)

- [ ] **F1.** A reader who only follows the bold scan-sentences can reconstruct: industry problem (a concrete failure, not "X is hard") → what prior work solved and what it did not → one insight → the method as an implementation of that insight → evidence that tests the insight, including ablations.
- [ ] **F2.** The story challenges a hidden assumption where that is true, and does not dress a module list as a new assumption. Losses are written honestly and, if possible, recovered on another dimension (cost, exactness, a tighter regime).
- [ ] **F3.** The conclusion opens a precise research connection; it does not close with "we proposed a method and it worked," and it does not self-negate.
- [ ] **F4.** Figure 1 lets a two-minute reader see the **gap** vs prior work, **this paper's contribution** vs upstream input, offline vs online, and (if used) an LLM icon. A method that can refuse shows a positive and a negative path. Do not draw strict pipeline arrows among modules that may run in parallel. (邓-会议)
- [ ] **F5.** A compact **problem-necessity** figure (e.g. iterative repair plateaus) is welcome; secondary module-ablation figures may leave the body if they do not earn their height. (邓-会议)

### H. Ten-minute scan and portfolio (邓-会议)

- [ ] **H1.** Novelty and experimental standing are obvious in a 10–15 minute pass (reviewers often run an LLM first, then judge idea and results themselves). (邓-会议)
- [ ] **H2.** Two papers that share business data and whose contributions are not clearly distinguished are **not** sent to the same venue. Pick the two or three strongest for that venue; official author-cap and dual-submission rules still apply (ICDE: 5 per author per round; PVLDB: 2 per month). (邓-会议, 官方)
- [ ] **H3.** One Overleaf project per paper, updated via Git; do not open a fresh Overleaf link at every iteration. The submission PDF is checked against this project, page by page, before form fields are prepared (`ccfa-submission-workflow`). (邓-会议)

### G. Venue compliance (官方)

- [ ] **G1.** Page budget, template, blindness, author caps, AI-content declaration, and (if EA&B) the reproducibility package, all as on the official page. No margin or spacing hacks. Body page count is measured on a freshly compiled PDF.
- [ ] **G2.** Re-run `results-presentation-review` and `manuscript-writing-review` after every presentation change.

## Workflow

1. **Identify the venue** and re-read its official pages (URLs in `references/venue-conflicts.md`). Record the access date.
2. **SOTA standing.** From *real* repository or manuscript numbers only, fill the per-paper row of the SOTA 总表 (best / second / worse vs the strongest run baseline, mechanism for losses, verdict). If the verdict is not 可投, say so; presentation polish does not replace missing SOTA.
3. **Lint and read.** Run `results-presentation-review` if installed. Then walk every table and figure as a first-time reader with this checklist.
4. **Apply only what the venue allows.** Fix marks, count rows, decimals, units, fonts and palettes **in the generator**, then regenerate and confirm that no value changed beyond rounding. Do not change frozen author lists or experimental numbers.
5. **Resolve conflicts** using `references/venue-conflicts.md`. Write each conflict in the report ("梁-附录 vs ICDE 不允许附录: 已压缩正文，未新增附录").
6. **Compile** (`pdflatex`/`bibtex` as the template requires) to **0 errors**, recount body pages, and inspect every page.
7. **Report** in Chinese: checklist ticks, SOTA 总表, conflicts with official rules, what was not changed and why.

## Worked expectations for the current portfolio (2026-11-12)

These are illustrations of how the skill judges, not a substitute for a fresh count:

- **RateQ** (SIGMOD Industrial): 79 best / 2 second / 0 worse; the two seconds are the same ENT Q1 phenomenon, already explained. Presentation (2026-11-12) added underlines, count rows and shorter captions; a later pass against 邓-会议 items needed **no further tex change** (datasets.tex shows RQ-Index structure, not a bare dataset list; Fig. 1 is a real rate-card example with the exact cheapest path highlighted; no empty unexplained scatter; no mixed up/down table needing an extra average row; figures already compact and claim-carrying). LLM item is N/A. L5 already states that conclusions hold on public official rate cards. Appendix: do not add pages the Industrial CFP does not grant. Figures were not redrawn (no generator in the tree).
- **ScopeCache** (PVLDB): main table already marks 8/2 against mixed baselines, but vs the strongest baseline PerScope+V the grid is 6 better / 6 tie / 3 worse (all three on SYN-FG). Presentation is ahead of the SOTA gate; method work belongs to the other worker — report findings, do not silently edit their tex.
- **CertKP** (PVLDB target): main table 61/13/0 is SOTA-at-a-glance; the risk is the 39 slower cells in the additional table (24 still slow after kplex18). Still IEEEtran in the local tree until the PVLDB conversion lands. 梁-附录 was already correctly *not* followed under ICDE's no-appendix rule; under PVLDB, appendix still counts toward 12 pages.
