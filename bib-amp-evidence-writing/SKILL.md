---
name: bib-amp-evidence-writing
description: Review and revise AMP evaluation or generation manuscripts for Briefings in Bioinformatics using verified exemplars, claim-level citations, and distinct reviewer and editor roles. Use for scientific argument, evidence scope, results organization, or reference expansion; not for changing results to favor acceptance.
---

# BiB AMP evidence writing

Produce a scientific argument organized around an answerable evaluation question. Learn from published examples without treating their wording, page counts, reference counts, or graphic choices as journal requirements.

## Start from the requested work

- For paragraph structure, experiment narration, or figures, read [the bbac343 case study](references/bbac343-writing-experiment-map.md). It maps 37 prose paragraphs and the actual three figures/two tables, without reproducing the paper.
- For reference expansion or public reviewer-history research, read [source verification](references/source-verification.md), then the [measured publication sample](references/bib-publication-sample.md).
- When review and editing must be separate, follow [independent review and revision](references/review-editor-workflow.md). An independent agent reviews a frozen version; a different person/agent edits; the reviewer checks the revision. Do not label an editor's self-check as independent review.
- Access sources through the environment's authorized data interface. This skill grants no additional source, repository, publishing, or installation permissions.

## Scientific decisions that survive rewriting

1. **Distinguish evaluation units.** Reconstruction on observed sequences, generation from a prior, prediction of activity, and measured antibacterial activity answer different questions. Low-order residue/dipeptide summaries do not establish agreement of the full sequence distribution. AMP classification is not MIC regression. A published motivating example is not a reproduced baseline.
2. **Write what was measured.** Preserve dataset partitions, experimental units, seed/repeat counts, selection rules, thresholds, units and material disagreements. Do not manufacture replication, confidence intervals, statistical significance, sample attribution, prospective status, or completed validation. A few within-run samples do not replace independent training seeds.
3. **Use scientific rather than procurement prose.** Describe the tested peptide panel and assays directly. Procurement and file-handoff details can leave the main paper when irrelevant to the scientific question. The denominator follows the stated target population and endpoint, not which fraction looks better. Material exclusions or discordant measurements remain accessible and accurately contextualized.
4. **Retain counterevidence that changes interpretation.** Different rankings across metrics can be a useful result. Compression may relocate implementation detail to a supplement; it must not turn a limited result into a general claim.

## Organize the argument

Use the shape that fits the evidence, commonly:

- Introduction: domain need → specific evaluation gap → question → controlled comparison and contribution.
- Methods: data and units → common settings → changed factors → measurement/aggregation. Mention important implementation differences once; place full reproducibility detail in the supplement/repository.
- Results: one question per subsection; comparison → effect/count → figure/table → explanation or exception. Separate observed facts from plausible mechanisms.
- Discussion: answer → relation to prior work → actionable recommendation → concise scope. Keep limitations proportional and specific; do not repeat a project-audit narrative.

Each figure should answer a question. For a workflow, arrows must represent established data flow or attribution. For comparisons, show the applicable conditions and label the actual aggregation and uncertainty. Use [the AMP figure skill](../amp-figure-design/SKILL.md) when available for detailed design; this skill remains usable without it.

## Finish with two different checks

**Scientific and citation check:** each substantive claim is supported by the manuscript data or an accurately scoped source. Verify bibliographic identity against primary records and read the supporting passage; a resolving DOI alone is insufficient. Use the citation ledger described in the references.

**Mechanical closure check:** for LaTeX with explicit `\bibitem` entries, run:

```bash
python3 scripts/check_citation_closure.py --tex /path/to/main.tex --out /path/to/citation_closure.json
```

The offline checker follows local `\input`/`\include`, ignores comments and supported literal code forms (`\verb`, `\lstinline` and listed verbatim environments), and reports undefined citation keys, duplicate entries, and entries never cited. It expects one `thebibliography` per manuscript; check independent documents separately. It does not verify existence, source support, or claim truth. BibTeX/BibLaTeX, custom TeX expansion or dynamically generated citation keys require the normal bibliography build plus a separate audit. Recognized unsupported constructs return a failure; this lexical checker is not a general TeX interpreter.

Compile the final manuscript, inspect the edited pages and all changed figures/tables, confirm citation numbering and links, then report actual changes and remaining evidence limits. Keep internal review/verification reports separate from reviewer-facing prose unless the user requests their inclusion.
