# Matplotlib Introduction

> Understand what Matplotlib is and why it is used to create visualizations in Python.

**Reference:** [Matplotlib Introduction — W3Schools](https://www.w3schools.com/python/matplotlib_intro.asp)

## Headings and one-line explanations

### What is Matplotlib?
Matplotlib is a Python library for creating charts and visualizations.

### Where is the Matplotlib Codebase?
The source code is maintained in the Matplotlib GitHub repository.

## Example

This example is included in both the notebook and the Python script.

```python
import matplotlib
import matplotlib.pyplot as plt

print("Matplotlib version:", matplotlib.__version__)

x = [1, 2, 3, 4]
y = [10, 15, 13, 20]

plt.plot(x, y)
plt.title("My First Matplotlib Plot")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()
```

## Files

- `01_matplotlib_intro.ipynb` — run the example interactively.
- `01_matplotlib_intro.py` — run the same example as a Python script.
- `README.md` — topic summary and one-line explanations for headings.

## Practice task

Modify the sample data and at least one chart property, then explain how the visualization changes.
