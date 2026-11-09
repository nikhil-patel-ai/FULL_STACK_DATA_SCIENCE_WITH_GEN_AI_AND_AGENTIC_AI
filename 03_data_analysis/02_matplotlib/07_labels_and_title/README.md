# Labels and Title

> Add a title and axis labels so readers understand what a chart represents.

**Reference:** [Labels and Title — W3Schools](https://www.w3schools.com/python/matplotlib_labels.asp)

## Headings and one-line explanations

### Create Labels for a Plot
Axis labels describe the information represented by each axis.

### Create a Title for a Plot
A title briefly communicates the chart's main subject.

### Set Font Properties for Title and Labels
Font properties control text size, family, weight, and color.

### Position the Title
The `loc` argument positions the title, for example left, center, or right.

## Example

This example is included in both the notebook and the Python script.

```python
import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5]
scores = [45, 52, 61, 70, 82]

plt.plot(hours, scores, marker="o")
plt.title("Study Time vs Score", loc="left", fontsize=15, fontweight="bold")
plt.xlabel("Study hours", fontsize=12)
plt.ylabel("Score (%)", fontsize=12)
plt.show()
```

## Files

- `07_labels_and_title.ipynb` — run the example interactively.
- `07_labels_and_title.py` — run the same example as a Python script.
- `README.md` — topic summary and one-line explanations for headings.

## Practice task

Modify the sample data and at least one chart property, then explain how the visualization changes.
