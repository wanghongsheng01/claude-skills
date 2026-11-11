# ICDE 2027 CMT subject areas: scope and signal words

Generated from `scripts/suggest_areas.py` (AREAS). Names are verbatim from the CMT form (checked 2026-11-11).

| Area | Covers | Signal words (regex) |
|---|---|---|
| AI and machine learning for data systems and vice versa | learned components inside data systems; data systems for ML | `machine learning`, `\blearned (index\|optimizer\|cost\|cardinality)`, `neural network`, `reinforcement learning`, `deep learning`, `\bml model`, `training data`, `feature store`, `model serving` |
| Benchmarking, performance modeling, tuning, and testing | benchmarks, experimental studies, cost/performance models, tuning, testing | `\bbenchmark`, `experimental (study\|survey\|evaluation of)`, `performance model`, `\btuning\b`, `knob`, `\btesting\b`, `\bfuzz`, `reproducib` |
| Cloud data management | cloud-native, serverless, multi-tenant, disaggregated data systems | `\bcloud`, `serverless`, `multi-tenan`, `disaggregat`, `object stor`, `\bsaas\b` |
| Data mining with a data-centric focus | mining algorithms over data (patterns, clusters, outliers, communities) | `data mining`, `frequent (pattern\|itemset)`, `clustering`, `outlier`, `anomaly detection`, `community detection`, `cohesive subgraph`, `\bk-core\b`, `\bk-plex\b`, `dense subgraph` |
| Data models, semantics, and query languages | data models, query languages, formal semantics, Datalog | `query language`, `\bdatalog\b`, `semantics`, `data model`, `relational algebra`, `recursive quer`, `\bschema\b`, `type system`, `declarative` |
| Data preparation, cleaning, and integration | cleaning, entity resolution, schema matching, integration, discovery | `data cleaning`, `entity (resolution\|matching)`, `schema matching`, `data integration`, `data lake`, `join discovery`, `table union`, `imputation`, `\betl\b`, `data preparation`, `deduplicat` |
| Data pricing and markets | pricing data and queries, data marketplaces | `data (pricing\|market)`, `query pricing`, `marketplace`, `\bprice\b` |
| Data quality, curation, provenance, and workflows | quality, constraints, provenance/lineage, curation, workflows | `data quality`, `provenance`, `lineage`, `curation`, `workflow`, `data validation`, `integrity constraint`, `functional dependenc`, `denial constraint` |
| Data security and privacy | access control, authorization, privacy, encryption, secure query processing | `access control`, `authori[sz]ation`, `permission`, `privacy`, `differential privacy`, `encrypt`, `\bsecurity\b`, `row-level security`, `\bpolicy\b`, `\bpolicies\b`, `revocation`, `\bdeny\b`, `zanzibar`, `\brebac\b`, `\brbac\b`, `\babac\b` |
| Data streams, complex event processing, and edge computing | streams, windows, CEP, IoT and edge | `\bstream`, `complex event`, `sliding window`, `edge computing`, `\biot\b`, `continuous quer`, `event processing` |
| Data systems on modern hardware | GPU, FPGA, NVM/CXL, RDMA, SIMD-aware data systems | `\bgpu`, `\bfpga`, `persistent memory`, `\bnvm\b`, `\brdma\b`, `\bsimd\b`, `\bcxl\b`, `modern hardware`, `accelerator` |
| Data visualization and interactive data exploration | visual analytics, interactive exploration, dashboards | `visuali[sz]ation`, `interactive (data )?exploration`, `dashboard`, `visual analytic` |
| Distributed and parallel data management | distribution, replication, partitioning, parallel processing | `distributed`, `parallel`, `replica`, `replication`, `partitioning`, `consensus`, `scale-out`, `\bshard` |
| Distributed ledgers and blockchains | blockchains, ledgers, smart contracts | `blockchain`, `\bledger`, `smart contract` |
| Domain-specific data engineering (scientific, medical, climate, urban, etc.) | data engineering for a science or application domain | `scientific data`, `medical`, `clinical`, `climate`, `\burban\b`, `genom`, `healthcare`, `e-commerce`, `\berp\b` |
| Energy-efficient data engineering | energy and carbon efficiency of data processing | `\benergy`, `power consumption`, `carbon`, `green comput` |
| Explainability, fairness, bias, trust, authentication, and regulatory compliance | explanations, fairness, trust, authentication, compliance | `explanation`, `explainab`, `fairness`, `\bbias\b`, `\btrust`, `authenticat`, `compliance`, `\bgdpr\b`, `regulat`, `\baudit` |
| Foundation models and LLMs for data engineering and vice versa | LLMs/foundation models used for or served by data systems | `\bllms?\b`, `large language model`, `foundation model`, `\bgpt`, `\bprompt`, `text-to-sql`, `\bnl2sql\b`, `semantic operator`, `\bagent`, `\brag\b` |
| Graph data | graph storage, indexing, querying and algorithms (reachability, paths, subgraphs, dynamic graphs) | `\bgraphs?\b`, `reachability`, `shortest path`, `subgraph`, `\bvertex`, `\bvertices`, `2-hop`, `hub label`, `transitive closure`, `dynamic graph`, `\bedges?\b`, `\bbfs\b`, `traversal` |
| Knowledge graphs for data engineering | KGs, RDF, SPARQL, ontologies, entity linking | `knowledge graph`, `\brdf\b`, `sparql`, `ontolog`, `entity linking`, `\btriples?\b` |
| Multi-modal and heterogeneous data | text, images, video, tables and mixed-model data | `multi-?modal`, `heterogeneous data`, `\bimages?\b`, `\bvideo`, `unstructured`, `semi-structured`, `\bjson\b` |
| Multidimensional data, data warehousing, OLAP, and analytics | OLAP, cubes, warehouses, BI and aggregate analytics | `\bolap\b`, `data cube`, `data warehous`, `aggregat`, `analytic`, `\bbi\b`, `business intelligence` |
| Query processing and optimization | query execution, joins, cardinality, plans, caching and reuse | `query processing`, `query optimi`, `\bjoins?\b`, `cardinality`, `cost model`, `query plan`, `execution`, `materiali[sz]ed view`, `\bcache`, `top-k`, `\bqueries\b`, `\blatency\b` |
| Responsible and ethical data management | responsible, ethical, consent-aware data management | `responsible`, `ethic`, `consent`, `societal` |
| Storage, indexing, and physical database design | indexes, storage layouts, compression, physical design | `\bindex`, `indexing`, `\bstorage`, `physical design`, `b\+?-tree`, `\blsm`, `compression`, `\blabels?\b`, `\blayout`, `index size`, `maintenance` |
| Time-series, temporal, spatial, and spatio-temporal data | time series, temporal databases, spatial and trajectory data | `time[- ]series`, `temporal`, `spatial`, `trajector`, `geo`, `spatio-temporal` |
| Transaction management, concurrency control, and recovery | transactions, isolation, concurrency, logging, recovery | `transaction`, `concurren`, `isolation`, `serializab`, `recovery`, `write-ahead`, `\bmvcc\b`, `snapshot`, `acknowledg`, `consistency` |
| Uncertain, probabilistic, and approximate data | approximation, sampling, probabilistic data, error guarantees | `approximat`, `sampling`, `probabilistic`, `uncertain`, `confidence interval`, `error bound`, `\bsketch`, `\baqp\b`, `estimat` |
| Vector data | vector search, ANN indexes, embeddings | `\bvector`, `\bann\b`, `nearest neighbo`, `embedding`, `similarity search`, `\bhnsw\b`, `filtered search` |

"None Of Above" exists as a Primary box only; never use it when an area fits.

## Typical pairings seen in ICDE papers

- Index or algorithm for a data type: primary = the data type (Graph data, Vector data, Time-series ...); secondary = Storage, indexing, and physical database design and/or Query processing and optimization.
- Security/privacy application of a data-management technique: primary = the technique's area; secondary = Data security and privacy (primary only if the contribution is the security mechanism or guarantee).
- LLM labels with statistical guarantees: primary = Uncertain, probabilistic, and approximate data; secondary = Foundation models and LLMs ...; add Multidimensional data ... for aggregate/BI queries.
- EAB / benchmark paper: Benchmarking, performance modeling, tuning, and testing (primary if the benchmark is the contribution) plus the area of the systems benchmarked.
- Cleaning/integration/discovery with constraints: Data preparation, cleaning, and integration + Data quality, curation, provenance, and workflows.
