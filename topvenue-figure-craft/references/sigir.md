# ACM SIGIR: observed figure profile

Sample (arXiv versions; acceptance from the ACM Reference Format and DOI in each PDF):
A Setwise Approach for Effective and Highly Efficient Zero-shot Ranking with Large Language Models (SIGIR'24, Fig. 1, 2);
Unbiased Learning to Rank Meets Reality (SIGIR'24, Fig. 1, 2);
Large Language Models can Accurately Predict Searcher Preferences (SIGIR'24, Fig. 1, 2);
counter-example: Evaluating Retrieval Quality in Retrieval-Augmented Generation (SIGIR'24 short, Fig. 1).

## Profile
- **Figure 1 shows evidence or positioning, not architecture.** Two page-1 teasers are data plots: error bars showing "no method beats the naive one",
  and a cost × quality positioning plot. One is a prompt-paradigm comparison grid (page 2, full width). None is a system diagram.
- **Placement:** page-1 teasers sit in the **right column**, because the ACM template fills the left column with authors, CCS concepts,
  keywords and the reference block. Single column about 241 pt wide, 150–190 pt tall. Full-width paradigm grids are flat (about 130 pt) at the top of page 2.
- **Fonts close to body size:** strong figures use 7.5–9 pt (body 9 pt), often in the body serif. The counter-example uses 5–6 pt default plot style.
- **Few colours:** one point colour; three role colours; gray + one red. **Emphasis by position** (best corner, end of grid), structural difference
  (one extra output branch) and bold labels.
- **Tools:** many raster exports from slide software, some vector charts; LaTeX-native prompt figures.
- **Captions are bold in acmart**, so a conclusion-first caption is especially strong.

## Transferable practices
1. **Page-1 right-column teaser = problem evidence:** a minimal measurement (error bars, scatter, trade-off) and a bold caption whose first sentence is the claim.
2. Contribution is a better trade-off → **positioning plot**: ours in the best corner with a bold label, one bold prior, everything else one colour.
3. Contribution is a new prompting or ranking paradigm → **isomorphic grid**: one "input → LLM → output" grammar for prior and ours. Ours goes last and has the extra capability.
4. Show efficiency as **sequence length**: the same initial state, a prior row vs our row, a dashed outline marking one LLM call.
5. Text ≥ 7.5 pt (0.85–0.95× body) in the body family.
6. Keep role colours fixed across the paper (input gray / model blue / output orange); ≤ 3 colours + gray.
7. Place out-of-range reference points outside the axes with an arrow instead of compressing the axis.

## Avoid
Default plotting styles pasted as is (gray grid, legend over axis label, 5–6 pt); one colour per method with no meaning; low-resolution rasters
(≥ 300 dpi effective if raster at all); large gray text blocks in Figure 1; a full-width architecture on page 1.

## Lessons from a real Figure 1 redesign (IR empirical motivation scatter paper)
1. When placing a single-column A1 motivating scatter plot at the top of page 1 (right column) in ACM `sigconf`, explicitly cite Figure 1 inside the opening Introduction paragraph directly below it so `float_proximity_audit` records exact same-page proximity (`p.1 -> p.1, delta=0`).
2. Put global correlation statistics and sample size (`Spearman ρ = ..., p = ... · N items`) cleanly on a single subtitle line above the axes rather than inside the scatter canvas, keeping the plot interior free of boxed legends or outlier label collisions.
3. On `twinx()` dual-y sensitivity curves, never call `ax2.set_xticks([])` (which clears the shared bottom axis ticks on `ax1`); instead hide only secondary tick labels (`ax2.tick_params(axis="x", which="both", bottom=False, labelbottom=False)` plus `lbl.set_visible(False)` for `ax2.get_xticklabels()`).
4. On horizontal grouped bar plots, keep each bar height near ~20% of group pitch with `>= 3 pt` intra-group gap and center dashed group dividers inside the open gap so end-of-bar value labels clear adjacent borders cleanly.
5. When switching matplotlib to `STIXGeneral` (to match `acmart`'s Linux Libertine), check stderr for `Glyph missing` warnings on decorative Unicode characters like `★` (U+2605) and replace them with standard ASCII/STIX text or math symbols for zero fallback glyphs.
6. Use filled vs. hollow circles and squares (`o`/`s` + `mfc="white"`) instead of solid triangles/diamonds on Pareto scatter plots, and turn off background gridlines behind directly annotated bars/scatters.
