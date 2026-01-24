
# Import Libraries
from pathlib import Path
import matplotlib.pyplot as plt
import csv

# Read Data File
BASE_PATH =  Path(__file__).resolve().parent
file_path = BASE_PATH / "company_sales_data task 3.csv"

# Containers
month_number = []
total_profit = []
bathingsoap = []
facewash = []

# Read CSV
with open(file_path, newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        month_number.append(int(row["month_number"]))
        total_profit.append(float(row["total_profit"]))
        bathingsoap.append(int(row["bathingsoap"]))
        facewash.append(int(row["facewash"]))

# Plot Data
plt.figure(figsize=(10, 6))
plt.plot(month_number, total_profit)
plt.xlabel("Month Number")
plt.ylabel("Total Profit")
plt.title("Total Profit by Months")

# ---Display the graph ---
plt.show()

# Subplots
fig, (ax1, ax2) = plt.subplots(2, sharex=True)
fig.suptitle('Subplots Showing Total Units of Bathingsoap '
             'and Facewash Sold by Month Number')
ax1.plot(month_number, bathingsoap)
ax1.set_title("Bathing Soap")
ax1.set_ylabel("Total Units Sold")
ax2.plot(month_number, facewash)
ax2.set_title("Face Wash")
ax2.set_ylabel("Total Units Sold")
ax2.set_xlabel("Month Number")

# ---Display the graph ---
plt.show()
