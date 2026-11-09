"""\nClassification Fundamentals\n\nLearning goal: Understand classification, labels, binary versus multiclass problems, and the basic model workflow.\nRun with: python "Classification_Fundamentals_practice.py"\n"""\n\nfrom sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
model = DecisionTreeClassifier(max_depth=3, random_state=42).fit(X_train, y_train)
print("Accuracy:", accuracy_score(y_test, model.predict(X_test)))\n