# -*- coding: utf-8 -*-
"""
Created on Fri May 11 13:39:25 2018

@author: u2355
"""
list03 = []
list09 = []
list20 = []
list51 = []
for n in range(10):
    with open("kcluster_{}".format(n)) as f:
        file = f.readlines()
        for line in range(len(file)):
            if file[line].startswith(">03"):
                for i in range(line + 1, len(file)):
                    if file[i].startswith(">"):
                        break
                    list03.append(file[i].strip("\n"))
            if file[line].startswith(">09"):
                for i in range(line + 1, len(file)):
                    if file[i].startswith(">"):
                        break
                    list09.append(file[i].strip("\n"))
            if file[line].startswith(">20"):
                for i in range(line + 1, len(file)):
                    if file[i].startswith(">"):
                        break
                    list20.append(file[i].strip("\n"))
            if file[line].startswith(">51"):
                for i in range(line + 1, len(file)):
                    if file[i].startswith(">"):
                        break
                    list51.append(file[i].strip("\n"))
string_03 = "".join(list03)
string_09 = "".join(list09)
string_20 = "".join(list20)
string_51 = "".join(list51)

with open("meta_gene", "w") as w:
    w.write(">03\n")
    w.write("{}\n".format(string_03))
    w.write(">09\n")
    w.write("{}\n".format(string_09))
    w.write(">20\n")
    w.write("{}\n".format(string_20))
    w.write(">51\n")
    w.write("{}".format(string_51))