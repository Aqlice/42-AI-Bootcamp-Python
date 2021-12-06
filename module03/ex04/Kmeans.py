import numpy as np
from sklearn.cluster import KMeans

class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid # number of centroids
        self.max_iter = max_iter # number of max iterations to update the centroids
        self.centroids = [] # values of the centroids

    def fit(self, X):
        self.kmeans = KMeans(init='random',
                             n_clusters=self.ncentroid,
                             n_init=self.max_iter)
        self.kmeans.fit(X)
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        Args:
          X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Returns:
          None.
        Raises:
          This function should not raise any Exception.
        """
    def predict(self, X):
        self.cluster_labels = self.kmeans.predict(X)
        self.centroids = self.kmeans.cluster_centers_
        return self.centroids
        """
        Predict from wich cluster each datapoint belongs to.
        Args:
          X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Returns:
          the prediction has a numpy.ndarray, a vector of dimension m * 1.
        Raises:
11
   This function should not raise any Exception.
"""
if __name__ == "__main__":
  X = np.genfromtxt("census.csv", delimiter=",", skip_header=0)
  X = X[:, 1:]
  k = KmeansClustering(ncentroid=4, max_iter=40)
  k.fit(X)
  k.predict(X)
  print(k.centroids)
  print(k.cluster_labels)