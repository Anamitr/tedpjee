import copy

import numpy as np
import matplotlib.pyplot as plt
import warnings

from score_calc import calculate_wcc_and_bcc

warnings.simplefilter("ignore", category=RuntimeWarning)

data = np.loadtxt("segmentacja_o.txt", delimiter=", ")


def calcualte_k_means(data, k):
    # Number of training data
    n = data.shape[0]
    # Number of features in the data
    c = data.shape[1]

    # Generate random centers, here we use sigma and mean to ensure it represent the whole data
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    centers = np.random.randn(k, c) * std + mean

    centers_old = np.zeros(centers.shape)  # to store old centers
    centers_new = copy.deepcopy(centers)  # Store new centers

    clusters = np.zeros(n)
    distances = np.zeros((n, k))

    error = np.linalg.norm(centers_new - centers_old)

    # When, after an update, the estimate of that center stays the same, exit loop
    MAX_ITER = 300
    iter = 0
    while error != 0 and iter < MAX_ITER:
        # Measure the distance to every center
        for i in range(k):
            distances[:, i] = np.linalg.norm(data - centers[i], axis=1)
        # Assign all training data to closest center
        clusters = np.argmin(distances, axis=1)

        centers_old = copy.deepcopy(centers_new)
        # Calculate mean for every cluster and update the center
        for i in range(k):
            centers_new[i] = np.mean(data[clusters == i], axis=0)
        error = np.linalg.norm(centers_new - centers_old)
        iter += 1

    return clusters


wcc_list = []
bcc_list = []

for k in range(2, 101):
    print("Iter", k)
    clustering_labels = calcualte_k_means(data, k)

    wcc, bcc = calculate_wcc_and_bcc(data, clustering_labels)
    wcc_list.append(wcc)
    bcc_list.append(bcc)

plt.plot(range(2, 101), wcc_list)
plt.xlabel("Num of clusters")
plt.ylabel("wc(C)")
plt.title("wc(C) per num of clusters")
plt.show()

plt.plot(range(2, 101), bcc_list)
plt.xlabel("Num of clusters")
plt.ylabel("bc(C)")
plt.title("bc(C) per num of clusters")
plt.show()
