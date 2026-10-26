# Getting Started

> Install Matplotlib, import it into Python, and check the installed version.

**Reference:** [Getting Started — W3Schools](https://www.w3schools.com/python/matplotlib_getting_started.asp)

## Headings and one-line explanations

### Installation of Matplotlib
Install the library with pip before importing it.

### Import Matplotlib
Import pyplot using the common alias `plt` to create charts.

### Checking Matplotlib Version
Print `matplotlib.__version__` to see which version is installed.

## Example

This example is included in both the notebook and the Python script.

```python
import matplotlib
import matplotlib.pyplot as plt

print("Matplotlib version:", matplotlib.__version__)

plt.plot([1, 2, 3], [2, 4, 6])
plt.title("Installation Check")
plt.show()
```

## Files

- `02_getting_started.ipynb` — run the example interactively.
- `02_getting_started.py` — run the same example as a Python script.
- `README.md` — topic summary and one-line explanations for headings.

## Practice task

Modify the sample data and at least one chart property, then explain how the visualization changes.
