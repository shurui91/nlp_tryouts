#coding=utf-8

__author__ = 'qing'
import numpy as np
import copy
import pandas as pd


def extract_features(df):
    label = 0
    label_dict = {}
    dict = {}
    idx = 0
    for index, row in df.iterrows():
        if not row['问题'] in label_dict:
            label_dict[row['问题']] = label
            label += 1
        for word in row['SegmentedInput'].split():
            if not word in dict:
                dict[word] = idx
                idx += 1

    feature = [0] * len(dict)
    features = []
    labels = []
    for index, row in df.iterrows():
        labels.append([label_dict[row['问题']]])
        f = copy.deepcopy(feature)
        pos = 0
        for word in row['SegmentedInput'].split():
            f[dict[word]] += 1
        features.append(f)

    return np.append(np.array(features), np.array(labels), axis=1), label_dict, dict


def extract_testfeatures(df, label_dict, dict):
    feature = [0] * len(dict)
    features = []
    labels = []
    for index, row in df.iterrows():
        if row['问题'] in label_dict:
            labels.append(label_dict[row['问题']])
        else:
            labels.append(0)

        f = copy.deepcopy(feature)
        for word in row['SegmentedInput'].split():
            if word in dict:
                f[dict[word]] += 1
        features.append(f)

    return np.array(features), np.array(labels)

def preprocess_data(input_file):
    df = pd.read_csv(input_file)

    dict = {}
    for index, row in df.iterrows():
        row['扩展问题'] = row['问题']
        if not row['问题'] in dict:
            dict[row['问题']] = row

    df = df.append(list(dict.itervalues()), ignore_index=True)
    return df

def preprocess_testdata(input_file):
    df = pd.read_csv(input_file)
    return df
