# Buildables Data Engineering Fellowship Portfolio

**Author:** Muhammad Awais  
**Role:** Data Engineer | ETL Specialist | Infrastructure Lead  
**Fellowship Duration:** Aug 2025 - Oct 2025  

[![Medium](https://img.shields.io/badge/Medium-Read%20My%20Journey-black?logo=medium)](https://medium.com/@awaisstack)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://linkedin.com/in/awaisstack)

---

## Executive Summary
This repository documents my intensive journey through the **Buildables Data Engineering Fellowship**. Over the course of the program, I transitioned from writing raw SQL queries to architecting scalable, containerized data platforms. 

The portfolio demonstrates proficiency in **Legacy ETL (SSIS)**, **Modern Stacks (Airflow, Docker, MinIO)**, and **Big Data Architecture**. It culminates in **SynthCart**, a production-grade platform where I led the infrastructure design for a cross-functional team.

---

## 🏆 Capstone Project: SynthCart Platform
> **📂 Location:** [`Week 7-12 Final_Project_SynthCart`](./Week%207-12%20Final_Project_SynthCart)

**Role:** Lead Infrastructure Engineer, Gold Layer Architect & Silver Layer Co-Developer  
**Goal:** Build a Medallion Architecture platform to process e-commerce data for BI dashboards.

**Key Achievements:**
* **Infrastructure:** Deployed the complete **Docker** environment, configuring Airflow, MinIO, PostgreSQL, and Redis to run seamlessly as a distributed system.
* **Gold Layer (Owner):** Engineered the Star Schema, creating business-ready Fact (`fact_orders`) and Dimension (`dim_customers`, `dim_products`) tables.
* **Silver Layer (Co-Developer):** Collaborated on **PySpark** jobs to clean raw data, handling missing values and enforcing schema validation to achieve a **98.5% data quality score**.
* **Orchestration:** Designed automated Airflow DAGs to manage the dependencies between the Bronze, Silver, and Gold layers.

---

## Weekly Roadmap & Technical Deep Dive

### 🔹 Phase 1: Foundations (SQL & Python)

| Week | Project & Description | Key Tech |
| :--- | :--- | :--- |
| **01** | **[Week 1: Querying Data with SQL](./Week_1_SQL)** <br> Mastered complex data retrieval on the Olist E-commerce dataset. Wrote 15 advanced queries utilizing **JOINS, CTEs, Window Functions, and Aggregations**. | `SQL` `PostgreSQL` |
| **02** | **[Week 2: Data Engineering with Python & Pandas](./Week_2_Python_ETL)** <br> Built a robust ETL script for Real Estate data. Handled **outlier detection**, schema enforcement, and created a reusable function to convert raw CSVs into optimized **Parquet** files. | `Python` `Pandas` `Parquet` |
| **03** | **[Week 3: Data Engineering Foundations](./Week%203--Data%20Engineering%20Foundations)** <br> A knowledge base documenting modern DE concepts: **Data Lake vs Warehouse**, **Star Schemas**, **Scaling**, and **Orchestration** theory. | `System Design` `Documentation` |

### 🔹 Phase 2: Enterprise & Modern Pipelines

| Week | Project & Description | Key Tech |
| :--- | :--- | :--- |
| **04-05** | **[Week 4-5: SSIS Pipelines (Enterprise ETL)](./Week%204-5--%20(SSIS)%20Fundamentals%20%26%20Hands-On)** <br> Developed visual ETL workflows using **SQL Server Integration Services (SSIS)**. Implemented Control Flows, Data Flows, Conditional Splits, and automated file loops for the PSL Cricket dataset. | `SSIS` `Visual Studio` `SQL Server` |
| **06** | **[Week 6: Mini ETL Project (Modern Stack)](./Week%206%20--Mini%20ETL%20Project)** <br> The bridge to the modern stack. Setup a local **Airflow** instance to orchestrate data movement from **MinIO** (Object Storage) to **PostgreSQL** (Warehouse) using Docker. | `Docker` `Airflow` `MinIO` |

### 🔹 Phase 3: Production Grade Engineering (The Final Project)

| Week | Project & Description | Key Tech |
| :--- | :--- | :--- |
| **07-12** | **[Week 7-12: Final Project - SynthCart](./Week%207-12%20Final_Project_SynthCart)** <br> **The Capstone.** A full-scale Data Platform connecting Data Engineers and Analysts. Implemented a Medallion Architecture with automated DAGs, Spark processing, and Power BI integration. | `Docker` `Spark` `Airflow` `Power BI` |

---

## 💻 Technical Stack

**Infrastructure & Cloud**
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![MinIO](https://img.shields.io/badge/MinIO-C72E49?style=flat&logo=minio&logoColor=white)

**Orchestration & Transformation**
![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-017CEE?style=flat&logo=Apache%20Airflow&logoColor=white)
![SSIS](https://img.shields.io/badge/SSIS-CC2927?style=flat&logo=microsoft-sql-server&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)

**Databases & Storage**
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=flat&logo=postgresql&logoColor=white)
![SQL Server](https://img.shields.io/badge/SQL%20Server-CC2927?style=flat&logo=microsoft-sql-server&logoColor=white)
![Parquet](https://img.shields.io/badge/Parquet-Data_Format-success)

---

## 📝 Engineering Log (Medium Articles)

I believe in "Learning in Public." Throughout this fellowship, I published detailed technical breakdowns of my projects:

1.  **[How Buildables Fellowship Helped Me Master SQL in 7 Days](https://medium.com/@awaisstack/how-buildables-fellowship-helped-me-master-sql-in-7-days-as-a-data-engineer-af92dbe79072)**
2.  **[From Chaos to Insights: My Week 2 ETL Adventure with Python](https://medium.com/@awaisstack/from-chaos-to-insights-my-week-2-etl-adventure-with-python-88df8086a2f4)**
3.  **[Week 3: Learning Data Engineering Foundations](https://medium.com/@awaisstack/data-engineer-week3-de5757087c92)**
4.  **[My Journey Learning SSIS in One Week](https://medium.com/@awaisstack/my-week-4-at-buildables-data-engineering-fellowship-learning-ssis-in-one-week-635e269956a1)**
5.  **[MinIO, PostgreSQL, and Airflow Journey](https://medium.com/@awaisstack/my-buildables-week-5-data-engineering-journey-minio-postgresql-and-airflow-5571f5d8d4fc)**

---

<p align="center">
  <i>"Data Engineering is not just about moving data; it's about delivering trust."</i>
</p>
