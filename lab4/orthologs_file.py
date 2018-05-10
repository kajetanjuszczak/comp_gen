def parser():
    with open("parsed09", "r") as f:
        prot09 = []
        for entry in f:
            entry = entry.strip("\n")
            prot09.append(entry.split(" "))
    with open("parsed20", "r") as f:
        prot20 = []
        for entry in f:
            entry = entry.strip("\n")
            prot20.append(entry.split(" "))
    with open("parsed51", "r") as f:
        prot51 = []
        for entry in f:
            entry = entry.strip("\n")
            prot51.append(entry.split(" "))
    dict09 = {}
    dict20 = {}
    dict51 = {}
    set_of_orfs = set()
    for entry in prot09:
        dict09[entry[0]] = entry
        set_of_orfs.add(entry[0])
    for entry in prot20:
        dict20[entry[0]] = entry
        set_of_orfs.add(entry[0])
    for entry in prot51:
        dict51[entry[0]] = entry
        set_of_orfs.add(entry[0])
    returndict = {}
    for entry in set_of_orfs:
        if entry in dict09:
            returndict[entry] = dict09[entry]
        if entry in dict20:
            try:
                returndict[entry] += dict20[entry]
            except KeyError:
                returndict[entry] = dict20[entry]
        if entry in dict51:
            try:
                returndict[entry] += dict51[entry]
            except KeyError:
                returndict[entry] = dict51[entry]
        returndict[entry] += "\n"
    return returndict

def write_orth():
    returndict = parser()
    with open("orth_db", "w") as w:
        for entry in returndict:
            w.write(" ".join(returndict[entry]))
            
def orth():
    """
    return 10 orthologs clusters in for of list of list(which are separate lines.)
    """
    n = 0
    list_of_10 = []
    returndict = parser()
    for entry in returndict:
        ### 13 because for things to work properly needed to add \n ###
        if len(returndict[entry]) == 13 and n < 10:
            list_of_10.append(returndict[entry])
        n += 1
    print(len(list_of_10))
    return list_of_10
def clusterfastanames():
    n = 0
    listof10 = orth()
    for line in listof10:
        w = open ("cluster_{}".format(n), "w")
        with open("allfasta.fasta") as f:
            for line2 in f:
                if line[0] == line2.strip("\n") or line[2] == line2.strip("\n") or line[6] == line2.strip("\n") or line[10] == line2.strip("\n"):
                    w.write(line2)
# =============================================================================
#                     for i in
# =============================================================================
        n += 1
        w.close()
if __name__ == "__main__":
    print(clusterfastanames())
    #print(orth())