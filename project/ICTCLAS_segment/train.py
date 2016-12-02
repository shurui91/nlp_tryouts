# -*- coding:utf-8 -*-
import csv
import xlrd
import numpy
import sys
import get_idf
import pickle

def match_two_sentence(query1, query2):
    query1 = query1.split(' ')
    query2 = query2.split(' ')
    #query1 = list(set(query1))
    #query2 = list(set(query2))
    score = 0
    for word1 in query1:
        for word2 in query2:
            if word1 == word2:
                    score += 1
    #return float(score) / (len(query1) + len(query1))
    return float(score) / numpy.sqrt(len(query1)*len(query2))

def match2_two_sentence(query1, query2, idf):
    query1 = query1.split(' ')
    query2 = query2.split(' ')
    #count the word frequency in queries
    q1 = {}
    for word in query1:
        if word in q1:
            q1[word] += 1
        else:
            q1[word] = 1
    q2 = {}
    for word in query2:
        if word in q2:
            q2[word] += 1
        else:
            q2[word] = 1

    score = 0
    for word1 in q1:
        for word2 in q2:
            if word1 == word2:
                if word1 in idf:
                    score += (q1[word1]*idf[word1]*q2[word2]*idf[word2])
                else:
                    score += 3
    de1 = 0
    de2 = 0
    for word1 in q1:
        if word1 in idf:
            de1 += pow(q1[word1]*idf[word1],2)
        else:
            de1 += 9
    for word2 in q2:
        if word2 in idf:
            de2 += pow(q2[word2]*idf[word2],2)
        else:
            de2 += 9
    return float(score) / numpy.sqrt(de1*de2)

def match3_two_sentence(query1, query2, impt_words):
    query1 = query1.split(' ')
    query2 = query2.split(' ')
    # query1 = list(set(query1))
    # query2 = list(set(query2))
    hit = 0
    for word1 in query1:
        for word2 in query2:
            if word1 == word2:
                if word1 in impt_words['重要']:
                    hit += 1.5
                elif word1 in impt_words['一般']:
                    hit += 1.3
                elif word1 in impt_words['不重要']:
                    hit += 0.7
                else:
                    hit += 1
    return float(hit) / numpy.sqrt(len(query1) * len(query2))

def match4_two_sentence(query1, query2, syns):
    query1 = query1.split(' ')
    query2 = query2.split(' ')
    #query1 = list(set(query1))
    #query2 = list(set(query2))
    hit = 0
    for word1 in query1:
        for word2 in query2:
            if word1 == word2:
                hit += 1
            elif (word1 in syns and word2 in syns[word1]) or \
                        (word2 in syns and word1 in syns[word2]):
                hit += 0.8
    return float(hit) / numpy.sqrt(len(query1) * len(query2))

def match5_two_sentence(query1, query2, syns, impt_words):
    query1 = query1.split(' ')
    query2 = query2.split(' ')
    #query1 = list(set(query1))
    #query2 = list(set(query2))
    hit = 0
    for word1 in query1:
        for word2 in query2:
            if word1 == word2:
                if word1 in impt_words['重要']:
                    hit += 1.5
                elif word1 in impt_words['一般']:
                    hit += 1.3
                elif word1 in impt_words['不重要']:
                    hit += 0.7
                else:
                    hit += 1
            elif (word1 in syns and word2 in syns[word1]) or \
                        (word2 in syns and word1 in syns[word2]):
                    hit += 1.2

    return float(hit)/numpy.sqrt(len(query1)*len(query2))

def read_synomnies():
    data = xlrd.open_workbook('./同义词和重要词/同义词.xls')
    table = data.sheets()[0]
    nrows = table.nrows
    syns = {}
    for rownum in range(1,nrows):
        sims =  table.row_values(rownum)[1]
        sims = sims.split(',')
        for sim in sims:
            tempsims = sims
            tempsims.remove(sim)
            syns[sim] = tempsims
    return syns

def read_important_words():
    data = xlrd.open_workbook('./同义词和重要词/重要词.xls')
    table = data.sheets()[0]
    nrows = table.nrows
    important_words = {}
    important_words['不重要'] = []
    important_words['重要'] = []
    important_words['一般'] = []
    for rownum in range(1, nrows):
        word = table.row_values(rownum)[1]
        importance = table.row_values(rownum)[2]
        important_words[importance].append(word)
    return important_words

def create_kb(dataset, testdata):
    with open(dataset, 'r') as csvfile:
        reader = csv.reader(csvfile)
        kb = {}
        for line in reader:
            standard = line[5]
            query = line[6]
            if standard in kb:
                kb[standard].append(query)
            else:
                kb[standard] = [query]
        print ("kb save finished")
    with open(testdata,'r') as testfile:
        reader = csv.reader(testfile)
        test_query = {}
        for line in reader:
            query = line[3]
            answer = line[4]
            test_query[query] = answer
        print ('test data get finished')
    return (kb, test_query)

def QA(kb, test_queries, syns, impt_words, idf, dataset, testdata, model):
    f_result = open("./report/result.txt","a")
    length = len(test_queries)
    print (length)
    best_match = ['']*len(test_queries)
    idx = 0
    hit = 0
    alpha = 0.5
    hhit =0
    test_queries = sorted(test_queries.items(), key=lambda asd:len(asd[0]))
    while idx < length:
        test_query = test_queries[idx][0]
        max_score = 0
        for (standard, queries) in kb.items():
            if model == '1':
                score1 = match_two_sentence(test_query, standard)
                for source_query in queries:
                    score2 = match_two_sentence(test_query, source_query)
            elif model == '2':
                score1 = match2_two_sentence(test_query, standard, idf)
                for source_query in queries:
                    score2 = match2_two_sentence(test_query, source_query, idf)
            elif model == '3':
                score1 = match3_two_sentence(test_query, standard, impt_words)
                for source_query in queries:
                    score2 = match3_two_sentence(test_query, source_query, impt_words)
            elif model == '4':
                score1 = match4_two_sentence(test_query, standard, syns)
                for source_query in queries:
                    score2 = match4_two_sentence(test_query, source_query, syns)
            elif model == '5':
                score1 = match5_two_sentence(test_query, standard, syns, impt_words)
                for source_query in queries:
                    score2 = match5_two_sentence(test_query, source_query, syns, impt_words)
            else:
                score13 = match3_two_sentence(test_query, standard, syns, impt_words)
                score12 = match2_two_sentence(test_query, standard, idf)
                score11 = match_two_sentence(test_query, standard)
                score21 = []
                score22 = []
                score23 = []
                for source_query in queries:
                    score23.append(match3_two_sentence(test_query, source_query, syns, impt_words))
                    score22.append(match2_two_sentence(test_query, source_query, idf))
                    score21.append(match_two_sentence(test_query, source_query))
                score21 = sum(score21)/len(queries)
                score22 = sum(score22) / len(queries)
                score23 = sum(score23) / len(queries)

                score1 = sum(numpy.array([0.4,0.4,0.2])*numpy.array([score11,score12,score13]))
                score2 = sum(numpy.array([4,4,2])*numpy.array([score21,score22,score23]))

            if test_queries[idx][1] == standard:
                s1 = score1
                s2 = score2
            if score1 + score2 > max_score:
                max_score = score1+score2
                best_match[idx] = standard

        if best_match[idx] == test_queries[idx][1]:
            hit += 1
            hhit += 1
        #else:
        #    f_miss.write(str(idx)+',,,'+test_query+',,,'+str(round(s1+s2,3))\
        #                 +',,,'+test_queries[idx][1]+'\n')
        #    f_miss.write(str(idx)+',,,'+test_query+',,,'+str(round(max_score,3))\
        #                +',,,'+best_match[idx]+'\n')
        idx += 1
        if idx%100 == 0:
            print (dataset + '\t' + model + '\t' + str(float(hit) / idx))
            #print(float(hit) / idx,  float(hhit)/100)
            hhit = 0
    f_result.write(dataset + '\t' + model + '\t' + str(float(hit) / length) + '\n')
    print ('match finished!')


if __name__ == '__main__':
    datasets = ['ICTCLAS.csv']
    testdatas = ['test.csv']
    syns = read_synomnies()
    important_words = read_important_words()
    f_record = open('record.txt', 'rb')
    models = ['1','2','3','4','5','6']
    # pickle.dump((kb,test_queries,idf,syns,important_words), f_record)
    # kb, test_queries, idf, syns, important_words = pickle.load(f_record)
    for i in range(len(datasets)):
        dataset = datasets[i]
        testdata = testdatas[i]
        idf = get_idf.get_idf(dataset)
        kb, test_queries = create_kb(dataset, testdata)
        for model in models:
            QA(kb, test_queries, syns, important_words, idf, dataset, testdata, model)