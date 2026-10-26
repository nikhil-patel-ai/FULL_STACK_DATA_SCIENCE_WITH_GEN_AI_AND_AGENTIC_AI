# Histograms

> Use histograms to understand how numerical observations are distributed across intervals.

**Reference:** [Histograms — W3Schools](https://www.w3schools.com/python/matplotlib_histograms.asp)

## Headings and one-line explanations

### Histogram
A histogram groups numeric observations into bins and displays their frequencies.

### Create Histogram
Use `plt.hist()` to divide values into bins and count observations in each bin.

## Example

This example is included in both the notebook and the Python script.

```python
import matplotlib.pyplot as plt

exam_scores = [42, 55, 58, 61, 62, 65, 68, 70, 72, 72, 75, 78, 81, 85, 90, 92]

plt.hist(exam_scores, bins=5, edgecolor="black")
plt.title("Distribution of Exam Scores")
plt.xlabel("Score range")
plt.ylabel("Number of students")
plt.show()
```

## Files

- `12_histograms.ipynb` — run the example interactively.
- `12_histograms.py` — run the same example as a Python script.
- `README.md` — topic summary and one-line explanations for headings.

## Practice task

Modify the sample data and at least one chart property, then explain how the visualization changes.
