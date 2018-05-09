# -*- coding: utf-8 -*-
"""
Created on Wed May  9 13:40:24 2018

@author: u2355
"""
with open("parsed09", "r") as f:
    prot09 = []
    for entry in f:
        prot09.append(entry.split(" "))
with open("parsed20", "r") as f:
    prot20 = []
    for entry in f:
        prot20.append(entry.split(" "))
with open("parsed51", "r") as f:
    prot51 = []
    for entry in f:
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