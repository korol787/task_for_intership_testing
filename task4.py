#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 23:16:20 2021

@author: korol787
"""

import sys
import numpy as np

filepath = sys.argv[1]
file = open(filepath)

num = []
for line in file:
    num.append(int(line))

median = int(np.median(sorted(num)))
print(sum(abs(number - median) for number in num))