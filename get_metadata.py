import check_sentence
import get_extension
import get_size
import os


# get all file in a folder
# input: folderpath
# flag indicates whether includes files in subfolder, 1 is including, 0 is not
# reference: https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
def file_in_folder(folder_path, flag):
	file_list = []
	for (dirpath, dirnames, filenames) in os.walk(folder_path):
		for i in filenames:
			file_list += [dirpath + os.sep + i]
		if flag == 0:
			break;
	return file_list

# main function
# input: folder_path: the path of folder we will work on
# flag: whether consider files in sub-folder, 1 is yes, 0 is not
# n: number of words want to sample for check sentence
# total_decision: number of words/number should be at least more than total_decision, maybe 0.5, for check sentence
# number_decision: number of number words(911) cannot more than pencent of words + number, maybe 0.6, for check sentence
# debug: debug for check sentence. 0 will not show debug, 1 will show some detail of check sentence
# output: a list of list, one column corresponding to one file
def get_metadata(folder_path, flag, n, total_decision, number_decision, debug):
	file_list = file_in_folder(folder_path, flag)
	metadata = []
	metadata += [get_extension.file_extension(file_list)]
	metadata += [get_size.file_size_list(file_list)]
	metadata += [check_sentence.check_sentence(file_list, n, total_decision, number_decision, debug)]
	print('\n')
	print(metadata)


#file_list = file_in_folder('C:\\E\\temp', 1)
file_list = file_in_folder('C:\\E\\University of Chicago\\CMSC33100\\project', 1)
get_metadata('C:\\E\\University of Chicago\\CMSC33100\\project', 1, 150, 0.5, 0.6, 0)