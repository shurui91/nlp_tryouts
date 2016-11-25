#test_function.py
'''
def printme( str ):
	"This prints a passed string into this function"
	print str
	return 0

printme("why this also works?")
'''

import hw3_corpus_tool
import os, sys, timeit

# timer
start = timeit.default_timer()

# THE CODE
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # Second Example
	print ('Current fruit :' + fruit)

the_file = hw3_corpus_tool.get_utterances_from_file("labeled data/0001.csv")
print("the_file's data type is " + type(the_file))


# print running time
stop = timeit.default_timer()
print("This file's running time is " + str(stop - start))