import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def euclidean_distance(a, b):
    return np.sqrt(np.sum((a - b) ** 2))


def kmeans(data, k, max_iterations=100):
    
    centroids = data.sample(n=k).values
    for _ in range(max_iterations):
       
        clusters = assign_clusters(data, centroids)
        
        new_centroids = calculate_centroids(data, clusters, k)
       
        if np.all(centroids == new_centroids):
            break
        centroids = new_centroids
    return centroids, clusters


def assign_clusters(data, centroids):
    clusters = []
    for _, row in data.iterrows():
        distances = [euclidean_distance(row.values, centroid) for centroid in centroids]
        cluster = np.argmin(distances)
        clusters.append(cluster)
    return np.array(clusters)


def calculate_centroids(data, clusters, k):
    centroids = []
    for i in range(k):
        cluster_points = data[clusters == i]
        if len(cluster_points) == 0:
            
            centroid = data.sample(n=1).values[0]
        else:
            centroid = cluster_points.mean(axis=0)
        centroids.append(centroid)
    return np.array(centroids)


csv_file = 'cleaned_data.csv'
data = pd.read_csv(csv_file)


data['Longitude'] = pd.to_numeric(data['Longitude'], errors='coerce')
data['Latitude'] = pd.to_numeric(data['Latitude'], errors='coerce')


data = data.dropna(subset=['Longitude', 'Latitude'])



k = 13


centroids, clusters = kmeans(data[['Longitude', 'Latitude']], k)


plt.scatter(data['Longitude'], data['Latitude'], c=clusters,s = 1, cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', s=10, c='red', label='Centroids')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('K-means Clustering')
plt.show()
