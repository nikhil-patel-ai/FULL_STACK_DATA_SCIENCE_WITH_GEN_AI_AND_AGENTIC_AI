"""Practice: Subplots.
Place multiple charts in one figure to compare related datasets.
Reference: https://www.w3schools.com/python/matplotlib_subplot.asp
"""

import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].plot(x, [2, 4, 6, 8], marker="o")
axes[0].set_title("Increasing")
axes[0].set_xlabel("X")
axes[0].set_ylabel("Y")

axes[1].bar(["A", "B", "C", "D"], [5, 3, 7, 4])
axes[1].set_title("Category Values")

fig.suptitle("Two Charts in One Figure")
fig.tight_layout()
plt.show()
