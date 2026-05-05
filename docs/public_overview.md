# Public Overview

This page summarizes the public-safe research direction behind **GenAI4Dresilience**. It is intentionally high level because the related manuscript is still under development.

## Research Motivation

Disaster resilience work spans mitigation, preparedness, response, and recovery. Existing geospatial AI methods often focus on one phase or one data modality. GenAI creates a useful bridge because it can combine scenario generation, multimodal perception, reasoning, and collaborative decision support.

The goal is not to replace physical hazard models, field expertise, or emergency management procedures. The goal is to make heterogeneous evidence easier to synthesize and easier to connect to decisions.

## Core Public Ideas

### 1. Lifecycle-Oriented GenAI

GenAI can be mapped to different tasks across the disaster lifecycle:

- mitigation: scenario reasoning and vulnerability reduction
- preparedness: monitoring, early warning, and anticipatory planning
- response: damage assessment and emergency coordination
- recovery: adaptation, trade-off analysis, and long-term resilience building

This framing avoids treating GenAI as a single-purpose model. It instead treats GenAI as a capability layer that can support different tasks under different temporal pressures.

### 2. Dataset-Specific Evidence Branches

The hurricane case study uses two public-safe evidence settings:

- cross-view evidence, where post-disaster street-view imagery and post-disaster remote sensing imagery describe matched locations
- bi-temporal evidence, where pre- and post-disaster street-view imagery show local change over time

These two branches motivate different reasoning patterns. Cross-view analysis focuses on scale and viewpoint alignment. Bi-temporal analysis focuses on visual change and temporal comparison.

### 3. Evidence-to-Decision Workflow

The public workflow has three conceptual stages:

1. Selectively restore degraded imagery only when restoration is needed.
2. Recognize visible damage indicators and damage severity from dataset-specific evidence.
3. Convert visual evidence into structured explanations and decision-support summaries with human review.

The details of thresholds, prompts, intermediate outputs, evaluation scores, and generated reports are withheld while the manuscript is unpublished.

### 4. Responsible GenAI for Disaster Resilience

Disaster applications are high-stakes. A public repository should therefore emphasize responsible release. The central concerns include:

- hallucination and overconfident model outputs
- uncertainty communication
- data bias and uneven geographic coverage
- privacy and sensitive disaster imagery
- human oversight in emergency decisions
- unequal access to large model infrastructure

## What Is Public Here

This repository currently provides:

- a high-level lifecycle framework
- a publication-safe conceptual workflow
- a lightweight hurricane location visualization script
- links to related public research repositories

## What Is Withheld for Now

To protect the manuscript and avoid premature disclosure, this repository does not currently release:

- unpublished experimental figures
- raw or processed case-study imagery
- quantitative evaluation tables
- full prompt templates
- model-generated disaster reports
- complete experimental code for reproducing unpublished findings

These materials can be added after the manuscript reaches an appropriate release stage.
