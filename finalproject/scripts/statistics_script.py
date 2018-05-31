from Bio import Seq
import matplotlib.pyplot as plt

def tostring(filename):
    """
    input: genome file
    output: string - seq - whole genome as one string 
    """
    with open(filename, "r") as f:
        seq = ""
        for line in f:
            if line.startswith(">") == False:
                seq += line
    return seq
    
def GC(filename):
    """
    counts number of Gs and Cs in genome and prints GC content in precentage format (odd_nucleotides - N excluded from total lenght of sequence)
    """
    seq = tostring(filename)
    gc_count = seq.count("G") + seq.count("C")
    odd_nucl = seq.count("N")
    print(gc_count/(len(seq) - odd_nucl) * 100)
    
def dinucleotides(filename):
    """
    for list of all possible nucleotides return their frequency in percent value
    """
    seq = tostring(filename)
    listofdi = ["AG", "AA", "AC", "AT","CG", "CA", "CC", "CT","GG", "GA", "GC", "GT", "TG", "TA", "TC", "TT"]
    listoffreq = []
    for i in listofdi:
        #print("{} content is {}".format(i , seq.count(i)/(len(seq) - 1)))
        listoffreq.append((seq.count(i)/(len(seq) - 1 - 2*seq.count("N"))*100))
    return listoffreq
def listorf(filename):
    with open(filename, "r") as f:
        totallen = 0
        list_of_orfs = []
        for line in f:
            if line.startswith(">") == False:
                list_of_orfs.append(Seq.translate(line))
                totallen += len(line)
        return list_of_orfs, totallen
                
def aminoacids(filename):
    """
    returns dictionary with frequency of aminoacids for given organism
    """
    orfs = listorf(filename)[0]
    amino_acids = 'ACDEFGHIKLMNPQRSTVWY'
    AAfreqdict = {}
    for orf in orfs:
        for i in list(amino_acids):
            #method to be allowed to add value even if key is not yet present in dictionary
            try:
                AAfreqdict[i] += orf.count("{}".format(i))  
            except KeyError:
                AAfreqdict[i] = orf.count("{}".format(i))
    for i in AAfreqdict:
        AAfreqdict[i] = (AAfreqdict[i] / listorf(filename)[1])*100
    return AAfreqdict
    
def diaminoacids(filename):
    """
    same as above but for all possible dinucleotides
    """
    amino_acids = 'ACDEFGHIKLMNPQRSTVWY'
    listodi = []
    for i in amino_acids:
        for j in amino_acids:
            listodi.append("{}{}".format(i,j))
    orfs = listorf(filename)[0]
    AAfreqdict = {}
    for orf in orfs:
        for i in listodi:
            try:
                AAfreqdict[i] += orf.count("{}".format(i))  
            except KeyError:
                AAfreqdict[i] = orf.count("{}".format(i))
    for i in listodi:
        #printing frequency for each diaminoacid
        print("freq of {} is {}".format(i, (AAfreqdict[i]) / listorf(filename)[1]))
    
def dinucleotides1(filename):
    list1 = dinucleotides(filename)
    print("AG {} AA {} AC {} AT {} CG {} CA {} CC {} CT {} GG {} GA {} GC {} GT {} TG {} TA {} TC {} TT {} \n"
          .format(list1[0],list1[1],list1[2],list1[3],list1[4],list1[5],list1[6],list1[7],list1[8],list1[9],
                  list1[10],list1[11],list1[12],list1[13],list1[14],list1[15]))

def dinuctodict(filename):
    """
    takes dinucleotides from dinucleotides function and store them in dictionary for easier plotting
    """
    listofdi = ["AG", "AA", "AC", "AT","CG", "CA", "CC", "CT","GG", "GA", "GC", "GT", "TG", "TA", "TC", "TT"]
    freq = dinucleotides(filename)
    dinudict = {}
    for i in range(len(freq)):
        dinudict[listofdi[i]] = freq[i]
    return dinudict

def nucleotide(filename):
    """
    count nucleotides frequency
    """
    seq = tostring(filename)
    T = seq.count("T") / len(seq)
    C = seq.count("C") / len(seq)
    G = seq.count("G") / len(seq)
    A = seq.count("A") / len(seq)
    print("T{}C{}G{}A{}".format(T,C,G,A))

def plotDi(filename):
    """
    plots dinucleotide frequency
    """
    Didict = dinuctodict(filename)
    plt.xlabel('dinucleotide symbol')
    plt.ylabel('dinucleotide frequency in %')
    plt.title("Spiribacter curvatus")
    plt.bar(range(len(Didict)), list(Didict.values()), align='center')
    plt.xticks(range(len(Didict)), list(Didict.keys()))
    plt.plot()
    
def plotAA(filename):
    """
    plots aminoacid frequency
    """
    plt.xlabel('Aminoacid symbol')
    plt.ylabel('Aminoacid frequency in %')
    plt.title("Spiribacter curvatus")
    AA = aminoacids(filename)
    plt.bar(range(len(AA)), list(AA.values()), align='center')
    plt.xticks(range(len(AA)), list(AA.keys()))
    plt.plot()

if __name__ == "__main__":
# =============================================================================
#     plotDi("../results/orfs_51")
# =============================================================================
    plotAA("../results/orfs_51")
