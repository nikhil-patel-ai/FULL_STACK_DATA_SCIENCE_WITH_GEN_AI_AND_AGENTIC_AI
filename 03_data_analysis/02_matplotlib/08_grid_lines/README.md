# Grid Lines

> Add grid lines to help readers estimate values from a chart.

**Reference:** [Grid Lines — W3Schools](https://www.w3schools.com/python/matplotlib_grid.asp)

## Headings and one-line explanations

### Add Grid Lines to a Plot
Call `plt.grid()` to display grid lines on the chart.

### Specify Which Grid Lines to Display
Choose `axis='x'`, `axis='y'`, or `axis='both'` to control the grid direction.

### Set Line Properties for the Grid
Style grid lines with options such as color, linestyle, and linewidth.

## Example

This example is included in both the notebook and the Python script.

```python
import matplotlib.pyplot as plt

months = [1, 2, 3, 4, 5]
sales = [12, 17, 14, 21, 25]

plt.plot(months, sales, marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(axis="y", color="gray", linestyle="--", linewidth=0.6)
plt.show()
```

## Files

- `08_grid_lines.ipynb` — run the example interactively.
- `08_grid_lines.py` — run the same example as a Python script.
- `README.md` — topic summary and one-line explanations for headings.

## Practice task

Modify the sample data and at least one chart property, then explain how the visualization changes.
