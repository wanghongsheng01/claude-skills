# ACM ISSTA: observed figure profile

Sample (arXiv versions, acceptance verified from arXiv comments/journal-ref and PDF headers):
AutoCodeRover: Autonomous Program Improvement (ISSTA'24, Fig. 1, 2);
Keep the Conversation Going: Fixing 162 out of 337 bugs for $0.42 each using ChatGPT (ISSTA'24, Fig. 1, 2);
Large Language Models are Zero-Shot Fuzzers: Fuzzing Deep-Learning Libraries via LLMs (ISSTA'23, Fig. 1, 4).

## Profile
- **Figure 1 is a motivating example in all three:** real bug code with oracles in comments, a real bug with a
  red/green diff and test output, or a real issue with the agent's trajectory. Architecture appears on pages 4–6 as "Overview of X".
- **Code is the protagonist:** monospace text, diffs, real identifiers.
- **Overview figures are dense:** icons, pastel background regions, loops, real prompts.
- **Small text is common here (0.43–0.78× body). Do not copy it.**
- **Tools:** diagram software (default pastel palette) and slide software. No TikZ or matplotlib in the sample.
- **Captions are short noun phrases** ("Overview of X"). This is an easy place to stand out.
- **Colour discipline in the good figures:** only I/O nodes or stage transitions are coloured. Red means bug, mutation or new data flow.

## Transferable practices
1. **Figure 1 = a minimal reproducing example:** one real or plausible program or query, each implementation's output written as a comment
   or side-by-side result, marked wrong/correct. No pipeline in Figure 1.
2. For repair or transformation work, use red/green diff lines and link the evidence string to the answer string with the same emphasis.
3. In overview figures, use **uncoloured pastel background regions without strokes**, at most 3 thick accent arrows for stage jumps,
   and thin black orthogonal arrows inside regions. This removes edges crossing container borders altogether.
4. Put real code or data snippets inside nodes and colour the mutated or compared token.
5. Use the caption to stand out: open with the claim ("Existing oracles miss X because …; our oracle exposes it via …").
6. Text ≥ 0.75× body (about 7 pt in acmart); code about 7 pt.

## Avoid
Curved arrows crossing panel borders or looping outside; 4–5 pt text walls; comic fonts or emoji for code or roles; typos in figures;
diagonal arrows; sub-figures a)/b) with no corresponding emphasis.

## Lessons from a real Figure 1 redesign (software testing / differential conformance paper)
1. Replace generic "pipeline on top + running example below" rounded-box templates with a native TikZ A6 minimal reproducing code + diff + differential-oracle witness figure: real numbered code lines, highlighted bug lines, `-`/`+` mutation diff, inline oracle-vs-code verdict, and a 3-number bottom bar—zero stacked rounded boxes.
2. Inside `acmsmall` (`13.88 cm` text width), draw native TikZ code figures at exact `13.40 cm` physical width (zero `\resizebox`), loading `[T1]{fontenc}`, aligning rows with `anchor=base west`/`base east`, and indenting monospace code via `\phantom{\texttt{xxxx}}` so typography matches the Libertine/Biolinum/Inconsolata body seamlessly.
3. For borderless tinted code-highlight bands in TikZ, keep single-line band height `>= 0.48 cm` (`>= 0.49 cm` with superscripts/descenders), `0.08–0.10 cm` white gap between stacked bands, `>= 0.10–0.12 cm` horizontal clearance from line-number vertical hairlines, and `>= 0.18 cm` between the bottom heavy rule and the last baseline so PDF geometry audits report `0 FAIL, 0 WARN`.
4. On log-x cost–recall Pareto scatter plots where baselines cluster within one decade, distribute labels by quadrant (low scores below, mid-left to the left, high scores above, rightmost high-cost inward) and audit matplotlib scripts in `run` mode to achieve zero label-arrow and label-label collisions.
5. Set matplotlib `font.family = 'STIXGeneral'` (`mathtext.fontset = 'stix'`) across all figures in `acmart` SE papers, reserve one high-saturation accent color strictly for the proposed tool while muting baseline groups to desaturated blue-gray, and replace solid triangle/diamond markers with circles and squares.
6. Load `enumitem` with `\setlist[enumerate]{label=\textup{(\arabic*)}}` for upright labels inside italic Definitions/Theorems and add `[beginpenalty=10000]` on post-intro contribution lists whenever a native TikZ Figure 1 floats to the top of page 3 so lead-in sentences never orphan at the bottom of page 2.
