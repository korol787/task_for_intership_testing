# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from collections import deque

n = int(input())
m = int(input())
numbers = deque(range(1, n + 1))

numbers.rotate(-(m-1))
way = [1]

while numbers[0] != 1:
    way.append(numbers[0])
    numbers.rotate(-(m-1))
print(''.join([str(i) for i in way]))
ope