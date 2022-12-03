#!/usr/bin/env python3  

import os

result = 0

with open("input.txt", "r") as file:
    line = file.readline()
    while line != "":
        print(line)
        if line[2] == 'X':
            if line[0] == 'A':
                result += 4
            if line[0] == 'B':
                result += 1
            if line[0] == 'C':
                result += 7
        if line[2] == 'Y':
            if line[0] == 'A':
                result += 8
            if line[0] == 'B':
                result += 5
            if line[0] == 'C':
                result += 2
        if line[2] == 'Z':
            if line[0] == 'A':
                result += 3
            if line[0] == 'B':
                result += 9
            if line[0] == 'C':
                result += 6
        print(result)
        line = file.readline()
