# -*- coding: utf-8 -*-
"""
Created on Thu May  3 16:07:29 2018

@author: u2355
"""
def nucleotide(filename):
    with open(filename, "r") as f:
        w = open("nucl_output", "w")
        nucleotide_set = set("agct\n")
        for lines in f:
            if lines.endswith("bp\n"):
                w.write(lines)
            if set(lines).issubset(nucleotide_set):
                if lines != "\n":
                    w.write(lines)
                    
def protein(filename):
    with open(filename, "r") as f:
        w = open("protein", "w")
        for lines in f:
            if lines.startswith(">"):
                w.write(lines)
            if lines.strip("\n").isupper():
                w.write(lines)
                    
if __name__ == "__main__":
    nucleotide("genresults.txt")
    protein("genresults2.txt")
    
    raxmlHPC-PTHREADS-AVX -f a -x 54321 -N 100 -T 4 -p 12345 -m PROTCATBLOSUM62 -s input -n output