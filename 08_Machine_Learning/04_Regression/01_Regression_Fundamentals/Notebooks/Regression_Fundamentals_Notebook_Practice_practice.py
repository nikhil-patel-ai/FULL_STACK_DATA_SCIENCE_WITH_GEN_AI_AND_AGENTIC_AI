"""\nRegression Fundamentals Notebook Practice\n\nLearning goal: Use the original notebooks in this folder as trainer material and start with a simple linear regression example.\nRun with: python "Regression_Fundamentals_Notebook_Practice_practice.py"\n"""\n\nfrom sklearn.linear_model import LinearRegression
X = [[1], [2], [3], [4]]
y = [2, 4, 6, 8]
model = LinearRegression().fit(X, y)
print("Prediction for 5:", model.predict([[5]])[0])\n