#!/bin/env python3

import os
import pdb

#file = "sample.txt"
file = "input.txt"
i = 0
dup = 0
j = 0
boo = 0

with open(file, "r") as file:
    bag = file.readline()
    while bag != "":
        middle = len(bag) / 2
        comp1 = bag[:middle]
        comp2 = bag[middle:]
        i = 0
        boo = 0
        while i < len(comp1):    
            j = 0
            while j < len(comp2):
                if comp2[j] == comp1[i]:
                    if ord(comp1[i]) < 91:
                        dup += ord(comp1[i]) - 38
                    else:
                        dup += ord(comp1[i]) - 96
                    boo = 1
                    break
                j += 1
            if boo == 1:
                break
            i += 1
        print(dup)
        bag = file.readline()



