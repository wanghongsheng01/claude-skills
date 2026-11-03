# Group A 综合分析：LLM-for-data 中的成本/准确率权衡（5 篇 ICDE 2025–2026 论文）

覆盖论文与阅读状态：
| 笔记 | 论文 | 会议 | 全文来源 | FULL TEXT READ |
|---|---|---|---|---|
| A_sparq.md | SPARQ（离线 TableQA 自适应路由） | ICDE 2026 | 作者 GitHub full version（27 页，含附录） | yes |
| A_carrot.md | CARROT（成本约束 RAG 检索优化） | ICDE 2026 | arXiv 2411.00744v2（注明 Accepted to ICDE 2026） | yes |
| A_bond.md | BOND（关系数据上 LLM 分析的协同设计） | ICDE 2026 | 无开放全文 | **no（仅摘要）** |
| A_shapley_csv.md | Constrained Shapley Value 选 ICL 示例做数据整理 | ICDE 2025 | 合作者主页托管 PDF（14 页 IEEE 版） | yes |
| A_zendb.md | ZenDB（查询模板化文档集合） | ICDE 2025 | arXiv 2405.04674v1（投稿前预印本，标题不同） | yes |

下文对 BOND 的判断只基于摘要，均已注明。

---

## (1) 问题建模：把"LLM 任务"变成数据工程优化问题的共同套路

**共同模式：选定一个"决策变量"，让 LLM 质量变成代价约束下的目标或约束。**

| 论文 | 决策变量 | 目标 | 约束 | 质量代理（proxy） | 形式化程度 |
|---|---|---|---|---|---|
| CARROT | 有序 chunk 序列 Φ | max W(Φ)（reranker 分） | Σ token ≤ B | reranker 分数（r=0.83 与 ROUGE-L 相关） | Definition + Eq.1 + Theorem（NP-hard） |
| SPARQ | 算子集合 S ⊆ O | min COST(S)（运行时间） | 充分性分数 Q ≥ τ | 学习得到的 verifier（跨模态 MI） | 加粗定义 + Eq.1，无复杂度结论 |
| CSV | 示例子集 D′，\|D′\|≤k | max U(D′)（验证集 F1） | LLM API 预算 B | 200 条验证样本上的 F1 | Problem 1/2 + 7 个 Proposition |
| ZenDB | 查询计划 + 每个元组要读的文本片段 | 最小化 LLM 美元成本，同时保持 P/R | 无显式预算 | 无（直接是 LLM 输出） | Preliminaries 定义 + 正确性定理；成本模型为启发式 |
| BOND（摘要） | 批划分 + 数据布局 + 调度 | min 执行时间 | GPU tile/硬件 | 无（假设精度不变） | bin-packing + 树搜索（细节未知） |

归纳出的 5 条规律：
1. **"三个 Challenge"框架几乎是标配**：CARROT（关系/非单调/多样性）、SPARQ（成本/推理与隐私/资源）、ZenDB（结构未知/数据模型/成本）、CSV（#P-hard + 两个 LLM 特有挑战）都用 2–3 个编号挑战，并与 2–4 个技术组件一一对应。
2. **成本以三种方式进入问题**：(a) 作为**硬约束**（CARROT 的 token 预算 B、CSV 的 API 预算 B）；(b) 作为**目标**（SPARQ min COST、ZenDB 最小化 LLM 调用、BOND 最小化执行时间）；(c) 作为**训练信号中的惩罚项**（SPARQ reward = acc × exp(−λ·COST) × 长度惩罚；CARROT UCB 中的 −λ·cost/B）。尚无论文同时把"准确率约束 + 成本目标 + 理论保证"三者做全。
3. **用便宜代理替代昂贵的 LLM 质量评估**是关键动作：reranker 分（CARROT）、学习的 verifier（SPARQ）、子样本 F1（CSV）、summary + search_oracle（ZenDB）。这些代理的误差都**没有被纳入理论保证**。
4. **借用经典 DB/算法概念做"包装"**：policy tree + MCTS（CARROT）、knapsack 式约束（CARROT）、昂贵谓词排序/谓词下推/投影上拉/惰性物化/provenance（ZenDB）、Shapley value 数据估值 + 多臂老虎机 top-k 识别（CSV）、算子/计划选择 = 查询优化器（SPARQ）、bin-packing（BOND）。审稿人看到熟悉的 DB 概念更容易认可"DB 贡献"。
5. **复杂度结论多为借用或缺失**：只有 CARROT 证明了 NP-hard（且证明放在 TR）；CSV 引用 SV 的 #P-hard；ZenDB 只有正确性定理；SPARQ 只给出 O(2^{m+n}) 暴力复杂度作动机。ICDE 并不强制要求新的难度证明，但有会加分。

## (2) 方法结构的共同模式

1. **"离线准备 + 在线轻量决策"两阶段**：CARROT（离线 grid search 训练 configuration agent → 在线 MCTS）、SPARQ（离线枚举 15 种算子集打标签 → 在线 router + verifier）、ZenDB（离线建 SHT/模板/表填充 → 在线树搜索）、CSV（选例阶段花预算 → 推理阶段复用；BCSV 还有离线/在线两阶段）、BOND（推理前数据重组 → 推理时批构造，摘要可见）。离线成本均被单独报告并论证可摊销。
2. **"学习组件预测配置/路由，搜索或规则组件保证质量"**：CARROT 的 agent 只预测 MCTS 超参和 reranker，而不直接预测结果（作者专门论证了原因）；SPARQ 的 router 预测算子集，verifier 兜底回滚。即"learned 部分做 knob tuning，确定性部分做主计算"——这与 learned query optimizer 的思路一致。
3. **"先近似、再校验/回退"（approximate-and-verify）**：SPARQ 的 rollback/fallback、ZenDB 的"容忍 FP、杜绝 FN"（表填充时宁大勿漏，再由树搜索精化）、CARROT 在所有深度选最优节点而不是只看叶子。
4. **复用/摊销是降本主杠杆**：ZenDB 的模板复用（LLM 成本只与模板数相关）、CSV 的 activated contribution（一次 U(S) 被 n 个示例共享）、CARROT 的批量 reranker 打分、BOND 的前缀共享（摘要）、SPARQ 的动态 batching + KV cache 复用。
5. **系统层优化作为第 3/4 个贡献点**：SPARQ 的 CPU–GPU 调度、CARROT 的并行展开、BOND 的 bubble-free 调度器——"算法 + 系统"组合比纯算法更像 ICDE 论文。

## (3) 实验协议

| 论文 | 数据集 | 基线数量（最新年份） | 质量指标 | 成本报告 |
|---|---|---|---|---|
| CARROT | 3（WikiPassageQA、MS MARCO、HotpotQA） | 9 + 2 个自变体（2024–25；无 DB 顶会方法） | ROUGE-1/L、BLEU-1、F1 | **token**（每查询在线 token；离线索引 token 与时间），延迟；不报美元 |
| SPARQ | 5（WikiTQ、TabFact、FeTaQA、TableBench、NIAT） | 约 12 个（含 SIGMOD'24 Table-GPT、VLDB'24 ReAcTable、NAACL'25 H-STAR） | 准确率、EM、ROUGE-L | **延迟、LLM 调用次数、token 吞吐、总 token**（3.8M vs 48.0M）；不报美元（论点是零 API 成本） |
| CSV | 14（Magellan 7 个 EM + ED/MVI/SM/DN/DD） | 13（含 ICDE'24 BatchER、ICDE'21 Ditto/IPM、VLDB'20 Baran） | F1、准确率，5 次重跑方差 + critical difference | **美元预算（$10/数据集）+ token 数 + 时间** |
| ZenDB | 3（论文、市政议程、违规通知；自建，41–100 篇文档） | 4 个策略型基线（GPT_single/merge、RAG_seq/tree） | 元组级 precision/recall | **美元 + token**（每查询每文档），延迟，离线成本单列，每 $1 可跑查询数 |
| BOND | 未知 | 未知 | 未知 | 执行时间（up to −71.8%） |

共同做法：
- **RQ 驱动**（CARROT 5 个 RQ、SPARQ Q1–Q5）或 "Experiment k"（ZenDB）、按小节（CSV）。
- **固定实验矩阵**：主结果大表 + 跨 LLM 表（CARROT：Llama3-8B/DeepSeek-V3/GPT-4o；SPARQ：Qwen3-4B/30B/Max；CSV：gpt-3.5/gpt-4o-mini/Llama；ZenDB：GPT-4-32k vs GPT-3.5）+ 消融 + 参数敏感性 + 泛化矩阵（CARROT 6×6 领域与 3×3 数据集，SPARQ 3×3 数据集）+ case study。
- **成本报告格式不统一**：token（CARROT、SPARQ）、美元（ZenDB、CSV）、时间（全部）。**只有 ZenDB 和 CSV 报美元**；没有一篇报告能耗或 GPU-hour 成本，也没有一篇画出完整的**成本-质量 Pareto 前沿**（CARROT Fig.6b 是"时间-质量"散点，最接近）。
- **离线/准备成本单列并论证可摊销**：CARROT Table IV + "一次性成本" Remark；ZenDB Table 6–7 + 端到端摊销段落；SPARQ 用少量难样本（92–487 条）训练。
- **上界/oracle 变体**：CARROT_upper（穷举）、SPARQ 预实验中的 Route+Check（人工修剪），用于说明"还有多少提升空间"。
- **规模普遍偏小**：ZenDB 每数据集 9 条查询、≤100 篇文档；CSV 只在 200 条样本上估计效用；CARROT 的可扩展性只到 10 万 chunk。

## (4) 写作与论文结构

- **标题**：三种模式——(a) `缩写: A [Cost-Efficient / Learned Cost-Constrained / Co-Designed] Framework/System for X`（SPARQ、CARROT、BOND，全部 2026 年）；(b) `Querying <数据性质> <数据> with LLMs`（ZenDB，把洞见写进标题）；(c) `Tailoring <经典理论> for <问题> towards <任务>`（CSV）。2026 年的三篇都在标题里放了成本/系统类修饰语。
- **摘要**：都是"背景 → gap（2–4 个并列缺点）→ 提出 X → 2–3 个组件 → 带 up to / on average 的数字 → 代码/可用性声明"。数字口径常不严谨（SPARQ 的 10.19× 在摘要是 up to、正文是 average；CSV 的 5.90% 在摘要是 average、贡献列表是 up to）。
- **引言**：
  - 都有 Figure 1 motivating example（CARROT Eiffel Tower chunks、SPARQ 足球比赛表、ZenDB 市政议程报告、CSV 实体匹配 prompt）；ZenDB 和 SPARQ 还有第二个"定位图"（ZenDB Fig.2 cheap vs accurate；SPARQ Fig.2 预实验）。
  - 段首加粗短语串联逻辑（ZenDB、CSV、CARROT 的 "Challenge k:"）。
  - 贡献列表 4–6 条，2026 年的论文倾向于在每条后标注章节号或 "addressing Challenge k"。
  - 预先回应审稿人质疑：CARROT（Agentic RAG 是否让标准 RAG 过时）、SPARQ（为何不用 VPC）、CSV（为何不直接塞满上下文）。
- **章节结构**：Intro → Preliminaries/Problem → (Motivation/预实验) → Overview → 2–3 个方法节 → Experiments → Related Work（CSV、ZenDB 放末尾；CARROT 放在问题定义之后；SPARQ 与 Preliminary 合并放在前面）→ Conclusion。实验约占 3–4 页（全文 25–30%）。
- **"外放"策略**：CARROT、CSV 把证明放在 GitHub Technical Report；SPARQ 发布带 12 页附录的 full version。ICDE 页数紧，这已是常规做法。
- **ICDE 2026 新增**：CARROT 和 SPARQ 都有 "AI-Generated Content Acknowledgment" 段（ICDE 2026 政策），我们的 ICDE 2027 投稿需要注意。
- **ICDE 对小瑕疵容忍度不低**（SPARQ 的图号/数字不一致，CSV 的交叉引用错误与模型名笔误），但这些仍是风险点，我们应避免。

## (5) 留给新 ICDE 论文的开放缺口（8 条，均对应具体论文与章节）

1. **代理质量与真实 LLM 质量之间缺少理论桥梁**（CARROT §II Definition 2 / §VII-C Fig.8；CSV §II-B 对 Problem 2 的讨论）。CARROT 用 reranker 分作为目标，只给出经验相关性 r=0.83；CSV 明确承认 top-k CSV 与最优 k-子集（Problem 1）之间的解质量"留作未来工作"。**可攻击点**：给出"代理误差 → 最终质量"的界，或设计带校准（calibration）的代理，并得到有保证的预算分配算法。

2. **"成本约束 + 准确率保证"的联合优化尚未完成**（SPARQ §V-A Eq.1；ZenDB §6.1）。SPARQ 是 min COST s.t. 学习的充分性分数 ≥ τ（τ 全局固定为 0.8，无准确率保证）；ZenDB 是启发式的昂贵谓词排序，不支持用户给出预算或目标精度。**可攻击点**：允许用户指定"精度目标或美元预算"的 LLM 查询优化器（例如带置信区间的级联 LLM 计划、预算感知的计划枚举），可输出成本-质量 Pareto 前沿。

3. **静态、每个数据集一次性的决策 vs 每查询/每元组自适应**（CSV §II-C、§IV-A 每个数据集只选一次示例；ZenDB 对每个模板只用一个代表文档做表填充，§5）。**可攻击点**：在线/增量版本——示例选择或模板识别随工作负载演化而更新，并在选择成本与推理收益之间做摊销分析（选择阶段花的钱何时能回本）。

4. **跨组件交互与顺序被忽略或只做启发式处理**（CSV §II-B "Example Ordering" 采用 CSV 升序启发式，并承认是开放问题；CARROT §V 虽处理了 chunk 顺序，但只在召回的 top-k 候选内、固定 chunk size 256）。**可攻击点**：联合"子集 + 顺序 + 粒度（chunk size/表切片粒度）"的优化，例如对 TableQA 的行/列子表顺序或文档片段顺序进行建模。

5. **规模与工作负载过小，缺少可扩展性与真实负载**（ZenDB §7.1：每数据集 9 条查询、≤100 篇文档；CSV §IV-A：只用 200 条样本估计效用、最大数据集约 2.9 万条；CARROT §VII RQ3 仅 1 万–10 万 chunk）。**可攻击点**：构建大规模、带真实查询日志的基准（如数千条查询、10^5 级文档/表），并研究跨查询的计算复用（物化中间 LLM 结果、语义缓存）。

6. **多表、跨文档推理基本未覆盖**（ZenDB §4.2 只允许 doc_id 上的文档内等值 join，作者计划未来放宽；SPARQ §IV 面向单表，§V-C 承认算子并行未利用；CARROT 只做单语料检索）。**可攻击点**：跨文档/多表 join 的 LLM 语义 join 优化（blocking + 级联 + 成本模型），或多表 TableQA 的算子路由。

7. **成本口径单一，缺少统一的"美元 + 延迟 + GPU 时间 + 能耗"模型，以及 API vs 自托管的统一视角**（CARROT Table II/IV 只报 token；SPARQ §VI-C 只报延迟/token，主张"零 API 成本"；BOND 摘要只报执行时间；ZenDB §6.1 说明成本模型可换成延迟但未实验）。**可攻击点**：提出混合部署（本地小模型 + 云端大模型）的路由/级联框架，用统一成本模型在两者间做最优分配——SPARQ（离线）与 ZenDB/CSV（在线 API）的设定恰好可以合并。

8. **语义一致性与正确性保障缺失**（ZenDB §4.2 明确把"抽取的属性值与谓词判断结果不一致"排除在范围外；BOND 摘要未说明数据重排是否改变 LLM 输出；SPARQ verifier 误判率与最终准确率的关系未分析，§V-B）。**可攻击点**：为 LLM 驱动的查询处理定义一致性语义（如同一元组多次 LLM 调用之间的约束检查与修复），或证明某些优化（重排、批处理、前缀共享）是"输出保持（output-preserving）"的，或量化其精度影响并纳入优化目标。

---

### 给 ICDE 2027 投稿的可操作建议（基于以上 5 篇）
- 问题定义节务必给出：决策变量、成本模型（同时给 token 和美元，必要时给延迟）、约束（预算或精度阈值）与目标；最好有复杂度结论（NP-hard 或 #P-hard），证明可放 TR。
- 引言用一个同时暴露所有 gap 的 Figure 1，加一个"成本-质量定位图"（参考 ZenDB Fig.2）；明确 3 个 Challenge ↔ 3 个技术 ↔ 3 组实验。
- 实验至少包含：主结果（质量 + 成本同表）、跨 LLM、离线成本与摊销分析、消融、参数敏感性、可扩展性、成本-质量 Pareto 曲线（这是 5 篇论文都没做完整的，可作为差异化）。
- 准备 GitHub 技术报告/full version 与代码；按 ICDE 政策加入 AI-generated content 声明。
