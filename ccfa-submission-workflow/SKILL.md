---
name: "ccfa-submission-workflow"
description: "Submission-prep commander for CCF-A data-management papers (ICDE, PVLDB/VLDB, SIGMOD Industrial, TKDE, KDD). Distills Dr.Wang's ICDE 2027 Round-2 process log into a reusable playbook: verify the Overleaf PDF against the local latest before preparing form fields; auto-invoke venue writing, review, presentation, integrity and CMT skills; write a second-author briefing; hand the author a Chinese walkthrough of what only they can submit (ORCID, COI, final click); one session per paper; survey the venue before new ideas; portfolio caps and no same-venue data overlap. Official CFPs win. Historical 'acceptance over honesty' wording is not adopted. Use when preparing a submission packet, filling CMT/portal fields, running a pre-deadline review, or directing parallel paper sessions (投稿总指挥 / 投稿准备 / CMT表单 / Overleaf核对 / 第二作者简介 / 任务说明书)."
---

# CCF-A submission workflow (投稿准备总指挥)

This skill is the **commander**: it says *in what order* to prepare a CCF-A submission and *what standing orders* the agent follows when the author directs that work. It does **not** replace venue-specific skills. Official author guidelines always win; re-open them and record the access date.

| Step | Skill to invoke | What it covers |
|---|---|---|
| Venue rules | `write-*`, `submit-icde` / equivalent, `icde-subject-areas` | Page budget, blindness, EAB tag, appendix, author caps |
| Presentation and SOTA | `paper-presubmission-review`, `results-presentation-review`, `results_lint` | Bold/underline, count rows, advisor vs official conflicts |
| Prose | `manuscript-writing-review`, `manuscript-proofcheck`, `academic-latex-polish` | Language and compile |
| Citations | `submission-integrity-check` | Every reference exists online |
| Form packet | `icde-cmt-submission` (or the venue's form skill) | Paste-ready English fields that match the PDF |

Reports to the author are **Chinese documents**. Reviewer-facing text (PDF, CMT abstract, relevance box) is **formal academic English**, copied from a generated file, never retyped by hand.

## Sources

Dr.Wang's process log for the ICDE 2027 R2 submissions (deadline 2026-11-11): https://loctek.feishu.cn/docx/UGXddY4xgoig82x3KxUcLtDDn1g, read 2026-11-12, plus a linked historical-rejection outline. No credential, password, API key, or raw enterprise datum from that log is copied here. Details: `references/process-log-sources.md`. The commander checklist itself is `references/commander-checklist.md`.

A standing sentence in that log, “准备投稿工作是以能被录用为最高原则……不是以你所谓的诚实为第一优先级,” is **not adopted**. Acceptance is pursued through stronger methods, complete experiments, clearer presentation, and honest analysis of losses — not by inventing numbers, dropping measured cells, or weakening disclosure. That rejection is consistent with `paper-presubmission-review` and with 邓老师 S07/S10.

## 1. Standing orders (what the author repeatedly asked the agent to do)

1. **Latest materials only.** Before preparing anything for the submission window, compare the author's Overleaf-compiled PDF with the local latest, **page by page**. If they differ, stop and reconcile. The title, abstract and numbers given for the form must be those of the final PDF.
2. **Final pre-submission review is mandatory**, not optional. Auto-invoke the skill pipeline in the table above. If any of those reviews has not been run on the current PDF, run it before handing over form fields.
3. **Give the author the packet; the author submits.** Prepare paste-ready fields, a Chinese click-path, and a list of ticks. Do not press Submit, create a public artifact repository, change repo visibility, or log into CMT, unless the author has explicitly authorized that exact action.
4. **What only the author can finish** (remind, don't do): every co-author's CMT/portal profile with **ORCID**; **domain and individual conflicts** (one missing author is a desk reject at ICDE); the final upload and Submit; copyright; confirming the AI-generated-content declaration; deciding to make an artifact public. After a paper record is created, every co-author may need to log in again to mark personal conflicts.
5. **CMT abstract tracks the PDF.** If the abstract changes after a form draft, flag that the portal text must be re-copied. Character limits are those of the live form (ICDE 2027 R2 abstract: 2,000 characters).
6. **Frozen authors.** Sync the author list, affiliations, corresponding-author marks and ORCID only from a written decision by the author. Never invent, drop, or reorder names.
7. **Second-author briefing.** Before sending the PDF to the second author, write a short document (Chinese, unless asked otherwise) covering: (1) the scientific problem, (2) how existing methods do it, (3) why they are not enough, (4) the proposed method, (5) experimental comparison and SOTA standing. Evaluate the second author's comments yourself (a fast pass can miss a table's intent); official CFP wins; absorb accepted comments into skills rather than one-off edits.
8. **Start now; 任务说明书 for the rest.** Everything the agent can run, start immediately. Everything that needs the author (a compile on Overleaf, a keystroke in a vault, a license confirmation) is delivered as a **任务说明书**: what, why, the exact command or click path, and what “done” looks like. Do not wait for a standing meeting.
9. **Do not stop current work** when a new parallel task arrives; start it alongside, in a **separate session per paper** so numbers and prompts do not pollute each other.
10. **Portfolio.** Do not put all eggs in one basket (research *and* EAB; more than one topic family). Do not submit two papers to the same venue when they share business data and the contributions are not clearly distinguished. Official caps still apply (ICDE: at most 5 research-track papers per author per round; PVLDB: 2 per author per month, 12 per year). A rejection at ICDE blocks that paper (and revisions) for a year; format/COI desk-rejects may return in the next round — confirm on the live CFP.
11. **New work starts with a venue survey**, not with an idea. Deep-read accepted papers' problems, methods, experiments and writing; then innovate; then run real experiments; then write. Deliver a Chinese document at each stage; deposit reusable skills.
12. **One Overleaf project per paper, via Git.** Do not open a new Overleaf link at every iteration (邓-会议, same process log). Pull first; do not overwrite author-only Overleaf edits.
13. **Numbers from one source of truth.** Macros, tables and the abstract come from the same final run. After a change, recompile to 0 errors and recount body pages on the fresh PDF.
14. **Safety.** Enterprise access is read-only. Do not ask anyone for a password. Do not write credentials into files, commands, or documents. No raw enterprise data in git or the manuscript. If an export contains unexpected personal fields, **stop and report**. Do not bypass security, anti-crawl, or a blocked download. Public data must independently support the same conclusions. LLM API spend follows the author's standing daily cap unless they raise it for a named window; “budget is insufficient” is not a reason to leave a hole without a cheaper alternative and a 任务说明书.

## 2. Commander sequence (run in this order)

1. Identify the venue and **re-read the official pages**. Record the access date. Apply `paper-presubmission-review`'s official-vs-advisor table.
2. Confirm SOTA standing from real repository numbers. If the verdict is not 可投, say so; a form packet does not replace missing results.
3. Run the skill pipeline on the current sources. Fix only presentation and compliance unless the author asked for method work. Do not change frozen authors or experimental numbers.
4. Compile; confirm the body page budget; inspect every page.
5. Diff the Overleaf PDF (if the author provided one, or after `sync_overleaf.sh`) against this compile, page by page.
6. Build the form packet: English paste-ready fields identical to the PDF; Chinese walkthrough; ORCID/COI reminder; artifact paragraph; AI declaration text; Relevance / similar boxes with live character counts.
7. Write or refresh the second-author briefing if a co-author review is next.
8. Hand the author a single Chinese index: links to the PDF, the form packet, what they must still do, and the official deadline in their timezone. The agent does not submit.

## 3. Venue hooks (always re-check the live page)

| Venue | Typical hard points (verify live) | Form skill |
|---|---|---|
| ICDE | 12 pages excluding only refs and AI ack; **no appendix**; single-blind; ORCID + COI for every author; 5 papers/author/round; EAB title **prefix** `[Experiment, Analysis, and Benchmark]`; artifacts mandatory for EAB; no revision (rebuttal exists); rejection blocks a year | `icde-cmt-submission`, `submit-icde` |
| PVLDB | 12-page body **including** appendix; single-blind; 2/month and 12/year caps; EA&B title **suffix** `[Experiment, Analysis & Benchmark]`; reproducibility package at initial submission; declare concurrent submissions | `write-vldb` |
| SIGMOD Industrial | 12 pages + refs; not double-blind; non-academic author required; CFP does not grant a Research-track-style extra appendix | `write-sigmod-industrial` |
| TKDE | Journal page limit includes refs and bios; supplemental as separate files; rolling | `write-tkde` |
| KDD research | 8 self-contained content pages at submission, then refs+appendix; camera-ready 12 (9+3) | `write-kdd` if present |

## 4. Cross-links

- Presentation, SOTA-at-a-glance, advisor meetings: `paper-presubmission-review` (邓-会议 items A5, B6–B7, C4, F4–F5, H1–H3).
- Experiment analysis under PVLDB rules: `write-vldb` §7 and `write-vldb/references/deng-meeting-experiment-analysis.md`.
- This commander does not rewrite those files' official-rule sections.
