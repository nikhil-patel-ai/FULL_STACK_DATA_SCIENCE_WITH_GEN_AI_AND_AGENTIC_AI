"""
Neural Networks

Goal: Train a small multilayer perceptron using scikit-learn.

Run from this folder with:
    python "Neural_Networks_practice.py"

This is a learning example. Review the code and dependencies before using it in production.
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
model = make_pipeline(StandardScaler(), MLPClassifier(hidden_layer_sizes=(16, 8), max_iter=2000, random_state=42))
model.fit(X_train, y_train)
print("Test accuracy:", accuracy_score(y_test, model.predict(X_test)))
