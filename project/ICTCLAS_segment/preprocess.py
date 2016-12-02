# -*- coding: utf-8 -*-
import os
import csv
import xlrd
'''
for rt, dirs, files in os.walk('./'):
    with open(f[:-4] + '.csv', 'w') as csvfile:
        for f in files:
            #print (f)
            if f[-4:] == '.txt':
                #print (os.path.join(rt,f))
                f_content = open(os.path.join(rt,f))
                writer = csv.writer(csvfile)
                writer.writerow(["问题", "扩展问题"])
                f_content = f_content.read()
                f_content = f_content.split('\n')
                data = []
                for line in f_content:
                    line = line.split('\t')
                    if len(line)<3:
                        continue
                    extend_que = line[2]
                    extend_que = extend_que.split(',')
                    temp_eq = []
                    for item in extend_que:
                        temp_eq.append(item.split('/')[0])

                    que = line[1]
                    que = que.split(',')
                    temp_q = []
                    for item in que:
                        temp_q.append(item.split('/')[0])

                    dat = (' '.join(temp_q), ' '.join(temp_eq))
                    data.append(dat)
                writer.writerows(data)
'''

for rt, dirs, files in os.walk('./测试集'):
    with open('test.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        #writer.writerow(["序号","领域","类别","问题","扩展问题","SegmentedInput","SegmentedTarget"])
        writer.writerow(["序号","问题","扩展问题","SegmentedInput","SegmentedTarget"])
        i = 0
        data = []
        while i < len(files):
            if files[i][-4:] == '.txt':
                index = 0
                seg_file = files[i]
                orig_file = files[i+1]
                print(seg_file)
                print(orig_file)
                i += 2
                orig_content = xlrd.open_workbook(os.path.join(rt,orig_file))
                table = orig_content.sheets()[0]
                orig_content = []
                for rownum in range(table.nrows):
                    orig_content.append(table.row_values(rownum))
                f_content = open(os.path.join(rt,seg_file))
                f_content = f_content.read()
                f_content = f_content.split('\n')
                for line, orig in zip(f_content, orig_content[1:]):
                    line = line.split('\t')
                    if len(line)<3:
                        continue
                    extend_que = line[2]
                    extend_que = extend_que.split(',')
                    temp_eq = []
                    for item in extend_que:
                        temp_eq.append(item.split('/')[0])

                    que = line[1]
                    que = que.split(',')
                    temp_q = []
                    for item in que:
                        temp_q.append(item.split('/')[0])

                    dat = (index, orig[1], orig[2], ' '.join(temp_q), ' '.join(temp_eq))
                    index += 1
                    data.append(dat)
            else:
                i += 1
        writer.writerows(data)