__author__ = "Shurui Liu"
__email__ = "shurui91@gmail.com"
# try to read from excel file
import sys, jieba, openpyxl, timeit, csv

# timer
start = timeit.default_timer()

# read excel file
wb1 = openpyxl.load_workbook('个人存款测试集2.xlsx')
wb2 = openpyxl.load_workbook('个人理财测试集2.xlsx')
wb3 = openpyxl.load_workbook('个人贷款测试集.xlsx')
wb4 = openpyxl.load_workbook('电子银行测试集.xlsx')
wb5 = openpyxl.load_workbook('银行卡测试集.xlsx')

# read from sheet
sheet1 = wb1.get_sheet_by_name('Sheet1')			#个人存款测试集
sheet2 = wb2.get_sheet_by_name('Sheet1')				#个人理财测试集
sheet3 = wb3.get_sheet_by_name('598个测试集')			#个人贷款测试集
sheet4 = wb4.get_sheet_by_name('上传格式')			#电子银行测试集
sheet5 = wb5.get_sheet_by_name('Sheet1')			#银行卡测试集

# for x in range(0, 3):
# 	print ("Were on time %d" % (x))
sheet1_length = sheet1.max_row	#1353
sheet2_length = sheet2.max_row	#900
sheet3_length = sheet3.max_row	#1975
sheet4_length = sheet4.max_row	#3890
sheet5_length = sheet5.max_row	#1608

# write to csv file
fd = open('jieba_seg_test.csv','w', encoding='utf-8')

# print column header
column_header = "编号,问题,预期问题,SegmentedInput,SegmentedTarget"
fd.write(column_header + "\n")

# read the third column from excel file
''' sheet1 '''
for x in range(2, (sheet1_length + 1)):
	# number, area, question type, question, expanded question, SegmentedInput, SegmentedTarget
	number = str(sheet1["A%d" % (x)].value)
	question = str(sheet1["B%d" % (x)].value)
	expected_question = str(sheet1["C%d" % (x)].value)
	
	# cut questions
	q_cut = jieba.cut(question, cut_all = False)
	expectedq_cut = jieba.cut(expected_question, cut_all = False)
	
	# print everything out
	record = number + "," + question + "," + expected_question + "," + " ".join(q_cut) + "," + " ".join(expectedq_cut)
	fd.write(record + "\n")
	
''' sheet2 '''
for x in range(2, (sheet2_length + 1)):
	# number, area, question type, question, expanded question, SegmentedInput, SegmentedTarget
	number = str(sheet2["A%d" % (x)].value)
	question = str(sheet2["B%d" % (x)].value)
	expected_question = str(sheet2["C%d" % (x)].value)
	
	# cut questions
	q_cut = jieba.cut(question, cut_all = False)
	expectedq_cut = jieba.cut(expected_question, cut_all = False)
	
	# print everything out
	record = number + "," + question + "," + expected_question + "," + " ".join(q_cut) + "," + " ".join(expectedq_cut)
	fd.write(record + "\n")

''' sheet3 '''
for x in range(2, (sheet3_length + 1)):
	# number, area, question type, question, expanded question, SegmentedInput, SegmentedTarget
	number = str(sheet3["A%d" % (x)].value)
	question = str(sheet3["B%d" % (x)].value)
	expected_question = str(sheet3["C%d" % (x)].value)
	
	# cut questions
	q_cut = jieba.cut(question, cut_all = False)
	expectedq_cut = jieba.cut(expected_question, cut_all = False)
	
	# print everything out
	record = number + "," + question + "," + expected_question + "," + " ".join(q_cut) + "," + " ".join(expectedq_cut)
	fd.write(record + "\n")

''' sheet4 '''
for x in range(2, (sheet4_length + 1)):
	# number, area, question type, question, expanded question, SegmentedInput, SegmentedTarget
	number = str(sheet4["A%d" % (x)].value)
	question = str(sheet4["B%d" % (x)].value)
	expected_question = str(sheet4["C%d" % (x)].value)
	
	# cut questions
	q_cut = jieba.cut(question, cut_all = False)
	expectedq_cut = jieba.cut(expected_question, cut_all = False)
	
	# print everything out
	record = number + "," + question + "," + expected_question + "," + " ".join(q_cut) + "," + " ".join(expectedq_cut)
	fd.write(record + "\n")

''' sheet2 '''
for x in range(2, (sheet5_length + 1)):
	# number, area, question type, question, expanded question, SegmentedInput, SegmentedTarget
	number = str(sheet5["A%d" % (x)].value)
	question = str(sheet5["B%d" % (x)].value)
	expected_question = str(sheet5["C%d" % (x)].value)
	
	# cut questions
	q_cut = jieba.cut(question, cut_all = False)
	expectedq_cut = jieba.cut(expected_question, cut_all = False)
	
	# print everything out
	record = number + "," + question + "," + expected_question + "," + " ".join(q_cut) + "," + " ".join(expectedq_cut)
	fd.write(record + "\n")

# close file
fd.close()

# print running time
stop = timeit.default_timer()
print ("Running time is " + str(stop - start) + " seconds.")