__author__ = "Shurui Liu"
__email__ = "shurui91@gmail.com"

# decision tree algorithm implementation
import os, sys, timeit, glob, csv
import pandas as pd
sys.path.append('/usr/local/lib/python3.4/dist-packages')
sys.path.append('/usr/lib/python3/dist-packages')
sys.path.append('/usr/lib/python3/dist-packages/scipy/sparse/sparsetools/csr.py')
import numpy
from sklearn import tree
from pprint import pprint

# timer
start = timeit.default_timer()

X = [[0, 0], [1, 1]]
Y = [0, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

# gives detailed info about the classifier
# print(clf)
# print(clf.predict([[2., 2.]]))

# process data
std_questions = []

with open('../csv_after_segmentation/jieba_seg_train.csv', 'rt', encoding='utf-8') as f:
	reader = csv.reader(f, delimiter=',')
	for row in reader:
		std_question = []
		std_question.append(row[3])
		std_questions.append(std_question)
	# print(len(std_questions))		# 9716

new_std_questions = []
for question in std_questions:
	if question not in new_std_questions:
		new_std_questions.append(question)
# print(len(new_std_questions))		# 890
pprint(new_std_questions)







# print running time
stop = timeit.default_timer()
print("advanced_crf.py running time is " + str(stop - start))