import hw3_corpus_tool
import os, sys, timeit

# print("hello world")
# test_function.printme("does this also work???")
__author__ = "Shurui Liu"
__email__ = "shurui91@gmail.com"

# timer
start = timeit.default_timer()

# inputdir, testdir, and outputfile
# python baseline_crf.py 'inputdir/inputfile' 'outputdir/outputfile' 'output.txt'
inputdir = sys.argv[1]
testdir = sys.argv[2]
outputfile = sys.argv[3]

# try to use functions from hw3_corpus_tool.py
the_file = hw3_corpus_tool.get_utterances_from_file("labeled data/0001.csv")
print("the_file's data type is " + type(the_file))








# print running time
stop = timeit.default_timer()
print("baseline_crf.py running time is " + str(stop - start))