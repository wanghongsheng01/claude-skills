# Verification log

| Date | What | How | Result |
|---|---|---|---|
| 2026-10-29 | ESWA Guide for Authors | Claude in Chrome, `get_page_text` (first call empty while the page rendered; second call returned 50k chars; tail read after trimming the DOM) | Full text read; digest in `guide-digest.md` |
| 2026-10-29 | Open access options | Claude in Chrome | APC USD 3,630 excl. tax; CC BY / BY-NC / BY-NC-ND; 24-month embargo; no posting of published PDF on ResearchGate/Academia |
| 2026-10-29 | Journal insights | Claude in Chrome | CiteScore 17.0, IF 9.4; 5 / 62 / 147 / 7 days; indexed in Scopus, SCIE, ABDC |
| 2026-10-29 | Editorial board | Claude in Chrome | EiC Prof. Ling Wang (Tsinghua); 156 editors, 32 countries; founding editor Jay Liebowitz |
| 2026-10-29 | Editorial Manager landing page | Claude in Chrome (not logged in) | https://www.editorialmanager.com/eswa/ ; "Continue with Elsevier" sign-in; the in-portal steps were not visible without logging in → tagged [CHECK] |
| 2026-10-29 | LaTeX bibliography style | GitHub (Ravby/eswa-template, community, MIT) | `elsarticle` + `\biboptions{authoryear}` + `model5-names.bst` (Elsevier, LPPL) for APA-style lists |
| 2026-10-30 | ESWA Guide for Authors (re-read) | Claude in Chrome, `get_page_text` (50k chars) + `javascript_tool` for the tail in ~950-character slices (longer returns are truncated or blocked when they contain URLs) | No rule changes since 2026-10-29; added own-script names, standard institution names, language-help acknowledgements, GenAI-and-figures details, `[dataset]` placement, submission checklist |
| 2026-10-30 | Editorial Manager registration page | Screenshot from the author | Field list recorded in the walkthrough |

## How to refresh
1. Open the guide in Claude in Chrome; if `get_page_text` returns nothing, wait and retry.
2. Diff against `guide-digest.md`; update tags in `SKILL.md` and this log.
3. After a real submission, replace the [CHECK] items of the Editorial Manager walkthrough with what the portal showed (item-type names, questionnaire questions, required fields), and add portal traps.
