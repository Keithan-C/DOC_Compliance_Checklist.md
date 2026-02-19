```mermaid
%% Compliance Paradox Flow — UX-friendly

flowchart TD
    %% Nodes
    Legal[Legal Interpretation]:::legal
    Engineering[Engineering Implementation]:::engineering
    Training[Literacy & Defensibility]:::training
    Audit[Regulatory Audit]:::audit

    LegalSilo[Legal Silo]:::silo
    EngSilo[Engineering Silo]:::silo
    PassiveTraining[Passive Training]:::silo
    Exposure[Audit Exposure]:::exposure

    %% Main flow
    Legal --> Engineering --> Training --> Audit

    %% Failure points
    LegalSilo --> Exposure
    EngSilo --> Exposure
    PassiveTraining --> Exposure

    %% Styling
    classDef legal fill:#00d9ff,stroke:#0066ff,stroke-width:2px,color:#fff
    classDef engineering fill:#0066ff,stroke:#003399,stroke-width:2px,color:#fff
    classDef training fill:#00ff99,stroke:#009966,stroke-width:2px,color:#000
    classDef audit fill:#ff9900,stroke:#cc6600,stroke-width:2px,color:#000,font-weight:bold
    classDef silo fill:#ff6666,stroke:#cc0000,stroke-width:2px,color:#fff
    classDef exposure f
