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
# python3 baseline_crf.py 'testdata/inputdir' 'testdata/testdir' 'output.txt'
inputdir = sys.argv[1]
testdir = sys.argv[2]
outputfile = sys.argv[3]

# all the csv files, data type is generator
train_file = hw3_corpus_tool.get_data(inputdir)
test_file = hw3_corpus_tool.get_data(testdir)

# a list of all the files in inputdir and testdir
train_list = list(train_file)
test_list = list(test_file)

# all the onefile_utterance in one file
onefile_utterance = train_list[0]
# first utterance tuple, first line
#first_utterance_tuple = onefile_utterance[0]
'''
first_utterance_tuple[0] = act_tag
first_utterance_tuple[1] = speaker
first_utterance_tuple[2] = pos[]
first_utterance_tuple[3] = text
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
file_feature = []
for i in range(len(onefile_utterance) - 1):
	features = []
	# speaker change
	if (onefile_utterance[i][1] != onefile_utterance[i + 1][1]):
		features.append(1)
	else:
		features.append(0)

	# first utterance
	if (i == 1):
		features.append(0)
	else:
		features.append(1)
	
	# posttag, contain empty ones
	posttag = onefile_utterance[i][2]
	if (posttag != None):
		for j in posttag:
			features.append("TOKEN_" + j[0])
			features.append("POS_" + j[1])
	file_feature.append(features)

pprint(file_feature)


























# print running time
stop = timeit.default_timer()
print("baseline_crf.py running time is " + str(stop - start))