# evaluate_model_baseline.py
import hw3_corpus_tool
import os, sys, timeit, glob
sys.path.append('/usr/local/lib/python3.4/dist-packages')
import pycrfsuite
from pprint import pprint

# timer
start = timeit.default_timer()

# inputdir, testdir, and outputfile
# python3 evaluate_model.py 'data/testdir' 'output.txt'
devdir = sys.argv[1]
textfile = sys.argv[2]

# create a list
output_tag = []

# read lines from output.txt
with open(textfile) as f:
	for line in f:
		line = line.strip()
		if not line:  # line is blank
			continue
		if line.startswith("Filename"):  # comment line
			continue
		output_tag.append(line)
print(len(output_tag))


# all the csv files, data type is generator
dev_file = hw3_corpus_tool.get_data(devdir)
dev_list = list(dev_file)

dev_tag = []

for file in dev_list:
	for line in range(len(file) - 1):
		#act_tag
		act_tag = file[line][0]
		dev_tag.append(act_tag)

print(len(dev_tag))

# total number of tags, correct tags number
total = len(dev_tag)
correct = 0

# compare two lists
for i in range(len(output_tag)):
	if (output_tag[i] == dev_tag[i]):
		correct += 1

print(correct)
rate = correct / len(dev_tag)
print("The accurate rate is " + str(rate))










# print running time
stop = timeit.default_timer()
print("baseline_crf.py running time is " + str(stop - start))