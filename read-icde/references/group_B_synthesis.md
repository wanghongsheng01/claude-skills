# B 组综合分析：Text-to-SQL × LLM 选择/评测（ICDE 2025–2026）

## 0. 阅读覆盖情况（先说清楚读了什么）
| 任务编号 | 论文 | 笔记文件 | 全文 |
|---|---|---|---|
| 1 | CYANSQL（ICDE'26，复旦 + 腾讯云） | `B_cyansql.md` | **否**——IEEE 闭源，无 arXiv/GitHub；只有元数据（16 页、70 篇参考文献）和一条厂商二手描述（BIRD EX 73.47%） |
| 2 | Beyond Majority Voting: Hint-guided SQL Selection with LLM（ICDE'27 R1） | —— | **未找到**（arXiv、OpenAlex、Web 均无），未写笔记 |
| 2′ 替代 | CycleSQL: Grounding NL2SQL with Data-Based Self-Explanations（ICDE'25，复旦，与 CYANSQL 同组） | `B_cyclesql_substitute.md` | 是 |
| 3 | FusionSQL: Efficient & Effective Evaluator on Unseen and Unlabeled Data（ICDE'26） | `B_fusionsql_evaluator.md` | 是 |
| 4 | SQLMorph（ICDE'26，EAB） | `B_sqlmorph.md` | 是 |
| 5 | KaSLA: Knapsack Optimization-based Schema Linking（ICDE'26） | `B_kasla.md` | 是 |
| 1′ 补充 | HEXGEN-FLOW: LLM Inference Scheduling for Agentic Text-to-SQL（ICDE'26） | `B_hexgenflow_substitute.md` | 是 |

下文的结论基于 **5 篇全文精读**（CycleSQL、FusionSQL、SQLMorph、KaSLA、HEXGEN-FLOW）；CYANSQL 只在书目层面提及，不对其内容下结论。

---

## 1. 问题框架（Problem framing）的共同模式
1. **"部署/真实场景与 benchmark 脱节"是统一的开场**：FusionSQL（上线前无标签）、SQLMorph（企业 schema 多 join、多缩写）、HEXGEN-FLOW（企业异构 GPU、多租户 SLO）、KaSLA（schema linking 漏一列 SQL 就错）、CycleSQL（首次输出不是最好）。ICDE 审稿人显然偏好"运营/部署驱动"的 motivation，而不是"在 leaderboard 上再涨 1 个点"。
2. **把 LLM 子问题还原成经典的数据/优化问题**：
   - KaSLA → 0-1 knapsack（Eq.15），DP 求解；
   - FusionSQL → 分布偏移描述子到准确率的回归（Eq.8），本质是 AutoEval / performance prediction；
   - HEXGEN-FLOW → 最大化截止期满足概率的随机调度（Eq.1），并声称 NP-hard；
   - CycleSQL → why-provenance + NLI 判定；
   - SQLMorph → schema graph 上的 join 扩展 + JQG 同构去重 + 多重集结果匹配。
   **规律**：每篇都"引进一个 DB/OR 经典工具"（背包、溯源、图同构、LLF、Wasserstein 距离）作为差异化卖点。
3. **gap 证据的三种形式**：(a) **预实验图**——CycleSQL Fig.1（beam/choices 增大时"任一命中"准确率上升，证明正确答案在候选里只是没选出）、KaSLA Fig.1（与 GT linking 差 14.91%）；(b) **真实失败例子**——KaSLA Fig.2、CycleSQL Fig.2；(c) **挑战编号列表**——FusionSQL ξ1–ξ5、HEXGEN-FLOW C1–C3。
4. **"新指标揭示新现象"**：KaSLA（Recall⁺/Precision⁺ → Missing & Redundancy Seesaw）与 SQLMorph（EXP/EXR → 过/欠预测）都靠自定义指标立论。
5. **形式化程度差异很大**：FusionSQL、HEXGEN-FLOW 有正式 Problem Formulation 节；KaSLA 在 Preliminary 里给定义；CycleSQL 只有 2 个 Definition；SQLMorph 完全没有形式化（EAB 轨道可接受）。**没有一篇给出复杂度证明**（HEXGEN-FLOW 的 NP-hard 仅引用教材）。

## 2. 方法结构的共同模式
1. **3–4 个组件、与挑战一一对应**：HEXGEN-FLOW（C1–C3 ↔ 三条需求 ↔ 三个组件）、FusionSQL（ξ1–ξ5 ↔ 四个性质 ↔ 组件）写得最工整；KaSLA（打分 / 冗余容忍度 / 分层背包）、CycleSQL（溯源 / 标注 / 解释生成 / 验证）是"流水线式四步"。
2. **plug-in 定位**：KaSLA（替换 7 个系统的 schema linking）、CycleSQL（套在 7 个模型的候选上）、FusionSQL（model-agnostic）、HEXGEN-FLOW（不改输出只改调度）。plug-in 带来"广覆盖实验"，弥补单点提升小（CycleSQL 多数 +0.5～+5 点）。
3. **小模型 + 规则/优化 胜过大模型直接判断**：KaSLA 1.6B 打分器；CycleSQL 自训 T5-Large NLI 验证器优于 5-shot GPT-3.5 验证器（Table III：+2.6 vs +0.7 EX）；FusionSQL 3 层 MLP 优于 GPT-5 judge。**"不要把关键决策交给 LLM 自评"是这组论文的共同立场。**
4. **理论保证几乎为零**：没有近似比、误差界或正确性证明。FusionSQL 在 Objective 中写了 1−α 覆盖的预测区间，但方法和实验都没有兑现；HEXGEN-FLOW 只在 α 调参触发处用了一个 t 检验。

### 重点：多候选 SQL 的选择/验证是怎么做的
| 论文 | 候选来源 | 选择/验证机制 | 是否跨候选比较 | 是否多 vendor | 统计保证 |
|---|---|---|---|---|---|
| CycleSQL | 单一模型的 top-k（beam=8 或 API n=5） | **顺序首过**：按原排名逐个用"溯源解释 → NLI 蕴含"验证，第一个通过即输出，全失败回退 top-1 | 否 | 否（每次只增强一个模型） | 无；Oracle 验证器上限 86.9% EX |
| HEXGEN-FLOW（工作负载中的 CHESS） | 单一模型并行生成多个候选 + 自纠错 | LLM 生成 NL 单元测试，LLM-as-judge 打分选最高（论文只调度不改选择） | 是（judge 打分） | 否（Llama-3.1-70B 或 Qwen3-30B） | 无（t 检验仅用于系统调参） |
| SQLMorph | 被测系统各自的选择（CHESS 的 unit tester、self-consistency 等，在 Background §II-2 中归纳） | 不提出选择法；EXP/EXR 只用于有 GT 的离线诊断 | —— | 否（统一 GPT-4o） | 无 |
| FusionSQL | 不涉及单题候选 | 数据集级准确率估计，可用于"选模型/批准发布"，不能用于"选单个 SQL" | —— | 评估对象覆盖 20+ 开源模型，但需白盒 embedding | 承诺未兑现 |
| KaSLA | 不涉及 SQL 候选；选择对象是 schema 元素 | 背包优化在冗余预算下选元素子集 | —— | 否 | 无 |
| CYANSQL（未读） | 标题/二手来源显示为"聚类式 test-time scaling" | **未知**——这是最需要补读的一篇 | 未知 | 未知 | 未知 |

**结论**：在已读论文中，候选选择要么是顺序首过的验证（CycleSQL），要么是 LLM-as-judge（CHESS 风格），要么默认多数投票（SQLMorph Background 中的 self-consistency）；**没有一篇组合多个 LLM vendor 的候选，没有一篇对选择结果给出统计保证（如错误接受率上界或带覆盖率的拒答）**。

## 3. 实验协议（Experimental protocol）
| 维度 | KaSLA | FusionSQL | SQLMorph | CycleSQL | HEXGEN-FLOW |
|---|---|---|---|---|---|
| Benchmark | BIRD dev、Spider dev、Spider2.0-lite（100 例） | Spider、WikiSQL、BIRD、SParC、CoSQL、SynSQL-2.5M、Spider 2.0（5 组迁移） | 仅 BIRD dev | Spider（dev+test）、Spider-Realistic/Syn/DK、ScienceBenchmark（**无 BIRD**） | BIRD dev（2 库）、Spider 1.0（trace） |
| LLM backbone | GPT-4(-turbo)、DeepSeek-V3、CodeS-15B、StarCoder2-15B；自身 DeepSeek-Coder-1.3B + RoBERTa-L | Qwen2.5-72B、Llama-3.1-70B、DeepSeek-Coder-33B、XiYanSQL-14B、CSC-SQL-7B（+20 元训练、5 未见）；judge 用 GPT-5 | GPT-4o + text-embedding-3-small | GPT-3.5-turbo、GPT-4、DeepSeek-33B（CHESS）、T5 系列 | Llama-3.1-70B、Qwen3-30B |
| 基线数 | ~14 | 7（+自身变体） | 3 个被测系统 | 7 个被增强模型 + 3 种验证器 | 5 个服务系统 + 2 消融 |
| 主要指标 | EX、VES、Recall⁺/Precision⁺/F1⁺ | MAE（5 seeds ±95% CI）、Pearson r | EX、FPR/SLR、EXP/EXR/F1 | EM、EX、TS | P95 SLO attainment、吞吐、Jain 指数 |
| 成本报告 | 每实例延迟（秒） | 数据构造预算 $1000（实际 ≈$666）；评估延迟；judge API 成本仅脚注 | **声称低成本但无任何数字** | 平均迭代次数、ms 级延迟 | P95 延迟、吞吐、调参 CPU 秒数、每查询 LLM 调用数 |
| token / $ | 否 / 否 | 否 / 仅数据构造 | 否 / 否 | 否 / 否 | 调用次数有，token/$ 否 |
| 方差/显著性 | 无 | 5 seeds CI | 无 | 无 | 3 seeds 误差棒 |

**共性**：
- **BIRD + Spider 是事实标准**（5 篇中 4 篇用 BIRD dev；CycleSQL 没用 BIRD 也被接收，但这是 2025 年初的稿件）；Spider 2.0 只是"点缀"（KaSLA 100 例、FusionSQL 一组迁移）。
- **单 vendor 是默认**：即使同时用了 GPT 和 DeepSeek（KaSLA），也是"不同基线配不同 backbone"，从未在一个系统内混合多家模型的输出。
- **成本以延迟为主**，**没有一篇报告 token 消耗或每题美元成本**——对 test-time scaling / 多候选方法来说，这是明显的评审弱点，也是新论文的差异化机会。
- **统计严谨性普遍偏弱**：大多数单次运行、无显著性检验；KaSLA Table V 存在算术上不可能的数字（unseen 子集 EX 86.48 而总体 60.17）仍被接收。

## 4. 写作结构的共同模式
1. **标题**：三种模式——"<系统名>: <技术> for <任务>"（SQLMorph、HEXGEN-FLOW、CYANSQL）、"<技术>-based <任务> for <场景>"（KaSLA）、"Grounding/An Efficient and Effective <X> on <困难设定>"（CycleSQL、FusionSQL）。都在标题中点出 **技术范式**（knapsack、clustering-based TTS、query mutation、data-based self-explanations）或 **困难设定**（unseen and unlabeled）。
2. **摘要**：背景 → gap（常带"why"一句）→ 系统名 + 一句核心思想 → 2–3 个技术点 → 实验规模 → 1–2 个亮点数字（"up to 17%"、"1.42∼1.56×"、"82.0% (+2.6%)"）。FusionSQL 是例外：完全不放数字，强调应用价值。
3. **引言**：5–7 段；第 2–4 段建立 gap（例子或编号挑战）；倒数第二段方法概述，常用 **圆圈编号/"To tackle C1"** 与图对应；**贡献列表 3 条为主**（KaSLA、SQLMorph、CycleSQL、HEXGEN-FLOW 各 3 条，FusionSQL 5 条）。Figure 1 有三种：性能差距柱状图（KaSLA）、pass@k 预实验（CycleSQL）、概念/流水线图（FusionSQL、HEXGEN-FLOW）；SQLMorph 没有 motivating figure。
4. **Related Work 放在实验之后**：5 篇中 4 篇（KaSLA、SQLMorph、CycleSQL、HEXGEN-FLOW）放在最后，只有 FusionSQL 紧随引言。分类通常为"Text-to-SQL 方法"+"本文所借用的技术领域"（provenance、LLM serving、label-free estimation 等）两类。
5. **实验节占 40–55% 篇幅**，按 RQ（KaSLA 4 个、FusionSQL 5 个）或按贡献分节 + Takeaway 框（SQLMorph）。
6. **常用技巧**：给现象起名字并加粗（Seesaw Problem）；一个 running example 贯穿全文（CycleSQL 的 Airbus 例子、SQLMorph 的 Customer–Purchase）；Oracle/上限实验（CycleSQL）；"先写预期方向、再给实测"（SQLMorph Table IX/X）；单列 Limitation 节（KaSLA）；"AI-Generated Content Acknowledgement" 已成为 ICDE 2026 的标配（KaSLA、FusionSQL、SQLMorph 都有）。

## 5. 可攻击的开放缺口（新 ICDE 论文的切入点）
1. **候选选择缺统计保证**——CycleSQL §IV-D / §V-A（顺序首过，验证器误判即错，无错误率控制）；FusionSQL §III-C（承诺 P(M* ∈ 区间) ≥ 1−α 却未实现，表中 "±95% CI" 只是种子间区间）。
   → 切入：用 conformal risk control / Learn-then-Test 校准选择阈值，给出"被接受 SQL 的错误率 ≤ ε"的有限样本保证，并允许拒答（abstain）或升级到更强模型；报告实际覆盖率与名义水平的对比。
2. **从未组合多个 LLM vendor 的候选**——KaSLA §V-A3（因 API 成本把 GPT-4o 换成 DeepSeek-V3，各基线各配一个 backbone）、SQLMorph §III-2（框架支持多后端，实验只用 GPT-4o）、CycleSQL Table I（每次只增强一个模型的 top-k）、HEXGEN-FLOW §5.1（单一开源模型）。
   → 切入：异构模型候选池上的选择——不同 vendor 错误相关性更低，可建模"跨模型一致性"作为证据；研究同 vendor 内多采样 vs 跨 vendor 少采样在同等预算下的准确率。
3. **token / 美元成本几乎无人报告**——SQLMorph §III（声称 cost-conscious 却无数字）、KaSLA Table IX（只报秒）、CycleSQL Fig.8b（只报 ms）、HEXGEN-FLOW §5（只报延迟/吞吐与调用次数）、FusionSQL §V-B（只报造数据的钱）。
   → 切入：把"生成多少候选、调用哪个模型、何时停止"做成 **预算约束下的选择问题**（可直接借用 KaSLA §IV-C 的背包形式：价值 = 预期正确率提升，重量 = token 成本），报告 accuracy–$ Pareto 前沿。
4. **选择机制不利用候选间的部分一致性**——CycleSQL 只逐个独立验证；SQLMorph §VI 的 EXP/EXR 只在有 GT 时离线诊断；多数投票要求结果完全相等。
   → 切入：把 SQLMorph 的 cell 级 precision/recall 改为 **候选两两之间的软相似度**（无需 GT），在执行结果上做软聚类/加权投票，再与 CycleSQL 式的数据溯源证据结合；这也是 CYANSQL（"clustering-based"）可能的方向，需补读确认以避免撞车。
5. **无标签评测依赖白盒、只到数据集级**——FusionSQL §IV-B（需模型最后一层 pooled embedding，闭源 API 模型无法使用；只估计数据集平均准确率）。
   → 切入：只用输出侧信号（候选一致性、执行结果分布）对黑盒/多 vendor 系统做 **逐题置信度 + 数据集级准确率** 估计，并与 Prediction-Powered Inference（FusionSQL 引用但未比较的 [41]）对比：少量标签 + 无偏区间。
6. **调度与选择被割裂**——HEXGEN-FLOW §4 明确不改变输出，候选数和修正轮数视为固定（约 20 次调用/题）。
   → 切入：**SLO/预算感知的自适应采样与早停**：当已有候选达到足够置信（可用第 1 点的校准阈值）即停止生成，把节省的算力分给难题；联合报告准确率、P95 延迟与 $。
7. **评测覆盖不足、鲁棒性未纳入选择方法评估**——CycleSQL §V-A1（无 BIRD）、SQLMorph §III-4/§IV-F（只 BIRD dev、3 个 2023–24 年系统、扩展集仅 58 条）、KaSLA Table VIII（Spider2.0-lite 仅 100 例）。
   → 切入：在 BIRD + Spider 2.0 之外，用 SQLMorph 的 JQE（多 join）与 TQA（缩写化命名）变体作为选择方法的 **压力测试**，检验选择/验证器在分布偏移下是否仍守住错误率保证。
8. **实验报告严谨性**——KaSLA Table V 数字不一致；KaSLA/SQLMorph/CycleSQL 均为单次运行、无显著性；FusionSQL 表格数字规律性过强。
   → 切入（作为差异化写作点）：多种子、bootstrap 置信区间、配对检验（如 McNemar 检验 EX 差异）、公开每题预测与成本日志——在这个子领域里会明显"更像 ICDE 应有的严谨度"。

## 6. 给 ICDE 2027 投稿的直接建议
- Motivation 用 CycleSQL 式的 **pass@k vs top-1 预实验图** 证明"答案在候选里"，再用一个真实失败例子说明现有选择（多数投票/LLM judge）为何失败。
- 把选择问题 **形式化**（输入：候选集合 + 执行结果 + 预算；输出：选中 SQL 或拒答；约束：错误率 ≤ ε、成本 ≤ B），给出至少一个可证明的保证（有限样本覆盖或风险界）——这是本组所有已读论文都缺的东西。
- 实验最低配置：BIRD dev + Spider 2.0（或其子集）+ 一个鲁棒性变体；≥3 个 vendor 的模型；基线包含多数投票 / self-consistency、LLM-as-judge（CHESS 式单元测试）、CycleSQL 式验证器；报告 EX、token、$、延迟、经验错误率与覆盖率；多种子 + 显著性。
- 写作上沿用"挑战编号 → 设计原则 → 组件"的对应结构，Related Work 放在实验后，贡献 3 条，标题点出技术范式（如 "Conformal" / "Budget-aware"）。
- **先补读 CYANSQL**（需机构 IEEE 访问），确认其聚类选择是否已覆盖第 4 点，以免撞车。
