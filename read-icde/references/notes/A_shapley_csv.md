# Tailoring the Shapley Value for In-context Example Selection towards Data Wrangling (ICDE 2025, Regular research paper；方法名 CSV / MCSV / ACSV / BCSV)
- Source of full text: 无 arXiv 版本。全文来自合作作者 Jianzhong Qi（墨尔本大学）个人主页托管的 PDF：https://jianzhongqi.github.io/assets/pdf/ICDE2025_CSV.pdf（IEEE 双栏，14 页，与 IEEE proceedings pp. 2281–2294 的 14 页一致，判断为 camera-ready 或其极近版本）。IEEE DOI 10.1109/ICDE65448.2025.00173。作者：Zheng Liang, Hongzhi Wang*, Xiaoou Ding, Zhiyu Liang, Chen Liang, Yafeng Tang（哈工大）, Jianzhong Qi（墨尔本）。证明与 prompt 细节放在 GitHub Technical Report [21]（github.com/Lorenzo0224/csv）。FULL TEXT READ: yes（PDF 存于 pdfs/A/CSV_Shapley_ICDE2025_jianzhongqi.pdf）。
- Length: 正文约 12.3 页 + 参考文献约 1.7 页；Figures 5 个（Fig.1 EM 示例、Fig.2 三种算法示意、Fig.3 critical difference 图、Fig.4 预算-F1 曲线、Fig.5 k 的影响）；Tables 5 个（Table I prompt 示例、II 数据集、III 主结果、IV 时间与 token 成本、V 跨 LLM）；references 71 篇；编号公式 16 个；7 个 Proposition（唯一性、MC 误差界、AC 等价、无偏性、偏差最小化误差界、遗憾最小化误差概率、BCSV 误差概率），证明全部放在 TR；6 个 Definition（6 种 DW 任务）+ Definition 7（CSV）+ Definition 8（Activated Contribution）；Problem 1（LESD）+ Problem 2（Top-k CSV selection）；3 个 Algorithm（MCSV、ACSV、BCSV）。

## 1. 科学问题的本质 (Problem essence)
- **表面问题**：LLM 做数据整理（entity matching、schema mapping、error detection、missing value imputation 等）时，few-shot prompt 里放哪几个示例。
- **本质问题**：**预算约束下的基数受限子集选择（cardinality-constrained subset selection with a costly black-box utility）**，并进一步转化为**基于博弈论贡献度的 top-k 识别问题**。
  - Problem 1 (LESD)：输入候选示例集合 D（n 个）、LLM API 预算 B、示例数上限 k；输出 D* = argmax_{D'⊂D, |D'|≤k} U(D')；U 为在验证集 V（m 条）上的 F1/准确率；每次计算 U 需要 m 次 LLM 调用，所有 U 调用的总成本 ≤ B。暴力枚举 O(m·n^k) 次提问。
  - Problem 2 (Top-k CSV selection)：选 CSV 最大的 k 个示例，s.t. |D*|=k，Σ cost(U') ≤ B（Eq.4）。作者明确承认：由于 LLM 的 U 非凹（非超可加博弈），Problem 2 只是 Problem 1 的近似，二者之间的解质量关系"留作未来工作"——这是一个公开的理论缺口。
- **为什么现有方法不够（gap）**：
  1. RAG（相似度检索）与 topic-model 方法只看相关性，不看示例对 LLM 效果的真实影响；
  2. Influence-based 方法（CondAcc 等）看影响但代价高、不稳定，且只满足 Shapley 公理中的 zero element 性质，贡献估计可能误导；
  3. 直接用 Shapley value：精确计算 #P-hard；传统近似会选出几百个示例，超出 prompt 容量/预算；SOTA (ε,δ)-近似需 O(mn log n) 次 LLM 调用。
  - 证据：Example 1 用 Beer 数据集算账——训练/验证/测试各 150 对、每次最多 8 个示例，influence-based 穷举需 150·Σ C(150,i) 次提问，相当于 **超过 17 万年**（每次 1 秒）或 **2.2 亿美元**（按 ChatGPT 价格）。这是一种"用美元和年数量化不可行性"的很有冲击力的写法。没有专门的预实验图。
- **问题定义形式**：标准的 Problem 1 / Problem 2 环境 + Definition；复杂度结论是引用的（SV #P-hard [18]），本文自身没有新的难度证明。

## 2. 方法的最关键之处 (Key insight)
- **一句话 key idea**：既然 prompt 最多放 k 个示例，就只需要在"大小 < k 的联盟"上算 Shapley 值（Constrained Shapley Value），这既让贡献度与真实使用场景一致，又把近似代价从 O(mn log n) 降到 O(mk log n)；再通过"activated contribution"让一次 LLM 评估 U(S) 被所有 n 个候选示例共享。
- **技术组件**：
  1. **CSV 定义（Eq.3）+ Proposition 1 唯一性**：在只接受 ≤k 规模联盟的博弈中，CSV 是唯一同时满足 Symmetry、Additivity、Balance、Zero element 的价值函数；以此论证优于 influence-based 方法。→ 解决 gap 1、2（理论动机）。
  2. **MCSV（Algorithm 1）**：把经典 permutation-based marginal contribution 采样改为只取长度 k 的排列，并复用 U0 节省一次评估；Proposition 2 给出 Hoeffding 型 (ε,δ) 样本复杂度（含 token 成本表达式 m·r²·avl(D)·k²/(4ε²)·log(2n/δ)）。→ 工程化适配。
  3. **ACSV（Algorithm 2，核心新意）**：定义 AC(S,di)=U(S)·f(S,di)，f 取 0 / −1 / n/|S|−1 三种"激活"权重（Eq.6–7），CSV 等于 AC 的加权平均（Prop.3），均匀采样下无偏（Prop.4）。两种分层采样分配：(a) 偏差最小化——把 token 预算约束写进优化（Eq.10–11），用 Lagrange 乘子得到闭式分配 m_j ∝ B·∛(1/j)/(avl(D)·Σ(j'+1)∛(1/j'))（Eq.12），Prop.5 给误差界；(b) 遗憾最小化——把 top-k 识别建模成 multiple arm identification，改造 SAR 算法（Eq.13），Prop.6 给错误概率界。→ 解决 gap 3（成本）。
  4. **BCSV（Algorithm 3）**：批处理场景，一次 prompt 处理 β 条测试记录；先用 RoBERTa embedding 做 kNN 取 top-K 候选（沿用 BatchER），再用 ACSV 精选 top-k；并用 meta-feature（数据集统计向量的余弦相似度 × 示例 embedding 距离）把历史批次的 CSV 加权迁移到新批次（Eq.14），Prop.7 给错误概率界。→ 扩展到大数据集。
  - 真正的新东西：CSV 的约束化定义 + activated contribution 估计器 + 带 token 预算的样本分配闭式解；MCSV 和 BCSV 的 meta-learning 部分更多是适配与组合。
- **理论保证**：本组 5 篇中理论最"重"的一篇——唯一性、无偏性、(ε,δ) 样本复杂度、错误概率界都有（但证明全在 TR）。缺失：CSV 的 top-k 与真正最优 k 子集（Problem 1）之间的差距。另外作者自己说明示例顺序采用"CSV 升序"启发式，最优顺序是开放问题。

## 3. 实验设计 (Experiments)
- **实验组织**：没有显式 RQ；分为 B 端到端性能（vs LLM-based、vs Task SOTA、critical difference 图）、C 成本与收敛、D 消融与参数（LLM、k、预算）。
- **数据集（14 个，6 类任务）**：EM 7 个（Magellan：Fodors-Zagats、iTunes-Amazon、Beer、DBLP-ACM、DBLP-GoogleScholar、Amazon-Google、Walmart-Amazon）；ED 2 个（Adult、Hospital）；MVI 2 个（Buy、Restaurant）；SM 1 个（Synthea）；DN 1 个（TableFact）；DD 1 个（BPID）。3:1:1 划分。注意摘要/结论只说"四类任务"，但 Table II/III 实际包含 6 类——摘要与正文范围不一致。
- **基线（13 个）**：Task SOTA 6 个（Ditto (ICDE'21)、Baran (VLDB'20)、IPM (ICDE'21)、SMAT、Binder、Sudowoodo）；LLM-based 7 个（Zero、Manual（专家选例，Narayan et al. VLDB'22）、SC、BatchER (ICDE'24)、CondAcc、CC-k、BestSoFar）。含多个 ICDE/VLDB 工作，最新为 2024。
- **LLM**：主实验 gpt-3.5-turbo；Table V 另测 Llama-2-70b、"Llama-3"、gpt-4o-mini（表注中模型名有笔误）。
- **设置细节**：候选池先用 SC（RAG 式）筛出 20 个，k=5，**每个数据集 US$10 示例选择预算**，每轮只在 200 条随机样本上估计效果；5 次重跑报均值与方差。
- **指标**：F1（MVI 用准确率）；效率：运行时间、Number of Tokens (NoT)、API 费用。
- **实验类型**：主结果（Table III，含方差与平均排名：BCSV 2.46、ACSV 3.92 最好）；统计检验（Fig.3 Wilcoxon-based critical difference，显著性 0.1）；成本（Table IV 时间与 token；BCSV 比 ACSV 快 3.6×、比 MCSV 快 15.2×，token 比 Manual 少 2×）；收敛/预算（Fig.4：预算 vs F1，anytime 性质）；k 敏感性（Fig.5：k=5 与 k=20 相当，节省 75%+ token）；跨 LLM（Table V）。无大规模可扩展性实验（最大数据集 ~2.9 万条，但只用 200 条验证样本估计）。
- **结果呈现**：大表（Table III/IV 横跨双栏，16 个方法列）+ 小图。表述："by 5.90% averagly in F1"（vs 专家手选）、"up to 5.90%"（贡献列表）、BCSV 比 SOTA batch prompting 高 4.43%；注意摘要与贡献列表对同一个 5.90% 用了"平均"与"up to"两种口径。

## 4. 写作结构 (Writing)
- **标题模式**：`Tailoring <经典理论工具> for <LLM 子问题> towards <DB 任务>`——"经典工具 + 定制"模式，强调把成熟理论（Shapley）改造到新场景，这是 DB 理论型论文常见标题。
- **摘要逐句功能**：S1 DW 的重要性 → S2 近期用 LLM 做轻量 DW → S3 需要 ICL 示例 → S4 gap：在示例规模约束下如何选示例尚未研究 → S5 提出 CSV（带 prompt 规模约束的 Shapley 变体）→ S6 CSV 性质良好 → S7 直接计算仍不可行 → S8 提出 ACSV 无偏估计 + 有近似保证的样本分配 → S9 结果（vs 专家手选平均 +5.90% F1，四类任务）→ S10 普适性声明。经典"gap → 定义 → 难 → 近似算法 → 实验"五段式。
- **引言逐段功能**：P1 DW 定义 → P2 "LLM-based DW."（加粗段首）+ Fig.1 → P3 "In-context example selection."：三类现有方法（RAG、topic model、influence-based）→ P4 "Limitations of existing solutions." + Example 1（17 万年 / 2.2 亿美元）→ P5 "The Shapley value."：引入 SV 定义（Eq.1）和直觉 → P6 SV 的优点（误差保证、与 RAG 正交）→ P7 "Challenges."：#P-hard + 两个 LLM 特有挑战（选出过多示例；选择成本高 O(mn log n)）→ P8 "Contributions."：3 条（建模+CSV；MCSV/ACSV 算法与复杂度；实验）。引言里就出现公式和复杂度，属于"理论导向"的写法。
- **章节顺序与篇幅**：I Intro（~1.7 页）→ II Preliminaries（6 种 DW 任务定义、prompt 示例、Problem 1、CSV 定义与性质、Problem 2、基本求解步骤，~2.2 页）→ III CSV Approximation（MCSV、ACSV + 两种分配、BCSV，~3.5 页）→ IV Experiments（~3.5 页）→ V Related Work（DW、ICL 示例选择、Shapley value 三类，~1 页，放末尾）→ VI Conclusion。
- **写作技巧**：
  - 用"算账"式例子量化朴素方法的不可行性（年数 + 美元），非常适合"成本受限"主题。
  - 每个算法后紧跟 "Algorithm analysis" 和 Proposition，形成"算法—保证"成对出现的节奏。
  - 主动与相近技术（complementary contributions、SVARM）划清界限，并在实验中实现一个改造版 CC-k 作为基线，以实验证明"小修小补不行"。
  - 示例短引：作者把核心约束概括为只需找到加入 k 示例集合后 "leads to the maximum utility gain" 的候选。
  - 瑕疵：存在交叉引用错误（"Figure IV-D"）、"LESE/LESD" 拼写不一、模型名笔误、摘要任务范围与实验不一致、Proposition 证明全部外放。说明 ICDE 审稿更看重问题建模与理论/实验完整性，但我们应避免这些硬伤。

## 5. 被录取的可能原因 (Why accepted) 与可借鉴点
1. **把"prompt 工程"问题变成一个有公理化基础的数据估值问题**：Shapley value 是 DB 社区熟悉的工具（data valuation、data debugging、SIGMOD Record 综述），"约束化 + 唯一性定理"给出了漂亮的理论包装。
2. **成本/预算是问题定义的一部分**：Problem 1/2 都显式带预算 B；样本分配的优化目标直接把 token 成本放进约束（Eq.10–12），这是"把 LLM 任务变成预算约束下的估计/优化问题"的典型范式。
3. **理论保证密集**：7 个 Proposition（无偏、误差界、错误概率），在 LLM-for-data 论文中少见，提升了"非纯经验"的学术分量。
4. **实验覆盖面广**：14 个数据集、6 类任务、13 个基线（含专用 SOTA）、方差、统计检验、跨 LLM——对"general applicability"论点支撑充分。
5. **可借鉴**：(a) 用 "anytime algorithm + 误差随预算单调下降" 的论证回避"到底花多少钱"的质疑；(b) 统一的 $10/数据集 预算设置便于公平比较；(c) critical difference 图展示多数据集排名。
- **潜在弱点（供我们攻击）**：(a) CSV 的 top-k 与最优 k-子集（Problem 1）之间无保证，且忽略示例间交互（冗余/互补）和顺序；(b) 示例选择是"每个数据集一次性"的静态选择，不是 per-query 自适应；(c) U 仅在 200 条样本上估计，估计噪声与 LLM 随机性未建模进误差界；(d) 预算只计 token/调用，未考虑选择阶段与推理阶段成本的联合优化（选择成本能否被推理阶段摊销）；(e) 只用 gpt-3.5 为主，较新的长上下文模型下 k 的约束可能变化；(f) 证明全在 TR，可复核性弱。
