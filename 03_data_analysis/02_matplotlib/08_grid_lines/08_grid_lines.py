"""Practice: Grid Lines.
Add grid lines to help readers estimate values from a chart.
Reference: https://www.w3schools.com/python/matplotlib_grid.asp
"""

import matplotlib.pyplot as plt

months = [1, 2, 3, 4, 5]
sales = [12, 17, 14, 21, 25]

plt.plot(months, sales, marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(axis="y", color="gray", linestyle="--", linewidth=0.6)
plt.show()
