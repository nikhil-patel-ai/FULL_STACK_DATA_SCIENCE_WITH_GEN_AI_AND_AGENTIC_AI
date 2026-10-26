# Markers

> Use markers to make individual data points visible and easier to compare.

**Reference:** [Markers — W3Schools](https://www.w3schools.com/python/matplotlib_markers.asp)

## Headings and one-line explanations

### Markers
Markers are symbols drawn at individual data points.

### Format Strings fmt
A format string can combine marker, line, and color shortcuts.

### Marker Reference
Matplotlib supports marker shapes such as circles, squares, triangles, and crosses.

### Marker Size
The `markersize` or `ms` argument controls marker size.

### Marker Color
The `markerfacecolor` and `markeredgecolor` arguments control marker fill and outline.

### Format Strings in `plt.plot()`
Format strings provide a compact way to specify line and marker styles.

## Example

This example is included in both the notebook and the Python script.

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [3, 8, 5, 11, 7]

plt.plot(
    x, y,
    marker="o",
    markersize=10,
    markerfacecolor="orange",
    markeredgecolor="black",
    linestyle="--",
    label="Scores"
)
plt.title("Markers Example")
plt.xlabel("Test")
plt.ylabel("Score")
plt.legend()
plt.show()
```

## Files

- `05_markers.ipynb` — run the example interactively.
- `05_markers.py` — run the same example as a Python script.
- `README.md` — topic summary and one-line explanations for headings.

## Practice task

Modify the sample data and at least one chart property, then explain how the visualization changes.
