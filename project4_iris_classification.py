import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 1. LOAD DATASET
iris = load_iris()
df_iris = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df_iris['Species'] = iris.target
df_iris['Species_Name'] = df_iris['Species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

# 2. MACHINE LEARNING MODEL SETUP
X = df_iris[iris.feature_names]
y = df_iris['Species']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# 3. DATA VISUALIZATION
sns.set_theme(style="ticks")
pair_plot = sns.pairplot(df_iris.drop(columns=['Species']), hue='Species_Name', palette='husl')
pair_plot.fig.suptitle('Iris Flower Species Clustering & Characteristics', y=1.02)
pair_plot.savefig('iris_species_clusters.png')
plt.close()

print(f"Project 4: Iris Species Classification completed smoothly!")
print(f"Model Accuracy: {accuracy * 100:.2f}%")
