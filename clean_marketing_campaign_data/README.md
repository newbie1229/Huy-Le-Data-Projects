# 🧹 Bank Marketing Data Cleaning Project

## 📌 Objective
Clean and preprocess the bank marketing dataset to prepare it for further analysis. Specifically:
- Normalize and encode categorical fields such as `job` and `education`
- Convert `yes`/`no`/`unknown` string fields into boolean format
- Split the cleaned data into three separate tables: `client.csv`, `campaign.csv`, and `economics.csv`
- Create a unified `last_contact_date` field from separate `day`, `month`, and `year` columns

## 🧰 Tools Used
- Pandas
- Numpy

## 🧠 Skills Used
- Data wrangling and cleaning with Pandas
- Handling missing and inconsistent values
- String manipulation
- Boolean and categorical encoding
- Date and time formatting
- Exporting DataFrames to CSV

## 🗂️ Folder Structure
```
project-folder/
│
├── bank_marketing.csv         # Original raw dataset
├── code.py                    # Data cleaning script
├── client.csv                 # Cleaned client data
├── campaign.csv               # Cleaned campaign data
└── economics.csv              # Extracted economic indicators
```

## 🚀 How to Run
1. Install required libraries (if not already installed):
```bash
pip install pandas numpy
```

2. Run the script:
```bash
python clean_data.py
```

This will generate the cleaned `.csv` files for analysis.

*Data Source: [DataCamp](https://projects.datacamp.com/projects/1613)*

