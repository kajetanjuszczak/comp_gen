import statistics_script

"""
creates string with reverse strand
"""
def complement(filename):
    seq = statistics_script.tostring(filename).replace("G", "c").replace("C", "g").replace("A", "t").replace("T", "a").upper()
    seq = seq[::-1]
    return seq
def orfsforward(filename): 
    """
    takes string - sequence of genome outputs list of forward orfs.
    conditions for orfs:
    Start codon = AUG 
    Stop codos = "TGA", "TAA", "TGA"
    does not allow overlaps in same reading frame.
    """
    seq = statistics_script.tostring(filename)
    list_of_treenuclf = []
    ### in order to get all possible frameshifts we create 3 lists with frameshift = 1 
    for i in range(3):
        forward = []
        for j in range(i ,len(seq), 3):
            forward.append(seq[j:j+3])
        list_of_treenuclf.append(forward)
    orflist = []
    stop = ["TGA", "TAA", "TGA"]
    for l in list_of_treenuclf:
        ###for all 3 lists
        temp = 0
        for trin in range(len(l)):
            #if we find start codon and its index is higher than stop codon for previous orf.
            if l[trin] == "ATG" and trin >  temp:
                orf = []
                for i in range(trin, len(l)):
                    orf.append(l[i])
                    if l[i] in stop:
                        break
                    temp = i
                    #stores value of current last codon index - for overlaping restriction
                orflist.append(orf)
    return orflist

def orfsreverse(filename): 
    """
    very similar script for reverse strand allow us to distinguis forward and reverse orfs.
    """
    comp = complement(filename)
    list_of_treenuclr = []
    for i in range(3):
        reverse = []
        for j in range(i ,len(comp), 3):
            reverse.append(comp[j:j+3])
        list_of_treenuclr.append(reverse)
    orflist = []
    stop = ["TGA", "TAA", "TGA"]
    for l in list_of_treenuclr:
        temp = 0
        for trin in range(len(l)):
            if l[trin] == "ATG" and trin > temp:
                orf = []
                for i in range(trin, len(l)):
                    orf.append(l[i])
                    if l[i] in stop:
                        break
                    temp = i
                orflist.append(orf)
    return orflist
    
def writeintofile(filename, i):
    """
    write orfs into file only if length of orf is over 100 codons
    counting to have different orfnames
    """
    forwardorfs = orfsforward(filename)
    reverseorfs = orfsreverse(filename)  
    with open("../results/orfs_{}".format(i), "w") as w:
        count = 0
        stop = ["TGA", "TAA", "TGA"]
        for i in forwardorfs:
            #i[-1] to control if our orfs are not artefacts
            if len(i) > 100 and i[-1] in stop:
                w.write(">orf_{} \n{}\n".format(count, "".join(i)))
                count+=1
        count = 0
        for i in reverseorfs:
            if len(i) > 100 and i[-1] in stop:
                w.write(">orf_{}_rev \n{}\n".format(count, "".join(i)))
                count+=1
                
# easu way to call function multiple times
list_names = ["03", "09", "20", "24", "51"]
for i in list_names:
    writeintofile(("../../genomes/{}.fa.txt".format(i)), i)
    
# =============================================================================
# if __name__ == "__main__":
#     writeintofile("./genomes/03.fa.txt")
# =============================================================================
