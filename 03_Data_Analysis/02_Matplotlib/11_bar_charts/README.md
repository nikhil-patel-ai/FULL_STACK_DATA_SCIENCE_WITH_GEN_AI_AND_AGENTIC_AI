# Bars

> Use bar charts to compare values across discrete categories.

**Reference:** [Bars — W3Schools](https://www.w3schools.com/python/matplotlib_bars.asp)

## Headings and one-line explanations

### Creating Bars
`plt.bar()` creates vertical bars for category comparisons.

### Horizontal Bars
`plt.barh()` creates horizontal bars, useful for long category labels.

### Bar Color
The `color` argument sets the color of bars.

### Bar Width
The `width` argument controls the width of vertical bars.

## Example

This example is included in both the notebook and the Python script.

```python
import matplotlib.pyplot as plt

subjects = ["Python", "Math", "Statistics", "ML"]
hours = [8, 5, 6, 4]

plt.bar(subjects, hours, color="teal", width=0.6)
plt.title("Weekly Study Hours")
plt.xlabel("Subject")
plt.ylabel("Hours")
plt.show()

plt.figure()
plt.barh(subjects, hours, color="coral")
plt.title("Weekly Study Hours (Horizontal)")
plt.xlabel("Hours")
plt.ylabel("Subject")
plt.show()
```

## Files

- `11_bar_charts.ipynb` — run the example interactively.
- `11_bar_charts.py` — run the same example as a Python script.
- `README.md` — topic summary and one-line explanations for headings.

## Practice task

Modify the sample data and at least one chart property, then explain how the visualization changes.
