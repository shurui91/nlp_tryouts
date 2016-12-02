#coding=utf-8

import thulac
import sys
import pandas as pd
import copy
from sklearn import neighbors, datasets
from sklearn.metrics import accuracy_score
import numpy as np


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


def extract_features_with_position(df):
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

    feature = [0] * len(dict) * 2
    features = []
    labels = []
    for index, row in df.iterrows():
        labels.append([label_dict[row['问题']]])
        f = copy.deepcopy(feature)
        pos = 0
        for word in row['SegmentedInput'].split():
            f[dict[word] * 2] += 1
            f[dict[word] * 2 + 1] = pos
            pos += 1
        features.append(f)

    return np.append(np.array(features), np.array(labels), axis=1), label_dict, dict


def extract_testfeatures_with_position(df, label_dict, dict):
    feature = [0] * len(dict) * 2
    features = []
    labels = []
    for index, row in df.iterrows():
        if row['预期问题'] in label_dict:
            labels.append(label_dict[row['预期问题']])
        else:
            labels.append(0)

        f = copy.deepcopy(feature)
        for word in row['SegmentedInput'].split():
            pos = 0
            if word in dict:
                f[dict[word] * 2] += 1
                f[dict[word] * 2 + 1] = pos
            pos += 1
        features.append(f)

    return np.array(features), np.array(labels)


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


def train_model(input_file, test_file, k):
    df = preprocess_data(input_file)
    X, label_dict, dict = extract_features(df)
    r, c = X.shape
    dft = preprocess_testdata(test_file)
    Xt, yt = extract_testfeatures(dft, label_dict, dict)
    for weights in [ 'distance']:
        clf = neighbors.KNeighborsClassifier(k, weights=weights)
        clf.fit(X[:,0:c-1], X[:,c-1])
        z = clf.predict(Xt)
        print(accuracy_score(yt, z))


def train_knn(input_file, fold=3):
    df = preprocess_data(input_file)
    X,label_dict, dict = extract_features(df)
    r, c = X.shape
    np.random.shuffle(X)
    row_count = r/fold
    rows = []
    for i in range(0, fold - 1):
        rows.append([i * row_count, (i + 1) * row_count - 1])
    rows.append([(fold - 1) * row_count, r - 1])
    accuracy = [0] * fold
    for k in range(5, 15, 2):
        print("k is " + str(k))
        for i in range(0, fold):
            print("round " + str(i))
            clf = neighbors.KNeighborsClassifier(k, weights='distance')
            x1 = np.append(X[0:rows[i][0],:],X[rows[i][1] + 1: r,:],0)
            x2 = X[rows[i][0]: rows[i][1] + 1,: ]
            clf.fit(x1[:,0:c-1], x1[:, c-1])
            z = clf.predict(x2[:,0:c-1])
            accuracy[i] = accuracy_score(x2[:,c - 1], z)
        print("accuracy is " + str(k))
        print reduce(lambda x, y: x + y, accuracy) / len(accuracy)


def tune_knn():
    for k in range(3, 11, 2):
        print(k)
        train_model("test/training_data_thu.csv", "test/test_data_thu.csv", k)


if __name__ == "__main__":
    reload(sys)
    sys.setdefaultencoding('utf-8')
    tune_knn()
    #train_knn("output/train_thu_segment.csv", 3)
    #train_model("training_set/training_data_thu.csv", "testset/test_data_thu.csv", 5)
    #train_model("test/jieba_seg_train.csv", "test/jieba_seg_test.csv", 5)



