"""
requires input of name of xlm file
outputs pirnt with correc format
"""
import sys
import re
from Bio.Blast import NCBIXML

blastOutputXMLFile = sys.argv [1]

blastOutputXMLHandle = open (blastOutputXMLFile)

listOfBlastRecords = NCBIXML.parse (blastOutputXMLHandle)

for aSingleBlastRecord in listOfBlastRecords:
    for i in range (len (aSingleBlastRecord.alignments)):
        description = aSingleBlastRecord.descriptions [i]
        alignment = aSingleBlastRecord.alignments [i]
        title = re.compile ("gnl\|BL_ORD_ID\|\d* ").sub ("", description.title)
        query = aSingleBlastRecord.query
        print (">{} {} >{} {}".format(query, alignment.hsps[0].query, title, alignment.hsps[0].sbjct))
        break