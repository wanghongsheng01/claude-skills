# Snapp portal walkthrough for DMKD (门户逐页说明)

Entry: https://submission.springernature.com/new-submission/10618/3 (log in with a Springer Nature account, Google or ORCID). The author clicks every button; Claude prepares the values. Values to paste are in English; the explanations for the author are in Chinese.

Generic steps from the Snapp help pages [SN]; DMKD-specific screens are [UNKNOWN] until the author has seen them. Record what the portal actually shows in this file after each submission.

1. **Article type** — 选 "Regular Paper"（或按稿件类型选 Survey Paper）。不要选任何 ECML PKDD collection。
2. **Upload files** — 上传 LaTeX zip（扁平结构，含 `main.tex`、`sn-jnl.cls`、图、参考文献），再上传编译好的 PDF 和 cover letter。Snapp 会自动编译 zip 生成审稿 PDF；编译失败会退回，需要检查 log 并重传。
3. **Confirm extracted details** — 系统自动提取标题、摘要、作者；逐项与 `main.tex` 对照（标题大小写、摘要全文、作者顺序、单位）。
4. **Additional information** — 作者与单位、通讯作者、ORCID、资助信息（Funding，按稿件 Statements and Declarations 原文填写）、作者贡献（Author contributions）、利益冲突（Competing interests；期刊只发表门户里填写的版本，必须与稿件一致）。
5. **Declarations / policies** — 双重投稿、第三方材料、预印本（如有 arXiv，填 DOI 与许可）、数据可用性；同意政策。开放获取在录用后才选择。
6. **Reviewers (if shown)** — 建议审稿人需独立、来自不同国家和机构，提供机构邮箱和 ORCID/Scopus ID；回避审稿人通常不超过两人/两个课题组。
7. **Review and submit** — 是否在 Research Square 预印（In Review）为可选项，由作者决定；最后由作者本人点击 "Submit Manuscript"。

## Consistency checks before clicking Submit
- 门户标题、摘要、关键词与 `main.tex` 完全一致（摘要 150-250 词，关键词 4-6 个）。
- Funding、Competing interests、Author contributions 三处门户文字与稿件原文逐字一致。
- Snapp 生成的审稿 PDF 打开检查：无 `??`、参考文献完整、图清晰、页数与本地编译一致。
