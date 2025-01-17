import numpy as np


def featureNormalize(X):
    """
        featureNormalization() Normalizes the features in X
        featureNormalization(X) returns a normalized version of X where
        the mean value of each feature is 0 and the standard deviation
        is 1. This is often a good preprocessing step to do when
        working with learning algorithms.
    """

    # You need to set these values correctly
    X_norm = X
    mu = np.zeros((1, len(X)))
    sigma = np.zeros((1, len(X)))

    # for each feature dimension, compute the mean
    # of the feature and subtract it from the dataset,
    # storing the mean value in mu. Next, compute the
    # standard deviation of each feature and divide
    # each feature by it's standard deviation, storing
    # the standard deviation in sigma.
    mu = np.mean(X)
    sigma = np.std(X)
    X_norm = np.divide(np.subtract(X, mu), sigma)

    return X_norm, mu, sigma
