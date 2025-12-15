# 📊 Week 1: Querying Data with SQL (Olist E-Commerce)

**Focus:** Advanced SQL, Data Analysis, Database Querying  
**Dataset:** [Olist Brazilian E-Commerce Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

## 📝 Project Overview
This project focuses on mastering SQL fundamentals by analyzing a real-world e-commerce database. The goal was to translate business questions into performant SQL queries, moving from basic selection to complex aggregations and joins.

## 🛠️ Technical Concepts Applied
* **Joins:** `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN` to connect Customers, Orders, and Products.
* **Aggregation:** `GROUP BY`, `SUM`, `AVG`, `COUNT` for sales reporting.
* **Filtering:** `WHERE`, `HAVING`, and complex logical operators.
* **Date Manipulation:** Extracting months/years for trend analysis.
* **Sorting & Ranking:** `ORDER BY` for finding top products and cities.

## 📂 Key Queries & Insights
This project consists of 15 structured queries divided into three levels:https://github.com/awaisstack/buildables/tree/main/Week_1_SQL

### 🔹 Basic
* Retrieving full customer lists.
* Filtering customers by specific states (e.g., SP) and zip codes.
* Sorting customers geographically.

### 🔹 Intermediate
* **Sales Analysis:** Total sales per product category.
* **Customer Segmentation:** Counting customers per city.
* **Outlier Detection:** Finding cities with >10 customers using `HAVING`.
* **Product Metrics:** Calculating Min/Max/Avg product weights for logistics.

### 🔹 Advanced
* **Full Order Context:** Joining `Customers` → `Orders` → `Items` → `Products`.
* **Reporting:** Generating a monthly sales report grouped by customer location and top-selling categories.
* **Payment Analysis:** Tracking orders with pending or missing payments via `LEFT JOIN`.

## 📖 Related Article
[**How Buildables Fellowship Helped Me Master SQL in 7 Days**](https://medium.com/@awaisstack/how-buildables-fellowship-helped-me-master-sql-in-7-days-as-a-data-engineer-af92dbe79072)

