# PCA (Principal Component Analysis)

This folder contains two visual summaries. Together, they introduce PCA,
explain its main terms, outline a practical workflow, and show an example of
reducing Iris dataset measurements to two dimensions.

## PCA in simple terms

Principal Component Analysis (PCA) takes measurements that may be related and
creates new directions called **principal components**:

- **PC1** points along the direction where the observations vary most.
- **PC2** is at a right angle to PC1 and captures the most remaining
  variation.
- Each later component is perpendicular to the earlier components and
  captures less variance than its predecessor.

Each component is a weighted combination of the original features. Projecting
observations onto only the first few components can reduce the number of
columns in a dataset, while retaining much (but not necessarily all) of its
variation.

## Terms explained in `PCA1.png`

- **Principal components:** New axes formed from linear combinations of the
  original features. The first axes are ordered by the amount of variance they
  capture.
- **Variance:** A measure of how spread out values are. PCA chooses directions
  with high variance first.
- **Orthogonality:** Component directions meet at right angles. For PCA on
  centered data, the component scores are uncorrelated in the data used to fit
  the transformation.

The diagram presents PCA as a dimensionality-reduction method: it represents
high-dimensional data in fewer dimensions while trying to preserve important
variation. It also introduces the idea that this can reduce redundant
information.

## Workflow explained in `PCA2.png`

The image lists these steps:

1. **Standardize features:** Make features have zero mean and unit variance
   when their units or scales differ. Scaling is a choice to make for the
   dataset, not a compulsory step in every PCA use.
2. **Calculate the covariance matrix:** Summarize each feature's variance and
   how pairs of features vary together.
3. **Find eigenvalues and eigenvectors:** Eigenvectors give component
   directions; eigenvalues give the variance along those directions.
4. **Select components:** Keep the directions with the largest eigenvalues,
   according to the desired dimension and acceptable information loss.
5. **Project the data:** Express each observation in the selected component
   coordinate system.

The image also lists common applications:

- **Dimensionality reduction:** Use fewer values to represent each
  observation.
- **Data visualization:** Plot high-dimensional observations in two or three
  dimensions.
- **Noise reduction:** Removing low-variance directions may remove noise, but
  low variance alone does not prove a feature is unimportant.

## Iris example shown in the image

The code illustration uses scikit-learn and the Iris dataset. It loads the
four measurements for each flower, creates a PCA model with two components,
transforms the measurements into two coordinates, and plots component 1
against component 2. The flower class labels color the points in the plot.
This is a way to visualize a four-feature dataset in two dimensions; it is
not a complete classification model.

The code is shown inside an image; this folder does not contain a runnable
Python script. For the handwritten two-feature calculation, see the
[parent folder's detailed explanation](..).
