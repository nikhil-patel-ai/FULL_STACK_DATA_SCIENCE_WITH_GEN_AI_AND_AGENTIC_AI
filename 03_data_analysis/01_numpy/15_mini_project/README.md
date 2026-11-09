# NumPy Mini Project

This notebook is a hands-on NumPy and Matplotlib project with two parts:

1. Convert an image into a NumPy array and display it.
2. Explore cricket player salary, games, and points data across the 2015-2024 seasons.

## Requirements

- Python 3.x
- Jupyter Notebook or VS Code with the Jupyter extension
- NumPy
- Matplotlib
- Pillow

Install the packages in the same Python environment used by the notebook:

```bash
python -m pip install numpy matplotlib pillow
```

## Topics Covered

- Importing NumPy, Matplotlib, and Pillow
- Opening an image with `PIL.Image`
- Converting an image to a NumPy array with `np.asarray()`
- Checking array types and shapes
- Building matrices from player data
- Performing element-wise arithmetic on arrays
- Calculating salary per game
- Mapping player and season names to array indexes
- Plotting one or more data series
- Customizing line styles, colors, markers, labels, legends, and tick labels

## Image to NumPy Array

The notebook opens an image and converts it into an array:

```python
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path

image_candidates = (
    Path("10_Images_to_Arrays/images.jpg"),
    Path("../10_Images_to_Arrays/images.jpg"),
)
image_path = next((path for path in image_candidates if path.is_file()), None)
if image_path is None:
    raise FileNotFoundError("Could not find 10_Images_to_Arrays/images.jpg.")
image = Image.open(image_path)
image_arr = np.asarray(image)

print(type(image))
print(image_arr.shape)

plt.imshow(image_arr)
plt.show()
```

Update the image path to match the image available in your workspace.

## Player Statistics Project

The proof of concept stores the following information for ten players:

- `Salary`: seasonal salary values
- `Games`: games played in each season
- `Points`: points earned in each season
- `Seasons`: season labels from 2015 through 2024

The data is organized into NumPy matrices, with one row per player and one column per season.

```python
Salary = np.array([...])
Games = np.array([...])
Points = np.array([...])
```

Element-wise operations can compare related values for each player and season:

```python
salary_per_game = np.divide(
    Salary,
    Games,
    out=np.full(Salary.shape, np.nan, dtype=float),
    where=Games != 0,
)
salary_per_game = np.round(salary_per_game, decimals=2)
```

Some player-season entries contain zero games. Those ratios are represented as
`NaN`, not as zero or infinity. Treat the embedded sports figures as sample
learning data; verify them against a trusted source before using them as facts.

## Visualization Examples

The notebook demonstrates how to:

- Plot a single player's salary trend
- Compare multiple players
- Plot games played for all players
- Add season labels to the x-axis
- Rotate tick labels
- Add markers, legends, and custom line styles

```python
plt.plot(
    Salary[0],
    color='green',
    linestyle='--',
    marker='d',
    label=Players[0],
)
plt.xticks(range(len(Seasons)), Seasons)
plt.xlabel('Season')
plt.ylabel('Salary (units as provided in sample data)')
plt.title('Salary by season')
plt.legend()
plt.show()
```

## Notebook

Open [`miniproj.ipynb`](miniproj.ipynb) to run the examples interactively.
