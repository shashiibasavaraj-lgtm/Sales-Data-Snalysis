import pandas as pd
import matplotlib.pyplot as plt

# Sample Superstore Sales Data
data = {
    'Category': ['Technology', 'Furniture', 'Office Supplies', 'Technology', 'Furniture', 'Technology', 'Office Supplies'],
    'Region': ['West', 'East', 'West', 'South', 'West', 'East', 'South'],
    'Sales': [1000, 500, 300, 1500, 800, 2000, 400],
    'Profit': [200, 50, 30, 300, 100, 400, 50],
    'Product': ['Laptop', 'Chair', 'Pen', 'Phone', 'Table', 'Canon Printer', 'Paper']
}
df = pd.DataFrame(data)

# Analysis
print("Sales by Category:")
print(df.groupby('Category')['Sales'].sum())

print("\nProfit by Region:")
print(df.groupby('Region')['Profit'].sum())

# Visualization
df.groupby('Category')['Sales'].sum().plot(kind='bar', color=['#1f77b4', '#ff7f0e', '#2ca02c'])
plt.title('Sales by Category', fontsize=14, fontweight='bold')
plt.ylabel('Sales (Rs)')
plt.tight_layout()
plt.savefig('sales_chart.png')
plt.show()
