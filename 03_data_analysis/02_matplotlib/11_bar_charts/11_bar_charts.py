"""Practice: Bars.
Use bar charts to compare values across discrete categories.
Reference: https://www.w3schools.com/python/matplotlib_bars.asp
"""

import matplotlib.pyplot as plt

subjects = ["Python", "Math", "Statistics", "ML"]
hours = [8, 5, 6, 4]

plt.bar(subjects, hours, color="teal", width=0.6)
plt.title("Weekly Study Hours")
plt.xlabel("Subject")
plt.ylabel("Hours")
plt.show()

plt.figure()
plt.barh(subjects, hours, color="coral")
plt.title("Weekly Study Hours (Horizontal)")
plt.xlabel("Hours")
plt.ylabel("Subject")
plt.show()
