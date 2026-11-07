# Official-source refresh: 2026-11-07

The journal-specific guide has **not** been newly read in full: its exact official URL returned HTTP 403 through both the registered fixed-URL verifier and the public web reader. The existing 2026-11-05 full browser snapshot remains the basis of the journal-specific requirements. Do not convert this into a claim that rules have or have not changed.

The following existing official sources returned HTTP 200 through the registered read-only verifier on 2026-11-07; HTML text was complete, not truncated. Public web reading independently exposed the same relevant policy sections.

| Source | Verified use |
|---|---|
| [CVIU-linked CAS ZIP](https://assets.ctfassets.net/o78em1y1w4i4/5uFmLZJTPDMAUjFnHRpjj8/6f19a979146eb93263763d87a894ab0d/els-cas-templates.zip) | 3,305,507 bytes; SHA256 `36d97da01c6bbd134f315bff6c3de553735e2550444a6ddd4f869ddc67a20757`, unchanged from the previous verified bundle. This validates that exact resource, not every possible future template link. |
| [Canonical LaTeX instructions](https://www.elsevier.com/researcher/author/policies-and-guidelines/latex-instructions) | Source bundles must include dependencies; item types depend on the workflow. The FAQ concerning EM source submissions requires one folder level. A ZIP container does not explicitly waive this requirement. |
| [Journal AI policy](https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals) | Manuscript assistance requires accurate disclosure; research-method use belongs in Methods. Figure categories have different conditions. Primary evidence cannot be invented or retouched with generative tools; general-purpose generative-image tools are not allowed for graphical abstracts. |
| [Research-data options](https://www.elsevier.com/researcher/author/tools-and-resources/research-data/data-guidelines) | Option C requires repository deposit/linking, or a factual explanation when sharing is impossible. Which option CVIU selects remains based on its journal-guide snapshot. |
| [Review guidance](https://www.elsevier.com/reviewer/how-to-review) | The publisher emphasizes specific, evidence-supported comments and sufficient methods/statistics. This is not a confidential CVIU review record. |

## EM wording and scope

The LaTeX page's FAQ says: “LaTeX submissions containing subfolders cannot be processed by EM.”

This appears in manuscript-submission guidance, not a production-only section. The same page notes that many journals initially accept PDF, and explains source-file upload when requested; it does not establish that every initial submission immediately requires EM source conversion. Its archive recommendation contains no express exception for nested directories. Confirm the actual route and required stage, prepare a flat variant when applicable, and inspect the platform's proof. Do not claim the current CVIU account workflow was observed or that an existing nested package must fail without that observation.

A prior network-restricted probe failure and the subsequent successful fixed-source GET are separate events. Their statuses should remain separate in project provenance. Public skills need source URLs and policy scope, not private paths, author facts, or full publisher-page mirrors.
