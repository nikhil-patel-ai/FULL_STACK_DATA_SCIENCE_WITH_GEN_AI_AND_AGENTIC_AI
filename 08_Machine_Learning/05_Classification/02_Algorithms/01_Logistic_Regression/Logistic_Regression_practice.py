"""\nLogistic Regression\n\nLearning goal: Train a logistic regression classifier with scaled features.\nRun with: python "Logistic_Regression_practice.py"\n"""\n\nfrom sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=3000)).fit(X_train, y_train)
print(classification_report(y_test, model.predict(X_test)))\n