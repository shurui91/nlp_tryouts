import os, json, sys, math

__author__ = "Shurui Liu"
__email__ = "shurui91@gmail.com"

f = open('nbmodel.txt', 'r', encoding="latin1")
lines = f.readlines()
# print(len(lines))

# these are strings
ham_data = lines[7]
spam_data = lines[8]
# strings
# print(type(ham_data))
# print(type(spam_data))

# give parameters
# 'Spam or Ham\dev\'
inputpath = sys.argv[1]

ham_dictionary = json.loads(ham_data)
spam_dictionary = json.loads(spam_data)
combine_dictionary = {}
# combine two dictionaries
combine_dictionary = ham_dictionary.copy()
combine_dictionary.update(spam_dictionary)

# These are dictionaries
# print(type(ham_dictionary))
# print(type(spam_dictionary))
# print(type(combine_dictionary))

dis_total = lines[0]		# distinct words in total, 108007
dis_in_ham = lines[1]		# distinct words in ham, 40306
dis_in_spam = lines[2]		# distinct words in spam, 85793
words_in_ham = lines[3]		# words in ham, 2618662
words_in_spam = lines[4]	# words in spam, 1839210
hams = lines[5]				# ham, 9533
spams = lines[6]			# spam, 7496

# convert to float
hams = float(hams)
spams = float(spams)
mails = spams + hams

# calculation part, vocabulary size = 108007
vocabulary_size = float(dis_total)

# p(spam) = 0.4401902636678607
# p_spam = spams / mails
p_spam = float(spams / mails)
p_spam = math.log(p_spam)

# p(not spam) = 0.5598097363321393
# p_ham = hams/mails
p_ham = float(hams / mails)
p_ham = math.log(p_ham)

# for each word shows up in ham
for key, value in ham_dictionary.items():
	# every word shows up for how many times in ham
	# print (key, 'shows up', value, 'times in ham')
	word_in_ham = float(value / float(words_in_ham))
	# print (value / float(words_in_ham))


# for each word shows up in spam
for key, value in spam_dictionary.items():
	# every word shows up for how many times in spam
	# print (key, 'shows up', value, 'times in spam')
	word_in_spam = float(value / float(words_in_spam))
	# print (value / float(words_in_spam))

# write to nboutput.txt
text_file = open("nboutput.txt", "w", encoding="latin1")	

# start to read from dev folder
for root, dirs, files in os.walk(inputpath):
	for file in files:
		product_msg_ham = 0
		product_msg_spam = 0
		# lists that contains words from ham and spam
		word_list_for_ham = []
		word_list_for_spam = []
		if file.endswith(".txt"):
			filepath = os.path.join(root, file)
			with open(filepath,'r', encoding="latin1") as f:
				for line in f:
					for word in line.strip().split():
						# test to see if this word is in ham
						if word in ham_dictionary.keys():
							# how many times this word shows up in ham, + 1
							word_showup_time_in_ham = ham_dictionary[word] + 1
							# p(X | ham)
							p_word_ham = float(word_showup_time_in_ham / (float(words_in_ham) + vocabulary_size))
							p_word_ham = math.log(p_word_ham)
							# append this p value into the list
							word_list_for_ham.append(p_word_ham)
						elif word in combine_dictionary.keys():
							word_showup_time_in_ham = 1
							# p(X | ham)
							p_word_ham = float(word_showup_time_in_ham / (float(words_in_ham) + vocabulary_size))
							p_word_ham = math.log(p_word_ham)
							# append this p value into the list
							word_list_for_ham.append(p_word_ham)
						
						# test to see if this word is in spam
						if word in spam_dictionary.keys():
							# calculate p(word | spam)
							word_showup_time_in_spam = spam_dictionary[word] + 1
							# p(X | spam)
							p_word_spam = float(word_showup_time_in_spam / (float(words_in_spam) + vocabulary_size))
							p_word_spam = math.log(p_word_spam)
							# append this p value into the list
							word_list_for_spam.append(p_word_spam)
						elif word in combine_dictionary.keys():
							word_showup_time_in_spam = 1
							# p(X | spam)
							p_word_spam = float(word_showup_time_in_spam / (float(words_in_spam) + vocabulary_size))
							p_word_spam = math.log(p_word_spam)
							# append this p value into the list
							word_list_for_spam.append(p_word_spam)
							
			# p(Msg | ham)
			for element in word_list_for_ham:
				product_msg_ham += element
			# p(Msg | spam)
			for element in word_list_for_spam:
				product_msg_spam += element
			# print("p(Msg | ham)")
			# print(product_msg_ham)
			# print("p(Msg | spam)")
			# print(product_msg_spam)
				
			# p(ham | Msg), in log
			p_ham_msg = p_ham + product_msg_ham
			# p(spam | Msg), in log
			p_spam_msg = p_spam + product_msg_spam
				
			# decide if it is ham or spam
			if(p_ham_msg > p_spam_msg):
				# print("HAM  " + filepath)
				text_file.write("HAM %s\n" % os.path.abspath(filepath))
			elif(p_ham_msg < p_spam_msg):
				# print("SPAM  " + filepath)
				text_file.write("SPAM %s\n" % os.path.abspath(filepath))
