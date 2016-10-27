# part 3
import os, json, sys, math

f = open('nbmodel_part3.txt', 'r', encoding="latin1")
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

dis_total = lines[0]		# distinct words in total, 35262
dis_in_ham = lines[1]		# distinct words in ham, 11981
dis_in_spam = lines[2]		# distinct words in spam, 28951
words_in_ham = lines[3]		# words in ham, 252833
words_in_spam = lines[4]	# words in spam, 218505
hams = lines[5]				# ham, 953
spams = lines[6]			# spam, 750

# convert to float
hams = float(hams)
spams = float(spams)
mails = spams + hams

# calculation part, vocabulary size = 108007
vocabulary_size = float(dis_total)

# p(spam) = 0.44039929536112743
# p_spam = spams / mails
p_spam = float(spams / mails)
p_spam = math.log(p_spam)

# p(not spam) = 0.5596007046388726
# p_ham = hams/mails
p_ham = float(hams / mails)
p_ham = math.log(p_ham)

# write to nboutput3.txt
text_file = open("nboutput3.txt", "w", encoding="latin1")	

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
						# test to see if this word is in combined dictionary
						elif word in combine_dictionary.keys():
							word_showup_time_in_ham = 1
							# p(X | ham)
							p_word_ham = float(word_showup_time_in_ham / (float(words_in_ham) + vocabulary_size))
							p_word_ham = math.log(p_word_ham)
							# append this p value into the list
							word_list_for_ham.append(p_word_ham)
						
						# if this word is unknown, treat it as spam
						elif word not in combine_dictionary.keys():
							# calculate p(word | spam)
							word_showup_time_in_spam = 0
							spam_dictionary.update({word: 1})
							word_showup_time_in_spam = spam_dictionary[word]
							# p(X | spam)
							p_word_spam = float(word_showup_time_in_spam / (float(words_in_spam) + vocabulary_size))
							p_word_spam = math.log(p_word_spam)
							# append this p value into the list
							word_list_for_spam.append(p_word_spam)
						
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
						elif word not in combine_dictionary.keys():
							# calculate p(word | spam)
							word_showup_time_in_spam = spam_dictionary[word] + 1
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
			
# compare to get the accuracy, open the file again
# text_file.write("The number of documents in total is %s\n" % int(mails)) = 1703
text_file_precision = open('nboutput3.txt', 'r', encoding="latin1")

# precision
ham_correct_classified = 0
spam_correct_classified = 0
ham_classified = 0
spam_classified = 0
for line in text_file_precision:
	if ("HAM") in line:
		ham_classified += 1
		if ("ham.txt") in line:
			ham_correct_classified += 1
	elif ("SPAM") in line:
		spam_classified += 1
		if ("spam.txt") in line:
			spam_correct_classified += 1

print ("Classified hams are " + str(ham_correct_classified))		# 950
print ("Classified spams are " + str(spam_correct_classified))		# 688
raw_ham_precision = float(ham_correct_classified / ham_classified)
raw_spam_precision = float(spam_correct_classified / spam_classified)
round_ham_precision = round(raw_ham_precision, 3)
round_spam_precision = round(raw_spam_precision, 3)
print ("The precision for hams is " + str(round_ham_precision))
print ("The precision for spams is " + str(round_spam_precision))
text_file_precision.close()


# recall
text_file_recall = open('nboutput3.txt', 'r', encoding="latin1")
belongs_in_ham = 0
belongs_in_spam = 0
for line in text_file_recall:
	if ("ham.txt") in line:
		belongs_in_ham += 1
	elif ("spam.txt") in line:
		belongs_in_spam += 1
print ("There are " + str(belongs_in_ham) + " files belongs in hams. ")		#953
print ("There are " + str(belongs_in_spam) + " files belongs in spams. ")	#697
raw_ham_recall = float(ham_correct_classified / belongs_in_ham)
raw_spam_recall = float(spam_correct_classified / belongs_in_spam)
round_ham_recall = round(raw_ham_recall, 3)
round_spam_recall = round(raw_spam_recall, 3)
print ("The recall for hams is " + str(round_ham_recall))
print ("The recall for spams is "+ str(round_spam_recall))
text_file_recall.close()

# F1
f1_ham = float(2 * raw_ham_precision * raw_ham_recall) / float(raw_ham_precision + raw_ham_recall)
f1_ham = round(f1_ham, 3)
print ("F1 for hams is " + str(f1_ham))

f1_spam = float(2 * raw_spam_precision * raw_spam_recall) / float(raw_spam_precision + raw_spam_recall)
f1_spam = round(f1_spam, 3)
print ("F1 for spams is " + str(f1_spam))

# make it in a nice format
print ("    precision  recall  F1")
print ("Ham    " + str(round_ham_precision) + "  " + str(round_ham_recall) + "  " + str(f1_ham))
print ("Spam    " + str(round_spam_precision) + "  " + str(round_spam_recall) + "  " + str(f1_spam))






