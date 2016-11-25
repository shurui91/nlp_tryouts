import os, fnmatch, glob, json
from collections import Counter

__author__ = "Shurui Liu"
__email__ = "shurui91@gmail.com"

ham_dictionary = {}
spam_dictionary = {}
combine_dictionary = {}

for root, dirs, files in os.walk('Spam or Ham/train/'):
	# for ham files
	for file in files:
		if file.endswith("ham.txt"):
			filepath = os.path.join(root, file)
			with open(filepath,'r', encoding="latin1") as f:
				for line in f:
					for word in line.split():
						# this counts the number of each word
						if word in ham_dictionary:
							ham_dictionary[word] += 1
						else:
							ham_dictionary[word] = 1
		elif file.endswith("spam.txt"):
			filepath = os.path.join(root, file)
			with open(filepath,'r', encoding="latin1") as f:
				for line in f:
					for word in line.split():
						# this counts the number of each word
						if word in spam_dictionary:
							spam_dictionary[word] += 1
						else:
							spam_dictionary[word] = 1

# combine two dictionaries
combine_dictionary = ham_dictionary.copy()
combine_dictionary.update(spam_dictionary)
print("The number of distinct words in total is " + str(len(combine_dictionary)))
							
# print(json.dumps(ham_dictionary))
print("The number of distinct words in ham_dictionary is " + str(len(ham_dictionary)))
print("The number of distinct words in spam_dictionary is " + str(len(spam_dictionary)))
