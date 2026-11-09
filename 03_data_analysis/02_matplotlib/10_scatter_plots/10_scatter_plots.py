"""Practice: Scatter Plots.
Use scatter plots to examine relationships between two numeric variables.
Reference: https://www.w3schools.com/python/matplotlib_scatter.asp
"""

import matplotlib.pyplot as plt

study_hours = [1, 2, 3, 4, 5, 6]
scores = [45, 50, 58, 65, 73, 88]
sizes = [40, 70, 90, 110, 140, 180]

plt.scatter(study_hours, scores, s=sizes, c=scores, cmap="viridis", alpha=0.8)
plt.colorbar(label="Score")
plt.title("Study Hours and Scores")
plt.xlabel("Study hours")
plt.ylabel("Score")
plt.show()
