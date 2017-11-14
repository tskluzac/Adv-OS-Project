import os

# def file_in_folder(folder_path, flag):
# 	file_list = []
# 	for (dirpath, dirnames, filenames) in os.walk(folder_path):
# 		for i in filenames:
# 			file_list += [dirpath + os.sep + i]
# 		if flag == 0:
# 			break;
# 	return file_list


def file_extension(file_list):
	extension_list = []
	for i in file_list:
		ext = os.path.splitext(i)[-1].lower()
		# print(ext)
		extension_list += [ext[1:len(ext)]]
	return extension_list


# file_list = file_in_folder('C:\\E\\University of Chicago\\CMSC33100\\project', 1)
# extension_list = file_extension(file_list)
# print(extension_list)