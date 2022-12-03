#!/bin/env python3

import os
import pdb

file = "sample.txt"
#file = "input.txt"
i = 0
dup = 0
j = 0

with open(file, "r") as file:
    bag = file.readline()
    while bag != "":
        middle = len(bag) / 2
        comp1 = bag[:middle]
        comp2 = bag[middle:]
        while i < len(comp1):    
            j = 0
            while j < len(comp2):
                if comp2[j] == comp1[i]:
                    if ord(comp1[i]) < 64:
                        dup += ord(comp1[i]) - 64
                    else:
                        dup += ord(comp1[i]) - 96
                j += 1
            i += 1
        print(dup)
        bag = file.readline()



