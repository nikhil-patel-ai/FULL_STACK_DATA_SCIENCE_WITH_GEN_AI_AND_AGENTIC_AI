"""Practice: Labels and Title.
Add a title and axis labels so readers understand what a chart represents.
Reference: https://www.w3schools.com/python/matplotlib_labels.asp
"""

import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5]
scores = [45, 52, 61, 70, 82]

plt.plot(hours, scores, marker="o")
plt.title("Study Time vs Score", loc="left", fontsize=15, fontweight="bold")
plt.xlabel("Study hours", fontsize=12)
plt.ylabel("Score (%)", fontsize=12)
plt.show()
