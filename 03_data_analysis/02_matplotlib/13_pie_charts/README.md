# Pie Charts

> Use pie charts to show how categories contribute to a whole.

**Reference:** [Pie Charts — W3Schools](https://www.w3schools.com/python/matplotlib_pie_charts.asp)

## Headings and one-line explanations

### Creating Pie Charts
`plt.pie()` displays values as proportional slices of a circle.

### Labels
The `labels` argument names each slice.

### Start Angle
The `startangle` argument rotates the chart to choose where the first slice begins.

### Explode
The `explode` argument offsets selected slices from the center.

### Shadow
Set `shadow=True` to add a shadow behind the pie chart.

### Colors
The `colors` argument assigns colors to slices.

### Legend
A legend identifies the categories represented by the slices.

### Legend With Header
Use `plt.legend(title=...)` to add a heading to the legend.

## Example

This example is included in both the notebook and the Python script.

```python
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
```

## Files

- `13_pie_charts.ipynb` — run the example interactively.
- `13_pie_charts.py` — run the same example as a Python script.
- `README.md` — topic summary and one-line explanations for headings.

## Practice task

Modify the sample data and at least one chart property, then explain how the visualization changes.
