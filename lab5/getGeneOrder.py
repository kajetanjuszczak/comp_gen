import sys, re

# acquire first needed data

geneOrderList = []

aHandle = open(sys.argv[1])

lines = aHandle.readlines ()

for aLine in lines:

    aLine = aLine.replace ("\n", "")

    if aLine.startswith (">"):

		# print aLine [1:len (aLine)],
        geneOrderList.append (aLine [1:len (aLine)])

# acquire second needed data

partOfCluster = {}

bHandle = open(sys.argv[2])

lines = bHandle.readlines ()

id = 0

for aLine in lines:

    aLine = aLine.replace ("\n", "")
    aLine = aLine.replace (">", "")
    words = aLine.split(" ")
    for aWord in words:
        if not partOfCluster.has_key (aWord):

            partOfCluster [aWord] = id

        id = id + 1

# put together

for aGene in geneOrderList:
    
	if partOfCluster.has_key (aGene):

		print partOfCluster [aGene],