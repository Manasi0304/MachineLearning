"""9. Write a program to do the following: You have given a collection of 8
points. P1=[0.1,0.6] P2=[0.15,0.71] P3=[0.08,0.9] P4=[0.16, 0.85]
P5=[0.2,0.3] P6=[0.25,0.5] P7=[0.24,0.1] P8=[0.3,0.2]. Perform the k-mean
clustering with initial centroids as m1=P1 =Cluster#1=C1 and
m2=P8=cluster#2=C2. Answer the following 1] Which cluster does P6
belong to? 2] What is the population of a cluster around m2? 3] What is
the updated value of m1 and m2?
"""


import numpy as np

# Given points
points = {
    'P1': np.array([0.1, 0.6]),
    'P2': np.array([0.15, 0.71]),
    'P3': np.array([0.08, 0.9]),
    'P4': np.array([0.16, 0.85]),
    'P5': np.array([0.2, 0.3]),
    'P6': np.array([0.25, 0.5]),
    'P7': np.array([0.24, 0.1]),
    'P8': np.array([0.3, 0.2])
}

# Initial centroids
m1 = points['P1']
m2 = points['P8']

# Perform k-means clustering (single iteration for this example)
cluster1 = []
cluster2 = []

for point_name, point in points.items():
    distance_m1 = np.linalg.norm(point - m1)
    distance_m2 = np.linalg.norm(point - m2)
    if distance_m1 < distance_m2:
        cluster1.append(point_name)
    else:
        cluster2.append(point_name)

# Answers:
# 1. Which cluster does P6 belong to?
if 'P6' in cluster1:
    print("P6 belongs to Cluster 1")
else:
    print("P6 belongs to Cluster 2")

# 2. What is the population of the cluster around m2?
print("Population of Cluster 2 (around m2):", len(cluster2))

# 3. What are the updated values of m1 and m2?
m1_updated = np.mean(np.array([points[p] for p in cluster1]))
m2_updated = np.mean(np.array([points[p] for p in cluster2]))

print("Updated m1:", m1_updated)
print("Updated m2:", m2_updated)