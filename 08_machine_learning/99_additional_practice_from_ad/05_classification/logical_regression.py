import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

# Import dataset
dataset = pd.read_csv(r"C:\Users\Nikhil\Full Stack Data Science\MACHINE LEARNING\05_classification\logit classification.csv")

# split with IV and DV
x = dataset.iloc[:,[2, 3]].values
y = dataset.iloc[:, -1].values

# 80-10 train test split
from sklearn.model_selection import train_test_split
x_train, x_test,y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# Scale the data 
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

# Train the model 
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)

# confusion matrix now
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)


# This is to get the model accuracy
from sklearn.metrics import accuracy_score
ac = accuracy_score(y_test, y_pred)
print(ac)


# This is to get the Classification Report
from sklearn.metrics import classification_report
cr = classification_report(y_test, y_pred) 
cr

bias = classification_report(x_test, y_test)
bias
































