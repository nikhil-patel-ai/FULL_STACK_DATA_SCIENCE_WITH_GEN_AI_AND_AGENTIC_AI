from sklearn.linear_model import LinearRegression
import pandas as pd
import pickle

# Load dataset
data = pd.read_csv(
    r"C:\Users\Nikhil\Full Stack Data Science\MACHINE LEARNING\01Regression\Salary_Data.csv"
)

# Input and output
X = data[["YearsExperience"]]
y = data["Salary"]

# Train model
regressor = LinearRegression()
regressor.fit(X, y)

# Save model
filename = "linear_regression_model.pkl"

with open(filename, "wb") as file:
    pickle.dump(regressor, file)

print("Model saved successfully.")