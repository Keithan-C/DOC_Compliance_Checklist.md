---
layout: default
title: System Diagrams
---

# System Alignment Model

```mermaid
flowchart TD
    Legal[Legal Interpretation]
    Engineering[Engineering Implementation]
    Training[Literacy & Defensibility]
    Audit[Regulatory Audit]

    Legal --> Engineering
    Engineering --> Training
    Training --> Audit

flowchart TD
    LegalSilo[Legal Silo]
    EngSilo[Engineering Silo]
    PassiveTraining[Passive Training]
    Exposure[Audit Exposure]

    LegalSilo --> Exposure
    EngSilo --> Exposure
    PassiveTraining --> Exposure




---

