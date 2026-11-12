# CVIU 上传界面与版本替换

## 证据范围

2026-11-12 作者提供的 CVIU `submit.elsevier.com/CVIU` 页面截图显示以下映射。它是这次可见界面的观察，不证明所有账号或文章类型永久相同；未来使用时以当前页面为准。截图本身、账号和稿件信息不随公共技能发布。

同日官方作者指南直接 GET 返回 403；这次界面观察不等于重新阅读全文指南。官方 Elsevier review 指南可读。原格式依据及其日期保留在 [requirements.md](requirements.md) 与 [official-refresh.md](official-refresh.md)。

## LaTeX 稿件的实际映射

|页面类别|文件内容|使用注意|
|---|---|---|
|Required: Cover letter|投稿信|按页面支持格式上传|
|Required: Manuscript|实际编译的主文 PDF|页面要求已编译 PDF；源码不能替代这一文件|
|Declaration of competing interests|官方声明 Word，或页面提供的无利益冲突确认|根据作者已确认事实选择；界面若显示 Confirmed，不擅自改变状态|
|Optional: LaTeX source files|主文完整 LaTeX ZIP|虽然置于 Optional 区域，页面明确要求 LaTeX 稿同时提供源码|
|Optional: Highlights|单独可编辑 Highlights|通用 Optional 区域不取消作者指南的具体要求|
|Optional: Supplementary material|补充 PDF、补充源码、代码或必要证据侧包|各文件类型明确；关联侧包缺失会使复现材料不完整|
|Optional: Figure / Table / Graphical abstract / Audio-Video|实际需要的相应附件|不因看到类别就凭空生成或重复上传已有内容|

源码组织版与同层版可同时保存在本地，上传同一角色时只选一套；若需要同层包，先核对资源重名与引用改写，再干净解压构建。补充源文件与主文源文件应明确区分，避免系统将第二个入口当成主文。

## 当前草稿已经有文件时

只问一个会影响动作的问题：是否已最终 Submit。尚未提交则可准备替换清单；已提交则查系统允许的修订流程，不能再按新稿重复投递。复用本轮已有回答，无需再次问同样问题。

1. 保留前版，生成一个完整新发布目录，未变文件按内容校验继承。
2. 建立“页面类别｜新文件｜替换旧文件｜是否改动”的短清单；实际上传的 PDF、源 ZIP、Highlights 和投稿信须属于同版。
3. 题名、摘要、作者、关键词与声明从最终材料复制。若只调整版式而这些字段未变，明确保留；若改了内容，同步修改在线字段。
4. 检查系统 proof 的文章与附件列表。组织版/同层版本地一致只能证明本地可重建，不能代替平台 proof。

只写实际完成状态：文件已核对、已本地构建、已上传、proof 已看、已提交。私有 Git 备份不是投稿上传，也不代表审稿人可以访问私人仓库。备份回执与科研审阅报告留在交付目录，不默认作为期刊附件。
