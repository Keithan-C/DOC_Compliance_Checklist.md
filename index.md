<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>EU AI Act Compliance Reference — Articles 12 & 19</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
/* Global Reset */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Inter', sans-serif;
    background-color: #f7f8fa;
    color: #333;
    line-height: 1.7;
}

/* Navigation */
nav {
    background: #0a243b;
    padding: 12px 24px;
    position: sticky;
    top: 0;
    z-index: 100;
}

nav .logo {
    font-size: 1.5rem;
    font-weight: 700;
    color: #ffffff;
}

nav .menu {
    float: right;
}

nav .menu a {
    color: #cbd5e1;
    margin-left: 20px;
    text-decoration: none;
    font-weight: 500;
}

nav .menu a:hover {
    color: #38bdf8;
}

/* Hero Section */
.hero {
    background: linear-gradient(135deg, #38bdf8 0%, #0a243b 100%);
    padding: 60px 20px 80px 20px;
    text-align: center;
    color: #fff;
}

.hero h1 {
    font-size: 2.8rem;
    margin-bottom: 12px;
}

.hero p {
    font-size: 1.1rem;
    margin-bottom: 16px;
}

.hero .deadline {
    font-size: 1rem;
    font-weight: 600;
    color: #e5f4ff;
}

/* Sections */
section {
    padding: 60px 20px;
}

section h2 {
    font-size: 2rem;
    margin-bottom: 18px;
    color: #0a243b;
    text-align: center;
}

.section-content {
    max-width: 900px;
    margin: auto;
}

/* Cards */
.card {
    background: #ffffff;
    border-radius: 8px;
    padding: 20px;
    margin-bottom: 24px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
}

.card h3 {
    font-size: 1.4rem;
    color: #0a243b;
    margin-bottom: 12px;
}

.card p, .card ul {
    color: #444;
}

.card ul {
    margin-top: 10px;
    padding-left: 18px;
}

.card li {
    margin-bottom: 8px;
}

/* Highlight */
.highlight {
    background: #ffffff;
    border-left: 4px solid #38bdf8;
    padding: 18px;
    margin: 24px auto;
    box-shadow: 0 3px 12px rgba(0,0,0,0.05);
    max-width: 900px;
}

/* Footer */
footer {
    background: #0a243b;
    color: #cbd5e1;
    text-align: center;
    padding: 28px 20px;
    font-size: 0.9rem;
}

/* Mobile */
@media (max-width: 768px) {
    nav .menu a {
        margin-left: 12px;
        font-size: 0.9rem;
    }
}
</style>

</head>

<body>

<!-- Navigation -->
<nav>
    <span class="logo">Compliance Reference</span>
    <span class="menu">
        <a href="#article12">Article 12</a>
        <a href="#article19">Article 19</a>
        <a href="#audit">Audit Readiness</a>
        <a href="#checklist">Checklist</a>
    </span>
</nav>

<!-- Hero -->
<section class="hero">
    <h1>EU AI Act Articles 12 & 19 — Engineering Compliance</h1>
    <p>Reference and readiness guide for automotive & ADAS teams building high-risk AI systems.</p>
    <p class="deadline">Enforcement Deadline: <strong>August 2, 2026</strong></p>
</section>

<!-- Article 12 -->
<section id="article12">
    <h2>Article 12 — Record-Keeping & Logging</h2>
    <div class="section-content">

        <div class="card">
            <h3>Core Engineering Requirement</h3>
            <p>High-risk AI systems must generate logs that enable:</p>
            <ul>
                <li>Decision reconstruction</li>
                <li>Model version traceability</li>
                <li>Data lineage tracking</li>
                <li>Human oversight verification</li>
            </ul>
        </div>

        <div class="highlight">
            Technically brilliant systems without structured logging are audit-exposed.
        </div>

        <div class="card">
            <h3>Minimum Logging Layers</h3>
            <ul>
                <li>Model Version IDs & Timestamps</li>
                <li>Input Data Lineage</li>
                <li>Decision Output & Confidence</li>
                <li>Override & Escalation Logs</li>
            </ul>
        </div>

    </div>
</section>

<!-- Article 19 -->
<section id="article19">
    <h2>Article 19 — Technical Documentation</h2>
    <div class="section-content">

        <div class="card">
            <h3>Pre-Market Documentation Requirements</h3>
            <ul>
                <li>System Architecture Description</li>
                <li>Intended Purpose Definition</li>
                <li>Risk Management Design</li>
                <li>Data Governance Processes</li>
                <li>Human Oversight Mechanisms</li>
                <li>Post-Market Monitoring Plans</li>
            </ul>
        </div>

        <div class="highlight">
            Documentation must reflect actual implementation — not abstract policy.
        </div>

    </div>
</section>

<!-- Audit -->
<section id="audit">
    <h2>Audit Readiness</h2>
    <div class="section-content">

        <div class="card">
            <h3>Regulatory Inspection Expectations</h3>
            <ul>
                <li>Review of technical documentation</li>
                <li>Inspection of logging systems</li>
                <li>Interviews with R&D leads</li>
            </ul>
        </div>

        <div class="card">
            <h3>Engineering Stress Test Questions</h3>
            <ul>
                <li>How do you reconstruct a decision event?</li>
                <li>Where is model version logging defined?</li>
                <li>How do you mitigate automation bias?</li>
                <li>How do you handle override conflicts?</li>
            </ul>
        </div>

    </div>
</section>

<!-- Checklist -->
<section id="checklist">
    <h2>Engineering Readiness Checklist</h2>
    <div class="section-content">

        <div class="card">
            <h3>Article 12 Checklist</h3>
            <ul>
                <li>Logging schema defined</li>
                <li>Version traceability implemented</li>
                <li>Retention policy documented</li>
                <li>Retrieval interface tested</li>
            </ul>
        </div>

        <div class="card">
            <h3>Article 19 Checklist</h3>
            <ul>
                <li>Architecture doc mirrors implementation</li>
                <li>Risk mapping aligned to components</li>
                <li>Oversight controls documented</li>
                <li>Monitoring defined and documented</li>
            </ul>
        </div>

    </div>
</section>

<!-- Footer -->
<footer>
    © 2026 EU AI Act Compliance Hub — Built for Automotive & ADAS Engineering Teams
</footer>

</body>
</html>
