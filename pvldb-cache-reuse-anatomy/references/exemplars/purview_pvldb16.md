# Exemplar deconstruction: Microsoft Purview (PVLDB 16(12), 2023)

Source PDF: `downloads/pvldb_exemplars/p3624-kaushik.pdf` (12 pages, read in full, every page rendered and checked).
Page convention: "p.N" = PDF page N (1-12); printed page = 3623 + N (p.1 = 3624, p.12 = 3635).
All descriptions are paraphrases; quoted fragments are short terms only.

---

## 1. Bibliographic facts

| Field | Value (evidence) |
|---|---|
| Title | Microsoft Purview: A System for Central Governance of Data (p.1) |
| Authors | 21 authors, all listed alphabetically by surname (Ahmad ... Wolter), with Kaushik and Ramakrishnan in the middle; contact author on the VLDB site is Raghav Kaushik (p.1) |
| Affiliation types | 100% industry, one affiliation: Microsoft Corporation (p.1). No academic co-author |
| Volume/issue/pages | PVLDB 16(12): 3624-3635, 2023 (p.1 reference-format box and footer) |
| DOI | 10.14778/3611540.3611552 (p.1, twice) |
| Track | **Industrial track.** The paper itself carries no track label; VLDB 2023 put industry papers in issue 16(12), and the official VLDB 2023 site lists this paper under "VLDB 2023: Industrial Track Papers" (vldb.org/2023/?papers-industrial, checked 2026-11-20) |
| Total pages | 12 (pdfinfo) |
| References start | p.12 (printed 3635), right column, about 45% of the way down |
| Body pages | about 11.7 (pp.1-12 up to the middle of the p.12 right column; references take about 0.27 page) |
| Reference count | 19 numbered entries [1]-[19] (counted, p.12) |
| Figures | 4 (Fig.1 p.6, Fig.2 p.7, Fig.3 p.9, Fig.4 p.11) |
| Tables | 0 |
| Algorithms (boxed / pseudocode) | 0. The PDP update logic is a 3-bullet prose procedure (p.8 §5.1.1); the permission check is a 4-condition prose list (p.9 §5.1.2) |
| Definitions / theorems / lemmas / propositions | 0 formal. Concepts are defined inline in bulleted prose (principal, resource, action, decision, role, scope, policy rule: p.4-5) |
| Numbered examples | 11: Ex 2.1-2.8 (pp.3-6), Ex 4.1 (p.8), Ex 5.1-5.2 (p.10). Plus named policies P1-P3 in the intro (p.2) |
| Equations | 0 displayed equations; no mathematical symbols at all. The only semi-formal notation is the scope wildcards `*` / `**` (p.4) and the predicate `Sensitivity_Label = Public` (p.5) |
| Footnotes | 0 |
| Artifact / code availability | None. No "PVLDB Artifact Availability" box on p.1, no repository link, no data release. The evaluation reports only normalized throughput because SQL Server rules forbid publishing absolute tps (p.11 §6.4) |
| Length | about 11.4k words in total (pdftotext); abstract about 515 words (very long for PVLDB) |

**What the industrial track changes in structure (observed):**
- No contribution bullet list; the intro ends with a roadmap only (p.3 §1.3).
- No formal model, no theorems, no correctness proofs; correctness is argued in prose plus worked interleavings (p.8, p.10).
- The evaluation is about 0.95 page with 1 workload, 1 baseline, 1 ablation and 1 figure (pp.10-11).
- All 19 references are product or web pages; there are no academic citations at all (p.12).
- Design choices are justified by "customers' requirements" and product constraints (on-prem products lack notification support; corporate rules on publishing tps) rather than by analysis (p.2, p.7, p.11).
- The paper spends about 28% of its body on product functionality and user scenarios (§2-§3) before any architecture appears.
- Novelty is asserted against competitor products ("first", "unique", "first of its kind, to our knowledge"), not against published techniques (p.2, p.11-12).

---

## 2. Title anatomy

`Microsoft Purview` + `:` + `A System for` + `Central Governance` + `of Data`

| Component | Function | Why it works / caveat |
|---|---|---|
| "Microsoft Purview" | Product brand name as the lead noun | For the industrial track the product name carries credibility (a real deployed system) and is how readers search. A research paper cannot lead with a brand. |
| "A System for" | Declares the genre: a system paper, not an algorithm | Tells reviewers to expect architecture plus implementation plus overhead measurement, not optimality proofs. |
| "Central Governance" | The value proposition (centralized as opposed to siloed) | Mirrors the abstract's core contrast: siloed versus unified governance (p.1). |
| "of Data" | Scope (deliberately broad) | Very broad. The body actually focuses on ABAC access control in SQL Server (p.1 abstract S13; p.8 §5). The title promises more than the technical depth delivers, which is acceptable for an industry overview but would be criticized in a research paper. |

Notably the title names neither the technical core (policy caching / native enforcement) nor any result.

---

## 3. Abstract (15 sentences, 4 paragraphs, about 515 words, zero numbers)

| # | Gist (paraphrase) | Rhetorical function | Concrete object / number carried |
|---|---|---|---|
| S1 | Data estates span on-prem, edge and clouds and many store types; this is called "data sprawl" | Context; coins a problem term | Term "data sprawl"; source types (relational, file/storage, NoSQL; operational/analytic) |
| S2 | Administrators must inventory data, find the sensitive parts and govern them across the whole estate | Defines the user's task (three steps) | Three-step workflow: inventory, identify, govern |
| S3 | Governance today is siloed, with each subsystem offering its own features | Problem statement | "siloed" |
| S4 | Policies are applied piecemeal, source by source, in source-specific languages | Mechanism of the problem | Per-source policy languages |
| S5 | So governance is cumbersome, error-prone (inconsistencies) and expensive | Consequences / pain | Three named costs |
| S6 | We present Purview, unified governance from one central pane | Solution announcement | System name; "single central pane of glass" |
| S7 | Purview has three parts: Data Map catalog via automated scanning, sensitivity classification, and a policy system, with a sample policy (non-FTEs denied access to PII) | System decomposition plus a concrete example | 3 components; example policy in natural language |
| S8 | Purview centralizes governance and automates discovery, classification and enforcement | Value claim | Automation of 3 activities |
| S9 | Other catalogs build global catalogs, but only Purview supports policies | Differentiation against competitors | "unique in its support for policies" |
| S10 | Also distinguished by covering structured and unstructured data via Office 365 integration; the brand merges O365 governance with former "Azure Purview" | Second differentiator plus product history | O365; former product name |
| S11 | Through O365 Rights Management, governance covers databases, Power BI reports and O365 documents | Scope of coverage | RMS, Power BI, O365 documents |
| S12 | The vision is a richer Data Map and policies from access control to lifecycle (retention, deletion, movement) | Vision / future scope | Policy classes beyond access control |
| S13 | This paper covers design and implementation challenges of the ABAC service, focusing on integration with Azure SQL Database | **Paper scope** (the actual technical core) | ABAC; Azure SQL Database (the body says "SQL Server", a naming drift) |
| S14 | We show unified O365 plus structured governance enforcing consistent access control as data flows across them | Demonstration claim | Data-flow scenario (developed on p.6 §3.2) |
| S15 | We also report an empirical evaluation of Purview's performance overheads | Evaluation announcement | No number (the "<2%" headline only appears on p.11 and p.12) |

Observations: the problem takes 5 sentences, the product 7 sentences, the technical scope 1 sentence (S13) and the evaluation 1 sentence (S15). The caching mechanism, the core performance idea, is not mentioned in the abstract. A research abstract would need the mechanism and at least one quantitative result.

---

## 4. Introduction (§1, pp.1-3, about 1.85 pages, 13 paragraphs incl. subsections)

| ¶ | Page | Function | Key moves |
|---|---|---|---|
| 1 | p.1 R | Context | Data estates split three ways: on-prem/edge/cloud, operational/analytic, and many kinds of each |
| 2 | p.1 R to p.2 L | **Problem through a persona** (the data security officer) then **gap** then **idea** | The officer must inventory, identify sensitive data, then translate one policy into many local languages (SQL grant-revoke versus data-lake ACLs). Conclusion: governance is "completely siloed". Introduces "unified data governance" and claims to be first to support fine-grained enforcement "out of the box" |
| 3 (§1.1) | p.2 L | Solution plus competitor positioning | Presents Purview [8]; AWS [2], Databricks [10] and Google [12] lack fine-grained in-database governance; O365 integration as second differentiator |
| 4 | p.2 L | Component 1 and 2 | Data Map (automated scanning for schema and lineage); classification (extensible sensitivity-label taxonomy, classification rules, built-in sampling classifiers) |
| 5 | p.2 L | Component 3 plus **running examples** | Policies; scope narrowed to access control; P1-P3 as bulleted natural-language policies |
| 6 | p.2 L to R | Concept naming | Policies use data, requestor and environment attributes, hence ABAC |
| 7 | p.2 R | **Design properties and non-goals** (4 numbered "points") | (1) consistent/scalable across sources; (2) succinct, matching author intent; (3) coexist with local policies, mandatory (local admin can restrict further but not override); (4) increasing expressive power is explicitly a "non-goal" |
| 8 | p.2 R | **Challenge plus design decision** | System is distributed (authored centrally, enforced locally). Key question: source of truth. Rejects dual truth kept in sync via 2PC; chooses Purview as truth for policies and local store as truth for metadata, with asynchronous updates and locally cached policies |
| 9 | p.2 R | Integration taxonomy | Native integration (SQL Server, Azure Storage; shared PDP component) versus proxy rewriting (non-Microsoft engines such as Oracle); paper focuses on native, with SQL Server as the case study |
| 10 | p.2 R to p.3 L | **Caching idea plus justification plus evaluation pointer** | Local policy cache avoids a service call and survives Purview outages; permission checks run on every query; typical SQL pattern is one user looping queries over the same tables and columns, so results of Purview calls are cached on the assumption that policy updates are infrequent; impact evaluated with a TPC-C-based benchmark |
| 11 (§1.2) | p.3 L | Background on O365 RMS | Encryption-based access control; key-release policy; central enforcement across the document lifecycle |
| 12 | p.3 L | Extension idea plus motivating scenario | Purview extends rights management to structured data via hub-and-spoke; scenario Excel to SQL to Power BI to Excel with labels re-applied; forward reference |
| 13 (§1.3) | p.3 R | Roadmap | Focus on structured data; sections 2-8 one sentence each |

**Move sequence:** context, problem (persona-driven), gap (siloed), idea (unified governance), solution components, design properties/non-goals, technical challenge (source of truth), design decision, caching idea, evaluation pointer, background, roadmap. There is **no results paragraph** (no number appears in the intro) and **no contribution list**.

**Contribution list:** absent. The closest substitutes are the 4 design "points" in ¶7 (p.2) and the abstract's S13-S15. A research paper should convert ¶7-¶10 into 3-4 verb-led contributions (design, mechanism, correctness, evaluation).

**First figure/table:** none in the intro. The first figure (Fig.1, hub-and-spoke) appears on p.6 in §2.5. The intro relies on the bulleted P1-P3 policies as its only "exhibit".

**Caching framing worth noting (p.2-3):** the caching rationale comes in three parts in a single paragraph: (a) availability (serve when Purview unreachable), (b) cost (a check on every query), (c) locality (same user, same objects, looping queries), with the validity assumption stated in the same sentence (policy updates are infrequent).

---

## 5. Remaining sections in order

### §2 Overview (pp.3-6, about 2.65 pages)
Purpose: product functionality and the policy language/semantics, which serve as the paper's "model" section.
- **§2.1 Initializing Purview (p.3):** 1 paragraph: account seeded with the O365 taxonomy; users add labels/rules; sources join by "registration".
- **§2.2 Catalog and Classification (p.3-4):** classification labels are free-form strings from an extensible taxonomy; unit of classification is file (Azure Storage) or column (SQL Server); objects have zero or more classification labels but at most one sensitivity label (which aggregates them). **Ex 2.1** (Contoso; SSN column with two labels, one sensitivity label) is placed directly after the definitions.
- **§2.3 Classification Rules (p.4):** rule language (regex, dictionaries, metadata matching); **Ex 2.2** (3 bullets: value regex, dictionary, column-name pattern); aggregation rules map classification labels to sensitivity labels; **Ex 2.3**; O365 ML classifiers mentioned in one sentence.
- **§2.4 ABAC (p.4-5):**
  - *2.4.1 Policy Language:* four components as bullets (principal, with a single identity provider assumed; resource, with a hierarchical Azure namespace extended to tables/columns/files; action; decision ∈ {grant, deny, inapplicable}). Then role = set of actions; scope = limited regex with `*` (one literal) and `**` (any path); policy rule = (principal, role, scope) to decision. **Ex 2.4**, optional sensitivity predicate, **Ex 2.5**. Scope is narrowed to equality predicates; extensions to classification predicates and Boolean combinations are called straightforward. **Crucially, the determinism property is stated here**: on a fixed catalog, classification and policy the predicate's output is fixed. Non-deterministic (time-of-day) predicates are forward-referenced (p.5).
  - *2.4.2 Semantics:* input triplet (user, fully specified resource, action); a rule matches under 3 conditions; aggregation is deny-overrides (grant if at least one grant and no deny; deny if any deny; inapplicable otherwise). **Ex 2.6** runs the running example (Alice in NonFTE; Column1 Confidential) through three requests (connect, read Column2, read Column1).
  - *2.4.3 Aggregation with local permissions:* the same deny-overrides combination across Purview and local checks; **Ex 2.7**; Purview policies are mandatory and cannot be overridden locally.
  - *2.4.4 Expressive Power:* restates the non-goal; maps the example to an equivalent SQL grant-revoke-deny configuration.
- **§2.5 Hub and Spoke (p.5-6):** repeats the RMS description from §1.2 almost sentence for sentence; Fig.1; the hub holds a subset language (cross-document actions, broad scopes); **Ex 2.8**; spokes per engine family, possibly multi-level; an engine applies all policies at its relevant scopes.

How formalism is introduced: **prose definition first, then a numbered example right away**, always with the same running example (Contoso, Alice, NonFTE, MyServer/MyDb/MyTable/Column1-2). No symbols are ever introduced. Semantics are given as enumerated conditions. Assumptions are stated at the point of use (single identity provider, p.4; equality predicates "for ease of exposition", p.5).

### §3 Example Scenarios (p.6, about 0.6 page)
Purpose: user-value demonstrations (characteristic of the industrial track).
- **§3.1 Self-service:** a data scientist discovers sources by classification, requests access, and one admin grants least privilege, compared with negotiating with each data owner.
- **§3.2 Governance through data flows:** two hub rules (Alice granted Confidential; NonFTE denied); Excel (RMS-encrypted), then loaded into SQL and re-classified (Customer.Name Confidential), then ABAC enforced, then Power BI query with column labels propagated, then export to Excel re-encrypted. No mechanism detail on label propagation is given.

### §4 Architecture (pp.6-8, about 1.55 pages)
Purpose: component diagram plus data flows (Fig.2) and the asynchrony decision.
- **Intro (p.6):** Fig.2; RMS integration put out of scope from here on.
- **§4.1 Catalog and Classification (p.7):** scan as a client with a configured credential; two efficiency optimizations: scan in the same region as the source, and scan only a fixed 128-row prefix (sampling is future work); configurable match threshold; only metadata plus classification leave the source (compliance); asynchronous, default every 8 hours.
- **§4.2 Policy Enforcement: Asynchrony (p.7):** policy UI to CosmosDB policy store; split source of truth restated; policies cached locally. **Two stated advantages of serving checks from a local cache: performance (no call in the inner loop) and fault tolerance (serve from an older policy when Purview is down).** Staleness is accepted as the price.
- **§4.3 Policy Distribution Service (p.7):** sources get updates via notifications or polling. **Freshness is an explicit by-design trade-off**: updates are not reflected immediately; the goal is "without a significant delay". SQL Server polls every **5 minutes** because on-prem products lack notification infrastructure. Interfaces: full pull, delta pull, notifications via Azure Event Hub. **Delivery semantics stated precisely: exactly-once but possibly out of order**, illustrated by insert-then-delete arriving reversed.
- **§4.4 Policy Decision Point (p.7-8):** PDP abstraction; proxy for non-Microsoft sources (parse query, derive permissions, check via PDP; **Ex 4.1** continues Ex 2.6); native integration inside the engine's permission logic. Policies are persisted in the local user DB and decisions aggregated with local checks. It forward-references §6 for native-versus-proxy performance, but §6 only argues this qualitatively (p.11).

### §5 Implementation in SQL Server (pp.8-10, about 2.4 pages): the technical core
Purpose: a native-integration case study. Scope is announced up front: other engines (Azure Storage, Cosmos DB) differ in details but share the main points; policies without predicates first, with predicates in §5.4 (p.8).
- **§5.1 PDP Algorithm (p.8):** rules preloaded into an in-memory cache with per-rule metadata (identifier plus monotone version counter, both assigned by the policy store).
  - *5.1.1 Updating rules after a delta:* full pull resets state; a delta carries rule plus metadata plus operation type (insert/delete/update). A 3-bullet procedure: an existing rule with a higher version means ignore; an existing rule with a lower version means update, with delete as a tombstone flag rather than removal; no existing rule means add, flagged deleted if the event is a delete. Then an **eventual-delivery argument** (because the delta API delivers everything, inserts and updates eventually land) and a **worked adversarial interleaving** justifying soft deletes (an undo-insert whose delete arrives first). Garbage collection: tombstones grow, so periodic full pulls (for example weekly) are justified by the rarity of policy updates.
  - *5.1.2 Permission check:* input (user, not group; resource path; action); linear scan over all rules with 4 match conditions; the host supplies group memberships. **Scope claim:** optimized for concise policies; a trie on scopes and a hash on principals are named as future work (p.9).
- **§5.2 Integration with SQL Query Processing and Security Caches (p.9)** — *the permission-decision cache section; most relevant to a permission-aware result cache.*
  - ¶1 (with Fig.3): explains host behaviour first. Plans are cached **without** permission checks; checks run in a pre-execution step; failure aborts the query. Because checking is expensive, SQL keeps in-memory **security caches**, two of which matter: an **object-level cache** (per user, per table/view, covering all its columns) and a **query-level cache** (per user, all objects referenced by a query). A same-query/different-parameters pattern hits the query cache; a different query over the same objects hits the object cache. **Eviction is coarse**: any security-metadata change clears the entire database's cache, which then repopulates on demand.
  - ¶2: integration. A background task polls PDS and **persists** the policy in the user DB (so it survives restart while Purview is down); the PDP runs as an in-process DLL with an in-memory policy cache. **PDP results are aggregated with local checks *before* the security caches are populated** (the word "before" is italicized on p.9), so existing caches are retained; on the hot path of iterative execution all checks are served from cache without calling the PDP. **Invalidation**: eviction is extended to clear the whole database's cache when the Purview policy changes, but only after checking that the updated rule's scope includes that database.
  - Justification structure: correctness rests on determinism (stated in §2.4.1, revisited in §5.5) plus database-wide flush on policy change; efficiency rests on the iterative single-user access pattern (p.3) and rare policy updates (p.7, p.11). **Not stated:** a revocation-latency bound (implicitly at most the poll interval plus flush), whether group-membership or classification/attribute changes also trigger a flush (§5.5 says decisions are fixed for a given policy *and classification*, yet only policy changes are said to flush), cache-hit rates, and flush cost.
- **§5.3 Discussion (pp.9-10):** three numbered implementation points:
  1. Azure multi-tenancy is via process isolation, so databases in a process share a tenant and policies overlap heavily; hence **one PDP instance and one polling task per SQL process** (not per database).
  2. **Delta pulls across restarts**: a sync token (unique per resource path) is persisted per database plus a local wall-clock timestamp; on restart use the most recent token. **Ex 5.1** (current vs restored DB). **Clock-skew case argued as no loss of correctness** (any persisted token is valid; an outdated token whose deltas expired triggers an error and then a full pull). New/restored DBs with a mismatched token get their persistent cache overwritten from the PDP's in-memory policy. **Ex 5.2** (new DB) admits that a per-DB subset optimization was not implemented: the full server-wide policy is stored in every DB.
  3. Read replicas obtain policy via log shipping (no network call); geo-replicas may belong to different Azure resources, so they fetch policy from PDS but classification from the log.
  - *5.3.1 Write-Ahead Principle:* always **persist before updating the in-memory PDP cache**, so post-restart queries never see an older policy than pre-restart queries. Justified by a counterfactual failure scenario (update memory, crash before persist, and the policy regresses).
- **§5.4 Handling Rule Predicates (p.10):** attributes also flow via PDS and a persistent cache, but the local store is the source of truth for metadata (stale classifications for dropped tables are ignored); attributes are **not preloaded**, fetched on demand via callback (memory footprint); replicas read attributes from the transaction log.
- **§5.5 Non-Deterministic Predicates (p.10):** **makes the caching precondition explicit**: security-cache integration depends on Purview checks being deterministic for a given policy and classification, which holds for the supported class. Time-based predicates (9am-5pm) would require clearing caches at every boundary instant; this is left as future work. A clean example of scoping a claim by naming the property it depends on and the case that breaks it.

How algorithms are presented overall: prose plus bullets, no pseudocode, no complexity analysis. Each rule is followed by an adversarial scenario that explains why it exists.

---

## 6. Evaluation (§6, pp.10-11, about 0.95 page)

**Goals (p.10):** end-to-end impact of Purview governance on SQL Server performance using a TPC-C-like benchmark. Implicitly two questions: (Q1) overhead of Purview with caching relative to no Purview; (Q2) the value of caching access-check results. No numbered RQs.

**Environment (§6.1, p.10-11):** a single bare-metal server (3.2 GHz, 64-core Intel Family 6, 64 GB RAM, separate data and log drives, SSD for log); driver machine with 4 cores and 14 GB. **Deviations from the standard benchmark, each with a stated reason:** the internal driver (Benchcraft) uses SQL authentication but Purview needs Azure AD, so a modified AAD-integrated driver was used; Purview does not yet cover stored-procedure execution permission, so prepared statements replace stored procedures.

**Systems compared (§6.2, p.11):** (1) SQLWithoutPurview = baseline (AAD auth, no Purview); (2) SQLWithPurview with caching enabled; (2b) SQLWithPurview with caching disabled (an ablation sub-configuration). There are no competitor systems and no proxy configuration. Fairness: same engine, same driver, same AAD auth in all configurations, so the comparison isolates Purview. Comparing against a no-security baseline is not done (the baseline still has AAD auth).

**Workload and policy (§6.3, p.11):** TPC-C (9 tables, 5 transaction types); required permissions are read/insert/delete/update on tables plus connect on the DB; the policy grants all of them. **The policy is held fixed for the whole run**, justified as realistic because permissions rarely change once configured. **Worst-case framing:** there is no local policy, so every permission derives from Purview. Scale factor W=200, chosen as the smallest value that maximizes baseline CPU, consistent with the TPC-C specification. Production data: none in the evaluation.

**Metrics (every one reported):**
1. Normalized throughput: tps divided by the maximum observed value (absolute tps withheld because of SQL Server publication rules, p.11).
2. Relative throughput at peak: SQLWithPurview = 98.38% of baseline at 150 threads, i.e. overhead <2%.
3. Worst-case overhead across loads: higher at lighter loads, never above 5%.
4. Throughput drop with caching disabled: up to 31%.
That is 1 underlying measurement (throughput) reported as 4 numbers. **Not measured:** latency, cache hit ratio, invalidation/flush cost, policy-propagation or revocation latency, PDP evaluation time versus policy size, memory footprint, scan cost, behaviour under policy churn.

**Per-exhibit analysis:**
| Exhibit | Varied | Measured | Headline (paraphrase) |
|---|---|---|---|
| Fig.4 (p.11), grouped bar chart | TPC-C client threads: 50, 100, 150, 200, 250, 300 | Normalized throughput of SQLWithoutPurview and SQLWithPurview (caching on) | Peak at 150 threads, where Purview reaches 98.38% of baseline (<2% overhead); overhead grows at lighter load but stays at or below 5% |
| Caching-off result (p.11, text only, no exhibit) | caching on/off | throughput drop | Without caching throughput falls by up to 31%, showing the optimizations matter |
| Native vs proxy (p.11, text only, **not measured**) | n/a | n/a | Proxy argued to be slower (extra hop; cannot couple with security caches) |

My reading of Fig.4 bars (approx): 50 threads about 0.994/0.957; 100 about 0.985/0.978; 150 about 1.000/0.984; 200 about 0.996/0.965; 250 about 0.989/0.969; 300 about 0.997/0.980. The largest gap is at 50 threads (about 3.7%), consistent with "lighter load is worse", but 200 threads (about 3%) is above the peak load, so the "lighter load" pattern is not monotonic. The **y-axis starts at 0.93**, which visually exaggerates gaps of 1-4%.

**Negative results / trade-offs / limitations (where stated):**
- Policy updates are not reflected immediately, by design; 5-minute polling (p.7 §4.3).
- Caching disabled costs up to 31% (p.11), framed positively as the value of the optimization.
- Overhead is up to 5% at light load (p.11).
- Proxy is not evaluated empirically (p.11).
- Stored-procedure permissions are unsupported, which forced the benchmark change (p.10-11).
- Linear-scan PDP suits only concise policies (p.9).
- Server-wide policy duplicated into every DB (p.10 Ex 5.2).
- Non-deterministic predicates unsupported (p.10 §5.5).
- 128-row prefix scan; sampling is future work (p.7).
- Expressive power not increased (p.2, p.5).

**Production / end-to-end evidence:** the benchmark is end-to-end, but no production telemetry for enforcement is shown. Production scale appears only in Related Work: operation over Microsoft's internal estate with hundreds of instances per DB system and Cosmos at more than 10 exabytes (p.11-12), used as a positioning claim, not as an evaluation result.

**Statistical treatment:** none. No repetitions, run duration, warm-up, variance, error bars or confidence intervals are reported. Results are single-point per configuration.

---

## 7. Figure and table inventory

| # | Page | Type | Purpose | What a reviewer can recover | Caption style |
|---|---|---|---|---|---|
| Fig.1 | p.6 (top-left, one column) | Tree diagram (raster JPEG, the only embedded image in the PDF): hub (Office + Data) with two spokes (Storage, Data) | Illustrates hub-and-spoke policy layering with O365 | Hierarchy of policy scopes only; no semantics or data flow | Short bold noun phrase, no final period ("Hub and Spoke Model of Integration with Office 365 RMS") |
| Fig.2 | p.7 (full width, top) | Block-and-arrow architecture: CDO, Policy UI, policy store, catalog, PDS, SQL/Storage/Other instances; arrows labelled Policy, Classification, Metadata | System architecture and asynchronous flows | Which components exchange policy vs classification vs metadata, and the direction of each flow | Very short bold noun phrase ("Purview system architecture.") |
| Fig.3 | p.9 (one column) | Layered engine stack: TDS, Query Compilation, Execution Engine (Permission Checks), Storage Engine, with PDP DLL (in-memory cache) on the side and a Persistent Policy Cache store | Where the PDP plugs into SQL query processing | Placement of PDP and persistent cache relative to permission checks. **It does not show the object-level or query-level security caches or the invalidation path**, even though §5.2's key idea is caching | Short bold descriptive phrase |
| Fig.4 | p.11 (one column) | Grouped bar chart, 6 load levels x 2 configurations; y-axis 0.93-1.01 | Throughput overhead of Purview vs baseline | Peak point, the overhead range across loads (about 1.6-3.7%), and which load is worst. Absolute tps, variance and the caching-off configuration are not recoverable | Longer bold caption stating metric, systems, x-variable and the fixed parameter (W=200) |
| Tables | — | none | — | — | — |

Ratio: 3 of 4 figures are conceptual/architecture; only 1 empirical exhibit.

---

## 8. Related work (§7, pp.11-12, about 0.6 page, placed after the evaluation and before the conclusion)

| Group | Refs | Count | Positioning pattern |
|---|---|---|---|
| Commercial data catalogs | Alation [1], Collibra [9], Google Data Catalog [11], Informatica [14]; self [8]; O365 [17], AAD [5] | 4 competitors (+3 own) | They offer scanning/classification/lineage "much like Purview"; Purview differs by scale (internal exabyte estate) and native Microsoft-ecosystem integration |
| Open-source catalog | Apache Atlas [3] | 1 | Purview is Atlas-compatible, "a significant extension", and that differentiates it from competitors |
| Industrial central policy management | AWS IAM [2], Databricks Unity [10], Google IAM [12] | 3 | Only coarse, database-level policies; none fine-grained inside a database |
| Open-source policy engines | Apache Ranger [4] (+ IBM Db2 Big SQL [13]), Open Policy Agent [18] | 3 | Ranger is tag-based but Hadoop-only; OPA has similar expressiveness but is not integrated out of the box; neither addresses distribution scalability (PDS); native SQL integration is "first of its kind, to our knowledge" |

Sentence pattern: "[Competitor set] provides [similar capability]. Purview is notable/unique/distinguished because [scale | integration | fine-grained policy]." Every comparison is product against product. **No academic literature is cited** (no ABAC/XACML models, no authorization-caching or decision-caching work, no fine-grained access control in DBMSs, no Zanzibar-style systems).

---

## 9. References (19 total, p.12)

| Split | Count |
|---|---|
| DB venues (PVLDB/SIGMOD/ICDE/etc.) | 0 |
| Security venues | 0 |
| Systems venues | 0 |
| Journals | 0 |
| Web/product docs | 19 (100%) |
| ...of which competitor/third-party products | 11 ([1],[2],[3],[4],[9],[10],[11],[12],[13],[14],[18]) |
| ...of which Microsoft's own products/infrastructure | 7 ([5],[6],[7],[8],[15],[16],[17]) |
| ...of which benchmark specification | 1 (TPC-C [19]) |
| Year ≤2010 | 0 |
| Year 2011-2020 | 1 (TPC-C, 2019) |
| Year 2021+ | 18 (10 dated 2021, 8 dated 2023; web-access years, not publication years) |
| PVLDB / SIGMOD / ICDE refs | 0 / 0 / 0 |

Most-cited in the body: O365 [17] (4 in-text uses), AAD [5] (3); all others 1-2.

---

## 10. Limitations / discussion / conclusion

- **No dedicated limitations section.** Limitations are spread through the text at the point of design: non-goals (p.2 ¶7, p.5 §2.4.4), by-design staleness (p.7 §4.3), PDP scaling (p.9 §5.1.2), unimplemented per-DB subset (p.10 Ex 5.2), non-deterministic predicates (p.10 §5.5), stored-procedure gap (p.11 §6.1), proxy not measured (p.11 §6.4).
- **"Discussion" (§5.3) is an implementation-details section**, not reflection: process topology, restart/token recovery, replicas, write-ahead ordering (pp.9-10).
- **Conclusion (§8, p.12), 3 paragraphs:** (1) restates Purview, O365 integration, the heterogeneity covered, the 3 components, and a "first system" plus scale/diversity claim; (2) recaps challenges (ABAC, native and proxy, asynchronous semantics plus "aggressive use of caching") and repeats the headline (<2% throughput drop on TPC-C); (3) vision: the first of what will be many such systems, "a good beginning", only access control so far, aims for full permission coverage, and future policy classes (masking, retention, deletion, data movement).
- How trade-offs are stated: honestly but softly. Each trade-off is paired with a justification (rare policy updates; customer requirements; on-prem constraints) or a future-work pointer, and none is quantified (for example, no staleness window measurement).

---

## 11. Transferable rules and anti-patterns

### DO (transferable to a caching / result-reuse / access-control PVLDB paper)
1. **DO state the determinism property of the decision function in the model section and later cite it explicitly as the precondition for caching**: because it gives reviewers the exact correctness condition of the cache and sets up the limitation case. (evidence: p.5 §2.4.1 determinism; p.10 §5.5 caching depends on it)
2. **DO name the case that breaks your caching precondition and sketch what it would require**: because it turns a hidden hole into a scoped claim. (evidence: p.10 §5.5, time predicates need flushes at 9am/5pm boundaries)
3. **DO motivate reuse with a concrete workload access pattern, not just "checks are expensive"**: because hit-rate plausibility depends on locality. (evidence: p.3 ¶10 one user, looping queries, same tables; p.9 parameterized repeats hit the query-level cache)
4. **DO describe the host system's existing caches by key granularity and the access pattern each serves before introducing your integration**: because reviewers need the baseline cache semantics to judge what you change. (evidence: p.9 ¶1 object-level vs query-level, per user)
5. **DO place your decision logic upstream of an existing cache so the hot path inherits it, and say explicitly that the hot path never calls your component**: because it explains near-zero overhead mechanistically. (evidence: p.9 ¶2, aggregate before populating; hot path without PDP)
6. **DO state invalidation granularity and its filter in one place (what is flushed, when, and what check limits it)**: because revocation correctness is the first thing an access-control reviewer probes. (evidence: p.9, DB-wide flush on policy change after a scope-containment check)
7. **DO assign a source of truth per object class and name the rejected alternative**: because it pre-empts "why not keep both in sync?" (evidence: p.2 ¶8, 2PC dual truth rejected; p.7 §4.2)
8. **DO declare staleness as a by-design trade-off with concrete parameters**: because quantified freshness knobs are reviewable while vague "eventually" claims are not. (evidence: p.7 §4.3 5-min polling; p.7 §4.1 8-h scans; p.8 weekly full pull)
9. **DO specify the delivery semantics of your update channel precisely (exactly-once, out-of-order) and then show how state maintenance tolerates them**: because invalidation correctness depends on channel guarantees. (evidence: p.7 §4.3; p.8 §5.1.1 versions plus tombstones)
10. **DO justify each state-maintenance rule with a minimal adversarial interleaving**: because it makes the rule's necessity obvious without a proof. (evidence: p.8 delete-before-insert motivates soft deletes)
11. **DO give crash-ordering rules a name and a counterfactual failure**: because "write-ahead" plus the regression scenario is memorable and checkable. (evidence: p.10 §5.3.1)
12. **DO cover restarts, restores, new objects, replicas and clock skew explicitly, each with an example and a correctness statement**: because these are where cached authorization goes wrong in practice. (evidence: p.10 §5.3, Ex 5.1-5.2, clock-skew argument, outdated token leads to a full pull)
13. **DO use one running example from the language section through semantics, aggregation and enforcement**: because readers verify each mechanism on familiar objects. (evidence: Alice/NonFTE/Column1 in Ex 2.6 p.5, Ex 2.7 p.5, Ex 4.1 p.8)
14. **DO follow each definition immediately with a numbered example**: because it halves the cost of reading the model. (evidence: Ex 2.1-2.5 pp.3-5)
15. **DO list design properties and explicit non-goals in the intro**: because a stated non-goal deflects "your language is not more expressive" attacks. (evidence: p.2 ¶7 point 4; p.5 §2.4.4)
16. **DO announce exposition scoping up front ("no predicates first; extension in §X")**: because it lets you present the clean core without appearing to hide cases. (evidence: p.8 §5 intro; p.10 §5.4)
17. **DO frame the evaluation configuration as worst case and say why**: because it makes a small overhead number conservative. (evidence: p.11 §6.3, no local policy so every check goes through Purview)
18. **DO include a cache-disabled ablation**: because it quantifies the cache's contribution separately from the system's overhead. (evidence: p.11, up to 31% drop without caching)
19. **DO pick the scale factor by a stated criterion and justify every deviation from a standard benchmark**: because it pre-empts cherry-picking concerns. (evidence: p.11 W=200 smallest maximizing CPU; p.10-11 AAD driver, prepared statements)
20. **DO report the headline at the peak operating point and the worst-case bound across the sweep**: because a single best-case number invites suspicion. (evidence: p.11, 98.38% at 150 threads; at most 5% elsewhere)
21. **DO name the concrete data structure for a future scaling fix when admitting a scaling limit**: because it signals the limit is engineering, not fundamental. (evidence: p.9, trie on scopes, hash on principals)
22. **DO justify deployment granularity of the cache by tenancy and overlap**: because per-process vs per-database instances is a reviewer question for shared caches. (evidence: p.9 §5.3 point 1, one PDP per process)
23. **DO repeat the headline number in the conclusion**: because it closes the claim-evidence loop. (evidence: p.12 §8 ¶2, <2%)

### Anti-patterns (what NOT to copy into a research-track paper)
- **No contribution list and no results in the intro** (p.3 §1.3). Research reviewers expect 3-4 verb-led contributions and headline numbers by page 2.
- **No formal model or correctness theorem.** Revocation and staleness safety are argued only in prose (pp.8-10). A research paper on permission caching needs a stated invariant (for example, a bounded-staleness or no-stale-grant property) with a proof or proof sketch.
- **Zero academic references; 100% product URLs** (p.12). That is fatal for the research track: cite ABAC/XACML, fine-grained DB access control, authorization/decision caching, cache-invalidation and view-maintenance literature.
- **Policy held fixed during the evaluation** (p.11). The hardest case for a permission cache (policy churn, revocation storms, flush cost, revocation latency) is not measured; "updates are rare" is asserted, never measured (p.3, p.8, p.11).
- **One workload, one metric, no repetitions, no variance, truncated y-axis from 0.93** (p.11). Research papers need multiple workloads, latency plus throughput, hit ratio, error bars, and an axis starting at 0 or a clearly marked break.
- **A key result only in prose** (31% caching-off, p.11) with no exhibit or breakdown.
- **Forward reference that over-promises**: §4.4 says §6 discusses native vs proxy performance (p.8), but §6 offers only a qualitative argument with no measurement (p.11).
- **Normalized throughput justified by corporate publication rules** (p.11). Acceptable only in industry; research needs absolute numbers or a released artifact.
- **No artifact availability** (p.1). PVLDB research papers are expected to provide one.
- **Scale and production claims placed in Related Work rather than measured** (p.11-12 exabyte estate).
- **"Straightforward to extend" hand-waving** for predicate classes and Boolean combinations (p.5, p.8). Research reviewers will ask for the details.
- **Near-verbatim duplicated passage** (RMS description in §1.2 p.3 and §2.5 p.5-6), a 515-word abstract with no numbers, naming drift (Azure SQL Database in the abstract vs SQL Server in the body; "SQL-NoPurview" vs "SQLWithoutPurview" p.11), and typos ("acess", p.3/p.5; "a attribute", p.2; garbled "Office'scalability", p.12).
- **Figure for the core caching mechanism omits the caches themselves** (Fig.3 p.9 shows PDP and persistent cache but not the object/query-level security caches or the invalidation path).
- **Unstated invalidation triggers**: group-membership changes and classification/attribute changes are not said to flush security caches, although determinism is defined relative to policy *and* classification (p.9 vs p.10 §5.5). A research paper must enumerate every input of the cached decision and its invalidation trigger.
- **28% of body on product features and user scenarios** (§2-§3). A research paper should compress this into a problem setting plus model.

---

## 12. Quantified fingerprint

| Metric | Value |
|---|---|
| Track | Industrial (VLDB 2023) |
| Total pages / body pages | 12 / about 11.7 |
| References | 19 (0 academic; 0 PVLDB/SIGMOD/ICDE) |
| Figures | 4 (3 conceptual/architecture, 1 empirical) |
| Tables | 0 |
| Algorithms / formal definitions / theorems / equations | 0 / 0 / 0 / 0 |
| Numbered examples | 11 (+ P1-P3 policies) |
| Footnotes | 0 |
| #Baselines | 1 (SQLWithoutPurview) + 1 ablation (caching disabled); 0 competitor systems; proxy not measured |
| #Metrics | 1 underlying (throughput, normalized), reported as 4 numbers (98.38% peak, <2% overhead, ≤5% worst, up to 31% drop without cache) |
| #Datasets / workloads | 1 (TPC-C-like, W=200, prepared statements, AAD) |
| Sweep dimensions | 1 (client threads 50-300, 6 levels) |
| #RQs | 0 explicit (2 implicit: overhead; cache value) |
| Statistical treatment | none |
| Pages on evaluation | about 0.95 |
| % of body on evaluation | about 8% |
| Page budget by section (approx) | Front matter/abstract 0.65; Intro 1.85; §2 Overview 2.65; §3 Scenarios 0.6; §4 Architecture 1.55; §5 Implementation 2.4 (of which §5.2 caching about 0.5); §6 Eval 0.95; §7 Related 0.6; §8 Conclusion 0.35; References 0.27 |
| Abstract | 15 sentences, about 515 words, 0 numbers |
| Contribution bullets | 0 |
| Artifact | none |
