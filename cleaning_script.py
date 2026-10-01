
import pandas as pd

# Load dataset
df = pd.read_excel("ApexPlanet_DataAnalytics_Dataset.xlsx")

# Convert Order_Date to date format
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")

# Fill missing Age using Gender-wise median
df["Age"] = df.groupby("Gender")["Age"].transform(
    lambda x: x.fillna(x.median())
)

# Fill missing City
df["City"] = df["City"].fillna("Unknown")

# Calculate sales for verification
df["Calculated_Sales"] = df["Quantity"] * df["Unit_Price"]

# Detect sales outliers using IQR
Q1 = df["Total_Sales"].quantile(0.25)
Q3 = df["Total_Sales"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df["Sales_Outlier"] = (
    (df["Total_Sales"] < lower) |
    (df["Total_Sales"] > upper)
)

# Save cleaned dataset
df.to_excel("ApexPlanet_Cleaned_Dataset.xlsx", index=False)
