import hw3_corpus_tool
import os, sys, timeit
sys.path.append('/usr/local/lib/python3.4/dist-packages')
import pycrfsuite
from pprint import pprint

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

# x_train, y_train
x_train = []
y_train = []

for file in train_list:
	for line in range(len(file) - 1):
		line_feature = []
		#act_tag
		act_tag = file[line][0]
		y_train.append(act_tag)

		# speaker change
		if (file[line][1] != file[line + 1][1]):
			line_feature.append("1")
		else:
			line_feature.append("0")

		# first utterance
		if (line == 1):
			line_feature.append("0")
		else:
			line_feature.append("1")
		
		# posttag, contain empty ones
		pos = file[line][2]
		if (pos != None):
			for posttag in pos:
				line_feature.append("TOKEN_" + posttag[0])
				line_feature.append("POS_" + posttag[1])
		
		x_train.append(line_feature)

print(len(x_train))
print(len(y_train))



'''
# train the model
trainer = pycrfsuite.Trainer(verbose=False)
for xseq, yseq in zip(x_train, y_train):
	trainer.append(x_train, y_train)
'''



























# print running time
stop = timeit.default_timer()
print("baseline_crf.py running time is " + str(stop - start))