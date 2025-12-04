# LLM Inference - arXiv 论文报告

**生成时间**: 2025-12-04 16:45:10

**分类**: LLM Inference

**论文数量**: 3 篇

---

## 1. AugServe: Adaptive Request Scheduling for Augmented Large Language Model Inference Serving

- **arXiv ID**: [2512.04013v1](http://arxiv.org/abs/2512.04013v1)
- **作者**: Ying Wang, Zhen Jin, Jiexiong Xu, Wenhai Lin, Yiquan Chen et al. (6 authors)
- **发布时间**: 2025-12-03T17:49:38+00:00
- **arXiv分类**: cs.CL
- **标签**: LLM Inference
- **PDF**: [下载链接](https://arxiv.org/pdf/2512.04013v1)

**摘要**:
As augmented large language models (LLMs) with external tools become increasingly popular in web applications, improving augmented LLM inference serving efficiency and optimizing service-level objectives (SLOs) are critical for enhancing user experience. To achieve this, inference systems must maximize request handling within latency constraints, referred to as increasing effective throughput. However, existing systems face two major challenges: (i) reliance on first-come-first-served (FCFS) scheduling causes severe head-of-line blocking, leading to queuing delays exceeding the SLOs for many requests; and (ii) static batch token limit, which fails to adapt to fluctuating loads and hardware conditions. Both of these factors degrade effective throughput and service quality.
  This paper presents AugServe, an efficient inference framework designed to reduce queueing latency and enhance effective throughput for augmented LLM inference services. The core idea of AugServe is a two-stage adaptive request scheduling strategy. Specifically, AugServe combines the inference features of augmented LLM requests to optimize the order of scheduling decisions (stage I). These decisions are continuously refined with runtime information (stage II), adapting to both request characteristics and system capabilities. In addition, AugServe dynamically adjusts the token batching mechanism based on hardware status and real-time load, further enhancing throughput performance. Experimental results show that AugServe achieves 4.7-33.1x and 3.3-13.2x higher effective throughput than vLLM and InferCept, while reducing time-to-first-token (TTFT) by up to 96.3% and 95.0%, respectively.

---

## 2. KVNAND: Efficient On-Device Large Language Model Inference Using DRAM-Free In-Flash Computing

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

## 3. Cache What Lasts: Token Retention for Memory-Bounded KV Cache in LLMs

- **arXiv ID**: [2512.03324v1](http://arxiv.org/abs/2512.03324v1)
- **作者**: Ngoc Bui, Shubham Sharma, Simran Lamba, Saumitra Mishra, Rex Ying
- **发布时间**: 2025-12-03T00:20:35+00:00
- **arXiv分类**: cs.LG, cs.AI
- **标签**: KV Cache, LLM Inference
- **PDF**: [下载链接](https://arxiv.org/pdf/2512.03324v1)

**摘要**:
Memory and computation remain core bottlenecks in long-horizon LLM inference due to the quadratic cost of self-attention and the ever-growing key-value (KV) cache. Existing strategies for memory-bounded inference, such as quantization, offloading, or heuristic KV eviction, either incur high orchestration costs or rely on unreliable attention-based proxies of importance. We propose TRIM-KV, a novel approach that learns each token's intrinsic importance at creation time via a lightweight retention gate. Each gate predicts a scalar retention score that decays over time, reflecting the long-term utility of the token for a specific layer and head. Tokens with low scores are evicted when the memory budget is exceeded, ensuring that the cache always contains the most critical tokens. TRIM-KV is trained efficiently through distillation from a frozen LLM combined with a capacity loss, requiring only gate fine-tuning and adding negligible inference overhead. Across mathematical reasoning (GSM8K, MATH-500, AIME24), procedural generation (LongProc), conversational long-memory benchmarks (LongMemEval), and long-context understanding (LongBench and SCBench), TRIM-KV consistently outperforms strong eviction and learnable retrieval baselines, especially in low-memory regimes. Remarkably, it even surpasses full-cache models in some settings, showing that selective retention can serve as a form of regularization, suppressing noise from uninformative tokens. Qualitative analyses further reveal that learned retention scores align with human intuition, naturally recovering heuristics such as sink tokens, sliding windows, and gist compression without explicit design. Beyond efficiency, retention scores provide insights into layer- and head-specific roles, suggesting a new path toward LLM interpretability.

---

