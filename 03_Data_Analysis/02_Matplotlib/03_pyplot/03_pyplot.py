"""Practice: Pyplot.
Use pyplot functions to create and customize figures and plots.
Reference: https://www.w3schools.com/python/matplotlib_pyplot.asp
"""

import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [5, 7, 4, 8]

plt.plot(x, y, "o")
plt.title("Pyplot Points")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
