import numpy as np
import math as math
import statistics_script


def vectors(list1, list2):
    """
    calculate distance. in our case distance is calculated based on dinucleotide frequency
    """
    list_of_substracted = []
    for index in range(len(list1)):
        list_of_substracted.append((list1[index] - list2[index])**2)
    return math.sqrt(sum(list_of_substracted))
    
def distancematrixtool(genome1, genome2, genome3, genome4, genome5):
    """
    takes all genomes, creates empty matrix and later fill cells with calculated distance between them.
    prints matrix.
    """
    matrix = np.zeros((5,5))
    listoffreq = [statistics_script.dinucleotides(genome1), statistics_script.dinucleotides(genome2),
                  statistics_script.dinucleotides(genome3), statistics_script.dinucleotides(genome4), 
                  statistics_script.dinucleotides(genome5)]
    for i in range(len(listoffreq)):
        for j in range(len(listoffreq)):
            matrix[i, j] = vectors(listoffreq[i], listoffreq[j])
    print(matrix)
    
if __name__ == "__main__":
    distancematrixtool("../.././genomes/03.fa.txt", "../.././genomes/09.fa.txt", "../.././genomes/20.fa.txt", "../.././genomes/24.fa.txt", "../.././genomes/51.fa.txt")