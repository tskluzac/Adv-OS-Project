# using kmean and validating with purity.

import numpy as np
from sklearn.cluster import  k_means
from sklearn.metrics import accuracy_score 
from sklearn.neighbors import KNeighborsClassifier
from sklearn import cross_validation
import time  
import matplotlib.pyplot as plt  
from mpl_toolkits.mplot3d import axes3d
import math
import time
import json
from collections import Counter

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


def most_common_elem(li):
	# print(li)
	count = Counter(li)
	# print(count.most_common()[0][1])
	try:
		# print(count.most_common()[0][1])
		return (count.most_common()[0][1])
	except IndexError:
		return 0


def calc_purity(label, data_ext_label, neighbors):
	purity_list = []
	for i in range(0, len(label)):
		print("This is " + str(i) + "run")
		label_order_list = []
		extension_dict = {}
		idx = 0;
		length_label = len(label[i])
		for j in range(0, len(label[i])):
			temp = []
			if label[i][j] not in extension_dict:
				#print(len(extension_dict.keys()))
				extension_dict[label[i][j]] = idx
				temp = data_ext_label[j]
				label_order_list += [temp]
				idx += 1
				#print(len(label_order_list[extension_dict[label[i][j]]]))
			else:
				label_order_list[extension_dict[label[i][j]]] += data_ext_label[j]

		temp_purity_list = []
		length_list = []
		for j in range(0, len(label_order_list)):
			leng = len(label_order_list[j])
			length_list += [leng]
			temp_purity_list += [most_common_elem(label_order_list[j])]
		
		total = 0
		# print(length_list)
		# print(temp_purity_list)
		# print(length_label)
		for j in range(0, len(length_list)):
			total += temp_purity_list[j]
		purity_list += [total / length_label]
		for j in extension_dict.keys():
			del label_order_list[extension_dict[j]][:]

	return purity_list


def showCluster(dataSet, k, centroids, label, inertia):  
    numSamples, dim = dataSet.shape  
    if dim != 2:  
        print("Sorry! I can not draw because the dimension of your data is not 2!"  )
        return 1  
  
    mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']  
    if k > len(mark):  
        print("Sorry! Your k is too large! please contact Zouxy"  )
        return 1  
    # draw all samples  
    for i in range(0,numSamples):
    	markIndex = int(label[i])  
    	plt.plot(dataSet[i, 0], dataSet[i, 1], mark[markIndex])  
  
    mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb']  
    # draw the centroids  
    for i in range(k):  
        plt.plot(centroids[i, 0], centroids[i, 1], mark[i], markersize = 10)  
  
    plt.show()  
# print(data)


def kmean(data, k):
	data_part = []
	for i in range(0, len(data)):
		data_part += [data[i][1:3]]
	# print(data_part)
	# data_part = np.mat(data_part)
	[centroid, label, inertia] = k_means(data_part, k)
	# print(centroid)
	# print(label)
	# print(inertia)
	return [centroid, label, inertia]
	# data_result = []
	# for i in range(0, len(label)):
	# 	data_result += [data_part[i].append(label[i])]
	# with open('data_kmean.json', 'w') as outfile:
	# 	json.dump(data_result, outfile)

	# showCluster(data_part, k, centroid, label, inertia)


def validation_purity(label_list, data_ext_label, neighbors):
	purity_list = calc_purity(label_list, data_ext_label, neighbors)
	print(purity_list)
	# plot misclassification error vs k
	plt.plot(neighbors, purity_list)
	plt.xlabel('Number of Clusters K')
	plt.ylabel('Accuracy')
	plt.show()


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

# print(data)

myList = list(range(3,len(extension_dict.keys())))
# myList = list(range(3, 20))
neighbors = list(filter(lambda x: x % 2 != 0, myList))
# neighbors = list(range(3,len(extension_dict.keys())))
iner_list = []
label_list = []
cent_list = []
purity = []
for i in neighbors:
	print("\nThis is " + str(i) + " times:")
	start_time = time.clock()
	[centroid, label, inertia] = kmean(data, i)
	iner_list += [inertia]
	label_list += [label]
	cent_list += [centroid]
	end_time = time.clock()
	print("Time is: %f CPU seconds" % (end_time - start_time))

validation_purity(label_list, data_ext_label, neighbors)