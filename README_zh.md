# GenAI4Dresilience（中文导读）

> 本文件仅为中文阅读辅助，[英文 README](./README.md) 为权威版本。

**生成式人工智能用于灾害韧性** —— 书章 *Generative AI for Disaster Resilience* 的配套仓库。该章已投稿至 **Geography in the Age of Generative AI: Innovations in Mapping, Analysis & Geospatial Applications**（CRC Press / Taylor & Francis），主编：Gengchen Mai（UT Austin）、Xiao Huang（Emory）、Devika Jain（Harvard）、Dalton Lunga（ORNL）。

作者：Yifan Yang、Lei Zou、Hao Tian、Bing Zhou、Joynal Abedin、Zongrong Li、Zhengzhong Tu。

## 内容概览

1. **生命周期框架**（Figure 1）：把 GenAI 的生成、多模态理解、推理、多智能体协同四类能力，映射到减灾、备灾、响应、恢复四个阶段，并为每个阶段给出任务、产出与安全边界。详见 [docs/lifecycle_framework.md](./docs/lifecycle_framework.md)。
2. **案例研究**：以 2022 年飓风 Ian（跨视角：灾后街景 + 遥感，300 对）和 2024 年飓风 Milton（双时相：灾前/灾后街景，300 对）为例，构建三阶段流程（Figure 3）：
   - 选择性图像修复：Q = 0.4C + 0.4S + 0.2N；卫星影像 0.62→0.73，街景 0.75→0.79。
   - GenAI 辅助损害识别：Gemini-3-Pro 在跨视角数据上最好（准确率 0.627，NCSE 0.190）；GPT-5.1 在双时相数据上最好（准确率 0.591，NCSE 0.218）。
   - 推理与决策支持：事实一致性与因果合理性普遍 >4.0，但可执行性仅 2.0–2.8，是当前主要短板。
   详见 [docs/case_study.md](./docs/case_study.md)，表格 CSV 在 [results/](./results/)。
3. **挑战与展望**：责任（Responsibility）、自主（Autonomy）、公平（Equity）三个维度。详见 [docs/challenges_and_outlook.md](./docs/challenges_and_outlook.md)。

## 目录

- `docs/` 章节正文（框架、案例、挑战、参考文献）
- `figure/` Figure 1–6
- `results/` Table 1–5 的 CSV
- `code/map.py` 飓风位置示意图脚本
- `CITATION.cff` 引用信息

提示词、原始模型输出和完整流程代码将在章节正式出版后补充。
