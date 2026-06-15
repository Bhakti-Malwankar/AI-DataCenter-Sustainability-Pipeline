# AI Data Center Sustainability Analytics Pipeline

## Overview

A Data Engineering project that processes and analyzes global data center sustainability data, focusing on water consumption, electricity usage, cooling efficiency, and environmental impact.

The project implements an end-to-end ETL pipeline using Python, PostgreSQL, and SQL to transform raw datasets into structured analytical insights and automated reports.

---

## Tech Stack

* Python
* PostgreSQL
* SQL
* Pandas
* SQLAlchemy
* Docker
* Git

---

## Dataset

Global Data Center & AI Water/Electricity Usage Dataset

Records Processed: 126,000+

---

## Architecture

Raw CSV Dataset
→ Extract
→ Transform & Data Validation
→ PostgreSQL Database
→ SQL Analytics
→ Automated Reporting

---

## Features

* End-to-End ETL Pipeline
* Data Cleaning and Validation
* PostgreSQL Data Storage
* SQL-Based Analytics
* Automated CSV Report Generation
* Sustainability Insights Dashboard Foundation

---

## Analytics Reports

The pipeline generates reports for:

* Top Water Consuming Countries
* Top Electricity Consuming Countries
* Water Stress Analysis
* Cooling System Efficiency
* Yearly Electricity Consumption Trends
* Year-over-Year Growth Analysis

---

## Project Structure

AI-DataCenter-Sustainability-Pipeline

├── data/

├── etl/

│ ├── extract.py

│ ├── transform.py

│ └── load.py

├── reports/

│ ├── generate_report.py

│ └── output/

├── sql/

├── dags/

├── README.md

└── requirements.txt

---

## Key Outcomes

* Processed 126K+ sustainability records
* Built ETL workflows using Python and SQL
* Designed PostgreSQL-based analytical storage
* Generated automated sustainability reports
* Applied Data Engineering best practices for data quality and reporting

---

## Future Enhancements

* Apache Airflow Workflow Orchestration
* Interactive Power BI Dashboard
* Cloud Deployment
* Real-Time Data Ingestion
