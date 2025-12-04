# LLM Training (System) - arXiv 论文报告

**生成时间**: 2025-12-04 16:45:10

**分类**: LLM Training (System)

**论文数量**: 1 篇

---

## 1. FFTrainer: Fast Failover in Large-Language Model Training with Almost-Free State Management

- **arXiv ID**: [2512.03644v1](http://arxiv.org/abs/2512.03644v1)
- **作者**: Bohan Zhao, Yuanhong Wang, Chenglin Liu, Jiagi Pan, Guang Yang et al. (9 authors)
- **发布时间**: 2025-12-03T10:27:35+00:00
- **arXiv分类**: cs.DC
- **标签**: LLM Training (System)
- **PDF**: [下载链接](https://arxiv.org/pdf/2512.03644v1)

**摘要**:
Recent developments in large language models (LLMs) have introduced new requirements for efficient and robust training. As LLM clusters scale, node failures, lengthy recoveries, and bulky checkpoints erode efficiency. Infrequent asynchronous checkpoints trigger costly rollbacks, yet higher frequencies add prohibitive overhead. To address these challenges, we propose FFTrainer, a system designed for robust LLM training. FFTrainer leverages surplus network capacity to quickly save and load states, thereby preventing rollbacks and accelerating recovery. Compared with prior checkpointing approaches, FFTrainer reduces recovery time by up to 98% and mitigates GPU utilization loss by up to 68% without hindering normal training.

---

