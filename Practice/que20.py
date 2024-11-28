""" 20. Write a program to cluster a set of points using K-means for IRIS
dataset. Consider, K=3, clusters. Consider Euclidean distance as the
distance measure. Randomly initialize a cluster mean as one of the data
points. Iterate at least for 10 iterations. After iterations are over, print the
final cluster means for each of the clusters.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the Iris dataset (assuming the file is named 'iris.csv' and located in the current directory)
df = pd.read_csv('Datasets/IRIS.csv')

# Select only the numerical columns for clustering (excluding 'species')
X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].values

# Set K (number of clusters)
K = 3

# Randomly initialize the centroids by picking random data points
np.random.seed(42)  # For reproducibility
initial_centroids = X[np.random.choice(X.shape[0], K, replace=False)]

# Function to compute the Euclidean distance between points
def euclidean_distance(a, b):
    return np.sqrt(np.sum((a - b) ** 2))

# Function to assign clusters based on the closest centroid
def assign_clusters(X, centroids):
    clusters = []
    for point in X:
        distances = [euclidean_distance(point, centroid) for centroid in centroids]
        clusters.append(np.argmin(distances))
    return np.array(clusters)

# Function to recalculate the centroids
def recalculate_centroids(X, clusters, K):
    new_centroids = np.zeros((K, X.shape[1]))
    for k in range(K):
        cluster_points = X[clusters == k]
        if len(cluster_points) > 0:
            new_centroids[k] = cluster_points.mean(axis=0)
    return new_centroids

# K-means algorithm
iterations = 10
centroids = initial_centroids
for i in range(iterations):
    clusters = assign_clusters(X, centroids)
    centroids = recalculate_centroids(X, clusters, K)

# Print the final centroids
print("Final Cluster Centroids after 10 iterations:")
for i, centroid in enumerate(centroids):
    print(f"Cluster {i+1} centroid: {centroid}")

# Optional: Plot the clusters for visualization (using only 2 features for simplicity)
plt.scatter(X[:, 0], X[:, 1], c=clusters, cmap='viridis', marker='o')
plt.scatter(centroids[:, 0], centroids[:, 1], color='red', marker='x', s=200, label='Centroids')
plt.title('K-means Clustering (K=3)')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.legend()
plt.show()
