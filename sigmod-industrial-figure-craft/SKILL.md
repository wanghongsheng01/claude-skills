---
name: "sigmod-industrial-figure-craft"
description: "Design, dissect, and elevate system architecture diagrams, motivating examples, and experimental plots specifically for ACM SIGMOD Industrial Track papers. Distilled from visual dissection of 10 published 2024-2027 SIGMOD/PVLDB/CIDR systems papers (FinSQL, Data-Juicer, AlayaDB, Enzyme, DIVER, WAIR, SALUS, Palimpzest, DocETL, LOTUS). Covers figure motivation, compositional archetypes (3-column phased pipeline, asymmetric control/data plane, problem-vs-solution contrast), focal spotlighting of novel components over muted infrastructure, numbered offline/online step traces, concrete running-example anchoring, vector iconography (DB cylinders, gates, decision branches), restrained palettes, and anti-patterns that trigger 'org-chart / model-generated' reviewer fatigue. Complements ccfa-figure-layout-review (R1-R16 red lines) and results-presentation-review (S01-S11). Use when designing, critiquing, or redrawing SIGMOD Industrial architecture or result figures (SIGMOD工业稿作图 / 架构图重构 / 论文构图优化 / 顶会作图规范)."
---

# SIGMOD Industrial Track Figure Craft (SIGMOD 工业稿作图设计指南)

A SIGMOD Industrial Track PC member spends **10–15 minutes** on a first pass and reads **Figure 1 before reading Section 3**. While `ccfa-figure-layout-review` enforces mechanical hygiene (R1–R16: no line crossing boxes, no text overlap, font $\ge 6$ pt) and `results-presentation-review` enforces experimental table/plot honesty (S01–S11), **this skill governs visual design craft**: *why a figure exists, how its composition guides the reviewer's eye, how it spotlights the paper's true technical contribution, and why it feels hand-crafted rather than auto-generated.*

Grounded in direct visual dissection of **10 published 2024–2027 SIGMOD / PVLDB / CIDR papers** (`references/PUBLISHED_SIGMOD_DISSECTION.md`).

---

## 1. Core Design Philosophy: Kill the "Corporate Org-Chart"

The single most common reason SIGMOD Industrial architecture figures fail to impress reviewers is the **Nested Box / PowerPoint Org-Chart Anti-Pattern**:
- 12–20 identical rounded rectangles packed wall-to-wall into 3 horizontal shelves;
- every box outlined with a thick saturated rainbow border (blue, green, orange, purple, red all shouting equally);
- zero concrete query/data example, zero numbered execution trace, zero distinction between *commodity infrastructure* and *this paper's novel contribution*;
- banner titles cluttered with vanity stats (`189K LOC, 386 Tests`) instead of architectural roles.

Published SIGMOD Industrial figures succeed by following **Six Design Laws**:

### Law 1 — Start With Figure Motivation (One Visual Question Per Figure)
Before drawing a single box, write one sentence answering: *"What misunderstanding does this figure prevent in 15 seconds?"*
- **Fig. 1 (Problem/Motivation Contrast or System Overview)**: Must answer *either* (a) **Why naive approaches fail vs. how our system fixes it** (`DIVER` SIGMOD '26 Fig. 1, `WAIR` SIGMOD '26 Fig. 2, `SALUS` SIGMOD '27 Fig. 1), *or* (b) **How offline governance / compilation connects to online execution and what concrete artifact flows through our core engine** (`FinSQL` SIGMOD '24 Fig. 1, `Palimpzest` CIDR '25 Fig. 1, `Data-Juicer` SIGMOD '24 Fig. 1).
- Never draw a pure "box inventory" that merely lists microservice ports without showing **mechanism** (decisions, gates, transformations, feedback).

### Law 2 — Choose One Proven SIGMOD Compositional Archetype
Pick the archetype that matches your system's real data/control flow rather than defaulting to stacked shelves:

| Archetype | Structure | Published Exemplar | Best For |
|---|---|---|---|
| **A. Phased 3-Column Pipeline (`I \| II \| III`)** | Dark crisp header bands across 3 dashed-divider columns; left-to-right flow with dual-track step badges | `FinSQL` (SIGMOD '24 Fig. 1), `Palimpzest` (CIDR '25 Fig. 1) | Compilation / multi-stage query engines with distinct offline & online phases |
| **B. Asymmetric Control vs. Execution Plane** | Top/Left muted **Offline Control Plane** feeding an immutable boundary into a spotlighted **Online Execution Core** on the center-right, backed by bottom storage cylinders + right-hand closed-loop feedback | `Data-Juicer` (SIGMOD '24 Fig. 1), `AlayaDB` (SIGMOD '25 Fig. 3) | Enterprise data platforms, governed semantic engines, MCP/multi-plane serving stacks |
| **C. Split Problem-vs.-Solution Contrast** | Top half: concrete real query breaking existing baseline (red `×`); Bottom half: same query succeeding through our system (teal/blue `✓`) | `DIVER` (SIGMOD '26 Fig. 1), `WAIR` (SIGMOD '26 Fig. 2) | Papers introducing a subtle failure mode (e.g., silent semantic failure, uncertified fallback) |
| **D. Companion Figure + Algorithm Pair** | Left 60%: visual plan-space diagram with steps `①–⑥`; Right 40%: Algorithm 1 with `# Step ①–⑥` annotations | `Palimpzest` (CIDR '25 Fig. 1 + Alg. 1) | Planning/optimization systems where visual intuition maps directly to pseudocode |

### Law 3 — Spotlight Focal Hierarchy (80% Muted Neutral, 20% High-Contrast Hero)
A reviewer must spot **your contribution in 2 seconds** without reading the caption:
- **Commodity Infrastructure & External Context** (warehouse storage, SSO, raw LLM APIs, caches): **low-saturation neutral gray** (`#F4F6F8` fill, `#94A3B8` thin `0.75 pt` border, muted slate `#475569` text).
- **Offline / Supporting Subsystems**: **single soft secondary tint** (e.g., warm sand `#FDF8EE` with `#B45309` thin border).
- **Hero Core Contribution** (e.g., *Deterministic Recursive Planner & 8-Dimension Certification Gate*): **single high-contrast primary brand hue** (Deep SIGMOD Navy `#0B4F8C` header bar, `#EDF5FC` soft canvas, crisp `1.3 pt` accent border, internal decision flow & gate badges).
- **Semantic Status Accents Only**: reserve Teal (`#0F766E`) strictly for *Certified / Pass (`✓`)* and Vermilion (`#C2410C`) strictly for *Blocked / Quarantined / Error (`⊘`/`×`)* — never use red/green as decorative container colors.

### Law 4 — Dual-Track Numbered Traces (`①–③` Offline vs. `1–5` Online) + Concrete Artifact Anchoring
- Follow `FinSQL` (SIGMOD '24 Fig. 1) and `Palimpzest` (CIDR '25 Fig. 1):
  - Use **amber circled badges (`① ② ③`)** for offline governance / asset compilation / closed-loop sync;
  - Use **navy filled badges (`1 2 3 4 5`)** for online request execution;
  - Anchor the left entry with a **mini concrete running-example callout** (e.g., `"Oct US RMA rate by category?"` → typed spec `S`) and exit on the right with **two concrete outcome cards**: `✓ Certified Primary KPI` vs. `⊘ Diagnostic Mode / Clean Refusal`.
- Include a compact **1-line visual legend** at the bottom of the figure explaining solid arrows (online query flow), dashed arrows (offline control / snapshot / audit loop), and badge shapes (`Bu24` PVLDB '24 Fig. 1).

### Law 5 — Use Real Architectural Visual Primitives (Not Uniform Rectangles)
Differentiate component ontology visually using clean vector shapes (`assets/sigmod_arch_primitives.py`):
- **Database Cylinders** for persistent analytical stores (StarRocks warehouse layers) and in-memory snapshot stores (Redis v3);
- **Stacked Layer Cards / Medallion Funnel** for ODS → DWD → DWS → ADS warehouse hierarchy (`Enzyme` SIGMOD '26 Fig. 1);
- **Gate / Shield Strip or Branching Decision Node** for multi-dimension certification checks (`8-Dim Gate: Pass?`);
- **Compact Sub-Chips** for multi-plane interfaces (`7207–7211`) instead of 5 full-sized bloated text boxes;
- **Clean Sans-Serif (`Helvetica` / `DejaVu Sans`) inside architecture diagrams** at `7.0–8.5 pt` printed size (easier to scan inside tight schematics than wide serifs), with **generous 20%+ internal padding** and **zero vanity stats (`LOC`, `test count`) inside diagram titles**.

### Law 6 — Experimental Figure Craft for SIGMOD Industrial
Beyond `results-presentation-review` (S01–S11) and `ccfa-figure-layout-review` (R1–R16):
1. **Every multi-panel plot uses full `figure*` width (`7.0 in`)** so tick labels never drop below `7.5 pt` printed size.
2. **Plot mechanisms, not flat bar dumps**: replace uniform ablation bars (e.g., six 83.3% bars) with a structured booktabs table + a high-information **Latency Distribution / Log-Scale Breakdown** or **Cross-Benchmark (Enterprise vs. Public) Multi-Model Matrix**.
3. **Callout annotations carry the takeaway directly on the canvas**: e.g., shaded trust/failure band (`SALUS` SIGMOD '27 Fig. 1), crisp `14 pp Audit Gap` arrow, or `< 0.001% overhead` bracket — never overlapping data!
4. **Always verify on the final pdfLaTeX / Overleaf PDF** (`S29`), not only standalone PNGs.

---

## 2. Pre-Draw & Post-Draw Review Workflow

1. **Dissect Before Drawing**: Read `references/PUBLISHED_SIGMOD_DISSECTION.md` and select one archetype (`A`, `B`, `C`, or `D`).
2. **Draft Visual Hierarchy Spec**: List every element in 3 tiers: *Hero (highlight)*, *Supporting (soft tint)*, *Commodity Infrastructure (neutral gray)*. Cut any text that belongs in prose/tables (LOC, file counts, long bullet lists).
3. **Render with Vector Primitives**: Build via `assets/sigmod_arch_primitives.py` (or clean TikZ/Illustrator) at exact final print width (`7.0 in` for `figure*`, `3.33 in` for `figure`), outputting both `.pdf` (for LaTeX) and 300-DPI `.png` (for visual inspection).
4. **Run Two-Pass Critique**:
   - **Pass 1 (Craft & Composition — This Skill)**: Apply the 6 Laws above. Can a reader identify the hero contribution, offline-vs-online boundary, concrete query path, and positive-vs-negative outcomes within 15 seconds? Is there at least 20% clean whitespace?
   - **Pass 2 (Mechanical Red Lines — `ccfa-figure-layout-review`)**: Verify R1–R16 (zero line-box crossings, zero label clipping, colorblind-safe Okabe-Ito + hatches/linestyles, exact R16 agreement with frozen JSON/tables).
5. **Final Overleaf / pdfLaTeX Check**: Compile in Overleaf/pdfLaTeX and inspect the embedded figure page at 200+ DPI.

---

## 3. Files in This Skill
- `references/PUBLISHED_SIGMOD_DISSECTION.md` — Visual dissection of 10 published 2024–2027 SIGMOD / PVLDB / CIDR papers across motivation, layout, iconography, focal hierarchy, and anti-patterns.
- `assets/sigmod_arch_primitives.py` — Reusable matplotlib vector primitives (DB cylinders, header-band panels, decision diamonds, step badges, orthogonal channels, restrained SIGMOD palette).
