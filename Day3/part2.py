#!/bin/env python3

import os
import pdb

#file = "sample.txt"
file = "input.txt"
#file = "test.txt"
i = 0
dup = 0
j = 0
boo = 0

with open(file, "r") as file:
    bag1 = file.readline()
    bag1 = bag1[:-2]
    bag2 = file.readline()
    bag2 = bag2[:-2]
    bag3 = file.readline()
    bag3 = bag3[:-2]
    while bag1 != "":
        i = 0
        boo = 0
        while i < len(bag1):    
            if bag2.find(bag1[i]) >=  0 and bag3.find(bag1[i]) >= 0:
                if ord(bag1[i]) < 91:
                    dup += ord(bag1[i]) - 38
                else:
                    dup += ord(bag1[i]) - 96
                boo += 1
                break
            if boo == 1:
                break
            i += 1
        print(dup)
        bag1 = file.readline()
        bag2 = file.readline()
        bag3 = file.readline()
