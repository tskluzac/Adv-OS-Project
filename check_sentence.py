import nltk
from nltk.corpus import wordnet
import re
import os
from docx import Document
import array
import PyPDF2
# from nltk.corpus import words
former_punctuation_list = ['"', '\'', '[', '{', '<', '(', '-']
latter_punctuation_list = ['"', '.', '\'', ']', '}', '>', ')', '!', '?', ';', '-', '\n']
debug = 0


# determine whether a string is a number
# input: string
# output: whether input is a number
def isNumber(value): 
  try:
    float(value)
    return True
  except:
  	try:
  		int(value)
  		return True
  	except:
  		return False


# remove punctuation at the beginning/end of a string
# input: string
# output: string without punctuation at the beginning and end
def remove_punctuation(wo): 
	i = 0
	l = len(wo)
	while i < l and wo[i] in former_punctuation_list:
		i += 1;
	wo = wo[i:len(wo)]
	i = 1
	l = len(wo)
	while i <= l and wo[len(wo)-i] in latter_punctuation_list:
		i += 1
	wo = wo[0:len(wo)+1-i]
	return wo


# split sentence into list of strings
# input: sentence
# list of words(string)
def split_sentence(line): 
	length = len(line) - 1
	i = -1;
	result = []
	old_result = re.split('\s', line)
	#print(result)
	for i in old_result: # remove empty strings
		if i != '':
			result += [i]
	# print(result)
	for i in range(0, len(result)):
		result[i] = remove_punctuation(result[i])
	return result


# check binary number and remove control part
# input: number
# output: if number in ascii is control part return false, else true
def check_number(a): 
	if (a != 10 and a < 32) or a > 126:
		return False
	return True


# get word_list from file
# input: filename and how many words need to get(assume average word length is less than 15)
# output: list of words(string)
def get_wordlist(filename, n): 
	word_list = []
	try:
		if filename.lower().endswith(('.doc', '.docx')): # for .doc/.docx
		# reference: https://stackoverflow.com/questions/25228106/how-to-extract-text-from-an-existing-docx-file-using-python-docx
			fp = open(filename, mode='rb')
			document = Document(fp)
			for i in document.paragraphs:
				#print(i.text)
				result = re.split('\s', i.text)
				for i in range(0, len(result)):
					result[i] = remove_punctuation(result[i])
				word_list += result
				if len(word_list) > n:
					break
			fp.close()
		elif filename.lower().endswith(('.pdf')): # for pdf file (cannot open all pdf file and i don't know why, for example kortzinger et al 1996 MC52.pdf), 
		# reference:http://www.geeksforgeeks.org/working-with-pdf-files-in-python/
			# creating a pdf file object
			pdfFileObj = open(filename, 'rb')
			# creating a pdf reader object
			pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
			# printing number of pages in pdf file
			#print(pdfReader.numPages)
			# creating a page object
			for i in range(0, pdfReader.numPages):
				#print(i)
				pageObj = pdfReader.getPage(i)
				temp = pageObj.extractText()
				#print(temp)
				result = re.split('\s', temp)
				for i in range(0, len(result)):
					result[i] = remove_punctuation(result[i])
				word_list += result
				if len(word_list) > n:
					break			 
			pdfFileObj.close()
			# extracting text from page
			# print(pageObj.extractText())
			# closing the pdf file object
			# pdfFileObj.close()
		else: # most for .txt, cannot open xls
			fp = open(filename, mode='rb')
			bi_line = fp.read((15*n))
			#print(bi_line)
			re_line = []
			for i in bi_line:
				if check_number(i):
					re_line += [i]
			re_line = array.array('B', re_line).tostring()
			#print(re_line)
			line = re_line.decode('utf-8')
			word_list = split_sentence(line)
			if debug:
				print(word_list)
			fp.close()
		try:
			return word_list[0:n]
		except:
			return word_list
	except: # cannot open file
		fp = open(filename, mode='rb')
		print('open file error: ' + filename)
		return word_list


# check words/number in word_list
# input: list of words(string)
# count number of word and number
def check_wordlist(word_list): 
	count_word = 0
	count_number = 0
	for i in word_list:
		if isNumber(i):
			count_number += 1
		else:
			if wordnet.synsets(i):
				count_word += 1
	return [count_word, count_number]


# the main function
# input: filename, number of words need to sample, 
# total_decision: number of words/number should be at least more than total_decision, maybe 0.5
# number_decision: number of number words(911) cannot more than pencent of words + number, maybe 0.8
# output: is the file contains readable sentence
def check_sentence_in_word(filename, n, total_decision, number_decision):
	if debug:
		print('working on ' + filename)
	word_list = get_wordlist(filename, n)
	if len(word_list) == 0:
		return False
	r = check_wordlist(word_list)
	count_word = r[0]
	count_number = r[1]
	count_total = r[0] + r[1]
	if count_total == 0:
		return False
	print('\n##############################################\n')
	print(count_total/len(word_list))
	print(count_number/count_total)
	if count_total/len(word_list) < total_decision or count_number/count_total > number_decision:
		return False
	else:
		return True


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


file_list = file_in_folder('C:\\E\\temp', 1)
#file_list = file_in_folder('C:\\E\\University of Chicago\\CMSC33100\\project', 1);
for i in file_list:
	print(i + ': ' + str(check_sentence_in_word(i, 150, 0.5, 0.6)))
