import numpy as np
import math as math

def tostring(filename):
    with open(filename, "r") as f:
        seq = ""
        for line in f:
            if line.startswith(">") == False:
                seq += line
    return seq
    
def GC(filename):
    seq = tostring(filename)
    gc_count = seq.count("G") + seq.count("C")
    odd_nucl = seq.count("N")
    print(gc_count/(len(seq) - odd_nucl) * 100)
    
def dinucleotides(filename):
    seq = tostring(filename)
    listofdi = ["AG", "AA", "AC", "AT","CG", "CA", "CC", "CT","GG", "GA", "GC", "GT", "TG", "TA", "TC", "TT"]
    listoffreq = []
    for i in listofdi:
        #print("{} content is {}".format(i , seq.count(i)/(len(seq) - 1)))
        listoffreq.append((seq.count(i)/(len(seq) - 1 - 2*seq.count("N"))*100))
    return listoffreq
        
        
def complement(filename):
    seq = tostring(filename).replace("G", "c").replace("C", "g").replace("A", "t").replace("T", "a").upper()
    seq = seq[::-1]
    return seq
def orfsforward(filename): 
    seq = tostring(filename)
    list_of_treenuclf = []
    for i in range(3):
        forward = []
        for j in range(i ,len(seq), 3):
            forward.append(seq[j:j+3])
        list_of_treenuclf.append(forward)
    orflist = []
    for l in list_of_treenuclf:
        temp = 0
        for trin in range(len(l)):
            if l[trin] == "ATG" and trin >  temp:
                orf = []
                for i in range(trin, len(l)):
                    orf.append(l[i])
                    if l[i] == "TGA" or l[i] == "TAA" or l[i] == "TGA":
                        break
                    temp = i
                orflist.append(orf)
    return orflist
def orfsreverse(filename): 
    comp = complement(filename)
    list_of_treenuclr = []
    for i in range(3):
        reverse = []
        for j in range(i ,len(comp), 3):
            reverse.append(comp[j:j+3])
        list_of_treenuclr.append(reverse)
    orflist = []
    for l in list_of_treenuclr:
        temp = 0
        for trin in range(len(l)):
            if l[trin] == "ATG" and trin > temp:
                orf = []
                for i in range(trin, len(l)):
                    orf.append(l[i])
                    if l[i] == "TGA" or l[i] == "TAA" or l[i] == "TGA":
                        break
                    temp = i
                orflist.append(orf)
    return orflist
    
def writeintofile(filename):
    forwardorfs = orfsforward(filename)
    reverseorfs = orfsreverse(filename)  
    with open("writefile", "w") as w:
        count = 0
        for i in forwardorfs:
            if len(i) > 100:
                w.write(">orf_{} \n{}\n".format(count, "".join(i)))
                count+=1
        count = 0
        for i in reverseorfs:
            if len(i) > 100:
                w.write(">orf_{}_rev \n{}\n".format(count, "".join(i)))
                count+=1
def vectors(list1, list2):
    list_of_substracted = []
    for index in range(len(list1)):
        list_of_substracted.append((list1[index] - list2[index])**2)
    return math.sqrt(sum(list_of_substracted))
    
def distancematrixtool(genome1, genome2, genome3, genome4, genome5):
    matrix = np.zeros((5,5))
    listoffreq = [dinucleotides(genome1), dinucleotides(genome2), dinucleotides(genome3), dinucleotides(genome4), dinucleotides(genome5)]
    for i in range(len(listoffreq)):
        for j in range(len(listoffreq)):
            matrix[i, j] = vectors(listoffreq[i], listoffreq[j])
    print(matrix)
    
            
        
if __name__ == "__main__":
#==============================================================================
#     print(writeintofile("./genomes/03.fa.txt"))
#==============================================================================
#==============================================================================
#     print(orfsreverse("./genomes/03.fa.txt"))
#==============================================================================
    distancematrixtool("./genomes/03.fa.txt", "./genomes/09.fa.txt", "./genomes/20.fa.txt", "./genomes/24.fa.txt", "./genomes/51.fa.txt")
