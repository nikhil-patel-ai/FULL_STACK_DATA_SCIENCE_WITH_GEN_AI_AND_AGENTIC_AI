"""Practice: Line Style.
Customize plot line patterns, colors, and widths for clearer charts.
Reference: https://www.w3schools.com/python/matplotlib_line.asp
"""

import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
plt.plot(x, [2, 5, 3, 7], linestyle="--", color="purple", linewidth=3, label="Dashed")
plt.plot(x, [1, 3, 4, 6], linestyle=":", color="green", linewidth=2, label="Dotted")
plt.title("Line Styles and Widths")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
