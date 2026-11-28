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
