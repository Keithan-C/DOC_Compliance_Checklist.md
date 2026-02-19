<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>EU AI Act Engineering Compliance Hub</title>

<style>
body {
    margin: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    background-color: #0f172a;
    color: #e2e8f0;
    line-height: 1.6;
}

/* Top Navigation */
nav {
    background: #0b1220;
    padding: 1rem 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: sticky;
    top: 0;
}

nav h1 {
    font-size: 1rem;
    color: #38bdf8;
    margin: 0;
}

nav a {
    color: #94a3b8;
    text-decoration: none;
    margin-left: 20px;
    font-size: 0.9rem;
}

nav a:hover {
    color: #38bdf8;
}

/* Hero Section */
.hero {
    padding: 80px 20px;
    text-align: center;
    background: linear-gradient(135deg, #0f172a, #1e293b);
}

.hero h2 {
    font-size: 2.5rem;
    margin-bottom: 20px;
}

.hero p {
    max-width: 700px;
    margin: auto;
    font-size: 1.1rem;
    color: #cbd5e1;
}

.deadline {
    margin-top: 20px;
    font-weight: bold;
    color: #38bdf8;
}

/* Section Styling */
section {
    padding: 60px 20px;
    max-width: 1000px;
    margin: auto;
}

section h3 {
    font-size: 1.8rem;
    margin-bottom: 20px;
    color: #38bdf8;
}

.card {
    background: #1e293b;
    padding: 25px;
    border-radius: 10px;
    margin-bottom: 25px;
}

ul {
    padding-left: 20px;
}

.highlight {
    background: #1e293b;
    padding: 20px;
    border-left: 4px solid #38bdf8;
    margin: 20px 0;
}

footer {
    text-align: center;
    padding: 40px 20px;
    background: #0b1220;
    font-size: 0.9rem;
    color: #94a3b8;
}
</style>
</head>

<body>

<nav>
    <h1>EU AI Act Compliance Hub</h1>
    <div>
        <a href="#article12">Article 12</a>
        <a href="#article19">Article 19</a>
        <a href="#audit">Audit Readiness</a>
        <a href="#checklist">Checklist</a>
    </div>
</nav>

<div class="hero">
    <h2>Engineering Interpretation of EU AI Act Articles 12 & 19</h2>
    <p>
        A structured compliance reference for Automotive & ADAS teams building
        high-risk AI systems.
    </p>
    <div class="deadline">
        Enforcement Milestone: August 2, 2026
    </div>
</div>

<section id="article12">
    <h3>Article 12 — Record-Keeping & Logging</h3>

    <div class="card">
        <h4>Core Engineering Requirement</h4>
        <p>High-risk AI systems must generate logs that enable:</p>
        <ul>
            <li>Decision reconstruction</li>
            <li>Model version traceability</li>
            <li>Data lineage tracking</li>
            <li>Human oversight verification</li>
        </ul>
    </div>

    <div class="highlight">
        A technically brilliant system without structured logging is audit-exposed.
    </div>

    <div class="card">
        <h4>Minimum Logging Layers</h4>
        <ul>
            <li>Model Version ID & Deployment Timestamp</li>
            <li>Input Data Reference & Processing Pipeline</li>
            <li>Decision Output & Confidence Score</li>
            <li>Override & Escalation Logging</li>
        </ul>
    </div>
</section>

<section id="article19">
    <h3>Article 19 — Technical Documentation</h3>

    <div class="card">
        <h4>Pre-Market Documentation Requirements</h4>
        <ul>
            <li>System Architecture Description</li>
            <li>Intended Purpose Definition</li>
            <li>Risk Management Framework</li>
            <li>Data Governance Process</li>
            <li>Human Oversight Mechanisms</li>
            <li>Post-Market Monitoring Plan</li>
        </ul>
    </div>

    <div class="highlight">
        Documentation must mirror real engineering implementation — not abstract policy.
    </div>
</section>

<section id="audit">
    <h3>Audit Readiness Framework</h3>

    <div class="card">
        <h4>What Regulators Will Do</h4>
        <ol>
            <li>Review technical documentation</li>
            <li>Inspect logging systems</li>
            <li>Interview R&D leads</li>
        </ol>
    </div>

    <div class="card">
        <h4>Engineering Stress Test Questions</h4>
        <ul>
            <li>How do you reconstruct a decision event?</li>
            <li>Where is model versioning documented?</li>
            <li>How is automation bias mitigated?</li>
            <li>What happens during an override conflict?</li>
        </ul>
    </div>
</section>

<section id="checklist">
    <h3>Engineering Readiness Checklist</h3>

    <div class="card">
        <h4>Article 12</h4>
        <ul>
            <li>Defined logging schema</li>
            <li>Model version traceability</li>
            <li>Retention policy documented</li>
            <li>Retrieval interface tested</li>
        </ul>
    </div>

    <div class="card">
        <h4>Article 19</h4>
        <ul>
            <li>Architecture diagram aligned with implementation</li>
            <li>Risk mapping per system component</li>
            <li>Oversight controls documented</li>
            <li>Post-market monitoring defined</li>
        </ul>
    </div>
</section>

<footer>
    © 2026 EU AI Act Engineering Compliance Hub  
    Built for Automotive & ADAS Engineering Teams
</footer>

</body>
</html>
