#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 17:44:07 2021

@author: korol787
"""

import sys

data1 = []
data2 = []

with open(sys.argv[1]) as f:
    for line in f:
        data1.append([int(x) for x in line.split()])
with open(sys.argv[2]) as f:
    for line in f:
        data2.append([int(x) for x in line.split()])

def round_dot(x_0, y_0, r, x, y):
    if (x - x_0)**2 + (y - y_0)**2 > r**2:
        return 2
    elif (x - x_0)**2 + (y - y_0)**2 < r**2:
        return 1
    else:
        return 0

for i in range(len(data2[0]) + 1):
    print(round_dot(data1[0][0], data1[0][1], data1[1][0], data2[i][0], data2[i][1]))