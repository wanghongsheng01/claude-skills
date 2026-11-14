---
name: ccfa-paper-layout-review
description: "Use when reviewing or fixing the PAGE LAYOUT of a two-column CCF-A database paper (PVLDB, SIGMOD, ICDE; acmart or IEEEtran): blank holes in a column (e.g. half a column empty under a text block because a table*/figure* or \\FloatBarrier left a gap), float-only pages, floats placed far from their first \\ref or never referenced, unbalanced last page, text in the gutter or margins, stranded headings, forbidden \\vspace/\\setlength spacing hacks, and the Overleaf main-document check. Red lines L1–L10 and style rules P1–P12 calibrated on 55 accepted 2024–2026 PVLDB/SIGMOD/ICDE papers (757 pages), plus layoutlint.py (per-page, per-column hole detector with PNG overlays) and floatmap.py (float definition vs first-reference positions in source). Reviewer and fixer are different agents; loop until 0 blocker and 0 major. Use for 排版 / 大面积空白 / 版面空洞 / 浮动体 / 表格位置 / 末页不平衡 / layout review."
---

# CCF-A 双栏论文页面排版审查（版式工具）

这个 skill 管整页版式：空洞、浮动体位置、末页、越界、禁用的间距 hack。图里画得对不对（线穿框、图例、字号）由 `ccfa-figure-layout-review` 负责；整篇论文的生产流程见 `pvldb-paper-craft`；官方格式规则以 `submit-pvldb` 和 `submit-sigmod` 为准。

- 清单（中文）：`references/LAYOUT_PRINCIPLES.md`，内容是 L1–L10 红线、P1–P12 风格规则、证据表和已验证的修法。
- 校准数据：`references/corpus_table.md`（55 篇逐篇实测）和 `references/corpus_stats.json`。
- 脚本：
  - `scripts/layoutlint.py`：从编好的 PDF 测出逐页、逐栏的空洞，找出浮动体专页、离引用太远的浮动体、末页不平衡、越界、孤立标题，同时扫 `.log` 和源码里的 hack；输出 Markdown 报告、JSON 和 PNG 叠图。
  - `scripts/floatmap.py`：展开 `\input` 后，列出每个浮动体的定义行、放置参数、首次 `\ref` 的行，以及 `\FloatBarrier`、`\clearpage`、负 `\vspace` 的位置。
  - `scripts/corpus_stats.py`：汇总一批已发表论文的 `--stats-only` 结果，用于重新校准阈值。

## 1. 角色：两个不同的 agent，循环进行

1. **审稿人（只读）：**
   - `git pull` 拿到最新版本，确认 Overleaf 的主文档（L10），只判 pdfLaTeX 编出的 PDF。
   - 跑 lint 和 floatmap，逐页看叠图。
   - 写出 `reviews/<paper>_layoutreview_rN.md`，每条包含：规则编号、页、栏、严重度、具体修法（哪个 label、哪一行源码、挪到哪、放置参数、宽度）。
   - 不改稿。修法能在临时副本上验证的就先验证，并写明"已验证"。
2. **修复者（另一个 agent）：** 逐条执行。约束：不改数字，不删结果，不超页数，不用 `\vspace` 或 `\setlength` 硬压。每改一处就重编，重跑 lint。
3. **复审：** 审稿人在新 PDF 上做第 N+1 轮。**0 blocker、0 major 之后才交给作者。**

## 2. 红线速查（细节与证据见 references）

| | 规则 | 默认严重度 |
|---|---|---|
| L1 | 正文页（非末页、非浮动体专页）任一栏不得有 ≥ 72 pt 的连续空白 | ≥ 25% 栏高为 blocker，≥ 15% 为 major，其余 minor；参考文献或附录从下一页顶部开始时降一级 |
| L2 | 栏顶空白 | 同 L1 |
| L3 | 浮动体专页的填充必须 ≥ 60% | < 35% 为 blocker，35–50% 为 major |
| L4 | 浮动体放在首次引用的同页或后 1 页；每个浮动体都必须被 `\ref` 引用 | 晚 ≥ 3 页或从未引用为 major，晚 2 页或早 1 页为 minor |
| L5 | 禁止负 `\vspace`、改浮动或图注间距的 `\setlength`、正文中间的 `\clearpage`、`[H]`、`baselinestretch<1`、`savetrees`/`geometry`/`titlesec` | major（`\FloatBarrier` 和单独的 `[h]` 为 minor，造成空洞时按 L1 判） |
| L6 | 末页两栏落差 ≤ 10% | > 50% 为 major；acmart 加 `pbalance` 选项即可 |
| L7 | 不越界、不伸进栏间距，日志里没有 Overfull > 1 pt | > 6 pt 为 major |
| L8 | 栏底不留孤立节标题，栏顶不留寡行 | major / minor |
| L9 | 浮动告警（Float too large、`h` 改成 `ht`）逐条确认 | 线索 |
| L10 | Overleaf 主文档必须是投稿稿件 | major |

已发表论文的基线：
- 42 篇 PVLDB 正式版的正文页**没有**栏中部空洞；
- 757 页中只有 3 页是浮动体专页，填充都 ≥ 84%；
- 86.9% 的浮动体在首次引用的同页或后 1 页；
- PVLDB 末页 42/42 平衡；
- 13 份录用稿源码中，`\FloatBarrier` 0/13，改浮动参数 0/13；
- 图注中位数约 10 词，p95 50 词。

## 3. 审稿人流程

```bash
pip install -r scripts/requirements.txt                     # pymupdf
git -C <overleaf_clone> pull --ff-only
mkdir /tmp/build && (cd <overleaf_clone> && git archive HEAD) | tar -x -C /tmp/build
(cd /tmp/build && latexmk -pdf -interaction=nonstopmode main.tex)   # pdfLaTeX only
python3 scripts/layoutlint.py /tmp/build/main.pdf out/ --log /tmp/build/main.log --tex /tmp/build
python3 scripts/floatmap.py /tmp/build/main.tex > out/floatmap.md
```

1. 读 `out/layoutlint.md`：逐页填充表、浮动体表（页、宽度、位置、首次引用页、图注词数）、末页情况、findings。
2. 打开 `out/overlays/page-NN.png` 逐页确认：红色是空洞，蓝色是浮动体框，紫色是越界。lint 只是线索：
   - 浮动体框可能漏掉子图；
   - 第 1 页作者块旁的空白已经排除；
   - 3 pt 左右的越界通常是字形外框，看日志里的 Overfull 来确认。
3. 用 `floatmap.md` 找成因：
   - 定义行远在首次引用之后；
   - 首次引用是方法节里的前瞻性提及；
   - 多个 `\input{table}` 连在一起，堵住了浮动体队列；
   - 屏障或 hack 所在的行。
4. 全稿缩略图过一遍，找 lint 测不到的问题：浮动体内部的大块留白、页底挤着表格。
5. 写 review。表头写明 commit、编译方式、页数和计数；每条给出可以直接执行的修法。修法优先级：
   1. 删屏障；
   2. 挪浮动体源码，或把前瞻性引用改成 §-引用；
   3. 改宽度；
   4. 缩短图注叙述；
   5. 重排文字。

## 4. 修复者速查

- **栏下半部空白：** 先找 `\FloatBarrier` 或 `\clearpage`，删掉后重编。`table*`/`figure*` 的定义写在引用段落**之前**，参数用 `[t]`。
- **末页左满右空：** `\documentclass[sigconf,pbalance]{acmart}`（有 `nonacm` 就保留）。IEEEtran 用 `\IEEEtriggeratref{N}`。
- **浮动体晚 3 页以上：** 方法节或 Setup 里对结果表的前瞻性 `\ref` 改成 `Section~\ref{}`；表格定义挪到首次讨论的段落之后；不要在节尾集中 `\input` 所有表。
- **未被引用的浮动体：** 加一句指引（"Table~\ref{x} reports …"），不新增数字。删不删由作者决定。
- **删掉 `\setlength` hack 后超页：** 先缩短 > 50 词的图注，再拆表或改宽度。不允许恢复 hack。
- **浮动体专页填不满：** 把浮动体压到 0.7 页以内，或与相邻浮动体合并。不要改 `\floatpagefraction`。

## 5. 已验证实例（匿名）

- **讨论节前的 `\FloatBarrier`：** 它卡住了一个待排的 `table*`，右栏空出 66%。删掉这一行后空洞消失，页数 11 → 10。
- **末页落差 50–92%：** 4 份 acmart 稿加 `pbalance` 后落差降到 0–3%，页数不变。
- **结果表晚 4–5 页：** 方法节和 Setup 里有前瞻性 `\ref`，表格又集中在节尾 `\input`。把前瞻性引用改成 §-引用，表格定义挪到讨论处。
- **5 行 `\setlength` 浮动间距 hack：** 删掉后正文恰好排满 12 页，仍然合规。
