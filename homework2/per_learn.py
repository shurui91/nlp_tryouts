import os, fnmatch, glob, json, sys
import random
import timeit
from collections import defaultdict

__author__ = "Shurui Liu"
__email__ = "shurui91@gmail.com"

# timer
start = timeit.default_timer()
# input path
# "Spam or Ham/train/"
inputpath = sys.argv[1]
print(inputpath)

# start the program, make a dictionary to keep all the words
combine_dictionary = {}
file_list = []

for root, dirs, files in os.walk(inputpath):
	# for ham files
	for file in files:
		if file.endswith("ham.txt"):
			hamfile = ['ham']		# create a list for this ham file
			filepath = os.path.join(root, file)
			with open(filepath,'r', encoding="latin1") as f:
				for line in f:
					for word in line.strip().split():
						hamfile.append(word)		# append words into hamfile list
						# this counts the number of each word
						if word in combine_dictionary:
							combine_dictionary[word] += 1
						else:
							combine_dictionary[word] = 1
			# append hamfile list to file_list
			file_list.append(hamfile)
			
		elif file.endswith("spam.txt"):
			spamfile = ['spam']		# create a list for this spam file
			filepath = os.path.join(root, file)
			with open(filepath,'r', encoding="latin1") as f:
				for line in f:
					for word in line.strip().split():
						spamfile.append(word)		# append words into spamfile list
						# this counts the number of each word
						if word in combine_dictionary:
							combine_dictionary[word] += 1
						else:
							combine_dictionary[word] = 1
			# append hamfile list to file_list
			file_list.append(spamfile)

# make all the index to be zero in the combined dictionary
combine_dictionary = combine_dictionary.fromkeys(combine_dictionary, 0)

# start to read from file_list
alpha = 0
wx = 0
bias = 0
y_alpha = 0

# counter
counter = 0
for counter in range(20):
	# shuffle the whole file_list
	random.shuffle(file_list)
	
	for email in file_list:
		# if email is ham, y = -1
		if email[0] == 'ham':
			# calculate y_alpha
			for word in email[1:]:
				wx += combine_dictionary[word]
			alpha = wx + bias
			y_alpha = (-1) * alpha
			wx = 0
			
			# when need to change bias
			if y_alpha <= 0:
				for word in email[1:]:
					combine_dictionary[word] -= 1
				bias -= 1

		# if email is spam, y = 1
		elif email[0] == 'spam':
			# calculate y_alpha
			for word in email[1:]:
				wx += combine_dictionary[word]
			alpha = wx + bias
			y_alpha = 1 * alpha
			wx = 0
			
			# when need to change bias
			if y_alpha <= 0:
				for word in email[1:]:
					combine_dictionary[word] += 1
				bias += 1

# add bias to the dictionary
combine_dictionary['hw_bias'] = bias
combine_dictionary['file_name'] = 'per_output.txt'
				
# start to write to a text file
text_file = open("per_model.txt", "w", encoding="latin1")
json.dump(combine_dictionary, text_file)	# Line 1

#close
text_file.close()

# print running time
stop = timeit.default_timer()
print ("per_learn.py running time is " + str(stop - start))