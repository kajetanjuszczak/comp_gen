#! /usr/bin/env python
"prints first argument aa sequences of length second argument to screen"
import random
import sys
#==============================================================================
# def stuff():
#     number=int(sys.argv[1])
#     length=int(sys.argv[2])
#     number=10
#     length=30
#     aas="ARNDCEQGHILKMFPSTWYV"
#     def r20():
#         return random.randrange(20)
#     for i in range(number):
#         s=""
#         for j in range(length):
#             s+=aas[r20()]
#         print(s)
#==============================================================================
def longrandomseq():
    with open("longrandomseqs", "w") as w:
        prot_list = ["03", "09", "20", "51"]
        for prot_name in prot_list:
            file = open("./input/{}.fa.txt.pfa".format(prot_name), "r")
            count = 0
            for line in file: 
                if line.startswith(">"):
                    count+=1
            number = count
            print(number)
            length=20
            aas="ARNDCEQGHILKMFPSTWYV"
            def r20():
                return random.randrange(20)
            templist = []
            for i in range(number + 1):
                s=""
                for j in range(length):
                    s+=aas[r20()]
                templist.append(s)
            w.write(">{}\n{}\n".format(prot_name, "".join(templist)))
        
    
if __name__ == "__main__":
    print(longrandomseq())