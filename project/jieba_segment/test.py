# test.py
import os, sys, timeit, glob, csv, copy
import pandas as pd
sys.path.append('/usr/local/lib/python3.4/dist-packages')
sys.path.append('/usr/lib/python3/dist-packages')
sys.path.append('/usr/lib/python3/dist-packages/scipy/sparse/sparsetools/csr.py')
import numpy
from sklearn import tree
from pprint import pprint

q_index = [1,1,1,2,2,3,3,3,4,5,5]
std_question = ['q1','q1','q1','q2','q2','q3','q3','q3','q4','q5','q5']
q_index2 = []

print(q_index)
print(std_question)
print(len(std_question))
print('\n\n')

counter = 1
for i in range(0, len(std_question)):
	if std_question[i] not in std_question[:i]:
		q_index2.append(counter)
		print("step " + str(i))
		print("index is " + str(counter))
		counter += 1
		
	elif std_question[i] not in std_question[:i]:
		index = std_question.index(std_question[i])
		print("step " + str(i))
		print("index is " + str(index))
	else:
		index = q_index[i-1]
		print("step " + str(i))
		print("index is " + str(index))

print(q_index2)

dictionary = {1: -0.3246, 2: -0.9185, 3: -3985}
testlist = []
values = dictionary.values()
for value in values:
	testlist.append(value)
print(testlist)

from sklearn import tree
X = [[0, 0], [1, 1]]
Y = [0, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)
print(clf)
test = clf.predict([[2, 2]])
print(type(test))