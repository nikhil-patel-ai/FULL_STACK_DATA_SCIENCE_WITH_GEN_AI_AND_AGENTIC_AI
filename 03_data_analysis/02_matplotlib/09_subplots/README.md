# Subplots

> Place multiple charts in one figure to compare related datasets.

**Reference:** [Subplots — W3Schools](https://www.w3schools.com/python/matplotlib_subplot.asp)

## Headings and one-line explanations

### Display Multiple Plots
Subplots let you display multiple axes within one figure.

### The `subplot()` Function
`plt.subplot(rows, columns, index)` selects a position in a grid of plots.

### Title
Give each subplot its own title and use a figure-level title when needed.

### Super Title
`plt.suptitle()` adds one shared title above all subplots.

### Multiple Plots
Create more than one chart in a figure to compare patterns side by side.

## Example

This example is included in both the notebook and the Python script.

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].plot(x, [2, 4, 6, 8], marker="o")
axes[0].set_title("Increasing")
axes[0].set_xlabel("X")
axes[0].set_ylabel("Y")

axes[1].bar(["A", "B", "C", "D"], [5, 3, 7, 4])
axes[1].set_title("Category Values")

fig.suptitle("Two Charts in One Figure")
fig.tight_layout()
plt.show()
```

## Files

- `09_subplots.ipynb` — run the example interactively.
- `09_subplots.py` — run the same example as a Python script.
- `README.md` — topic summary and one-line explanations for headings.

## Practice task

Modify the sample data and at least one chart property, then explain how the visualization changes.
