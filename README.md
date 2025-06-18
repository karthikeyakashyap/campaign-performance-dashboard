📊 Live Campaign Performance Dashboard with Automated Insights
TL;DR
End-to-end, near-real-time marketing analytics pipeline powered by Python, PostgreSQL, and Power BI, featuring automated anomaly detection and production-ready Docker orchestration.

🚀 Project Overview
Marketing teams often spend hours manually exporting CSVs, eyeballing performance charts, and reacting late to performance drops. This project eliminates that bottleneck.

It ingests live campaign data, processes KPIs (like CTR, CPA), detects anomalies using statistical logic, and presents actionable insights in interactive Power BI dashboards—all automatically and ready to scale.

🧱 Architecture Breakdown
Layer	Tech Stack	Purpose
Ingestion	Python (pandas) + cron / Task Scheduler	Simulates or pulls live campaign data → saves to /data/
Storage	PostgreSQL (campaign_metrics table)	Durable relational store, optimized for BI queries
Processing	Python (detect_anomalies.py)	Adds derived fields: ctr, is_anomaly using z-score logic
Visualization	Power BI Desktop / Power BI Service	Live dashboards with drill-downs, alerts, and KPI cards
Containerization	Docker + Docker Compose	Spin up the full pipeline with a single command for local development

🔍 Key Feature: Automated Anomaly Detection
Every data refresh runs a lightweight Python script that flags anomalies based on CTR deviation:

Anomaly = CTR < mean(CTR) - 2 * std(CTR)
Flagged rows are immediately visible in Power BI with color-coded highlights (e.g., red for underperformance), helping marketing teams catch and react to issues in real time.

🧠 Key Metrics Tracked
Impressions

Clicks

CTR (Click-Through Rate)

Cost

CPA (Cost per Acquisition)

Conversion Rate

Anomaly Flags

📈 Power BI Visualizations
Built with clarity, actionability, and professional design in mind:

Visual Type	What It Shows
KPI Cards	CTR, CPA, Cost with red/green thresholds
Time-Series Line Charts	Trends over time for CTR, conversions, spend
Table with Conditional Formatting	Anomaly-flagged rows highlighted in red
Slicers	Filter by campaign name, date, or platform
Drillthrough Pages	View campaign-specific performance by clicking rows

All metrics are formatted (percentages, currency), responsive, and mobile-ready (via Power BI Service).

🐳 One-Command Setup
Run the entire system using Docker:
docker-compose up --build
This spins up:
PostgreSQL with seeded campaign_metrics data

Python scripts (ETL + anomaly detection)

Optional pgAdmin for query exploration

🧪 Use Cases
Marketing teams who need proactive campaign monitoring

Analysts who want to move away from manual spreadsheets

Data engineers building lightweight real-time dashboards
