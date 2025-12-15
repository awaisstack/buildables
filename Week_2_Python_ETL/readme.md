# 🐍 Week 2: Data Engineering with Python & Pandas

**Focus:** ETL Pipelines, Data Cleaning, Pandas, Parquet  
**Dataset:** US Real Estate / Housing Prices

## 📝 Project Overview
This project simulates a production ETL (Extract, Transform, Load) task. The goal was to take raw, "messy" housing data, clean it programmatically using Python/Pandas, and export it into optimized formats for analysis.

## 🛠️ The Pipeline Stages

### 1. Extract (Ingestion)
* Loaded raw CSV data containing housing listings.
* Inspected schema and data types.

### 2. Transform (Cleaning & Logic)
* **Schema Enforcement:** Renamed columns to `snake_case` and converted dates to datetime objects.
* **Missing Values:** Implemented strategies to fill gaps (Median for prices, Mode for categorical fields).
* **Outlier Removal:** Removed the top 1% of house sizes to fix skewed distributions.
* **Feature Engineering:** Created a new KPI: `price_per_sqft`.
* **Deduplication:** Identified and removed duplicate listing entries.

### 3. Load (Storage)
* Exported the clean data to **CSV** (for human readability).
* Exported to **Parquet** (for high-performance columnar storage).

## 💻 Reusable ETL Function
I encapsulated the entire logic into a reusable function `etl_real_estate(file_path)` that enables automated processing of new data batches without rewriting code.

## 📖 Related Article
[**From Chaos to Insights: My Week 2 ETL Adventure with Python**](https://medium.com/@awaisstack/from-chaos-to-insights-my-week-2-etl-adventure-with-python-88df8086a2f4)
