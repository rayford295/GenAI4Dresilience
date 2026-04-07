# 🌍 GenAI4Dresilience
**生成式人工智能用于灾害韧性**

[English Version](./README.md)

---

## 项目简介

**GenAI4Dresilience** 探索**生成式人工智能（GenAI）**如何融入灾害韧性工作流，涵盖灾前准备、灾中响应与灾后恢复三个阶段。本仓库提供概念框架、案例研究与代码演示，聚焦于大语言模型、扩散模型及多模态 AI 在灾害场景中的地理空间应用。

---

## 🧠 框架

下图展示了**生成式 AI 如何在灾害生命周期各阶段融入灾害韧性任务**：

![GenAI4DisasterResilience 框架](https://github.com/rayford295/GenAI4Dresilience/blob/main/figure/framework.png)

---

## 📁 仓库结构

```
GenAI4Dresilience/
├── figure/          # 框架图与可视化结果
│   └── framework.png
├── code/            # 演示脚本与案例研究
│   └── map.py       # 飓风路径可视化（Milton 与 Ian，佛罗里达）
└── README.md
```

---

## 🌀 案例：飓风路径可视化

`code/map.py` 利用 `matplotlib` 和 `cartopy`，生成**飓风 Milton** 与**飓风 Ian** 在佛罗里达地区路径的地理空间可视化图。

**依赖安装：**
```bash
pip install matplotlib cartopy
```

**运行：**
```bash
python code/map.py
```

---

## 🔗 相关项目

| 项目 | 描述 |
|---|---|
| [Agent4Disaster](https://github.com/rayford295/Agent4Disaster) | 多智能体 GeoAI 灾害感知与推理流水线 |
| [Sat2Street-DisasterGen](https://github.com/rayford295/Sat2Street-DisasterGen) | 卫星图像合成街景用于灾后评估 |
| [DamageArbiter](https://github.com/rayford295/DamageArbiter) | 基于 CLIP 的多模态飓风损害评估框架 |
| [Bi-Temporal-StreetView](https://github.com/rayford295/Bi-Temporal-StreetView) | 双时相街景图像灾害损失超精细评估 |
| [DisasterVLP](https://github.com/rayford295/DisasterVLP) | 视觉语言模型用于多维度灾害损失感知 |

---

## 📬 联系方式

**杨一帆（Yifan Yang）** — 德克萨斯农工大学
- GitHub: [@rayford295](https://github.com/rayford295)
- 邮箱: yyang295@tamu.edu
