#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Vincent Na"

from nltk.tokenize.stanford_segmenter import StanfordSegmenter
import pandas as pd
import timeit
from os import listdir

segmenter = StanfordSegmenter(path_to_jar="stanford-segmenter/stanford-segmenter-3.6.0.jar",
                              path_to_slf4j="stanford-segmenter/slf4j-api.jar",
                              path_to_sihan_corpora_dict="stanford-segmenter/data",
                              path_to_model="stanford-segmenter/data/pku.gz",
                              path_to_dict="stanford-segmenter/data/dict-chris6.ser.gz")


def raw_data_to_df(path_to_data, mode='train'):
    # load data
    files = listdir(path_to_data)
    df_list = [pd.read_excel(path_to_data + name) for name in files if name.endswith(u".xls")]
    if mode != 'train':
        categories = [name[:len(name)-7] for name in files if name.endswith(u".xls")]
        for i in range(len(df_list)):
            names = pd.DataFrame.from_records([tuple([categories[i]])] * len(df_list[i]))
            df_list[i]['领域'] = names
    combined_df = pd.concat(df_list)
    if mode != 'train':
        combined_df.columns = ['编号', '扩展问题', '问题', '领域']
    lx = "##".join(combined_df['扩展问题'].tolist())
    ly = "##".join(combined_df['问题'].tolist())

    # segment sentences, this part can be replaced by other segmenters
    segmented_lx = segmenter.segment(lx)
    segmented_ly = segmenter.segment(ly)

    segmented_lx = segmented_lx.split('##')
    segmented_ly = segmented_ly.split('##')
    segmented_df = pd.DataFrame.from_records([(segmented_lx[i], segmented_ly[i]) for i in range(len(segmented_lx))])
    segmented_df.columns = ['SegmentedInput', 'SegmentedTarget']

    # concate segmented questions to the combined data frame
    combined_df['SegmentedInput'] = segmented_df['SegmentedInput']
    combined_df['SegmentedTarget'] = segmented_df['SegmentedTarget']
    return combined_df

print('Start processing training data')
training_files_path = u"导入的郑州银行知识库/扩展问题/"
train_df = raw_data_to_df(training_files_path)
# write to csv
train_df.to_csv('training_data.csv', encoding='utf-8')

print('Start processing test data')
test_files_path = u"导入的郑州银行知识库/测试集/"
test_df = raw_data_to_df(test_files_path,mode='test')
# write to csv
test_df.to_csv('test_data.csv', encoding='utf-8')