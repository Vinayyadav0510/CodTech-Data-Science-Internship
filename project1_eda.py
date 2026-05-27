import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. GENERATE DATASET
np.random.seed(42)
data_size = 200
data = {
'Customer_ID': range(1001, 1001 + data_size),
'Age': np.random.choice([22, 28, 35, 40, np.nan, 55, 62], size=data_size),
'Gender': np.random.choice(['Male', 'Female'], size=data_size),
'Purchase_Amount': np.round(np.random.uniform(10.0, 500.0, size=data_size), 2),
'Product_Category': np.random.choice(['Electronics', 'Clothing', 'Home', 'Books'], size=data_size),
'Satisfied': np.random.choice(['Yes', 'No'], size=data_size, p=[0.7, 0.3])
}
df = pd.DataFrame(data)

# 2. DATA CLEANING
median_age = df['Age'].median()
df['Age'].fillna(median_age, inplace=True)

# 3. STATISTICAL ANALYSIS
category_sales = df.groupby('Product_Category')['Purchase_Amount'].sum()

# 4. DATA VISUALIZATION
sns.set_theme(style="whitegrid")

# Plot 1: Age Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['Age'], bins=10, kde=True, color='skyblue')
plt.title('Customer Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')
plt.savefig('age_distribution.png') 
plt.close()

# Plot 2: Total Sales Bar Chart
plt.figure(figsize=(8, 5))
sns.barplot(x=category_sales.index, y=category_sales.values, palette='muted')
plt.title('Total Purchase Amount by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Total Sales ($)')
plt.savefig('sales_by_category.png') 
plt.close()

print("Project 1 executed smoothly! Visualizations generated.")
