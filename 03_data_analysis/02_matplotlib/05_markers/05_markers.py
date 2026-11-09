"""Practice: Markers.
Use markers to make individual data points visible and easier to compare.
Reference: https://www.w3schools.com/python/matplotlib_markers.asp
"""

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [3, 8, 5, 11, 7]

plt.plot(
    x, y,
    marker="o",
    markersize=10,
    markerfacecolor="orange",
    markeredgecolor="black",
    linestyle="--",
    label="Scores"
)
plt.title("Markers Example")
plt.xlabel("Test")
plt.ylabel("Score")
plt.legend()
plt.show()
