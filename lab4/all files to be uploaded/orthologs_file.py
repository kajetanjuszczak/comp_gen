def parser():
# =============================================================================
#     reading in all the files into lists of lines, each line is also consisting of list of 4 strings in format:
#     <template id><template seq><query id><query seq>
# =============================================================================
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
# =============================================================================
#     creating set which consist all of orfs present in reference genome and dictionaries in a format:
#     key = name of orf in reference genome, value = line in parsed code
# =============================================================================
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
# =============================================================================
#     running a loop taking one gene from reference genome at a time as key and assigning names of best hits from other genomes
# =============================================================================
    for entry in set_of_orfs:
        if entry in dict09:
            returndict[entry] = "{} {} ".format(dict09[entry][0], dict09[entry][2])
        if entry in dict20:
            try:
                returndict[entry] += "{} ".format(dict20[entry][2])
            except KeyError:
                returndict[entry] = "{} {} ".format(dict20[entry][0], dict20[entry][2])
        if entry in dict51:
            try:
                returndict[entry] += "{} ".format(dict51[entry][2])
            except KeyError:
                returndict[entry] = "{} {} ".format(dict51[entry][0], dict51[entry][2])
# =============================================================================
#         "\n" to indicate start of new line for another entry
# =============================================================================
        returndict[entry] += "\n"
    return returndict

def write_orth():
    """
    creates file with lists of names of orthologs
    """
    returndict = parser()
    with open("orth_db", "w") as w:
        for entry in returndict:
            w.write(returndict[entry])
            
def orth():
    """
    return 10 orthologs clusters in forn of list of list(which are separate lines.)
    """
# =============================================================================
#     n used as counter to get only 10 clusters
# =============================================================================
    n = 0
    list_of_10 = []
    returndict = parser()
    for entry in returndict:
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
# =============================================================================
#     n is used to create variable in filename
# =============================================================================
    n = 0
    listof10 = orth()
    for line in listof10:
        w = open ("cluster_{}".format(n), "w")
# =============================================================================
#         reading from fasta file containing all entries from all genomes
# =============================================================================
        with open("allfasta.fasta") as f:
# =============================================================================
#             using readlines because to append lines with aminoacids indexing is necessary
# =============================================================================
            file = f.readlines()
            for line2 in range(len(file)):
# =============================================================================
#                 check for > indicating fasta entry 
# =============================================================================
                if line[0] == file[line2].strip("\n") or line[1] == file[line2].strip("\n") or line[2] == file[line2].strip("\n") or line[3] == file[line2].strip("\n"):
                    w.write(">" + file[line2][3:5] + "\n")
# =============================================================================
#                     writes next lines untill another > indicating next fasta entry is found
# =============================================================================
                    for i in range(line2 + 1, len(file)):
                        if file[i].startswith(">"):
                            break
                        w.write((file[i]))
        n += 1
        w.close()


if __name__ == "__main__":
    print(clusterfastanames())
    #print(parser())
    #print(orth())