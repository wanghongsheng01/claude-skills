# ICML: observed figure profile

Sample (PMLR open access): Language Models with Conformal Factuality Guarantees (ICML'24, Fig. 1, 2);
Fast Inference from Transformers via Speculative Decoding (ICML'23, Fig. 1, 2, 5);
C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models (ICML'24, Fig. 1, 2);
EAGLE: Speculative Sampling Requires Rethinking Feature Uncertainty (ICML'24, Fig. 1, 6, 7).
Note: some PMLR direct PDF links return an HTML 404; the proceedings repository mirror serves the same files.

## Profile
- **Four papers, four archetypes:** insight sketch (LM outputs ↔ nested confidence sets), concrete execution trace (one row per iteration, only new tokens coloured),
  annotated two-stage architecture with numbered guarantees, and a headline result teaser (bars before the abstract).
  Idea papers draw equivalences or traces. Only system-like papers draw architecture.
- **Width:** half single column (page-1 right column next to the abstract), half full width at the top of page 1 or 2.
- **Mathematical notation in the figure:** the core definition (E(y) := {y′ : y′ ⇒ y}), the estimators, even "Theorem 1: …".
  The figure becomes the visual definition that later theorems use.
- **Numbers:** result teasers label every bar ("3.07x"). Concept figures carry mechanism numbers ("5 tokens in one call"), not experiment numbers.
- **Colour:** the best two figures use 2–3 semantic hues for one binary or ternary state (correct/wrong, accepted/rejected/corrected).
  A 5-hue figure works only because each hue has a role and an in-figure note.
- **Caption as legend:** coloured words in the caption replace the legend box.
- **Tools:** slide software for concepts, matplotlib for results. Strong figures 7–9 pt (body 10 pt); weak ones 5–6 pt.
- **Captions:** the best first sentence is the claim ("Conformal factuality uses conformal prediction to ensure the correctness of LM outputs."). Many waste it on "Overview of X".

## Transferable practices
1. First ask whether the contribution is a system, a reformulation or a number. A reformulation gets an **insight sketch** (user view ↔ mathematical view),
   a number gets a result teaser, and only a system gets an architecture. Guarantee or theory papers should not draw a pipeline.
2. **Write the core definition or guarantee into the figure.** Number the problem → input → output → guarantee steps (1)(2) consistently in figure and caption.
3. **Traces beat block diagrams** for step-wise algorithms (iterative verification, decoding, differential testing): one row per step, only the increment coloured.
4. Colour encodes **one semantic dimension**, ≤ 3 hues, named in the caption.
5. Theorem-heavy papers add a **proof roadmap**: solid boxes for definitions, dashed boxes for theorems, arrows for dependencies, section numbers on bands.
6. Latency claims use **aligned wall-time bars**, where length is the result.
7. In result teasers, put ours first in the only saturated colour, label bar tops, and state the fairness limits of the comparison in the caption.

## Avoid
The generic "pipeline on top, running example below" template for idea or theory papers; cartoon emoji or logos; 5 pt default plot text, primary RGB colours,
duplicated axes, overlapping bar labels; full-width content squeezed into one column (leading to 5 pt text and dashed arrows crossing containers); "Overview of X" as the first sentence.

## Lessons from a real Figure 1 redesign (statistical ML / risk-control theory paper)
1. Replace boxed workflow diagrams with an A5/A13 two-panel concept-plus-evidence figure: left panel draws the exact mathematical partition (e.g., discrete boolean/stratum lattice with one accent hue for supported strata, neutral gray hatching `///` for zero-support strata, one alert hue for a high-confidence out-of-support failure, and two flat formula cards); right panel plots real multi-seed coverage collapse vs. shift magnitude directly from JSON with direct end-of-curve labels (no legend box).
2. Align target lattice cells along the rightmost column of the grid and connect horizontal orthogonal arrows with `shrinkA=0, shrinkB=0` anchored cleanly on cell/card borders—eliminating cross-cell routing and `DANGLING_ARROW` alerts in one stroke.
3. Match ICML two-column full width 1:1 (`6.75 in`) with `8.0–9.2 pt` readable text (`>= 80%` of 10 pt body), and set `font.serif = ["Times New Roman", "Times", "STIXGeneral"]` with `mathtext.fontset = "stix"` so equations render in STIX math while bold percentage labels stay upright Times rather than falling back to bold-italic.
4. Keep multi-column top legends strictly inside `[0, 1]` via explicit `subplots_adjust(top=0.77..0.86)` + `bbox_to_anchor=(0.5, 0.99)` (eliminating `TEXT_OUTSIDE_CANVAS`), and replace solid triangle/diamond markers with `o/s/X/P/p/h`.
5. In grouped horizontal bar charts split by a dashed divider (e.g., tabular vs. LLM benchmarks), widen the inter-group gap (`+0.65` offset -> `1.65` channel) and add `>1` unit of top `ylim` headroom for threshold labels (`\alpha=0.05`) so divider lines and threshold labels stay `>6 pt` clear of bar values.
6. On `loglog` scaling plots, extend the lower y-limit by half a decade to open a clean legend corridor beneath the lowest curve, set inset backgrounds to opaque white (`alpha=1.0`), and verify every mathematical subscript inside Figure 1 matches prose notation verbatim (`figure_formula_consistency_audit` `0 FAIL`).
