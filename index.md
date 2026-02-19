<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LXD Advisory | Automotive AI Compliance</title>
    <style>
        /* Reset & Base */
        body, h1, h2, h3, p, ul, li, a {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }
        body {
            background-color: #0f111a;
            color: #e0e0e0;
            line-height: 1.6;
        }
        a {
            color: #00d9ff;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }

        /* Container */
        .container {
            width: 90%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px 0;
        }

        /* Hero Section */
        .hero {
            text-align: center;
            padding: 80px 20px;
            background: linear-gradient(135deg, #0f111a 0%, #1a1c2c 100%);
        }
        .hero h1 {
            font-size: 3rem;
            color: #00d9ff;
            margin-bottom: 1rem;
        }
        .hero p {
            font-size: 1.3rem;
            color: #a8b3cc;
            margin-bottom: 2rem;
        }
        .hero .cta-btn {
            background-color: #00d9ff;
            color: #fff;
            padding: 14px 28px;
            border-radius: 6px;
            font-weight: bold;
            transition: 0.3s;
        }
        .hero .cta-btn:hover {
            background-color: #fff;
            color: #0066ff;
        }

        /* Sections */
        section {
            padding: 60px 0;
        }
        h2 {
            font-size: 2.2rem;
            color: #00d9ff;
            margin-bottom: 1rem;
            text-align: center;
        }
        p {
            max-width: 800px;
            margin: 0 auto 1.5rem auto;
            text-align: center;
            font-size: 1.1rem;
        }

        /* Services */
        .services {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 30px;
            margin-top: 40px;
        }
        .service-card {
            background-color: #1a1c2c;
            padding: 20px;
            border-radius: 10px;
            width: 280px;
            text-align: left;
            transition: 0.3s;
        }
        .service-card:hover {
            background-color: #22253b;
        }
        .service-card h3 {
            color: #00d9ff;
            margin-bottom: 10px;
        }
        .service-card p {
            color: #a8b3cc;
        }

        /* Resources */
        .resources {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 20px;
            margin-top: 30px;
        }
        .resource-card {
            background-color: #1a1c2c;
            padding: 16px;
            border-radius: 8px;
            width: 260px;
            text-align: center;
            transition: 0.3s;
        }
        .resource-card:hover {
            background-color: #22253b;
        }
        .resource-card a {
            display: inline-block;
            margin-top: 1rem;
            padding: 8px 16px;
            background-color: #00d9ff;
            color: #fff;
            border-radius: 6px;
            font-weight: bold;
            transition: 0.3s;
        }
        .resource-card a:hover {
            background-color: #fff;
            color: #0066ff;
        }

        /* Footer */
        footer {
            text-align: center;
            padding: 40px 20px;
            background-color: #0f111a;
            border-top: 1px solid #22253b;
        }
        footer a {
            font-weight: bold;
        }

        /* Responsive */
        @media (max-width: 768px) {
            .services, .resources {
                flex-direction: column;
                align-items: center;
            }
            .service-card, .resource-card {
                width: 90%;
            }
        }
    </style>
</head>
