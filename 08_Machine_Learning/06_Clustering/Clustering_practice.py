"""
Clustering

Goal: Group unlabeled observations with K-Means and inspect cluster assignments.

Run from this folder with:
    python "Clustering_practice.py"

This is a learning example. Review the code and dependencies before using it in production.
"""

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

X, _ = make_blobs(n_samples=150, centers=3, cluster_std=1.0, random_state=42)
X_scaled = StandardScaler().fit_transform(X)
model = KMeans(n_clusters=3, random_state=42, n_init=10)
labels = model.fit_predict(X_scaled)

print("First 20 cluster labels:", labels[:20])
print("Cluster centers (scaled space):\n", model.cluster_centers_)
print("Inertia:", model.inertia_)
