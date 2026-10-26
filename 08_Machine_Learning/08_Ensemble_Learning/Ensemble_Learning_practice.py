"""
Ensemble Learning

Goal: Compare a single decision tree with a random forest classifier.

Run from this folder with:
    python "Ensemble_Learning_practice.py"

This is a learning example. Review the code and dependencies before using it in production.
"""

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)
models = {
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=150, random_state=42)
}
for name, model in models.items():
    model.fit(X_train, y_train)
    print(name, "accuracy:", round(accuracy_score(y_test, model.predict(X_test)), 4))
