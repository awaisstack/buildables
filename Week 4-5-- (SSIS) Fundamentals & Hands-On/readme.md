# ⚡ Week 4-5: Enterprise ETL with SSIS

**Focus:** Visual ETL, Control Flow, Data Flow, SQL Server  
**Tools:** Visual Studio 2022, SQL Server Integration Services (SSIS), SQL Server

## 📝 Project Overview
This project focuses on **Enterprise-grade ETL** using Microsoft's SSIS. I built a comprehensive pipeline to process Pakistan Super League (PSL) cricket data, demonstrating how visual ETL tools handle complex logic, branching, and automation.

## 🛠️ Pipeline Features

### 🔹 Control Flow (The Brain)
* **Precedence Constraints:** dynamic logic (e.g., "Only run next task if row count > 100").
* **Containers:** Used `Foreach Loop Containers` to iterate through multiple source files automatically.
* **Variables:** Implemented dynamic file paths and run-time variables.

### 🔹 Data Flow (The Muscle)
* **Sources:** Flat Files (CSV) and OLE DB Sources.
* **Transformations:**
    * `Derived Column`: Creating new calculated fields.
    * `Conditional Split`: Separating data based on city (e.g., Filtering "Lahore" matches).
    * `Multicast`: Sending the same data stream to multiple destinations.
    * `Merge Join`: Joining batting data with match data.
    * `Data Conversion`: Handling Unicode vs. Non-Unicode type mismatches.

## 🚀 Key Challenges Solved
* **Metadata Mismatches:** Resolved `DT_WSTR` vs `NVARCHAR` issues common in SSIS.
* **Dynamic Workflows:** Used Expressions to make the package adaptable to changing file dates/names.

## 📖 Related Article
[**My Journey Learning SSIS in One Week**](https://medium.com/@awaisstack/my-week-4-at-buildables-data-engineering-fellowship-learning-ssis-in-one-week-635e269956a1)
