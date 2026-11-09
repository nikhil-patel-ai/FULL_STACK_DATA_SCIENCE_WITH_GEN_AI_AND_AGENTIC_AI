# Scatter Plots

> Use scatter plots to examine relationships between two numeric variables.

**Reference:** [Scatter Plots — W3Schools](https://www.w3schools.com/python/matplotlib_scatter.asp)

## Headings and one-line explanations

### Creating Scatter Plots
`plt.scatter()` draws each x-y pair as an individual point.

### Compare Plots
Plot multiple datasets with different colors to compare groups.

### Colors
The `color` or `c` argument controls point colors.

### Color Each Dot
Provide a sequence of colors or numeric values to vary point colors.

### ColorMap
A colormap maps numeric values to a range of colors.

### Size
The `s` argument controls marker area.

### Alpha
The `alpha` argument controls transparency and helps reveal overlapping points.

## Example

This example is included in both the notebook and the Python script.

```python
import matplotlib.pyplot as plt

study_hours = [1, 2, 3, 4, 5, 6]
scores = [45, 50, 58, 65, 73, 88]
sizes = [40, 70, 90, 110, 140, 180]

plt.scatter(study_hours, scores, s=sizes, c=scores, cmap="viridis", alpha=0.8)
plt.colorbar(label="Score")
plt.title("Study Hours and Scores")
plt.xlabel("Study hours")
plt.ylabel("Score")
plt.show()
```

## Files

- `10_scatter_plots.ipynb` — run the example interactively.
- `10_scatter_plots.py` — run the same example as a Python script.
- `README.md` — topic summary and one-line explanations for headings.

## Practice task

Modify the sample data and at least one chart property, then explain how the visualization changes.
