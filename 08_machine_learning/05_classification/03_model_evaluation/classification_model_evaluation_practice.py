"""\nClassification Model Evaluation\n\nLearning goal: Evaluate classifiers using confusion matrix, precision, recall, F1-score, and ROC-AUC where appropriate.\nRun with: python "Classification_Model_Evaluation_practice.py"\n"""\n\nfrom sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, roc_auc_score

X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=3000)).fit(X_train, y_train)
pred = model.predict(X_test)
print("Confusion matrix:\n", confusion_matrix(y_test, pred))
print(classification_report(y_test, pred))
print("ROC-AUC:", roc_auc_score(y_test, model.predict_proba(X_test)[:, 1]))\n