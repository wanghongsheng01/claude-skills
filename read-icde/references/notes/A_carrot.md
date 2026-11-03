# CARROT: A Learned Cost-Constrained Retrieval Optimization System for RAG (ICDE 2026, Regular research paper)
- Source of full text: arXiv 2411.00744v2 (2026-03-12 修订版, 作者注明 "Accepted to ICDE 2026"; v1 原题为 "CORAG: A Cost-Constrained Retrieval Optimization System for Retrieval-Augmented Generation")。作者: Ziting Wang, Haitao Yuan, Wei Dong, Gao Cong (NTU), Feifei Li (Alibaba)。代码 https://github.com/wang0702/CARROT ；另有 Technical Report [40] 放在 GitHub（NP-hard 证明、非可加性实验、基线细节都放在 TR 里）。FULL TEXT READ: yes（arXiv v2 全文 14 页，含参考文献；PDF 存于 pdfs/A/CARROT_2411.00744v2.pdf）
- Length: 正文约 12.5 页 + 参考文献约 1.5 页（共 14 页，IEEE 双栏）；12 个 figures（Fig.1–12）；6 个 tables（Table I–VI）；68 篇 references；编号公式 2 个（Eq.1 目标函数、Eq.2 cost-aware UCB），另有若干行内损失函数；1 个 Theorem（NP-hard，证明放 TR）；伪代码 1 个 Algorithm + 4 个 Function + "Algorithm 6"（编号跳号，说明 Function 也计入了算法计数）。

## 1. 科学问题的本质 (Problem essence)
- **表面问题**：RAG 中"检索哪些 chunk 放进 prompt"。
- **本质问题**：一个**带预算约束的有序子集选择（ordered subset selection / knapsack-with-order）问题**，且目标函数不可加、非单调。
  - 输入：query Q；向量库召回的候选 chunk 集合 {χ1..χk}；token 预算 B；chunk 成本 cost(χ)=|χ|（token 数）。
  - 输出：有序 chunk 序列 Φ = ⟨χφ1,…,χφm⟩（既选子集又定顺序）。
  - 约束：Σ cost(χi) ≤ B。
  - 目标：max W(Φ)，W 由 reranker 对"整个组合"打分（W(Φ) ≠ ΣW(χi)，即非可加），作为最终回答质量的代理（proxy）。
  - 关键建模动作：把"LLM 回答质量"用一个便宜的 reranker 分数代替，从而把问题变成可在线搜索的组合优化问题；并在 Fig.8 用 Pearson r=0.83 验证 reranker 分与 ROUGE-L 的相关性来支撑这个代理。
- **为什么现有方法不够（3 个 Challenge = gap）**：
  1. Chunk 间关系（冗余、顺序）被忽略：AKNN top-k 独立打分、聚类整簇返回 → 冗余；"lost in the middle" 说明顺序重要。证据：Fig.1 Eiffel Tower 例子（AKNN 选 χ3+χ1 只覆盖历史；聚类返回全部 4 个造成冗余；最优是 χ3+χ4，且 χ4 在前更好）。
  2. 效用非单调：现有方法默认"chunk 越多越好"，把预算耗尽当终止条件。证据：Fig.1 中在 χ3+χ4 后加 χ1 反而降分；Table V 中基线随预算增大不单调提升。
  3. 查询多样性：单一 reranker 不能通吃。证据：Fig.5 预实验，不同领域（Academic/Commerce/Literature/Healthcare/Legal/Others）最优 reranker 分布不同。
  - 另外在 P2–P3 先把 RAG 分成 tuning-based / graph-based / rank-based 三类，用"计算成本"排除前两类，再用 Table II 的经验观察指出 rank-based 在难查询和长上下文上表现差，从而引出三个 Challenge。
- **问题定义形式**：Definition 1 (Chunk)、Definition 2 (Optimal Chunk Combination Order Selection，Eq.1 argmax s.t. 预算)；Theorem 1：该问题 NP-hard，由 Maximum Weighted Hyperclique Problem (MWHP) 多项式归约，证明在 TR。引言中的 "Problem Statement" 是一个设问句（能否同时高效、有效且成本可接受），而非形式化定义——形式化定义放在 Section II Preliminaries。

## 2. 方法的最关键之处 (Key insight)
- **一句话 key idea**：把"选哪些 chunk、按什么顺序"建成一棵 policy tree（每个节点=一个有序组合），用带成本惩罚项的 UCB-MCTS 在预算内搜索全深度节点，用 batched reranker 并行打分；再用一个对比学习的 configuration agent 按 query+数据预测 reranker 与 MCTS 超参。
- **技术组件**：
  1. **Policy tree + MCTS 搜索（解决 Challenge 1、2）**：根=空集，子节点=父序列追加一个 chunk。与标准 MCTS 的四点差异是论文强调的"新东西"：(a) Cost-aware utility U(v)=V/N + c·sqrt(ln N_parent/N) − λ·cost(Φv)/B（Eq.2，把预算写进选择函数，而不仅仅是终止条件）；(b) Expansion 一次展开所有可行子节点；(c) Simulation 不做随机 rollout，而是一次 batched reranker 调用给所有子节点打分（O(r) 而非 O(k·r)）；(d) 最终从所有深度（不只是叶子）中选 W 最大且满足预算的节点——这一点直接对应"非单调"：短组合可能优于长组合。
  2. **Configuration Agent（解决 Challenge 3）**：输入 BGE-M3 的 query embedding ⊕ 召回 chunk 的 mean-pooled embedding（2048 维），Siamese 网络 512→256→128，输出：分类头（6 个 reranker 中选一个）+ 回归头（iteration、c、λ）。训练：对比损失 + CE + MSE 联合；标签来自 1K seed query × 6 reranker × 20 组参数的 grid search（ROUGE-L 选优），约 10,000 对训练对，Llama3-8B 本地生成。论文论证了为什么不直接学习预测组合顺序（N! 空间、非可加难拟合、结构化输出），只预测超参是"轻量回归"——这是一个很好的设计取舍论证。
  3. **Parallel expansion**：工程优化，消融显示延迟 16.1s→3.1s。
  - 真正的新东西：问题建模（有序+预算+非可加）+ cost-aware MCTS 的改造；configuration agent 是"learned component 做 knob tuning"的典型 DB 套路（类比 learned query optimizer，引用了 Lero）。
- **理论保证**：仅有 NP-hard 结论（证明在 TR）+ 时间复杂度 O(I·(D_B·N + r))、空间 O(I·N)，D_B=min{N,⌊B/s⌋}；agent 训练/推理复杂度分析。**没有近似比或收敛保证**。

## 3. 实验设计 (Experiments)
- **RQ 列表（5 个）**：RQ1 有效性（(1) 跨数据集与 chunk size；(2) 跨 LLM）；RQ2 效率；RQ3 可扩展性；RQ4 不同预算；RQ5 消融（组件 + 设计选择 + 泛化）。另有 case study。
- **数据集（3 个）**：WikiPassageQA（4,165 问题，244,136 passages）、MS MARCO（8.8M passages）、HotpotQA（多跳，5M+ passages）。前两个单跳，最后一个多跳。Table I 给出 train/dev/test 与 #p 统计。
- **基线（9 个 + 2 个自变体）**：rank-based：RAPTOR (ICLR'24)、NaiveRAG、HYDE (ACL'23)、FLARE (EMNLP'23)；graph-based：GraphRAG (2024)、Graph-CoT (ACL'24)、G-Retriever (NeurIPS'24)、HippoRAG2；tuning-based：ColBERT（论证 RankRAG/Self-RAG 需 128/4 张 A100 不可行，只选 ColBERT 代表）。自变体：CARROT w/o Agent、CARROT_upper（top-5 候选内穷举，作为上界）。基线中无 ICDE/VLDB/SIGMOD 方法（相关工作中引用了大量 PVLDB 的 LLM-for-data 工作作为背景）。
- **LLM**：默认 Llama3-8B；跨 LLM 用 DeepSeek-V3、GPT-4o（通过 OpenRouter）。
- **指标**：单跳 ROUGE-1、ROUGE-L、BLEU-1；多跳 F1；效率=检索延迟（s）；成本=每查询在线 token 数（"On." 列）+ 离线索引时间与 token（Table IV）。**成本用 token 报告，不报美元**。
- **实验类型**：主结果（Table II：3 数据集 × 3 chunk size {256,512,1024}，附在线 token 列）；跨 LLM（Table III）；效率（Fig.6a 延迟柱状图，Fig.6b 质量-时间 trade-off 散点）；成本分解（Table IV：离线索引 vs 在线，GraphRAG 离线需 2.3M tokens/55,003s，CARROT 仅 66.9s）；可扩展性（Fig.7：10K→100K chunks，延迟仅升约 10%）；预算敏感性（Table V：B=1024/2048/8192）；消融（Table VI：Top-k+JinaV2、Agent-Only、Beam Search、Bandit、MLP、w/o 各预测量、w/o Parallel Expansion，以及延迟分解脚注：Simulation 占 48.4%，Tree Ops 9.7%）；设计验证（Fig.8 reranker-质量相关 r=0.83；Fig.9 候选数影响；Fig.10 顺序敏感性：比 score-desc 高 11–15%）；泛化（Fig.11：6×6 领域矩阵 + 3×3 跨数据集矩阵）；case study（Fig.12）；一次性成本 Remark（数据收集 1.8h + 训练 7min）。
- **结果呈现**：效果/成本用大表（加粗最优、下划线次优），效率/可扩展性/敏感性用图。提升表述："up to 30% improvement"（摘要/结论），"about 30% relative gain"，"32.1% gain over Top-k+JinaV2"，"80.7% reduction" latency。
- 值得注意的公平性处理：只有支持 token 预算的方法（RAPTOR/NaiveRAG/HYDE）固定 1024 预算，其他方法不限预算并单列 token 消耗；对 NaiveRAG/HYDE 改造为"超预算即停止加 chunk"。

## 4. 写作结构 (Writing)
- **标题模式**：`缩写: A Learned <约束>-Constrained <任务> Optimization System for <领域>`——"系统 + 约束 + 优化"三个 DB 关键词齐全。
- **摘要逐句功能**：S1 背景（LLM 难处理最新知识）→ S2 RAG 是解法 → S3 因上下文窗口与长上下文幻觉只能取最相关 chunk → S4 三个挑战并列（关系、非单调、查询多样性）→ S5 "我们设计 cost-constrained 框架" → S6 MCTS 解决顺序/相关性 → S7 不以预算耗尽为终止、解决非单调 → S8 configuration agent 解决适配 → S9 结果 "up to 30%" + 代码链接。三挑战与三技术一一对应，结构非常对称。
- **引言逐段功能**：P1 背景：RAG 重要性 + 顺带回应"Agentic RAG 是否让标准 RAG 过时"（预先防御审稿人质疑）；P2 tuning-based 与 graph-based 方法计算代价高；P3 rank-based 方法高效但在难查询/长上下文下表现差（引 Table II），引出三个挑战；P4–P6 Challenge 1/2/3 各一段，各配 Fig.1 或 Fig.5 证据，并在 Challenge 1 中预告 "NP-hard in Section II"；P7 Problem Statement（设问句）；P8 Our contributions 总述；随后 4 条 bullet 贡献（三个技术各对应一个 Challenge + 一个实验）。Figure 1 是 motivating example（同时展示组合、顺序和 token 成本），Figure 2 是架构总览。
- **章节顺序与篇幅**：I Intro（~2.3 页）→ II Preliminaries（问题定义 + NP-hard，~0.7 页）→ III Related Work（RAG、Reranking、RL for LLM 三类，~0.8 页，放在问题定义之后、系统之前）→ IV System Overview（~0.8 页）→ V Chunk Combination Search（~2.5 页，含 Algorithm 1 + Function 1–4 + 复杂度）→ VI Configuration Agent（~1.5 页）→ VII Experiment（~4 页）→ VIII Conclusion + 致谢 + AI-generated content acknowledgment（ICDE 2026 新要求的声明段）。
- **写作技巧**：
  - "Challenge k → 技术 k → 实验验证 k" 的严格三元对齐，contribution bullet 末尾显式写 "addressing Challenge k"。
  - 在方法节开头用 "Motivation" 段说明穷举规模（n=10 时超 900 万有序组合）和贪心失败的反例，再提出 MCTS。
  - 与标准 MCTS 逐条对比（"Unlike standard MCTS …"），把"组合已有技术"写成"有针对性的改造"。
  - 把繁重证明和细节外放到 GitHub Technical Report，正文保持可读——这是 ICDE 页数受限下的常见做法。
  - 示例短引：作者称 MCTS 让低分节点"can still be discovered if they lead to superior combinations"。

## 5. 被录取的可能原因 (Why accepted) 与可借鉴点
1. **把 LLM 应用问题还原成经典 DB 风格的组合优化**：有形式化定义、预算约束、NP-hard 证明、复杂度分析——审稿人熟悉的"问题-难度-算法"叙事。
2. **成本是一等公民**：token 预算写进目标（Eq.2 的 λ·cost/B 项），并用 Table IV 单独拆分离线索引与在线 token 成本，正面击中 graph-based RAG 的离线成本痛点（GraphRAG 2.3M tokens）。
3. **实验面广且直接对应论点**：每个 Challenge 都有专门实验（顺序敏感性 Fig.10、预算非单调 Table V、领域差异 Fig.5/Fig.11），并提供上界变体 CARROT_upper 与多种搜索策略消融（Beam/Bandit/Agent-Only），回答"为什么一定要 MCTS"。
4. **代理目标被验证**：用 reranker-质量相关性（r=0.83）为"用 reranker 分代替 LLM 质量"辩护，堵住最大漏洞。
5. **可借鉴**：(a) 用一个小例子同时展示所有 gap 的 Figure 1；(b) 自建 upper-bound 变体；(c) 延迟分解脚注；(d) 一次性训练成本 Remark 预先回应"训练开销"质疑。
- **潜在弱点（供我们攻击）**：只有 NP-hard，无近似保证；reranker 作为 benefit 是代理，最终 LLM 质量与代理之间的 gap 未被建模；固定 chunk size 假设；评测指标仍是 ROUGE/BLEU 等词面指标；没有报告美元成本；"30%" 主要相对 rank-based 基线。
