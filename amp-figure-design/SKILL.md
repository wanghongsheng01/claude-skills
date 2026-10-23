---
name: "amp-figure-design"
description: "AMP (antimicrobial peptide) / protein generative-model paper figure design conventions. Use when creating or revising figures for AMP, antimicrobial peptide, or protein-generative-model papers submitted to Briefings in Bioinformatics, Nature Biomedical Engineering, Nature Communications, Cell, Science, or Nature Methods. Covers color palettes, panel layout, typography, categorical grid / matrix figure conventions, and schematic/workflow figure style. Grounded in 13+ published papers (Das 2021, Wan 2024, HydrAMP, Diff-AMP, AMPSphere, ESMFold, DOME)."
---

# AMP / protein-generative-model paper figure design

Use this skill when the user asks to design, redesign, or critique a figure for an AMP, antimicrobial peptide, or protein-generative-model paper. The defaults come from a selected sample of published figures (Nature Biomedical Engineering, Nature Communications, Cell, Science, Nature Methods, Briefings in Bioinformatics). They are observations and design suggestions, not journal requirements or proof that other designs are unacceptable.

## Workflow

1. **Identify the figure type.** Choose one of:
   - **Categorical grid** (rows = items, columns = conditions, cells = yes/no or pass/fail) → see "Categorical grid rules" below.
   - **Continuous heatmap** (e.g. MIC values across peptides × strains) → see "Heatmap rules".
   - **Workflow / schematic** (pipeline, decision tree, reporting checklist) → see "Schematic rules".
   - **Data plot** (bar, violin, scatter, ROC) → see "Color and typography".

2. **Read the reference file for the chosen type.** The detailed conventions and example paper + figure numbers are in `references/design-conventions.md`. Read it before drawing.

3. **Choose the defaults below that fit the data.** Match encoding to the question, preserve quantities and units, and check current official artwork requirements separately when needed.

4. **Use the matplotlib style template when useful.** Copy `assets/matplotlib_style.py` and adapt it. Its font, colors and panel labels are starting choices, not a venue mandate.

## Observed design defaults

### 1. Choose matrix or table encodings for the values being compared.

The selected examples favor the alternatives below. Absence of a checkmark style in this sample is not evidence of a venue ban. Choose a clean table, dots or a heatmap according to the actual data and readability:

| Cell type | Use this instead | Reference example |
|-----------|-----------------|-------------------|
| Binary (yes/no, has/has not) | Solid / hollow dot matrix | Diff-AMP Fig. 6 (Brief Bioinform 2024) |
| Continuous (MIC, AUC) | Heatmap with values printed inside cells | Wan 2024 Fig. 4a; Cell 2024 Fig. 6B/C |
| Pass/fail decision | Diamond flowchart with Yes/No on arrows | HydrAMP Fig. 6c; Huang 2023 Fig. 1b |
| Precise numeric values | Clean three-line table (no vertical lines, no color) | Sidorczuk Table 1/2; DOME Table 1 |

### 2. Color: low-saturation, semantic, not decorative.

- One hue per method / condition; reuse the same color across all panels in the paper.
- One available palette is **ochre-terracotta (#D2691E) + medium blue (#4682B4) + neutral gray (#808080)**; it is not required by a venue.
- Example scales include **blue-white-red diverging** (#2166AC → #F7F7F7 → #B2182B) or **orange-brown sequential** (#FFF7E6 → #8B4513). Use a diverging scale only when a meaningful center exists. A perceptually ordered sequential scale, including viridis, can be appropriate; sample absence does not prohibit it.
- Favor readable contrast and avoid decorative saturation that obscures the data.
- Ensure color is not the only encoding: add numbers, shape, or line style for colorblind safety.

### 3. Panel labels: match the target format and remain consistent.

- The observed Briefings in Bioinformatics examples use **uppercase A, B, C** at the upper-left of panels; this is an observed default, not a verified blanket rule.
- Nature family (Nat Biomed Eng, Nat Commun): bold lowercase a, b, c.
- Cell / Science: bold uppercase A, B, C, D.

### 4. Typography: use a legible, consistent font.

- Arial / Helvetica are useful starting choices; follow the actual artwork instructions and inspect embedded fonts at final size.
- Axis labels outside the plot area; cell values inside the heatmap cells.
- Wrap or rotate long labels (peptide names, strain names) only as needed for legibility.
- Panel letters are bold and slightly larger; axis labels regular; tick labels one size smaller.

### 5. Schematic / workflow figures: favor simple vector shapes and clear flow.

- Right-angle rectangles with thin arrows; white background.
- Low-saturation macaron colors for zone blocks: light blue (#B8D4E8), light red (#E8B8B8), light green (#B8D8B8), light yellow (#F5EED8).
- Module names printed inside the module blocks.
- Key formulas or conclusions highlighted with a beige (#F5EED8) background box.
- A checklist usually works well as a clean table or structured text. Use a workflow diagram when it communicates real decisions or data flow; do not add arrows that imply unestablished model-to-sample attribution.

## Evaluation-figure observations from bbac343

The published PDF was visually rechecked on 2026-10-23: Figure 1 (page 6) contrasts a confounded comparison with a controlled cross-design; Figure 2 (page 8) combines a paired scatter with factor-wise boxplots; Figure 3 (page 9) uses consistent small-multiple heatmaps, color for mean AUC and point size for SD. Tables 1/2 (pages 3/5) define sampling rules and architectures rather than displaying project progress.

Learn the question-to-encoding relation, not just the palette. Keep the complete applicable comparison visible. Use uncertainty only for the units actually repeated; single-seed models do not justify invented across-seed intervals. Property-summary metrics are not evidence for a full sequence distribution. For paragraph and evidence organization, see [bib-amp-evidence-writing](../bib-amp-evidence-writing/SKILL.md) and its [detailed exemplar map](../bib-amp-evidence-writing/references/bbac343-writing-experiment-map.md).

## Reference files

- `references/design-conventions.md` — full observations with paper + figure number for every rule.
- `references/color-palette.md` — all hex values, when to use each.
- `assets/matplotlib_style.py` — reusable matplotlib rcParams template.

## When the user asks "is this style acceptable?"

Assess whether the figure answers its question, faithfully encodes the data and remains legible at final size. Explain observed examples as examples. Suggest alternatives when they improve readability; do not claim that a design is forbidden solely because it was absent from the surveyed papers.
