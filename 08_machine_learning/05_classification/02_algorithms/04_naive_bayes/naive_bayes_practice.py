"""\nNaive Bayes\n\nLearning goal: Train a Gaussian Naive Bayes classifier on a small standard dataset.\nRun with: python "Naive_Bayes_practice.py"\n"""\n\nfrom sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
model = GaussianNB().fit(X_train, y_train)
print("Accuracy:", accuracy_score(y_test, model.predict(X_test)))\n