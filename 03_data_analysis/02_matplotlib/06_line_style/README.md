# Line Style

> Customize plot line patterns, colors, and widths for clearer charts.

**Reference:** [Line Style — W3Schools](https://www.w3schools.com/python/matplotlib_line.asp)

## Headings and one-line explanations

### Linestyle
The `linestyle` argument selects solid, dashed, dotted, or dash-dot lines.

### Shorter Syntax
Short format codes can specify line style and color compactly.

### Line Color
The `color` argument changes the line's color.

### Line Width
The `linewidth` or `lw` argument controls line thickness.

## Example

This example is included in both the notebook and the Python script.

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
plt.plot(x, [2, 5, 3, 7], linestyle="--", color="purple", linewidth=3, label="Dashed")
plt.plot(x, [1, 3, 4, 6], linestyle=":", color="green", linewidth=2, label="Dotted")
plt.title("Line Styles and Widths")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
```

## Files

- `06_line_style.ipynb` — run the example interactively.
- `06_line_style.py` — run the same example as a Python script.
- `README.md` — topic summary and one-line explanations for headings.

## Practice task

Modify the sample data and at least one chart property, then explain how the visualization changes.
