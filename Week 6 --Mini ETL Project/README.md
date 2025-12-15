# Mini-ETL Project: Getting Started with DE Tools

This repository contains my **mini-ETL project** for the Data Engineering course, Task 5: *Getting Started with DE Tools: MinIO, PostgreSQL, and Airflow*. The goal of this project was to set up the three core components of a modern ETL pipeline and run a small workflow to understand how they interact in practice.

---

## 🚀 Project Overview

In this project, I built a **complete ETL pipeline** using:

1. **MinIO (Landing Zone)**
   - Stores and retrieves raw CSV data files.
   - Functions as an S3-compatible object storage.

2. **PostgreSQL (Data Warehouse)**
   - Stores structured and transformed data.
   - Allows running SQL queries to validate the ETL process.

3. **Apache Airflow (Orchestration Tool)**
   - Automates and schedules ETL tasks.
   - Orchestrates Extract → Transform → Load (ETL) workflow via DAGs.

---

## 🛠️ Tools & Technology Stack

- **Python 3.12**
- **Pandas** for data transformation
- **SQLAlchemy & psycopg2-binary** for PostgreSQL integration
- **MinIO Python SDK** to interact with object storage
- **Docker & Docker Compose** for environment setup
- **Airflow 3** to orchestrate ETL tasks

---

## 📂 Project Structure

```
mini-etl/
├── dags/
│   └── etl_run_dag.py          # Airflow DAG for ETL pipeline
├── plugins/                     # Airflow plugins (if any)
├── logs/                        # Airflow logs
├── employees_large.csv          # Input CSV file
├── employees_summary.csv        # ETL output
├── generate_csv.py              # Script to generate sample CSVs
├── etl.py                       # Main ETL script
├── requirements.txt             # Python dependencies
├── Dockerfile                   # Custom Airflow Docker image
├── docker-compose.yml           # Docker Compose setup
├── .gitignore                   # Git ignore file
└── README.md                    # Project documentation
```

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone 
cd mini-etl
```

### 2. Build & Start Docker Containers

```bash
docker compose down
docker compose up --build -d
```

### 3. Access Airflow UI

Open in your browser:

```
http://localhost:8080
```

Login credentials (default):

```
Username: admin
Password: admin
```

### 4. Trigger ETL DAG

- DAG Name: `run_etl_docker`
- Tasks: Extract → Transform → Load
- Schedule: Manual trigger

### 5. Verify PostgreSQL

Check the loaded data:

```sql
SELECT * FROM employees_summary;
```

---

## 🧩 ETL Workflow

1. **Extract:** Download CSV from MinIO using Python.
2. **Transform:** Clean and summarize data using pandas.
3. **Load:** Insert cleaned data into PostgreSQL.
4. **Orchestrate:** Airflow DAG executes all steps sequentially.


This project forms a solid foundation before moving on to team-based ETL projects and more advanced data engineering pipelines.

---
