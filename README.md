# Awesome Multimodal Token Compression

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![Paper](https://img.shields.io/badge/Paper-Published-green.svg)](https://arxiv.org/abs/2507.20198)

> **When Tokens Talk Too Much: A Survey of Multimodal Long-Context Token Compression across Images, Videos, and Audios** [[arXiv]](https://arxiv.org/pdf/2507.20198)   
> [Kele Shao](https://cokeshao.github.io/)<sup>\*,1,2</sup>, [Keda Tao](https://kd-tao.github.io/)<sup>\*,1,2</sup>, [Kejia Zhang](https://kejiazhang-robust.github.io/)<sup>3</sup>, [Sicheng Feng](https://fscdc.github.io/)<sup>2,4</sup>, [Mu Cai](https://pages.cs.wisc.edu/~mucai/)<sup>5</sup>, [Yuzhang Shang](https://42shawn.github.io/)<sup>6</sup>, [Haoxuan You](https://hxyou.github.io/)<sup>7</sup>, [Can Qin](https://canqin.tech/)<sup>8</sup>, [Yang Sui](https://eclipsess.github.io/yangsui.github.io/)<sup>9</sup>, [Huan Wang](https://huanwang.tech/)<sup>†,2</sup>
> 
> <sup>1</sup>Zhejiang University, <sup>2</sup>Westlake University, <sup>3</sup>Xiamen University, <sup>4</sup>National University of Singapore, <sup>5</sup>University of Wisconsin-Madison, <sup>6</sup>University of Central Florida, <sup>7</sup>Columbia University, <sup>8</sup>Salesforce AI Research, <sup>9</sup>Rice University

\* Equal Contribution.  † Corresponding Author (wanghuan@westlake.edu.cn).

##  Contact

For questions, suggestions, or collaboration opportunities, please feel free to reach out:

✉️ Email:  [shaokele@gmail.com](mailto:shaokele@gmail.com) or [KD.TAO.CT@outlook.com](mailto:KD.TAO.CT@outlook.com)

## 🔥 News

- **[2025.07.29]** The v1 survey is now published! We've also initialized the repository.

## 🎯 Motivation
<div align="left">
  <img src="images/motivation.png" alt="Awesome Token Compression" width="400"/>
</div>

> **Motivation:** **Up:** Image, video, and audio data types can scale in their representation dimensions, leading to a corresponding increase in the number of tokens. **Down:** Top-performing MLLMs cannot address real-world demands, as the number of tokens for multimodal information, especially video, vastly exceeds that of text. Therefore, token compression is crucial to address this limitation.

## 📚 Contents

- [Awesome Token Compression](#awesome-multimodal-token-compression)
    - [Image-centric](https://github.com/cokeshao/Awesome-Multimodal-Token-Compression/tree/main/image.md)
    - [Video-centric](https://github.com/cokeshao/Awesome-Multimodal-Token-Compression/tree/main/video.md)
    - [Audio-centric](https://github.com/cokeshao/Awesome-Multimodal-Token-Compression/tree/main/audio.md)


## 🚧 TODO

- [ ] Release a web page for easily finding relevant research papers.
- [ ] Release a download tool.
- [ ] Release an easy-to-use pull request tool.

---

## 📌 Citation

Please consider citing our paper in your publications if our findings help your research.

```bibtex
@article{token_compression_survey,
  title={When Tokens Talk Too Much: A Survey of Multimodal Long-Context Token Compression across Images, Videos, and Audios},
  author={Shao, Kele and Tao, Keda and Zhang, Kejia and Feng, Sicheng and Cai, Mu and Shang, Yuzhang and You, Haoxuan and Qin, Can and Sui, Yang and Wang, Huan},
  journal={arXiv preprint arXiv:2507.20198},
  year={2025}
}
```

---

## 🤝 Contributing

We welcome contributions to this survey! Please follow these guidelines:

1. **Fork** the repository
2. **Create** a feature branch
3. **Add** relevant papers with proper formatting
4. **Submit** a pull request with a clear description

### Badge Colors
- ![arXiv Badge](https://img.shields.io/badge/arXiv-red) `red` for arXiv papers
- ![PDF Badge](https://img.shields.io/badge/PDF-blue) `blue` for conference/journal papers
- ![GitHub Badge](https://img.shields.io/badge/GitHub-white) `white` for GitHub repositories
- ![Research Areas Badge](https://img.shields.io/badge/Areas-purple) `purple` for research areas
- ![Categories Badge](https://img.shields.io/badge/Categories-green) `green` for categories
- ![Cost Badge](https://img.shields.io/badge/Cost-yellow) `yellow` for training cost

---
## Image LLM

### 2025

*  [![Arxiv](https://img.shields.io/badge/arXiv-2025\.06-red)]() [![Star](https://img.shields.io/github/stars/Theia-4869/CDPruner.svg?style=social&label=Star)](https://github.com/Theia-4869/CDPruner) [Beyond Attention or Similarity: Maximizing Conditional Diversity for Token Pruning in MLLMs](https://arxiv.org/abs/2506.10967)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2025\.06-red)]() [Generic Token Compression in Multimodal Large Language Models from an Explainability Perspective](https://arxiv.org/abs/2506.01097v1)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Similarity--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Publish](https://img.shields.io/badge/ACL-2025-blue)]() [![Star](https://img.shields.io/github/stars/EffiVLM-Bench/EffiVLM-Bench.svg?style=social&label=Star)](https://github.com/EffiVLM-Bench/EffiVLM-Bench) [EffiVLM-Bench: A Comprehensive Benchmark for Evaluating Training-Free Acceleration in Large Visual-Languge Models](https://arxiv.org/abs/2506.00479)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2025\.05-red)]() [![Star](https://img.shields.io/github/stars/Tencent/SelfEvolvingAgent.svg?style=social&label=Star)](https://github.com/Tencent/SelfEvolvingAgent) [VScan: Rethinking Visual Token Reduction for Efficient Large Vision-Language Models](https://arxiv.org/abs/2505.22654)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Attention--Based-green)]() [![Type](https://img.shields.io/badge/Similarity--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Free-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2025\.05-red)]() [Balanced Token Pruning: Accelerating Vision Language Models Beyond Local Optimization](https://arxiv.org/abs/2505.22038)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Attention--Based-green)]() [![Type](https://img.shields.io/badge/Similarity--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Free-yellow)]()
*  [![Publish](https://img.shields.io/badge/ICML-2025-blue)]() [![Star](https://img.shields.io/github/stars/wangqinsi1/2025-ICML-CoreMatching.svg?style=social&label=Star)](https://github.com/wangqinsi1/2025-ICML-CoreMatching) [CoreMatching: A Co-adaptive Sparse Inference Framework with Token and Neuron Pruning for Comprehensive Acceleration of Vision-Language Models](https://arxiv.org/abs/2505.19235)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Attention--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Free-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2025\.05-red)]() [![Star](https://img.shields.io/github/stars/shilinyan99/CrossLMM.svg?style=social&label=Star)](https://github.com/shilinyan99/CrossLMM) [CrossLMM: Decoupling Long Video Sequences from
LMMs via Dual Cross-Attention Mechanisms](https://arxiv.org/abs/2505.17020)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Area](https://img.shields.io/badge/Video_LLM-purple)]() [![Type](https://img.shields.io/badge/Transformation--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2025\.05-red)]() [![Star](https://img.shields.io/github/stars/xuyang-liu16/VidCom2.svg?style=social&label=Star)](https://github.com/xuyang-liu16/VidCom2) [Video Compression Commander: Plug-and-Play Inference Acceleration for Video Large Language Models](https://arxiv.org/abs/2505.14454)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Area](https://img.shields.io/badge/Video_LLM-purple)]() [![Type](https://img.shields.io/badge/Similarity--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Free-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2025\.05-red)]() [Why 1 + 1 < 1 in Visual Token Pruning: Beyond Naive Integration via Multi-Objective Balanced Covering](https://arxiv.org/abs/2505.10118)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2025\.04-red)]() [![Star](https://img.shields.io/github/stars/MikeWangWZHL/dymu.svg?style=social&label=Star)](https://github.com/MikeWangWZHL/dymu) [DyMU: Dynamic Merging and Virtual Unmerging for Efficient VLMs](https://arxiv.org/abs/2504.17040)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Similarity--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Free-yellow)]()
*  [![Publish](https://img.shields.io/badge/CVPR-2025-blue)]() [PACT: Pruning and Clustering-Based Token Reduction for Faster Visual
Language Models](https://arxiv.org/pdf/2504.08966)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]()
*  [![Publish](https://img.shields.io/badge/ICCV-2025-blue)]() [Skip-Vision: Efficient and Scalable Acceleration of Vision-Language Models via Adaptive Token Skipping](https://arxiv.org/abs/2503.21817)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Similarity--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2025\.03-red)]() [![Star](https://img.shields.io/github/stars/ludc506/InternVL-X.svg?style=social&label=Star)](https://github.com/ludc506/InternVL-X) [InternVL-X: Advancing and Accelerating InternVL Series with Efficient Visual Token Compression](https://arxiv.org/abs/2503.21307)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Area](https://img.shields.io/badge/Video_LLM-purple)]() [![Type](https://img.shields.io/badge/Query--Based-green)]() [![Type](https://img.shields.io/badge/Transformation--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Publish](https://img.shields.io/badge/CVPR-2025-blue)]() [TopV: Compatible Token Pruning with Inference Time Optimization for Fast and Low-Memory Multimodal Vision Language Model](https://arxiv.org/abs/2503.18278)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Similarity--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Free-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2025\.03-red)]() [![Star](https://img.shields.io/github/stars/ShawnTan86/TokenCarve.svg?style=social&label=Star)](https://github.com/ShawnTan86/TokenCarve) [TokenCarve: Information-Preserving Visual Token Compression in Multimodal Large Language Models](https://arxiv.org/abs/2503.10501)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Attention--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Free-yellow)]()
*  [![Publish](https://img.shields.io/badge/CVPR-2025-blue)]() [![Star](https://img.shields.io/github/stars/vbdi/divprune.svg?style=social&label=Star)](https://github.com/vbdi/divprune) [DivPrune: Diversity-based Visual Token Pruning for Large Multimodal Models](https://arxiv.org/abs/2503.02175)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Similarity--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Free-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2025\.03-red)]() [DivPrune: Diversity-based Visual Token Pruning for Large Multimodal Models](https://arxiv.org/pdf/2503.02175)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]()
*  [![Publish](https://img.shields.io/badge/NAACL-2025-blue)]() [MEDA: Dynamic KV Cache Allocation for Efficient
Multimodal Long-Context Inference](https://arxiv.org/abs/2502.17599)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Area](https://img.shields.io/badge/Video_LLM-purple)]()
*  [![Publish](https://img.shields.io/badge/ACL_Findings-2025-blue)]() [Token Pruning in Multimodal Large Language Models: Are We Solving the Right Problem?](https://arxiv.org/abs/2502.11501)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Attention--Based-green)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2025\.02-red)]() [![Star](https://img.shields.io/github/stars/ZichenWen1/DART.svg?style=social&label=Star)](https://github.com/ZichenWen1/DART) [Stop Looking for Important Tokens in Multimodal Language Models: Duplication Matters More](https://arxiv.org/abs/2502.11494)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2025\.01-red)]() [AdaFV: Rethinking of Visual-Language alignment for VLM acceleration](https://arxiv.org/abs/2501.09532)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Query--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Free-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2025\.01-red)]() [![Star](https://img.shields.io/github/stars/xuyang-liu16/GlobalCom2.svg?style=social&label=Star)](https://github.com/xuyang-liu16/GlobalCom2) [Global Compression Commander: Plug-and-Play Inference Acceleration for High-Resolution Large Vision-Language Models](https://arxiv.org/abs/2501.05179)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Attention--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Free-yellow)]()
*  [![Publish](https://img.shields.io/badge/ICLR-2025-blue)]() [![Star](https://img.shields.io/github/stars/ictnlp/LLaVA-Mini.svg?style=social&label=Star)](https://github.com/ictnlp/LLaVA-Mini) [LLaVA-Mini: Efficient Image and Video Large Multimodal Models with One Vision Token](https://arxiv.org/abs/2501.03895)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Area](https://img.shields.io/badge/Video_LLM-purple)]() [![Type](https://img.shields.io/badge/Query--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Publish](https://img.shields.io/badge/ICCV-2025-blue)]() [![Star](https://img.shields.io/github/stars/anakin-skywalker-Joseph/Folder.svg?style=social&label=Star)](https://github.com/anakin-skywalker-Joseph/Folder) [FOLDER: Accelerating Multi-modal Large Language Models with Enhanced Performance](https://arxiv.org/abs/2501.02430)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Attention--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Free-yellow)]()
*  [![Publish](https://img.shields.io/badge/AAAI-2025-blue)]() [What Kind of Visual Tokens Do We Need? Training-free Visual Token Pruning for Multi-modal Large Language Models from the Perspective of Graph](https://arxiv.org/abs/2501.02268)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Similarity--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Free-yellow)]()

### 2024

*  [![Publish](https://img.shields.io/badge/AAAI-2025-blue)]() [ST3: Accelerating Multimodal Large Language Model by Spatial-Temporal Visual Token Trimming](https://arxiv.org/abs/2412.20105)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Attention--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Free-yellow)]()
*  [![Publish](https://img.shields.io/badge/CVPR-2025-blue)]() [![Star](https://img.shields.io/github/stars/OpenGVLab/PVC.svg?style=social&label=Star)](https://github.com/OpenGVLab/PVC) [PVC: Progressive Visual Token Compression for Unified Image and Video Processing in Large Vision-Language Models](https://arxiv.org/abs/2412.09613)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Area](https://img.shields.io/badge/Video_LLM-purple)]() [![Type](https://img.shields.io/badge/Transformation--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2024\.12-red)]() [![Star](https://img.shields.io/github/stars/hulianyuyy/iLLaVA.svg?style=social&label=Star)](https://github.com/hulianyuyy/iLLaVA) [iLLaVA: An Image is Worth Fewer Than 1/3 Input Tokens in Large Multimodal Models](https://arxiv.org/abs/2412.06263)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Attention--Based-green)]() [![Type](https://img.shields.io/badge/Similarity--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Free-yellow)]()
*  [![Publish](https://img.shields.io/badge/CVPR-2025-blue)]() [![Star](https://img.shields.io/github/stars/dvlab-research/VisionZip.svg?style=social&label=Star)](https://github.com/dvlab-research/VisionZip) [VisionZip: Longer is Better but Not Necessary in Vision Language Models](https://arxiv.org/abs/2412.04467)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Attention--Based-green)]() [![Type](https://img.shields.io/badge/Similarity--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Free-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2024\.12-red)]() [![Star](https://img.shields.io/github/stars/Theia-4869/FasterVLM.svg?style=social&label=Star)](https://github.com/Theia-4869/FasterVLM) [[CLS] Attention is All You Need for Training-Free Visual Token Pruning: Make VLM Inference Faster](https://arxiv.org/abs/2412.01818)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Attention--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Free-yellow)]()
*  [![Publish](https://img.shields.io/badge/ICCV-2025-blue)]() [![Star](https://img.shields.io/github/stars/Theia-4869/VisPruner.svg?style=social&label=Star)](https://github.com/Theia-4869/VisPruner) [Beyond Text-Visual Attention: Exploiting Visual Cues for Effective Token Pruning in VLMs](https://arxiv.org/abs/2412.01818)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Attention--Based-green)]() [![Type](https://img.shields.io/badge/Similarity--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Free-yellow)]()
*  [![Publish](https://img.shields.io/badge/CVPR-2025-blue)]() [Accelerating Multimodal Large Language Models by Searching Optimal Vision Token Reduction](https://arxiv.org/abs/2412.00556)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Attention--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Free-yellow)]()
*  [![Publish](https://img.shields.io/badge/CVPR-2025-blue)]() [ATP-LLaVA: Adaptive Token Pruning for Large Vision Language Models](https://arxiv.org/abs/2412.00447)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Attention--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2024\.11-red)]() [Efficient Multi-modal Large Language Models via Visual Token Grouping](https://arxiv.org/abs/2411.17773v1)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Query--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2024\.11-red)]() [![Star](https://img.shields.io/github/stars/kawhiiiileo/FiCoCo.svg?style=social&label=Star)](https://github.com/kawhiiiileo/FiCoCo) [Filter, Correlate, Compress: Training-Free Token Reduction for MLLM Acceleration](https://arxiv.org/abs/2411.17686v3)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Attention--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Free-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2024\.11-red)]() [FocusLLaVA: A Coarse-to-Fine Approach for Efficient and Effective Visual Token Compression](https://arxiv.org/abs/2411.14228)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Attention--Based-green)]() [![Type](https://img.shields.io/badge/Transformation--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Publish](https://img.shields.io/badge/CVPR_Highlight-2025-blue)]() [AdaCM2: Adaptive Cross‑Modality Memory Reduction](https://arxiv.org/abs/2411.12593)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Area](https://img.shields.io/badge/Video_LLM-purple)]() [![Type](https://img.shields.io/badge/Query--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2024\.11-red)]() [![Star](https://img.shields.io/github/stars/liuting20/MustDrop.svg?style=social&label=Star)](https://github.com/liuting20/MustDrop) [Multi-Stage Vision Token Dropping: Towards Efficient Multimodal Large Language Model](https://arxiv.org/abs/2411.10803)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Attention--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Free-yellow)]()
*  [![Publish](https://img.shields.io/badge/CVPR-2025-blue)]() [![Star](https://img.shields.io/github/stars/Cooperx521/PyramidDrop.svg?style=social&label=Star)](https://github.com/Cooperx521/PyramidDrop) [PyramidDrop: Accelerating Your Large Vision-Language Models via Pyramid Visual Redundancy Reduction](https://arxiv.org/abs/2410.17247)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Attention--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]() [![Cost](https://img.shields.io/badge/Training--Free-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2024\.10-red)]() [Efficient Vision-Language Models by Summarizing Visual Tokens into Compact Registers](https://arxiv.org/abs/2410.14072v1)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Query--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Publish](https://img.shields.io/badge/ICCV-2025-blue)]() [ZipVL: Efficient Large Vision-Language Models with Dynamic Token Sparsification](https://arxiv.org/abs/2410.08584)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Attention--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Free-yellow)]()
*  [![Publish](https://img.shields.io/badge/ICML-2025-blue)]() [![Star](https://img.shields.io/github/stars/Gumpest/SparseVLMs.svg?style=social&label=Star)](https://github.com/Gumpest/SparseVLMs) [SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference](https://arxiv.org/abs/2410.04417)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Attention--Based-green)]() [![Type](https://img.shields.io/badge/Query--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Free-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2024\.09-red)]() [![Star](https://img.shields.io/github/stars/NVIDIA/Megatron-LM.svg?style=social&label=Star)](https://github.com/NVIDIA/Megatron-LM) [NVLM: Open Frontier-Class Multimodal LLMs](https://arxiv.org/abs/2409.11402)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Transformation--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Publish](https://img.shields.io/badge/COLING-2025-blue)]() [![Star](https://img.shields.io/github/stars/FreedomIntelligence/TRIM.svg?style=social&label=Star)](https://github.com/FreedomIntelligence/TRIM) [Less is More: A Simple yet Effective Token Reduction Method for Efficient Multi-modal LLMs](https://arxiv.org/abs/2409.10994)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Similarity--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Free-yellow)]()
*  [![Publish](https://img.shields.io/badge/AAAI-2025-blue)]() [![Star](https://img.shields.io/github/stars/ywh187/FitPrune.svg?style=social&label=Star)](https://github.com/ywh187/FitPrune) [Fit and Prune: Fast and Training-free Visual Token Pruning for Multi-modal Large Language Models](https://arxiv.org/abs/2409.10197)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Attention--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Free-yellow)]()
*  [![Publish](https://img.shields.io/badge/AAAI-2025-blue)]() [![Star](https://img.shields.io/github/stars/hasanar1f/HiRED.svg?style=social&label=Star)](https://github.com/hasanar1f/HiRED) [HiRED: Attention-Guided Token Dropping for Efficient Inference of High-Resolution Vision-Language Models](https://arxiv.org/abs/2408.10945)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Transformation--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Free-yellow)]()
*  [![Publish](https://img.shields.io/badge/IJCV-2025-blue)]() [![Star](https://img.shields.io/github/stars/CircleRadon/TokenPacker.svg?style=social&label=Star)](https://github.com/CircleRadon/TokenPacker) [TokenPacker: Efficient Visual Projector for Multimodal LLM](https://arxiv.org/abs/2407.02392)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Query--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Publish](https://img.shields.io/badge/EMNLP_Findings-2024-blue)]() [![Star](https://img.shields.io/github/stars/SUSTechBruce/LOOK-M.svg?style=social&label=Star)](https://github.com/SUSTechBruce/LOOK-M) [LOOK-M: Look-Once Optimization in KV Cache for Efficient Multimodal Long-Context Inference](https://arxiv.org/abs/2406.18139)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]()
*  [![Publish](https://img.shields.io/badge/CVPR-2025-blue)]() [![Star](https://img.shields.io/github/stars/Yxxxb/VoCo-LLaMA.svg?style=social&label=Star)](https://github.com/Yxxxb/VoCo-LLaMA) [VoCo-LLaMA: Towards Vision Compression with Large Language Models](https://arxiv.org/abs/2406.12275v2)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Query--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Publish](https://img.shields.io/badge/CVPR-2025-blue)]() [![Star](https://img.shields.io/github/stars/Yxxxb/VoCo-LLaMA.svg?style=social&label=Star)](https://github.com/Yxxxb/VoCo-LLaMA) [VoCo-LLaMA: Towards Vision Compression with Large Language Models](https://arxiv.org/abs/2406.12275)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Query--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2024\.05-red)]() [![Star](https://img.shields.io/github/stars/yaolinli/DeCo.svg?style=social&label=Star)](https://github.com/yaolinli/DeCo) [DeCo: Decoupling Token Compression from Semantic Abstraction in Multimodal Large Language Models](https://arxiv.org/abs/2405.20985)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Transformation--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Publish](https://img.shields.io/badge/ICLR-2025-blue)]() [![Star](https://img.shields.io/github/stars/mu-cai/matryoshka-mm.svg?style=social&label=Star)](https://github.com/mu-cai/matryoshka-mm) [Matryoshka Multimodal Models](https://arxiv.org/abs/2405.17430)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Transformation--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Publish](https://img.shields.io/badge/AAAI_oral-2025-blue)]() [![Star](https://img.shields.io/github/stars/lzhxmu/VTW.svg?style=social&label=Star)](https://github.com/lzhxmu/VTW) [Boosting multimodal large language models with visual tokens withdrawal for rapid inference.](https://arxiv.org/abs/2405.05803)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Attention--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Free-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2024\.04-red)]() [![Star](https://img.shields.io/github/stars/OpenGVLab/InternVL.svg?style=social&label=Star)](https://github.com/OpenGVLab/InternVL) [How Far Are We to GPT-4V? Closing the Gap to Commercial Multimodal Models with Open-Source Suites](https://arxiv.org/abs/2404.16821)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Transformation--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Publish](https://img.shields.io/badge/ICCV-2025-blue)]() [![Star](https://img.shields.io/github/stars/42Shawn/LLaVA-PruMerge.svg?style=social&label=Star)](https://github.com/42Shawn/LLaVA-PruMerge) [LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models](https://arxiv.org/abs/2403.15388)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Attention--Based-green)]() [![Type](https://img.shields.io/badge/Transformation--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Free-yellow)]()
*  [![Publish](https://img.shields.io/badge/ECCV_Oral-2024-blue)]() [![Star](https://img.shields.io/github/stars/pkunlp-icler/FastV.svg?style=social&label=Star)](https://github.com/pkunlp-icler/FastV) [An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models](https://arxiv.org/abs/2403.06764)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Attention--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Free-yellow)]()
*  [![Publish](https://img.shields.io/badge/EMNLP_Findings-2024-blue)]() [LaCo: Layer-wise Compression for Efficient MLLMs](https://arxiv.org/abs/2402.11187)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Transformation--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2024\.02-red)]() [![Star](https://img.shields.io/github/stars/Meituan-AutoML/MobileVLM.svg?style=social&label=Star)](https://github.com/Meituan-AutoML/MobileVLM) [MobileVLM V2: Faster and Stronger Baseline for Vision Language Model](https://arxiv.org/abs/2402.03766)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Transformation--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()

### 2023

*  [![Arxiv](https://img.shields.io/badge/arXiv-2023\.12-red)]() [![Star](https://img.shields.io/github/stars/Meituan-AutoML/MobileVLM.svg?style=social&label=Star)](https://github.com/Meituan-AutoML/MobileVLM) [MobileVLM : A Fast, Strong and Open Vision Language Assistant for Mobile Devices](https://arxiv.org/abs/2312.16886)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Transformation--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Publish](https://img.shields.io/badge/CVPR-2024-blue)]() [![Star](https://img.shields.io/github/stars/khanrc/honeybee?tab=readme-ov-file.svg?style=social&label=Star)](https://github.com/khanrc/honeybee?tab=readme-ov-file) [Honeybee: Locality-enhanced Projector for Multimodal LLM](https://arxiv.org/abs/2312.06742)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Transformation--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2023\.08-red)]() [![Star](https://img.shields.io/github/stars/QwenLM/Qwen-VL.svg?style=social&label=Star)](https://github.com/QwenLM/Qwen-VL) [Qwen-VL: A Versatile Vision-Language Model for Understanding, Localization, Text Reading, and Beyond](https://arxiv.org/abs/2308.12966)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Query--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2023\.06-red)]() [Video-LLaMA: An Instruction-tuned Audio-Visual Language Model for Video Understanding](https://arxiv.org/abs/2306.02858)
 [![Area](https://img.shields.io/badge/Audio_LLM-purple)]() [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Area](https://img.shields.io/badge/Video_LLM-purple)]() [![Type](https://img.shields.io/badge/Query--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2023\.05-red)]() [![Star](https://img.shields.io/github/stars/csarron/PuMer.svg?style=social&label=Star)](https://github.com/csarron/PuMer) [PuMer: Pruning and Merging Tokens for Efficient Vision Language Models](https://arxiv.org/abs/2305.17530)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Similarity--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2023\.05-red)]() [![Star](https://img.shields.io/github/stars/salesforce/LAVIS.svg?style=social&label=Star)](https://github.com/salesforce/LAVIS) [InstructBLIP: Towards General-purpose Vision-Language Models with Instruction Tuning](https://arxiv.org/abs/2305.06500)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Query--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2023\.04-red)]() [![Star](https://img.shields.io/github/stars/X-PLUG/mPLUG-Owl.svg?style=social&label=Star)](https://github.com/X-PLUG/mPLUG-Owl) [mPLUG-Owl: Modularization Empowers Large Language Models with Multimodality](https://arxiv.org/abs/2304.14178)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Query--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Publish](https://img.shields.io/badge/ICLR-2024-blue)]() [![Star](https://img.shields.io/github/stars/Vision-CAIR/MiniGPT-4.svg?style=social&label=Star)](https://github.com/Vision-CAIR/MiniGPT-4) [Minigpt-4: Enhancing vision-language understanding with advanced large language models.](https://arxiv.org/abs/2304.10592)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Query--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Publish](https://img.shields.io/badge/ICML-2023-blue)]() [![Star](https://img.shields.io/github/stars/salesforce/LAVIS.svg?style=social&label=Star)](https://github.com/salesforce/LAVIS) [BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models](https://arxiv.org/abs/2301.12597)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Query--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()

### 2022

*  [![Publish](https://img.shields.io/badge/NeurIPS-2022-blue)]() [Flamingo: a Visual Language Model for Few-Shot Learning](https://arxiv.org/abs/2204.14198)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Query--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()

---
## Video LLM

### 2025

*  [![Publish](https://img.shields.io/badge/ICCV-2025-blue)]() [![Star](https://img.shields.io/github/stars/HYUNJS/STTM.svg?style=social&label=Star)](https://github.com/HYUNJS/STTM) [Multi-Granular Spatio-Temporal Token Merging for Training-Free Acceleration of Video LLMs](https://arxiv.org/abs/2507.07990)
 [![Area](https://img.shields.io/badge/Video_LLM-purple)]() [![Type](https://img.shields.io/badge/Similarity--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Free-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2025\.06-red)]() [![Star](https://img.shields.io/github/stars/HumanMLLM/LLaVA-Scissor.svg?style=social&label=Star)](https://github.com/HumanMLLM/LLaVA-Scissor) [LLaVA-Scissor: Token Compression with Semantic Connected Components for Video LLMs](https://www.arxiv.org/abs/2506.21862)
 [![Area](https://img.shields.io/badge/Video_LLM-purple)]() [![Type](https://img.shields.io/badge/Similarity--Based-green)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2025\.06-red)]() [DynTok: Dynamic Compression of Visual Tokens for Efficient and Effective Video Understanding](https://arxiv.org/abs/2506.03990)
 [![Area](https://img.shields.io/badge/Video_LLM-purple)]() [![Type](https://img.shields.io/badge/Similarity--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Free-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2025\.06-red)]() [![Star](https://img.shields.io/github/stars/mnyuew/METok.svg?style=social&label=Star)](https://github.com/mnyuew/METok) [METok: Multi-Stage Event-based Token Compression for Efficient Long Video Understanding](https://arxiv.org/abs/2506.02850)
 [![Area](https://img.shields.io/badge/Video_LLM-purple)]() [![Type](https://img.shields.io/badge/Attention--Based-green)]() [![Type](https://img.shields.io/badge/Query--Based-green)]() [![Type](https://img.shields.io/badge/Transformation--Based-green)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2025\.06-red)]() [![Star](https://img.shields.io/github/stars/yunzhuzhang0918/flexselect.svg?style=social&label=Star)](https://github.com/yunzhuzhang0918/flexselect) [FlexSelect: Flexible Token Selection for Efficient Long Video Understanding](https://arxiv.org/abs/2506.00993)
 [![Area](https://img.shields.io/badge/Video_LLM-purple)]() [![Type](https://img.shields.io/badge/Attention--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Free-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2025\.05-red)]() [![Star](https://img.shields.io/github/stars/cokeshao/HoliTom.svg?style=social&label=Star)](https://github.com/cokeshao/HoliTom) [HoliTom: Holistic Token Merging for Fast Video Large Language Models](https://arxiv.org/abs/2505.21334)
 [![Area](https://img.shields.io/badge/Video_LLM-purple)]() [![Type](https://img.shields.io/badge/Attention--Based-green)]() [![Type](https://img.shields.io/badge/Similarity--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Free-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2025\.05-red)]() [AdaTP: Attention-Debiased Token Pruning for
Video Large Language Models](https://arxiv.org/abs/2505.20100)
 [![Area](https://img.shields.io/badge/Video_LLM-purple)]() [![Type](https://img.shields.io/badge/Attention--Based-green)]() [![Type](https://img.shields.io/badge/Query--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Free-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2025\.05-red)]() [![Star](https://img.shields.io/github/stars/shilinyan99/CrossLMM.svg?style=social&label=Star)](https://github.com/shilinyan99/CrossLMM) [CrossLMM: Decoupling Long Video Sequences from
LMMs via Dual Cross-Attention Mechanisms](https://arxiv.org/abs/2505.17020)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Area](https://img.shields.io/badge/Video_LLM-purple)]() [![Type](https://img.shields.io/badge/Transformation--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2025\.05-red)]() [![Star](https://img.shields.io/github/stars/xuyang-liu16/VidCom2.svg?style=social&label=Star)](https://github.com/xuyang-liu16/VidCom2) [Video Compression Commander: Plug-and-Play Inference Acceleration for Video Large Language Models](https://arxiv.org/abs/2505.14454)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Area](https://img.shields.io/badge/Video_LLM-purple)]() [![Type](https://img.shields.io/badge/Similarity--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Free-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2025\.05-red)]() [![Star](https://img.shields.io/github/stars/ByteDance-Seed/Seed1.5-VL.svg?style=social&label=Star)](https://github.com/ByteDance-Seed/Seed1.5-VL) [Seed1.5-VL Technical Report](https://arxiv.org/abs/2505.07062)
 [![Area](https://img.shields.io/badge/Video_LLM-purple)]() [![Type](https://img.shields.io/badge/Transformation--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2025\.04-red)]() [![Star](https://img.shields.io/github/stars/yaolinli/TimeChat-Online.svg?style=social&label=Star)](https://github.com/yaolinli/TimeChat-Online) [TimeChat-Online: 80% Visual Tokens are Naturally Redundant in Streaming Videos](https://arxiv.org/abs/2504.17343)
 [![Area](https://img.shields.io/badge/Streaming_Video_LLM-purple)]() [![Type](https://img.shields.io/badge/Similarity--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2025\.04-red)]() [QG-VTC: Question-Guided Visual Token Compression in MLLMs for Efficient VQA](https://arxiv.org/abs/2504.00654)
 [![Area](https://img.shields.io/badge/Video_LLM-purple)]() [![Type](https://img.shields.io/badge/Query--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2025\.03-red)]() [![Star](https://img.shields.io/github/stars/ludc506/InternVL-X.svg?style=social&label=Star)](https://github.com/ludc506/InternVL-X) [InternVL-X: Advancing and Accelerating InternVL Series with Efficient Visual Token Compression](https://arxiv.org/abs/2503.21307)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Area](https://img.shields.io/badge/Video_LLM-purple)]() [![Type](https://img.shields.io/badge/Query--Based-green)]() [![Type](https://img.shields.io/badge/Transformation--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2025\.03-red)]() [![Star](https://img.shields.io/github/stars/LunarShen/FastVID.svg?style=social&label=Star)](https://github.com/LunarShen/FastVID) [FastVID: Dynamic Density Pruning for Fast Video Large Language Models](https://arxiv.org/abs/2503.11187)
 [![Area](https://img.shields.io/badge/Video_LLM-purple)]() [![Type](https://img.shields.io/badge/Attention--Based-green)]() [![Type](https://img.shields.io/badge/Similarity--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Free-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2025\.03-red)]() [Keyframe-oriented Vision Token Pruning: Enhancing Efficiency of Large Vision Language Models on Long-Form Video Processing](https://arxiv.org/abs/2503.10742v1)
 [![Area](https://img.shields.io/badge/Video_LLM-purple)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2025\.03-red)]() [Token-Efficient Long Video Understanding for Multimodal LLMs](https://arxiv.org/abs/2503.04130v1)
 [![Area](https://img.shields.io/badge/Video_LLM-purple)]() [![Type](https://img.shields.io/badge/Transformation--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Publish](https://img.shields.io/badge/NAACL-2025-blue)]() [MEDA: Dynamic KV Cache Allocation for Efficient
Multimodal Long-Context Inference](https://arxiv.org/abs/2502.17599)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Area](https://img.shields.io/badge/Video_LLM-purple)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2025\.02-red)]() [![Star](https://img.shields.io/github/stars/QwenLM/Qwen2.5-VL.svg?style=social&label=Star)](https://github.com/QwenLM/Qwen2.5-VL) [Qwen2.5-VL Technical Report](https://arxiv.org/abs/2502.13923)
 [![Area](https://img.shields.io/badge/Video_LLM-purple)]() [![Type](https://img.shields.io/badge/Transformation--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Publish](https://img.shields.io/badge/ICLR-2025-blue)]() [![Star](https://img.shields.io/github/stars/ictnlp/LLaVA-Mini.svg?style=social&label=Star)](https://github.com/ictnlp/LLaVA-Mini) [LLaVA-Mini: Efficient Image and Video Large Multimodal Models with One Vision Token](https://arxiv.org/abs/2501.03895)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Area](https://img.shields.io/badge/Video_LLM-purple)]() [![Type](https://img.shields.io/badge/Query--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Publish](https://img.shields.io/badge/ICCV-2025-blue)]() [![Star](https://img.shields.io/github/stars/thu-nics/FrameFusion.svg?style=social&label=Star)](https://github.com/thu-nics/FrameFusion) [FrameFusion: Combining Similarity and Importance for Video Token Reduction
on Large Visual Language Models](https://arxiv.org/abs/2501.01986)
 [![Area](https://img.shields.io/badge/Video_LLM-purple)]() [![Type](https://img.shields.io/badge/Attention--Based-green)]() [![Type](https://img.shields.io/badge/Similarity--Based-green)]()
*  [![Publish](https://img.shields.io/badge/ICLR-2025-blue)]() [![Star](https://img.shields.io/github/stars/rese1f/aurora.svg?style=social&label=Star)](https://github.com/rese1f/aurora) [AuroraCap: Efficient, Performant Video Detailed Captioning and a New Benchmark](https://arxiv.org/abs/2410.03051)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Area](https://img.shields.io/badge/Video_LLM-purple)]() [![Type](https://img.shields.io/badge/Similarity--Based-green)]()
*  [![Publish](https://img.shields.io/badge/CVPR-2025-blue)]() [Zero-shot 3D Question Answering via Voxel-based Dynamic Token Compression](https://openaccess.thecvf.com/content/CVPR2025/papers/Huang_Zero-shot_3D_Question_Answering_via_Voxel-based_Dynamic_Token_Compression_CVPR_2025_paper.pdf)
 [![Area](https://img.shields.io/badge/Video_LLM-purple)]() [![Area](https://img.shields.io/badge/3D_LLM-purple)]() [![Type](https://img.shields.io/badge/Similarity--Based-green)]()
*  [![Publish](https://img.shields.io/badge/IROS-2025-blue)]() [ToSA: Token Merging with Spatial Awareness](https://arxiv.org/abs/2506.20066) 
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Type](https://img.shields.io/badge/Similarity--Based-green)]()

### 2024

*  [![Publish](https://img.shields.io/badge/ACL-2025-blue)]() [![Star](https://img.shields.io/github/stars/Visual-AI/PruneVid.svg?style=social&label=Star)](https://github.com/Visual-AI/PruneVid) [PruneVid: Visual Token Pruning for Efficient Video Large Language Models](https://arxiv.org/abs/2412.16117v1)
 [![Area](https://img.shields.io/badge/Video_LLM-purple)]() [![Type](https://img.shields.io/badge/Attention--Based-green)]() [![Type](https://img.shields.io/badge/Similarity--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Free-yellow)]()
*  [![Publish](https://img.shields.io/badge/CVPR-2025-blue)]() [![Star](https://img.shields.io/github/stars/OpenGVLab/PVC.svg?style=social&label=Star)](https://github.com/OpenGVLab/PVC) [PVC: Progressive Visual Token Compression for Unified Image and Video Processing in Large Vision-Language Models](https://arxiv.org/abs/2412.09613)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Area](https://img.shields.io/badge/Video_LLM-purple)]() [![Type](https://img.shields.io/badge/Transformation--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Publish](https://img.shields.io/badge/ICCV-2025-blue)]() [![Star](https://img.shields.io/github/stars/Hon-Wong/ByteVideoLLM.svg?style=social&label=Star)](https://github.com/Hon-Wong/ByteVideoLLM) [Dynamic-VLM: Simple Dynamic Visual Token Compression for VideoLLM](https://arxiv.org/abs/2412.09530)
 [![Area](https://img.shields.io/badge/Video_LLM-purple)]() [![Type](https://img.shields.io/badge/Similarity--Based-green)]() [![Type](https://img.shields.io/badge/Transformation--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Publish](https://img.shields.io/badge/CVPR-2025-blue)]() [![Star](https://img.shields.io/github/stars/KD-TAO/DyCoke?tab=readme-ov-file.svg?style=social&label=Star)](https://github.com/KD-TAO/DyCoke?tab=readme-ov-file) [DyCoke: Dynamic Compression of Tokens for Fast Video Large Language Models](https://arxiv.org/abs/2411.15024)
 [![Area](https://img.shields.io/badge/Video_LLM-purple)]() [![Type](https://img.shields.io/badge/Similarity--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Free-yellow)]()
*  [![Publish](https://img.shields.io/badge/CVPR_Highlight-2025-blue)]() [AdaCM2: Adaptive Cross‑Modality Memory Reduction](https://arxiv.org/abs/2411.12593)
 [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Area](https://img.shields.io/badge/Video_LLM-purple)]() [![Type](https://img.shields.io/badge/Query--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Publish](https://img.shields.io/badge/ICML-2025-blue)]() [![Star](https://img.shields.io/github/stars/Vision-CAIR/LongVU.svg?style=social&label=Star)](https://github.com/Vision-CAIR/LongVU) [LongVU: Spatiotemporal Adaptive Compression for Long Video-Language Understanding](https://arxiv.org/abs/2410.17434)
 [![Area](https://img.shields.io/badge/Video_LLM-purple)]() [![Type](https://img.shields.io/badge/Query--Based-green)]() [![Type](https://img.shields.io/badge/Similarity--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2024\.10-red)]() [![Star](https://img.shields.io/github/stars/LLaVA-VL/LLaVA-NeXT.svg?style=social&label=Star)](https://github.com/LLaVA-VL/LLaVA-NeXT) [Video Instruction Tuning with Synthetic Data](http://arxiv.org/abs/2410.02713)
 [![Area](https://img.shields.io/badge/Video_LLM-purple)]() [![Type](https://img.shields.io/badge/Transformation--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2024\.09-red)]() [![Star](https://img.shields.io/github/stars/QwenLM/Qwen2-VL.svg?style=social&label=Star)](https://github.com/QwenLM/Qwen2-VL) [Qwen2-VL: Enhancing Vision-Language Model's Perception of the World at Any Resolution](https://arxiv.org/abs/2409.12191)
 [![Area](https://img.shields.io/badge/Video_LLM-purple)]() [![Type](https://img.shields.io/badge/Transformation--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2024\.08-red)]() [![Star](https://img.shields.io/github/stars/LLaVA-VL/LLaVA-NeXT.svg?style=social&label=Star)](https://github.com/LLaVA-VL/LLaVA-NeXT) [LLaVA-OneVision: Easy Visual Task Transfer](https://arxiv.org/abs/2408.03326)
 [![Area](https://img.shields.io/badge/Video_LLM-purple)]() [![Type](https://img.shields.io/badge/Transformation--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2024\.07-red)]() [![Star](https://img.shields.io/github/stars/apple/ml-slowfast-llava.svg?style=social&label=Star)](https://github.com/apple/ml-slowfast-llava) [SlowFast-LLaVA: A Strong Training-Free Baseline for Video Large Language Models](https://arxiv.org/abs/2407.15841)
 [![Area](https://img.shields.io/badge/Video_LLM-purple)]() [![Type](https://img.shields.io/badge/Transformation--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2024\.06-red)]() [![Star](https://img.shields.io/github/stars/DAMO-NLP-SG/VideoLLaMA2.svg?style=social&label=Star)](https://github.com/DAMO-NLP-SG/VideoLLaMA2) [VideoLLaMA 2: Advancing Spatial-Temporal Modeling and Audio Understanding in Video-LLMs](https://arxiv.org/abs/2406.07476)
 [![Area](https://img.shields.io/badge/Audio_LLM-purple)]() [![Area](https://img.shields.io/badge/Video_LLM-purple)]() [![Type](https://img.shields.io/badge/Transformation--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2024\.04-red)]() [![Star](https://img.shields.io/github/stars/magic-research/PLLaVA.svg?style=social&label=Star)](https://github.com/magic-research/PLLaVA) [PLLaVA : Parameter-free LLaVA Extension from Images to Videos for Video Dense Captioning](https://arxiv.org/abs/2404.16994)
 [![Area](https://img.shields.io/badge/Video_LLM-purple)]() [![Type](https://img.shields.io/badge/Transformation--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Publish](https://img.shields.io/badge/ECCV-2024-blue)]() [![Star](https://img.shields.io/github/stars/ziplab/LongVLM.svg?style=social&label=Star)](https://github.com/ziplab/LongVLM) [LongVLM: Efficient Long Video Understanding via Large Language Models](https://arxiv.org/abs/2404.03384)
 [![Area](https://img.shields.io/badge/Video_LLM-purple)]() [![Type](https://img.shields.io/badge/Transformation--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()

### 2023

*  [![Publish](https://img.shields.io/badge/ECCV-2024-blue)]() [![Star](https://img.shields.io/github/stars/dvlab-research/LLaMA-VID.svg?style=social&label=Star)](https://github.com/dvlab-research/LLaMA-VID) [LLaMA-VID: An Image is Worth 2 Tokens in Large Language Models](https://arxiv.org/abs/2311.17043)
 [![Area](https://img.shields.io/badge/Video_LLM-purple)]() [![Type](https://img.shields.io/badge/Query--Based-green)]() [![Type](https://img.shields.io/badge/Transformation--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Publish](https://img.shields.io/badge/CVPR_Highlight-2024-blue)]() [![Star](https://img.shields.io/github/stars/PKU-YuanGroup/Chat-UniVi.svg?style=social&label=Star)](https://github.com/PKU-YuanGroup/Chat-UniVi) [Chat-UniVi: Unified Visual Representation Empowers Large Language Models with Image and Video Understanding](https://arxiv.org/abs/2311.08046)
 [![Area](https://img.shields.io/badge/Video_LLM-purple)]() [![Type](https://img.shields.io/badge/Similarity--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Publish](https://img.shields.io/badge/CVPR-2024-blue)]() [![Star](https://img.shields.io/github/stars/rese1f/MovieChat.svg?style=social&label=Star)](https://github.com/rese1f/MovieChat) [MovieChat: From Dense Token to Sparse Memory for Long Video Understanding](https://arxiv.org/abs/2307.16449)
 [![Area](https://img.shields.io/badge/Video_LLM-purple)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Publish](https://img.shields.io/badge/ACL-2024-blue)]() [![Star](https://img.shields.io/github/stars/mbzuai-oryx/Video-ChatGPT.svg?style=social&label=Star)](https://github.com/mbzuai-oryx/Video-ChatGPT) [Video-ChatGPT: Towards Detailed Video Understanding via Large Vision and Language Models](https://arxiv.org/abs/2306.05424v2)
 [![Area](https://img.shields.io/badge/Video_LLM-purple)]() [![Type](https://img.shields.io/badge/Transformation--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2023\.06-red)]() [Video-LLaMA: An Instruction-tuned Audio-Visual Language Model for Video Understanding](https://arxiv.org/abs/2306.02858)
 [![Area](https://img.shields.io/badge/Audio_LLM-purple)]() [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Area](https://img.shields.io/badge/Video_LLM-purple)]() [![Type](https://img.shields.io/badge/Query--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()

---
## Audio LLM

### 2025

*  [![Arxiv](https://img.shields.io/badge/arXiv-2025\.03-red)]() [Qwen2.5-Omni Technical Report](https://arxiv.org/pdf/2503.20215)
 [![Area](https://img.shields.io/badge/Audio_LLM-purple)]() [![Type](https://img.shields.io/badge/Transformation--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2025\.03-red)]() [MMS-LLaMA: Efficient LLM-based Audio-Visual Speech Recognition with Minimal Multimodal Speech Tokens](https://arxiv.org/abs/2503.11315v1)
 [![Area](https://img.shields.io/badge/Audio_LLM-purple)]() [![Type](https://img.shields.io/badge/Query--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2025\.03-red)]() [Adaptive Audio-Visual Speech Recognition via Matryoshka-Based Multimodal LLMs](https://arxiv.org/abs/2503.06362)
 [![Area](https://img.shields.io/badge/Audio_LLM-purple)]() [![Type](https://img.shields.io/badge/Transformation--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2025\.02-red)]() [Baichuan-Audio: A Unified Framework for End-to-End Speech Interaction](https://arxiv.org/abs/2502.17239)
 [![Area](https://img.shields.io/badge/Audio_LLM-purple)]() [![Type](https://img.shields.io/badge/Transformation--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2025\.01-red)]() [OSUM: Advancing Open Speech Understanding Models with Limited Resources in Academia](https://arxiv.org/abs/2501.13306)
 [![Area](https://img.shields.io/badge/Audio_LLM-purple)]() [![Type](https://img.shields.io/badge/Transformation--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()

### 2024

*  [![Arxiv](https://img.shields.io/badge/arXiv-2024\.12-red)]() [Typhoon 2: A Family of Open Text and Multimodal Thai Large Language Models](https://arxiv.org/abs/2412.13702)
 [![Area](https://img.shields.io/badge/Audio_LLM-purple)]() [![Type](https://img.shields.io/badge/Query--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Publish](https://img.shields.io/badge/ICME-2025-blue)]() [SpeechPrune: Context-aware Token Pruning for Speech Information Retrieval](https://arxiv.org/abs/2412.12009)
 [![Area](https://img.shields.io/badge/Audio_LLM-purple)]() [![Type](https://img.shields.io/badge/Attention--Based-green)]() [![Type](https://img.shields.io/badge/Query--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Free-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2024\.09-red)]() [Large Language Models are Strong Audio-Visual Speech Recognition Learners](https://arxiv.org/abs/2409.12319)
 [![Area](https://img.shields.io/badge/Audio_LLM-purple)]() [![Type](https://img.shields.io/badge/Transformation--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2024\.09-red)]() [LLaMA-Omni: Seamless Speech Interaction with Large Language Models](https://arxiv.org/abs/2409.06666)
 [![Area](https://img.shields.io/badge/Audio_LLM-purple)]() [![Type](https://img.shields.io/badge/Transformation--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2024\.07-red)]() [Qwen2-Audio Technical Report](https://arxiv.org/pdf/2407.10759)
 [![Area](https://img.shields.io/badge/Audio_LLM-purple)]() [![Type](https://img.shields.io/badge/Transformation--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2024\.07-red)]() [![Star](https://img.shields.io/github/stars/QwenLM/Qwen2-Audio.svg?style=social&label=Star)](https://github.com/QwenLM/Qwen2-Audio) [Qwen2-Audio Technical Report](https://arxiv.org/abs/2407.10759)
 [![Area](https://img.shields.io/badge/Audio_LLM-purple)]() [![Type](https://img.shields.io/badge/Transformation--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Publish](https://img.shields.io/badge/ICML-2024-blue)]() [video-SALMONN: Speech-Enhanced Audio-Visual Large Language Models](https://arxiv.org/abs/2406.15704)
 [![Area](https://img.shields.io/badge/Audio_LLM-purple)]() [![Type](https://img.shields.io/badge/Query--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Publish](https://img.shields.io/badge/Interspeech-2024-blue)]() [Enhancing Automated Audio Captioning via Large Language Models with
Optimized Audio Encoding](https://arxiv.org/abs/2406.13275)
 [![Area](https://img.shields.io/badge/Audio_LLM-purple)]() [![Type](https://img.shields.io/badge/Query--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2024\.06-red)]() [![Star](https://img.shields.io/github/stars/DAMO-NLP-SG/VideoLLaMA2.svg?style=social&label=Star)](https://github.com/DAMO-NLP-SG/VideoLLaMA2) [VideoLLaMA 2: Advancing Spatial-Temporal Modeling and Audio Understanding in Video-LLMs](https://arxiv.org/abs/2406.07476)
 [![Area](https://img.shields.io/badge/Audio_LLM-purple)]() [![Area](https://img.shields.io/badge/Video_LLM-purple)]() [![Type](https://img.shields.io/badge/Transformation--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Publish](https://img.shields.io/badge/Interspeech-2024-blue)]() [Improving Audio Codec-based Zero-Shot Text-to-Speech Synthesis with Multi-Modal Context and Large Language Model](https://arxiv.org/abs/2406.03706)
 [![Area](https://img.shields.io/badge/Audio_LLM-purple)]() [![Type](https://img.shields.io/badge/Query--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2024\.05-red)]() [SpeechVerse: A Large-scale Generalizable Audio Language Model](https://arxiv.org/abs/2405.08295)
 [![Area](https://img.shields.io/badge/Audio_LLM-purple)]() [![Type](https://img.shields.io/badge/Transformation--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2024\.05-red)]() [SpeechVerse: A Large-scale Generalizable Audio Language Model](https://arxiv.org/abs/2405.08295)
 [![Area](https://img.shields.io/badge/Audio_LLM-purple)]() [![Type](https://img.shields.io/badge/Transformation--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2024\.02-red)]() [An Embarrassingly Simple Approach for LLM with Strong ASR Capacity](https://arxiv.org/abs/2402.08846)
 [![Area](https://img.shields.io/badge/Audio_LLM-purple)]() [![Type](https://img.shields.io/badge/Transformation--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()

### 2023

*  [![Publish](https://img.shields.io/badge/ICLR-2024-blue)]() [SALMONN: Towards Generic Hearing Abilities for Large Language Models](https://arxiv.org/abs/2310.13289)
 [![Area](https://img.shields.io/badge/Audio_LLM-purple)]() [![Type](https://img.shields.io/badge/Query--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2023\.09-red)]() [Connecting Speech Encoder and Large Language Model for ASR](https://arxiv.org/abs/2309.13963)
 [![Area](https://img.shields.io/badge/Audio_LLM-purple)]() [![Type](https://img.shields.io/badge/Query--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Publish](https://img.shields.io/badge/ICASSP-2024-blue)]() [Prompting Large Language Models with Speech Recognition Abilities](https://arxiv.org/pdf/2307.11795)
 [![Area](https://img.shields.io/badge/Audio_LLM-purple)]() [![Type](https://img.shields.io/badge/Transformation--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()
*  [![Arxiv](https://img.shields.io/badge/arXiv-2023\.06-red)]() [Video-LLaMA: An Instruction-tuned Audio-Visual Language Model for Video Understanding](https://arxiv.org/abs/2306.02858)
 [![Area](https://img.shields.io/badge/Audio_LLM-purple)]() [![Area](https://img.shields.io/badge/Image_LLM-purple)]() [![Area](https://img.shields.io/badge/Video_LLM-purple)]() [![Type](https://img.shields.io/badge/Query--Based-green)]() [![Cost](https://img.shields.io/badge/Training--Based-yellow)]()

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

This repository is inspired by [Awesome-Efficient-Reasoning-Models](https://github.com/fscdc/Awesome-Efficient-Reasoning-Models), [Awesome-Efficient-LLM](https://github.com/horseee/Awesome-Efficient-LLM/), [Awesome-Context-Engineering](https://github.com/Meirtz/Awesome-Context-Engineering)

## 🧑‍💻 Contributors

👏 Thanks to these contributors for this excellent work！

<a href="https://github.com/cokeshao/Awesome-Multimodal-Token-Compression/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=cokeshao/Awesome-Multimodal-Token-Compression" />
</a>
