# 🛒 Building a Retail Data Pipeline

This project demonstrates how to build a modular **ETL data pipeline** for retail sales analysis using Python. It extracts, transforms, aggregates, and validates sales data from different file formats.

## 📌 Overview

This project was developed as a hands-on exercise to practice building ETL pipelines using Python. The focus was on structuring reusable components and handling data from multiple sources (CSV and Parquet). It also aims to simulate part of a real-world data engineering workflow.

## 📁 Project Structure

```
building_retail_pipeline/
│
├── data/                   # Source and output data files
│   ├── grocery_sales.xlsx
│   ├── extra_data.parquet
│   ├── clean_data.csv
│   └── agg_data.csv
│
├── etl_utils/              # Utility functions for ETL
│   ├── __init__.py
│   └── pipeline_utils.py
│
├── main_script.py          # Main script to execute the ETL pipeline
```

## ⚙️ Pipeline Workflow

1. **Extract**  
   Load `.csv` and `.parquet` files, then merge on the `index` column.

2. **Transform**  
   - Select relevant columns.
   - Handle missing values.
   - Add `Month` column from `Date`.
   - Filter out records with low `Weekly_Sales`.

3. **Aggregate**  
   Compute average weekly sales by month.

4. **Load**  
   Export transformed and aggregated datasets to `.csv` files.

5. **Validation**  
   Ensure exported files exist in the output directory.

## 🖼️ Pipeline Flow

```
CSV + Parquet → Merge → Clean → Monthly Aggregation → CSV Output → File Validation
```

## 📜 How to Run

1. Install required packages:
```bash
pip install pandas pyarrow
```

2. Run the pipeline:
```bash
python main_script.py
```

> ⚠️ Ensure your working directory matches the one set inside `main_script.py`

## 📊 Input Files

- `grocery_sales.csv`: Raw sales data.
- `extra_data.parquet`: Additional features to merge on `index`.

## 📦 Output Files

- `clean_data.csv`: Cleaned dataset ready for analysis.
- `agg_data.csv`: Aggregated data with monthly average sales.

## 🧠 Author

Huy Le – Aspiring Data Engineer  

*Project developed as part of learning and practice in building pipelines.*

### 🛠️ Key Skills Practiced

- ETL design using pure Python
- Data cleaning & transformation with Pandas
- Working with multiple file formats (CSV, Parquet)
- Writing modular, reusable pipeline functions

## 🚀 Future Work

- Parameterize file paths via CLI or config file
- Automate execution with Apache Airflow (future learning)
- Visualize sales trends by store or department
