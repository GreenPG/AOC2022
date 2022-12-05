#!/bin/env python3

import os
import pdb

#file = "sample.txt"
file = "input.txt"

result = 0
with open(file, "r") as file:
    pair = file.readline()
    while pair != "":
        ranges = pair.split(",")
        range_a = ranges[0].split("-")
        range_b = ranges[1].split("-")
        max_a = int(range_a[1])
        min_a = int(range_a[0])
        max_b = int(range_b[1])
        min_b = int(range_b[0])
        if ((min_b >= min_a and min_b <= max_a) or (max_b >= min_a and max_b <= max_a) or (min_a >= min_b and min_a <= max_b) or (max_a >= min_b and max_a <= max_b)):
            result += 1
        pair = file.readline()
print result

