"""\nSupport Vector Machines (SVM)\n\nLearning goal: Scale features and train a support vector classifier.\nRun with: python "Support_Vector_Machines_SVM_practice.py"\n"""\n\nfrom sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report

data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.25, random_state=42, stratify=data.target)
model = make_pipeline(StandardScaler(), SVC(kernel="rbf", C=1.0)).fit(X_train, y_train)
print(classification_report(y_test, model.predict(X_test), target_names=data.target_names))\n