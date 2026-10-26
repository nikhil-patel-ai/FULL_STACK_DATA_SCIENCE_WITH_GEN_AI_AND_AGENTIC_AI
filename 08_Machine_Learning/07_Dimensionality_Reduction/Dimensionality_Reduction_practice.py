"""
Dimensionality Reduction

Goal: Use PCA to reduce many features to fewer components.

Run from this folder with:
    python "Dimensionality_Reduction_practice.py"

This is a learning example. Review the code and dependencies before using it in production.
"""

from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

X = load_iris().data
X_scaled = StandardScaler().fit_transform(X)
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X_scaled)

print("Original shape:", X.shape)
print("Reduced shape:", X_reduced.shape)
print("Explained variance ratio:", pca.explained_variance_ratio_)
print("Total variance retained:", pca.explained_variance_ratio_.sum())
