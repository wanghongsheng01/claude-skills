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
