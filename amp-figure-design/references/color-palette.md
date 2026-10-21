# Color palette reference

All hex values extracted from published AMP / protein-generative-model figures.

## Categorical / method colors (use one per method, reuse across all panels)

| Role | Hex | Source |
|------|-----|--------|
| Main method / protagonist | `#D2691E` (ochre-terracotta) | Das 2021, Wan 2024 |
| Comparison method B | `#4682B4` (medium blue) | Das 2021 |
| Baseline / neutral | `#808080` (neutral gray) | Das 2021 |
| Highlight / red | `#B2182B` (brick red) | Wan 2024 Fig. 5e |
| Deep teal | `#2C7A7B` | Wan 2024 baselines |
| Light green | `#90BE6D` | Wan 2024 baselines |
| Light blue | `#7FB3D5` | HydrAMP Basic |

## Heatmap scales

### Diverging (for MIC, dual-direction)
Low → mid → high:
```
#2166AC (deep blue) → #F7F7F7 (near white) → #B2182B (brick red)
```
Source: Wan 2024 Fig. 4a (40+ peptides × 11 strains MIC).

### Sequential orange-brown (for one-direction values)
Low → high:
```
#FFF7E6 (cream yellow) → #F4A460 (sandy brown) → #8B4513 (saddle brown)
```
Source: AMPSphere / Cell 2024 Fig. 6B/C.

## Schematic / workflow zone colors (low-saturation macaron)

| Zone | Hex | Source |
|------|-----|--------|
| Data / input zone | `#B8D4E8` (light blue) | DOME Fig. 2 |
| Model / method zone | `#E8B8B8` (light red) | DOME Fig. 2 |
| Evaluation / output zone | `#B8D8B8` (light green) | DOME Fig. 2 |
| Highlight / formula box | `#F5EED8` (beige) | DOME Fig. 2 |
| Optional 4th zone | `#9B7FB8` (light purple) | DOME Fig. 2 |

## Bar chart primary
`#5B8DC9` (sky blue) — DOME Fig. 1.

## What to avoid
- Neon / fluorescent colors
- High-saturation pure red #FF0000, pure blue #0000FF, pure green #00FF00
- Viridis, plasma, inferno (not used in any surveyed AMP paper)
- Rainbow color scales
