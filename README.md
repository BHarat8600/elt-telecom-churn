# ELT Telecom Churn Pipeline

## Overview
An end-to-end ELT pipeline that processes telecom customer churn data, stores it in SQL Server, and visualizes via Metabase.

## Tech Stack
- Python (ETL)
- SQL Server (Data Warehouse)
- Apache Airflow (Orchestration)
- Metabase (BI Dashboard)
- Docker (Containers)

## Folder Structure
elt-telecom-churn
├── airflow/
│ ├── dags/
│ │ └── churn_pipeline_dag.py
│ └── Dockerfile
├── data/
│ └── telecom_churn.csv
├── etl/
│ ├── transform.py
│ └── load_to_sqlserver.py
├── metabase/
│ └── Dockerfile
├── sqlserver/
│ ├── init.sql
│ └── reporting_table.sql
├── docker-compose.yml
├── requirements.txt
└── README.md

## How to Run

1. Clone the repo
2. Install Docker
3. Run the containers

```bash
docker-compose up --build -d
