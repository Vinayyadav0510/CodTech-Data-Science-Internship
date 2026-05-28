import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. GENERATE NETFLIX DATASET
np.random.seed(42)
data_size = 300

netflix_data = {
'Show_ID': [f's{i}' for i in range(1, data_size + 1)],
'Type': np.random.choice(['Movie', 'TV Show'], size=data_size, p=[0.7, 0.3]),
'Title': [f'Netflix Title {i}' for i in range(1, data_size + 1)],
'Release_Year': np.random.choice([2016, 2018, 2019, 2021, 2022, 2024], size=data_size),
'Rating': np.random.choice(['TV-MA', 'TV-14', 'PG-13', 'R', 'PG'], size=data_size),
'Duration': np.random.choice(['95 min', '110 min', '1 Season', '3 Seasons'], size=data_size)
}

df_netflix = pd.DataFrame(netflix_data)

# 2. DATA ANALYSIS
type_counts = df_netflix['Type'].value_counts()

# 3. DATA VISUALIZATION
sns.set_theme(style="whitegrid")

# Plot 1: Pie Chart of Content Types
plt.figure(figsize=(6, 6))
plt.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', colors=['coral', 'skyblue'], startangle=140)
plt.title('Distribution of Netflix Content: Movies vs TV Shows')
plt.savefig('netflix_content_type.png')
plt.close()

# Plot 2: Content Release Trends Over Years
plt.figure(figsize=(8, 5))
sns.countplot(x='Release_Year', hue='Type', data=df_netflix, palette='Set2')
plt.title('Netflix Content Release Trends')
plt.xlabel('Release Year')
plt.ylabel('Count of Titles')
plt.savefig('netflix_release_trends.png')
plt.close()

print("Project 2: Netflix Content Visualization executed smoothly!")
