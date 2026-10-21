---
name: "amp-figure-design"
description: "AMP (antimicrobial peptide) / protein generative-model paper figure design conventions. Use when creating or revising figures for AMP, antimicrobial peptide, or protein-generative-model papers submitted to Briefings in Bioinformatics, Nature Biomedical Engineering, Nature Communications, Cell, Science, or Nature Methods. Covers color palettes, panel layout, typography, categorical grid / matrix figure conventions, and schematic/workflow figure style. Grounded in 13+ published papers (Das 2021, Wan 2024, HydrAMP, Diff-AMP, AMPSphere, ESMFold, DOME)."
---

# AMP / protein-generative-model paper figure design

Use this skill when the user asks to design, redesign, or critique a figure for an AMP, antimicrobial peptide, or protein-generative-model paper. The rules come from studying published figures in top-tier venues (Nature Biomedical Engineering, Nature Communications, Cell, Science, Nature Methods, Briefings in Bioinformatics).

## Workflow

1. **Identify the figure type.** Choose one of:
   - **Categorical grid** (rows = items, columns = conditions, cells = yes/no or pass/fail) → see "Categorical grid rules" below.
   - **Continuous heatmap** (e.g. MIC values across peptides × strains) → see "Heatmap rules".
   - **Workflow / schematic** (pipeline, decision tree, reporting checklist) → see "Schematic rules".
   - **Data plot** (bar, violin, scatter, ROC) → see "Color and typography".

2. **Read the reference file for the chosen type.** The detailed conventions and example paper + figure numbers are in `references/design-conventions.md`. Read it before drawing.

3. **Apply the hard rules below.** These are non-negotiable; they come from observing 13+ published figures.

4. **Use the matplotlib style template.** Copy `assets/matplotlib_style.py` and adapt it. It sets the correct font, colors, and panel-label style.

## Hard rules (do not violate)

### 1. Never draw hand-drawn boxed tables with ✓/✗ marks.

This style does not appear in the published figures of any surveyed venue. It reads as a draft / PPT slide, not a peer-reviewed figure. Instead:

| Cell type | Use this instead | Reference example |
|-----------|-----------------|-------------------|
| Binary (yes/no, has/has not) | Solid / hollow dot matrix | Diff-AMP Fig. 6 (Brief Bioinform 2024) |
| Continuous (MIC, AUC) | Heatmap with values printed inside cells | Wan 2024 Fig. 4a; Cell 2024 Fig. 6B/C |
| Pass/fail decision | Diamond flowchart with Yes/No on arrows | HydrAMP Fig. 6c; Huang 2023 Fig. 1b |
| Precise numeric values | Clean three-line table (no vertical lines, no color) | Sidorczuk Table 1/2; DOME Table 1 |

### 2. Color: low-saturation, semantic, not decorative.

- One hue per method / condition; reuse the same color across all panels in the paper.
- Dominant palette: **ochre-terracotta (#D2691E) + medium blue (#4682B4) + neutral gray (#808080)** — the classic Nature BME trio.
- Heatmaps use **blue-white-red diverging** (#2166AC → #F7F7F7 → #B2182B) or **orange-brown sequential** (#FFF7E6 → #8B4513). **Do not use viridis.**
- Never use neon or high-saturation primary colors.
- Ensure color is not the only encoding: add numbers, shape, or line style for colorblind safety.

### 3. Panel labels: uppercase A/B/C for Briefings in Bioinformatics; lowercase a/b/c for Nature family.

- Briefings in Bioinformatics: **bold uppercase A, B, C** at the upper-left corner of each panel.
- Nature family (Nat Biomed Eng, Nat Commun): bold lowercase a, b, c.
- Cell / Science: bold uppercase A, B, C, D.

### 4. Typography: sans-serif only.

- Use Arial / Helvetica. No serif (Times New Roman) fonts in figures.
- Axis labels outside the plot area; cell values inside the heatmap cells.
- Long labels (peptide names, strain names) rotated 90°.
- Panel letters are bold and slightly larger; axis labels regular; tick labels one size smaller.

### 5. Schematic / workflow figures: flat vector, no 3D, no shadows, no gradients.

- Right-angle rectangles with thin arrows; white background.
- Low-saturation macaron colors for zone blocks: light blue (#B8D4E8), light red (#E8B8B8), light green (#B8D8B8), light yellow (#F5EED8).
- Module names printed inside the module blocks.
- Key formulas or conclusions highlighted with a beige (#F5EED8) background box.
- Do NOT draw checklists as a "tick box" figure. If the user needs a reporting checklist, make it a three-line table (like MIQE / ARRIVE 2.0) or a conceptual workflow diagram (like DOME Fig. 2).

## Reference files

- `references/design-conventions.md` — full observations with paper + figure number for every rule.
- `references/color-palette.md` — all hex values, when to use each.
- `assets/matplotlib_style.py` — reusable matplotlib rcParams template.

## When the user asks "is this style acceptable?"

Check against the hard rules above. If the user has drawn a hand-drawn table with ✓/✗ marks, explicitly tell them this style does not appear in the target venue and suggest the alternative from the table in rule 1.
