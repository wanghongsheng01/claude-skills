---
name: pvldb-data-validation-anatomy
description: "逐节、逐段、逐句拆解四篇已发表的 PVLDB 数据质量/数据校验/错误解释论文（SPADE PVLDB 17、Deequ PVLDB 11、YouTube CI/CD for data pipelines PVLDB 18、Scorpion PVLDB 6），给出每个要素的量化标尺（min/median/max）、逐节逐段的审查程序（met/partial/gap + 文件:行号证据）、阻断条件，以及 reviewer/fixer 分离的双门循环：Gate A 方法在每个报告指标上胜过每个 baseline（平局只在已证界限处，如 0% 误报 / 100% 检测），Gate B 稿件从标题到参考文献与已发表范文对齐。Use when writing, self-reviewing or acceptance-reviewing a PVLDB paper on data quality, data validation, assertions/constraints/checks derived for ETL or data pipelines, error detection or error explanation in aggregate queries. 触发词：数据质量论文、数据校验PVLDB范文、ETL校验、数据管道检查派生、对账/守恒类检查、断言合成、Deequ、SPADE、Scorpion、YouTube CI/CD、范文对齐、全指标超过baseline、Gate A/Gate B、审稿循环；data validation paper, data quality assertions, pipeline checks, PVLDB exemplar alignment, reviewer loop."
---

# PVLDB 数据质量 / 数据校验 / 错误解释论文解剖

四篇官方 PDF 逐页读完，拆到句子功能（详见 `references/<paper>.md`）：

| 缩写 | 论文 | 出处 | 为什么是范文 |
|---|---|---|---|
| SPA | SPADE：为 LLM pipeline 合成数据质量断言 | PVLDB 17(12): 4173–4186, 2024 | 从代码/版本历史**派生**检查 + 集合层面最优选择（ILP、NP-hard、subsumption）+ 部署证据与受控评估分节 |
| DEE | Deequ：大规模数据质量自动校验 | PVLDB 11(12): 1781–1794, 2018 | 声明式约束 → 聚合查询；增量计算模型；约束建议；"读起来像研究稿的工业稿" |
| YTC | YouTube 数仓数据管道 CI/CD | PVLDB 18(12): 4887–4895, 2025 | 数据管道的生产 CI；摘要量化与规模交代可借鉴，证据可追溯性是**反面**检查项 |
| SCO | Scorpion：解释聚合查询中的异常 | PVLDB 6(8): 553–564, 2013 | 形式化问题 + 聚合函数代数性质（可减、独立、反单调）+ 按性质分派算法与剪枝正确性 + 构造 ground truth 的实验 |

官方 URL、SHA256、字节数、第 4 篇的选择理由、核验方法与 DataHub 登记状态见 `references/provenance.md`。

配套 skill（本 skill 不重复它们）：`submit-pvldb`（Vol 20 官方规则、页数、声明）、`write-pvldb`（各节写法、W/T/L、局限不自我否定）、`review-pvldb`（官方评审流程、自我否定检查）、`pvldb-paper-craft`（版面与审稿人速读顺序、PDF lint）、`vldb-exemplar-sop`（12 篇通用 PVLDB 分布与 8 条阻断门 G1–G8）、`vldb-playbook`（venue 规则与做图 SOP）、`pvldb-cache-reuse-anatomy`（同格式的缓存/复用方向）。官方 PVLDB 页面永远优先。**绝不输出录取概率。**

## 什么时候用

- 写一篇 PVLDB 研究稿，贡献是：从 ETL/管道代码或查询语义**派生**数据质量检查/断言/约束、在成本预算下选择检查、检测或定位/解释数据错误，并希望结构对齐已发表的同类论文。
- 作为**独立 reviewer** 审这样一份稿件（reviewer/fixer 循环，见 `references/two-gate-loop.md`）。
- 判断证据是否足够：先跑 Gate A，再谈文字。

## 工作流

1. **锁版本**：记录 PDF 与源码哈希、页数、artifact/DEV/TEST 证据文件哈希。
2. **Gate A 先行**：建全指标优势矩阵（`references/two-gate-loop.md`）——每个指标 × 每个 baseline × 每个分块，W/T/L 与总量。每个非 PASS 行写一个**算法层面**的修改请求及验收测试。改措辞永远不能关闭 Gate A 行。
3. **指纹计数**：按 `references/fingerprints.md` 逐项计数，与区间对照。区间外是问题，不自动等于缺陷。
4. **逐节逐段对齐**：按 `references/review-procedure.md` 从标题走到参考文献，每条规则判 met / partial / gap，附**文件:行号**与 PDF 页码，并给出范文证据。
5. **阻断检查**：`references/review-procedure.md` 第 11 节的 11 条阻断条件 + `vldb-exemplar-sop` 的 G1–G8。
6. **写报告并交给 fixer**：版本锁 → Gate A 结论与矩阵 → Gate B 结论与阻断命中 → 指纹对照 → 按影响排序的发现 → 编号修改请求（ID、门、严重度、位置、范文证据、要求的改动、验收测试）。reviewer 不自己改。
7. **复审**：新版本交付后由另一次独立 reviewer 对照上一轮清单逐条判 CLOSED / OPEN / REGRESSED，并重跑完整 Gate A 矩阵。两门都过才批准；任一门未过就发出下一组最小要求，进入下一轮。

## 量化标尺（四篇 min / median / max；逐篇值见 `references/fingerprints.md`）

| 要素 | min | median | max | 研究稿标尺（判定） |
|---|---|---|---|---|
| 正文页 | 8.3 | 11.7 | 12 | ≤12（Vol 20 Regular，不含参考文献），超出即阻断 |
| 正文词数 | 5,600 | 9,850 | 11,300 | 9,000–11,500 |
| 摘要词 / 句 | 152 / 7 | 175 / 7.5 | 219 / 8 | 150–220 词、7–8 句 |
| 摘要中的数字 | 0 | 0.5 | 4 | ≥2 个，逐字可追溯并写明口径 |
| Intro 占比 | 8% | 8.5% | 16% | 0.9–1.5 页 |
| 方法（含形式化）占比 | 57% | 60% | 78% | 55–65% |
| 实验占比（有实验节者） | 20% | 21% | 24% | 20–30%（一般 PVLDB 中位 27.8%） |
| RW 占比 / 位置 | 4% | 5% | 6% | 4–6%，4/4 放末尾 |
| 结论词数 | 198 | 273 | 314 | 200–320 |
| Figures（结果图） | 1（0） | 7.5（3） | 16（8） | ≥6 图，其中结果图 ≥4 |
| Tables（结果表） | 2（0） | 3（0.5） | 6（3） | 2–6 |
| 实测结果展品 | 0 | 5.5 | 8 | ≥5（一般 PVLDB 中位 7） |
| 编号定义 / 定理 | 0 / 0 | 0 / 0 | 3 / 0 | 声称保证则必须有定理 + 证明（四篇都没有，研究稿须超过） |
| 展示公式 | 0 | 6.5 | 20 | 视形式化需要 |
| 贡献 bullet | 4 | 4 | 4 | 4 条，带节号与证据展品编号 |
| 非平凡对照 / 外部系统对照 | 0 / 0 | 0.5 / 0 | 1 / 0 | ≥1 外部已发表方法（或忠实重实现）+ 强精确对照 + 廉价对照 + 自家消融 |
| 数据集 / 工作负载 | 1 | 3 | 9 | ≥3，或 1 个真实 + 可控合成（ground truth 由构造给出） |
| 指标数 | 4 | 5 | 6 | 检测、误报、成本（实测）、延迟分位数、派生成本 |
| 重复 / 误差棒 | 0/4 有误差棒 | — | — | 必须有重复与 CI（超过范文） |
| 带数字的负结果 | 3/4 有 | — | — | ≥1 处，附机制 |
| 参考文献 | 19 | 34.5 | 65 | ≥35 |
| 5 年内文献占比 | 42% | 63% | 92% | ≥50% |
| DB 核心 venue 占比 | 14% | 31% | 53% | ≥30% |
| 自引占比 | 5% | 6.5% | 11% | ≤10% |
| 首页图 / artifact 链接 | 2/4 / 1/4 | — | — | 都要有 |

## 审查程序（摘要；完整清单见 `references/review-procedure.md`）

逐节逐段输出 `规则ID | met/partial/gap | 文件:行号（PDF 页/栏） | 现状 | 范文证据 | 要求的改动 | 验收测试`。分组：T 标题（3 条）、A 摘要逐句（6）、I 引言逐段（10）、P 问题与形式化（9）、M 方法与算法（10）、E 实验逐小节逐段（17）、F 图表（7）、R 相关工作（4）、C 结论（3）、B 参考文献（6）。先给每一段标注段落角色（Context / Gap / Example / Insight / Challenge / Approach / Contribution / Result / Roadmap），再逐条查规则。

## 阻断条件（任一命中 → Gate B 为 NOT CLEAN，不批准）

1. 正文超过 12 页或违反 `submit-pvldb` 硬规则。
2. 摘要/结论中有数字在正文表图里找不到、口径不一致，或首次出现在结论。
3. 声称保证（零误报、完备检测、预算最优、soundness）但无编号定理与证明落点，或定理前提未在实验中被检查。
4. 所有对照都是稻草人（无外部方法或其忠实重实现，也无自家弱化变体/消融）。
5. 对照不公平（预算/输入/硬件不一致，或对照实现被本轮修改拖慢未修复）。
6. 全稿没有任何带数字的自家不利结果。
7. 头条结果来自 DEV/调参数据，或冻结后的 TEST/gold/scorer 被改动。
8. 任一贡献 bullet 没有对应节或对应实测证据。
9. 首页 artifact 块为空、占位或个人主页。
10. 交叉引用/表格行号指向不存在的对象，或同一量两处数值不一致。
11. Gate A 有任一 FAIL / MISSING / 不在已证界限处的 PARTIAL 行。

## 双门循环（完整规则见 `references/two-gate-loop.md`）

- **Gate A**：方法必须在**每个**报告指标上胜过**每个** baseline。平局只有在稿件证明它处于不可超越的界限时才算未被击败（如 0% 误报、100% 检测、可证明的最少读取量）。否则要求**算法层面**的改进（不是改措辞、缩小声明、删指标或移到附录），在 DEV 预登记、按哈希冻结、新种子上评估一次，然后进入下一轮。放弃作答的廉价对照必须同时报总量、双方都作答子集、每检出一个故障的成本；以哪个口径为判据由作者在打分前预先登记，未登记时按最严口径。
- **Gate B**：稿件从标题到参考文献与范文对齐；任何 blocking/major 发现都要写成具体修订要求（改哪一段、改成什么结构、以哪篇范文哪一处为样板、如何验收），进入下一轮。
- **角色分离**：reviewer 只判定、不修改；fixer 只修改、不自批；复审由另一次独立 reviewer 执行。每轮都重跑完整 Gate A 矩阵。两门都过才批准；不降门槛、不宣布放弃。绝不输出录取概率。

## 四篇范文共同做到的事（候选稿最常漏的）

1. **把新问题挂到 DB 老概念上**：SPA 的 PVLDB 版标题专门加了 "Data Quality"；SCO 把聚合性质类比到 OLAP 的 distributive/algebraic 函数并给反例；DEE 把约束翻译成聚合查询。
2. **一个可手算的运行例子贯穿形式化**：SCO 的 9 行传感器表让每个定义都有数值演算；SPA 用玩具例子讲方法、换真实 pipeline 讲形式化与实验（避免"例子即测试集"）；DEE 的视频日志从 Intro 贯穿到 Listing。
3. **难点 = 朴素方案为什么不行，且朴素方案就是实验对照**：SCO Intro 难点 → §4.2 NAIVE → §8 对照；SPA I-P8 逐条 FFR 过滤 → §4.2 基线。
4. **操作性定义**：SCO 摘要把"解释异常"写成"删去谓词所选元组后异常消失"，形式化就是这句话的符号版。
5. **难度与可解性连写**：SPA "NP-hard（set cover 归约）→ 但本文规模下 ILP 可行（数千变量）→ 实测 ≤1.2 s"。
6. **性质要写前提并能被系统检查**：SCO 的反单调性只在非负数据上成立，并提供 check(D)；DEE 明确 append-only。
7. **每个趋势配"为什么"、每个实验小节有结论句**：DEE 每条曲线给机制解释；SCO 每小节一段粗体 Takeaway 带数字。
8. **主动报告自家不利结果并解释**：DEE 增量计算在全唯一列上总是更差；SCO MC 代价随 c 增长、DT 在非影响分区浪费时间；SPA 保留重复断言。
9. **部署证据与受控评估分节、分句**：SPA §2.4 vs §4、摘要 A7 vs A8；部署数字附口径与测量盲区。
10. **RW 每段以技术对比句收尾**：SPA 4/4 段；SCO 3/5 段；DEE 只有 1/3 段做到（反例）。

## 不要照搬的地方

- 四篇都**没有定理与证明**、都**没有外部已发表系统作对照**、都**没有误差棒**——这是 2013–2025 年这几篇的共同短板，不是研究轨道的标准；声称保证的稿件必须超过它们。
- SPA：组件 1 没有受控评估；评估集与开发集 6/9 重叠未作为威胁讨论；14%/21% 是百分点差却没说明；"significantly" 无统计检验；交叉引用笔误。
- DEE：摘要 0 个数字；无外部基线；RW 后两段纯罗列。
- YTC：无实验节、0 结果图表；94.5% 与 10,000× 在正文没有定义与出处；"novel" 8 次；交叉引用指向不存在的节。整篇作为**反面检查表**使用。
- SCO：文献 19 条且偏旧；贡献无节号；结果图注为描述式；公式下标笔误。

## 文件

- `references/fingerprints.md` —— 四篇逐篇计数、min/median/max 区间、研究稿标尺与判定。
- `references/review-procedure.md` —— 逐节逐段审查规则（T/A/I/P/M/E/F/R/C/B 共 75 条）、阻断条件、报告格式。
- `references/two-gate-loop.md` —— Gate A 全指标矩阵规则、Gate B、reviewer/fixer 轮次协议与批准条件。
- `references/sentence-templates.md` —— 按节组织的英文 `<slot>` 句式模板（含图注、RW 对比句、局限写法）。
- `references/spade_pvldb17.md` —— SPADE 逐句账本（已核验修正）。
- `references/deequ_pvldb11.md` —— Deequ 结构拆解（已核验修正）。
- `references/youtube_cicd_pvldb18.md` —— YouTube CI/CD 结构拆解 + 两篇工业稿对照与 20 条可检查规则（已核验修正）。
- `references/scorpion_pvldb6.md` —— Scorpion 完整新拆解（摘要逐句、引言逐段、各节、形式化与算法、图表、实验、文献、18 条规则）。
- `references/provenance.md` —— PDF URL/SHA256/字节数、选择理由、核验方法、DataHub 登记状态、恢复命令。

## 输出语言

给作者的报告用简体中文；模拟 PC 审稿意见及任何提交给审稿人或编辑的文字用学术英文；句式模板保持英文。
