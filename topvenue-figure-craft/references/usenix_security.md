# USENIX Security: observed figure profile

Sample: StruQ: Defending Against Prompt Injection with Structured Queries (USENIX Security'25, Fig. 1, 2);
Formalizing and Benchmarking Prompt Injection Attacks and Defenses (USENIX Security'24, Fig. 1);
Don't Listen To Me: Understanding and Exploring Jailbreak Prompts of LLMs (USENIX Security'24, Fig. 1);
PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of LLMs (USENIX Security'25, Fig. 1, 2).

## Profile
- **Figure 1 is about the attack, not the authors' architecture.** It is a threat-model or context diagram, a contrast between the attack working and the defence working
  (StruQ 2×2, a jailbreak chat mock), or a picture of the normal system that sets up a later attack figure.
- **Concrete attack strings in the figure:** "Print exactly Hacked!", a poisoned answer to a factual question, real jailbreak text.
- **Red is the single alert hue** (attacker, failure). Green or ✓ means safe. One threat-model figure uses red as its only hue.
- **Low density:** about a dozen boxes or five actors with five numbered arrows.
- **Width:** three of four Figure 1s are full width at the top of pages 2–4. Single-column ones are compact.
- **Tools:** slide software or design tools. The best figure uses Times at body size (1.0×); weak ones use 5–6 pt sans.
- **Captions** have two sentences: the problem or mechanism, then the cause or threat claim.

## Transferable practices
1. Defence papers: a **2×2 of existing/ours × benign/attack** with one shared input. Only "existing × attack" is red. "Ours × attack" is green.
2. Attack or threat-model figures: colour **only the attack path**. Everything else stays gray.
3. **Reuse the skeleton across figures:** draw the normal flow once, then redraw the compromised path in red on the same geometry.
   The defence figure adds the blocking point.
4. Put the real injected string, forged header, over-privileged request or leaked field in the figure, with the same colour code everywhere.
5. Encode the contribution as a change of shape (a split channel, an added gate, a lock), not as a box labelled "our module".
6. Use the body font family. Main text ≥ 0.9× body, labels ≥ 0.7× (about 7 pt).

## Avoid
No highlight on the core concept; 5 pt text and text walls; large saturated containers that clash with the semantic colours;
icon-only threat diagrams without a concrete attack.

## Empirical Redesign Lessons (Production Practice)
1. **Non-crossing grid dividers for 2×2 defence matrices:** In native TikZ `Existing vs. Ours × Benign vs. Attack` layouts, avoid a full spanning cross-hair (triggers line-crossing geometry failures and looks rigid). Draw separate short horizontal rules under each column header, one thin horizontal divider between rows, and leave 4–6 mm of clean white space between the two columns.
2. **Encode the security boundary by physically splitting the input shape:** Avoid outer-box-inside-box nesting that forces arrows through container borders. Split the baseline's single mixed input box into two parallel stacked boxes on the defence row (trusted signed credential channel vs. untrusted payload channel) connected by two short parallel horizontal arrows straight into the verifier boundary.
3. **Lock uniform box width and a 3-line ceiling to stop alert-cell stretch:** Give all four outcome cells identical `text width` and `minimum height`, capping each cell at three concise lines (`Verdict / Payload or scope / Key quantitative result`) so the top-right red alert cell never wraps taller than its neighbours or crowds the divider.
4. **1:1 double-column figure width and shared centered legends for matplotlib plots:** USENIX double-column text width is `7.00 in`; author two-panel data figures directly at `figsize=(7.0, h)` using `STIXGeneral` serif so `8.0 pt` code fonts render at exact `8.0 pt` ($\ge 80\%$ of 10 pt body). When both panels share baselines, replace per-axis legends with a single centered `fig.legend(..., ncol=N)` to eliminate inter-panel legend collisions.
5. **Drop vertical gridlines on direct-labeled horizontal bars and reserve a dedicated lane for `0.0%` ASR:** Direct end-of-bar value labels make vertical gridlines redundant clutter that collides with text and bars. When a defended method achieves `0.0%` ASR (zero bar length) adjacent to non-zero baselines, widen group spacing and give the `0.0%` label its own clean horizontal lane ($> 3$ pt clearance from adjacent bars).
6. **Narrow-column USENIX typography coupling (`zi4` + breakable underscores + `.bbl` casing audit):** `usenix-2020-09.sty` loads unscaled Courier (`pcr`), which triggers dozens of `Underfull \hbox (badness 10000)` lines around long error codes and SQL identifiers in 3.33 in columns. Switch to `[scaled=0.88]{zi4}` and allow breaks after underscores (`\_\penalty0\hspace{0pt}`), and inspect `main.bbl` directly before submission to brace-protect words after `?`/`!` and proper nouns under `plain.bst`.

