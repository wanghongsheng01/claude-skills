import json, sys, re
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, __import__('os').path.dirname(__file__)); import llm  # set LLM_KEYS_JSON first
acc = json.load(open('accepted_all.json'))
AREAS = ["graph-algorithms (cohesive subgraphs, paths, matching, community, centrality, graph queries)",
 "graph-learning (GNN, graph embedding, graph clustering by learning)", "vector-search (ANN, similarity search, embeddings retrieval)",
 "query-optimization (optimizer, cardinality/cost estimation, query rewrite, execution)", "indexing-storage (learned index, KV store, LSM, compression, file formats)",
 "transactions-distributed (concurrency control, replication, distributed/cloud DB, serverless)", "time-series-streams (forecasting, anomaly detection, streaming systems)",
 "spatial-temporal (trajectory, road network, POI, urban, spatial queries)", "llm-for-data (text-to-SQL, LLM data wrangling, RAG over data, LLM agents for data tasks)",
 "data-quality-integration (cleaning, imputation, entity resolution, schema/table matching, data discovery, provenance)",
 "privacy-security-blockchain", "data-markets-valuation (pricing, Shapley/data valuation, federated data sharing)",
 "db4ai-ml-systems (training data management, model serving, embedding caching, ML pipelines)", "recommendation-mining (recommender, pattern mining, clustering, classification)",
 "explainability-fairness", "crowdsourcing-spatial-crowdsourcing", "modern-hardware (GPU, FPGA, CXL, NVM, PIM)", "benchmark-tuning (DB tuning, benchmarks, testing)",
 "knowledge-graphs-text-multimodal", "other"]
PROMPT = """You classify research papers accepted at IEEE ICDE (data engineering). For each paper return a JSON object with keys:
"i" (the given index), "area" (exactly one label prefix from: %s),
"problem" (one of: efficiency-exact [make a well-defined query/algorithm faster or scalable], new-problem [formulates a new query/problem], effectiveness [improve accuracy/quality of a learned or heuristic task], system [design/build a system or framework], benchmark [experimental study/benchmark/evaluation]),
"method" (one of: algorithmic-index [exact/approximate algorithms, index structures, complexity bounds], learned-model [trained neural/ML model], llm-based [uses LLMs/foundation models as a core component], system-architecture, theory-guarantee, empirical-study),
"llm" (true if LLMs/foundation models are central), "dynamic" (true if the paper targets dynamic/evolving/streaming data or updates).
Papers:
%s
Return only a JSON list."""
labels = [a.split(' ')[0] for a in AREAS]
def run(chunk):
    txt = "\n".join(f"[{i}] {acc[i]['title']} :: {(acc[i].get('abstract') or '')[:600]}" for i in chunk)
    out = llm.chat('deepseek', [{"role": "user", "content": PROMPT % ("; ".join(AREAS), txt)}], max_tokens=3000)
    t = out['text']; t = t[t.find('['): t.rfind(']') + 1]
    return json.loads(t)
chunks = [list(range(i, min(i + 15, len(acc)))) for i in range(0, len(acc), 15)]
with ThreadPoolExecutor(8) as ex:
    for res in ex.map(run, chunks):
        for r in res:
            a = acc[int(r['i'])]; a.update({k: r.get(k) for k in ['area', 'problem', 'method', 'llm', 'dynamic']})
            a['area'] = next((l for l in labels if str(a['area']).startswith(l)), 'other')
json.dump(acc, open('accepted_all.json', 'w'), indent=1, ensure_ascii=False)
print(sum(1 for a in acc if a.get('area')), len(acc))
