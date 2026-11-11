# ICDE 2027 research track: must-follow items for the submitted PDF

Read on 2026-11-11 from the official pages:
- https://icde2027.github.io/cf-research-papers.html
- https://icde2027.github.io/submission-guidelines.html

Both pages are byte-identical to the 2026-11-10 snapshot. The last site commit, `eeabdfdc` on 2026-11-09, changed only the demo dates. Quotations below are short fragments.

| # | Rule (paraphrased; short quotes) | Checked by | Consequence |
|---|---|---|---|
| 1 | IEEE format. "negative spaces, content entering the margins, or similar" are format violations | C01, C02; visual pass for margins | desk reject ("Formatting violations") |
| 2 | Research and EAB papers: at most 12 pages, "excluding references and the AI-generated content declaration". | C04 | desk reject |
| 3 | "No appendix is allowed". | C05 | desk reject |
| 4 | PDF only (CMT also caps uploads at 20 MB). | C03 | upload refused |
| 5 | Single-blind review: author names and affiliations are shown. | C07 | — |
| 6 | Mandatory disclosure of AI-generated content (text, figures, images, code) in the acknowledgments. Name the AI system and identify the sections that use AI content, with the level of use. Tools used for data processing or experiments are named too. AI cannot be an author. | C06 | desk reject (non-compliance with instructions); the CR notes say the disclosure is "mandatory" |
| 7 | EAB title starts with "[Experiment, Analysis, and Benchmark]". The tag is removed in the camera-ready. | C08 | — |
| 8 | Supplemental material through a standard open service, such as a public GitHub repository; no personal web pages. EAB papers must provide all artifacts, "No exceptions". | C09 | availability is considered in review; for EAB, missing artifacts are a hard failure |
| 9 | At most 5 submissions per author per round, research and EAB combined. | CMT (icde-cmt-submission) | desk reject |
| 10 | Relevance to data engineering. If scope may be questioned, explain within 1,000 characters on the form. | icde-cmt-submission (Relevance) | desk reject |
| 11 | Every author has a CMT profile with domain and individual conflicts. | CMT (author action) | desk reject |
| 12 | Original work, not in a prior publication longer than 4 double-column pages. | author statement | reject |
| 13 | After acceptance, the title and authors cannot change. In the final version the title, abstract, authors and other CMT metadata cannot change. | icde-cmt-submission | — |

The call has no rule about the citation style beyond "IEEE format". The IEEE conference template uses numeric `[n]` citations with `IEEEtran.bst`, and C12 checks this.

## Reference integrity

The call does not mention reference integrity. Integrity is covered by:
- IEEE's publication ethics;
- the AI guideline the call cites (https://icbc2025.ieee-icbc.org/ai-content-generation-guidelines): authors "remain responsible" for the "veracity" of AI-edited text.

An invented reference counts as fabrication. A wrong citation counts as a misrepresentation. Either one discredits the paper with reviewers.
