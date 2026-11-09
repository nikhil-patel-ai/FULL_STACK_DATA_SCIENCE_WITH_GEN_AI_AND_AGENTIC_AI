"""Practice: Getting Started.
Install Matplotlib, import it into Python, and check the installed version.
Reference: https://www.w3schools.com/python/matplotlib_getting_started.asp
"""

import matplotlib
import matplotlib.pyplot as plt

print("Matplotlib version:", matplotlib.__version__)

plt.plot([1, 2, 3], [2, 4, 6])
plt.title("Installation Check")
plt.show()
