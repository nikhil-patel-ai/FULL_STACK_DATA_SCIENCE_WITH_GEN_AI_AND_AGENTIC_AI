"""\nK-Nearest Neighbors (KNN)\n\nLearning goal: Explore how the number of neighbors affects predictions.\nRun with: python "K_Nearest_Neighbors_KNN_practice.py"\n"""\n\nfrom sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
for k in [3, 5, 7]:
    model = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=k)).fit(X_train, y_train)
    print(f"k={k}: {accuracy_score(y_test, model.predict(X_test)):.3f}")\n