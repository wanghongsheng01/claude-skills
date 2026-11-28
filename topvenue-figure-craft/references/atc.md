# USENIX ATC: observed figure profile

Sample: Cost-Efficient LLM Serving for Multi-turn Conversations with CachedAttention (ATC'24, Fig. 1, 3, 5);
On-demand container loading for serverless functions (ATC'23, Fig. 1, 3, 7);
Transactional Stateful Serverless Workflows with Affinity-Aware Leasing (ATC'25, Fig. 1, 3, 6);
TGW: Operating an Efficient and Resilient Cloud Gateway at Scale (ATC'25, Fig. 1);
counter-examples: Data Caching for Enterprise-Grade Petabyte-Scale OLAP (ATC'24, Fig. 1, 3) and
Distributed Transactions at Scale (ATC'23, Fig. 1, 2).

## Profile
- **Figure 1 types vary.** Academic papers lean towards motivating measurements: a 100% stacked overhead breakdown, or a
  concept sketch combined with a measurement. Industry and operations papers lean towards a background architecture of the existing system.
  The most persuasive figure is often Fig. 2–3, for example the CachedAttention before/after token grid.
- **Single column**, 120–200 pt tall. Full-width figures are rare and are often low-density counter-examples.
- **Tools:** diagram software with its default pastel palette, slide software, and matplotlib/ggplot for data. Text is 5–8 pt (0.5–0.8× body).
- **Colour:** good figures use one accent (a red dashed shared-memory pool, a dark-green reused-KV block). Weak figures use many hues without meaning.
- **Edges: clean orthogonal routing separates figures here.** Even an award-cited paper (container loading, Fig. 3)
  and a 2025 operations paper (TGW, Fig. 1, four thick diagonals crossing the data-plane container) cross containers.
- **Data units as glyphs:** the best mechanism figures draw tokens, keys or table cells, not component boxes.

## Transferable practices
1. To show what caching or reuse saves, draw before/after columns of identical, aligned data units and change only saturation and bracket ranges.
2. For a motivating figure, use a 100% stacked bar with a sequential palette, the attacked overhead darkest. Say in the caption that the baseline is well tuned.
3. Control-plane/data-plane figures: one container per plane, dashed = control and solid = data. **Align the two endpoints of every cross-plane
   message vertically so the edge crosses the container edge straight, or end it on the container border.** Never cross a container diagonally.
4. Explain grouping with one small coloured note above a container ("scale: per invoke"), not text inside it.
5. In the architecture, give only the new abstraction an emphasis (tinted region + bold name).
6. In mechanism figures, use a worked example with ❶❷❸ steps and a red frame only on the cells that change.
7. Background figures stay minimal: at most 5 components, one colour.
8. Export vectors; text ≥ 7–8 pt.

## Avoid
Raster exports; rotated labels; low-density full-width figures; diagonals crossing containers or each other;
diagram-software default colours used without meaning; lightning-bolt connectors; mixing emoji or clip-art with line art.

## Lessons from a real Figure 1 redesign (systems gateway / isolation paper)
1. Replace nested box-and-arrow gateway diagrams with an A9 log-log design-space Pareto trajectory plot showing how competing granularities scale across catalog size against a hard protocol/context ceiling while the proposed system anchors the optimal lower-left corner—conveying systems contribution in 5 seconds with zero box crossings.
2. When a systems paper resolves three heterogeneous failure modes with different units (drop %, tail ms, miss %), place them in a companion horizontal bar panel normalized to `Baseline = 100%` severity while printing the exact raw physical values and reduction factors to the right of each bar—eliminating dual-y clutter while preserving full quantitative honesty.
3. Highlight Pareto or optimal zones using borderless softly tinted `Rectangle(..., edgecolor="none")` regions with `>= 4 pt` clearance from adjacent labels and trajectories rather than hard-stroked inner boxes.
4. Set all matplotlib figures in USENIX systems papers to `STIXGeneral` / Times serif (`>= 7.2–8.5 pt`, Type 42 vector embedding), distinguishing curves by filled vs. hollow circles/squares and line styles rather than solid triangle/diamond markers.
5. Place horizontal frameless legends (`frameon=False`) centered in top subplot padding with `tight_layout(rect=[0, 0, 1, 0.96])` instead of corner boxed legends that crowd bar labels.
6. Clear USENIX narrow-column `Underfull \hbox >= 2000` stretches with `[T1]{fontenc}`, upright `enumitem` lists, `\hyphenation{}` proper-noun guards, `\allowbreak` inside long monospace identifiers/inline sets, lifting multi-parameter recurrences to display equations, and wrapping proper nouns / special-symbol terms (e.g., `{$\mu$Kernel}`) in `{...}` in BibTeX for `plain.bst`.
