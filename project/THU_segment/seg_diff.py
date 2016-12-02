#coding=utf-8
#python2.7.6
"""
this file output the differences between two columns with the same name from different .csv file
eg.
python seg_diff.py training_data_stanford.csv training_data_thu.csv SegmentedInput stanford_thu_diff.csv
"""
__author__ = 'qing'
import sys, difflib, os
import pandas as pd


def diff(in_file1, in_file2, col_name, out_file):
    df1 = pd.read_csv(in_file1)
    df2 = pd.read_csv(in_file2)
    l1 = df1[col_name].tolist()
    l2 = df2[col_name].tolist()

    diff1 = []
    diff2 = []
    diff1_count = [0] * len(l1)
    total1 = 0
    diff2_count = [0] * len(l1)
    total2 = 0
    for i in range(len(l1)):
        s1 = l1[i].split()
        s2 = l2[i].split()
        dl1 = []
        dl2 = []
        total1 += len(s1)
        total2 += len(s2)
        for line in difflib.context_diff(s1, s2):
            if line.startswith('***'):
                dl = dl1
                count = diff1_count
            elif line.startswith('---'):
                dl = dl2
                count = diff2_count
                continue
            elif line.startswith('!') or line.startswith('+') or line.startswith('-'):
                dl.append(line)
                count[i] += 1
        diff1.append(" ".join(dl1))
        diff2.append(" ".join(dl2))

    diff_df = pd.DataFrame.from_records([(diff1[i], diff1_count[i], diff2[i], diff2_count[i]) for i in range(len(diff1))])
    h, name1 = os.path.split(in_file1)
    h, name2 = os.path.split(in_file2)
    diff_df.columns = [name1 + '_diff', 'count1', name2 + '_diff', 'count2']
    diff_df[name1 + '_' + col_name] = df1[col_name]
    diff_df[name2 + '_' + col_name] = df2[col_name]
    diff_df.to_csv(out_file)
    print('total difference/total of ' + name1 + ' is\n' + str(sum(diff1_count)) + '/' + str(total1))
    print('total difference/total of ' + name2 + ' is\n' + str(sum(diff2_count)) + '/' + str(total2))


if __name__ == "__main__":
    if len(sys.argv) >= 5:
        in_file1 = sys.argv[1]
        in_file2 = sys.argv[2]
        column = sys.argv[3]
        out_file = sys.argv[4]
        diff(in_file1, in_file2, column, out_file)
    else:
        print('please use this file as below:')
        print('python seg_diff.py file1.csv flle2.csv column_name file1_file2_diff.csv')