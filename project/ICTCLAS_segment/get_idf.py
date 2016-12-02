import numpy
import csv

def get_idf(dataset):
    dic = create_dic(dataset)
    idf = {}
    D_num = 0
    with open(dataset, 'r') as csvfile:
        reader = csv.reader(csvfile)
        kb = {}
        last_standard = ""
        for line in reader:
            D_num += 1
            standard = line[5]
            query = line[6]
            for word in list(set(query.split(' '))):
                if word in idf:
                    idf[word] += 1
                else:
                    idf[word] = 1
            if standard != last_standard:
                D_num += 1
                for word in list(set(standard.split(' '))):
                    if word in idf:
                        idf[word] += 1
                    else:
                        idf[word] = 1
            last_standard = standard
    for word in idf:
        idf[word] = numpy.log(D_num) - numpy.log(idf[word])
    #idf = sorted(idf.items(), key=lambda asd:asd[1], reverse=True)
    return idf

def create_dic(dataset):
    dic = []
    with open(dataset, 'r') as csvfile:
        reader = csv.reader(csvfile)
        kb = {}
        for line in reader:
            standard = line[5]
            query = line[6]
            dic.extend(standard.split(' '))
            dic.extend(query.split(' '))
    dic = list(set(dic))
    return dic

#get_idf()