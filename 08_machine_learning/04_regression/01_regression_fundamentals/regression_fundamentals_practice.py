"""\nRegression Fundamentals\n\nLearning goal: Understand regression, features, target values, fitting, and prediction.\nRun with: python "Regression_Fundamentals_practice.py"\n"""\n\nimport numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 5, 8, 10])
model = LinearRegression().fit(X, y)
print("Coefficient:", model.coef_[0])
print("Intercept:", model.intercept_)
print("Prediction for X=6:", model.predict([[6]])[0])\n