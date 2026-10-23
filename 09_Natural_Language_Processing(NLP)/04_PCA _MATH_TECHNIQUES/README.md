# Principal Component Analysis (PCA): Visual Notes Explained

This folder's images introduce PCA with a two-feature example. This guide
explains the ideas and calculations shown in the handwritten images, followed
by the summary and code diagram in the [`PCA`](PCA) subfolder.

## 1. The problem PCA solves

Each row of a dataset is an observation, and each column is a feature. When
features are related, observations may vary mostly along a shared direction.
PCA finds new axes that describe those directions:

- **PC1 (the first principal component)** points along the direction of
  greatest variation in the data.
- **PC2** is perpendicular to PC1 and captures the greatest variation left
  after PC1.
- Further components are also perpendicular to earlier components and are
  ordered by how much variation they capture.

The new axes are combinations of the original features. PCA does not simply
choose the most useful original columns. It changes the coordinate system,
then lets us keep fewer coordinates if that is appropriate.

### A picture-based intuition

The first handwritten drawings show a cloud of points on two axes. The points
follow a diagonal pattern: although each point has an X and Y coordinate, most
of their movement is in one direction. PCA aligns PC1 with that direction.
PC2 runs across it. If the point cloud is narrow across PC2, the data may be
represented reasonably well using PC1 alone.

Projecting onto fewer components saves dimensions, but also loses some
information. PCA describes directions of variation; it does not know which
variation is important to a particular prediction task.

## 2. The handwritten example data

The notes use ten observations with two measurements, X and Y:

| Observation | X | Y |
| ---: | ---: | ---: |
| 1 | 2.5 | 2.4 |
| 2 | 0.5 | 0.7 |
| 3 | 2.2 | 2.9 |
| 4 | 1.9 | 2.2 |
| 5 | 3.1 | 3.0 |
| 6 | 2.3 | 2.7 |
| 7 | 2.0 | 1.6 |
| 8 | 1.0 | 1.1 |
| 9 | 1.5 | 1.6 |
| 10 | 1.1 | 0.9 |

The means shown in the notes are:

- Mean of X: **1.81**
- Mean of Y: **1.91**

Before finding directions, PCA centers each feature by subtracting its mean.
For example, observation 1 becomes `(2.5 - 1.81, 2.4 - 1.91)`, or
`(0.69, 0.49)`. Centering moves the cloud so that each feature has mean zero;
it does not change the relative positions of the observations.

## 3. Covariance: how the measurements vary together

Covariance describes whether two features tend to move together:

- Positive covariance: above-average values of one tend to occur with
  above-average values of the other.
- Negative covariance: above-average values of one tend to occur with
  below-average values of the other.
- Covariance of a feature with itself is its variance.

For sample data, the covariance between X and Y is calculated as:

`cov(X, Y) = sum((X_i - mean(X)) * (Y_i - mean(Y))) / (n - 1)`

The denominator is `n - 1` because the notes calculate sample covariance for
the ten observations. They sum the centered products and divide by 9.

The resulting covariance matrix in the notes is approximately:

|  | X | Y |
| --- | ---: | ---: |
| **X** | 0.6165 | 0.6154 |
| **Y** | 0.6154 | 0.7165 |

The diagonal entries are the variances of X and Y. The off-diagonal entries
are their covariance. The positive value `0.6154` indicates that X and Y tend
to increase together in this example.

## 4. Eigenvalues and eigenvectors find the new axes

The next images show how the covariance matrix is used to find principal
components:

1. Find the **eigenvalues** of the covariance matrix. These give the variance
   captured along the corresponding component directions.
2. Find each matching **eigenvector**. Each eigenvector gives the direction of
   a component in the original X-Y coordinate system.
3. Sort the components from the largest eigenvalue to the smallest.

The notes form the characteristic equation `det(C - lambda I) = 0`, where
`C` is the covariance matrix, `lambda` is an eigenvalue, and `I` is the
identity matrix. For this example, the approximate eigenvalues shown are:

- Larger eigenvalue: **1.2840**
- Smaller eigenvalue: **0.0490**

The corresponding unit eigenvectors (component directions) are approximately:

- **PC1:** `(0.6778, 0.7351)` — the direction for the larger eigenvalue.
- **PC2:** `(0.7351, -0.6778)` — the direction for the smaller eigenvalue.

The vectors are perpendicular: their dot product is approximately zero. The
sign of an eigenvector can be flipped without changing the component, so a
diagram or software package may show the same direction with both signs
reversed.

## 5. Project observations onto the components

To get a component value for an observation:

1. Subtract the feature means, so the data is centered.
2. Take the dot product of the centered observation with the component's
   eigenvector.

Using observation 1, whose centered values are `(0.69, 0.49)`, gives
approximately:

- `PC1 = 0.6778 * 0.69 + 0.7351 * 0.49 = 0.828`
- `PC2 = 0.7351 * 0.69 - 0.6778 * 0.49 = 0.175`

These component scores are the observation's coordinates in the new PCA
coordinate system. Keeping only PC1 would represent each two-number
observation with one number, while discarding the PC2 direction.

## 6. How much information does each component retain?

The total variance is the sum of the eigenvalues:

`1.2840 + 0.0490 = 1.3330`

The fraction explained by a component is its eigenvalue divided by the total:

- PC1 explains approximately `1.2840 / 1.3330`, or **96.3%** of the variance.
- PC2 explains approximately `0.0490 / 1.3330`, or **3.7%**.

For this small example, using only PC1 preserves most of the measured
variation. Whether that is enough depends on what the data will be used for;
variance retained is not the same as task-specific usefulness.

## 7. Practical PCA workflow shown in the summary image

The PCA summary diagram shows this general workflow:

1. **Prepare the features.** Center them. Standardize to zero mean and unit
   variance when features use different units or scales.
2. **Calculate the covariance structure** (or use an equivalent numerical
   method).
3. **Find eigenvalues and eigenvectors** to identify component directions and
   their variances.
4. **Choose the number of components** to retain.
5. **Project the data** onto those components.
6. **Inspect or visualize** the transformed data.

The hand-worked example calculates covariance after centering the original
X and Y values; it does not show a separate unit-variance scaling step.
Standardization is not always appropriate. With very different feature
scales it is often important; with comparable units, it may not be needed.
Decide based on the measurements and goal.

The summary image lists dimensionality reduction, lower-dimensional data
visualization, and possible noise reduction as use cases. Noise reduction
requires care: a low-variance direction is not automatically irrelevant.

## 8. What the scikit-learn example image demonstrates

The `PCA2.png` diagram in the subfolder contains an illustrative Python
workflow using the Iris dataset:

1. Import `PCA` from `sklearn.decomposition`.
2. Load the Iris dataset and separate its feature matrix (`X`) and class
   labels (`y`).
3. Create a PCA model with `n_components=2`.
4. Fit PCA to `X` and transform it into two component values per flower.
5. Plot the first component against the second with a scatter plot, using the
   Iris class labels as colors.

This reduces the four Iris measurements to two coordinates for visualization.
The image is a code illustration, not a runnable script in this folder.

For a predictive evaluation, fit preprocessing and PCA using training data
only, then apply the same fitted transformations to validation or test data.
This avoids leaking information from evaluation data into training.

## Image inventory

- `1.PNG`–`7.PNG` — initial point-cloud drawings showing the original axes,
  the main direction of spread, and the idea of projecting observations onto
  component axes.
- `8.PNG`–`10.PNG` — the two-feature example data, feature means, and
  arithmetic used to calculate variances and covariance.
- `11.PNG`–`14.PNG` — the covariance matrix, characteristic equation,
  eigenvalues, eigenvectors, and resulting principal-component directions.
- [`PCA1.png`](PCA/PCA1.png) — a compact definition of PCA and the ideas of
  principal components, variance, and orthogonality.
- [`PCA2.png`](PCA/PCA2.png) — workflow, use cases, and the illustrative
  scikit-learn Iris example described above.

All the images are visual notes. There are no runnable Python scripts in this
folder.
