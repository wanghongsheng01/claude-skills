# Lessons from 邓老师's meeting records (2026-11-12)

Six files of past meeting records in which 邓达臻 guided Dr.Wang on top-venue papers. They were missing at the first skill commit and are now read in full from `/workspace/deng_meetings/` (same bytes as the attachments folder). **Prefer the verbatim transcripts** over the AI chapter summaries (those end with “内容由 AI 生成，仅供参考”).

| Short name | File (sha256 prefix) | What it is |
|---|---|---|
| M1-逐字稿 | `cdb7ea3ecaa27ca425303a0b7cc9cfb816051d328f1a585fae0ff416599a06b0.md` | ICDE 投稿评审，邓达臻、王宏升，逐字稿 |
| M1-纪要 | `001f874cdee921974499e00a4846cd5c940d63267f4dcc87901066ef277b6218.md` | Same meeting, structured minutes |
| M1-章节 | `0f530452a38116cdd3b806d9a4cda3c1c074cd1d2680b9960b1b587a2fe893dd.md` | Same meeting, short chapter list |
| M2-逐字稿 | `dbdb0539685b567f2e911c51092680d568006c38604b8739453ed14d3ab52a05.md` | 架构图与实验图评审，邓达臻、Magii，逐字稿 |
| M2-纪要 | `ccabf2cc1593372771d647f73d36a58ed96153b4feb36f37eaf6f7bfb265c672.md` | Same meeting, structured minutes |
| M2-章节 | `daf1d25dcd83df24f319ce952ea8329d11f4d11fd095ea9502ef9f8da0b777a8.md` | Same meeting, short chapter list |

Quotes below are from 邓达臻's speech in the transcripts, lightly punctuated. Tag in the checklist: **邓-会议**. Advisor experience is not a CFP. Official pages still win (see `venue-conflicts.md`). A remark by Dr.Wang in M1 that “EAB 对新颖性要求比较低” is **not** adopted as a rule.

## 1. Problem selection and portfolio (投稿策略)

- **Ten-minute, often LLM-assisted, review.** Write so novelty and experimental standing are obvious in one pass. Small issues will be caught automatically; the human then judges idea and results.
  - Source: M1-逐字稿 00:12:39. “审稿人可能也就是花10分钟，十几分钟，可能就把你的整个文章给过了一遍，因为现在有了大模型嘛，很多人可能也是用大模型去审了。……他会结合这个结果再去看一下这个文章整体的一些实验的结果，以及它的一个 idea 的 novelty。”
- **Do not send overlapping-data papers to the same venue** when contributions are not clearly distinguished. Pick the two or three strongest (novelty + experiments) for that venue; hold or divert the rest.
  - Source: M1-逐字稿 00:13:32（及 00:11:37）. “如果像我们有重叠的那几个点，我觉得肯定要避免掉，就是起码你不要投到一个地方去……我们就挑2~3篇，我们这边觉得分最高的就是质量最好的，然后就结合 novelty 和实验的一个结果。”
  - Official override: venue dual-submission and author-cap rules (PVLDB: two papers per author per month) still apply and can be stricter or more specific than “2–3 篇.”

## 2. Story and novelty framing

- **Figure 1 should make the gap visible**, distinguish this paper's contribution from upstream input, and mark offline vs online and where an LLM is used. A method that can refuse should show a positive and a negative example. Modules that are not strictly sequential must not have misleading arrows.
  - Source: M2-逐字稿 00:20:25–00:20:46. “B 和 C 是我们的贡献。……这里面可能就是要加一些大模型的符号进去，让他知道说，c 是和大模型是关联来做的。b 是我们离线……提取的一些规则和这种 contract。” Deng also accepted a revision that added a visual Gap module (M2-逐字稿 00:19:36: “我觉得在思路上挺清晰的”). The Gap idea was proposed from observing other top-venue figures; Deng endorsed the clarity.
- **Problem-necessity evidence is worth a compact figure**: if iterative repair or post-hoc linking plateaus and a residual error remains, that figure argues why the problem is real. It is not a substitute for the main SOTA table.
  - Source: M2-逐字稿 00:29:18. “这里面你是想说的是我们的必要性嘛，我感觉是可以有的，但是可以稍微压缩一下篇幅，比如说它下面涂的那种 caption 可以少一些。”

## 3. Experiment design and analysis

- **Wins and losses by scenario, with takeaways.** If the method is better on some datasets and worse on others, a reviewer will ask why. Discuss the difference, the advantage, and the reason the baseline wins in its regime. “All best” is not realistic and is not required.
  - Source: M1-逐字稿 00:22:27. “如果我是审稿人的话，我就会很好奇，就是为什么有的你好，有的别人更好……我会对在什么场景之下你会更好，更感兴趣……深入的讨论一下和这个方法的区别和优势是在哪里，以及你比他好的原因是什么，然后他在一些地方比你好，原因又是什么，我觉得这个可能很关键。”
  - Source: M1-逐字稿 00:29:47–00:30:37. “如果比不过的话，为什么比不过……如果能讨论的清楚，我觉得也可以，也不一定说你的结构一定要都是最好的。”“如果都是最好不是很真实，也不可能说你的这个方法在所有数据集上都最好，那如果有不好的，那怎么样去讨论你的优势和不足，我觉得这个就很重要。可能就得增加一下这方面的一些分析，然后一些 takeaways。”
- **Average / summary row** when a table moves up on some datasets and down on others, so a first glance sees the overall effect. This is *in addition to* the Best/2nd count row.
  - Source: M1-逐字稿 00:23:51–00:25:00. “有的增加，有的减少……我第一眼看这个图我看不出来到底哪的性能到底因为哪个模块变好了。……加一行，然后把这个平均值给列一下……起码你在这么多个不同数据集上平均下来……abrasion 的效果是怎么样的。”
- **95% confidence-interval bands are acceptable** on venue figures (they show swing, not decoration).
  - Source: M2-逐字稿 00:32:54. “还是有的，就是它是95的一个置信区间，相当于是说它这个数据的上下摆动。”
- **Secondary module-ablation figures can leave the body** when they do not earn their page space; keep the necessity / main-result panels.
  - Source: M2-逐字稿 00:40:05. “对这些没必要了。”（各模块消融图不进正文）

## 4. Tables and figures

- Best in **bold**, second **underlined**, including close losses (values that lose only at extra decimals). Already in A1; the meeting is the source of the close-loss case.
  - Source: M1-逐字稿 00:19:40 及 00:20:43. “你可以把第二名也标出来，就第一第二都标出来……最好的你就标加粗，然后第二的你就下划线。”“有的0.48你也0.48，那可能也就是在小数位上面输掉了，那基本上的话你如果再加上下划线把第二名也划出来，那就说明你基本上就是最优或者是第二了。”
- **Empty regions** in a scatter or cost plot need a one-sentence explanation (caption or body).
  - Source: M1-逐字稿 00:17:58. “它中间我看基本上都是空的，就是这个中间的这一大段基本上是空的，我感觉这个可能要解释一下是为什么。”
- **Anomalous aggregate curves**: if a mean line looks wrong, check the data or replace it with a **box plot**.
  - Source: M1-逐字稿 00:20:43. “绿色的平均线为什么会长这样有点奇怪……这个数据可能是要 CHECK 一下，或者是你换一个那种。那种箱线图来可能会更合适一些。”
- **Drop a table that only lists other people's datasets** and does not show this method (index size, cost, accuracy, etc.).
  - Source: M1-逐字稿 00:27:07–00:27:49. “都是别人的数据集，那好像也没有必要列出来。”“如果只是数据集的介绍的话，那我觉得可能没有太大必要放在 paper 里面。”
- **Compress long table headers and captions.** “一般不会写的这么长.”
  - Source: M1-逐字稿 00:30:37.
- **Whitespace, overflow, overlap look unprofessional and “model-generated.”** Tighten the layout. If code-drawn corners cannot be fixed, **redraw by hand**. Deng tells students to manually redraw coding-produced figures when details are poor.
  - Source: M2-逐字稿 00:12:12. “因为空的地方很多……到时候他比较明显，觉得你这个是模型生成的可能印象不太好。”
  - Source: M2-逐字稿 00:25:21. “边角的地方都没办法弄得比较完善的话，可能还是得人重新画一下，因为我跟我的学生都是说你用那个……coding 画出来的图，你一定要重新手动重新画一个，因为现在它就是有一些细节处理的不好。”
  - Source: M2-逐字稿 00:38:25. “很多 overlapping 就是那个字和图这些。可能得优化一下。”
- **Compact multi-panel layout.** Several large, low-information figures should become one row of small panels. The “7 页纸” remark is about that paper's budget, not a universal page cap — compress to the *target venue's* limit.
  - Source: M2-逐字稿 00:33:50. “这几张图可以太大了……整个最后投稿的篇幅也不是很长，7页纸，那这几张图其实信息量没有那么大，所以我觉得可以稍微压缩一下它大小，比如说一排四个从左到右。”
- **Captions about 1–2 lines**; do not repeat results already in the body.
  - Source: M2-逐字稿 00:34:18–00:34:30. “每个图一般 AI 的文章它的 caption 可能也就一两行左右就差不多了。”“因为你实验的结果，文章正文里面会讲的，你这个这一块没必要讲太多。”

## 5. Writing, revision, collaboration

- **Look at the body**, not only an AI summary of the paper, in a co-author review. (M1-逐字稿 00:16:59: “看正文，这个总结的版本我这边打开看了。”)
- **One Overleaf project per paper, with Git.** Do not share a fresh Overleaf link at every iteration; the project already has history. Clone via Overleaf's Git integration and push to sync.
  - Source: M2-逐字稿 00:02:44–00:03:58. “我看你每次都会分享一个新的 overleaf，您其实可以直接在上面改的 overleaf 它有历史追踪的。”“他底层有一个它背后其实有 git 会维护的。”
- **Page budget is a review item**, not an afterthought. (M1-逐字稿 00:25:39: “它页数，篇幅这些可能要注意一下，不会超？”) Blindness (anonymous vs single-blind) is whatever the official CFP says — Deng asked; he did not invent a rule.
- Prefer a tighter, professional figure over a busier one (in M2 they kept the cleaner set and dropped the more complex Codex panels). Information density and no overlap beat decorative complexity.

## What is already in the checklist (meetings confirm, not new)

A1–A2 (bold / underline / standing), A4 (explain losses), B5 (figures must show the claim), S01 (short claim-first captions), E2 (public data), F1 (problem → gap → insight). The meetings supply sharper *operations*: the average row, empty-region captions, box plots for bad aggregates, Figure 1's gap / contribution / LLM marks, the “model-generated” whitespace test, dataset-only table deletion, 10-minute LLM-assisted review, and same-venue overlap.
