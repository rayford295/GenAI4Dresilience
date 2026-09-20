<div align="center">

# Generative AI for Disaster Resilience

**A lifecycle framework for GenAI across mitigation, preparedness, response, and recovery,
with a hurricane damage-assessment case study on Florida street-view and satellite imagery.**

[**🌐 Project website**](https://rayford295.github.io/GenAI4Dresilience/) · [Framework](./docs/lifecycle_framework.md) · [Case study](./docs/case_study.md) · [Challenges](./docs/challenges_and_outlook.md) · [References](./docs/references.md) · [中文导读](./README_zh.md)

<img src="./figure/fig1_lifecycle_framework.png" alt="Lifecycle framework" width="820">

</div>

---

Book chapter submitted to **_Geography in the Age of Generative AI: Innovations in Mapping, Analysis & Geospatial Applications_** (CRC Press / Taylor & Francis Group), co-edited by Gengchen Mai (UT Austin), Xiao Huang (Emory), Devika Jain (Harvard), and Dalton Lunga (ORNL).

**Authors:** [Yifan Yang](https://orcid.org/0009-0009-9496-6925), [Lei Zou](https://orcid.org/0000-0001-6206-3558), [Hao Tian](https://orcid.org/0009-0003-4564-8185), [Bing Zhou](https://orcid.org/0000-0003-1106-1370), [Joynal Abedin](https://orcid.org/0000-0001-6203-0959), [Zongrong Li](https://orcid.org/0009-0008-0933-6439), [Zhengzhong Tu](https://orcid.org/0000-0002-7594-2292)

## What is in the chapter

- **Lifecycle framework.** GenAI as a cross-cutting layer combining generation, multimodal understanding, reasoning, and multi-agent collaboration, with phase-specific tasks, products, and safeguards. → [docs/lifecycle_framework.md](./docs/lifecycle_framework.md)
- **Case study.** Hurricane Ian 2022 (300 cross-view street-view + satellite pairs) and Hurricane Milton 2024 (300 bi-temporal street-view pairs). Three stages: selective image restoration, GenAI-assisted damage recognition, reasoning and report generation. → [docs/case_study.md](./docs/case_study.md)
- **Challenges.** Responsibility, autonomy, and equity as complementary directions. → [docs/challenges_and_outlook.md](./docs/challenges_and_outlook.md)

## Key results

| Task | Cross-view (Ian) | Bi-temporal (Milton) |
|---|---|---|
| Image restoration, quality score Q | satellite 0.62 → 0.73 · SVI 0.75 → 0.79 | SVI 0.76 → 0.79 |
| Severity classification (best model) | Gemini-3-Pro, acc 0.627, NCSE 0.190 | GPT-5.1, acc 0.591, NCSE 0.218 |
| Indicator recognition (best F1) | Gemini-3-Pro, 0.774 | GPT-5.1, 0.553 |
| Report reasoning (0–5) | factual and plausibility > 4.0; actionability 2.0–2.8 | same pattern, lower completeness |

Full tables as CSV in [results/](./results/); all chapter figures in [figure/](./figure/).

## Repository layout

```text
index.html      project website (GitHub Pages)
docs/           chapter text: framework, case study, challenges, references
figure/         Figures 1–6
results/        Tables 1–5 as CSV
code/map.py     Hurricane Ian / Milton location map
CITATION.cff
```

Prompts, raw model outputs, and pipeline code will be released after publication. Source imagery follows the CVDisaster and BiTemporal dataset licenses.

## Citation

```bibtex
@incollection{yang2026genai4dresilience,
  title     = {Generative AI for Disaster Resilience},
  author    = {Yang, Yifan and Zou, Lei and Tian, Hao and Zhou, Bing and Abedin, Joynal and Li, Zongrong and Tu, Zhengzhong},
  booktitle = {Geography in the Age of Generative AI: Innovations in Mapping, Analysis \& Geospatial Applications},
  editor    = {Mai, Gengchen and Huang, Xiao and Jain, Devika and Lunga, Dalton},
  publisher = {CRC Press / Taylor \& Francis Group},
  year      = {2026},
  note      = {Submitted}
}
```

## Related

[disaster-crossview-datasets](https://github.com/Rayford-AI/disaster-crossview-datasets) · [Agent4Disaster](https://github.com/rayford295/Agent4Disaster) · [Sat2Street-DisasterGen](https://github.com/rayford295/Sat2Street-DisasterGen) · [DamageArbiter](https://github.com/rayford295/DamageArbiter) · [Bi-Temporal-StreetView](https://github.com/rayford295/Bi-Temporal-StreetView) · [DisasterVLP](https://github.com/rayford295/DisasterVLP)

**Contact:** Yifan Yang, Texas A&M University · yyang295@tamu.edu · [@rayford295](https://github.com/rayford295)
