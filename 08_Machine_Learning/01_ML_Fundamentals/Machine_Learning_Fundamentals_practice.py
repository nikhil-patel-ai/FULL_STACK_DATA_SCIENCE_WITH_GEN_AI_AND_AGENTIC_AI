"""
Machine Learning Fundamentals

Goal: Understand the basic ML workflow and the difference between supervised and unsupervised learning.

Run from this folder with:
    python "Machine_Learning_Fundamentals_practice.py"

This is a learning example. Review the code and dependencies before using it in production.
"""

# A tiny supervised-learning example: predict a numeric value from one feature.
# Install if needed: pip install scikit-learn
from sklearn.linear_model import LinearRegression

X = [[1], [2], [3], [4], [5]]  # feature values
y = [2, 4, 6, 8, 10]            # target values

model = LinearRegression()
model.fit(X, y)

print("Prediction for X=6:", model.predict([[6]])[0])
print("Learned coefficient:", model.coef_[0])
print("Learned intercept:", model.intercept_)
