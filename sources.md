# GraphRAG reading list

Maintained by `scout`. Entry format:

```
### <Title>
- URL: <url>
- Topics: <comma-separated: graphrag, entity-extraction, use-cases, evaluation, ...>
- Why: <one sentence on what it adds>
- Last checked: <YYYY-MM-DD>
```

## Sources

### From Local to Global: A GraphRAG Approach to Query-Focused Summarization (Edge et al., Microsoft Research)
- URL: https://arxiv.org/abs/2404.16130
- Topics: graphrag, use-cases, evaluation
- Why: The original Microsoft GraphRAG paper. It defines "global sensemaking" questions as the case where vector RAG fails, and shows community summaries beat a RAG baseline on comprehensiveness and diversity over corpora of about 1M tokens.
- Last checked: 2026-11-24

### RAG vs. GraphRAG: A Systematic Evaluation and Key Insights (Han et al.)
- URL: https://arxiv.org/abs/2502.11371
- Topics: graphrag, use-cases, evaluation
- Why: Compares RAG and GraphRAG on QA and query-based summarization under the same settings. Finds the two complementary, with RAG stronger on single-hop and detail questions and GraphRAG stronger on multi-hop reasoning, and shows that selecting or combining the two improves results.
- Last checked: 2026-11-24

### When to use Graphs in RAG: A Comprehensive Analysis for Graph Retrieval-Augmented Generation (GraphRAG-Bench)
- URL: https://arxiv.org/abs/2506.05690
- Topics: graphrag, use-cases, evaluation
- Why: A benchmark with four task levels (fact retrieval, complex reasoning, summarization, creative generation) on medical and novel corpora. Graphs help on reasoning and summarization but not on simple fact lookup, and token costs differ by orders of magnitude (MS-GraphRAG global search uses about 330k tokens per query vs about 900 for basic RAG).
- Last checked: 2026-11-24

### Do We Still Need GraphRAG? Benchmarking RAG and GraphRAG for Agentic Search Systems (Fan et al.)
- URL: https://arxiv.org/abs/2604.09666
- Topics: graphrag, use-cases, evaluation, agentic-search
- Why: Shows that multi-round agentic retrieval closes much of the gap between dense RAG and GraphRAG. GraphRAG keeps an edge only on complex multi-hop reasoning, and only once its indexing cost is spread over many queries.
- Last checked: 2026-11-24

### Towards Practical GraphRAG: Efficient Knowledge Graph Construction and Hybrid Retrieval at Scale (Min et al.)
- URL: https://arxiv.org/abs/2507.03226
- Topics: graphrag, entity-extraction, use-cases, hybrid-retrieval
- Why: An enterprise case study (legacy code migration) with hybrid vector and graph retrieval via RRF. Gains of up to 15% over vector-only retrieval, and dependency-parsing extraction reaches 94% of LLM-extraction quality at much lower cost.
- Last checked: 2026-11-24

### Stop graphing everything: when GraphRAG actually beats vector RAG (VentureBeat, Dattaraj Rao)
- URL: https://venturebeat.com/ai/stop-graphing-everything-when-graphrag-actually-beats-vector-rag
- Topics: use-cases, graphrag, evaluation
- Why: A practitioner synthesis of several benchmarks by task type (global, multi-hop, single-fact), with counterevidence, indexing cost and the bias of LLM-as-judge evaluation. It recommends routing each query between graph and chunk retrieval. Most of its figures are second-hand.
- Last checked: 2026-11-24

### Vector RAG vs. GraphRAG: Which retrieval do you need? (Neo4j blog)
- URL: https://neo4j.com/blog/agentic-ai/vector-rag-vs-graphrag/
- Topics: use-cases, graphrag, hybrid-retrieval
- Why: A diagnostic approach: first check whether failures come from poor semantic matching (fix chunking and embeddings) or from missing connections between facts (consider a graph). Vendor-slanted, and some of its figures come from a Neo4j-sponsored study.
- Last checked: 2026-11-24
