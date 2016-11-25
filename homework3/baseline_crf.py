import hw3_corpus_tool
import os, sys, timeit
sys.path.append('/usr/local/lib/python3.4/dist-packages')
import pycrfsuite
from pprint import pprint

__author__ = "Shurui Liu"
__email__ = "shurui91@gmail.com"

# timer
start = timeit.default_timer()

# inputdir, testdir, and outputfile
# python3 baseline_crf.py 'data/inputdir' 'outputdir/outputfile' 'output.txt'
inputdir = sys.argv[1]
testdir = sys.argv[2]
outputfile = sys.argv[3]

# try to use functions from hw3_corpus_tool.py
# target folder is "labeled data/"
# test folder is "testdata/"

# all the csv files, data type is generator
the_file = hw3_corpus_tool.get_data(inputdir)

# a list of lists
the_list = list(the_file)
pprint(the_list[0][0])
# start to write to a text file
# text_file = open("test.txt", "w", encoding="latin1")
# text_file.write(str(the_list[0][0]))
# text_file.close()
'''
DialogUtterance(
	act_tag='qw', 
	speaker='A', 
	pos=[
		PosTag(token='What', pos='WP'), 
		PosTag(token='are', pos='VBP'), 
		PosTag(token='your', pos='PRP$'), 
		PosTag(token='favorite', pos='JJ'), 
		PosTag(token='programs', pos='NNS'), 
		PosTag(token='?', pos='.')
	], 
	text='What are your favorite programs? /')
'''






# print running time
stop = timeit.default_timer()
print("baseline_crf.py running time is " + str(stop - start))