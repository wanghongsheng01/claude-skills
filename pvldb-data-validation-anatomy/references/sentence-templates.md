# 可复用句式模板（英文模板 + 中文功能说明）

用法：模板用 `<slot>` 占位，写英文论文时填入自己的对象与数字。模板是根据四篇范文的**句子功能**重新写成的通用句式，不是原句；任何模板都不包含范文中超过约 12 个连续词的原文。每条注明功能与来源范文（SPA = SPADE，DEE = Deequ，YTC = YouTube CI/CD，SCO = Scorpion）。填槽规则：数字必须能在正文表/图中逐字找到，并写明口径。

## 1. 标题

- `<System>: <Gerund> <DB-familiar artifact> for <emerging workload>` —— 系统名 + 动作 + DB 熟悉的产物 + 新负载（SPA）。
- `<System>: <Verb-ing> Away <symptom> in <query or pipeline class>` —— 用"使症状消失"给出问题的操作性定义（SCO）。
- `<Gerund> <Scale qualifier> <Task noun phrase>` —— 无系统名、动作即贡献（DEE）。

## 2. 摘要

| 功能 | 模板 | 来源 |
|---|---|---|
| Context | `<Technology/operator> is increasingly deployed as part of <workload> that repeatedly <operation> over <data>.` | SPA A1 |
| Problem | `However, a key barrier to <deployment goal> is that <component> can <fail> silently and unpredictably.` | SPA A2 |
| Gap（能力缺失） | `Existing <systems> offer no way to <missing capability> from <observed symptom> to <its cause in the input>.` | SCO A3 |
| 重构 | `Accepting that <failures> are inevitable, we propose <DB concept> that detect when <component> errs.` | SPA A3 |
| System + I/O | `We present <System>, which takes <input> and returns <output> that <purpose>.` | SCO A4 |
| 操作性定义 | `Specifically, <output> is <object> such that <testable condition holds> while <side condition>.` | SCO A5 |
| Insight | `We observe that <users/code> already encode <requirements> in <observable artifact>.` | SPA A5 |
| Technique | `<System> therefore derives <candidate artifacts> from <artifact>, and selects <a subset> that satisfies <constraint 1> under <budget/constraint 2>.` | SPA A6 |
| Guarantee | `We prove that <selected checks> never <raise a false alarm> on <class of correct runs>, and detect every <fault class> within <budget>.` | 研究稿补充（四篇均无，见 P6） |
| Result（受控） | `On <N> <workloads> with <ground-truth construction>, <System> <metric verb> <x> (<unit: percentage points/relative>) compared with <named baseline class>, at <cost statement>.` | SPA A7（补口径） |
| Result（证据类型分离） | `On <real data> <System> finds <qualitative outcome>; on <synthetic data with ground truth> it matches <exhaustive baseline> in <quality metric> while running <factor>× faster.` | SCO A7 |
| Deployment | `<Component> is deployed in <product> and has been used by <N>+ <units> across <scope>.` | SPA A8 |

## 3. 引言

| 功能 | 模板 | 来源 |
|---|---|---|
| 用 DB 语言框定 | `A <pipeline/operator> can be viewed as a query over <relations> that is executed <offline in batch/online per tuple>.` | SPA I-P1 |
| 动机实例 + 目标 | `For example, Figure 1 shows <real data>. <Region/run> exhibits <symptom>. Our goal is to find <object> that <testable condition>, while <side condition>.` | SCO I-P2 |
| 揭晓真相 | `In this case, <symptom> is caused by <root cause>; yet this is not apparent from <what the user sees> and requires <manual effort>.` | SCO I-P3 |
| 难点（朴素代价） | `**<Challenge name>:** <what must be computed>. The naive approach <enumerates/re-executes> <space>, which is <cost> for <scale>.` | SCO I-P4 |
| Gap（已有方法） | `Existing <tools> [cites] can <execute/check> <artifacts> that users write or pick, but determining <which artifacts> remains open.` | SPA I-P2 |
| 与最近 DB 工作切割 | `While <prior line> [cites] targets <old setting>, it assumes <property>, which does not hold for <new setting>.` | SPA I-P2 S7 |
| 研究问题 | `We therefore ask: can we <goal> with as little <human effort/cost> as possible?` | SPA I-P2 S8 |
| 洞见（数据支撑） | `Our first insight is that <artifact> encodes <requirements> implicitly, because <users> <behavior>. To validate this, we analyzed <N> <real artifacts>.` | SPA I-P4 |
| 朴素 → 不足 → 设计 | `Instead of directly <naive approach>, which <failure mode>, we <technique>, since <reason>.` | SPA I-P7 |
| 难度 + 可解性 | `We show that <selection problem> is NP-hard. That said, it can be cast as <ILP/known problem> and solved within <time> at our scale (<size>).` | SPA I-P8 |
| 通用性 + 效率来源 | `<System>'s formulation applies to arbitrary <user-defined operators>, albeit slowly for black-box ones; we further identify <properties> that enable <efficient algorithms>.` | SCO I-P5 |
| 贡献（带节号） | `We <verb> <contribution> that <benefit> (Section <k>).` ×4 | SPA、DEE |
| 贡献（实验，带数字） | `We evaluate <System> on <N> <workloads> against <baselines>; it <result with unit> (Section <k>).` | SPA B4 |
| 范围声明（一次） | `We focus on <scope>; <excluded aspect> is orthogonal and left to future work because <reason>.` | DEE §3.2；SCO I-P4 |

## 4. 问题定义与形式化

| 功能 | 模板 | 来源 |
|---|---|---|
| 符号 + 立即实例化 | `Let <symbol> denote <object>. For example, in <running query>, <symbol> = <instance>.` | SCO §3.1 |
| 范围扩展一句话 | `We model <harder case> by <reduction to the base case>, and construct <outputs> with respect to <the reduced input>.` | SCO §3.1（join 物化） |
| 逐层定义 | `We first define <quantity> for a single <output>, then incorporate <user input 1>, and finally generalize to <sets of outputs>.` | SCO §3.2 |
| 设计理由 | `We use <max/abs/conjunction> because it <bounds/penalizes/ensures> <property>.` | SCO §3.2 |
| 未选的设计 | `Alternative formulations, e.g., <alternative>, are possible but not explored here.` | SCO 脚注 3 |
| 数值演算 | `For example, removing <tuple> from <group> changes <aggregate> from <a> to <b>, so its <quantity> is <value>.` | SCO §3.2 |
| 理想量 → 样本 | `In practice, <ideal metric> cannot be computed since <universe> is unknown; we assume a labeled sample <E'> (which may miss <X>, addressed in Section <k>) and use <metric on E'>.` | SPA 3.1-P3 |
| 优化问题 | `Formally, we minimize <objective> subject to <metric 1> ≥ α and <metric 2> ≤ τ.` | SPA 3.2 |
| 复杂度一句话 | `For <special parameters>, the problem is NP-hard via a reduction from <classic problem>; it is in NP since <certificate>.` | SPA 3.2 |
| 预先回应捷径 | `It is not immediately obvious why this problem is hard: why not simply <shortcut>? We give <k> reasons.` | SCO §3.3 |
| 定理陈述 | `Theorem <k> (<name>). If <preconditions>, then for every <input> in <class>, <property> holds.` | 研究稿补充 |
| 定理前提的可检查性 | `<System> checks <precondition> at <time> via <mechanism>; if the check fails, it <falls back/abstains>.` | SCO §5.3 check(D) |
| 性质 + 已知概念 | `This property is related to <classic concept> [cite]; in contrast, <ours> only requires <weaker/different condition>. Not all <classic class> satisfy it, e.g., <counterexample>.` | SCO §5.1 |
| 前提声明 | `Note that the property only holds if <data constraint>.` | SCO §5.3 |
| 增量形式化 | `Changes relative to <previous formulation> are highlighted in <color>. We keep <old constraint> because <reason>.` | SPA 3.3.1 |

## 5. 方法与算法

| 功能 | 模板 | 来源 |
|---|---|---|
| 节首路标 | `We first describe how <signal> informs <artifact>, then how to derive <artifact> from it.` | SPA §2 |
| 通用 → 快版本 | `These implementations assume nothing about <operator>, so they apply to arbitrary <operators>; Section <k> exploits <property> to make them efficient.` | SCO §4 |
| 改编经典算法 | `Our approach builds on <classic algorithm> [cite]. We first sketch it, then describe our <k> modifications.` | SCO §6.1/6.2 |
| 剪枝正确性 | `Pruning <candidate> is unsafe when <case>, e.g., <counterexample>. It is safe whenever <sufficient condition>, which we check by <mechanism>.` | SCO §6.2 |
| 按行讲解伪代码 | `Lines <a>–<b> initialize <state>; Lines <c>–<d> <update/prune>; the loop terminates when <condition>.` | SCO §6.2 |
| 设计取舍 | `We implement <component> on <platform> because <ecosystem reason>; the design does not rely on <platform-specific feature>.` | DEE §4 |
| 常数前指 | `We set <parameter> to <value>; Section <k> shows that <performance> is stable for <range>.` | SPA 4.3-P2；SCO §8.2 |
| 旋钮 | `We expose <trade-off> as a single parameter <c>: <c = low> favors <A>, while larger values favor <B>. None of the algorithms need to change.` | SCO §7 |

## 6. 实验

| 功能 | 模板 | 来源 |
|---|---|---|
| 目标段 | `Our experiments answer <k> questions: (Q1) <...>? (Q2) <...>? We use <synthetic data with ground truth> to control <difficulty>, and <real data> to <purpose>.` | SCO §8；DEE §5 |
| 数据集构造 | `We inject <fault types> into <base data>; the <severity> parameter <µ> controls how hard faults are to distinguish from clean runs.` | SCO §8.1 |
| 平凡基线 | `The simplest baseline, <trivial>, yields <degenerate result>; we instead compare against <reasonable baseline> that <rule>.` | SPA 4.2-P2 |
| 外部基线 | `We compare against <published method> [cite], using the authors' implementation (or a re-implementation that follows [cite] on the same code base), with the same <budget/hardware/inputs>.` | 研究稿补充 |
| 公平化昂贵对照 | `Because <exhaustive baseline> is exponential, we run an anytime variant for up to <T> and log its best answer every <Δt>.` | SCO §8.2 |
| 协议 | `Each configuration is run <n> times on <hardware>; we report <mean/median> and <95% CI> over <unit>. Errors during <step> are counted as <outcome>.` | SPA 4.2；研究稿补充 |
| 未测指标 | `We do not assess <metric> because <impracticality>; <measured metric> matters more here because <reason>.` | SPA 4.2-P4 |
| 可行性先行 | `<Component> achieves <accuracy> on average (Table <k>), and <step> takes under <t> in all cases except <case> (<t_max>).` | SPA 4.3-P1 |
| 走读 + 计数 | `Consider <workload>: <baseline> selects <a>, while <System> selects <b>. All methods satisfy <c1>, but <baseline> violates <c2> in <k> of <N> workloads.` | SPA 4.3-P2 |
| 趋势 + 原因 | `<Metric> grows linearly with <size> because <mechanism from Section k>.` | DEE §5.1 |
| Takeaway | `**Takeaway:** <System> <result with number> relative to <baseline>; <condition under which it holds>.` | SCO §8.3 |
| 负结果 | `On the flip side, <component> may <miss/cost more> when <condition>, e.g., <instance>; Section <k> discusses <mitigation>.` | SPA 4.3-P5；SCO §8.3.2 |
| 自家不利趋势 | `<Our variant>'s cost increases with <parameter> because fewer <candidates> can be pruned.` | SCO Fig 14 |
| 值不值 | `Given that the difference is under <x> for <k> workloads, one may ask whether <complexity> is worth it. <Answer with evidence>.` | SPA 4.3-P8 |
| ground truth 局限 | `A single ground truth does not exist here because <reason>; we therefore report results against both <GT1> and <GT2>.` | SCO §8.3.1 |
| 真实数据（无 GT） | `Since <real data> has no ground truth, we report the <outputs> and verify them against <independent evidence>; <metric> is <low value> because <reason>.` | SCO §8.4 |
| 部署数字口径 | `We observed over <N> runs on <custom inputs> (i.e., excluding <defaults>); we did not measure <blind spot>.` | SPA 2.4-P2 |

## 7. 图表图注

- 结论式：`<Metric> of <System> grows linearly with <size>, while <baseline> grows <super-linearly>.`（DEE Fig 4 风格）
- 协议进标题：`<Result> for <datasets>. Checks are derived on <x%> of the data and evaluated on the remaining <y%>; failed checks are shown in gray.`（DEE Table 3 风格）
- 主张式机制图：`A <candidate> is <invalid> if it (a) <case 1> or (b) <case 2>.`（SCO Fig 6 风格）
- 表内约束标记：`✓/✗ indicate whether <constraint> is satisfied; best values per workload are in bold.`（SPA Table 4 风格）

## 8. 相关工作段末对比句

- `Our work does not directly <their goal>, but complements it by <our function>.`（SPA 5-P1）
- `These works rank <individual items> by <measure>, but do not <construct/derive> <our artifact>.`（SCO §9）
- `<System> differs by explicitly optimizing <objective> and supporting <additional inputs>.`（SCO §9）
- `Recent work [cites] and tools [cites] <execute> <artifacts> that users <write or pick>; we instead <derive and select> them automatically.`（SPA 5-P2）
- `In contrast to <prior work>, which assumes <property>, <our setting> <violates it because ...>.`（SPA I-P2 S7）

## 9. 结论

- `This paper introduced <problem> and <System>, which <mechanism 1> and <mechanism 2>.`
- `We formalized <selection> as <problem> and proved <guarantee>; in the absence of <labels>, it reduces to <tractable case>.`
- `Across <N> <workloads>, <System> <headline result with the same unit as the abstract>.`
- `Open problems include <future work 1, derived from a limitation> and <future work 2, derived from a rejected alternative>.`

## 10. 局限写法（不自我否定）

- `<System> targets <scope>; <out-of-scope case> requires <additional mechanism>, which <is orthogonal / we sketch in Section k>.`
- `When <condition>, <System> falls back to <safe behavior>, which costs <x> but preserves <guarantee>.`
- 避免：在摘要、引言、结论里逐句重复免责；避免 "we do not claim", "only a prototype" 一类自我否定句式（详见 `write-pvldb` §7）。
