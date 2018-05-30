import statistics_script

def complement(filename):
    seq = statistics_script.tostring(filename).replace("G", "c").replace("C", "g").replace("A", "t").replace("T", "a").upper()
    seq = seq[::-1]
    return seq
def orfsforward(filename): 
    seq = statistics_script.tostring(filename)
    list_of_treenuclf = []
    for i in range(3):
        forward = []
        for j in range(i ,len(seq), 3):
            forward.append(seq[j:j+3])
        list_of_treenuclf.append(forward)
    orflist = []
    stop = ["TGA", "TAA", "TGA"]
    for l in list_of_treenuclf:
        temp = 0
        for trin in range(len(l)):
            if l[trin] == "ATG" and trin >  temp:
                orf = []
                for i in range(trin, len(l)):
                    orf.append(l[i])
                    if l[i] in stop:
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
    forwardorfs = orfsforward(filename)
    reverseorfs = orfsreverse(filename)  
    with open("../results/orfs_{}".format(i), "w") as w:
        count = 0
        stop = ["TGA", "TAA", "TGA"]
        for i in forwardorfs:
            if len(i) > 100 and i[-1] in stop:
                w.write(">orf_{} \n{}\n".format(count, "".join(i)))
                count+=1
        count = 0
        for i in reverseorfs:
            if len(i) > 100 and i[-1] in stop:
                w.write(">orf_{}_rev \n{}\n".format(count, "".join(i)))
                count+=1
list_names = ["03", "09", "20", "24", "51"]
for i in list_names:
    writeintofile(("../../genomes/{}.fa.txt".format(i)), i)
    
# =============================================================================
# if __name__ == "__main__":
#     writeintofile("./genomes/03.fa.txt")
# =============================================================================
