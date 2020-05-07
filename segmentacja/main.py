import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pylab import rcParams
# sklearn
import sklearn
from sklearn.cluster import KMeans
from sklearn.preprocessing import scale  # for scaling the data
import sklearn.metrics as sm  # for evaluating the model
from sklearn import datasets
from sklearn.metrics import confusion_matrix, classification_report

# data = np.loadtxt("segmentacja.txt")
from score_calc import calculate_wcc_and_bcc

INPUT_FILE_NAME = "segmentacja.txt"
OUTPUT_FILE_NAME = "segmentacja_o.txt"

with open(INPUT_FILE_NAME, 'r') as infile, \
        open(OUTPUT_FILE_NAME, 'w') as outfile:
    data = infile.read()
    data = data.replace("[", "")
    data = data.replace("]", "")
    outfile.write(data)

data = np.loadtxt("segmentacja_o.txt", delimiter=", ")

wcc_list = []
bcc_list = []

for i in range(2, 101):
    print("Iter", i)
    clustering = KMeans(n_clusters=i)
    clustering.fit(data)

    wcc, bcc = calculate_wcc_and_bcc(data, clustering.labels_)
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
