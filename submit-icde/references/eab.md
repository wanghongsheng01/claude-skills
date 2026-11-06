# Submitting an ICDE "Experiment, Analysis, and Benchmark" (EAB) paper — ICDE 2027, Round 2

Every rule below was read on **2026-11-06** from public pages and is cited with its URL. Tags:
- **[CFP]**: https://icde2027.github.io/cf-research-papers.html (the call for research papers);
- **[SG]**: https://icde2027.github.io/submission-guidelines.html (an older page with partly different wording);
- **[ID]**: https://icde2027.github.io/important-dates.html;
- **[HOME]**: https://icde2027.github.io/ (news: "The Round 2 submission is open with deadline November 11, 2026");
- **[IEEE-ICDE]**: https://ieee-icde.org/ (series page, which links the 2027 edition at https://ieee-icde.org/2027 and lists earlier editions);
- **[INF]**: our inference from the rules. It is not a rule; re-check it.

The two official 2027 pages disagree in places; always follow the stricter reading. The general
checklist is in `../SKILL.md`. The full requirements snapshot is in `requirements-recheck-2026-11-06.md`;
the 2026-11-06 text matches it.

## 1. What an EAB paper is [CFP]
- The CFP defines two research-track categories: regular papers and the "Experimental, Analysis, and
  Benchmark (EAB)" category.
- EAB papers focus on "the extensive evaluation of algorithms, data structures, and systems that are of
  wide interest, or on benchmarks". The contribution is fundamentally new insight into the strengths and
  weaknesses of existing methods, or new ways to evaluate existing methods.
- [INF] A paper whose main contribution is a new method is a regular paper. A small "insight is
  actionable" variant is fine in an EAB paper. A headline new system mixed into a benchmark blurs the
  category; NL2SQL360 (PVLDB 2024) is an example, see `write-icde/references/eab.md`.
- [INF] Choose regular instead of EAB if you cannot release every artifact (section 3): for regular
  papers the CFP accepts an explanation; for EAB papers it does not.

## 2. Title tag
| Rule | Source |
|---|---|
| The title starts with `[Experiment, Analysis, and Benchmark]`: a prefix, with exactly this spelling ("Experiment", singular; "and" before "Benchmark"; commas). | [CFP] |
| The tag is removed in the camera-ready version. | [CFP], camera-ready section |
| Do not reuse the PVLDB or SIGMOD tags: PVLDB appends `[Experiment, Analysis & Benchmark]` as a suffix; SIGMOD 2027 uses the suffix `: [Experiments & Analysis]`. | https://vldb.org/pvldb/volumes/20/submission ; https://2027.sigmodconf.hosting.acm.org/calls_papers_sigmod_research.shtml (both read 2026-11-06) |
| After acceptance the title cannot change, except that reviewers may request a title change "to better align the paper's contents". | [CFP], [SG] |
| [INF] Enter the tagged title in the CMT title field too, so that the PDF and CMT agree. The CFP itself allows removing the tag at camera-ready, although CMT metadata are otherwise frozen. | [CFP] |

## 3. Artifacts and data availability (the EAB-specific hard rule)
| Rule | Source |
|---|---|
| EAB papers "MUST provide all artifacts necessary to reproduce the results. No exceptions in this paper category are allowed." | [CFP]; [SG] has the same sentence |
| All authors are expected to submit supplemental material (code, data, implementation artifacts); its availability "will be considered in the evaluation". Regular papers may explain in the submission form why they cannot. | [CFP] |
| Supplemental material must be at a URL on a standard, openly accessible file-sharing service with a well-understood privacy policy, for example a public GitHub repository. Personal web pages or anything that can track reviewers are not allowed. | [CFP] |

[INF] What follows for an EAB submission:
- **Public at the deadline.** The repository must be complete when you submit. "Will be released upon
  acceptance", "available on request" and private links contradict the "no exceptions" rule.
- **Every result reproducible from the package.** This means code, configurations, workloads, data or
  data generators, raw results, and scripts that redraw every table and figure. The PVLDB checklist is a
  good model; see `review-icde/references/eab.md` section 1.
- **LLM experiments.** Release:
  - the prompts;
  - the exact model identifiers, with access dates and parameters (temperature, max tokens);
  - the cached raw responses, because API models change and re-querying them does not give the same outputs;
  - the judge prompts and the human labels, if used.
- **Enterprise or personal data.** A dataset that cannot be released cannot carry an EAB result.
  - Release a de-identified version, a faithful synthetic generator, or the derived statistics needed to
    recompute every number, together with the scripts.
  - Otherwise drop that dataset from the EAB claims, or submit as a regular paper with an explanation in
    the form.
  - Never put internal hostnames, credentials or employee identifiers into the artifact.
- **Large files.** Put them in an archival store with a DOI (Zenodo, figshare, Hugging Face datasets) and
  link it from the GitHub README. Tag a release, for example `icde27-r2-submission`, so that reviewers
  see a frozen state.
- **Single-blind review.** Names in the repository are fine. Do not add analytics, link shorteners or
  forms that log visitors.

## 4. Format and length
| Rule | Source |
|---|---|
| IEEE conference template. Negative spaces or content entering the margins are format violations. | [CFP] |
| At most 12 pages for research and EAB papers, excluding only the references and the AI-generated content declaration. No appendix. PDF only. | [CFP]; [SG] says "AI-generated content acknowledgement" |
| ORCIDs are required for all authors at submission. | [CFP], [SG] |

[INF] EAB results sprawl, and the full per-query tables cannot go into an appendix. Keep every claim
supported inside the 12 pages, and put the extended tables in the artifact. Reviewers are not obliged to
open the artifact, and SemBench's "see the website" deferrals would be weak at ICDE.

## 5. Review model, conflicts of interest and CMT
| Rule | Source |
|---|---|
| Single-blind review. | [CFP], [SG] |
| At least 3 reviewers; a senior PC member coordinates and writes a meta-review. [SG] says "area chair". Outcome: accept or reject, with no revisions. | [CFP]; [SG] |
| A COI exists if the author and the PC or senior PC member: are co-authors of a submission under review; co-authored a paper published from 2023 to the present; co-authored 4 or more papers from 2016 to the present; were co-workers in the same company or university from 2023 to the present (declare these as Domain Conflicts); were collaborators in the past three years or from 2023 to the present (the CFP lists both wordings); have a primary thesis-advisor relation, no matter how long ago; or are relatives or close friends. | [CFP] |
| [SG] uses older wording: co-authors in the past three years; 4 or more in the last 10 years; co-workers in the past three years. It also lists "grant proposal in submission". | [SG] |
| Incorrect or incomplete COIs as of the submission closing time lead to desk rejection, and so do frivolous COIs. Automated software checks them. | [CFP] |
| Every author must create a CMT profile with domain and individual conflicts. If one author's profile is missing, the paper is desk-rejected. Conflicts are set via your name (top right) → Domain Conflicts / Individual Conflicts and apply to all your submissions. | [CFP] |
| Submit on CMT: https://cmt3.research.microsoft.com/ICDE2027 . The site opens a week before each deadline. | [CFP] |
| At most 5 research-track papers per author per round, regular and EAB combined. | [CFP], [SG] |

CMT steps are in `../SKILL.md` section 2a: profile, ORCID, domain conflicts, creating the paper record
early, then individual conflicts, the PDF, subject areas, the supplemental URL and the optional scope
statement.

## 6. AI-generated content acknowledgement [CFP]
- Generative AI tools may not be listed as authors.
- Use of AI-generated content (text, figures, images, code) must be disclosed in the acknowledgments.
  Name the system and the sections, and say briefly at what level it was used. This explicitly includes
  tools and LLMs "used for data processing, filtering, visualisation, and facilitating or running
  experiments". Editing and grammar enhancement fall outside the intent of the policy.
- The declaration does not count toward the 12 pages. It is mandatory at camera-ready.
- [INF] **EAB of LLM systems.** The evaluated LLMs, the LLM judges and any LLM used for labelling,
  data generation or filtering are "used for running experiments". Name them, with versions, in the
  acknowledgement, separately from any coding or writing assistant. The checker warns when the body
  names LLMs that the acknowledgement does not cover.

## 7. Desk-reject causes [CFP]
1. Not following the instructions for research papers. For EAB this includes [INF] a missing tag and
   missing artifacts.
2. Format or length violations.
3. COI violations, including frivolous ones.
4. Out of scope. The paper must fit a topic area and position itself within data-engineering research;
   typically related work explains how it builds on ICDE, VLDB or SIGMOD work.
   - [INF] A benchmark of pure ML models (forecasters, classifiers) needs an explicit data-engineering
     angle: workloads, systems, data quality or cost.
   - If unsure, fill in the 1000-character scope statement: (a) the challenge, (b) principled
     contributions with section references, (c) the core-venue work you build on.
   - "A similar paper appeared at ICDE" is not a valid argument.
- **Round 1 → Round 2.** Papers desk-rejected for COI or format in Round 1 may be resubmitted;
  out-of-scope papers may not. A paper rejected in Round 1 is not eligible for Round 2.
- **1-year wait.** A rejected paper cannot be resubmitted to ICDE for one year, including revisions of it.
  - [CFP] counts the year from the rejection; [SG] counts it from the last submission.
  - [INF] A rejected EAB paper cannot come back reworded as a regular paper within the year.
- **Duplicates and novelty.**
  - A paper under consideration at ICDE may not be under review anywhere else.
  - It must differ substantially from any prior publication longer than 4 double-column pages.
  - It must cite overlapping prior work even when that work is shorter, for example a workshop version of
    the benchmark.

## 8. Round 2 dates [CFP], [ID], [HOME]
| Event | Date (5:00 PM Pacific Time) | Beijing time |
|---|---|---|
| Submission due | 2026-11-11 | 2026-11-12 09:00 (PST, UTC−8) |
| Author rebuttal period | 2027-01-08 to 01-15 | ends 2027-01-16 09:00 |
| Notification (approximate) | 2027-02-10 | |
| Camera-ready | 2027-03-10 | |

- **Rebuttal.** ICDE publishes no format or length; check CMT. The rebuttal cannot change the paper, so
  anything a reviewer could demand as a new experiment must be in the paper before submission. Use the
  `review-icde` pre-submission loop.
- **Camera-ready** [CFP]:
  - upload through IEEE CPS, not CMT, with PDF eXpress validation;
  - keep the 12-page limit, remove the tag, keep the AI acknowledgement;
  - title, abstract, authors and CMT metadata unchanged;
  - one unique full registration per paper.
  - [SG] says presentation is not required, but the CFP assumes an author attends and presents.

## 9. EAB countdown (Round 2) [INF]
- **T−7 days.**
  - Freeze the experiment matrix and every number in the paper; regenerate all tables and figures from
    the raw results with the scripts.
  - Confirm that every dataset can be released.
- **T−5.**
  - Repository complete: README, `make reproduce` or an equivalent per-table command, environment file or
    Docker image, licence, data links with DOI, and the raw results.
  - A fresh clone on a clean machine regenerates at least one table end to end.
- **T−3.** Run `write-icde` (EAB register), the `review-icde` EAB review, `manuscript-writing-review` and
  `manuscript-proofcheck`.
- **T−2.**
  - CMT: every author has a profile, ORCID and both kinds of conflicts.
  - Create the paper record so that individual conflicts can be entered.
- **T−1.**
  - Run `python3 scripts/check_icde_submission.py paper/ --pdf paper/main.pdf --eab --artifact ../artifact`
    and reach 0 ERROR.
  - Tag the release, upload the PDF, paste the frozen repository URL into the supplemental field, and keep
    the CMT confirmation.

## 10. What the checker adds in EAB mode (`scripts/check_icde_submission.py --eab`)
EAB mode switches on when you pass `--eab` or when the title starts with the tag.
- **Tag spelling and position** (ERROR):
  - must be a prefix, with the exact ICDE spelling;
  - catches the PVLDB/SIGMOD variants and a tag placed as a suffix;
  - `--camera-ready` requires the tag to be gone.
- **Artifact link** (ERROR if missing in EAB mode). It warns when the link points to a personal page,
  a link shortener or cloud-drive sharing instead of a neutral public host.
- **"Upon acceptance", "on request" or "will be released"** wording about code or data (ERROR in EAB).
  So is wording that says data are proprietary or confidential and cannot be released.
- **Reproducibility facts in the text** (WARN if absent): hardware, number of runs or repetitions,
  dispersion (std, IQR, confidence interval), software or model versions; for LLM papers also
  temperature and cost (dollars or tokens).
- **AI acknowledgement**: warns when the body names LLMs (GPT, Claude, Gemini, Llama, Qwen, DeepSeek and
  others) but the acknowledgement does not mention their use in experiments.
- **`--artifact DIR`** (local clone of the repository), WARN for each missing item: README with run
  instructions; licence; environment specification (requirements, environment.yml, Dockerfile,
  Cargo.toml, pom.xml and similar); a scripts or experiments directory; raw results; plotting or
  table-generation scripts. It also flags files that look like secrets (`.env`, `*.pem`, `id_rsa`, key
  patterns) or internal hostnames/IPs.
