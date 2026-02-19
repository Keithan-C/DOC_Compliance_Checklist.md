---
layout: default
title: Article 12 – Record-Keeping & Logging
---

# Article 12 – Record-Keeping & Logging

## Core Engineering Requirement

High-risk AI systems must generate logs that allow:

- Decision reconstruction
- Model version traceability
- Data lineage tracking
- Human oversight verification

---

## Logging Architecture Model

```mermaid
flowchart LR
    Input[Sensor Input] --> Model[AI Model]
    Model --> Decision[System Output]
    Model --> VersionLog[Model Version Log]
    Input --> DataLog[Data Lineage Log]
    Decision --> DecisionLog[Decision Log]
    Oversight[Human Oversight] --> OverrideLog[Override Log]

    VersionLog --> Storage[Secure Log Storage]
    DataLog --> Storage
    DecisionLog --> Storage
    OverrideLog --> Storage
