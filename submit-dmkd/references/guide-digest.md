# Submission notes: Data Mining and Knowledge Discovery (DMKD)

Journal: *Data Mining and Knowledge Discovery*, Springer (Springer Science+Business Media, LLC, part of Springer Nature).
Print ISSN 1384-5810, electronic ISSN 1573-756X. Springer journal no. 10618.
All pages below were read on **2026-10-29** unless stated otherwise.

Tags:
- **[VERIFIED]**: read on an official DMKD page or on Springer/Springer Nature pages for this journal.
- **[SPRINGER-GENERIC]**: a Springer / Springer Nature policy that applies to DMKD.
- **[INFERRED]**: my conclusion from the evidence cited, not stated anywhere.
- **[UNKNOWN]**: could not be found in public sources.

Key URLs (all read 2026-10-29):
- G = Submission guidelines: https://link.springer.com/journal/10618/submission-guidelines
- A = Aims and scope: https://link.springer.com/journal/10618/aims-and-scope
- E = Editorial board: https://link.springer.com/journal/10618/editorial-board
- H = Journal home: https://link.springer.com/journal/10618
- P = How to publish with us (fees, licences): https://link.springer.com/journal/10618/how-to-publish-with-us
- X = Ethics & disclosures: https://link.springer.com/journal/10618/ethics-and-disclosures
- J = Springer journal policies (brand level): https://link.springer.com/brands/springer/journal-policies
- L = SN LaTeX author support: https://www.springernature.com/gp/authors/campaigns/latex-author-support
- S1 = Snapp, how to submit: https://www.springernature.com/gp/snapp/submitting/how-to-submit
- S2 = Snapp, common issues: https://www.springernature.com/gp/snapp/submitting/common-issues
- SUB = Submit link on the journal pages: https://submission.springernature.com/new-submission/10618/3
- ECML26 = ECML PKDD 2026 journal track: https://ecmlpkdd.org/2026/submissions-journal-track/
- RDP = SN research data policy: https://www.springernature.com/gp/authors/research-data-policy

---

## 1. Aims and scope, article types, and stance on benchmark/evaluation papers

- **Scope** [VERIFIED, A]. KDD covers theory and foundations, data mining methods, and algorithms. It also covers the **knowledge discovery process**, which A describes as "Data pre-processing for data mining, including data cleaning, selection, efficient sampling, and data reduction methods; evaluating, consolidating, and explaining discovered knowledge". Application issues include "data mining systems and tools". KDD is "concerned with issues of scalability, the multi-step knowledge discovery process … (including data cleaning and noise modelling)". The journal "accepts paper submissions of any work relevant to DMKD".
  - A also mentions "Short (2-4 pages) application summaries … in a special section". This category does **not** appear in the article-type list on G, so treat it as legacy text [INFERRED].
- **Article types to choose from in the portal** [VERIFIED, G, "Types of Papers"]. G says "make sure that your select the most suitable type during the submission process". The types are:
  1. **Regular Papers (Manuscripts)**
     - Judging criteria: (i) the main contribution is clear from the abstract; (ii) the motivation is a clearly defined research gap. G: "it is typically not enough that a paper presents a new method, it must a clearly defined research gap that can currently not be addressed with alternative methods"; (iii) success is shown by experiments that answer clearly formulated research questions, or by formal proofs.
     - Extended conference papers are submitted as Regular Papers (see §6).
  2. **Survey Papers**
     - This type explicitly includes "papers that report on extensive independent experimental comparisons of different competing approaches to a problem class".
     - Such papers need not contain a new research contribution, but must give a "comprehensive and novel point of view". They are judged on comprehensiveness, balance, and novel insight.
     - G: "A mere concatenation of summaries of previously published papers is typically not of interest". Surveys are shown in a separate Topical Collection.
  3. **Application Papers**
     - G: "A paper that experimentally compares different well-known algorithms on a newly collected dataset and concludes which of them performs best, is not sufficiently interesting for data mining researchers."
  4. **Contributions to Special Issues**
     - Must answer an open call. Judged additionally on relevance to the call.
  5. **Editorials**
     - Open only to guest editors.
- **Benchmark / evaluation-methodology / reproducibility papers** [VERIFIED for the quoted text; INFERRED for the conclusions].
  - DMKD has no separate "benchmark" or "datasets & benchmarks" type.
  - A large independent experimental comparison fits **Survey Papers**.
  - A paper whose main contribution is a new auditing or evaluation method fits **Regular Papers**. It must argue the research gap explicitly (criterion ii) and back its claims with research-question-driven experiments (criterion iii).
  - A "we ran known methods on a new dataset" paper is explicitly discouraged (Application Papers text).
  - On reproducibility, DMKD only has the generic SN data policy (§5). The ECML PKDD journal track additionally encourages "Reproducible Research", with code and data in standard repositories [VERIFIED, ECML26].
- **Special issues / collections** [VERIFIED].
  - The only open collection is "Quantification and Classification under Dataset Shift (QCDS 2026) – By Invitation Only", deadline 30 Nov 2026. No upcoming collections are listed. Source: https://link.springer.com/journal/10618/collections?filter=Open (and `?filter=Upcoming`).
  - FAQ on G: DMKD "generally do[es] not publish post-workshop or post-conference special issues".
- **ECML PKDD journal track**: see §8.

## 2. Editorial board

- **Editor-in-Chief**: Eyke Hüllermeier, Ludwig-Maximilians-Universität München, Germany [VERIFIED, E and H].
- **Advisory Board**: Aggarwal, Agrawal, Faloutsos, Fayyad, Mannila, Ramakrishnan, Smyth, Webb [VERIFIED, E].
- **Action Editors** (~50 listed) [VERIFIED, E]. Names relevant to data quality, cleaning, or evaluation work include:
  - Wil van der Aalst, Albert Bifet, Toon Calders, Michelangelo Ceci, Joao Gama, Aristides Gionis, Bart Goethals
  - Eamonn Keogh, Matthijs van Leeuwen, Alexander Marx, Pauli Miettinen, Eirini Ntoutsi, John Paparrizos, Heiko Paulheim
  - Panagiotis Papapetrou, Nikolaj Tatti, Mohammed J. Zaki, Min-Ling Zhang (Southeast Univ., China), Arthur Zimek, Albrecht Zimmermann, Indre Zliobaite
  - A separate "Editorial Board" list follows (Appice … Tong …).
- **How editors are assigned**:
  - G FAQ: "We have a hierarchical system, where action editors invite reviewers that seem suitable for a particular paper" [VERIFIED].
  - G FAQ: the EIC does a first evaluation, "typically done within 2 weeks or so" [VERIFIED].
  - Snapp status after the technical check is "Editorial assignment … the editorial team is selecting an editor" [SPRINGER-GENERIC, S1].
- **Can the author pick an action editor / "responsible editor"?**
  - **[UNKNOWN]** whether the DMKD Snapp form has a field for this. Nothing on G, A, E or S1 says authors choose one.
  - Evidence it is editor-assigned [INFERRED]: S1 describes editor selection by the editorial team. Five 2025–2026 DMKD articles I checked carry **no** "Responsible editor" line (older DMKD papers did). The checked articles are 10.1007/s10618-026-01283-y, -01278-9, -01281-0, -01274-z and 10.1007/s10618-025-01147-x.
  - Safe practice [INFERRED]: name 1–3 fitting action editors in the cover letter as a *suggestion*, phrased as optional.

## 3. Submission system and portal fields

- **System: Springer Nature "Snapp"**, not Editorial Manager.
  - The journal's "Submit your manuscript" link is `https://submission.springernature.com/new-submission/10618/3` [VERIFIED, G/H]. It opens a Springer Nature account login: "Log in, or register a new account to continue with your submission to Data Mining and Knowledge Discovery", with email / Google / ORCID options.
  - ECML26 also says DMKD uses "the relevant journal's dedicated SNAPP submission platform" [VERIFIED].
  - I did not log in, so the DMKD-specific form screens were **not seen**.
- **Steps in Snapp** [SPRINGER-GENERIC, S1]:
  1. Prepare the files, then write the cover letter. S1 advice: "Keep it focused and to a single page". State the title, what was done and found, and why it suits the journal.
  2. Upload the manuscript and cover letter. For LaTeX this is "a .zip file containing LaTeX files … our system automatically compiles them into a PDF for peer review".
  3. Confirm the auto-extracted data: "title, abstract, and author details, are automatically extracted".
  4. Provide extra information:
     - author details and affiliations
     - corresponding author
     - funding details
     - authorship statement
  5. "Agree to our policies and open access requirements, and disclose any competing interests, dual publication, or use of third-party material."
  6. Review the submission. There is an option to "share your work as a preprint on Research Square" (In Review). Then "Submit Manuscript".
- **DMKD-specific statements about portal fields** [VERIFIED, G]:
  - **Article type** must be selected.
  - **Author Contribution** and **Competing Interest** information "must be provided at submission via the submission interface. Only the information submitted via the interface will be used in the final published version." Editorial-board members who are authors must declare this under Competing Interest.
  - **Funding** must be disclosed "upon submission … in the peer review system" (feeds CrossMark). It must also appear in the manuscript's Declarations (G, "Competing Interests" section).
  - **Extended conference version**: "this request must be made at the time of submission". State the conference publication and provide a statement of revisions.
  - **Suggested / excluded reviewers** are welcome. Reviewers must be independent and come from a mix of countries and institutions. For each one the Corresponding Author "must provide an institutional email address … or … other means of verifying the identity … in the submission letter".
    - Brand policy J adds: "usually a maximum of two people/research groups" for exclusions; give the suggested reviewer's "institutional email address and ORCID or Scopus ID"; "Each manuscript should be reviewed by at least one reviewer who was not suggested by the author" [SPRINGER-GENERIC].
  - **Source files**: "provide all relevant editable source files at every submission and revision. Failing to submit a complete set of editable source files will result in your article not being considered for review". The LaTeX submission should include "the original source (including all style files and figures) and a PDF version of the compiled output".
- **Preprint disclosure**: "Authors should disclose details of preprint posting, including DOI and licensing terms, upon submission" [SPRINGER-GENERIC, J "Preprint sharing"].
- **Snapp LaTeX technical rules** [SPRINGER-GENERIC, L]:
  - "If you are submitting to Snapp your files must be able to compile using pdflatex and must be compressed in .zip format."
  - The SN processing platform compiles with **TeX Live 2021**.
  - No custom fonts. Convert diacritics to TeX codes (`\"a`).
  - The FAQ (written for EM/eJP) says: don't use subfolders, use local `\includegraphics` paths, and the most reliable route is to paste the `.bbl` content into the `.tex`. [INFERRED: also do this for Snapp.]
  - The template header says: "Please do not use \input{...} … Submit your LaTeX manuscript as one .tex document" [VERIFIED, sn-article.tex].
- **Field-by-field list of the DMKD Snapp form** (keywords field, related manuscripts, opposed reviewers, data availability box, editor suggestion, previous-submission question, etc.): **[UNKNOWN]**. It is visible only after login. Expected from S1 and G [INFERRED]: article type; collection (for special issues or ECML PKDD); file upload; title/abstract/keywords confirmation; authors, affiliations, ORCID; funding; competing interests; author contributions; dual-publication and third-party material questions; policy/OA agreement; Research Square preprint opt-in.

## 4. Manuscript preparation

- **Format** [VERIFIED, G "Text"].
  - "Manuscripts should be submitted in LaTeX. We recommend using Springer Nature's LaTeX template." Word files are also accepted.
  - Headings: "decimal system of headings with no more than three levels".
  - Define abbreviations at first use. Footnotes, never endnotes. No figures in footnotes.
- **Template downloaded** [VERIFIED, L]: "Download the journal article template package (December 2024 version)" (ZIP, 880.68 KB). Overleaf: https://www.overleaf.com/latex/templates/springer-nature-latex-template/gsvvftmrppwq. Details in "Template files" below.
- **Reference style** [VERIFIED, G "References"]:
  - **Author–year**. G: "Cite references in the text by name and year in parentheses", e.g. "(Thompson 1990)", "Becker and Seligman (1996)", "(Abbott 1991; Barakat et al. 1995a, b; …)".
  - The list is **alphabetized** by first author, then chronologically.
  - Include full DOI links if available.
  - Springer basic format: `Gamelin FX, Baquet G, … (2009) Title. Eur J Appl Physiol 105:731-738. https://doi.org/…`. Abbreviate journal names per ISSN LTWA.
  - Published 2025–2026 DMKD papers follow exactly this: "(Zhou et al. 2021)"; "Han L, Chen XY, Ye HJ, et al (2024) Softs: … In: Globerson A, … (eds) Advances in neural information processing systems, vol 37. … pp 64145–64175" [VERIFIED, 10.1007/s10618-026-01281-0, 10.1007/s10618-025-01147-x].
- **Recommended `\documentclass`**: `\documentclass[pdflatex,sn-basic]{sn-jnl}`. Do **not** add `Numbered`.
  - [VERIFIED] In `sn-jnl.cls`, `sn-basic` without `Numbered` loads `natbib[authoryear]`, sets `\setcitestyle{aysep={}}` (gives "(Thompson 1990)" with no comma) and `\bibliographystyle{sn-basic}`. With `Numbered` it would switch to `[numbers,sort&compress]`.
  - [INFERRED] `sn-basic` is the "Basic Springer Nature Reference Style", which is what G prescribes. `sn-mathphys-ay` is also author–year but a different format.
  - Use `\citep{}` / `\citet{}`. The sample `sn-article.tex` defaults to `sn-mathphys-num` (numbered), so this must be changed.
  - `pdflatex` is required by Snapp (L).
- **Length / page limits** for regular DMKD papers: **none stated** [VERIFIED absence on G]. The ECML PKDD journal track only: recommended ≤20 pages including references; >23 pages is a desk reject; unlimited appendices allowed [VERIFIED, ECML26].
- **Abstract**: "150 to 250 words", with no undefined abbreviations or unspecified references [VERIFIED, G].
- **Keywords**: "4 to 6 keywords" [VERIFIED, G]. ECML JT cover letter additionally asks for 5 general and 5 specific keywords [VERIFIED, ECML26].
- **Title page** [VERIFIED, G]:
  - concise, informative title
  - author names
  - affiliations (institution, department, city, state, country)
  - corresponding author clearly marked, with an active email
  - 16-digit ORCID "if available"
  - In sn-jnl: `\author*[1]{\fnm{} \sur{}}\email{}`, `\affil*[1]{\orgdiv{}, \orgname{}, \orgaddress{\city{}, \country{}}}`.
- **Review model / anonymization**: DMKD is **single-anonymous**. X: "Research content published in this journal is peer reviewed (single-anonymous)" [VERIFIED]. Do **not** anonymize; author names stay on the manuscript.
- **Line numbering, spacing, columns**: no DMKD requirement [VERIFIED absence on G].
  - The class offers `lineno` (line numbers), `referee` (double spacing) and `iicol` (two-column). Default is single column [VERIFIED, cls / sample tex].
  - Recommended: single column; `lineno` optional (it helps reviewers) [INFERRED].
- **Figures** [VERIFIED, G "Artwork"]:
  - Preferred formats: EPS (vector) and TIFF (halftones). Embed fonts. Name files Fig1.eps, etc.
  - Minimum resolution: line art 1200 dpi, halftone 300 dpi, combination 600 dpi. RGB. Lines ≥0.1 mm.
  - Lettering in Helvetica/Arial at 8–12 pt. No titles inside figures.
  - Caption starts with bold "**Fig. 1**", with no final punctuation.
  - Width 84 mm (double-column area) or 174 mm (single-column area), height ≤234 mm.
  - Accessibility: patterns as well as colour; contrast ≥4.5:1.
  - Generative-AI images: follow the SN policy.
  - [INFERRED] With pdflatex, vector PDF figures are the practical choice. Snapp's common issues ask for "plain text captions and be of a high resolution", with no captions embedded in images [S2].
- **Tables**: Arabic numerals, cited in order, with a caption. Table footnotes use superscript lower-case letters [VERIFIED, G].
- **Supplementary Information** [VERIFIED, G]:
  - Cite in the text as "Online Resource n". Name files ESM_n.ext.
  - Text material as PDF; spreadsheets as .csv/.xlsx; multiple files can go in a .zip.
  - Published "as received".
  - Put title, journal, author names and corresponding author's email in each file.
- **Acknowledgements**: G (generic text) says to put them "in a separate section on the title page"; write funder names in full [VERIFIED]. In sn-jnl use `\bmhead{Acknowledgements}` in `\backmatter` [VERIFIED, template]. Published DMKD papers print "Acknowledgements" after the references [VERIFIED, 10.1007/s10618-026-01283-y].
- **Math**: no DMKD rules beyond the template. The template loads amsmath/amssymb/amsthm and theorem styles `thmstyleone/two/three` [VERIFIED, sn-article.tex].

### Template files (downloaded 2026-10-29)

- Source URL (linked from L): https://cms-resources.apps.public.k8s.springernature.io/springer-cms/rest/v1/content/18782940/data/v12
- Server filename: "Download the journal article template package (December 2024 version).zip". 901,814 bytes. SHA-256 `812e76dcaa9c28dc1bff1fb6065d51729b67d4ea140552a05088317414a3ecae`.
- Saved as `research/sn-template/download/sn-article-template.zip` and unzipped into `research/sn-template/unzipped/sn-article-template/`. Nothing was executed.
- Version:
  - `sn-article.tex` header: `%Version 3.1 December 2024`.
  - Zip entries are dated 2024-12-13.
  - `sn-jnl.cls` still declares `\ProvidesClass{sn-jnl}[2019/11/18 v0.1 …]` (a stale header string).
- Files:
  - `sn-jnl.cls`
  - `sn-article.tex` (sample) and `sn-article.pdf` (compiled sample)
  - `sn-bibliography.bib`
  - `user-manual.pdf`
  - `fig.eps`, `empty.eps`
  - `bst/` folder: `sn-basic.bst`, `sn-mathphys-num.bst`, `sn-mathphys-ay.bst`, `sn-apacite.bst`, `sn-aps.bst`, `sn-chicago.bst`, `sn-nature.bst`, `sn-vancouver-num.bst`, `sn-vancouver-ay.bst`
- Class options found:
  - Reference styles: `sn-basic`, `sn-mathphys-num`, `sn-mathphys-ay`, `sn-aps`, `sn-vancouver-num`, `sn-vancouver-ay`, `sn-apa`, `sn-chicago`, `sn-nature`, `Numbered`
  - Layout and output: `pdflatex`, `lineno`, `referee`, `iicol`, `twocolumn`/`onecolumn`, `a4paper`, `draft`, `remarkboxoff`, `bibcomment`
- For the Snapp upload [INFERRED]:
  - Copy `bst/sn-basic.bst` next to `main.tex` (no subfolder).
  - Paste the generated `.bbl` into the `.tex`, or ship `.bib` + `.bst`.
  - Keep a flat directory.
  - Include `sn-jnl.cls`.

## 5. Statements and Declarations, data policy, AI policy

- **Mandatory section** [VERIFIED, G "Title Page → Statements and Declarations"]. G: "The following statements should be included under the heading 'Statements and Declarations' for inclusion in the published paper. Please note that submissions that do not include relevant declarations will be returned as incomplete."
  - G explicitly lists **Competing Interests**.
  - G's "Summary of requirements" adds: place the statements "in a 'Declarations' section before the reference list under a heading of 'Funding' and/or 'Competing interests'. Other declarations include Ethics approval, Consent, Data, Material and/or Code availability and Authors' contribution statements."
- **Template headings** [VERIFIED, sn-article.tex]. `\section*{Declarations}` with:
  - Funding
  - Conflict of interest/Competing interests ("check journal-specific guidelines for which heading to use")
  - Ethics approval and consent to participate
  - Consent for publication
  - Data availability
  - Materials availability
  - Code availability
  - Author contribution
  - Template rule: "If any of the sections are not relevant … include the heading and write 'Not applicable'".
- **Recommended block for DMKD** [INFERRED from G + template]. Use `\section*{Statements and Declarations}` placed before the bibliography (after `\backmatter`), with these sub-headings:
  - **Funding**
  - **Competing interests** (G uses this term)
  - **Ethics approval and consent to participate**
  - **Consent for publication**
  - **Data availability**
  - **Materials availability**
  - **Code availability**
  - **Author contributions**
- **Wording samples from G** [VERIFIED]:
  - Funding: "This work was supported by […] (Grant numbers […] and […])"; "No funding was received for conducting this study."
  - Competing interests: "The authors have no competing interests to declare that are relevant to the content of this article." Or "The authors have no relevant financial or non-financial interests to disclose."
  - Disclose interests within the last 3 years: funding, employment, financial and non-financial interests (e.g. editorial-board positions).
  - Author contributions: free text ("All authors contributed to the study conception and design. … The first draft of the manuscript was written by [full name] …") or CRediT ("Conceptualization: …; Methodology: …; …").
- **How published DMKD papers display them** [VERIFIED, 4 articles from Oct 2026 + 1 from Aug 2025]:
  - "Data availability" appears before References.
  - "Ethics declarations → Conflict of interest: The authors declare no conflict of interest."
  - "Contributions" appears under Author information.
  - "Funding" appears where present.
  - So production re-flows these from the interface data. The manuscript must still contain them (G).
- **Research data policy** [VERIFIED, G; SPRINGER-GENERIC, RDP]:
  - DMKD "follows Springer Nature research data policy". "Sharing of all relevant research data is strongly encouraged and authors must add a Data Availability Statement to original research articles."
  - SN now has a single **standard** policy rather than the old numbered "Type 1–4" labels. RDP says:
    1. All original articles must include a data availability statement.
    2. Public sharing is strongly encouraged, and community-endorsed data types are mandated.
    3. "Peer reviewers are entitled to request access to underlying data (and code)".
    4. If data cannot be shared, state the access conditions.
  - The brand page (J) says the policy meets TOP Guidelines Level 1.
  - Cite datasets in the reference list with a persistent identifier, following DataCite minimum fields (G).
- **AI / LLM policy**:
  - DMKD page [VERIFIED, G "Title Page"]:
    - LLMs "do not currently satisfy our authorship criteria".
    - "Use of an LLM should be properly documented in the Methods section (and if a Methods section is not available, in a suitable alternative part) of the manuscript."
    - "AI assisted copy editing" (readability, style, grammar, spelling, tone) "does not need to be declared". Generative editorial work and autonomous content creation are not counted as copy editing.
    - Generative-AI images: follow the SN policy.
  - Current brand-level policy [SPRINGER-GENERIC, J "Artificial intelligence (AI)", as read 2026-10-29]:
    - A newer **risk-assessment framework**.
    - Green (assistive, e.g. language polishing): "Permitted. Disclosure enhances trust and transparency".
    - Amber (evaluative or interpretive use, e.g. "Extensive copy editing or writing support", suggesting methods, drafting summaries): "Permitted with human oversight, verification, and transparency through disclosure".
    - Red: not permitted. Examples include "Fabricating data, citations or results", using an LLM to generate core research reasoning without disclosure, and AI authorship.
    - Authors: "Disclose AI use for trust and transparency".
    - The citations policy also bans "non-existent/hallucinated references".
  - [INFERRED] The two texts differ slightly. Safe practice:
    - Describe any AI used in the research pipeline (e.g. LLM-based repair or auditing components) in Methods/Experimental setup.
    - Add a one-line AI-use disclosure for anything beyond light copy editing. The journal text points to the Methods section; a short note in Acknowledgements or Declarations is optional extra transparency.

## 6. Policies

- **Duplicate / concurrent submission**: not allowed [VERIFIED, G]. "The manuscript should not be submitted to more than one journal for simultaneous consideration". No salami slicing. Be transparent about text reuse (text recycling). Plagiarism software is used. Snapp: "Submissions to multiple journals at the same time isn't allowed" [SPRINGER-GENERIC, S2].
- **Extended conference papers** [VERIFIED, G]:
  - Accepted as Regular Papers. "This request must be made at the time of submission; the authors must clearly state the conference publication and provide a statement of revisions/updates".
  - FAQ: "There is no strict rule on how much new material a paper should contain, but it must contain enough new material to provide a significant contribution beyond the conference paper." Acknowledge the prior publication in the paper. Clarify what is new. Ensure there is no copyright infringement.
  - **No fixed % threshold** (e.g. no "30%" rule) [VERIFIED absence].
  - The ECML PKDD journal track does **not** accept journal versions of conference papers [VERIFIED, ECML26].
- **Previously rejected papers / resubmission**:
  - Regular DMKD: no explicit policy on G [UNKNOWN].
  - Journal track: "Papers rejected by a previous submission deadline may not be resubmitted to any subsequent deadline … papers rejected by the Machine Learning Journal may not be resubmitted to the Data Mining and Knowledge Discovery journal, and vice versa"; ineligible papers "can be resubmitted as regular papers" [VERIFIED, ECML26].
  - Springer Transfer Desk suggests other SN journals after rejection [SPRINGER-GENERIC, S1].
  - A paper previously rejected by *another* publisher's journal (e.g. Elsevier IS) is not restricted. Ordinary practice is to not mention it unless asked [INFERRED].
- **Preprints / arXiv**: allowed.
  - G FAQ: "Can I make a pre-print of my paper available on arXiv? Yes, but you need to link and reference the official publication." [VERIFIED]
  - Brand policy: posting at any time "is not considered prior publication". Disclose the preprint DOI/licence at submission. After publication, update the preprint with the DOI. Any licence, including CC, is fine [SPRINGER-GENERIC, J].
  - Self-archiving page linked from G: https://www.springer.com/gp/open-access/authors-rights/self-archiving-policy/2124 (not opened; embargo details [UNKNOWN]).
- **ORCID**: recommended, not mandatory. G: "If available, the 16-digit ORCID"; "Authors are recommended to use their ORCID ID … or acquire an ORCID ID via the submission process" [VERIFIED]. Snapp login offers "Continue with ORCID" [VERIFIED, SUB].
- **Authorship changes**: author list and order must be correct at submission. Changes during revision are at the EIC's discretion, and none are allowed after acceptance [VERIFIED, G].
- **Open access / fees** [VERIFIED, P]:
  - Hybrid journal. Subscription publishing has **no charge**. The OA choice is made **after acceptance**.
  - APC: "£2390.00 GBP / $3390.00 USD / €2790.00 EUR", plus VAT where applicable, priced at the acceptance date.
  - OA licences: CC BY 4.0 or CC BY-NC-ND 4.0, with authors keeping copyright.
  - Colour online is free.
- **Transformative agreements (China)** [SPRINGER-GENERIC]:
  - https://www.springernature.com/gp/open-science/oa-agreements/china lists only **one** mainland institution with a Springer-brand agreement ("National Institute of Parasitic Diseases China").
  - So there is no broad agreement for Chinese universities. Check by institution at https://link.springer.com/journal/10618/funding-eligibility?bpid=no-bpid (not opened).
- **Copyright** [VERIFIED, G + P + articles]:
  - Subscription route: authors sign a Publication Agreement that "licenses exclusively to Springer the right to distribute". Published subscription articles say "Springer Nature or its licensor … holds exclusive rights to this article under a publishing agreement" (10.1007/s10618-026-01283-y).
  - OA route: no copyright transfer (CC licence).
- **Third-party material**: you need permission for print and online, with evidence at submission [VERIFIED, G].

## 7. Review process facts

- **Peer review type**: single-anonymous [VERIFIED, X]. Under SN anonymized review, "The pre-publication history of articles is not made available online", so **reviews are not published** [SPRINGER-GENERIC, J "Peer review models"]. Authors receive the reports with the decision [SPRINGER-GENERIC, J].
- **Timing** [VERIFIED]:
  - H: "Submission to first decision (median) 3 days". This most likely reflects desk decisions [INFERRED].
  - G FAQ: EIC first evaluation "typically … within 2 weeks or so"; regular review "usually take[s] 1-3 months, sometimes more"; "it is very rare that a paper is accepted after the first submission, accepted papers often undergo two or three iterations".
  - Examples of received → accepted: 22 Oct 2025 → 30 Sep 2026; 30 Nov 2025 → 30 Sep 2026; 25 Feb 2026 → 19 Sep 2026; 8 Jun 2025 → 20 Jul 2025 [VERIFIED, articles listed in §2].
  - Snapp generic: "Around 97% of accepted submissions require at least one revision" [SPRINGER-GENERIC, S1].
- **Metrics**:
  - Journal Impact Factor **5.5 (2025)**; 5-year JIF **6.7 (2025)**; downloads 563.9k (2025) [VERIFIED, H].
  - Scopus **CiteScore 2025 = 9.7** (3,483 citations / 358 documents, 2022–2025, calculated 05 May 2026); CiteScoreTracker 2026 = 10.6 (updated 05 Oct 2026); SJR 2025 1.200; SNIP 2025 2.333 [VERIFIED, https://www.scopus.com/sourceid/13579, Scopus preview].
  - Acceptance rate: **[UNKNOWN]**, not published on the journal pages.
- **Indexing**: SCIE, Scopus, EI Compendex, DBLP, ACM DL, CNKI, etc. [VERIFIED, H].

## 8. ECML PKDD journal track (do not confuse with a regular submission)

- **Relationship** [VERIFIED, ECML26]:
  - A joint track run with the *Machine Learning* journal and *DMKD*.
  - Submit the full paper to the journal's Snapp **choosing the Collection "ECMLPKDD 2026"**, and also to CMT (`https://cmt3.research.microsoft.com/ECMLPKDDJT2026/`) for bidding and conflicts. Missing either submission, or submitting to both journals, means a desk reject.
  - Accepted papers appear in the DMKD collection "ECML PKDD 2026" (e.g. 10.1007/s10618-026-01278-9). Authors commit to presenting at the conference.
- **2026 rules** (cutoffs **30 Oct 2025** and **15 Jan 2026**, AoE) [VERIFIED, ECML26]:
  - Page limits: ≤20 pages recommended; >23 pages is a desk reject; 21–22 pages are scrutinized.
  - **DMKD cover letter ≤2 pages** answering:
    - the main claim
    - the evidence
    - 3–5 closely related works from the last 7 years by researchers outside the group
    - 5 general + 5 specific keywords
    - institutional-conflict email domains and Guest Editorial Board conflicts
    - up to 4 suggested reviewers, and optionally up to 4 to exclude (no PhD students)
  - No journal versions of conference papers. No surveys.
  - Single-blind review. Gen-AI use must be documented in the cover letter. At least one author must be a qualified reviewer.
  - Initial decision about 10 weeks after the cutoff.
- **2027 status**:
  - Official page: ECML PKDD 2027 is in Eindhoven, 30 Aug – 3 Sep 2027 [VERIFIED, https://ecmlpkdd.org/2027/]. A third-party listing says 20–24 Sep; the official page wins.
  - **No 2027 journal-track call is posted** (https://ecmlpkdd.org/2027/submissions-journal-track/ returns 404).
  - DMKD shows no upcoming or open ECML PKDD 2027 collection [VERIFIED, collections page].
  - By pattern, cutoffs would likely be around Oct 2026 – Feb 2027 [INFERRED].
- **For a regular submission** [INFERRED]: choose the regular article type and **do not select an ECML PKDD collection**. Regular papers carry no conference-presentation obligation and no 20-page cap.

---

## Open questions for the author

1. **Article type**: Regular Paper (new auditing/repair method plus experiments) or Survey Paper (extensive independent experimental comparison)? This sets the judging criteria (§1).
2. **Prior versions**: is any part of the work published at a conference or workshop? If so, it must be declared at submission with a statement of new content (§6). Also, should the paper be framed as a resubmission of a manuscript rejected elsewhere? (No DMKD rule; normally not mentioned.)
3. **Preprint**: is there an arXiv preprint? If so, give its DOI/ID and licence for the portal (§6). Opt in or out of Research Square "In Review" at the last Snapp step.
4. **Reviewers**: which reviewers to suggest (independent; mix of countries; institutional emails / ORCID / Scopus IDs) and which, if any, to exclude (max ~2)? Optionally, which action editors to name in the cover letter (e.g. Paparrizos, Zimek, Paulheim, Marx, Ntoutsi, Gionis)? Whether the form has an editor field is UNKNOWN.
5. **Declarations content**: funders and grant numbers; competing interests (any DMKD board links?); CRediT contributions; data and code availability (repository URL/DOI for code, benchmarks and repaired datasets); ethics/consent ("Not applicable" unless human-subject data).
6. **AI-use disclosure**: was any LLM used in the method or experiments (document in Methods) or for writing beyond light copy editing (disclose)?
7. **Open access**: subscription (free) or OA (APC USD 3390 / EUR 2790 / GBP 2390)? This is decided after acceptance. Check institutional eligibility (mainland China coverage is minimal).
8. **Portal-only items to confirm on screen**: the exact list of Snapp fields (keywords count enforcement, related-manuscripts box, opposed reviewers, data-availability box, cover-letter upload slot, previous-submission question). These were UNKNOWN without login.
9. **Bibliography packaging**: inline the `.bbl` into the single `.tex` (most robust), or upload `.bib` + `sn-basic.bst`? Use line numbers (`lineno`)?
