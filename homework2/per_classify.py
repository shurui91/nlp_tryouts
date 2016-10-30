import os, json, sys

# 'Spam or Ham\dev\'
inputpath = sys.argv[1]
# 'per_output.txt'
outputpath = sys.argv[2]

file = open('per_model.txt', 'r', encoding="latin1")
lines = file.readlines()

# read from file
weights = lines[0]

# convert str to dictionary
weights_dictionary = json.loads(weights)
bias = weights_dictionary['hw_bias']

'''
print("bias is ")
print(bias)
print("bias type ")
print(type(bias))
print("bias type finish")
'''

# write to nboutput.txt
text_file = open(outputpath, "w", encoding="latin1")

# initiate some values
alpha = 0
wx = 0

# start to read from dev folder
for root, dirs, files in os.walk(inputpath):
	for file in files:
		# deals with ham files
		if file.endswith("ham.txt"):
			currentfile = []		# create a list for this file
			filepath = os.path.join(root, file)
			with open(filepath,'r', encoding="latin1") as f:
				for line in f:
					for word in line.strip().split():
						if word in weights_dictionary:
							wx += weights_dictionary[word]
				alpha = wx + bias
				if (alpha > 0):
					# print("SPAM  " + filepath)
					text_file.write("SPAM %s\n" % os.path.abspath(filepath))
				else:
					# print("HAM  " + filepath)
					text_file.write("HAM %s\n" % os.path.abspath(filepath))
				wx = 0
				alpha = 0
		
		# deals with spam files
		elif file.endswith("spam.txt"):
			currentfile = []		# create a list for this file
			filepath = os.path.join(root, file)
			with open(filepath,'r', encoding="latin1") as f:
				for line in f:
					for word in line.strip().split():
						if word in weights_dictionary:
							wx += weights_dictionary[word]
				alpha = wx + bias
				if (alpha > 0):
					# print("SPAM  " + filepath)
					text_file.write("SPAM %s\n" % os.path.abspath(filepath))
				else:
					# print("HAM  " + filepath)
					text_file.write("HAM %s\n" % os.path.abspath(filepath))
				wx = 0
				alpha = 0
