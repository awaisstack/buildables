# 📚 Week 3: Data Engineering Foundations & Architecture

**Focus:** System Design, Documentation, DE Theory, Architecture

## 📝 Project Overview
This week shifted focus from coding to **Engineering Design**. Data Engineering is not just about writing scripts; it is about choosing the right architecture for the job. This folder contains research and documentation on the core building blocks of modern data platforms.

## 🧠 Key Concepts Covered

### 1. Storage Architectures
* **Data Warehouse:** Structured, schema-on-write (e.g., Snowflake, Redshift).
* **Data Lake:** Unstructured/Semi-structured, schema-on-read (e.g., S3, MinIO).
* **Data Lakehouse:** The hybrid approach combining ACID transactions with object storage.

### 2. Data Modeling
* **Star Schema:** Fact Tables (Events) vs. Dimension Tables (Attributes).
* **Normalization vs. Denormalization.**

### 3. Processing Paradigms
* **ETL vs. ELT:** When to transform data (in-flight vs. in-database).
* **Batch vs. Streaming:** Trade-offs between latency and complexity.
* **Scaling:** Vertical (Hardware upgrade) vs. Horizontal (Distributed nodes).

### 4. Orchestration
* Understanding DAGs (Directed Acyclic Graphs).
* Introduction to Airflow as a scheduler.

## 📄 Deliverables
* **DE Handbook:** A compiled PDF explaining these concepts with diagrams.
* **Architecture Comparisons:** Trade-off analysis for different DE tools.

## 📖 Related Article
[**Week 3: Learning Data Engineering Foundations**](https://medium.com/@awaisstack/data-engineer-week3-de5757087c92)
