# Advisor sources absorbed into this skill

The nine hashed attachment paths named in the 2026-11-12 request were not present on the shared box at execution time. The content below was read from (1) the verbatim 邓老师 and 梁老师 comments in the author's message, and (2) 邓老师's writing-method documents stored on the author's Mac and in the Feishu-sourced copies used in earlier work. No credential, enterprise dump, or copyrighted full-paper text is copied here — only distilled rules.

## 1. Verbatim advisor comments (author message, 2026-11-12)

- Reviewers focus on **performance** and **novelty** (which story is attractive).
- 邓老师: experiment tables are complex and dense; without bold marks one cannot tell whether the method is good. Is it SOTA, or SOTA on most metrics? Second-best is acceptable. It must be clear in which papers the method is best.
- 梁老师, Ladder: only Kimi / DeepSeek / GLM (Chinese models) may be judged insufficient internationally; Tables 4/5 decimals inconsistent; Fig. 3 and Fig. 1(a) do not show Ladder's advantage.
- 梁老师, TopUp: high practical value; charts are only lines and bars; decimals still inconsistent; title does not convey what "TopUp" means; no need to mention Ladder in related work; the production dataset cannot be public (attackable); do not add experiments — reorganise the data.
- 梁老师, k-Plexes: Table 5 mixed units, Table 7 mixed decimals, figure fonts inconsistent; Table 6 looks like an experiment log; Table 1 and Algorithms 1–2 "usually" go to the appendix.
- 梁老师, EAB: should "[Experiment, Analysis, and Benchmark]" be in the title? Tables 1 and 9 are mostly missing data; most tables look like logs; does ICDE put related work last? Presentation is far from A-venue standard.
- Dr.Wang: advisors are not always right; judge every item against the **official** author guidelines of the target venue (including whether VLDB EA&B papers put the tag in the title, and related-work norms in accepted papers).

## 2. 邓老师第二次指导文章进化

One-line skeleton: **problem → gap → insight → method → evidence**.

- Problem is a concrete shared failure, not "X is hard."
- Gap says what prior work already solved and what it did not (do not pretend to beat a paper on the problem it actually solved).
- Insight is one sentence; the method is the implementation of that insight, not a module list.
- At most two public names and three contributions.
- Each experiment table tests one piece of the insight (ablate this compiler, this policy, public vs industrial).
- For refusal/safety, report both refusal quality and utility (do not "just refuse more").

## 3. 做顶会文章的方法论 (including AutoLink craft, distilled)

- Bold has a job: method name, headline numbers with an external anchor, at most one scan-sentence per paragraph. Conclusion does not shout.
- Tables: ↑/↓ in the header; best bold, second underlined; **a baseline's best is also bold**; qualitative ✓/✗ columns; self-contained captions; ablation with a delta.
- Figure 1 is a real-example trace, not an abstract box diagram. Scaling figures share an axis and show sample shares. Our curve is solid and highlighted; baselines are dashed.
- A loss is written plainly and, if true, recovered on cost or another dimension.
- Five narrative upgrades (质疑假设 / 问题驱动 / 原理机制 / 机制解释 / 连接式收尾) only when the research actually supports them.

## 4. 做顶会文章通用 (process only)

Venue survey → absorb accepted papers' writing → idea and real experiments → write → independent review by a different agent → revise. Skills are deposited in `wanghongsheng01/claude-skills`. Historical wording that asked to reduce honest disclosure is **not** a rule of this skill.

## 5. Relationship to existing skills

S01–S11 in `results-presentation-review` and the first-round co-author lessons in `review-icde/references/coauthor-review-lessons.md` already encode many of the same presentation rules for ICDE. This skill **generalises** them across VLDB, SIGMOD Industrial, TKDE and KDD, adds the official-vs-advisor conflict table, and adds the novelty-story and SOTA-总表 gates. It does not rewrite those files.
