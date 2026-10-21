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
