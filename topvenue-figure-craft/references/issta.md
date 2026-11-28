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
