# Detailed figure design conventions for AMP / protein-generative-model papers

Grounded in a selected sample of published figures. Every observation cites a specific paper + figure number. These observations are design examples, not journal-wide requirements; a style absent from the sample is not thereby prohibited. The 2026-10-23 recheck of bbac343 is documented in the companion [exemplar map](../../bib-amp-evidence-writing/references/bbac343-writing-experiment-map.md).

## Table of contents
1. Color
2. Panel structure
3. Typography
4. Categorical grid / matrix figures (the most common question)
5. Schematic / workflow / checklist figures
6. Full paper list

---

## 1. Color

### 1.1 Saturation
Low. The dominant blues are medium blue (#4682B4), not bright royal blue. Oranges are terracotta / ochre (#D2691E), not vivid orange. Reds are brick red (#B2182B), not fire-engine red. No neon.

### 1.2 Semantic use
One hue per method / dataset / condition, fixed across all figures in the paper. No decorative color.

- **Das et al. 2021, Fig. 4a–d** (Nat Biomed Eng 5:613): Gen-amp = ochre, Train-amp = medium blue, Train-unlab = neutral gray. The same three colors are reused across all four panels.
- **Wan et al. 2024, Fig. 2a–b** (Nat Biomed Eng 8:854): APEX = deep brick red; baselines: RF = light green, GBDT = teal, ElasticNet = dark blue, LinearSVR = light blue, ExtraTree = gray.
- **HydrAMP (Szymczak et al. 2023, Nat Commun 14:1453), Fig. 1–4**: training modes fixed as reconstruction=pink, unconstrained=yellow, analogue=blue, all modes=gray. Methods: HydrAMP=red, PepCVAE=dark blue, Basic=light blue, Joker=dark green.

### 1.3 Heatmap color scales
- **Diverging blue-white-red** for MIC / dual-direction data: **Wan 2024 Fig. 4a** (40+ peptides × 11 strains MIC), deep blue = low MIC (good), white = middle, red = high MIC (bad).
- **Sequential orange-brown** for one-direction data: **AMPSphere (Santos-Júnior et al. 2024, Cell 187:3761), Fig. 6B/C** (100 peptides × 19 strains MIC), light cream yellow → deep brown orange.
- Viridis was not recorded in this sample. This does not make it inappropriate: choose a perceptually ordered sequential scale for ordered magnitudes, and a diverging scale only for a meaningful center.

### 1.4 Colorblind safety
No paper explicitly declares Okabe-Ito, but the actual approach approximates ColorBrewer qualitative palettes. Information is never carried by color alone: color + number + shape / line style are used as redundant encodings.

### 1.5 pass/fail encoding
The cited examples use MIC magnitudes or written Yes/No decisions rather than checkmarks. A continuous MIC color is not automatically a clinical pass/fail verdict; any activity threshold must be defined for the study.

---

## 2. Panel structure

### 2.1 Panel label convention
| Venue | Label style | Position |
|-------|------------|----------|
| Nature family (Nat Biomed Eng, Nat Commun) | bold lowercase a, b, c | upper-left outside each panel |
| Cell / Science | bold uppercase A, B, C, D | upper-left outside each panel |
| Briefings in Bioinformatics | bold uppercase A, B, C (sometimes "(A)") | upper-left of panel or in caption |
| Nature Methods review / commentary (e.g. DOME) | text title ("Classification metrics") | top of block, no a/b/c |

### 2.2 Aspect ratio
- Main figures are double-column full width (~170 mm).
- Workflow figures: landscape 2:1 or wider (Das 2021 Fig. 1 is a ~9:1 timeline banner).
- Multi-panel data plots: 4:3 or 3:2 landscape.
- Small multiples (violin / box plots): 3:4 or 2:3 portrait (HydrAMP Fig. 3 is 2×4, 8-panel portrait).
- Large heatmaps: near-square (Cell Fig. 6 ~1770×1779 px).

### 2.3 Density
High but ordered. Grid alignment, shared axes, unified legends. Example: **Cell Fig. 6B/C** is ~100 rows × ~20 columns, with row labels rotated 90°, values printed inside cells, continuous color scale.

---

## 3. Typography

### 3.1 Font family
Sans-serif is the observed preference in this sample, approximating Arial / Helvetica. It is a useful default rather than a prohibition on other legible fonts.

### 3.2 Font size hierarchy
```
Panel letter (a/A)  >  axis title  >  tick label ≈ legend ≈ cell value
   (bold, larger)      (regular)         (one size smaller)
```
Heatmap cell numbers are smallest (~6–7 pt equivalent) but use contrast (white on dark fill / dark on light fill).

### 3.3 Label placement
- Axis labels: outside the plot area (below X axis, left of Y axis).
- Legends: inside the panel, in empty space, not over data.
- Cell values: inside the heatmap cells (e.g. Cell Fig. 6 prints 32/64/128 μM directly).
- Module names: inside the module blocks (HydrAMP Fig. 1 Encoder/Decoder/Classifier).
- Detailed explanation goes in the caption, not in the figure.

### 3.4 Avoiding overflow
- Long labels (peptide names, strain names) rotated 90° (standard) or 45° (Diff-AMP Fig. 6/7 attribute names).
- Use abbreviations (e.g. "anti-Gram+" not the full name).
- Flowchart text fits inside blocks; blocks are sized to text.

---

## 4. Categorical grid / matrix figures (key question)

When a paper needs to show rows = items, columns = conditions, cells = yes/no or pass/fail, there are four standard approaches:

### 4.1 Approach A: Continuous heatmap + values printed in cells (most common)
| Paper | Figure | Content | Visual form |
|-------|--------|---------|-------------|
| Wan 2024 | **Fig. 4a** | 40+ peptides × 11 strains MIC | blue-white-red diverging, cells print 4, 8, 16, 32... |
| Wan 2024 | **Fig. 5e** | peptide pair FICI synergy index | 3-class blocks (dark blue=Indifferent, light gray=Additive, dark red=Synergistic) + cell values |
| Cell 2024 | **Fig. 6B/C** | 100 peptides × 19 strains MIC | orange-brown sequential, cells print 32/64/128/256 μM |
| Huang 2023 | **Fig. 2b** | 4 model confusion matrices | color depth = sample count |
| Sidorczuk 2022 | **Fig. 3** (Brief Bioinform 23:bbac343) | 12 architectures × 11×11 sampling method matrix | 12 small-multiples heat maps, red-orange-yellow scale + black dot size = SD |

Key observation: even essentially binary antimicrobial activity is encoded as a continuous color scale (MIC magnitude), not a simple "active / inactive" two-color block.

### 4.2 Approach B: Solid / hollow dot matrix (binary matrix)
- **Diff-AMP (Wang et al. 2024, Brief Bioinform 25:bbae078), Fig. 6**:
  - Rows = 8 AMP samples (A, B, C, Real_1, D, E, F, Real_2)
  - Columns = 20 attributes (antibacterial, anti-Gram+, anti-Gram−, antifungal, antiviral...)
  - Cells = **solid light-purple circle = has attribute, hollow circle = no attribute**
  - A dashed box highlights the region where "generated AMPs have broader spectrum than real AMPs."
  - This is the typical way Briefings in Bioinformatics shows "which samples have which attributes."

### 4.3 Approach C: Diamond decision flowchart (Yes/No on arrows, colored terminal boxes)
- **HydrAMP Fig. 6c** (Nat Commun 2023): MD1 → diamond "Is S > 0.5?" → Yes/No text arrows → green box "Active AMP" / purple box "Inactive AMP" → second MD2 diamond.
- **Huang 2023 Fig. 1b**: decision tree "Electropositive?" → Yes/No → "Amphiphilic structure?" → Yes/No → final "Potential AMP library" or "Abandoned."
- Yes/No written on arrows, no checkmarks / crosses.

### 4.4 Approach D: Clean three-line table (text yes/no, no symbols)
- **DOME (Walsh et al. 2021, Nat Methods 18:1122), Table 1**: concerns → consequences → recommendations, three columns, formal three-line table style.
- **MIQE (Bustin et al. 2009, Clin Chem 55:611), Table 1**: each item graded with **E (essential) / D (desirable)** letter, no checkmark symbols.
- **ARRIVE 2.0 (Percie du Sert et al. 2020, PLoS Biol 18:e3000410), Table 1/2**: three-line tables.
- **Sidorczuk Table 1/2**: sampling method summary, yes/no written as text "yes" / "no."
- **García-Jacas Table 4** (Brief Bioinform 23:bbac094): diversity values, missing values marked with "–".

### 4.5 Verdict on hand-drawn "boxed table with ✓/✗"
**Not recorded in the selected examples.** This includes:
- Nature BME: Das 2021, Huang 2023, Wan 2024 — no ✓/✗.
- Briefings in Bioinformatics: Diff-AMP 2024, García-Jacas 2022, Sidorczuk 2022 — no ✓/✗.
- NatComm / Cell / Science: HydrAMP, AMPSphere, ESMFold — no ✓/✗.
- DOME / FAIR / MIQE / ARRIVE 2.0 — no ✓/✗.

The observation does not establish a venue-wide prohibition. Prefer the form that communicates the measured quantities clearly at final publication size.

---

## 5. Schematic / workflow / checklist figures

### 5.1 Standard visual language
Simple vector diagrams are a useful default; the examples below include other forms, so they do not establish a universal ban on 3D or varied shapes.

| Paper | Figure | Description |
|-------|--------|-------------|
| Das 2021 | **Fig. 1** | Ultra-wide timeline banner, 7 gray rectangular blocks (Data → Autoencoder → ... → Discovery), white text, gray arrows, last block slightly darker teal. Time labels (7 d, 2 d, 1 d...) above each block. |
| Huang 2023 | **Fig. 1a** | Horizontal 6-stage pipeline, each stage an equal-size 3D cube block. Colors: gray (empirical screen) → dark blue (XGBoost) → gold (LSTM) → red (wet lab) → green (target product). Simple sketch icons. |
| Wan 2024 | **Fig. 1** | Top: horizontal geologic timeline (Pleistocene → Holocene), 20+ extinct animal gray silhouettes, colored dashed arrows. Bottom: horizontal workflow text labels + protein structure renders (PyMOL) + colored dots. |
| HydrAMP 2023 | **Fig. 1** | White background; light gray trapezoid/rectangle blocks (Encoder, Decoder, Classifier); colored thick arrows for data flow (pink/yellow/blue/gray); top three gray rounded rectangles for data sources. |
| AMPSphere 2024 | **Fig. 1A** | Thick black arrows linking data pipeline (63,410 metagenomes → ... → AMPSphere), numbers written upstream of arrows. |
| ESMFold 2023 | **Fig. 2A** | Three-stage horizontal architecture: LM → Folding trunk → Structure module, arrows for information flow. |
| Diff-AMP 2024 | **Fig. 1** | Multi-module layout (A–H), rectangles + hexagons + ellipses + arrows, light blue main tone, light green (data), light purple (attention), orange (arrows). |
| Sidorczuk 2022 | **Fig. 1** | Shape semantics: hexagon=model, rectangle=dataset, ellipse=sampling method, parallelogram=architecture, cloud=result. Training set blue, benchmark set red, model orange. |

### 5.2 DOME / FAIR / MIQE / ARRIVE checklist figures
**The cited checklists use text or tables.** Examples are:

| Paper | Checklist carrier | Form |
|-------|-------------------|------|
| DOME (Walsh 2021, Nat Methods) | Box 1 + Table 1 + Suppl. Table 1 | text box + three-line table |
| FAIR (Wilkinson 2016, Sci Data 3:160018) | Box 2 | pure numbered text list F1–R1.3 |
| MIQE (Bustin 2009, Clin Chem) | Table 1 | three-line table + E/D letter grading |
| ARRIVE 2.0 (Percie du Sert 2020, PLoS Biol) | Table 1 + Table 2 | three-line tables |

### 5.3 If the user wants a "checklist" figure
Choose a carrier appropriate to the content. Two useful options are:

**Option A (recommended): DOME Fig. 2 style conceptual workflow.**
- Left-to-right single-direction workflow, 4 zones (e.g. Data / Optimization / Model / Evaluation for AMP).
- Each zone filled with low-saturation light color: light blue #B8D4E8, light red #E8B8B8, light green #B8D8B8, light yellow #F5EED8.
- Right-angle rectangles, thin arrows, white background.
- Zone titles in text (not a/b/c letters).
- Key formulas or conclusions highlighted with a beige #F5EED8 background box.
- Reference: DOME Fig. 2 (Nat Methods 2021, 18:1122) — classification/regression metrics workflow.

**Option B: Formal three-line table + E/D grading.**
- Make it Table 1 (main text) or Supplementary Table.
- Use E (essential) / D (desirable) letter grading.
- Three-line table, no vertical lines, no color.
- MIQE / ARRIVE 2.0 illustrate this form; it still needs content and layout review.

### 5.4 Common tools
- Protein structure renders: PyMOL (Wan 2024, Diff-AMP).
- Experimental workflow diagrams: BioRender.com (Wan 2024 Fig. 6a,c explicitly credits "created with BioRender.com").
- Data charts: matplotlib / seaborn.

---

## 6. Full paper list
| # | Paper | Venue | Figures verified |
|---|-------|-------|-----------------|
| 1 | Das et al. 2021, Accelerated antimicrobial discovery via deep generative models | Nat Biomed Eng 5:613 | Fig. 1/4 ✅ |
| 2 | Huang et al. 2023, Identification of potent AMPs via ML pipeline | Nat Biomed Eng 7:797 | Fig. 1/2 ✅ |
| 3 | Wan et al. 2024, Deep-learning antibiotic discovery through molecular de-extinction | Nat Biomed Eng 8:854 | Fig. 1/2/4/5 ✅ |
| 4 | Szymczak et al. 2023, HydrAMP | Nat Commun 14:1453 | Fig. 1–7 ✅ |
| 5 | Santos-Júnior et al. 2024, AMPSphere | Cell 187:3761 | Fig. 1/2/3/6 ✅ |
| 6 | Lin et al. 2023, ESMFold | Science 379:1123 | Fig. 1–4 ✅ |
| 7 | Wang et al. 2024, Diff-AMP | Brief Bioinform 25:bbae078 | Fig. 1/3/6/7 ✅ |
| 8 | García-Jacas et al. 2022, Do deep learning models make a difference in AMP identification? | Brief Bioinform 23:bbac094 | Table 4 ✅ |
| 9 | Sidorczuk et al. 2022, Benchmarks in AMP prediction are biased | Brief Bioinform 23:bbac343 | Fig. 1–3 ✅ |
| 10 | Walsh et al. 2021, DOME recommendations | Nat Methods 18:1122 | Fig. 1/2 ✅ |
| 11 | Wilkinson et al. 2016, FAIR Guiding Principles | Sci Data 3:160018 | Box 2 ✅ |
| 12 | Bustin et al. 2009, MIQE | Clin Chem 55:611 | Table 1 ✅ |
| 13 | Percie du Sert et al. 2020, ARRIVE 2.0 | PLoS Biol 18:e3000410 | Table 1/2 ✅ |
