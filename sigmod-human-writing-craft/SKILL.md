---
name: sigmod-human-writing-craft
description: Reverse-engineered human academic writing craft and anti-AI-smell review protocol distilled from published human-authored ACM SIGMOD Industrial papers (Measures in SQL, Enzyme, FinSQL, AlayaDB, Data-Juicer). Use on EVERY new manuscript version (regardless of target venue—SIGMOD, PVLDB, ICDE) to dissect closely related published human papers, audit prose for AI-smell stylometric tells, and rewrite paragraphs with authentic human cadence, organic Given-New transitions, and balanced section budgets.
---

# Top-Venue Human Academic Writing Craft & Anti-AI-Smell Protocol

Reviewers at SIGMOD, PVLDB, and ICDE reject manuscripts that read with unmistakable **"AI-smell" (AI 味)**—even when the engineering and experiments are strong. This skill codifies the **reverse-engineered prose patterns of published human database authors** (Julian Hyde/Google *Measures in SQL* SIGMOD '24, Databricks *Enzyme* SIGMOD '26, ZJU *FinSQL* SIGMOD '24, *AlayaDB* SIGMOD '25, Alibaba *Data-Juicer* SIGMOD '24) and enforces a **permanent per-version writing review workflow**.

---

## Permanent Per-Version Workflow (Apply to Every Manuscript Version)
Whenever a new draft version is produced for **any** target venue (SIGMOD, PVLDB, ICDE, etc.):
1. **Reverse-Engineer 3–5 Closely Related Human Papers** published in the target venue (2023–2026), extracting their section page-share %, paragraph move structure, and stylometric norms.
2. **Run Quantitative AI-Smell Audit**: Execute `python3 scripts/ai_smell_audit.py <paper.tex>` to flag exact line numbers of em-dash overuse, bold-colon bullet walls, AI lexical tics, mechanical stamps, and meta-reviewer leaks.
3. **Deliver a Dedicated Writing Review Report** diagnosing every section (Title → Abstract → Intro → Design → Evaluation → Lessons → Related Work → Conclusion).
4. **Rewrite Prose in Authentic Human Systems Voice** while preserving **100% of verified numbers, citations, algorithms, and formal guarantees**, then re-run `ai_smell_audit.py` to confirm all stylometric indicators sit cleanly inside human norms.

---

## Quantitative Stylometric Norms (Human SIGMOD Baseline vs. AI-Smell Thresholds)

Empirical measurements across 5 published human SIGMOD '24–'26 Industrial papers (see [references/HUMAN_SIGMOD_PROSE_DISSECTION.md](references/HUMAN_SIGMOD_PROSE_DISSECTION.md)):

| Metric | Human Published Range (Mean) | AI-Smell Red Flag | Target After Polish |
|---|---:|---:|---:|
| **Em-dashes (`---`) / 1K words** | 0.00 – 2.32 (**0.82**) | > 2.5 / 1K | **≤ 1.2 / 1K** (≤ 10 total in 12p) |
| **Colons (`:`) / 1K words** (prose + bullets) | 5.0 – 6.6 (**6.1**) | > 15 / 1K | **≤ 12 / 1K** (prefer prose over `\textbf{X:}` lists) |
| **Mean sentence length** | 21.2 – 23.4 words | > 25 words (stuffed clauses) | **19 – 23 words** with varied cadence (SD 9–13) |
| **AI cliché density / 1K words** | 0.88 – 4.31 (`Measures`: **0.88**) | > 2.5 / 1K | **≤ 1.0 / 1K** |
| **Mechanical `Takeaway (RQn).` stamps** | **0** in 5/5 papers | ≥ 2 | **0** (weave insight into closing prose sentence) |
| **Meta-reviewer leaks** ("Reviewers rightly ask...") | **0** in 5/5 papers | ≥ 1 | **0** (write directly to practitioners/readers) |

---

## The 7 Laws of Authentic Human Database Systems Writing

### Law 1 — Kill AI Lexical Tics & Over-Emphatic Adverbs
Never use stock LLM rhetorical crutches. Replace them with concrete, plain verbs and physical mechanisms:
- **Ban / Eliminate**: `crucially`, `notably`, `importantly`, `merit emphasis`, `exposes [N] sharp/generalizable findings`, `bridges X and Y`, `cleanly separates`, `strictly enforces`, `unconditionally`, `delineates`, `distills`, `spotlights`, `imperative`, `paramount`, `holistic`, `seamless`, `dramatically`, `novel`, `comprehensive`, `Following this X discipline`, `Reviewers rightly ask`, `demonstrating empirically why...`.
- **Human Substitute**: State the plain fact directly (*"Table 7 shows three patterns..."*, *"Direct SQL failed on 52.8% of Loctek traps because..."*, *"When a schema has fewer than ten static tables, a prompt glossary is cheaper to maintain."*).

### Law 2 — Replace Em-Dash Chains (`---`) with Crisp Sentence Boundaries
LLMs overuse paired em-dashes (`---like this---`) to cram two thoughts into one 35-word sentence. Human database authors break long thoughts into **one short claim + one concrete explanation** (cf. Julian Hyde, *Measures in SQL*; Databricks *Enzyme* Sec. 6.2.1). Keep total em-dashes ≤ 8–10 across a 12-page paper.

### Law 3 — Write Analytical Prose, Not Endless `\textbf{Label:} ...` Slide Bullets
Use numbered/bulleted lists **only** for genuinely parallel taxonomies (e.g., 4 core contributions, 4 failure modes, 8 certification checks). Convert mechanical bullet dumps in **Evaluation roadmaps (RQ1–RQ5)**, **Experimental findings**, and **Operating regimes** into cohesive paragraphs where each paragraph opens with a concrete subject (`Prospect performs poorly under incremental refresh because...` — *Enzyme* p. 11).

### Law 4 — Master Given-to-New Paragraph Transitions (No Robotic Connectors)
Human paragraphs flow without `Moreover`, `Furthermore`, or `Crucially`. Use **Given → New cohesion**:
- End Paragraph $k$ on a concrete technical tension (e.g., *"leaving daily rates averaged across unequal volumes"*).
- Open Paragraph $k+1$ by echoing that exact object as the subject (*"To prevent invalid rate rollups, Stage 1 checks six equivalence flags..."*).

### Law 5 — Section-by-Section Human Paragraph Moves (先写什么、再写什么)
- **Title**: Direct, concrete `[System]: [Core Mechanism] for [Domain]` (10–14 words, no hype).
- **Abstract (180–230 words, 2 compact paragraphs)**: (1) Concrete failure/bottleneck with 1 real number; (2) What the system is + its 2–3 core database mechanisms (NO LOC/test-suite bragging in sentence 1 of Para 2!); (3) Tight empirical headline across production + public benchmarks.
- **Introduction (1.6–2.0 pp, 14–17%)**: Context → Concrete industrial failure with real numbers → Why existing tracks fail structurally (2 concise contrasts) → System thesis & exact deployment boundary → 3–4 tight contributions (Problem → Mechanism → Result).
- **System Design & Algorithms (4.2–5.0 pp, 36–42%)**: Start with the architectural trade-off (*why* a naive single-store or single-plane design breaks) → Introduce the abstraction → Formalize algorithm/invariant → Trace one concrete worked example end-to-end.
- **Experimental Evaluation (2.6–3.2 pp, 22–27%)**: Open with 1 concise roadmap paragraph (no bloated RQ bullet list) + reproducibility note. In each subsection: (1) Dataset/setup in 2 sentences → (2) Main quantitative result → (3) **Mechanistic diagnosis** of *why* baselines fail or *where* curves bend (cf. *Enzyme* Sec. 6.2.1, *AlayaDB* Sec. 9.1) → (4) Natural concluding sentence (NO `Takeaway (RQk).` stamp!).
- **Operational Lessons (0.7–1.0 pp, 6–8%)**: Concrete incident → Root cause → Transferable engineering rule (cf. *Enzyme* Sec. 5).
- **Conclusion (0.25–0.35 pp, 3%)**: Do **not** copy-paste the Abstract's metric list word-for-word. Synthesize the architectural principle learned, summarize the overarching evidence in 1–2 fresh sentences, and close with 1 concrete forward-looking database research direction.

### Law 6 — Vary Sentence Cadence ("Burstiness")
Alternate 10–14 word punchy diagnostic sentences (*"The SQL compiles, executes, and returns a plausible percentage. Yet the number is wrong."*) with 22–28 word technical explanations. Uniform 26-word sentences scream AI generation.

### Law 7 — Zero Integrity Trade-Offs During Polish
Never alter a single verified experimental metric, citation key, algorithm step, or redaction rule during stylistic rewriting. Always verify numerical invariance and run `layoutlint.py` after rewriting.
