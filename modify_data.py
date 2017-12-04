import numpy as np
import time  
import check_sentence
import get_extension
import get_size
import get_metadata
import os
import math
import json

extension_dict = {}


def modify_data(inter):
	#print("===============" + str(len(inter)) + "========================" + str(len(inter[0])))
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
				inter[j][i] = np.log2(inter[j][i])
		elif i == 2:
			for j in range(0, len(inter)):
				if inter[j][i] == True:
					inter[j][i] = 3
				else:
					inter[j][i] = 0
	return inter



start_time = time.clock()
inter = get_metadata.get_metadata('/home/tskluzac/pub8/', 1, 150, 0.5, 0.6, 0)
# inter = get_metadata.get_metadata('C:\\E\\temp', 1, 150, 0.5, 0.6, 0)
end_time = time.clock()
print("Get metadata time: %f CPU seconds" % (end_time - start_time))
#print('This is inter:')
#print(inter)
data = []
for i in range(0, len(inter[0])):
	temp = []
	for j in range(0, len(inter)):
		temp += [inter[j][i]]
	data += [temp]
# print(data)

# data = modify_data(data)
# print(data)
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
