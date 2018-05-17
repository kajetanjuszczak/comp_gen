import sys, re
partOfCluster = {}

bHandle = open("input/orth_db", "r")

lines = bHandle.readlines ()

id = 0

for aLine in lines:

    aLine = aLine.replace ("\n", "")
    words = aLine.split ("\t")
    print (words)

    for aWord in words:

        if not partOfCluster in aWord:

            partOfCluster [aWord] = id

        id = id + 1