---
name: topvenue-figure-craft
description: "Design, redraw and audit Figure 1 / overview figures for top-venue papers (OSDI, ATC, USENIX Security, ISSTA, ICDE, PVLDB, PODS, SIGMETRICS, ACL, SIGIR, ICML, IJCAI). Use when a paper's first figure is a generic boxes-and-arrows pipeline, when every paper in a portfolio shares one figure template, when arrows cross container borders or titles, labels sit on lines, text is too small or walls of text fill boxes, or when choosing what Figure 1 should argue. Provides an archetype decision table distilled from ~50 published Figure 1s, an intent -> composition -> emphasis -> execution workflow, measurable execution rules, an anti-pattern list, a portfolio uniqueness rule, a geometry audit script (matplotlib hook + vector-PDF mode) and reusable TikZ styles."
---

# Top-venue figure craft

A reviewer decides in about ten seconds whether Figure 1 makes a point. In a reverse-engineering study of
about fifty Figure 1s from 2023–2026 papers at twelve venues (per-venue notes in `references/`), only about
28% were architecture diagrams (mostly industry, platform, or workflow-integration papers). **Strong Figure 1s
argue why something matters rather than merely cataloguing modules.**

Importantly, **do not blanket-ban or label the "top pipeline + bottom running-example" dual-band layout as a
weak archetype.** It is a legitimate, effective Figure 1 design when a paper genuinely benefits from pairing an
end-to-end mechanism overview with a concrete visual trace, step-by-step data transformation, or numbered
guarantees (e.g., *C-RAG*, ICML'24, Fig. 1). What fails in practice is **(1) portfolio sameness** — stamping
every paper in a submission batch with the exact same template regardless of contribution type — and **(2) poor
execution** (nested box-in-box crossings, prose walls instead of visual instances, rainbow equal-weight boxes,
tiny non-body fonts). Choose the archetype **case-by-case** to fit the paper's core claim.

Use this skill together with any venue-specific layout or review skill you already have. It does not replace them.

## Files

| Path | What it is |
|---|---|
| `references/archetypes.md` | 13 Figure 1 archetypes with ASCII sketches, when to use each, published examples |
| `references/<venue>.md` | Observed figure profile + transferable practices for each of the 12 venues |
| `scripts/figure_geometry_audit.py` | Collision audit: `run` (hooks matplotlib `savefig`), `pdf` (any vector PDF incl. TikZ), `selftest` |
| `assets/topvenue_tikz_styles.tex` | TikZ styles: palette with semantic roles, nodes, containers with title band, orthogonal edges, haloed labels, badges |
| `assets/demo_figure.tex` | Compilable demo: a problem-contrast timeline Figure 1 plus a container/edge style sheet figure |

## Workflow (do the steps in order; do not start by drawing)

### 1. Intent: write one sentence
Write what the reviewer must believe after 10 seconds, as a claim with a cause:
"*X fails because Y; our Z avoids it by W*", "*A and B look equivalent but differ on C*",
"*the trade-off between P and Q is not fundamental*". If the sentence names modules, it is not an intent.
Also write the one number (from the results files) that would make the claim concrete.

### 2. Archetype: pick from the decision table
Choose the archetype that turns the intent into something *visible*. Draw 2–3 candidate thumbnails on paper and
keep the one in which the claim is visible without reading the caption.

| Paper type / core contribution | First choice | Alternative | Avoid |
|---|---|---|---|
| Systems: the problem is measurable (tail latency, dropped requests, overhead) | A1 motivating measurement | A3, A9 | full-width architecture on page 1 |
| Systems: correctness or timing bug (crash, lease, concurrency) | A3 success-vs-failure timeline | A4 minimal counterexample | nested pipeline boxes |
| Systems: breaks a trade-off (granularity, cost, memory) | A9 positioning plot | A1 | listing every module |
| Caching / reuse / access-control rewriting | A8 aligned before/after data units | A4 | component boxes |
| Databases: query- or data-level problem | A4 real query/data instance + one result number | A2 | system name card |
| Database theory: classification / complexity | A10 complexity or reduction landscape | A4 minimal pair of instances | slide-style architecture |
| Performance modelling / queueing / cache theory | A5 policy in state space or on a timeline, next to an evidence curve | A11 | system diagram |
| ML guarantees / conformal / theory | A5 insight sketch (+ small result inset) | A10 proof roadmap | module list |
| NLP verification / hallucination / RAG | A7 text-span teaser, single column, page 1 right column | A1 | full-width method figure on page 1 |
| IR ranking | A1 problem evidence or A9 positioning | A2 paradigm grid | default plotting-library style |
| Software testing / repair | A6 minimal reproducing code with oracles as comments | A2 | pipeline on page 1 |
| Security defence | A2 2×2: existing/ours × benign/attack, with the real attack string | threat model with only the attack path coloured | icons without any concrete attack |
| AI / neuro-symbolic / constrained decoding | A5 trellis or path sketch, or A2 N+1 panels | A13 | clip-art |
| Industry / platform / multi-stage certified workflow | A12 annotated architecture (incl. well-crafted top-pipeline + bottom visual-trace/guarantee dual band when the lower band adds concrete evidence) | A4 | unfocused all-module diagram or prose-wall lower band |

### 3. Composition
- **One reading path** (left→right, or top→bottom), ending at the claim or the number.
- **Single column first.** Most Figure 1s in the sample were single column (about 240 pt wide, 120–200 pt tall). Use
  full width only for overview figures (usually Fig. 2–5) or industry platforms.
- **Controlled comparison:** panels share one input and one grid; only one visual variable changes.
- **Show the instance.** Draw a real query, code line, timeline, data cell or text span instead of prose in boxes.
  At most 1–3 words per box. Any sentence longer than that belongs in the caption.
- **Avoid nesting.** A box inside a box inside a box forces edges through borders. Prefer flat layouts,
  uncoloured background regions (no stroke), or edges that end on the container border.

### 4. Emphasis (pick one main device)
- Reserve **one accent hue for "ours"** and **one alert hue for failure/attack**. Everything else is gray.
- Desaturate what is shared or prior. Saturate only the contribution.
- Put **1–3 result numbers at the end of the reading path** (for example "> 5 min → 1.67 s"). Do not label everything.
- Use numbered badges ①②③ only when the same numbers appear in the text or caption.
- In the caption, use colour words as the legend ("blue = served by the new epoch") instead of a legend box.

### 5. Execution rules (measurable)
1. **Font:** same family as the body text; every readable glyph ≥ 80% of the body size (10 pt body → ≥ 8 pt;
   9 pt acmart body → ≥ 7.2 pt). Badge digits are the only exception.
2. **Colour:** ≤ 4–5 hues + neutrals, colour-blind-safe (Okabe–Ito). Each hue has one meaning across all
   figures of the paper. One accent is reserved for the contribution.
3. **Edges:** orthogonal only (TikZ `|-` / `-|`). Endpoints sit on node borders, normally at side midpoints.
   Diagonals are allowed only for one-to-many fan-out.
4. **No crossings:** an edge never passes through any container that is not its source or target, and never
   through any container's title band. Edges from outside a container end **on the container border**.
   They do not dive through it to a child box. Edges do not cross each other.
5. **Labels:** labels go in whitespace beside the line (above/below/left/right), with ≥ 2 pt clearance from any
   line or border. Never place a label midway on a line. A white halo (`fill=white, inner sep`) is a safety margin,
   not a licence to sit on the line.
6. **Geometry consistency:** one corner radius, two stroke widths (regular 0.6 pt, contribution 1.0 pt),
   one arrowhead style.
7. **Numbers** come only from results files (JSON/CSV), read by the plotting script or pasted from a checked
   table. Never type a number by hand.
8. **Caption** opens with the claim in one sentence (bold where the template allows), then explains how to read
   the figure. Do not open with "Overview of X".
9. **Tooling:** use TikZ for structure figures (same font, exact alignment); use matplotlib for data
   (`font.family` set to the body font, `pdf.fonttype 42`). Export vector graphics only.
10. **Gate:** `figure_geometry_audit.py` reports 0 FAIL, and every page is inspected at 180 DPI.

### 6. Audit
```bash
# matplotlib script: ALWAYS run a copy, with saves redirected (scripts often hard-code absolute output paths)
python scripts/figure_geometry_audit.py run gen_figs.py --match fig1 --out-dir /tmp/fig_audit
# any vector PDF (TikZ output, exported figure, or a single page of the paper)
python scripts/figure_geometry_audit.py pdf figures/fig1.pdf
python scripts/figure_geometry_audit.py selftest
```
Options: `--clearance 2` (pt), `--endpoint-tol 3` (pt), `--strict` (WARN→FAIL), `--allow-parent-entry`
(downgrades border crossings into a container to WARN; use only when the venue's published figures clearly do it), `--json out.json`.
Checks: `TEXT_ON_LINE`, `TEXT_ON_BORDER`, `TEXT_OVERLAP`, `TEXT_OUTSIDE_CANVAS`, `LINE_THROUGH_CONTAINER`,
`LINE_CROSSES_BORDER`, `LINE_THROUGH_TITLE`, plus WARNs `ENDPOINT_INSIDE_BOX`, `LINE_CROSSING`,
`LEGEND_OVER_DATA`, `DANGLING_ARROW`. Exit code 1 on any FAIL. Each finding prints its location in points and,
for matplotlib, in data coordinates, so you can find the offending line in the script.

**Safety:** the `run` mode only intercepts `savefig`. Before running, grep the copied script for absolute paths
and rewrite them. Never run a figure generator inside a directory you are not allowed to modify.

## Anti-patterns (each one was observed, in our drafts or in published papers)
- **Edge through a container title** (the edge enters a container across its title text).
- **Edge through a container border to reach a child box**, and the label beside it sitting on the border.
- Label sitting on a line or touching a box edge. Two labels overlapping.
- Arrow starting or ending inside a box instead of on its border, or an arrowhead floating short of its target.
- Curved or diagonal connectors leaving a panel, looping around it, or crossing each other.
- **Gray box stacking:** 2–3 levels of nested rounded boxes, all the same visual weight.
- **Text walls:** 2–4 lines of prose per box. A "running example" written as sentences instead of drawn.
- 4–6 hues without meaning. Default palettes from diagram tools. The same colour used for "problem" and for "ours".
- Plotting-library default fonts at 5–6 pt next to a serif body text. Raster exports.
- Clip-art, emoji, logos and comic fonts in a research figure.
- Caption opening with "Overview of X" or "Illustration of …".
- **Portfolio sameness:** mechanically stamping every paper's Figure 1 with the same layout (for instance, forcing every paper into a top-pipeline + bottom-example template) regardless of whether that archetype fits the paper's core contribution. *(The dual-band form itself is valid when well-matched to a paper and executed cleanly; blanket reuse across a whole portfolio is the anti-pattern.)*

## Portfolio uniqueness rule
When several papers are prepared together (one group, one author, one submission season), no two Figure 1s may
share an archetype *and* layout. Before drawing, list each paper's (intent sentence, archetype, layout,
accent hue) in one table. If two rows share archetype and layout, change one of them, starting with the paper
whose intent fits its second-choice archetype better. Shared house style (palette, fonts, stroke widths) is
fine. A shared template across every paper is not. **Never blanket-ban any valid archetype** (including the
top-pipeline + bottom-running-example dual band): keep it whenever it is genuinely the clearest fit for a
specific paper, provided the lower band draws a real visual trace/data/guarantee instance (not a prose wall),
one accent hue establishes visual focus, and geometry passes `0 FAIL / 0 WARN`.

## Portfolio-Wide Before/After Redesign Retrospective (12-Venue Production Practice)
Applying this workflow end-to-end across a 12-paper portfolio spanning all 12 venues replaced 12 homogeneous
"pipeline + running-example" diagrams with **12 visually distinct Figure 1 archetypes** and eliminated **352 FAIL
and 139 WARN** geometry defects (`491 → 0`) under `--strict` automated audit plus 180 DPI visual proofread:

| Venue | Paper Domain | Redesigned Figure 1 Archetype | Tooling | Strict Geometry Audit |
|---|---|---|---|---|
| ICDE Ind | Access-control rewriting | A8 Authorization Grid Before/After + Flat Deployment Anchor | Native TikZ | 67 FAIL / 11 WARN → 0/0 |
| OSDI | Distributed lease recovery | A3 Dual-Lane Shared Timeline (Prior Crash vs. Guarded Takeover) | Native TikZ | 62 FAIL / 18 WARN → 0/0 |
| PODS | Complexity classification | A10 Three-Lane Complexity Landscape (instance moved to Table) | Native TikZ | 16 FAIL / 5 WARN → 0/0 |
| PVLDB | Multi-plane catalog drift | A4 Four-Plane Color-Paired Alignment + Quantitative 2×2 Matrix | Native TikZ | 30 FAIL / 11 WARN → 0/0 |
| ACL ARR | Claim staleness verification | A7 Single-Column Page-1 Right-Column Text-Span Teaser | Native TikZ | 45 FAIL / 14 WARN → 0/0 |
| IJCAI | Constrained agent planning | A5 Planar State-Transition Trellis + Right Impact Strip | Native TikZ | 31 FAIL / 7 WARN → 0/0 |
| SIGMETRICS | Cache freshness modeling | A5 Continuous Phase Map + Oracle Floor & Tail Evidence | Matplotlib (`STIX`) | 41 FAIL / 30 WARN → 0/0 |
| ISSTA | Conformance mutation testing | A6 Minimal Reproducing Code (lines 01–09) + Diff Oracle Witness | Native TikZ | 3 FAIL / 0 WARN → 0/0 |
| USENIX ATC | Proxy fault/drift isolation | A9 Log-Log Granularity Pareto Trajectory + Normalized Failure Bars | Matplotlib (`STIX`) | 10 FAIL / 2 WARN → 0/0 |
| SIGIR | Post-purchase outcome ranking | A1 Single-Column Page-1 Right-Column Empirical Motivation Scatter | Matplotlib (`STIX`) | 15 FAIL / 21 WARN → 0/0 |
| ICML | Conformal risk under premise shift | A5/A13 Boolean Premise-Lattice Partition + Coverage-Collapse Curve | Matplotlib (`STIX`) | 8 FAIL / 18 WARN → 0/0 |
| USENIX Sec | Multi-app gateway security | A2 2×2 Isomorphic Attack/Defense Contrast Matrix (Split Channel) | Native TikZ | 24 FAIL / 2 WARN → 0/0 |

### Cross-Venue Native TikZ Production Recipes
1. **Compile standalone previews with the exact target venue class and font packages** (`IEEEtran` + `courier`, `acmart` with `acmsmall,nonacm`, `usenix-2020-09`, `ijcai27.sty`, etc.). Templates such as `ijcai27.sty` enlarge `\footnotesize` to 9 pt; specify explicit `\fontsize{8}{9.6}\selectfont` inside TikZ styles when strict parity is required.
2. **Always load `\usepackage[T1]{fontenc}`** whenever TikZ nodes contain underscores (`\_`). Without `T1`, TeX draws `\_` as a separate vector rule that triggers false-positive `TEXT_ON_LINE` audit failures.
3. **Eliminate cross-hair dividers in 2×2 and aligned grids**: draw short independent rules under each header and a single horizontal row separator with 4–6 mm white gutters between columns rather than a crossing `+` wireframe.
4. **Never stack rounded containers**: encode architecture hierarchy with flat background regions (no border stroke) or physically split input shapes (e.g., trusted credential channel above untrusted payload channel) so edges connect straight to borders without piercing parent frames.

### Cross-Venue Matplotlib Production Recipes
1. **Safe `twinx()` dual-axis tick hiding**: `twinx()` draws duplicate x-tick text on top of the primary axis (`TEXT_OVERLAP`). Hide only the secondary axis tick labels via `ax_r.tick_params(axis="x", which="both", bottom=False, labelbottom=False)` and `for lbl in ax_r.get_xticklabels(): lbl.set_visible(False)` — **never** call `ax_r.set_xticks([])`, which wipes the shared primary ticks.
2. **Decouple text from callout arrows**: place callout prose in clean whitespace using `ax.text(...)`, then draw an empty-text pointer `ax.annotate("", xy=..., xytext=...)` stopping 2–4 pt short of the curve/bar so arrowheads never clip text or data markers. Use `textcoords="offset points"` on log-scale bars.
3. **Avoid filled triangle (`^`, `v`) and diamond (`D`) scatter markers near axes or annotations**: static vector-PDF audits parse tiny filled polygons as arrowheads (`DANGLING_ARROW`); prefer circles (`o`), squares (`s`), hollow rings, or crosses.
4. **Match body serif typography at 1:1 width**: author figures at exact single-column (`3.30–3.35 in`) or double-column (`6.9–7.0 in`) width with `font.serif = ["Times New Roman", "Times", "STIXGeneral"]`, `mathtext.fontset = "stix"`, and `pdf.fonttype = 42`. Guard against missing Unicode symbols in `STIXGeneral` (e.g., render stars via `$\star$` or `DejaVu Sans`, not bare `★`).
5. **Prevent legend collisions cleanly**: keep top legends strictly inside the `[0, 1]` figure box via explicit `subplots_adjust(top=...)`; for paired subplots sharing baselines, replace two per-axis legends with one centered `fig.legend(..., ncol=N)`. On direct-labeled horizontal bars, drop vertical gridlines and allocate a dedicated clean lane (`> 3 pt` clearance) for `0.0%` baseline labels.

### Narrow-Column Formatting Coupling (Fix Together With Figures)
Before final sign-off, pair the figure geometry audit with a narrow-column LaTeX formatting pass targeting **0 body `Underfull \hbox (badness >= 2000)`**:
1. **Upright theorem list labels**: inside italic `theorem`/`proposition` environments, use `\begin{enumerate}[label=\textup{\arabic*.}]` so item numbers stay upright Roman and never mix italic digits with upright colons.
2. **Lift unbreakable wide inline formulas**: move long `sup`/probability/fraction inline formulas out of 3.3-inch columns into display equations to cure giant inter-word gaps.
3. **Tame long monospace identifiers**: scale monospace fonts to match Times x-height (e.g., `\usepackage[scaled=0.88]{zi4}` in USENIX/IEEE instead of unscaled Courier), enable breakable underscores (`\_\penalty0\hspace{0pt}`) or `\allowbreak`, and add `\hyphenation{...}` guards for technical words and system names.
4. **Audit `.bbl` capitalization and bibliography raggedness**: add `\raggedright` around `named.bst` bibliographies if narrow columns stretch DOIs/titles, and inspect `main.bbl` directly to brace-protect proper nouns and title words following `?` or `!` under `plain.bst`.

## Final checklist (all must be true)
- [ ] Intent sentence written; the figure shows it without the caption.
- [ ] Archetype chosen from the table; unique within the portfolio.
- [ ] One reading path; the claim or number is at its end.
- [ ] One accent hue for the contribution, one alert hue, everything else neutral; ≤ 4–5 hues in total.
- [ ] Real instance shown (query, code, timeline, data cells, text spans); ≤ 3 words per box.
- [ ] Every number traced to a results file.
- [ ] Body font family; every glyph ≥ 80% of body size (measure it: PyMuPDF spans or the pdf audit).
- [ ] Orthogonal edges, endpoints on borders, no edge through any non-endpoint container or title band.
- [ ] Labels in whitespace with ≥ 2 pt clearance; no overlapping text; nothing outside the canvas.
- [ ] `figure_geometry_audit.py`: 0 FAIL (and WARNs reviewed).
- [ ] 180 DPI render inspected by a person or agent other than the one who drew it.
- [ ] Caption opens with the claim; colour words decode the figure; symbols match the body text.
- [ ] Single column unless it is an overview or platform figure; page count unchanged.
