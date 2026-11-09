"""\nDecision Trees\n\nLearning goal: Train a decision tree and inspect its classification performance.\nRun with: python "Decision_Trees_practice.py"\n"""\n\nfrom sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
model = DecisionTreeClassifier(max_depth=3, random_state=42).fit(X_train, y_train)
print(classification_report(y_test, model.predict(X_test)))\n