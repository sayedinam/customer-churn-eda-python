"""
Project: Customer Churn & Retention Exploratory Data Analysis
Author: Sayed Inamulhasan
Toolkit: Python (Pandas, NumPy, Matplotlib, Seaborn)
"""

import pandas as pd
import numpy as np

# 1. Dataset Simulation / Setup
data = {
    'CustomerID': range(1001, 1021),
    'Tenure_Months': [1, 24, 3, 12, 48, 2, 36, 6, 9, 60, 4, 18, 2, 72, 8, 30, 5, 15, 1, 40],
    'Contract': ['Month-to-Month', 'Two-Year', 'Month-to-Month', 'One-Year', 'Two-Year', 
                 'Month-to-Month', 'Two-Year', 'Month-to-Month', 'One-Year', 'Two-Year',
                 'Month-to-Month', 'One-Year', 'Month-to-Month', 'Two-Year', 'Month-to-Month',
                 'Two-Year', 'Month-to-Month', 'One-Year', 'Month-to-Month', 'Two-Year'],
    'MonthlyCharges': [70.5, 20.1, 85.0, 45.2, 19.8, 95.5, 60.0, 75.2, 55.4, 25.0,
                      80.1, 49.9, 90.2, 22.5, 65.0, 58.0, 88.0, 52.1, 92.4, 24.0],
    'Churn': ['Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'No', 'No',
              'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No']
}

df = pd.DataFrame(data)

# 2. Summary Statistics
print("--- DATASET OVERVIEW ---")
print(df.info())
print("\n--- DESCRIPTIVE STATISTICS ---")
print(df.describe())

# 3. Churn Distribution
churn_rate = (df['Churn'].value_counts(normalize=True) * 100).round(2)
print("\n--- CHURN RATE PERCENTAGE ---")
print(churn_rate)

# 4. Churn by Contract Type
contract_churn = df.groupby(['Contract', 'Churn']).size().unstack(fill_value=0)
contract_churn['Churn_Rate_Pct'] = (contract_churn['Yes'] / (contract_churn['Yes'] + contract_churn['No']) * 100).round(2)
print("\n--- CHURN BY CONTRACT TYPE ---")
print(contract_churn)

# 5. Average Charges & Tenure for Churned vs Retained Customers
metrics_comparison = df.groupby('Churn').agg({
    'Tenure_Months': 'mean',
    'MonthlyCharges': 'mean'
}).round(2)

print("\n--- METRICS: CHURNED VS RETAINED ---")
print(metrics_comparison)
