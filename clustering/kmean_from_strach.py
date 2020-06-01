import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import style
import numpy as np
style.use('ggplot')

class K_Means:
    def __init__(self, k=2, tol=0.001, max_iter=300):
        self.k = k
        self.tol = tol
        self.max_iter = max_iter

    def fit(self, data):
        self.centroids = {}
        for i in range(self.k):
            self.centroids[i] = data[i]

        for i in range(self.max_iter):
            self.classifications = {}

            for i in range(self.k):
                self.classifications[i] = []

            for featureset in data:
                distances = [np.linalg.norm(featureset - self.centroids[centroid]) for centroid in self.centroids]
                classification = distances.index(min(distances))
                self.classifications[classification].append(featureset)

            prev_centroids = dict(self.centroids)

            for classification in self.classifications:
                self.centroids[classification] = np.average(self.classifications[classification], axis=0)

            optimized = True

            for c in self.centroids:
                original_centroid = prev_centroids[c]
                current_centroid = self.centroids[c]
                if np.sum((current_centroid-original_centroid)/original_centroid*100) > self.tol:
                    print(np.sum((current_centroid-original_centroid)/original_centroid*100))
                    optimized=False

                if optimized:
                    break

    def predict(self, data):
        distances = [np.linalg.norm(data-self.centroids[centroid]) for centroid in self.centroids]
        classification = distances.index(min(distances))
        return classification


X = np.array([[1,2,4],
              [1.5, 1.8, 4],
              [5, 8, 3.2],
              [8, 8, 2],
              [1, 0.6, 4],
              [9, 11,5]])

clf = K_Means()
clf.fit(X)
colors = ["g", "r", "c", "b", "k"]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for centroid in clf.centroids:
    ax.scatter(clf.centroids[centroid][0], clf.centroids[centroid][1], clf.centroids[centroid][2], marker="o", color="k", s=150, linewidths=5)

for classification in clf.classifications:
    color = colors[classification]
    for featureset in clf.classifications[classification]:
        ax.scatter(featureset[0], featureset[1], featureset[2], marker="x", color=color, s=150, linewidths=5)

unknowns = np.array([[1,3,1],
                     [8,9,1],
                     [0,3,1],
                     [5,4,1],
                     [6,4,1]])

for unknown in unknowns:
    classification = clf.predict(unknown)
    ax.scatter(unknown[0], unknown[1],unknown[2], marker="*", color=colors[classification], s=150, linewidths=5)

plt.show()












