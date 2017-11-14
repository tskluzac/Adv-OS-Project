import os

# def file_in_folder(folder_path, flag):
# 	file_list = []
# 	for (dirpath, dirnames, filenames) in os.walk(folder_path):
# 		for i in filenames:
# 			file_list += [dirpath + os.sep + i]
# 		if flag == 0:
# 			break;
# 	return file_list


def file_size_list(file_list):
	size_list = []
	for i in file_list:
		# print(os.stat(i).st_size)
		size_list += [os.stat(i).st_size]
	return size_list

#file_list = file_in_folder('C:\\E\\temp', 1)
# file_list = file_in_folder('C:\\E\\University of Chicago\\CMSC33100\\project', 1)
# print(file_list)
# file_size_list(file_list)