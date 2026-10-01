# ApexPlanet-Task-1-Data-Wrangling
Data Immersion and Wrangling – Task 1


## Project Overview

This project is part of Task 1: Data Immersion & Wrangling.

The main objective of this task is to understand the dataset, identify data quality issues, clean and transform the data, and prepare it for further analysis.

## Dataset

The dataset contains 1000 records and 12 main columns related to customer orders and sales.

### Main Columns

- Order_ID – Unique order identification number
- Order_Date – Date when the order was placed
- Customer_ID – Unique customer identification number
- Customer_Name – Name of the customer
- Age – Age of the customer
- Gender – Gender of the customer
- City – City of the customer
- Product – Name of the purchased product
- Category – Category of the product
- Quantity – Number of units purchased
- Unit_Price – Price of one unit
- Total_Sales – Total sales amount

## Data Quality Assessment

The following data quality checks were performed:

- Missing values
- Duplicate records
- Data types and formatting
- Sales calculation verification
- Outlier detection

### Findings

- 20 missing values were found in the Age column.
- 13 missing values were found in the City column.
- No exact duplicate rows were found.
- Order_Date was converted into proper date format.
- 19 potential outliers were detected in Total_Sales using the IQR method.
- Total_Sales was verified against Quantity × Unit_Price.

## Data Cleaning

The following cleaning steps were performed:

- Converted Order_Date into datetime format.
- Filled missing Age values using Gender-wise median.
- Filled missing City values with "Unknown".
- Verified Total_Sales using Quantity × Unit_Price.
- Detected sales outliers using the IQR method.
- Saved the cleaned dataset for further analysis.

## Files Included

- `ApexPlanet_DataAnalytics_Dataset.xlsx` – Original dataset
- `ApexPlanet_Cleaned_Dataset.xlsx` – Cleaned dataset
- `Data_Dictionary.xlsx` – Data dictionary
- `cleaning_script.py` – Python/Pandas cleaning script

## Tools Used

- Python
- Pandas
- Microsoft Excel
- Google Colab
- GitHub

## Conclusion

The dataset was examined, cleaned, and transformed into an analysis-ready format. Data quality issues such as missing values, date formatting, and potential outliers were identified and handled appropriately.
