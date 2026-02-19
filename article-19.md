
---

# 4️⃣ `article-19.md`

```markdown
---
layout: default
title: Article 19 – Technical Documentation
---

# Article 19 – Technical Documentation

## Pre-Market Documentation Requirements

- System architecture description
- Intended purpose definition
- Risk management framework
- Data governance process
- Human oversight mechanisms
- Post-market monitoring design

---

## Documentation Structure

```mermaid
flowchart TD
    Purpose[Intended Purpose]
    Architecture[System Architecture]
    Risk[Risk Management]
    Data[Data Governance]
    Oversight[Human Oversight]
    Monitoring[Post-Market Monitoring]

    Purpose --> Architecture
    Architecture --> Risk
    Risk --> Data


---

# 6️⃣ `engineering-checklists.md`

```markdown
---
layout: default
title: Engineering Checklists
---

# Engineering Readiness Checklists

## Article 12

- [ ] Logging schema defined
- [ ] Model version traceability
- [ ] Data lineage mapping
- [ ] Override logging implemented
- [ ] Retention policy documented
- [ ] Retrieval interface tested

---

## Article 19

- [ ] Architecture diagram aligned with implementation
- [ ] Risk mapping per component
- [ ] Oversight documentation validated
- [ ] Update governance defined
- [ ] Post-market monitoring documented

    Risk --> Oversight
    Oversight --> Monitoring
