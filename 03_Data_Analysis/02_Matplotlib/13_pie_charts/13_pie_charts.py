"""Practice: Pie Charts.
Use pie charts to show how categories contribute to a whole.
Reference: https://www.w3schools.com/python/matplotlib_pie_charts.asp
"""

import matplotlib.pyplot as plt

labels = ["Python", "Statistics", "Math", "ML"]
hours = [8, 5, 4, 6]
explode = [0.08, 0, 0, 0]

plt.pie(
    hours,
    labels=labels,
    autopct="%1.1f%%",
    startangle=90,
    explode=explode,
    shadow=True
)
plt.title("Study Time by Subject")
plt.legend(title="Subjects", loc="best")
plt.show()
