#!/usr/bin/env python3  

import os

result = 0
file = "input.txt"
#file = "sample.txt"

with open(file, "r") as file:
    line = file.readline()
    while line != "":
        print(line)
        if line[0] == 'A':
            if line[2] == 'X':
                result += 3
            if line[2] == 'Y':
                result += 4
            if line[2] == 'Z':
                result += 8
        if line[0] == 'B':
            if line[2] == 'X':
                result += 1
            if line[2] == 'Y':
                result += 5
            if line[2] == 'Z':
                result += 9
        if line[0] == 'C':
            if line[2] == 'X':
                result += 2
            if line[2] == 'Y':
                result += 6
            if line[2] == 'Z':
                result += 7
        line = file.readline()
    print(result)
