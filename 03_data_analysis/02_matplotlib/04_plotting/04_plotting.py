"""Practice: Plotting.
Learn how x and y coordinates are paired and displayed in a plot.
Reference: https://www.w3schools.com/python/matplotlib_plotting.asp
"""

import matplotlib.pyplot as plt

# Explicit x and y values
plt.plot([1, 2, 3, 4], [10, 15, 12, 20], marker="o", label="Measured")
# A second series can be added to the same axes
plt.plot([1, 2, 3, 4], [8, 11, 14, 17], label="Comparison")
plt.title("Two Data Series")
plt.xlabel("Observation")
plt.ylabel("Value")
plt.legend()
plt.show()
