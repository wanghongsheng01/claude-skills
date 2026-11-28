# USENIX OSDI: observed figure profile

Sample: DistServe (OSDI'24, Fig. 1, 6); Anvil: Verifying Liveness of Cluster Management Controllers (OSDI'24, Fig. 1, 5, 6);
ServerlessLLM (OSDI'24, Fig. 1, 2); Take Out the TraChe: Maximizing (Tra)nsactional Ca(che) Hit Rate (OSDI'23, Fig. 1, 2, 5);
Llumnix (OSDI'24, Fig. 1). Open-access PDFs: usenix.org/system/files/osdi2X-<author>.pdf.

## Profile
- **Figure 1 proves the problem; it is rarely the architecture.** Four of the five Figure 1s were a measurement with a threshold
  (DistServe), a success/failure dual timeline (Anvil), a three-node counterexample (TraChe) or small multiples
  (Llumnix). Architecture figures come in §3–4 as Fig. 5–8.
- **Single column**, about 240 pt wide and 120–200 pt tall. Full width is used only for staged system overviews (TraChe Fig. 5).
- **Numbers as the only annotation:** "rps = 1.6 / 5.6 / 10", "51% diff.".
- **Colour:** 3–4 light hues plus black and gray, all with meaning (who wrote it, which phase). Red only for violations (Anvil).
- **Tools:** mostly slide software and matplotlib; small TikZ sketches for minimal examples. Figure text is
  5.5–7.5 pt against a 10 pt Times body (0.55–0.75×). The best figures use Times inside the figure.
- **Edges:** in good figures, orthogonal or short straight edges leave box-side midpoints. Diagonals appear only for fan-out.
  Counter-example: ServerlessLLM Fig. 1, where four contribution leader lines cross each other.
- **Captions** are mostly descriptive. The strongest pattern is a bold first sentence with the claim, followed by a sentence on generality (Anvil).

## Transferable practices
1. Figure 1 answers "what is the problem and how bad is it": a measurement reduced to 1–3 numbers, or a correct-vs-failing dual timeline of one minimal real example.
2. Split overview figures by stage or responsibility (compile/run, control/data). Put panel titles where no edge enters.
3. Under each step box, show a tiny concrete artifact (toy data) instead of a sentence.
4. Use two line weights for two relations and declare them in a legend. Fan-out is the only place for diagonals.
5. Use one emphasis device for the contribution (one coloured, bold or double-framed box). Everything else stays white or light gray.
6. When mapping contributions onto an existing system, order the contribution boxes by their target's horizontal position so the leader lines run vertically and never cross.
7. Use numbered badges that match section numbers or code lines.

## Avoid
A large generic boxes-and-arrows architecture on page 1 with no data or contrast; crossing leader lines; labels on lines;
text below 6 pt; a sentence inside every box; many colours without meaning.
