from Bio import Seq

def Readfiles(filename1, filename2):
    with open(filename1, "r") as f:
        orf_list1 = []
        for line in f:
            if line.startswith(">") == False:
                orf_list1.append((Seq.translate(line)).strip("*"))
    with open(filename2, "r") as f:
        orf_list2 = []
        f1 = f.readlines()
        for line in range(len(f1)):
            if f1[line].startswith(">"):
                temp =[]
                for i in range(line + 1, len(f1)):
                    if f1[i].startswith(">"):
                        break
                    temp.extend(f1[i].rstrip())
                orf_list2.append("".join(temp))
    return orf_list1, orf_list2

def TP(filename1, filename2):
    my = Readfiles(filename1, filename2)[0]
    prog = Readfiles(filename1, filename2)[1]
    TP = 0
    for i in my:
        if i in prog:
            TP += 1
    return TP
def FP(filename1, filename2):
    my = Readfiles(filename1, filename2)[0]
    prog = Readfiles(filename1, filename2)[1]
    FP = 0
    for i in my:
        if i not in prog:
            FP += 1
    return FP
def FN(filename1, filename2):
    my = Readfiles(filename1, filename2)[0]
    prog = Readfiles(filename1, filename2)[1]
    FN = 0
    for i in prog:
        if i not in my:
            FN += 1
    return FN
def numberorfs(filename1, filename2, i):
    print("nr of orfs predicted for {} = {}".format(i, (len(Readfiles(filename1, filename2)[0]))))
    
def F1(filename1, filename2):
    precision=float(TP(filename1, filename2))/(TP(filename1, filename2)+FP(filename1, filename2))
    recall=float(TP(filename1, filename2))/(TP(filename1, filename2)+FN(filename1, filename2))
    return 2*((precision*recall)/(precision+recall))
# =============================================================================
# list_names = ["03", "09", "20", "24", "51"]
# for i in list_names:
#     numberorfs("orfs_{}".format(i), "./lab2/{}.fa.txt.pfa".format(i), i)
#     print("F1 for {} is {}".format(i, F1("orfs_{}".format(i), "./lab2/{}.fa.txt.pfa".format(i))))
# =============================================================================
if __name__ == "__main__":
    Readfiles("writefile", "./lab2/03.fa.txt.pfa")
