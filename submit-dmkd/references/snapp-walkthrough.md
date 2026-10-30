# Snapp portal walkthrough for DMKD (门户逐页说明)

Entry: https://submission.springernature.com/new-submission/10618/3 (log in with a Springer Nature account, Google or ORCID). The author clicks every button; Claude prepares the values. Values to paste are in English; the explanations for the author are in Chinese.

The screens below are what DMKD's Snapp actually showed on 2026-10-30 (Regular/Research submission, LaTeX zip). Snapp has five tabs: Files → Details → Authors → Declarations → Review. Ask the author for a full-page screenshot of each tab and check it before they click Next.

1. **Files** — "Upload manuscript" 上传扁平 LaTeX zip（`main.tex`、`sn-jnl.cls`、图；正文自带 thebibliography 时不需要 .bst/.bib）。没有单独上传编译 PDF 的位置。Figures and tables、Supplementary material、Related files 均为可选，补充材料已在 Zenodo 时不传。
2. **Details** — Collection 留空（不要选 ECML PKDD）。Title、Abstract 由系统从 zip 自动抽取：**抽取的摘要会保留 LaTeX 转义**（实测出现 `et al.\repository`、`30\%`），必须清空后粘贴纯文本摘要。Cover letter 在此页上传（`Upload cover letter`）。
3. **Authors** — 先在 "Affiliated institutions" 逐个添加稿件中的每个单位（名称、国家、城市、可选的院系），再给每位作者选 Primary/Other affiliation（每人最多两个）。系统只自动建了第一个单位，并把它默认给所有作者，需逐人核对。通讯作者下拉框与稿件一致，不要多勾。Author Contributions Statement 用姓名缩写（"H.W.: …"），该文本取代稿件里的版本。
4. **Declarations** — Publishing policy 勾选；**Competing interests 默认可能停在 "No"**，稿件有申报时必须改选 Yes 并粘贴原文（期刊只发表门户版本）；Dual publication、Authorship 确认、Third party material、Data availability（选 Yes 后出现文本框）、Acknowledgements（取代稿件版本）、Research funding（选 Yes 后按作者填资助机构）。
5. **Review** — 汇总页，可点 Edit 回到各页修改。**没有建议审稿人字段**：推荐审稿人（姓名、单位、机构邮箱、一句理由，必要时披露远关系）应写进 cover letter。Research Square "In Review" 预印为可选，作者未发预印本时选 No。先点 "Download generated PDF for review" 下载 Snapp 用 pdflatex 生成的审稿 PDF 并核对，再由作者勾选条款并点 "Submit manuscript"。
6. **After submission** — 状态页显示 "Technical check"，并给出 Submission ID 与编辑部邮箱；保存截图和生成 PDF。

## Consistency checks before clicking Submit
- 门户标题、摘要、关键词与 `main.tex` 完全一致（摘要 150-250 词，关键词 4-6 个），摘要中无 `\`、`~`、`--` 等 LaTeX 残留。
- 每位作者的单位与稿件 `\affil` 一一对应。
- Funding、Competing interests、Author contributions、Acknowledgements 的门户文字与稿件原文一致。
- Snapp 生成的审稿 PDF：与本地定稿逐字比对（忽略断行）、无 `??`、参考文献完整、所有表格竖排、无超出版心的行、页数一致。
