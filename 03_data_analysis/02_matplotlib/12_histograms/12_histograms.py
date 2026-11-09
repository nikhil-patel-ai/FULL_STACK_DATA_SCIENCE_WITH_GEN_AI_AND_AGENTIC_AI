"""Practice: Histograms.
Use histograms to understand how numerical observations are distributed across intervals.
Reference: https://www.w3schools.com/python/matplotlib_histograms.asp
"""

import matplotlib.pyplot as plt

exam_scores = [42, 55, 58, 61, 62, 65, 68, 70, 72, 72, 75, 78, 81, 85, 90, 92]

plt.hist(exam_scores, bins=5, edgecolor="black")
plt.title("Distribution of Exam Scores")
plt.xlabel("Score range")
plt.ylabel("Number of students")
plt.show()
