# ACM SIGMETRICS / POMACS: observed figure profile

Sample (arXiv versions; acceptance from arXiv comments or the footer "Proc. ACM Meas. Anal. Comput. Syst."):
Optimistic No-regret Algorithms for Discrete Caching (SIGMETRICS'23, Fig. 1);
Heavy-Traffic Optimal Size- and State-Aware Dispatching (POMACS 8(1), 2024, Fig. 1.1–1.2);
Strongly Tail-Optimal Scheduling in the Light-Tailed M/G/1 (POMACS 8(2), 2024, Fig. 1.1, 1.2);
Outperforming Multiserver SRPT at All Loads (SIGMETRICS'26, Fig. 1, 3);
supplementary systems paper on prefix-cache sharing for LLM serving (POMACS 10(3), Dec 2026, Fig. 1).

## Profile
- **Model visualisation is the protagonist of theory Figure 1s:** not architecture, but *how the policy acts in the model*.
  Examples: a state space split by a threshold line, boost drawn as arrows on a time axis, a sample-path Gantt chart,
  the problem set-up next to the per-round loop.
- **Sketch + evidence pairs:** an intuition figure and an evidence curve side by side on page 1 (Fig. 1.1 + 1.2,
  numbered by subsection). The curve draws the theoretical limit as a dashed line.
- **Restrained colour semantics:** existing state in gray or black, the new event in 1–2 accent colours. The single new element (for example a prediction)
  keeps one colour across all sub-figures.
- **Tools split by role:** mechanism sketches are TikZ (body font, about 9 pt); curves are matplotlib. Setting matplotlib's font to the body font
  looks clearly better than the default. Slide-software figures (4–7 pt, foreign fonts) look weakest.
- **Sub-figure titles are conclusion sentences** ("Boost serves X before Y if their arrival times are far apart"). Captions end with who wins in which case.
- **Proof roadmap:** lemma nodes with bold numbers, a one-line conclusion and magnitude, and a colour band showing the method sections they use.

## Transferable practices
1. Figure 1 = **one concrete action of the policy in the model.** Draw TTLs, leases, boosts and deadlines as directed lengths on a time axis,
   and decisions as "crosses / expires". Use prior | ours-case-1 | ours-case-2 panels that change one parameter.
2. A **policy × future-scenario Gantt grid:** existing state gray, only new events coloured, event instants as same-colour vertical dashes, values inside the bars.
3. **Draw rules in state space:** axes are state variables (queue work, cache occupancy, remaining lease), threshold lines are decision boundaries,
   and actions are written in the regions. A **regime map** with the theoretical boundary plus simulation markers is the data version of this.
4. Put a **sketch | evidence curve** pair of half-width figures on page 1. Draw the theoretical bound in the same colour, dashed; say "lower is better".
5. With 3 or more chained lemmas, add a proof roadmap.
6. Use one font: TikZ is naturally in the body family; set matplotlib's `font.family` to the body font; text ≥ 7–8 pt. Do not shrink a TikZ picture after drawing it.

## Avoid
Saturated default plot colours mixed with highlighter colours; our curve overlapping the baselines (use an inset or log axis); small slide-software text and raster icons;
noun-phrase or duplicated captions; curves leaving the axes without clipping or annotation.

## Lessons from a real Figure 1 redesign (performance modeling / caching paper)
1. Pairing a 2D closed-form regime map (left panel: analytical decision boundary separating gain/over-cost/degenerate regimes overlaid with real workload optima) with an empirical evidence curve anchored to an offline oracle lower bound (right panel: multi-policy tail latency + single bidirectional gap arrow) convinces both theory and systems *POMACS* reviewers in 10 seconds.
2. Match `acmsmall` serif body typography in matplotlib with `STIXGeneral` + `mathtext.fontset="stix"`, and position all labels and shared top legends strictly inside `[0, 1] × [0, 1]` via explicit `subplots_adjust` (avoiding implicit `bbox_inches="tight"` cropping) so median text stays `>= 8.2 pt` with zero `TEXT_OUTSIDE_CANVAS`.
3. On dual-y (`twinx()`) plots, hide secondary x-ticks explicitly with `ax_r.tick_params(axis="x", which="both", bottom=False, top=False, labelbottom=False, labeltop=False)` in addition to `ax_r.xaxis.set_visible(False)` to prevent duplicate overlaid bottom tick text.
4. Keep curve callouts collision-free by decoupling `ax.text` in open whitespace from an empty-text short arrow `ax.annotate("", xy=..., xytext=...)` stopping 2–3 pt outside the target curve, and truncate vertical threshold lines below legend boxes so `LEGEND_OVER_DATA` never fires.
5. Replace full 2D gridlines with subtle horizontal-only major gridlines (`yaxis.grid(alpha=0.35)`) and swap filled triangle/diamond markers for circles, squares, or pluses (`o`, `s`, `P`) to keep curves airy and prevent false arrowhead detection in static PDF audits.
6. In long `acmsmall` theory+measurement manuscripts, load `enumitem` with `\setlist[enumerate]{label=\textup{(\arabic*)}, ref=\textup{\arabic*}}` for upright theorem numbering, protect proper names in `\hyphenation{}`, keep method names upright vs. monospace dataset/trace names, and clear all `Underfull \hbox >= 2000` stretches.
