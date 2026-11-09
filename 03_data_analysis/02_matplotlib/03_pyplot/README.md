# Pyplot

> Use pyplot functions to create and customize figures and plots.

**Reference:** [Pyplot — W3Schools](https://www.w3schools.com/python/matplotlib_pyplot.asp)

## Headings and one-line explanations

### What is Pyplot?
Pyplot is Matplotlib's state-based interface for making charts with simple function calls.

### Plotting x and y points
Pass x-coordinates and y-coordinates to `plt.plot()` to draw data.

### The x-axis
The x-axis usually represents the independent variable or categories.

### The y-axis
The y-axis usually represents the measured values.

### Plotting Without Line
Use a format string such as `o` to show points without connecting lines.

## Example

This example is included in both the notebook and the Python script.

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [5, 7, 4, 8]

plt.plot(x, y, "o")
plt.title("Pyplot Points")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
```

## Files

- `03_pyplot.ipynb` — run the example interactively.
- `03_pyplot.py` — run the same example as a Python script.
- `README.md` — topic summary and one-line explanations for headings.

## Practice task

Modify the sample data and at least one chart property, then explain how the visualization changes.
