# Distance Comparison Operations Are Not Silver Bullets in Vector Similarity Search: A Benchmark Study on Their Merits and Limits (ICDE 2026, EAB)
- Source of full text: arXiv 2604.02801v1（2026-04-03，"full paper" 版本，含附录 A–H）；benchmark 代码与数据 github.com/zzlin237/dco-benchmark。FULL TEXT READ: yes（正文 12 页 + 参考文献 + 附录全部读完；附录图表的数值只能从文字读到，图本身文字提取不可读）
- Length: 正文 12 页（IEEE 双栏）+ 1 页 AI 使用声明与参考文献 + 附录约 9 页（arXiv 共 23 页）；正文 Fig.1–14（14 个 figure，其中多个为 12 子图的 QPS-recall 网格），附录另有 Fig.15–30 左右；4 个 table（Table I 先前工作评测设置对比、Table II 符号、Table III 方法对比含复杂度、Table IV 数据集）；54 篇参考文献；3 个 algorithm（三类方法的通用框架）；约 8 个公式；0 个定理（Definition 1–3）
- 作者：北航 Yongxin Tong / Yuxiang Zeng 组。有趣的是：被测方法中 DDC_res/DDC_pca/DDC_opq 即论文 2（ICDE 2025）

## 1. 科学问题的本质 (Problem essence)
- **表面问题**：最近的 DCO 算法（ADSampling SIGMOD'23、DADE PVLDB'24、DDC_* ICDE'25）声称比全维扫描快 2–4×，它们是否"production-ready"？
- **本质问题**：一个**外部有效性 (external validity)** 问题——已有结论是在狭窄评测条件下得出的，换到真实部署条件（维度范围、硬件 SIMD/GPU、查询分布、非查询负载）后结论是否还成立？可形式化为：在因素空间 {维度 D ∈ [96, 12288]} × {硬件: CPU±SIMD, GPU} × {查询: ID/OOD} × {metric: L2/IP/cos} × {负载: query/index build/insert} × {索引: HNSW/IVF} 上，比较 8 个 DCO 方法相对 FDScanning 的 QPS@recall 排名是否稳定。
- **为什么现有评测不够（4 个根因，正是 Table I 的 4 列）**：
  1. Narrow dimensionality coverage（只测 128–960 维，忽略低维和 LLM 超高维）；
  2. Insufficient direct comparison（SOTA 之间互不对比，[2][3][4] 都只对比 [1]）；
  3. Restricted hardware（多数关闭 SIMD）；
  4. Limited scenario（只看 in-distribution query，忽略 OOD、建索引、更新）。
  证据形式：**Table I 是全文的 "Figure 1"**——把 4 篇先前工作的数据集数、维度范围、规模、对比算法、硬件、场景、metric、OOD 列成表，并把 "Ours" 放最后一行，一眼可见覆盖面差异。这是 EAB 论文最有效的 gap 呈现方式。
- **问题定义形式**：Definition 1（向量）、Definition 2（KNN）、Definition 3（DCO，引自 [1]：判定 dis(o,q) ≤ τ，真则返回精确距离）；外加按维度对数据集分类（低维 [10,100]、高维 (100,1000]、超高维 ≥10³），这个分类成为后续所有 findings 的组织轴。无复杂度 hardness 结论，但 Table III 给出各方法 offline/online 预处理与在线计算复杂度——并指出 ADSampling 低估了查询投影的 O(D²) 在线预处理成本，这是一个"分析性"贡献，后来被实验证实（超高维下成为瓶颈）。

## 2. 方法的最关键之处 (Key insight)
- **一句话 key idea**：把 DCO 从"算法创新"重新放回"系统部署"语境——统一框架从零重实现 8 个方法、在 SIMD/GPU 下测、扩到超高维与 OOD 与建索引/插入，从而揭示**成本模型的隐藏项**（判定逻辑开销、O(D²) 查询旋转、训练数据依赖）决定了 DCO 是否有收益。
- **技术组件（EAB 的"方法"即评测设计）**：
  1. **Taxonomy**（Fig.2/3 + Alg.1–3）：simple scanning（FDScanning、PDScanning、PDScanning+）/ hypothesis testing（ADSampling、DADE、DDC_res；又细分 residual-distance estimator vs cross-term estimator）/ classification（DDC_pca、DDC_opq）。为每类写出统一伪代码框架——这既是 survey 功能，也让实现可比。
  2. **"被忽略的基线" PDScanning+**（PCA 旋转 + 部分扫描，来自 Data Eng. Bull. 综述）被提升为独立基线，结果在 GPU/超高维常与 SOTA 打平——"强简单基线"是 EAB 新意的常见来源。
  3. **统一实现与公平性控制**：同一索引数据布局，DCO 不得改布局；在线部分统一 C++，Python 只用于 PCA/训练；SIMD 用 hnswlib 例程；GPU 上每个 IVF 分区一个 kernel、每线程一个候选；参数用原论文推荐值，再在附录 H 单独做 Δ0/Δd 参数研究。
  4. **新数据集 XUltra**（12,288 维，用 MSMARCO token embedding 拼接合成，模拟 davinci-001 维度）——用于压力测试超高维。
- **理论保证**：无。替代物是 Table III 的复杂度拆解（offline pre-processing / online pre-processing / online computation 三栏），把"为什么超高维会慢"从实验现象提前到分析层面。

## 3. 实验设计 (Experiments)
- **研究问题（Sec.V-A..F，每节一个 Takeaway）**：
  - A Query processing（含 pruning ratio 分析）→ Takeaway #1 DCO is no silver bullet；
  - B OOD queries → #2；
  - C Beyond Euclidean（IP，cos 在附录）→ #3；
  - D Index construction → #4；
  - E Dynamic data（顺序插入 + 有限初始数据）→ #5；
  - F Diversified hardware（CPU±SIMD、GPU）→ #6；
  - G Summary：Fig.14 推荐决策图 + Merits(4) + Limitations(4)。
- **数据集**：10 个（Table IV）——Deep 96d/100M、GloVe 100d/400K、SIFT 128d/1M、Text2Image 200d/10M、Laion 512d/1M、Wikipedia 768d/1M、GIST 960d/1M、OpenAI 1536d/2.3M、Trevi 4096d/99.9K、XUltra 12288d/100K（合成）。覆盖低/高/超高维三档 + 两个天然 OOD 多模态集（文本查询 vs 图像数据）。
- **被测方法**：8 个——3 个工业常用基线 + 5 个 SOTA（SIGMOD'23、PVLDB'24、ICDE'25×3）。**选择逻辑**：覆盖 taxonomy 的每一类且包含所有已发表 DCO 工作；明确排除硬件专用方法（GPU/SIMD 只作为环境维度而非被测方法）；FINGER 只在相关工作出现。
- **指标**：recall、QPS、dimension pruning ratio、index construction time、insertion time。
- **环境**：AMD Ryzen 9 5950X、128GB RAM、RTX 3090、CUDA 12.4、Ubuntu 24.04；默认开 SSE SIMD、单线程；HNSW M=16/efC=500，IVF 4096 分区；efSearch 100–1500、nprobe 20–400；k=20/100。
- **结果呈现**：几乎全部是 QPS-recall 曲线网格（Fig.4 12 子图、Fig.13 3×4 硬件网格），柱状图用于建索引时间；结论用 "up to X×" 和区间表述，正负两面都量化：SOTA 最多提升 1.4–1.9×（假设检验类）/1.6–2.1×（分类类）；但低维最多慢 20%–42%，超高维 XUltra 最多慢 77%–79%；OOD 下 DDC_pca 从快 1.5× 变为慢 1.6×；SIMD 使 IVF 上加速比从 2.0–4.4× 缩到 1.2–3.8×，HNSW 上从 1.9–3.1× 缩到 1.1–2.1×；建索引加速最多 64%、插入最多 63%（DDC_res 达 39%）；GPU 上相对 FDScanning 最多 4.7–7.6×。一个关键统计："14 个子图中只有 4 个" SOTA 稳定优于 FDScanning。

## 4. 写作结构 (Writing)
- **标题模式**：结论式标题 "X Are Not Silver Bullets in Y: A Benchmark Study on Their Merits and Limits"——标题直接给出否定性结论 + 双面（merits & limits），非常适合 EAB。
- **摘要逐句功能**：S1 定义 DCO 及其为瓶颈 → S2 新方法承诺加速但"readiness for production"未知（研究问题）→ S3 规模（8 算法、10 数据集、最高 100M/12,288 维、CPU±SIMD 和 GPU）→ S4 负面发现三条（维度敏感、OOD 退化、硬件不稳）→ S5 正面发现（加速建索引与更新）→ S6 总结论（尚不适合生产部署）。
- **引言逐段功能**：P1 向量检索背景 + 研究从索引转向算子级 → P2 DCO 定义 + SOTA 宣称 2–4× → P3 以加粗问句提出核心研究问题 + 分析先前评测协议的 4 个局限（bullet）→ P4 "我们做了全面 benchmark" + **4 条 findings（编号加粗：Dimensionality Sensitivity / Robustness Dilemma / Benefit Beyond Query / No Universal Winner）** → Contributions 3 条（首个全面 benchmark；merits & limits 分析及最终答案；实践指南 + 开源）→ Road Map。引言就把 findings 和数字全部亮出——EAB 惯例。
- **章节顺序与篇幅**：I Intro（~1.3 页，含 Table I）→ II Preliminary（~1 页）→ III Existing DCO Methods（taxonomy + 3 框架 + Table III 对比，~2.3 页）→ IV Benchmark Setup（~1.2 页）→ V Experimental Evaluation（~5 页，A–G）→ VI Related Work（~0.5 页，两类：向量检索 / 向量距离操作）→ VII Conclusion & Future Direction（4 条研究方向）。Related Work 放在末尾。
- **好的写作技巧**：
  - 每个实验小节以 **"Takeaway #n:"** 加粗框收尾，结论一句话可被引用；Summary 节再做 Merits/Limitations 对称清单 + Fig.14 决策树式推荐图。
  - 每个负面结论都给出**机制解释**而非只报现象（如低维下"省下 6%–36% 维度的时间被判定与分支开销吞掉"；超高维下 O(D²) 旋转无法在 HNSW 的 O(log N) 次 DCO 中摊销；IVF 候选远离查询所以 pruning 随 nprobe 上升）。
  - 自己设计了一个 Fig.1 toy example（τ=11，扫描 6 维即可判定）帮助非专家理解 DCO。
  - 有 "AI-Generated Content Acknowledgement"（DeepSeek-R1 仅用于语法润色）——ICDE 2026 新要求的写法示例。

## 5. 被录取的可能原因 (Why accepted) 与可借鉴点
1. **"fundamentally new" insight 来自否定已有共识**：先前 4 篇论文都报告 DCO 有 2–4× 加速；本文证明在默认开 SIMD 的真实条件下，大部分场景收益缩小甚至变负，并且排名会翻转（DDC_opq 在 SIFT 上从最差变最好）。这是 EAB 最被认可的新意类型：**揭示先前评测协议的系统性偏差**。
2. **gap 可视化做得极好**：Table I 一张表让审稿人立刻相信"之前没人这样测过"。
3. **双面结论**：不只是"打假"，还找到被忽视的优点（建索引/插入加速），并给出可操作的选择指南（Fig.14）与 4 条未来方向，避免成为纯负面论文。
4. **可复现性**：从零统一重实现 + 开源代码与数据 + 附录详细实现细节（数据布局、语言、kernel 组织）+ 参数研究说明默认参数的影响。
5. **可借鉴点**：做 EAB 时 (a) 先把先前工作的评测协议列成表找"系统性盲区"；(b) 引入被忽视的强简单基线；(c) 加入一个现实但被忽视的维度（硬件、OOD、超高维、更新）；(d) Takeaway 框 + 推荐决策图。不足：未做多线程/批量并行查询、未覆盖磁盘索引与量化索引（RaBitQ 等）的交互——这些是后续可攻的 gap。
