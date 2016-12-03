__author__ = "Shurui Liu"
__email__ = "shurui91@gmail.com"

# decision tree algorithm implementation
import os, sys, timeit, glob, csv, copy
import pandas as pd
sys.path.append('/usr/local/lib/python3.4/dist-packages')
sys.path.append('/usr/lib/python3/dist-packages')
sys.path.append('/usr/lib/python3/dist-packages/scipy/sparse/sparsetools/csr.py')
import numpy
from sklearn import tree
from pprint import pprint

# timer
start = timeit.default_timer()

'''
process training data
'''
std_question_raw_train = []
std_question_train = []
with open('../csv_after_segmentation/jieba_seg_train.csv', 'rt', encoding='utf-8') as f:
	reader = csv.reader(f, delimiter=',')
	for row in reader:
		# append standard questions
		std_question_raw_train.append(row[3])

# remove the header element
std_question_train = std_question_raw_train[1:]

std_question_length_train = len(std_question_train)		# 9715 = 9716 - 1

# convert to index numbers
# q_index_train is essentially the Y in decision tree model
q_index_train = []
counter = 1
'''
q_index_train = [1,1,1,2,2,3,3,3,4,5,5]
std_question_test = [q1,q1,q1,q2,q2,q3,q3,q3,q4,q5,q5]

'''

for i in range(0, std_question_length_train):
	# if element i first occur, record its index as the current counter value, counter++
	if std_question_train[i] not in std_question_train[:i]:
		q_index_train.append(counter)
		counter += 1
	elif std_question_train[i] not in std_question_train[:i]:
		index = std_question_train.index(std_question_train[i])
		q_index2.append(index)

	else:
		index = q_index_train[i-1]
		q_index_train.append(index)

# read segmentTarget column from training csv, for X_train
# first, read all the words in the csv file and save them in a list
unique_word_raw = []
X_train = []

with open('../csv_after_segmentation/jieba_seg_train.csv', 'rt', encoding='utf-8') as f:
	reader = csv.reader(f, delimiter=',')
	for row in reader:
		words = row[6]		# for each row's extended questions (segmentTarget), save all the words into a list
		# seperate words by finding the space in between
		for word in words.strip().split():
			unique_word_raw.append(word)

# make a list to save all the unique word, 3239
unique_word_train = []
for word in unique_word_raw:
	if word not in unique_word_train:
		unique_word_train.append(word)
# print(len(unique_word_train))

# make a unique dict with values = 0
unique_word_train = {}
for word in unique_word_train:
	unique_word_train[word] = 0
# pprint(unique_word_train)

# make vectors for each extended question
with open('../csv_after_segmentation/jieba_seg_train.csv', 'rt', encoding='utf-8') as f:
	reader = csv.reader(f, delimiter=',')
	for row in reader:
		words = row[6]		# for each row's extended questions (segmentTarget)
		word_vector = []			# ['how', 'are', 'you, 'doing', 'where', 'are', 'you', 'going']
		matrix_vector = []			# [1, 1, 1, 1, 0, 0, ......]
		dict_copy = copy.deepcopy(unique_word_train)		# copy the dictionary

		for word in words.strip().split():
			count = words.count(word)
			dict_copy[word] = count
		values = dict_copy.values()
		for value in values:
			matrix_vector.append(value)
			X_train.append(matrix_vector)

# train the model
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, q_index_train)

'''
process the testing data
'''
std_question_raw_testing = []
std_question_test = []
with open('../csv_after_segmentation/jieba_seg_test.csv', 'rt', encoding='utf-8') as f:
	reader = csv.reader(f, delimiter=',')
	for row in reader:
		# append standard questions
		std_question_raw_testing.append(row[3])

# remove the header element
std_question_test = std_question_raw_testing[1:]

std_question_length_test = len(std_question_test)		# 9715 = 9716 - 1

# convert to index numbers
# q_index_test is essentially the Y in decision tree model
q_index_test = []
counter = 1
'''
q_index_test = [1,1,1,2,2,3,3,3,4,5,5]
std_question_test = [q1,q1,q1,q2,q2,q3,q3,q3,q4,q5,q5]

'''

for i in range(0, std_question_length_test):
	# if element i first occur, record its index as the current counter value, counter++
	if std_question_test[i] not in std_question_test[:i]:
		q_index_test.append(counter)
		counter += 1
	elif std_question_test[i] not in std_question_test[:i]:
		index = std_question_test.index(std_question_test[i])
		q_index2.append(index)

	else:
		index = q_index_test[i-1]
		q_index_test.append(index)

# read segmentTarget column from training csv, for X_test
# first, read all the words in the csv file and save them in a list
unique_word_raw = []
X_test = []

with open('../csv_after_segmentation/jieba_seg_test.csv', 'rt', encoding='utf-8') as f:
	reader = csv.reader(f, delimiter=',')
	for row in reader:
		words = row[6]		# for each row's extended questions (segmentTarget), save all the words into a list
		# seperate words by finding the space in between
		for word in words.strip().split():
			unique_word_raw.append(word)

# make a list to save all the unique word, 3239
unique_word_test = []
for word in unique_word_raw:
	if word not in unique_word_test:
		unique_word_test.append(word)
# print(len(unique_word_test))

# make a unique dict with values = 0
unique_word_test = {}
for word in unique_word_test:
	unique_word_test[word] = 0
# pprint(unique_word_test)

# make vectors for each extended question
with open('../csv_after_segmentation/jieba_seg_test.csv.csv', 'rt', encoding='utf-8') as f:
	reader = csv.reader(f, delimiter=',')
	for row in reader:
		words = row[6]		# for each row's extended questions (segmentTarget)
		word_vector = []			# ['how', 'are', 'you, 'doing', 'where', 'are', 'you', 'going']
		matrix_vector = []			# [1, 1, 1, 1, 0, 0, ......]
		dict_copy = copy.deepcopy(unique_word_test)		# copy the dictionary

		for word in words.strip().split():
			count = words.count(word)
			dict_copy[word] = count
		values = dict_copy.values()
		for value in values:
			matrix_vector.append(value)
			X_test.append(matrix_vector)

# predict testing data
results = []
for i, j in X_test, q_index_test:
	result = clf.predict([[i, j]])
	results.append(result)

# accuracy
correct = 0
total = len(result)
for i in range(total): # assuming the lists are of the same length
	if q_index_test[i]==result[i]:
		correct += 1
accuracy = correct / total
print(accuracy)



# print running time
stop = timeit.default_timer()
print("decision_tree.py running time is " + str(stop - start))