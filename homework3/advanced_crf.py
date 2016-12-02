__author__ = "Shurui Liu"
__email__ = "shurui91@gmail.com"

import hw3_corpus_tool
import os, sys, timeit, glob
# sys.path.append('/usr/local/lib/python3.4/dist-packages')
import pycrfsuite
from pprint import pprint

# timer
start = timeit.default_timer()

# inputdir, testdir, and outputfile
# python3 baseline_crf.py 'data/inputdir' 'data/testdir' 'advanced_output.txt'
inputdir = sys.argv[1]
testdir = sys.argv[2]
outputfile = sys.argv[3]

# all the csv files, data type is generator
train_file = hw3_corpus_tool.get_data(inputdir)
test_file = hw3_corpus_tool.get_data(testdir)

# a list of all the files in inputdir and testdir
train_list = list(train_file)
test_list = list(test_file)

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


# x_test, y_test
x_test = []
y_test = []
file_len = []

for file in test_list:
	# length for each file
	length = len(file)
	file_len.append(length)


	for line in range(len(file) - 1):
		line_feature = []
		# act_tag
		act_tag = file[line][0]
		y_test.append(act_tag)

		# act_tag change
		if (file[line][1] != file[line + 1][1]):
			line_feature.append("1")
		else:
			line_feature.append("0")

		# speaker change
		if (file[line][1] != file[line - 1][1]):
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
		
		x_test.append(line_feature)


# In[8], train the model
trainer = pycrfsuite.Trainer(verbose=False)
trainer.append(x_train, y_train)

# In[9], set training parameters
trainer.set_params({
	'c1': 1.0,   # coefficient for L1 penalty
	'c2': 1e-3,  # coefficient for L2 penalty
	'max_iterations': 100,  # stop earlier

	# include transitions that are possible, but not observed
	'feature.possible_transitions': True
})

# In[11], Train the model
trainer.train('conll2002-esp.crfsuite')

# pprint(trainer.logparser.last_iteration)

tagger = pycrfsuite.Tagger()
tagger.open('conll2002-esp.crfsuite')
#y_pred = [tagger.tag(xseq) for xseq in x_test]
#pprint(y_pred)


# print(len(tagger.tag(x_test)))
tags = tagger.tag(x_test)

def get_filename(data_dir):
	dialog_filenames = sorted(glob.glob(os.path.join(data_dir, "*.csv")))
	return dialog_filenames

all_filename = get_filename(testdir)

# write to nboutput.txt
text_file = open("advanced_output.txt", "w")
# text_file.write()

t = 0
for i in range(len(all_filename)):
	head, tail = os.path.split(all_filename[i])
	text_file.write('Filename=\"' + tail + '\"\n')
	for j in range(file_len[i] - 1):
		text_file.write(tags[t] + '\n')
		t += 1
	text_file.write('\n')

text_file.close()


# print running time
stop = timeit.default_timer()
print("advanced_crf.py running time is " + str(stop - start))