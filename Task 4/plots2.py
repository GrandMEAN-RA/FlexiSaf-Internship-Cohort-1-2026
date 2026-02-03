
#Import Libraries
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Read data files
BASE_PATH = Path(__file__).resolve().parent
file_path1 = BASE_PATH / r'dataset\churn.csv'
file_path2 = BASE_PATH / r'dataset\electricity.csv'

churn = pd.read_csv(file_path1)
energy = pd.read_csv(file_path2)

#Preview datasets
print('CHURN \n', churn.head(15))
print('\n\nENERGY \n', energy.head(15))

#Extract plot data for line chart
x = energy['DATE']
x = pd.to_datetime(x, format='%d/%m/%Y') #convert date strings to datetime
y = energy.groupby(x.dt.to_period('M'))['IPG2211A2N'].sum() #compute total energy for every month

#Line Chart
plt.figure(figsize=(10,5))
y.plot(kind='line')
plt.title('Monthly Energy Usage by Year')
plt.xlabel('Date')
plt.ylabel('Monthly Energy Usage')
plt.savefig('lineplot.png',dpi=300)

#Scatter Chart
x = churn['CreditScore']
y = churn['EstimatedSalary']
plt.figure(figsize=(10,5))
plt.scatter(x,y)
plt.title('Salary vs Credit Score')
plt.xlabel('Credit Score')
plt.ylabel('Estimated Salary')
plt.savefig('scatterplot.png',dpi=300)

#Set seaborn default theme
sns.set_theme()

#Histogram
plt.figure(figsize=(10,5))
sns.histplot(data=churn, x='Age')
plt.title('Age Distribution')
plt.xlabel('Age(years)')
plt.ylabel('Count')
plt.savefig('histogram.png',dpi=300)

#Boxplot
plt.figure(figsize=(10,5))
sns.boxplot(data=churn, x='Geography', y='Tenure')
plt.title('Tenure by Geography')
plt.xlabel('Geography')
plt.ylabel('Tenure(years)')
plt.savefig('boxplot.png',dpi=300)

plt.show()
