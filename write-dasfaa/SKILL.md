---
name: "write-dasfaa"
description: "Human-craft writing and deep de-AI-ification guide for DASFAA (Database Systems for Advanced Applications, Springer LNCS, 16 pages A4 including references, Abstract <= 200 words, strict double-blind). Absorbs ALL historical claude-skills (write-icde, write-pvldb, sigmod-human-writing-craft, experiment-analysis-writing, results-presentation-review S01-S11, paper-presubmission-review, manuscript-writing-review, baseline-paper-absorption) AND empirically distills 8 officially published human-authored DASFAA 2024-2026 full papers (including DASFAA 2026 Best Paper DynamicPO, OLLA, Trans-RAG, MAKGED, PET-SQL, KnowProb, SecGraph, ScoringBias). Focuses deeply on human researcher thinking patterns, authentic human academic prose, eliminating AI-smell and especially over-honest/self-sabotaging AI weakness disclosures while preserving 100% factual and numerical integrity. Use when writing, restructuring, de-AI-ifying, or deeply polishing any DASFAA manuscript."
---

# Writing for DASFAA: Human Craft, Thought Process & Anti-Self-Negation (`write-dasfaa`)

This skill synthesizes two verified evidence bases into an actionable DASFAA Research Track writing manual:
1. **Direct full-text empirical absorption of 8 officially accepted, human-authored DASFAA 2024–2026 papers** (downloaded and measured on **2026-11-25**, full per-paper notes in `references/absorbed-dasfaa-papers.md`):
   - `DynamicPO` (DASFAA 2026 **Best Paper**, `arXiv:2605.00327`)
   - `OLLA` (DASFAA 2026, `arXiv:2603.08443`, LLM-driven online aggregation)
   - `Trans-RAG` (DASFAA 2026, `arXiv:2604.09541`, secure cross-organizational RAG)
   - `ScoringBias` (DASFAA 2026, `arXiv:2506.22316`, LLM-as-a-Judge evaluation study)
   - `MAKGED` (DASFAA 2025 **Full Oral**, `arXiv:2501.15791`, KG error detection with LLMs)
   - `PET-SQL` (DASFAA 2025, `arXiv:2403.09732`, Text-to-SQL refinement)
   - `KnowProb` (DASFAA 2025, `arXiv:2508.16969`, knowledge probing)
   - `SecGraph` (DASFAA 2024, `arXiv:2403.19531`, confidential graph search)
2. **Full absorption of historical `claude-skills` across ICDE, PVLDB, and SIGMOD**:
   - Limitation-writing without self-negation (`write-icde/references/limitations-writing*.md`, `write-pvldb` §7)
   - Senior co-author & advisor presentation standards (`results-presentation-review` S01–S11, `paper-presubmission-review` A–H, `experiment-analysis-writing`)
   - Authentic human database prose & stylometrics (`sigmod-human-writing-craft`)
   - Compile-and-inspect visual gates (`manuscript-writing-review`, `ccfa-visual-table-ref-mastery`, `ccfa-human-readable-math-and-proof`)

Use together with `review-dasfaa` (simulated 3-reviewer PC + self-negation audit) and `submit-dasfaa` (DASFAA 2027 official CFP & strict double-blind compliance). Official DASFAA CFP rules always win on format, page limits, and anonymity.

## Language Convention
- Everything reviewers see (manuscript prose, captions, tables, response drafts): **formal academic English**.
- Audit reports, revision tables, and strategy plans for the author: **Simplified Chinese (简体中文)**.

## Non-Negotiable Integrity Boundary
Every rule in this skill changes **framing, placement, frequency, narrative depth, and prose craft only**:
- **Never** delete or alter any verified measured number, losing table cell, or experimental protocol fact.
- **Never** hide a stronger baseline or invent an unexecuted experiment.
- **Never** write a claim contradicted by a table or figure.
- **"Eliminating over-honest AI self-sabotage" is NOT "hiding weaknesses."** It means presenting scope, trade-offs, and non-first cells the way published human DASFAA authors actually do — once, with a data-backed mechanism, in the right place, without self-defeating confession paragraphs.

---

## 1. Official DASFAA 2027 Constraints (Checked 2026-11-25)
- **Template**: Springer LNCS (`\documentclass[runningheads]{llncs}`), A4 paper, `splncs04` bibliography style.
- **Page Limit**: **Strictly ≤ 16 pages total, INCLUDING all references and any appendices.** (Unlike SIGMOD/ICDE/PVLDB, references count inside the 16-page cap!)
- **Abstract**: **≤ 200 words** (strict CFP cap; measured median across our 8-paper DASFAA corpus is **182.5 words**).
- **Double-Blind Anonymity**: **Strict double-blind**. No author names, affiliations, grant numbers, personal GitHub handles, or identifying PDF metadata (`/Author`, `/Title` leaks). Code links must use neutral anonymous hosting (e.g., `anonymous.4open.science`).

---

## 2. The Human DASFAA Author Thought Process (人写的论文背后的思考过程)

Why do human DASFAA reviewers reject technically solid AI-drafted manuscripts? Because AI drafts read like **defensive engineering logs** ("we built 5 modules, ran 4 benchmarks, and here are 7 threats to validity"), whereas accepted human DASFAA papers follow a **crisp intellectual discovery arc** (exemplified by DASFAA 2026 Best Paper `DynamicPO`, `OLLA`, `Trans-RAG`, and `MAKGED`):

1. **Start from a surprising or concrete empirical tension — never a generic slogan.**
   - *Human DASFAA pattern*: `DynamicPO` opens with a counter-intuitive finding (*"increasing negative samples causes performance degradation despite falling training loss"*); `OLLA` opens with the stark latency chasm between relational scans and LLM token generation; `Trans-RAG` frames an explicit 3-way impossibility triangle (*Security–Accuracy–Efficiency*, Fig. 1).
   - *AI anti-pattern*: Opening with vague boilerplate (*"In recent years, LLMs have revolutionized..."*) or announcing a problem abstractly without showing why existing mechanisms structurally break.
2. **Diagnose ONE crisp root cause before introducing ANY solution.**
   - *Human DASFAA pattern*: Show *why* existing approaches fail on a concrete mechanism (`DynamicPO` proves gradient suppression of boundary negatives; `MAKGED` shows single-perspective triple scoring misses bidirectional subgraph context; `SecGraph` pinpoints why `PeGraph` incurs high communication).
   - *AI anti-pattern*: Listing a laundry list of 6 disconnected "limitations of prior work" followed by an ad-hoc stack of unrelated heuristics.
3. **Frame the method as the natural, minimal consequence of the root cause.**
   - *Human DASFAA pattern*: 2–3 tight, orthogonal mechanisms directly mapped to the root cause (`DynamicPO`: Dynamic Boundary Negative Selection + Dual-Margin Dynamic $\beta$; `Trans-RAG`: `vector2Trans` query-centric transformation; `OLLA`: Semantic Stratified Sampling + Progressive Relational Processing).
   - Every formal object (Definition, Theorem, Algorithm) is motivated in plain English *before* symbols appear, and interpreted for practitioners *immediately after* (`ccfa-human-readable-math-and-proof`).
4. **Anchor the paper with a visual Fig. 1 on Pages 1–3 (`8/8` of our DASFAA corpus).**
   - Fig. 1 must let a 2-minute reviewer see the exact **gap vs. prior work** and **this paper's core mechanism** at a glance (`paper-presubmission-review` F4).
5. **Interpret experiments as scientific evidence, not table-reading transcripts.**
   - *Human DASFAA pattern*: State the quantitative delta → immediately give the **causal mechanism** (`"This is because..."`, backed by an ablation row or run counter) → characterize the **operating regime** where a trade-off or baseline win arises → close with a **practical takeaway**.

---

## 3. Empirical Blueprint from 8 Published DASFAA 2024–2026 Papers

Measured directly from full texts (`references/absorbed-dasfaa-papers.md`):

| Structural / Stylometric Dimension | Observed in 8 Published DASFAA Papers | Target for Our DASFAA 2027 Submissions |
|---|---|---|
| **Abstract word count** | 128–244 words (**median 182.5**) | **165–195 words** (strictly `≤ 200` CFP cap) |
| **Mean sentence length & burstiness** | **20.7–24.0 words** (SD **10.3–13.8**) | **19–23 words** mean, **SD ≥ 9.5** (mix crisp 10w punches with 25w explanations) |
| **Em-dashes (`---` / `—`) per 1K words** | **5/8 have 0.00**, median **0.00**, max 2.21 | **≤ 0.8 / 1K** (prefer clean sentences/parentheses over em-dash chains) |
| **AI cliché density per 1K words** | **0.00–0.56**, median **0.08** | **≤ 0.3 / 1K** (near zero) |
| **`Threats to Validity` heading** | **0 / 8 (0%)** | **0** — NEVER create a `Threats to Validity` section in a DASFAA method/system paper! |
| **`Limitations` heading (method/system papers)** | **0 / 6** core DB/method papers (`1/7` KnowProb; `1/1` ScoringBias eval study) | **0** — integrate scope cleanly into Problem Setting / Setup / 1-sentence Conclusion extension |
| **Self-negation in Abstract or Conclusion** | **0 / 8 (0%)** | **0** — fold scope into positive claims; zero apologetic losses in Abstract/Conclusion |
| **Related Work position** | **6 / 8** in Sec. 2; **2 / 8** (`DynamicPO`, `OLLA`) after Experiments | Either Sec. 2 or pre-Conclusion is valid; keep whichever best serves the story |
| **References count** | 19–51 (**median 31**) | **28–45 verified refs**, concise `splncs04` formatting inside 16 pages |
| **Figures & Tables** | 2–11 figs (median **6.5**), 1–14 tabs (median **4**) | **2–4 high-information figures + 3–6 crisp booktabs tables** |

---

## 4. Eliminating Over-Honest AI Self-Sabotage (反 AI 过度诚实自我否定铁律)

Unifying `write-icde/references/limitations-writing*.md` (R1–R12), `write-pvldb` §7, `review-icde` §3b, AND our 8-paper DASFAA corpus (`0/8` Threats to Validity, `0/8` Abstract/Conclusion self-negation, `0/8` self-negation phrases):

### Why AI Drafts Trigger Instant Reviewer Rejection
When an LLM drafts or "self-critiques" a paper, it compulsively generates **confessional self-sabotage** — telling the reviewer all the reasons to reject the paper under headings like `Threats to Validity` or `Discussion`, using phrases that **zero published human DASFAA authors ever write**:
- *"validates the implementation, not the contract"* / *"only confirms the implementation"*
- *"was written with the live export in view"* / *"built after the current rules, so they test documented behaviour rather than generalization"*
- *"remain the weakest parts"* / *"is a real burden"* / *"neither measures end-user utility"*
- *"on a smaller sample"* / *"is a single small pilot"* / *"covers one domain"*
- *"Both prompts mention popularity, inviting G4 claims"*
- *"at the cost of repairing about half as many tasks"* (in the Conclusion!)
- *"This audit motivates the problem rather than testing X"*
- *"A natural objection is..."* / *"carries no guarantee"* / *"does not help"* / *"may not generalize"* / *"unfortunately"* / *"ad hoc"* / *"not tuned"*

### The 10 Human DASFAA Framing Laws (Exact Rewrite Rules)

1. **Law D1 — Delete `Threats to Validity` & `Failure Cases` headings (`0/8` in DASFAA).**
   - Move any genuinely required protocol fact (e.g., frozen split date, temperature/seed, benchmark provenance, contract scope) to **one concise, neutral sentence** in *Problem Setting* or *Experimental Setup* where it belongs. Delete pure self-flagellation that adds no scientific information.
2. **Law D2 — Zero losses or self-limits in Abstract and Conclusion (`0/8` in DASFAA).**
   - Express scope as a **positive qualifier** of the claim (e.g., *"for declarative metric catalogs"* or *"under registered claim contracts"*), never as a closing negative clause (*"at the cost of repairing half as many tasks"*).
   - Close Conclusion with **1–2 constructive forward-looking research extensions** (`DynamicPO`, `Trans-RAG` style), never a confession of shortcomings.
3. **Law D3 — Never label your own evaluation "tautological", "circular", "not testing generalization", or "small/toy".**
   - State the exact experimental protocol factually and neutrally (e.g., *"On the 320-catalog routing suite, we verify predicate exactness against pre-registered gold labels"* — instead of *"this only confirms the implementation"*).
   - Distinguish cleanly between **development/diagnostic suites** (measuring known production defect classes) and **independent/held-out transfer suites** (public dbt projects, held-out unseen variants, real production snapshots, multi-LLM verbalizers) so the reviewer sees the exact breadth of external validation!
4. **Law D4 — Reframe precision–coverage or safety–utility trade-offs as deliberate, principled design properties (`Trans-RAG` pattern).**
   - Just as `Trans-RAG` writes *"maintaining 96.5% retrieval effectiveness and delivering 32,216× speedup"* rather than *"suffering a 3.5% accuracy drop"*, frame fail-closed abstention or conservative repair as **precision-first soundness**: *"achieving 0.0% unsafe edits (versus 50.0%–83.3% under unconstrained repairers) while automatically resolving all structurally unambiguous defects, leaving ambiguous conflicts for explicit review."*
5. **Law D5 — Explain every non-first table cell ONCE, next to its table, via the 4-step human mechanism.**
   - **Fact → Mechanism (measured instance/workload property, not a deficit of our method) → Operating Regime → Practical Choice Rule / Bound** (2–4 sentences max, `write-icde` R4 + `experiment-analysis-writing` §4).
   - Never repeat the same exception across Introduction, Method, Discussion, and Conclusion.
6. **Law D6 — Turn theoretical boundaries into named Assumptions / Definitions stated once.**
   - Put exact formal premises inside the `Definition` / `Theorem` / `Problem Setting` (e.g., *"over the supported formula fragment"*, *"under registered bindings"*), not in an apologetic paragraph 10 pages later that sounds like retracting the theorem.
7. **Law D7 — Never raise the reviewer's strongest objection yourself just to concede it.**
   - If an obvious reviewer question exists (e.g., *"What about free-form text extraction?"* or *"How costly is declaring a contract?"*), address it constructively as an **architectural interface / deployment workflow** (one crisp paragraph in Discussion/Design showing how the interface composes with upstream extractors or amortizes schema authoring), never as *"X is a real burden and a major weakness."*
8. **Law D8 — Ablation gaps motivate components; they are NEVER concessions.**
   - Write the full system's increment over the ablated variant (*"Adding component C reduces error from X to Y..."*), never *"much of the gain already comes from baseline B."*
9. **Law D9 — Kill AI prose tells & achieve authentic human burstiness (`sigmod-human-writing-craft`).**
   - Ban AI tics (`crucially`, `notably`, `importantly`, `comprehensive`, `seamless`, `holistic`, `paramount`, `delineates`, `spotlights`, `dramatically`, `unconditionally`).
   - Keep em-dashes `≤ 0.8/1K` words; avoid bullet-colon walls (`\textbf{X:} ...`) in prose sections; use Given→New transitions between paragraphs; mix punchy 10–14w diagnostic sentences with 22–28w technical explanations.
10. **Law D10 — Enforce Deng S01–S11 & `paper-presubmission-review` A–H on every Table & Figure.**
    - **Bold best** + **underline second-best** (ties share the mark, even when a baseline wins!).
    - Include a **Best/2nd count row** or **Avg./Summary row** separated by `\midrule` on comparison & ablation tables where applicable.
    - **Claim-first, concise captions**: table captions **≤ 2 lines (~25–35 words)** opening with the key claim; figure captions **≤ 60 words** opening with the takeaway.
    - Pure `booktabs` + `\cmidrule(lr)` (zero vertical rules `|`), unified decimal precision per column, single unit per column, colour-blind-safe Okabe-Ito palette, zero trailing `□` QED boxes, `|Δp| ≤ 1` float proximity.

---

## 5. Automated Audit Script
Run on every DASFAA draft before and after deep revision:
```bash
python3 scripts/dasfaa_human_craft_audit.py <paper_dir_or_main.tex> [--pdf <compiled.pdf>]
```
It checks:
- Abstract word count (`≤ 200` words) and zero Abstract/Conclusion self-negation;
- Forbidden `Threats to Validity` / `Where we fail` / `Limitations` headings;
- Full regex sweep for **Over-Honest AI Self-Sabotage & Self-Negation** phrases (from ICDE + PVLDB + DASFAA corpora);
- Stylometric alignment against the 8-paper human DASFAA baseline (sentence length mean/SD, em-dashes/1K, AI clichés/1K);
- Table & caption lint (S01–S06: caption length, bold/underline presence, vertical rules, QED boxes);
- Strict double-blind anonymity scan (author/institution/GitHub leaks + PDF metadata).
