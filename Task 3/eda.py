# Import Libraries
from pathlib import Path
import pandas as pd
import numpy as np

# Read Data File
BASE_PATH = Path(__file__).resolve().parent
file_path = BASE_PATH / "dataset.csv"
data = pd.read_csv(file_path)

# --- Preview data ---
print("Data Preview:\n", data.head(), "\n")
print("Column data types:\n")
data.info()
print("\nSummary Statistics:\n", data.describe(), "\n")

# -------- EDA Summary --------
stats = {
    "Age": [
        data["Age"].mean(),
        data["Age"].median(),
        data["Age"].mode().iloc[0],
        data["Age"].std()
    ],
    "MonthlyBill": [
        data["MonthlyBill"].mean(),
        data["MonthlyBill"].median(),
        data["MonthlyBill"].mode().iloc[0],
        data["MonthlyBill"].std()
    ],
    "DataUsageGB": [
        data["DataUsageGB"].mean(),
        data["DataUsageGB"].median(),
        data["DataUsageGB"].mode().iloc[0],
        data["DataUsageGB"].std()
    ],
    "TenureMonths": [
        data["TenureMonths"].mean(),
        data["TenureMonths"].median(),
        data["TenureMonths"].mode().iloc[0],
        data["TenureMonths"].std()
    ]
}

summary_df = pd.DataFrame(
    stats,
    index=["Mean", "Median", "Mode", "Std. Dev"]
)

print("\nEDA Summary Table:\n")
print(summary_df)

numeric_data = data.select_dtypes(include=[np.number])
print(f"\nCorrelation Matrix: \n\n {numeric_data.corr()} \n")
