# Claude skills

## academic-latex-polish
Polishes the English of a LaTeX research paper to the register of published PVLDB/SIGMOD papers. It does not change any fact, number, macro, citation or reference. A preservation checker verifies this after every edited file.

```
academic-latex-polish/
  SKILL.md                  instructions: writing rules, workflow, preservation checker
  scripts/check_preserve.py check that macros, refs, cites, labels, math and numbers survive an edit
  scripts/fix_tt_quotes.py  upright quotes inside \texttt{}; Unicode quotes/dashes -> LaTeX
  scripts/style_stats.py    compare sentence length, parentheses and semicolons with published papers
```

### Install on another machine
- **Claude Code (CLI or desktop).** Clone this repository and copy the skill folder into your personal skills directory:
  ```bash
  git clone https://github.com/wanghongsheng01/claude-skills.git
  mkdir -p ~/.claude/skills && cp -r claude-skills/academic-latex-polish ~/.claude/skills/
  ```
  To make it available in one project only, copy it to `<project>/.claude/skills/` instead.
- **claude.ai.** Zip the `academic-latex-polish` folder and upload it under Settings → Capabilities → Skills, or ask Claude in a chat to install it from this repository.

### Use
Ask Claude to "polish the paper with academic-latex-polish", or invoke the skill by name. The scripts are run as:
```bash
python3 academic-latex-polish/scripts/check_preserve.py OLD.tex NEW.tex
python3 academic-latex-polish/scripts/fix_tt_quotes.py sections/*.tex
python3 academic-latex-polish/scripts/style_stats.py refpapers/* paper/
```

## amp-figure-design
AMP (antimicrobial peptide) / protein-generative-model paper figure design conventions. Use when creating or revising figures for AMP papers submitted to Briefings in Bioinformatics, Nature Biomedical Engineering, Nature Communications, Cell, Science, or Nature Methods. Grounded in 13+ published papers (Das 2021, Wan 2024, HydrAMP, Diff-AMP, AMPSphere, ESMFold, DOME).

```
amp-figure-design/
  SKILL.md                        core rules: color, panel labels, typography, grid figure do/don't
  references/design-conventions.md full observations with paper + figure number
  references/color-palette.md     hex values for every color
  assets/matplotlib_style.py     reusable matplotlib rcParams template
```

### Install on another machine
```bash
git clone https://github.com/wanghongsheng01/claude-skills.git
mkdir -p ~/.claude/skills && cp -r claude-skills/amp-figure-design ~/.claude/skills/
```

### Use
Ask Claude to "design this AMP figure following amp-figure-design", or invoke the skill by name. The skill will tell you:
- never draw hand-drawn boxed tables with ✓/✗ marks (not present in any surveyed venue)
- use solid/hollow dot matrices for binary grids (Diff-AMP Fig. 6)
- use heatmaps with values printed in cells for continuous data (Wan 2024 Fig. 4a)
- use low-saturation ochre-blue-gray palette, not viridis
- use uppercase A/B/C panel labels for Briefings in Bioinformatics

## information-systems-submission
Pre-submission checklist (投稿前须知) for the Elsevier journal *Information Systems* (ISSN 0306-4379, CCF B). Scope test, required files, elsarticle formatting, highlights, exact declaration wording (CRediT, competing interests, data availability, generative AI), reproducibility programme and portal steps. Rules are tagged [GUIDE] (read from the Guide for Authors on 2026-10-21), [ELSEVIER] or [CHECK].

```
information-systems-submission/
  SKILL.md                      checklist with VERIFIED / ELSEVIER / CHECK status and sources
  scripts/check_submission.py   checks a LaTeX folder: journal line, abstract words, keywords, declarations,
                                AI heading, citations, labels, figure files, highlights, forbidden codes
  references/verification-log.md what was readable on which date and how to update the skill
```

```bash
python3 information-systems-submission/scripts/check_submission.py paper/ --main main.tex \
        --highlights highlights.txt --forbid 'OLDJOURNAL|ProjectCode'
```

## information-systems-writing
Writing guide for *Information Systems* papers in data quality, data cleaning, entity resolution, benchmarking and reproducibility. Built from published IS papers (measured register, title, abstract and introduction moves, results and limitations style, captions, references) plus the rules of `academic-latex-polish`. Includes an AI-flavor and register checker and a matplotlib style for figures.

```
information-systems-writing/
  SKILL.md                         title, abstract, section plan, language targets, anti-AI-flavor rules,
                                   figures, references, highlights, final checklist
  scripts/is_style_check.py        sentence length, long sentences, parentheses, semicolons, negations,
                                   em dashes, AI-tell words and internal codes, per section
  references/observed-papers.md    the surveyed IS papers with DOIs and observations
  assets/is_figure_style.py        matplotlib defaults, colour-blind-safe palette, box/arrow helpers
```

```bash
python3 information-systems-writing/scripts/is_style_check.py paper/main.tex --codes 'P19|v[0-9]+'
```

Install either skill like the others: `cp -r claude-skills/<skill> ~/.claude/skills/`.
