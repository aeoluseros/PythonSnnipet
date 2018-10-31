# SVD (Singular Value Decomposition) is a popular implementation of PCA
# PCA is really useful for things like image compression and facial recognition
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import pylab as pl
from itertools import cycle

iris = load_iris()

numSamples, numFeatures = iris.data.shape
print(numSamples)
print(numFeatures)
print(list(iris.target_names))

X = iris.data
pca = PCA(n_components=2, whiten=True).fit(X) # A whitening transformation or sphering transformation is a linear transformation that transforms a vector of random variables with a known covariance matrix into a set of new variables whose covariance is the identity matrix, meaning that they are uncorrelated and each have variance 1. The transformation is called "whitening" because it changes the input vector into a white noise vector.
# https://theclevermachine.wordpress.com/tag/principal-components-analysis-pca/
X_pca = pca.transform(X)

# What we have done is distill our 4D data set down to 2D, by projecting it down to two orthogonal 4D vectors that make up the basis of our new 2D projection. We can see what those 4D vectors are, although it's not something you can really wrap your head around:
print(pca.components_)

# see how much information we've managed to preserve:
print(pca.explained_variance_ratio_)
print(sum(pca.explained_variance_ratio_))

from pylab import *

colors = cycle('rgb')
target_ids = range(len(iris.target_names))
pl.figure()  #It is not always necessary because a figure is implicitly created when you create a scatter plot;
for i, c, label in zip(target_ids, colors, iris.target_names):
    pl.scatter(X_pca[iris.target == i, 0], X_pca[iris.target == i, 1], c=c, label=label)
pl.legend()
pl.show()


### Note:
# About pl.figure(): however, in the case you have shown, the figure is being created explicitly using plt.figure so that the figure will be a specific size rather than the default size.
plt.figure(figsize=(10,8))

plt.scatter(df['attacker_size'][df['year'] == 298],
        # attacker size in year 298 as the y axis
        df['defender_size'][df['year'] == 298],
        # the marker as
        marker='x',
        # the color
        color='b',
        # the alpha
        alpha=0.7,
        # with size
        s = 124,
        # labelled this
        label='Year 298')

# The other option would be to use gcf to get the current figure after creating the scatter plot and set the figure size retrospectively:  plt.gcf().set_size_inches(10, 8)



