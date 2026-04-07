# 🌍 GenAI4Dresilience
**Generative AI for Disaster Resilience**

[中文版](./README_zh.md)

---

## Overview

**GenAI4Dresilience** explores how **Generative AI (GenAI)** can be integrated into disaster resilience workflows — spanning preparedness, response, and recovery phases. This repository provides conceptual frameworks, case studies, and code demonstrations centered on geospatial applications of large language models, diffusion models, and multimodal AI in disaster contexts.

---

## 🧠 Framework

The proposed framework conceptualizes how **Generative AI integrates into disaster resilience tasks** across the disaster lifecycle:

![GenAI4DisasterResilience Framework](https://github.com/rayford295/GenAI4Dresilience/blob/main/figure/framework.png)

---

## 📁 Repository Structure

```
GenAI4Dresilience/
├── figure/          # Framework diagrams and visualizations
│   └── framework.png
├── code/            # Demo scripts and case studies
│   └── map.py       # Hurricane track visualization (Milton & Ian, Florida)
└── README.md
```

---

## 🌀 Case Study: Hurricane Track Visualization

`code/map.py` generates a geospatial visualization of hurricane tracks for **Hurricane Milton** and **Hurricane Ian** over the Florida region using `matplotlib` and `cartopy`.

**Dependencies:**
```bash
pip install matplotlib cartopy
```

**Run:**
```bash
python code/map.py
```

---

## 🔗 Related Projects

| Project | Description |
|---|---|
| [Agent4Disaster](https://github.com/rayford295/Agent4Disaster) | Multi-agent GeoAI pipeline for disaster perception and reasoning |
| [Sat2Street-DisasterGen](https://github.com/rayford295/Sat2Street-DisasterGen) | Satellite-to-street-view synthesis for post-disaster assessment |
| [DamageArbiter](https://github.com/rayford295/DamageArbiter) | CLIP-enhanced multimodal hurricane damage assessment |
| [Bi-Temporal-StreetView](https://github.com/rayford295/Bi-Temporal-StreetView) | Hyperlocal damage assessment via bi-temporal street-view imagery |
| [DisasterVLP](https://github.com/rayford295/DisasterVLP) | Visual-language models for multidimensional disaster damage perception |

---

## 📬 Contact

**Yifan Yang** — Texas A&M University
- GitHub: [@rayford295](https://github.com/rayford295)
- Email: yyang295@tamu.edu
