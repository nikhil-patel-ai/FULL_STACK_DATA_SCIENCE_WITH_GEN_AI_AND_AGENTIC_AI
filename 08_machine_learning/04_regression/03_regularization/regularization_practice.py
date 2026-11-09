"""\nRegularization\n\nLearning goal: Compare Ridge and Lasso to understand how regularization penalizes large coefficients.\nRun with: python "Regularization_practice.py"\n"""\n\nfrom sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge, Lasso
from sklearn.metrics import mean_squared_error

X, y = make_regression(n_samples=180, n_features=8, noise=15, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
for name, estimator in [("Ridge", Ridge(alpha=1.0)), ("Lasso", Lasso(alpha=0.1, max_iter=10000))]:
    model = make_pipeline(StandardScaler(), estimator).fit(X_train, y_train)
    print(name, "MSE:", round(mean_squared_error(y_test, model.predict(X_test)), 2))\n