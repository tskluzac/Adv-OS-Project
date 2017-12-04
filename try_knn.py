import numpy as np
from sklearn.cluster import  k_means
from sklearn.metrics import accuracy_score 
from sklearn.neighbors import KNeighborsClassifier
from sklearn import cross_validation
import time  
import matplotlib.pyplot as plt  
from mpl_toolkits.mplot3d import axes3d
import check_sentence
import get_extension
import get_size
import get_metadata
import os
import math
import time
import json


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


def try_knn(data, neighbor):
	data_train = []
	data_label = []
	for i in range(0, len(data)):
		data_train += [data[i][0:2]]
		data_label += [data[i][2:3]]
	print(len(data_train))
	print(len(data_label))
	data_train = np.asarray(data_train)
	data_label = np.asarray(data_label)
	c, r = data_label.shape
	data_label = data_label.reshape(c,)
	knn = KNeighborsClassifier(n_neighbors = neighbor)
	cv_scores = []
	score = cross_validation.cross_val_score(knn, data_train, data_label, cv = 10, scoring = 'accuracy')

	return score.mean()
	# print(score.mean())

with open('data.json') as json_data:
    data = json.load(json_data)
    # print(data)
data = modify_data(data)
for i in range(0, len(data)):
	if data[i][0] not in extension_dict:
		extension_dict[data[i][0]] = 1;
print(len(extension_dict.keys()))

# print(data)

myList = list(range(1,50))

neighbors = list(filter(lambda x: x % 2 != 0, myList))

cv_scores = []
for i in neighbors:
	print("\nThis is " + str(i) + " times:")
	start_time = time.clock()
	cv_scores += [try_knn(data, i)]
	end_time = time.clock()
	print("Time is: %f CPU seconds" % (end_time - start_time))

print(cv_scores)


# plot misclassification error vs k
plt.plot(neighbors, cv_scores)
plt.xlabel('Number of Neighbors K')
plt.ylabel('Accuracy')
plt.show()