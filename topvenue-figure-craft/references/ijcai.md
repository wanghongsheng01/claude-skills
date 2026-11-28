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
