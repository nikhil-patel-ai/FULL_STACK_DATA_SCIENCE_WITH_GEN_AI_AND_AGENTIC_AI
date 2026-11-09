"""\nRegression Algorithms\n\nLearning goal: Practice linear and polynomial regression and compare predictions.\nRun with: python "Regression_Algorithms_practice.py"\n"""\n\nimport numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

X = np.arange(1, 8).reshape(-1, 1)
y = np.array([1, 4, 9, 16, 25, 36, 49])
model = make_pipeline(PolynomialFeatures(degree=2), LinearRegression())
model.fit(X, y)
print("Predictions:", model.predict([[2], [5], [8]]))\n