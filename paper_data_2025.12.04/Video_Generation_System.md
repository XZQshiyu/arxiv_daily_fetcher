# Video Generation (System) - arXiv 论文报告

**生成时间**: 2025-12-04 16:45:10

**分类**: Video Generation (System)

**论文数量**: 4 篇

---

## 1. ReCamDriving: LiDAR-Free Camera-Controlled Novel Trajectory Video Generation

- **arXiv ID**: [2512.03621v1](http://arxiv.org/abs/2512.03621v1)
- **作者**: Yaokun Li, Shuaixian Wang, Mantang Guo, Jiehui Huang, Taojun Ding et al. (9 authors)
- **发布时间**: 2025-12-03T09:55:25+00:00
- **arXiv分类**: cs.CV
- **标签**: Video Generation (System)
- **PDF**: [下载链接](https://arxiv.org/pdf/2512.03621v1)

**摘要**:
We propose ReCamDriving, a purely vision-based, camera-controlled novel-trajectory video generation framework. While repair-based methods fail to restore complex artifacts and LiDAR-based approaches rely on sparse and incomplete cues, ReCamDriving leverages dense and scene-complete 3DGS renderings for explicit geometric guidance, achieving precise camera-controllable generation. To mitigate overfitting to restoration behaviors when conditioned on 3DGS renderings, ReCamDriving adopts a two-stage training paradigm: the first stage uses camera poses for coarse control, while the second stage incorporates 3DGS renderings for fine-grained viewpoint and geometric guidance. Furthermore, we present a 3DGS-based cross-trajectory data curation strategy to eliminate the train-test gap in camera transformation patterns, enabling scalable multi-trajectory supervision from monocular videos. Based on this strategy, we construct the ParaDrive dataset, containing over 110K parallel-trajectory video pairs. Extensive experiments demonstrate that ReCamDriving achieves state-of-the-art camera controllability and structural consistency.

---

## 2. LAMP: Language-Assisted Motion Planning for Controllable Video Generation

- **arXiv ID**: [2512.03619v1](http://arxiv.org/abs/2512.03619v1)
- **作者**: Muhammed Burak Kizil, Enes Sanli, Niloy J. Mitra, Erkut Erdem, Aykut Erdem et al. (6 authors)
- **发布时间**: 2025-12-03T09:51:13+00:00
- **arXiv分类**: cs.CV
- **标签**: Video Generation (System)
- **PDF**: [下载链接](https://arxiv.org/pdf/2512.03619v1)

**摘要**:
Video generation has achieved remarkable progress in visual fidelity and controllability, enabling conditioning on text, layout, or motion. Among these, motion control - specifying object dynamics and camera trajectories - is essential for composing complex, cinematic scenes, yet existing interfaces remain limited. We introduce LAMP that leverages large language models (LLMs) as motion planners to translate natural language descriptions into explicit 3D trajectories for dynamic objects and (relatively defined) cameras. LAMP defines a motion domain-specific language (DSL), inspired by cinematography conventions. By harnessing program synthesis capabilities of LLMs, LAMP generates structured motion programs from natural language, which are deterministically mapped to 3D trajectories. We construct a large-scale procedural dataset pairing natural text descriptions with corresponding motion programs and 3D trajectories. Experiments demonstrate LAMP's improved performance in motion controllability and alignment with user intent compared to state-of-the-art alternatives establishing the first framework for generating both object and camera motions directly from natural language specifications.

---

## 3. GeoVideo: Introducing Geometric Regularization into Video Generation Model

- **arXiv ID**: [2512.03453v1](http://arxiv.org/abs/2512.03453v1)
- **作者**: Yunpeng Bai, Shaoheng Fang, Chaohui Yu, Fan Wang, Qixing Huang
- **发布时间**: 2025-12-03T05:11:57+00:00
- **arXiv分类**: cs.CV
- **标签**: Video Generation (System)
- **PDF**: [下载链接](https://arxiv.org/pdf/2512.03453v1)

**摘要**:
Recent advances in video generation have enabled the synthesis of high-quality and visually realistic clips using diffusion transformer models. However, most existing approaches operate purely in the 2D pixel space and lack explicit mechanisms for modeling 3D structures, often resulting in temporally inconsistent geometries, implausible motions, and structural artifacts. In this work, we introduce geometric regularization losses into video generation by augmenting latent diffusion models with per-frame depth prediction. We adopted depth as the geometric representation because of the great progress in depth prediction and its compatibility with image-based latent encoders. Specifically, to enforce structural consistency over time, we propose a multi-view geometric loss that aligns the predicted depth maps across frames within a shared 3D coordinate system. Our method bridges the gap between appearance generation and 3D structure modeling, leading to improved spatio-temporal coherence, shape consistency, and physical plausibility. Experiments across multiple datasets show that our approach produces significantly more stable and geometrically consistent results than existing baselines.

---

## 4. GalaxyDiT: Efficient Video Generation with Guidance Alignment and Adaptive Proxy in Diffusion Transformers

- **arXiv ID**: [2512.03451v1](http://arxiv.org/abs/2512.03451v1)
- **作者**: Zhiye Song, Steve Dai, Ben Keller, Brucek Khailany
- **发布时间**: 2025-12-03T05:08:18+00:00
- **arXiv分类**: cs.CV, cs.AI, cs.LG
- **标签**: Video Generation (System)
- **PDF**: [下载链接](https://arxiv.org/pdf/2512.03451v1)

**摘要**:
Diffusion models have revolutionized video generation, becoming essential tools in creative content generation and physical simulation. Transformer-based architectures (DiTs) and classifier-free guidance (CFG) are two cornerstones of this success, enabling strong prompt adherence and realistic video quality. Despite their versatility and superior performance, these models require intensive computation. Each video generation requires dozens of iterative steps, and CFG doubles the required compute. This inefficiency hinders broader adoption in downstream applications.
  We introduce GalaxyDiT, a training-free method to accelerate video generation with guidance alignment and systematic proxy selection for reuse metrics. Through rank-order correlation analysis, our technique identifies the optimal proxy for each video model, across model families and parameter scales, thereby ensuring optimal computational reuse. We achieve $1.87\times$ and $2.37\times$ speedup on Wan2.1-1.3B and Wan2.1-14B with only 0.97% and 0.72% drops on the VBench-2.0 benchmark. At high speedup rates, our approach maintains superior fidelity to the base model, exceeding prior state-of-the-art approaches by 5 to 10 dB in peak signal-to-noise ratio (PSNR).

---

