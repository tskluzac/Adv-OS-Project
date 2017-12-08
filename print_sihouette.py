#Using the data from kmean_sihouette.py to plot sihouette change with clustering number change.

from __future__ import print_function

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import json
import time

print(__doc__)

extension_dict = {}
sentence_weight = 6

def modify_data(inter):
    # print("===============" + str(len(inter)) + "========================" + str(len(inter[0])))
    for i in range(0, len(inter[0])):
        if i == 0:
            count = 0
            for j in range(0, len(inter)):
                if inter[j][i] not in extension_dict:
                    extension_dict[inter[j][i]] = count
                    count += 1
                inter[j][i] = extension_dict[inter[j][i]]
        elif i == 1:
            for j in range(0, len(inter)):
                #print("+++++++++++++++++++" + str(j) + "+++++++++++++++++++++++" + str(i))
                if inter[j][i] != 0:
                    inter[j][i] = np.log2(inter[j][i])
        elif i == 2:
            for j in range(0, len(inter)):
                if inter[j][i] == True:
                    inter[j][i] = sentence_weight
                else:
                    inter[j][i] = 0
    return inter


def get_data(filename):
    with open('kmean_sihouette.json') as json_data:
        data = json.load(json_data)
        # print(data)
    data = modify_data(data)

    for i in range(0, len(data)):
        if data[i][0] not in extension_dict:
            extension_dict[data[i][0]] = 1;
    print(len(extension_dict.keys()))

    data_ext_label = []
    for i in range(0, len(data)):
            data_ext_label += [data[i][0:1]]

    data_part = []
    for i in range(0, len(data)):
        data_part += [data[i][1:3]]
    return data_part


def easy_print(neighbors, silhouette_list):
    plt.plot(neighbors, silhouette_list)
    plt.xlabel('Number of Clusters K')
    plt.ylabel('silhouette')
    plt.show()
# Generating the sample data from make_blobs
# This particular setting has one distinct cluster and 3 clusters placed close
# together.
X, y = make_blobs(n_samples=500,
                  n_features=2,
                  centers=4,
                  cluster_std=1,
                  center_box=(-10.0, 10.0),
                  shuffle=True,
                  random_state=1)  # For reproducibility

with open('kmean_sihouette.json') as json_data:
        data = json.load(json_data)

print(data[0][0])
range_n_clusters = []
silhouette = []
labels = []
for i in range(0, len(data)):
    range_n_clusters += [data[i][0]]
    silhouette += [data[i][1]]
    labels += [data[i][4]]

X = np.asarray(get_data('data.json'))
print(type(X))

# range_n_clusters = range(2,5)
result = []

easy_print(range_n_clusters, silhouette)
