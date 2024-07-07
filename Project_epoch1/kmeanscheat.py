import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Read data from CSV file
file_path = 'cleaned_data.csv'
df = pd.read_csv(file_path)

# Ensure your CSV contains 'Latitude' and 'Longitude' columns
if 'Latitude' not in df.columns or 'Longitude' not in df.columns:
    raise ValueError("CSV file must contain 'Latitude' and 'Longitude' columns")

# Extracting the features for clustering
X = df[['Latitude', 'Longitude']].values

# Performing K-means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

# Getting the cluster centers and labels
centers = kmeans.cluster_centers_
labels = kmeans.labels_

# Adding the cluster labels to the DataFrame
df['cluster'] = labels

# Plotting the results
plt.scatter(df['Latitude'], df['Longitude'], c=df['cluster'], cmap='viridis', marker='o')
plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='x')
plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.title('K-means Clustering of Pincodes in Andhra Pradesh')
plt.show()
