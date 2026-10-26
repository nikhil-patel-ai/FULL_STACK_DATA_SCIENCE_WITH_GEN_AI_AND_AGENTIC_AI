import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(r"C:\Users\Nikhil\Full Stack Data Science\MACHINE LEARNING\01Regression\Polynomial_regression\emp_sal.csv")

x = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(x,y)

plt.scatter(x, y, color = 'red')
plt.plot(x, lin_reg.predict(x), color = 'blue')
plt.title('Linear regression graph')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()


from sklearn.preprocessing import PolynomialFeatures
poly_reg =PolynomialFeatures(degree=6)
x_poly = poly_reg.fit_transform(x)
poly_reg.fit(x_poly,y)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(x_poly, y)    

plt.scatter(x, y, color = 'red')
plt.plot(x, lin_reg_2.predict(poly_reg.fit_transform(x)), color = 'blue')
plt.title('level or Salary(Polynomial Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()


lin_model_pred = lin_reg.predict([[6.5]])
lin_model_pred

poly_model_pred = lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))
poly_model_pred


# svr model

from sklearn.svm import SVR
svr_reg = SVR(kernel = 'poly', degree=4, gamma='auto')
svr_reg.fit(x,y)

svr_model_pred = svr_reg.predict([[6.5]])
svr_model_pred

print(svr_reg.get_params())


# KNN Regressor
from sklearn.neighbors import KNeighborsRegressor
knn_reg = KNeighborsRegressor(n_neighbors=2,p=2,weights='uniform',algorithm='auto')
knn_reg.fit(x, y)

# Prediction
knn_reg_pred = knn_reg.predict([[6.5]])
knn_reg_pred


# Decission Tree Regression
from sklearn.tree import DecisionTreeRegressor
dt_reg = DecisionTreeRegressor(criterion="absolute_error",splitter="random", max_depth=3)
dt_reg.fit(x, y)

# pred
dt_reg_pred = dt_reg.predict([[6.5]])
dt_reg_pred



# Random Forest
from sklearn.ensemble import RandomForestRegressor
rf_reg = RandomForestRegressor(n_estimators=45,random_state=0,max_depth=None,max_samples=5,min_samples_leaf=2)
rf_reg.fit(x, y)

rf_reg_pred = rf_reg.predict([[6.5]])
rf_reg_pred


# XGboost regressor
import xgboost as xg
xgb_r = xg.XGBRegressor(objective='reg:linear',n_estimators=4)
xgb_r.fit(x, y)
xgb_reg_pred = xgb_r.predict([[6.5]])
xgb_reg_pred




















































