import hw3_corpus_tool
import os, sys, timeit

print("hello world")

# timer
start = timeit.default_timer()

# inputdir, testdir, and outputfile
# python baseline_crf.py 'inputdir/inputfile' 'outputdir/outputfile' 'output.txt'
inputdir = sys.argv[1]
testdir = sys.argv[2]
outputfile = sys.argv[3]









# print running time
stop = timeit.default_timer()
print ("per_learn.py running time is " + str(stop - start))