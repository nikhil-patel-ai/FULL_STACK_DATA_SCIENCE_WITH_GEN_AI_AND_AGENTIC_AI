# Plotting

> Learn how x and y coordinates are paired and displayed in a plot.

**Reference:** [Plotting — W3Schools](https://www.w3schools.com/python/matplotlib_plotting.asp)

## Headings and one-line explanations

### Plotting
A plot displays relationships between data points on coordinate axes.

### Plotting x and y points
Each x value is paired with the y value at the same position.

### Default X-Points
If x values are omitted, Matplotlib uses point positions such as 0, 1, 2, and so on.

## Example

This example is included in both the notebook and the Python script.

```python
import matplotlib.pyplot as plt

# Explicit x and y values
plt.plot([1, 2, 3, 4], [10, 15, 12, 20], marker="o", label="Measured")
# A second series can be added to the same axes
plt.plot([1, 2, 3, 4], [8, 11, 14, 17], label="Comparison")
plt.title("Two Data Series")
plt.xlabel("Observation")
plt.ylabel("Value")
plt.legend()
plt.show()
```

## Files

- `04_plotting.ipynb` — run the example interactively.
- `04_plotting.py` — run the same example as a Python script.
- `README.md` — topic summary and one-line explanations for headings.

## Practice task

Modify the sample data and at least one chart property, then explain how the visualization changes.
