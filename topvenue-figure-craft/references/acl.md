# ACL (ARR main conference): observed figure profile

Sample (aclanthology.org, *.acl-long): When Not to Trust Language Models: Investigating Effectiveness of Parametric and Non-Parametric Memories (ACL'23, Fig. 1, 2, 9);
RARR: Researching and Revising What Language Models Say, Using Language Models (ACL'23, Fig. 1, 2);
Don't Hallucinate, Abstain: Identifying LLM Knowledge Gaps via Multi-LLM Collaboration (ACL'24, outstanding paper, Fig. 1, 2);
Astute RAG: Overcoming Imperfect Retrieval Augmentation and Knowledge Conflicts for LLMs (ACL'25, Fig. 1, 4);
Blinded by Generated Contexts (ACL'24, Fig. 1, 3).

## Profile
- **Two stable forms.** (i) A **page-1 right-column teaser:** single column (about 219–232 pt wide, 120–265 pt tall), next to the abstract, vertical or a single plot.
  (ii) A **full-width overview at the top of page 2 or 3** (about 456–465 pt). No paper puts a full-width figure on page 1.
- **Evidence or phenomenon first:** of the five Figure 1s, two are real measurement plots with annotations, one is a 2×2 table of real statistics,
  one is a task-definition teaser with a running example, and only one is an architecture. Method figures come at Fig. 2–4.
- **Example-driven, with coloured spans:** every paper shows a real text instance and colours only the deciding tokens
  (subject/relation/object backgrounds; red strikethrough + green bold for edits; blue = correct, red = wrong answer words).
- **Colour:** 2–4 functional hues plus grays. Emphasis by saturated vs tinted (only the selected bar is saturated), a single coloured method box,
  one conclusion colour at the end of the path ("Abstain"), or black bold vs gray italic.
- **Tools:** slide software exports; data plots from matplotlib, then annotated. Text is commonly 5–8 pt against an 11 pt body (0.5–0.75×). The best are 7–9 pt.
- **Captions:** a bold title sentence; or a description followed by a fully bold take-away; colour words in the caption decode the figure.

## Transferable practices
1. **Page-1 teaser = single column, vertical, ≤ 1/3 page tall**, about the phenomenon or task. Method architecture goes on p2–p3, full width.
2. Prefer **real data** (a measurement bar chart or a 2×2 statistics table) plus 1–2 conclusion call-outs, which turns a measurement into an argument.
3. Carry **one real text instance** and colour only the deciding tokens.
4. **Ours is the only saturated or gradient element.** Prior and background elements are tinted, gray, gray italic or dashed.
5. Region titles are full claims or "state ⇒ action", so the figure reads without the caption.
6. The caption's first sentence (bold) gives the task or conclusion and **names colours in words**, so no legend is needed.
7. Symbols (x, y, A, q) match the text and sit next to their boxes.
8. Two dual methods → mirrored left/right panels with a shared top row.

## Avoid
Text < 6 pt (aim for ≥ 7 pt); a full-width architecture or multi-panel pipeline on page 1; piles of raster icons; decorative colours with no meaning;
long loop-back connectors (use numbered panels or regroup repeated elements to show iteration).
