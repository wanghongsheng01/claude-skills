# SPARQ: A Cost-Efficient Framework for Offline Table Question Answering via Adaptive Routing (ICDE 2026, Regular research paper)
- Source of full text: arXiv 上无版本（多种检索均未命中）。全文来自作者官方 GitHub 仓库 https://github.com/authurlord/SPARQ 中的 `SPARQ-Full-Version.pdf`（摘要中脚注明确指向该仓库 "Code, full version and artifacts are provided"）。IEEE DOI 10.1109/ICDE65706.2026.00199（proceedings pp. 2668–2682，15 页）。Full version 共 27 页 = 正文 12 页 + 参考文献约 3 页 + Appendix A–Q 约 12 页；正文与 ICDE 版应基本一致（文中写 "Fig. 8 (now located in Appendix D)"，说明是由会议版扩展而来）。作者：Yang Liu, Mengyi Yan*, Jiao Xue, Weilong Ren, Yutong Ye, Haoyi Zhou, Jianxin Li*, Zhumin Chen（北航、山大、深圳计算科学研究院、浪潮云）。FULL TEXT READ: yes（正文全部 + 附录主要部分）。PDF 存于 pdfs/A/SPARQ_Full_Version_github.pdf。
- Length: 正文 12 页（IEEE 双栏），参考文献 89 篇；正文 Figures 7 个（Fig.1–7），正文 Tables 7 个（Table I–VII）；附录另有 Fig.8–18（调度流水线、案例、全部 prompt）与 Table VIII–XVIII；编号公式 5 个（Eq.1 优化目标、Eq.2 reward、Eq.3 verifier 分数、Eq.4 InfoNCE、Eq.5 总损失）；0 个 Theorem/Lemma；伪代码以 Fig.4 "Workflow" 形式给出（6 行）。

## 1. 科学问题的本质 (Problem essence)
- **表面问题**：在本地小模型（Qwen3-4B / 30B-A3B，2×RTX 4090）上做 Table QA，既准又快又不泄露隐私。
- **本质问题**：一个**按查询自适应的算子集选择（operator-set selection）问题**——在"足够回答"的约束下最小化执行成本，核心对象是"最小充分子表（minimally sufficient subtable）"。
  - 输入：(q, T)、离线 LLM、算子池 O = {o_prep, o_col, o_row, o_Ret, o_SQL}（+ o_Base），候选算子集合族 𝕊 = {S0..Sk}（按成本排序，k=15）。
  - 输出：算子集 S 及其产生的子表 T_S 与中间上下文 Context(S)，最终答案 a。
  - 约束：verifier 充分性分数 Q(q, T_S, Context(S)) ≥ τ（默认 τ=0.8）；|S| ≤ 3。
  - 目标：min_{S⊆O} COST(S)（Eq.1；COST 定义为生成答案的总运行时间）。
  - 理想对象定义："minimally sufficient subtable" T* ⊂ T：(a) 含回答 q 所需信息（sufficiency），(b) token 长度最小（minimality）；精确求解需 O(2^{m+n}·COST(LLM)) 枚举，所以用"approximate-and-verify"近似。
- **为什么现有方法不够（根因）**：引言列出 3 个挑战（(a) 金钱成本与效率/overthinking；(b) LLM 推理与隐私限制；(c) 数据与资源约束），而真正驱动设计的是 Section III 预实验得出的 5 个发现：
  1. 离线 LLM 在长表上崩溃（"reasoning cliff"，远早于上下文窗口上限）；
  2. 符号执行（SQL/Python）强但脆，失败率可达 30.30%；
  3. Overthinking：H-STAR、ReAcTable 比 Select Row 多 3.3×/3.5× LLM 调用，准确率却分别低 14.08%/40.06%；
  4. 传统 RAG 把行列当孤立文本，破坏表结构（比 Base 低 2.78%），但带 rewrite + 混合检索的 RAG 有用；
  5. "minimal yet sufficient" 信息最好：人工修剪算子的 Route+Check 比 Base 高 21.31%。
  - 证据：Fig.1 motivating example（WikiTQ "how many games were played after October 1st?"，四种策略只有 Select Column + LLM 答对 11）；Fig.2 预实验（WikiTQ 中 476 个 >4K token 的难样本，11 种方法的准确率与平均 LLM 调用次数）。
- **问题定义形式**：没有单独的 Definition/Problem 环境；"Minimally sufficient" 以加粗段落定义，优化目标 Eq.1 写在 Router 小节内部。**无复杂度（NP-hard）结论**，只给出暴力枚举复杂度 O(2^{m+n}) 作为动机。Notation 用 Table I 汇总。

## 2. 方法的最关键之处 (Key insight)
- **一句话 key idea**：对离线小模型而言，"少即是多"——不要堆叠更深的推理链，而是为每个查询预测**最便宜但足够**的算子组合，再用一个跨模态 verifier 判断充分性，不够就按 fitness 概率回滚（rollback）或兜底 SQL（fallback），全程不重新调用 LLM 生成。
- **技术组件**：
  1. **扩展算子池**（工程组合为主，但 o_Ret 被称为 "key innovation"）：o_col/o_row 采用 LLM 枚举 ∪ SQL 选择的双路径；o_Ret 做多粒度 query rewrite（general/balanced/specific）+ SBERT dense + BM25 sparse + Weighted RRF；o_SQL 不可行时返回 [UNKNOWN] 自动跳过。对应 gap 2、4。
  2. **Adaptive Query Router E**（核心新意之一）：两种实现——training-free（LLM in-context 选算子）与 training-based（BGE-m3 多分类器，预测 P(S|q,T)）。训练数据：在少量难样本上枚举 15 种算子集执行离线 LLM，reward R = acc × exp(−λc·COST(S)) × ρ_len(S)（Eq.2，把成本直接写进监督信号），以 reward 为 soft label 做知识蒸馏 + InfoNCE。每个算子的 fitness 概率 o_i.p = 包含 o_i 的算子集概率之和。对应 gap 1、3。
  3. **Mutual-Information Verifier Q**（核心新意之二）：Q = σ(α·f(q,T_S) + β·f(q,Context) + γ·f(T_S,Context))（Eq.3），f 为 BGE-Reranker-v2-m3 CrossEncoder，三模态对（query、子表、SQL）用 InfoNCE 做对比训练（Eq.4–5，α=β=1, γ=0.2）；负样本来自错配 query-table、跨 query 上下文替换、随机删行列。Rollback：删去 fitness 最低的抽取算子并重新评估，直到充分或回到 S0；Fallback：全表生成 SQL 补证据。对应"router 过度剪枝"问题。
  4. **CPU–GPU 协同调度**（系统工程）：producer-consumer 流水线、多线程异步 SQL、按 router 预测成本分组的动态 batching、KV cache 复用（细节在 Appendix D）。对应效率 gap。
  - 真正的新东西：把"充分性"显式建模成可学习的约束 + approximate-and-verify 的 router/verifier 协同；算子池与调度是工程组合。
- **理论保证**：无。只有 O(2^{m+n}) 暴力复杂度动机与各算子调用次数的成本分析。论文自己承认算子可并行但当前调度未利用（future work）。

## 3. 实验设计 (Experiments)
- **研究问题（5 个）**：Q1 与在线方法比有效性；Q2 同一离线环境下与其他方法比（跨模型规模）；Q3 效率（调度）；Q4 自适应性（不同查询/表规模）；Q5 组件贡献（消融）。另有超参与泛化。
- **数据集（5 个）**：WikiTQ（denotation accuracy）、TabFact（二分类准确率）、FeTaQA（ROUGE-L，长答案）、TableBench（886 个金融报告表，ROUGE-L）、NeedleInATable/NIAT（脏表、>100K token，EM）。训练 router/verifier 只用少量难样本：487/476/376/92/199 条。
- **基线**：训练类：TaPas (ACL'20)、TAPEX (ICLR'22)、LEVER (ICML'23)、Table-GPT (SIGMOD'24)、TableGPT2 7B/70B、T5（FeTaQA）；免训练：DATER (SIGIR'23)、TabSQLify (NAACL'24)、ReAcTable (VLDB'24)、Chain-of-Table (ICLR'24)、H-STAR (NAACL'25，另测 GPT-4o-mini 与 Llama-3.1-70B 版)。含 SIGMOD、VLDB 工作。只选有公开代码的方法（"考虑离线 TQA 的性质"）。
- **公平性设计（值得学习）**：两套比较——(1) 与在线方法比时直接引用原论文最好结果（Table II）；(2) 同一离线 vLLM 后端下重跑所有免训练基线（Table III：Qwen3-4B 与 Qwen3-30B 两种规模 × 4 数据集，准确率 + 延迟）。另在 Appendix O 用在线 Qwen3-Max 测试，报告 token 消耗。
- **实验类型**：主结果（Table II、III；Table XV FeTaQA）；效率（Table III 16 线程延迟；Table IV 单线程分解：prediction/execution 时间、I/O token 吞吐、端到端延迟，SPARQ 0.85s vs H-STAR 15.19s）；自适应（Table V 左：按表大小 Small/Med/Large 分层；Table V 右：NIAT 上的 reasoning cliff 曲线）；消融（Table VI：training-free router、w/o Q、w/o 表抽取、w/o SQL、w/o Retrieval；Fig.5：|S| 分布）；泛化（Table VII 3×3 跨数据集）；超参（Fig.6：τ ∈ {0.2..0.99}、采样数 1–5；Fig.7/10：训练集分布 Hard vs 随机 R1–R4、池大小 k、候选数 L、算子集扩展到 Python）；附录：rollback/fallback 触发统计（Table IX）、时间分解（Table XII）、错误案例（Fig.11–12）、表宽度鲁棒性（Table XVIII）。每个实验跑 3 次取均值。
- **成本报告**：主要是**延迟（秒）、LLM 调用次数、token 吞吐、总 token 消耗**（Qwen3-Max 下 SPARQ 3.8M tokens vs ReAcTable 48.0M，≈12×），**不报美元**；"零 API 成本"作为离线部署论点。
- **提升表述**："over 5%" 准确率（WikiTQ/TabFact）、"up to 10.19×" / "average speedup of 10.19×" 端到端延迟（摘要写 up to，正文写 average；贡献列表还出现 12.19×、正文 "up to 17.93×"——数字口径不完全一致，是写作瑕疵）、"fewer than 5% of the parameters"、"over 14%"（Qwen3-4B 上超所有基线）。

## 4. 写作结构 (Writing)
- **标题模式**：`缩写: A Cost-Efficient Framework for <设定> <任务> via <机制>`——"成本"放在标题第一个修饰语。缩写 SPARQ = Sufficient Precise Adaptive Routing for TableQA，把核心概念"sufficient"嵌入名字。
- **摘要逐句功能**：S1 任务定义 + "引起 DB 社区兴趣"（定位社区）→ S2 在线 LLM SOTA 的四个缺点（隐私、延迟、成本、overthinking）→ S3 提出 SPARQ 面向离线部署 → S4 方法两点（扩展算子池 + 自适应路由 + verifier 回滚/兜底）→ S5 结果（>5% 准确率、up to 10.19× 延迟，消费级硬件）→ S6 "first systematic framework" 声明 → S7 代码与 full version。
- **引言逐段功能**：P1 TQA 定义 + 举例 + DB 社区关注 → P2 研究三阶段（supervised / LLM-based / hybrid）→ P3 现有系统偏向在线 LLM，提出 3 个挑战 (a)(b)(c) → P4 朴素做法"直接换小模型"不行 → P5–P6 Example 1 + Fig.1 详细剖析四种策略的失败（long-context collapse、半结构化日期导致 SQL 错、混合方法传播错误）→ P7 三个设问句（零额外成本能否答对？能否超越在线 SOTA？能否自适应加速？）→ P8 Contributions & Organization：6 条编号贡献，每条标注对应章节（Preliminary analysis §III、Framework §IV、Router §V-A、Verifier §V-B、Scheduling §V-C、Experiments §VI）。
- **章节顺序与篇幅**：I Intro（~2 页）→ II Preliminary & Related Work（合并；LLM for TQA、NL2SQL、CoT，~1 页）→ III Motivation & Preliminary Analysis（预实验，~1.5 页）→ IV Framework Design（算子池 + 总览，~1.5 页）→ V Model & Algorithm（router、verifier、调度，~2.5 页）→ VI Experiment（~3.5 页）→ VII Conclusion（1 段）→ 致谢 + AI-generated content 声明 → 附录。Related Work 很靠前且与 Preliminary 合并，篇幅很短。
- **写作技巧**：
  - **把"预实验"做成独立一节（Section III）**：11 种方法、统一离线设置、5 条带数字的发现，最后 "Our findings" 归纳出两个冲突（reasoning-size conflict、complexity-efficiency conflict），直接导出设计需求（router 选最简算子集 + verifier 保证充分性）。这是"empirical study → design"叙事的范本。
  - 贯穿全文的 running example（Example 1–4 都用同一类表/问题，Fig.3 中 q1–q5 展示路由与 rollback/fallback）。
  - 每个组件小节用固定结构：Challenge/Motivation → Mechanism → Design/Training → Remark（与相关工作的区别）。
  - 预先回应审稿人："为什么不用 VPC？"（honest-but-curious 威胁模型 + 中小企业成本）；"是否过拟合难样本？"（随机训练集对照）。
  - 示例短引：作者将结论概括为 offline models benefit from "minimal yet sufficient information"。
  - 瑕疵：加速倍数口径不一致（10.19×/12.19×/17.93×）；正文 Fig.7 与文字引用 "Fig. 10(a)-(c)" 不一致；Table VI 中 SPARQ WikiTQ 77.04 与 Table II 77.03 不一致。说明 ICDE 对此类小瑕疵容忍，但我们应避免。

## 5. 被录取的可能原因 (Why accepted) 与可借鉴点
1. **场景切口新且贴合 DB 关切**：把"离线/本地部署 + 隐私 + 零 API 成本"作为一等目标，而不是又一个追求在线 GPT 精度的方法；"消费级 GPU 上超过 GPT 系方法"是很强的卖点（4B 模型 WikiTQ 77.03 > H-STAR GPT-4o-mini 74.93）。
2. **扎实的 empirical-study-first 叙事**：Section III 的 5 条发现让方法设计显得"必然"，审稿人容易认同。
3. **成本被写进训练信号与优化目标**：reward = acc × 成本惩罚 × 长度惩罚；Eq.1 是"min 成本 s.t. 充分性 ≥ τ"的约束优化形式——把 LLM 任务写成了 DB 风格的 cost-based optimization（类似查询优化器选计划）。
4. **系统层工程完整**：CPU-GPU 调度、动态 batching、full version + 代码 + 数据，满足 artifact 期待；5 个数据集含两个"企业脏数据"基准（TableBench、NIAT）提升实用性说服力。
5. **可借鉴**：双轨公平比较（引用原文结果 + 统一后端重跑）；分层分析（按表大小）；"reasoning cliff"曲线；"router 过度剪枝"的分布图（Fig.5）。
- **潜在弱点（供我们攻击）**：无理论保证（router 次优性、verifier 误判率与最终准确率的关系均未分析）；COST 定义为运行时间但训练用的是离线枚举测得的成本，未考虑负载/硬件变化；算子可并行但未利用；verifier 阈值 τ 全局固定；没有美元/能耗成本模型；多表、多跳、表间 join 场景未覆盖。
