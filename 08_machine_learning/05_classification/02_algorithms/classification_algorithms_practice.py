"""\nClassification Algorithms\n\nLearning goal: Compare classifiers only after preparing a consistent train/test split and choosing suitable metrics.\nRun with: python "Classification_Algorithms_practice.py"\n"""\n\nfrom sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
models = {
    "Logistic Regression": make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)),
    "KNN": make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5)),
    "SVM": make_pipeline(StandardScaler(), SVC())
}
for name, model in models.items():
    model.fit(X_train, y_train)
    print(name, "accuracy:", round(accuracy_score(y_test, model.predict(X_test)), 3))\n