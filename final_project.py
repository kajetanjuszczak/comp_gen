"""

"""
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
    for i in listofdi:
        print("{} content is {}".format(i , seq.count(i)/(len(seq) - 1)))
        
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
        for trin in range(len(l)):
            if l[trin] == "ATG":
                orf = []
                for i in range(trin, len(l)):
                    orf.append(l[i])
                    if l[i] == "TGA" or l[i] == "TAA" or l[i] == "TGA":
                        break
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
        for trin in range(len(l)):
            if l[trin] == "ATG":
                orf = []
                for i in range(trin, len(l)):
                    orf.append(l[i])
                    if l[i] == "TGA" or l[i] == "TAA" or l[i] == "TGA":
                        break
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

def distancematrixtool(filename):
    pass
    
            
        
if __name__ == "__main__":
    print(writeintofile("./genomes/03.fa.txt"))
