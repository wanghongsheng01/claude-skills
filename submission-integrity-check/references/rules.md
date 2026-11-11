# Rules of compliance_check.py and ref_check.py

## compliance_check.py (per venue profile)

| Rule | What | Level |
|---|---|---|
| C01 | `\documentclass` and options match the profile (IEEEtran, conference). Flags 9pt/11pt/12pt, draftcls and onecolumn. | ERROR |
| C02 | Spacing, margin and font hacks: negative `\vspace`/`\hspace`, `geometry`, `\enlargethispage`, changed text block, `\baselinestretch`/`\linespread`, negative float or caption skips, body text below 9 pt, font packages that override the template. `\tiny`/`\scriptsize` is a WARN. | ERROR |
| C03 | PDF size (≤ profile limit) and page size (US Letter). | ERROR |
| C04 | Body pages up to the first of the References heading and the AI-declaration heading must be ≤ the limit. A heading at the top of a page means the body ended on the previous page. | ERROR |
| C05 | No appendix: an Appendix heading in the PDF, or `\appendix` in the source. Pointers to an "extended version" or "technical report" are a WARN. | ERROR |
| C06 | AI-generated content declaration present, names an AI system and the sections it covers. | ERROR / WARN |
| C07 | Single-blind: author block present and not anonymised; e-mails on page 1. | ERROR |
| C08 | EAB: the title starts with the profile's tag. Also flags the tag on a non-EAB paper. | ERROR |
| C09 | Artifact URLs on standard services are reachable (HTTP 200). Links to personal pages or private sharing services are a WARN. For EAB, no URL at all is an ERROR. | ERROR |
| C10 | No `??`, `[?]`, TODO, FIXME, XXX or TBD in the PDF text. | ERROR |
| C11 | All fonts are embedded. Type 3 fonts are a WARN (fix before the camera-ready). | ERROR |
| C12 | The number of entries in the reference list matches the distinct cited keys; numeric IEEE style; the bst is the profile's. | WARN |

## ref_check.py

### Format lint (cited entries only)

- ERROR:
  - a key cited but missing from the .bib;
  - an implausible year (in the future, or before 1600);
  - the same title cited under two keys.
- WARN:
  - a required field is missing for the entry type;
  - the author list is cut short with `and others` or "et al.";
  - a `@misc` entry has no URL;
  - a DOI is malformed;
  - placeholder or "to appear / under review / submitted" text.
- INFO:
  - a web reference has no access date;
  - one venue is written more than two ways.

### Online verdicts

`VERIFIED`, `CHECK`, `SUSPECT`, `NOT_FOUND` and `WEB` are defined in SKILL.md. `CHECK` reasons are:

- the title wording differs (similarity 0.85–0.93, with the first author and year matching);
- the first author is missing from the record;
- the year differs by more than 1;
- the venue family differs (for example ICLR vs NeurIPS, PVLDB vs SIGMOD);
- the DOI is not found;
- the paper is cited as arXiv/CoRR, but a peer-reviewed version exists;
- a web URL does not return 200.

### Sources, in order

1. Crossref by DOI.
2. Crossref bibliographic search, with the first author.
3. OpenAlex search.
4. Second pass when needed: title-only queries to Crossref and OpenAlex.
5. arXiv: exact title, then all title words, then the part before the colon.
6. The entry's own URL: the PDF's first pages or the landing page, for venues that are not indexed.
