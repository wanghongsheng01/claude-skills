# 出处、核验方法与恢复说明

## 1. 范文 PDF（官方来源，2026-11-20 下载）

均从 vldb.org 以 HTTPS GET 下载（禁止重定向），存入一个新的空目录，只用 `pdftotext`/`pdfinfo`/`pdftoppm` 读取，未执行其中任何内容。PDF 本身**不随本 skill 分发**；恢复时按下表 URL 重新下载并核对 SHA256。

| 缩写 | 论文 | 官方 URL | 字节数 | SHA256 |
|---|---|---|---|---|
| SPA | Shankar et al., spade: Synthesizing Data Quality Assertions for Large Language Model Pipelines, PVLDB 17(12): 4173–4186, 2024, DOI 10.14778/3685800.3685835 | https://www.vldb.org/pvldb/vol17/p4173-shankar.pdf | 1,320,966 | `36be0fd3a5022e88fa833d83068a2b4677b899fcb527fc28b700c38c729b230c` |
| DEE | Schelter et al., Automating Large-Scale Data Quality Verification, PVLDB 11(12): 1781–1794, 2018, DOI 10.14778/3229863.3229867 | https://www.vldb.org/pvldb/vol11/p1781-schelter.pdf | 1,049,733 | `d451ecf77b0fdc0756f91ec82aaa511c86bdb18229af13ab943c0f9e89a350cc` |
| YTC | Yang et al., Unlocking the Power of CI/CD for Data Pipelines in Distributed Data Warehouses, PVLDB 18(12): 4887–4895, 2025, DOI 10.14778/3750601.3750613 | https://www.vldb.org/pvldb/vol18/p4887-yang.pdf | 872,291 | `cfc18924fc06d13819a74b2bfd9a6619ace9122eb3eebc93c63576978216bf81` |
| SCO | Wu & Madden, Scorpion: Explaining Away Outliers in Aggregate Queries, PVLDB 6(8): 553–564, 2013（PDF 未印 DOI） | https://www.vldb.org/pvldb/vol6/p553-wu.pdf | 6,311,136 | `89190c93c2da7cd7e4b17a0b1b604f89dce6adc9c62d3d107bf3834ed3d9a6de` |

页数（pdfinfo）：SPA 14、DEE 14、YTC 9、SCO 12；均为 letter。

## 2. 第 4 篇范文的选择

考察了两篇候选：
- **Scorpion**（PVLDB 6, `vol6/p553-wu.pdf`）——采用。形式化问题 + 聚合函数代数性质 + 按性质分派的算法与剪枝正确性 + 构造 ground truth 的合成实验 + 真实数据，最接近"形式化保证 + 算法 + 数据管道中错误检测/定位 + 强实验"的研究稿形态；它把 SUM/COUNT/AVG 的可减性作为算法性质，与"由聚合语义派生守恒/对账类检查"的稿件直接同构。
- **Abedjan et al., Detecting Data Errors: Where are we and what needs to be done?**（PVLDB 9, `vol9/p993-abedjan.pdf`，2026-11-20 下载核对过 URL 可达，SHA256 `a6e6653f81d439f671af9f2e14c35a89514d384291e317fa3c5056399e911147`，688,165 字节）——未采用：它是对已有错误检测工具的实验性分析，没有新算法也没有形式化保证，形态更接近 EA&B。下载副本已删除，不作为本 skill 的证据。

## 3. 核验方法

- SPA 的逐句账本与 DEE/YTC 的结构拆解来自此前的人工拆解；2026-11-20 由一个独立核验者对照官方 PDF 逐项复核（按栏裁切计字数、逐条解析参考文献年份与 venue、重算 Table 4 均值、抽查 15 条句子级断言）。不一致处在各文件开头的「核验修正」中列出并已改正，主要是：DEE 与 YTC 的摘要字数原先把 PVLDB Reference Format 块算了进去（实为 161 与 152 词），SPA 参考文献约 1.35 页而非 1.7 页，YTC 三级标题 19 个而非 22 个。
- SCO 为本次新做的完整拆解：按栏裁切（x=0/306pt）逐页阅读全部 12 页；字数用"每行 ≥6 词、剔除散点图符号行"的口径统计；图表位置逐栏 grep 图注核对。
- 计数口径在 `fingerprints.md` 开头说明；所有字数为近似值。

## 4. 版权

所有拆解为中文转述、功能标注与统计；不连续引用原文超过约 12 个英文词；`sentence-templates.md` 中的模板按句子功能重写，不是原句。不分发 PDF。

## 5. DataHub 登记状态（2026-11-20）

按用户的永久规则，这 4 个官方 PDF 出处应登记到 DataHub 模块 `academic-review-evidence`（固定 URL、PDF 仅 hash/字节数出处）。本次尝试的结果是 **DATAHUB_REGISTRATION_BLOCKED**，原因：

1. 规范检出 `/Users/loctek/ai-workspace/datahub-cli` 中，`academic-review-evidence` 模块**本身尚未进入 git**：其 registry 条目只是 `src/core/registry.mjs` 中他人的未提交改动（HEAD 中 0 处），清单 `policies/academic-review-evidence-sources.json`、`bin/datahub-academic-review-evidence.py`、`src/core/academic-review-evidence.mjs`、测试和生成的 skill 都是未跟踪文件，属于另一个会话的在制工作（清单当日仍在修改）。只提交"自己的 hunk"在技术上不可能——任何提交都会连带提交他人的整份未跟踪模块。
2. 仓库的备份脚本 `scripts/backup-to-github.sh` 要求工作区干净且在 `main` 上推送；当时工作区有 224 项他人改动，且本地 `main` 落后 `origin/main` 5 个提交。
3. 该模块的 verifier 用 `POLICY_SHA256` 锁定清单并枚举固定数量（133）的来源；新增来源必须同时修改他人未提交的 verifier。

缺少的前提：模块所有者先把 `academic-review-evidence` 提交并推送（或工作区恢复干净、与 origin 同步）。之后可用一个独立提交追加下面 4 条来源（格式与 2026-11-20 STsCache/Crystal/Sieve 条目一致），同步更新 `POLICY_SHA256`、来源计数、`refs`、`triggers` 与 `provenance`，用仓库自带的 `scripts/gen-skills.mjs` 重新生成派生目录，并运行 `datahub academic-review-evidence +test --json`。

拟追加的 `sources` 条目：

```json
{ "id": "pvldb-spade-dq-assertions", "url": "https://www.vldb.org/pvldb/vol17/p4173-shankar.pdf",
  "title": "Shankar et al., spade, PVLDB 17(12), 4173-4186, DOI 10.14778/3685800.3685835; official PDF; data-quality assertion exemplar for PVLDB data-validation writing anatomy (PDF provenance only)" },
{ "id": "pvldb-deequ-dq-verification", "url": "https://www.vldb.org/pvldb/vol11/p1781-schelter.pdf",
  "title": "Schelter et al., Automating Large-Scale Data Quality Verification, PVLDB 11(12), 1781-1794, DOI 10.14778/3229863.3229867; official PDF; data-quality verification exemplar (PDF provenance only)" },
{ "id": "pvldb-youtube-cicd-data-pipelines", "url": "https://www.vldb.org/pvldb/vol18/p4887-yang.pdf",
  "title": "Yang et al., CI/CD for Data Pipelines in Distributed Data Warehouses, PVLDB 18(12), 4887-4895, DOI 10.14778/3750601.3750613; official PDF; industrial data-pipeline CI exemplar (PDF provenance only)" },
{ "id": "pvldb-scorpion-outlier-explanation", "url": "https://www.vldb.org/pvldb/vol6/p553-wu.pdf",
  "title": "Wu and Madden, Scorpion, PVLDB 6(8), 553-564; official PDF; aggregate outlier explanation exemplar (PDF provenance only)" }
```

预期 SHA256 / 字节数见第 1 节表格。拟追加的路由触发词：数据质量范文、Deequ、SPADE、Scorpion、YouTube CI/CD数据管道、数据校验PVLDB范文、ETL校验写作范文、Conserve写作范文、data validation PVLDB exemplar。

## 6. 在新机器上恢复

```bash
git clone https://github.com/wanghongsheng01/claude-skills.git
mkdir -p ~/.claude/skills && cp -r claude-skills/pvldb-data-validation-anatomy ~/.claude/skills/
# 需要复核 PDF 时：
mkdir -p ~/pvldb_exemplars && cd ~/pvldb_exemplars
for u in vol17/p4173-shankar vol11/p1781-schelter vol18/p4887-yang vol6/p553-wu; do
  curl -sS --max-redirs 0 -o "$(basename $u).pdf" "https://www.vldb.org/pvldb/$u.pdf"; done
shasum -a 256 *.pdf   # 与第 1 节表格比对
```
