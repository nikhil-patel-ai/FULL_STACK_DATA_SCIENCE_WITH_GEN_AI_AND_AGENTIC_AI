"""
Hyperparameter Tuning

Goal: Use cross-validation and GridSearchCV to find useful hyperparameters.

Run from this folder with:
    python "Hyperparameter_Tuning_practice.py"

This is a learning example. Review the code and dependencies before using it in production.
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)
pipeline = make_pipeline(StandardScaler(), SVC())
param_grid = {
    "svc__C": [0.1, 1, 10],
    "svc__kernel": ["linear", "rbf"]
}
search = GridSearchCV(pipeline, param_grid, cv=5, scoring="accuracy")
search.fit(X_train, y_train)
print("Best parameters:", search.best_params_)
print("Best cross-validation score:", search.best_score_)
print("Held-out test accuracy:", accuracy_score(y_test, search.predict(X_test)))
