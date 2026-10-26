"""Practice: Matplotlib Introduction.
Understand what Matplotlib is and why it is used to create visualizations in Python.
Reference: https://www.w3schools.com/python/matplotlib_intro.asp
"""

import matplotlib
import matplotlib.pyplot as plt

print("Matplotlib version:", matplotlib.__version__)

x = [1, 2, 3, 4]
y = [10, 15, 13, 20]

plt.plot(x, y)
plt.title("My First Matplotlib Plot")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()
