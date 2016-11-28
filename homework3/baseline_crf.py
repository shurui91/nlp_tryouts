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
	# all the onefile_utterance in one file
	# onefile_utterance = train_list[0]

	# deal with file
	file_feature = []
	file_label = []

	for line in range(len(file) - 1):
		features = []
		label = []

		#act_tag
		act_tag = file[line][0]
		label.append(act_tag)

		# speaker change
		if (file[line][1] != file[line + 1][1]):
			features.append("1")
		else:
			features.append("0")

		# first utterance
		if (line == 1):
			features.append("0")
		else:
			features.append("1")
		
		# posttag, contain empty ones
		pos = file[line][2]
		if (pos != None):
			for posttag in pos:
				features.append("TOKEN_" + posttag[0])
				features.append("POS_" + posttag[1])
		else:
			continue
		file_feature.append(features)
		file_label.append(label)
	
	# append to the big list
	x_train.append(file_feature)
	y_train.append(file_label)

	print(file_feature[0])
	print(file_label[0])
	print("\n")

# train the model
'''
trainer = pycrfsuite.Trainer(verbose=False)
for xseq, yseq in zip(x_train, y_train):
	trainer.append(xseq, yseq)
'''




























# print running time
stop = timeit.default_timer()
print("baseline_crf.py running time is " + str(stop - start))