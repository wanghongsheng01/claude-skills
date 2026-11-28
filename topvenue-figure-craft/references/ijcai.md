# IJCAI: observed figure profile

Sample (ijcai.org proceedings): KG-CoT: Chain-of-Thought Prompting of LLMs over Knowledge Graphs for Knowledge-Aware Question Answering (IJCAI'24 main, Fig. 1, 2);
FactCHD: Benchmarking Fact-Conflicting Hallucination Detection (IJCAI'24 main, Fig. 1, 2);
AriGraph: Learning Knowledge Graph World Models with Episodic Memory for LLM Agents (IJCAI'25 main, Fig. 1, 2);
Resolving Conflicting Evidence in Automated Fact-Checking: A Study on Retrieval-Augmented LLMs (IJCAI'25, AI and Social Good track, Fig. 1, 2).

## Profile
- **Figure 1 is usually a problem-driven concrete instance:** (a)(b)(c) panels contrasting the problems; a task teaser instance; opposing motivating instances.
  One uses a concept + result double panel. Three of four Figure 1s are not architectures. The overview is Fig. 2 on pages 3–4.
- **Placement:** single column on the page-1 right column next to the "challenges" paragraph. The full-width Figure 1 sits at the top of page 2. The overview Fig. 2 is full width.
- **Bound to the introduction:** panels (a)/(b) correspond to Challenge 1/2 in the text, and each caption sentence states one challenge.
- **Numbered alignment:** stage labels (1)(2)(3) in the overview match "(1) We first … (2) … (3) …" in the caption.
- **Colour:** the best figure uses 3 light hues + 1 accent with clear meaning (wrong / right / question). Weaker figures use many hues without meaning.
- **Fonts split into two camps:** body-family Times at 7–8 pt (0.75–0.8× body), which looks best, vs mixed sans/comic fonts at 5–7 pt, which looks casual.
- **Decoration:** LLM papers often use icons (robots, avatars, logos, thought clouds). The strongest figure uses none.

## Transferable practices
1. **Figure 1 = the introduction's challenges, visualised:** N challenges + solution as N+1 isomorphic panels on the same input, the last one marked "(Ours)".
   One claim sentence per sub-figure in the caption, using the same names as the text.
2. Mark wrong/right with **light background highlights** (wrong = light orange, right = light green, input = light blue). Body font at about 0.8×; no icons.
3. **Opposing motivating instance:** the same input leads to two conflicting results, mirrored left/right, each with its deciding evidence highlighted
   and opposing verdict labels underneath. Fits differential testing, cache or consistency conflicts, and evidence conflicts.
4. **Concept sketch + result inset** double panel: one new concept on the left, one summary bar chart on the right with ours outlined and an upper-bound reference.
5. **Write the running example into the architecture's module cards** (2–4 monospace lines) instead of a separate example band.
6. Draw the baseline once and show variants only as diffs. New elements get the single accent; unchanged parts are grayed.
7. Show iterations as isomorphic step panels, with the step colour carried through labels, vectors and node outlines. The chosen path is saturated and thick; the rest is faded.

## Avoid
Comic fonts, cartoon emoji and logo piles; mixing four font families; span or background arrows leaving boxes or crossing text;
one saturated colour per baseline in bar charts; "Overview of …" / "Illustration of …" captions; typos.

## Lessons from a real Figure 1 redesign (neuro-symbolic constrained decoding paper)
1. Watch out for `ijcai27.sty` redefining `\footnotesize` to 9 pt (instead of 8 pt in standard `article`): a wide TikZ figure that fits in a standalone preview will crowd once embedded. Either compile previews with the real IJCAI `.sty` or explicitly lock `\fontsize{8}{9.6}\selectfont` (exact 80% of 10 pt body).
2. For sequential neuro-symbolic / state-machine papers, draw an A5 state-transition trellis using subtle gray grid dots instead of full-span horizontal/vertical gridlines, and pick a real trace where the compared trajectories maintain a clean vertical partial order—yielding a strictly planar, zero-crossing contrast between illegal jumps, greedy local traps, and the globally optimal legal path.
3. Avoid filled triangle/diamond markers at polyline endpoints in matplotlib plots: static PDF geometry analyzers interpret 3–4-vertex solid polygons near line ends as arrowheads, triggering false dangling-arrow flags; prefer solid/hollow circles, squares, or hexagons.
4. On horizontal grouped bar charts with end-of-bar value labels, derive row spacing from actual point height (`>= 7.5 pt` per bar pitch), drop redundant vertical gridlines, and place legends strictly inside `[0, 1]` to achieve `0 FAIL` in both `run` and `pdf` audit modes.
5. On Pareto / budget-sweep curves, truncate vertical reference markers to a local dashed delta segment spanning *only* between the baseline and proposed curve at the target budget (preventing full-height `axvline` from cutting through legends), and decouple unboxed whitespace labels from leader lines.
6. Eliminate IJCAI narrow-column `Underfull \hbox >= 2000` stretches by lifting wide inline recurrences into display equations, forcing upright `\textup{(i)}`/`\textup{(1)}` list labels inside theorems, and wrapping `named.bst` bibliographies in `\raggedright` to prevent white-space rivers caused by long hanging `[Author et al., Year]` citations.
