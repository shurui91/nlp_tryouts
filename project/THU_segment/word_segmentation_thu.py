#coding=utf-8

import thulac
import sys
import pandas as pd
from os import listdir
import csv
import xlwt
import os
import numpy as np

def segment(input, output, seg_only):
    if seg_only:
        thu2 = thulac.thulac("-seg_only -input " + input + " -output " + output) #设置模式为分词和词性标注模式
    else:
        thu2 = thulac.thulac("-input " + input + " -output " + output) #设置模式为分词和词性标注模式
    thu2.run() #根据参数运行分词和词性标注程序，从cs.txt文件中读入，屏幕输出结果


def parse_file(in_dir, out_dir, type, seg_only):
    print(in_dir)
    files = listdir(in_dir)

    for name in files:
        if name.endswith(".xls"):
            df = pd.read_excel(os.path.join(in_dir, name))

            if type == "tr":
                l = df['扩展问题'].tolist()
            else:
                l = df['预期问题'].tolist()

            with open(out_dir + "col1.txt", 'w') as outfile:
                outfile.write("\n".join(l))
            l = df['问题'].tolist()
            with open(out_dir + "col2.txt", 'w') as outfile:
                outfile.write("\n".join(l))

            segment(out_dir + "col1.txt", out_dir + "col1s.txt", seg_only)
            segment(out_dir + "col2.txt", out_dir + "col2s.txt", seg_only)

            with open(out_dir + 'col1s.txt') as f:
                l1 = f.read().splitlines()

            with open(out_dir + 'col2s.txt') as f:
                 l2 = f.read().splitlines()

            df1 = pd.DataFrame(l1, columns=['SegmentedTarget'])
            df2 = pd.DataFrame(l2, columns=['SegmentedInput'])

            df['SegmentedInput'] = df2['SegmentedInput']
            df['SegmentedTarget'] = df1['SegmentedTarget']

            df.to_csv(os.path.join(out_dir, name + "thu_segment"+ ".csv"), index=False)
    df = [pd.read_csv(os.path.join(out_dir, name + "thu_segment"+ ".csv")) for name in files if name.endswith(".xls")]
    df = pd.concat(df, axis=0)
    df.to_csv(os.path.join(out_dir, "thu_segment"+ ".csv"), index=False)


if __name__ == "__main__":
    reload(sys)
    sys.setdefaultencoding('utf-8')
    if len(sys.argv) >= 5:
        input = sys.argv[1]
        output = sys.argv[2]
        data_type = sys.argv[3]
        seg_only = sys.argv[4]
        parse_file(input, output, data_type, seg_only == 'true')


