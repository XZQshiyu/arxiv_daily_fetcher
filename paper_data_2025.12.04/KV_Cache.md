# KV Cache - arXiv 论文报告

**生成时间**: 2025-12-04 16:45:10

**分类**: KV Cache

**论文数量**: 4 篇

---

## 1. RELIC: Interactive Video World Model with Long-Horizon Memory

- **arXiv ID**: [2512.04040v1](http://arxiv.org/abs/2512.04040v1)
- **作者**: Yicong Hong, Yiqun Mei, Chongjian Ge, Yiran Xu, Yang Zhou et al. (14 authors)
- **发布时间**: 2025-12-03T18:29:20+00:00
- **arXiv分类**: cs.CV
- **标签**: KV Cache
- **PDF**: [下载链接](https://arxiv.org/pdf/2512.04040v1)

**摘要**:
A truly interactive world model requires three key ingredients: real-time long-horizon streaming, consistent spatial memory, and precise user control. However, most existing approaches address only one of these aspects in isolation, as achieving all three simultaneously is highly challenging-for example, long-term memory mechanisms often degrade real-time performance. In this work, we present RELIC, a unified framework that tackles these three challenges altogether. Given a single image and a text description, RELIC enables memory-aware, long-duration exploration of arbitrary scenes in real time. Built upon recent autoregressive video-diffusion distillation techniques, our model represents long-horizon memory using highly compressed historical latent tokens encoded with both relative actions and absolute camera poses within the KV cache. This compact, camera-aware memory structure supports implicit 3D-consistent content retrieval and enforces long-term coherence with minimal computational overhead. In parallel, we fine-tune a bidirectional teacher video model to generate sequences beyond its original 5-second training horizon, and transform it into a causal student generator using a new memory-efficient self-forcing paradigm that enables full-context distillation over long-duration teacher as well as long student self-rollouts. Implemented as a 14B-parameter model and trained on a curated Unreal Engine-rendered dataset, RELIC achieves real-time generation at 16 FPS while demonstrating more accurate action following, more stable long-horizon streaming, and more robust spatial-memory retrieval compared with prior work. These capabilities establish RELIC as a strong foundation for the next generation of interactive world modeling.

---

## 2. Reconstructing KV Caches with Cross-layer Fusion For Enhanced Transformers

- **arXiv ID**: [2512.03870v1](http://arxiv.org/abs/2512.03870v1)
- **作者**: Hongzhan Lin, Zhiqi Bai, Xinmiao Zhang, Sen Yang, Xiang Li et al. (13 authors)
- **发布时间**: 2025-12-03T15:22:00+00:00
- **arXiv分类**: cs.CL
- **标签**: KV Cache
- **PDF**: [下载链接](https://arxiv.org/pdf/2512.03870v1)

**摘要**:
Transformer decoders have achieved strong results across tasks, but the memory required for the KV cache becomes prohibitive at long sequence lengths. Although Cross-layer KV Cache sharing (e.g., YOCO, CLA) offers a path to mitigate KV Cache bottleneck, it typically underperforms within-layer methods like GQA. To understand the root cause, we investigate the information flow of keys and values of the top-layers. Our preliminary reveals a clear distribution: values are predominantly derived from the bottom layer, while keys draw more information from both bottom and middle layers. Building upon this, we propose FusedKV, whose top-layer KV caches are a learnable fusion of the most informative ones from the bottom and middle layers. This fusion operates directly on post-RoPE keys, preserving relative positional information without the computational cost of re-applying rotary embeddings. To further improve efficiency, we propose FusedKV-Lite, an cross-layer sharing approach, where top-layer KV caches are directly derived from the bottom-layer values and the middle-layer keys. Compared to FusedKV, FusedKV-Lite reduces I/O overhead at the cost of a slight increase in perplexity. In experiments on LLMs ranging from 332M to 4B parameters, our proposed method reduce 50\% cache memory while achieving lower validation perplexity than the standard Transformer decoder, establishing it as a memory-efficient, high-performance architectural alternative.

---

## 3. KVNAND: Efficient On-Device Large Language Model Inference Using DRAM-Free In-Flash Computing

- **arXiv ID**: [2512.03608v1](http://arxiv.org/abs/2512.03608v1)
- **作者**: Lishuo Deng, Shaojie Xu, Jinwu Chen, Changwei Yan, Jiajie Wang et al. (7 authors)
- **发布时间**: 2025-12-03T09:41:03+00:00
- **arXiv分类**: cs.AR, cs.AI, cs.ET
- **标签**: KV Cache, LLM Inference
- **PDF**: [下载链接](https://arxiv.org/pdf/2512.03608v1)

**摘要**:
Deploying large language models (LLMs) on edge devices enables personalized agents with strong privacy and low cost. However, with tens to hundreds of billions of parameters, single-batch autoregressive inference suffers from extremely low arithmetic intensity, creating severe weight-loading and bandwidth pressures on resource-constrained platforms. Recent in-flash computing (IFC) solutions alleviate this bottleneck by co-locating weight-related linear computations in the decode phase with flash, yet still rely on DRAM for the key-value (KV) cache. As context length grows, the KV cache can exceed model weights in size, imposing prohibitive DRAM cost and capacity requirements. Attempts to offload KV cache to flash suffer from severe performance penalties.
  We propose KVNAND, the first DRAM-free, IFC-based architecture that stores both model weights and KV cache entirely in compute-enabled 3D NAND flash. KVNAND addresses the fundamental performance challenges of flash under intensive KV cache access by leveraging IFC for all memory-bound operations to reduce data transfer overhead, introducing head-group parallelism to boost throughput, and employing page-level KV cache mapping to align token access patterns with flash organization. In addition, we propose a design space exploration framework that evaluates discrete and compact KVNAND variants to balance weight and KV placement, automatically identifying the optimal design trade-off. These techniques mitigate latency, energy, and reliability concerns, turning flash into a practical medium for long-context KV storage. Evaluations on MHA 7B and GQA 70B LLMs show that KVNAND achieves 1.98\(\times\)/1.94\(\times\)/2.05\(\times\) geomean speedup at 128/1K/10K-token contexts compared to DRAM-equipped IFC designs and addresses out-of-memory failures at 100K context length.

---

## 4. Cache What Lasts: Token Retention for Memory-Bounded KV Cache in LLMs

- **arXiv ID**: [2512.03324v1](http://arxiv.org/abs/2512.03324v1)
- **作者**: Ngoc Bui, Shubham Sharma, Simran Lamba, Saumitra Mishra, Rex Ying
- **发布时间**: 2025-12-03T00:20:35+00:00
- **arXiv分类**: cs.LG, cs.AI
- **标签**: KV Cache, LLM Inference
- **PDF**: [下载链接](https://arxiv.org/pdf/2512.03324v1)

**摘要**:
Memory and computation remain core bottlenecks in long-horizon LLM inference due to the quadratic cost of self-attention and the ever-growing key-value (KV) cache. Existing strategies for memory-bounded inference, such as quantization, offloading, or heuristic KV eviction, either incur high orchestration costs or rely on unreliable attention-based proxies of importance. We propose TRIM-KV, a novel approach that learns each token's intrinsic importance at creation time via a lightweight retention gate. Each gate predicts a scalar retention score that decays over time, reflecting the long-term utility of the token for a specific layer and head. Tokens with low scores are evicted when the memory budget is exceeded, ensuring that the cache always contains the most critical tokens. TRIM-KV is trained efficiently through distillation from a frozen LLM combined with a capacity loss, requiring only gate fine-tuning and adding negligible inference overhead. Across mathematical reasoning (GSM8K, MATH-500, AIME24), procedural generation (LongProc), conversational long-memory benchmarks (LongMemEval), and long-context understanding (LongBench and SCBench), TRIM-KV consistently outperforms strong eviction and learnable retrieval baselines, especially in low-memory regimes. Remarkably, it even surpasses full-cache models in some settings, showing that selective retention can serve as a form of regularization, suppressing noise from uninformative tokens. Qualitative analyses further reveal that learned retention scores align with human intuition, naturally recovering heuristics such as sink tokens, sliding windows, and gist compression without explicit design. Beyond efficiency, retention scores provide insights into layer- and head-specific roles, suggesting a new path toward LLM interpretability.

---

