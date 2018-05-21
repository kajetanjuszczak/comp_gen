#! /usr/bin/env python
"prints first argument aa sequences of length second argument to screen"
import random
import sys
def dictionary():
    file = open("./input/09.fa.txt.pfa", "r")
    count = 0
    for line in file: 
        if line.startswith(">"):
            count+=1
    number = count
    length=20
    aas="ARNDCEQGHILKMFPSTWYV"
    def r20():
        return random.randrange(20)
    dictionary = {}
    for i in range(number + 1):
        s=""
        for j in range(length):
            s+=aas[r20()]
        dictionary[i] = s
    return dictionary
def longrandomseq():
    dictionary1 = dictionary()
    with open("longrandomseqsA", "w") as w:
        prot_list = ["03", "09", "20", "51"]
        for prot_name in prot_list:
            with open("out_{}b".format(prot_name)) as f:
                templist = []
                for line in f:
                    templist.append(dictionary1[int(line)])
                w.write(">{}\n{}\n".format(prot_name, "".join(templist)))
                
if __name__ == "__main__":
    print(dictionary())
    print(longrandomseq())