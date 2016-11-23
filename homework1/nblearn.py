import os, fnmatch, glob, json, sys

__author__ = "Shurui Liu"
__email__ = "shurui91@gmail.com"

ham_dictionary = {}
spam_dictionary = {}
combine_dictionary = {}
ham = 0
spam = 0
inputpath = sys.argv[1]
# 'Spam or Ham\train\'

for root, dirs, files in os.walk(inputpath):
	# for ham files
	for file in files:
		if file.endswith("ham.txt"):
			ham += 1
			filepath = os.path.join(root, file)
			with open(filepath,'r', encoding="latin1") as f:
				for line in f:
					for word in line.strip().split():
						# this counts the number of each word
						if word in ham_dictionary:
							ham_dictionary[word] += 1
						else:
							ham_dictionary[word] = 1
		elif file.endswith("spam.txt"):
			spam += 1
			filepath = os.path.join(root, file)
			with open(filepath,'r', encoding="latin1") as f:
				for line in f:
					for word in line.strip().split():
						# this counts the number of each word
						if word in spam_dictionary:
							spam_dictionary[word] += 1
						else:
							spam_dictionary[word] = 1

# combine two dictionaries
combine_dictionary = ham_dictionary.copy()
combine_dictionary.update(spam_dictionary)
print("The number of distinct words in total is " + str(len(combine_dictionary)))
							
# number of distinct words
print("The number of distinct words in ham_dictionary is " + str(len(ham_dictionary)))
print("The number of distinct words in spam_dictionary is " + str(len(spam_dictionary)))

#number of words in total
print("The number of words in ham_dictionary is " + str(sum(ham_dictionary.values())))
print("The number of words in spam_dictionary is " + str(sum(spam_dictionary.values())))

# ham and spam count
print("Number of hams is " + str(ham))
print("Number of spams is " + str(spam))

# start to write to a text file
text_file = open("nbmodel.txt", "w", encoding="latin1")
text_file.write("%s\n" % str(len(combine_dictionary)))
text_file.write("%s\n" % str(len(ham_dictionary)))
text_file.write("%s\n" % str(len(spam_dictionary)))
text_file.write("%s\n" % str(sum(ham_dictionary.values())))
text_file.write("%s\n" % str(sum(spam_dictionary.values())))
text_file.write("%s\n" % str(ham))
text_file.write("%s\n" % str(spam))

# dump dictionary into the text file
json.dump(ham_dictionary, text_file)
text_file.write("\n")
json.dump(spam_dictionary, text_file)

#close
text_file.close()


