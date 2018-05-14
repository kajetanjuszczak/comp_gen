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
            returndict[entry] = dict09[entry][0] + " " + dict09[entry][2] + " "
        if entry in dict20:
            try:
                returndict[entry] += dict20[entry][2] + " "
            except KeyError:
                returndict[entry] = dict20[entry][0] + " " + dict20[entry][2] + " "
        if entry in dict51:
            try:
                returndict[entry] += dict51[entry][2] + " "
            except KeyError:
                returndict[entry] = dict51[entry][0] + " " + dict51[entry][2] + " "
        returndict[entry] += "\n"
    return returndict

def write_orth():
    returndict = parser()
    with open("orth_db", "w") as w:
        for entry in returndict:
            w.write(returndict[entry])
            
def orth():
    """
    return 10 orthologs clusters in for of list of list(which are separate lines.)
    """
    n = 0
    list_of_10 = []
    returndict = parser()
    for entry in returndict:
        ### 13 because for things to work properly needed to add \n ###
        temp = []
        temp = returndict[entry].split(" ")
        if len(temp) == 5 and n < 10:
            list_of_10.append(temp)
            n += 1
    return list_of_10

def clusterfastanames():
    """
    creates 10 files each containing one 
    """
    n = 0
    listof10 = orth()
    for line in listof10:
        w = open ("cluster_{}".format(n), "w")
        with open("allfasta.fasta") as f:
            file = f.readlines()
            for line2 in range(len(file)):
                if line[0] == file[line2].strip("\n") or line[1] == file[line2].strip("\n") or line[2] == file[line2].strip("\n") or line[3] == file[line2].strip("\n"):
                    w.write(">" + file[line2][3:5] + "\n")
                    for i in range(line2 + 1, len(file)):
                        if file[i].startswith(">"):
                            break
                        w.write((file[i]))
        n += 1
        w.close()

belvu -T u -o tree kcluster_0 >tree0
belvu -T u -o tree kcluster_1 >tree1
belvu -T u -o tree kcluster_2 >tree2
belvu -T u -o tree kcluster_3 >tree3
belvu -T u -o tree kcluster_4 >tree4
belvu -T u -o tree kcluster_5 >tree5
belvu -T u -o tree kcluster_6 >tree6
belvu -T u -o tree kcluster_7 >tree7
belvu -T u -o tree kcluster_8 >tree8
belvu -T u -o tree kcluster_9 >tree9




if __name__ == "__main__":
    print(clusterfastanames())
    #print(orth())