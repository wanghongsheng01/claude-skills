# HEXGEN-FLOW: Optimizing LLM Inference Request Scheduling for Agentic Text-to-SQL (ICDE 2026, Regular)
> **替代说明**：因第 1 篇 CYANSQL 无公开全文（见 `B_cyansql.md`，FULL TEXT READ: no），按任务规则补读一篇 ICDE 2026、有 arXiv 版本的 Text-to-SQL × LLM 论文。选它的理由：它是本组唯一一篇把 **多候选生成 + LLM-as-judge 选择** 的 agentic 流水线当作 **系统负载** 来研究的论文，直接关系到"候选越多、成本/延迟越高"的问题，也是 ICDE 接收"LLM 系统/服务"类论文的样例。
- Source of full text: arXiv 2505.05286v3（2026-03-08，cs.DB，单栏 preprint 排版，非 IEEE 双栏）；IEEE DOI 10.1109/ICDE65706.2026.00134；FULL TEXT READ: yes
- Length: arXiv 版共 21 页（正文约 17 页单栏 + 参考文献约 4 页；折合 IEEE 双栏约 10–11 页正文）；10 张图（Figure 1–10，Fig.4/5/6/7/8/9/10 多为多子图面板）；4 张表（Table 1 符号表、Table 2 分派分布、Table 3 队列快照、Table 4 调参开销）；64 条参考文献；约 10 个编号公式；0 个定理/引理（但给出一个"NP-hard"论断）
- 作者：HKUST（Binhang Yuan 组）+ ETH Zurich + 清华（Chen Wang）

## 1. 科学问题的本质 (Problem essence)
- **表面问题**：CHESS 这类 agentic Text-to-SQL 每个用户问题触发约 20 次相互依赖的 LLM 调用（schema linking → 并行候选生成 → 迭代自纠错 → LLM 生成单元测试并做 judge 选择），在企业的 **异构 GPU 集群**、多租户、不同 SLO 下，用 vLLM/TGI 这类面向独立请求的调度器会造成大量 SLO 违约。
- **本质问题**：**带 DAG 依赖的多阶段 LLM 请求在异构实例上的在线调度**。形式化（§4 Eq.1）：查询流 Q_i ~ P_Q，每个查询含请求 {q_i,1..q_i,n_i} 与端到端 SLO T_i；N 个模型实例，请求在实例 m 上耗时 t^m_i,j（排队 + 计算）；求分派策略 φ 最大化 P(Σ_j t^{φ(q_i,j)}_i,j ≤ T_i)。即"最大化端到端截止期满足概率"的随机调度问题。
- **根因 / gap**（引言中列为 C1–C3）：C1 请求间依赖（早期阶段延迟传导到下游）；C2 异构性（各阶段 prompt/输出长度差异 + GPU 能力差异）；C3 多租户不同 SLO。现有系统（vLLM 的 FCFS + 连续批处理、VTC 的公平性、QLM 的 SLO 分组）都把请求当独立任务。**证据**：Section 2 的定性分析 + Fig.1 流水线依赖图；**没有** 专门的预实验图量化 gap，而是直接以端到端实验对比体现。
- **问题定义形式**：§4 开头 "Problem formulation" 段落 + Eq.1，并声称在未知到达与服务分布下求最优策略 **NP-hard**（引用排队论教材，未给出归约证明），以此为由采用启发式。Table 1 给出完整符号表——这是系统类 ICDE 论文的常见写法。

## 2. 方法的最关键之处 (Key insight)
- **一句话 key idea**：把 agentic Text-to-SQL 视为带截止期的工作流，用"全局按负载与算力均衡分派 + 本地按松弛度（laxity）动态重排"的两级调度，并把每个查询剩余的 SLO 预算按各阶段估计耗时比例实时下发到每个请求。
- **技术组件**：
  1. **Workload-balanced dispatching（全局，解决 C2）**（§4.1）：用输出长度预测器估计计算时间 t^comp = t^prefill(L_in) + t^decode(L̂_out)（Eq.2），排队时间为队列中已有请求的计算时间之和（Eq.3），用非线性分数 Score = (1−α)·β/t^queue − α·t^comp 选实例（Eq.4）；β 每次部署校准一次。
  2. **SLO 预算分配 + 紧迫度优先队列（本地，解决 C1/C3）**（§4.2）：每个请求的预算 = 剩余端到端时间 × 本请求估计耗时 / 剩余所有请求估计耗时之和（Eq.5–6），完成后实时重算（Fig.3 示意"超支 10ms 由下游分摊"）；紧迫度 U = t^comp − (t^SLO − τ)（Eq.7，LLF 风格），在 batch 边界选 U 最大者（Eq.8）。**这是真正的新东西**：把 LLF 从"作业级"细化到"请求级 + 动态重分配"。
  3. **Simulation-guided α-tuning**（§4.3）：滑动窗口监测 P95 尾延迟，用 **单侧两样本 t 检验**（p < 0.01）判断是否显著退化，触发后用 CPU 上的 trace 回放模拟器在 α∈{0,0.1,…,1} 网格上找最优（Eq.9–10）。
- **与"候选选择"的关系**：作者明确声明调度 **不改变 Text-to-SQL 的输出结果**——它不做候选选择，只优化"生成多个候选 + judge 选择"这一流程的服务效率；文中把 test-time scaling（Snell et al.、Large Language Monkeys）列为驱动负载增长的原因。
- **理论保证**：无性能界或近似比；唯一的"统计"成分是用 t 检验触发调参（**本组唯一使用假设检验的论文**，但用于系统监控而非结果正确性）。

## 3. 实验设计 (Experiments)
- **研究问题**（§5 开头 3 问）：端到端性能 vs SOTA 服务系统；各组件贡献；α-tuning 的收益与开销。
- **工作负载**：以 CHESS 流水线 + **Llama-3.1-70B**（vLLM，TP=8）为主；Trace 1/2/3 采样自 **BIRD dev** 的 financial、formula1 库（simple/moderate/challenging = 14%/72%/14%），每查询平均 19.4/20.7/21.1 次 LLM 调用；泊松到达 0.5、1.0 QPS，压力测试 30 QPS，突变负载 5→20→5 QPS；泛化性用 **MAC-SQL + Qwen3-30B** 在 **Spider 1.0** 上采样 Trace 4（9 个库）；Trace 5/6 混入 25%/50% 非 Text-to-SQL 单次请求。
- **硬件**：Hetero-1（A100 + A6000）、Hetero-2（A100 + L40 + A6000）、Homo（全 A100），每实例 4 GPU。
- **基线**（5 个）：vLLM（FCFS + round-robin）、VTC（OSDI'24 公平调度）、QLM（SoCC'24 SLO 队列管理）、LLF（经典最小松弛优先）、Ray Serve（Po2C 路由）；消融变体 RR+PQ、WB+FCFS。**无 DB 会议基线**（这是系统/ML-sys 领域的问题）。
- **指标**：SLO attainment 曲线（SLO scale = 独占执行时间的倍数），关注达到 95% 满足率所需的最小 SLO scale（即 P95 尾延迟）；吞吐量（查询/秒）；多租户的 Jain 公平指数（0.98）。
- **实验类型**：主结果（Fig.4 SLO attainment、Fig.5 吞吐，异构）；同构（Fig.6）；高负载/非平稳/跨工作流/竞争负载（Fig.7 六个子图）；多租户（Fig.8）；消融（Fig.9）；分派分布案例（Table 2：WB 把计算密集的候选生成阶段 57.5% 放到 A100，RR 仅 18.1%）；队列快照案例（Table 3）；α 敏感性（Fig.10，最优 α 在 0.1–0.4 随配置变化）；调参开销（Table 4，每窗口 1.9–3.1 s）。
- **统计**：随机种子 0/1/2 三次运行，图中给误差棒。
- **成本报告**：报告 **延迟（P95）与吞吐**、调参 CPU 时间，以及每查询 LLM 调用次数的均值与方差；**不报 token 数、不报 $**（自托管开源模型，成本以 GPU 时间隐含）。
- **结果呈现**：几乎全部用图（SLO attainment 曲线）；文字用"reduces P95 tail latency by 1.42∼1.56× and increases throughput by 1.49∼1.81×"的区间倍数表述，并对每个基线逐条给出"X% ∼ Y%"区间及一个具体例子（"vLLM 需 5.4 倍 SLO scale，我们只需 3.5"）。

## 4. 写作结构 (Writing)
- **标题模式**："<系统名>: Optimizing <系统层问题> for <应用负载>"——系统名沿用该组 HexGen 系列品牌（HexGen、HexGen-2），把 Text-to-SQL 当作"应用场景"。
- **摘要逐句功能**：S1 背景（agentic LLM 提升 Text-to-SQL）→ S2 部署挑战（多阶段依赖、严格延迟、异构 GPU）→ S3 现有服务框架不适配 → S4 方案（HEXGEN-FLOW）→ S5 核心设计（两级调度）→ S6 次要设计（模拟调参）→ S7–S8 结果（"1.42∼1.56×"、"1.49∼1.81×"）。
- **引言逐段功能**：P1 Text-to-SQL 价值；P2 agentic 四阶段流水线 + Fig.1，强调 SQL 执行毫秒级、端到端延迟由 LLM 推理主导（为"这是 LLM 服务问题"铺垫）；P3 企业用异构 GPU（脚注列 NVIDIA 架构代际）；P4 三个挑战 C1–C3（编号列表）；P5 现有系统为何不够；P6 方案概述，**每个设计点用 "To tackle C1/C2/C3" 一一对应**；贡献列表 **3 条**（设计原则 / 框架 / 评估）。
- **章节顺序与篇幅（arXiv 单栏页数）**：1 Intro（~2.5 页）→ 2 Preliminaries（流水线 + 现有调度，~1.5 页）→ 3 HEXGEN-FLOW（需求 / 概览 / 实现，~2 页）→ 4 Scheduling Algorithm（形式化 + 三组件，~3.5 页）→ 5 Evaluation（~6.5 页）→ 6 Related Work（**放在实验之后**，~1 页，分 "LLM Advances for Text-to-SQL" 与 "LLM Inference Request Scheduling" 两类）→ 7 Conclusion。
- **写作技巧**：
  - **挑战–需求–组件三重对应**：C1–C3（§1）→ 三条系统需求（§3.1）→ 三个调度组件（§4），每一层都用同一编号/顺序，审稿人可一一核对。
  - Table 1 符号表 + Fig.3 数值小例子（40ms 预算超支 10ms 的再分配），让公式直观。
  - 基线对比逐条写成项目符号，每条"区间 + 具体例子 + 失败原因"三段式，非常利于审稿人快速确认优势来源。
  - 以 Text-to-SQL 为"杀手级应用"包装通用的 LLM 工作流调度问题，使系统论文契合 ICDE 的数据管理主题。

## 5. 被录取的可能原因 (Why accepted) 与可借鉴点
1. **抓住 LLM-for-data 的"系统侧"空白**：大家都在提准确率，它研究 agentic Text-to-SQL 的服务效率，问题新且工业相关（异构 GPU、多租户、SLO）。
2. **形式化 + 启发式 + 系统实现** 的完整链条，并给出 NP-hard 论断为启发式辩护——ICDE 系统论文的标准套路。
3. **实验矩阵大**：3 种硬件 × 6 条 trace × 多负载 × 5 基线 + 消融 + 案例 + 开销，且有误差棒。
4. 可借鉴的缺口：(a) 把候选数、修正轮数视为 **外生固定**，没有与"选择算法"联合优化——例如自适应决定生成多少候选、何时提前停止（early stopping）以同时满足 SLO 与准确率；(b) 只用单一开源模型（Llama-3.1-70B / Qwen3-30B），不涉及 **多 vendor API 混合**（商用 API 的速率限制、价格差异）；(c) 不报 token/$ 成本；(d) 准确率–延迟的 trade-off 完全未讨论。这些正好是"成本感知的多 LLM 候选生成与选择"类论文可以切入的点。
