import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. GENERATE DUMMY MOVIE RATINGS DATASET
np.random.seed(10)
data_size = 250

movie_data = {
    'Movie_ID': range(5001, 5001 + data_size),
    'Genre': np.random.choice(['Action', 'Comedy', 'Drama', 'Sci-Fi', 'Horror'], size=data_size),
    'Director_Rating': np.round(np.random.uniform(5.0, 9.5, size=data_size), 1),
    'Audience_Rating': np.round(np.random.uniform(4.5, 9.8, size=data_size), 1),
    'Budget_Millions': np.random.randint(10, 200, size=data_size)
}

df_movies = pd.DataFrame(movie_data)

# 2. DATA VISUALIZATION
sns.set_theme(style="darkgrid")

# Plot 1: Box Plot (Saves to folder)
plt.figure(figsize=(8, 5))
sns.boxplot(x='Genre', y='Audience_Rating', data=df_movies, palette='Set3')
plt.title('Audience Rating Distribution by Movie Genre')
plt.xlabel('Movie Genre')
plt.ylabel('Audience Rating (1-10)')
plt.savefig('movie_rating_distribution.png')
plt.close()

# Plot 2: Scatter Plot (Saves to folder)
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Director_Rating', y='Audience_Rating', hue='Genre', data=df_movies, palette='deep')
plt.title('Director Ratings vs Audience Ratings')
plt.xlabel('Director Rating')
plt.ylabel('Audience Rating')
plt.savefig('director_vs_audience.png')
plt.close()

print("Project 3: Movie Rating Analysis executed smoothly!")
