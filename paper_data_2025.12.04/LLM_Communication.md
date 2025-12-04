# LLM Communication - arXiv 论文报告

**生成时间**: 2025-12-04 16:45:10

**分类**: LLM Communication

**论文数量**: 2 篇

---

## 1. Physics-Based Communication Compression via Lyapunov-Weighted Event-Triggered Control

- **arXiv ID**: [2512.03604v1](http://arxiv.org/abs/2512.03604v1)
- **作者**: Abbas Tariverdi
- **发布时间**: 2025-12-03T09:36:20+00:00
- **arXiv分类**: eess.SY
- **标签**: LLM Communication
- **PDF**: [下载链接](https://arxiv.org/pdf/2512.03604v1)

**摘要**:
Event-Triggered Control (ETC) reduces communication overhead in networked systems by transmitting only when stability requires it. Conventional mechanisms use isotropic error thresholds ($\|e\| \le σ\|x\|$), treating all directions equally. This ignores stability geometry and triggers conservatively. We propose a static directional triggering mechanism that exploits this asymmetry. By weighting errors via the Lyapunov matrix $P$, we define an anisotropic half-space scaling with instantaneous energy margins: larger deviations tolerated along stable modes, strict bounds where instability threatens. We prove global asymptotic stability and exclusion of Zeno behavior. Monte Carlo simulations ($N=100$) show 43.6\% fewer events than optimally tuned isotropic methods while achieving $2.1\times$ better control performance than time-varying alternatives. The mechanism functions as a runtime safety gate for learning-based controllers operating under communication constraints.

---

## 2. AsymPuzl: An Asymmetric Puzzle for multi-agent cooperation

- **arXiv ID**: [2512.03466v1](http://arxiv.org/abs/2512.03466v1)
- **作者**: Xavier Cadet, Edward Koh, Peter Chin
- **发布时间**: 2025-12-03T05:42:01+00:00
- **arXiv分类**: cs.MA, cs.AI
- **标签**: LLM Communication
- **PDF**: [下载链接](https://arxiv.org/pdf/2512.03466v1)

**摘要**:
Large Language Model (LLM) agents are increasingly studied in multi-turn, multi-agent scenarios, yet most existing setups emphasize open-ended role-play rather than controlled evaluation. We introduce AsymPuzl, a minimal but expressive two-agent puzzle environment designed to isolate communication under information asymmetry. Each agent observes complementary but incomplete views of a symbolic puzzle and must exchange messages to solve it cooperatively. Using a diverse set of current-generation and open-source LLMs, we show that (i) strong models such as GPT-5 and Claude-4.0 reliably converge across puzzle sizes on the solution by sharing complete information in two turns, (ii) weaker models often ignore partner messages or over-correct their hypotheses, and (iii) feedback design is non-trivial: simple self-feedback improves success rates, while detailed joint feedback can hurt performance. These findings show that even in simple cooperative tasks, LLM communication strategies diverge and depend on the granularity of feedback signals. AsymPuzl thus provides a testbed for probing the limits of multi-turn cooperation and opens avenues for studying coordination mechanisms.

---

