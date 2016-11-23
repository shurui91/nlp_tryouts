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










# print running time
stop = timeit.default_timer()
print("baseline_crf.py running time is " + str(stop - start))