"""\nClassification Starter Scripts\n\nLearning goal: Start with a baseline classifier, then compare it with algorithm-specific examples.\nRun with: python "Classification_Starter_Scripts_practice.py"\n"""\n\nfrom sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
model = DummyClassifier(strategy="most_frequent").fit(X_train, y_train)
print("Baseline accuracy:", accuracy_score(y_test, model.predict(X_test)))\n