# This file is using kmean and validating with sihouette. The result and sihouette calculated will be saved in file kmean_sihouette.json.



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
    with open('data.json') as json_data:
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


X = np.asarray(get_data('data.json'))
print(type(X))
range_n_clusters = range(2,len(extension_dict.keys()))
# range_n_clusters = range(2,5)
result = []
label_result = []
for n_clusters in range_n_clusters:
    print(n_clusters)
    # Create a subplot with 1 row and 2 columns
    #fig, (ax1, ax2) = plt.subplots(1, 2)
    #fig.set_size_inches(18, 7)

    # The 1st subplot is the silhouette plot
    # The silhouette coefficient can range from -1, 1 but in this example all
    # lie within [-0.1, 1]
    #ax1.set_xlim([-0.1, 1])
    # The (n_clusters+1)*10 is for inserting blank space between silhouette
    # plots of individual clusters, to demarcate them clearly.
    #ax1.set_ylim([0, len(X) + (n_clusters + 1) * 10])

    # Initialize the clusterer with n_clusters value and a random generator
    # seed of 10 for reproducibility.
    start = time.clock()
    clusterer = KMeans(n_clusters=n_clusters, random_state=10)
    cluster_labels = clusterer.fit_predict(X)
    end = time.clock()
    time1 = end-start
    # The silhouette_score gives the average value for all the samples.
    # This gives a perspective into the density and separation of the formed
    # clusters
    start = time.clock()
    silhouette_avg = silhouette_score(X, cluster_labels)
    end = time.clock()
    time2 = end-start
    print("For n_clusters =", n_clusters,
          "The average silhouette_score is :", silhouette_avg)
    print("Time is: %f CPU seconds" % time1 + " Time is: %f CPU seconds" % time2)
    result += [[n_clusters, silhouette_avg, time1, time2, [cluster_labels.tolist()]]]
    label_result += [cluster_labels.tolist()]

with open('kmean_sihouette.json', 'w') as outfile:
    json.dump(result, outfile)