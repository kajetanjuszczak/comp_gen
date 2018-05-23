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
def orfs(filename): 
    seq = tostring(filename)
    comp = complement(filename)
    list_of_treenucl = []
    for i in range(3):
        forward = []
        reverse = []
        for j in range(i ,len(seq), 3):
            forward.append(seq[j:j+3])
            reverse.append(comp[j:j+3])
        list_of_treenucl.append(forward)
        list_of_treenucl.append(reverse)
    for l in list_of_treenucl:
        temp = []
        for trin in range(len(l)):
            if l[trin] == "ATG":
                orf = []
                for i in range(trin, len(l)):
                    orf.append(l[i])
                    if l[i] == "TGA" or l[i] == "TAA" or l[i] == "TGA":
                        break
                temp.append(orf)
    orf_list = []
    for i in temp:
        if len(i) > 100:
            orf_list.append(i)
    print(len(orf_list))
            
            
        
if __name__ == "__main__":
#==============================================================================
#     GC("./genomes/03.fa.txt")
#     dinucleotides("./genomes/03.fa.txt")
#==============================================================================
#==============================================================================
#     print(complement("./genomes/03.fa.txt"))
#==============================================================================
    print(orfs("./genomes/03.fa.txt"))
