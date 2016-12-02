#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Vincent Na"

import pandas as pd
import numpy as np
import sklearn
import time
from os import listdir
from collections import defaultdict
from collections import Counter
from sklearn import svm
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC

def preprocess_data(df_train, df_test):
    # get labels
    targets = df_train['问题'].tolist()
    target_map = {q: i for i, q in enumerate(set(targets))}
    y_train = np.array([target_map[q] for q in targets])
    # map segmented sentences to vectors
    word_list = [set(s.split()) for s in df_train['SegmentedInput'].tolist()]
    unique_words = {i: word for i, word in enumerate(set(item for sublist in word_list for item in sublist))}
    vector_len = len(unique_words)
    X_train = np.array([[1 if unique_words[i] in words else 0 for i in range(vector_len)]
                  for words in word_list])
    # transform test data
    targets = df_test['问题'].tolist()
    y_test = np.array([target_map[q] for q in targets])
    word_list = [set(s.split()) for s in df_test['SegmentedInput'].tolist()]
    X_test = np.array([[1 if unique_words[i] in words else 0 for i in range(vector_len)]
                       for words in word_list])

    return (X_train, y_train, X_test, y_test)

if __name__ == "__main__":

    df_train = pd.read_csv(u"training_data.csv")
    df_test = pd.read_csv(u"test_data.csv")
    categories = list(set(df_train['领域'].tolist()))
    #df1 = df[df['领域'] == categories[4]]

    # Data Preprocess:
    # 1.transform segmented sentences to vectors -- X
    # 2.encode target to numerical categorical value: -- y
    start_time = time.time()
    print("Start Data Preprocess")
    X_train, y_train, X_test, y_test = preprocess_data(df_train, df_test)
    print("End Data Preprocess:", time.time() - start_time, "s elapsed")

    print("Start Training")
    clf = OneVsRestClassifier(LinearSVC(random_state=0))
    clf.fit(X_train, y_train)
    print("End Training:", time.time() - start_time, "s elapsed")

    print("Start Prediction")
    yhat = clf.predict(X)
    print("End Prediction:", time.time() - start_time, "s elapsed")

    identicals = [y[i] == yhat[i] for i in range(len(y))]
    print("Total: ", len(y), " Correctly-Classified: ", len([i for i in identicals if i]),
          " Accuracy: ", len([i for i in identicals if i]) / len(y))
    """
    svc = svm.SVC(kernel='linear')
    svc.fit(X, y)
    yhat = svc.predict(X)
    # Prediction"""