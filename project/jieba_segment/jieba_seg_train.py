__author__ = 'Shurui Liu'
# try to read from excel file
import sys, jieba, openpyxl, timeit, csv

# timer
start = timeit.default_timer()

# read excel file
wb1 = openpyxl.load_workbook('个人存款扩展问题.xlsx')
wb2 = openpyxl.load_workbook('个人理财扩展问题.xlsx')
wb3 = openpyxl.load_workbook('个人贷款扩展问题.xlsx')
wb4 = openpyxl.load_workbook('电子银行扩展问题2.xlsx')
wb5 = openpyxl.load_workbook('银行卡扩展问题.xlsx')

# show sheet names
'''
print(wb1.get_sheet_names())
print(wb2.get_sheet_names())
print(wb3.get_sheet_names())
print(wb4.get_sheet_names())
print(wb5.get_sheet_names())
'''

# read from sheet
sheet1 = wb1.get_sheet_by_name('汇总的')			#个人存款扩展问题
sheet2 = wb2.get_sheet_by_name('扩展问题0827')		#个人理财扩展问题
sheet3 = wb3.get_sheet_by_name('扩展问题')			#个人贷款扩展问题
sheet4 = wb4.get_sheet_by_name('Sheet1')			#电子银行扩展问题
sheet5 = wb5.get_sheet_by_name('Sheet1')			#银行卡扩展问题

# cell value, row number, column number
value1 = sheet1['D10'].value
row_count = sheet1.max_row
column_count = sheet1.max_column

# test cut
# seg_list = jieba.cut(value1, cut_all = False)
# print(" ".join(seg_list))  # 精确模式

# for x in range(0, 3):
# 	print ("Were on time %d" % (x))
sheet1_length = sheet1.max_row	#1353
sheet2_length = sheet2.max_row	#900
sheet3_length = sheet3.max_row	#1975
sheet4_length = sheet4.max_row	#3890
sheet5_length = sheet5.max_row	#1608

# write to csv file
fd = open('jieba_seg_train.csv','w', encoding='utf-8')

# print column header
column_header = "序号,领域,类别,问题,扩展问题,SegmentedInput,SegmentedTarget"
fd.write(column_header + "\n")

# read the third column from excel file
''' sheet1 '''
for x in range(2, (sheet1_length + 1)):
	# number, area, question type, question, expanded question, SegmentedInput, SegmentedTarget
	number = str(x - 2)
	area = sheet1["A%d" % (x)].value
	q_type = sheet1["B%d" % (x)].value
	question = sheet1["C%d" % (x)].value
	expanded_question = sheet1["D%d" % (x)].value
	
	# cut questions
	q_cut = jieba.cut(question, cut_all = False)
	expandedq_cut = jieba.cut(expanded_question, cut_all = False)
	
	# print everything out
	record = number + "," + area + "," + q_type + "," + question + "," + expanded_question + "," + " ".join(q_cut) + "," + " ".join(expandedq_cut)
	fd.write(record + "\n")

''' sheet2 '''
for x in range(2, (sheet2_length + 1)):
	# number, area, question type, question, expanded question, SegmentedInput, SegmentedTarget
	number = str(x - 2)
	area = sheet2["A%d" % (x)].value
	q_type = sheet2["B%d" % (x)].value
	question = sheet2["C%d" % (x)].value
	expanded_question = sheet2["D%d" % (x)].value
	
	# cut questions
	q_cut = jieba.cut(question, cut_all = False)
	expandedq_cut = jieba.cut(expanded_question, cut_all = False)
	
	# print everything out
	record = number + "," + area + "," + q_type + "," + question + "," + expanded_question + "," + " ".join(q_cut) + "," + " ".join(expandedq_cut)
	fd.write(record + "\n")

''' sheet3 '''
for x in range(2, (sheet3_length + 1)):
	# number, area, question type, question, expanded question, SegmentedInput, SegmentedTarget
	number = str(x - 2)
	area = sheet3["A%d" % (x)].value
	q_type = sheet3["B%d" % (x)].value
	question = sheet3["C%d" % (x)].value
	expanded_question = sheet3["D%d" % (x)].value
	
	# cut questions
	q_cut = jieba.cut(question, cut_all = False)
	expandedq_cut = jieba.cut(expanded_question, cut_all = False)
	
	# print everything out
	record = number + "," + area + "," + q_type + "," + question + "," + expanded_question + "," + " ".join(q_cut) + "," + " ".join(expandedq_cut)
	fd.write(record + "\n")

''' sheet4 '''
for x in range(2, (sheet4_length + 1)):
	# number, area, question type, question, expanded question, SegmentedInput, SegmentedTarget
	number = str(x - 2)
	area = sheet4["A%d" % (x)].value
	q_type = sheet4["B%d" % (x)].value
	question = sheet4["C%d" % (x)].value
	expanded_question = sheet4["D%d" % (x)].value
	
	# cut questions
	q_cut = jieba.cut(question, cut_all = False)
	expandedq_cut = jieba.cut(expanded_question, cut_all = False)
	qcut_str = " ".join(q_cut)		#str
	expandedqcut_str = " ".join(expandedq_cut)		#str
	
	# print everything out
	record = number + "," + area + "," + q_type + "," + question + "," + expanded_question + "," + qcut_str + "," + expandedqcut_str
	fd.write(record + "\n")


''' sheet5 '''
for x in range(2, (sheet5_length + 1)):
	# number, area, question type, question, expanded question, SegmentedInput, SegmentedTarget
	number = str(x - 2)
	area = sheet5["A%d" % (x)].value
	q_type = sheet5["B%d" % (x)].value
	question = sheet5["C%d" % (x)].value
	expanded_question = sheet5["D%d" % (x)].value
	
	# cut questions
	q_cut = jieba.cut(question, cut_all = False)
	expandedq_cut = jieba.cut(expanded_question, cut_all = False)
	
	# print everything out
	record = number + "," + area + "," + q_type + "," + question + "," + expanded_question + "," + " ".join(q_cut) + "," + " ".join(expandedq_cut)
	fd.write(record + "\n")

# close file
fd.close()

# print running time
stop = timeit.default_timer()
print ("Running time is " + str(stop - start) + " seconds.")