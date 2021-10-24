#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 20:55:03 2021

@author: korol787
"""

import json
with open('tests.json') as fp:
    tests = json.load(fp)
with open('values.json') as fp:
    values = json.load(fp)
    
super_dict = {}
for d in values['values']:
    super_dict[d['id']] = d['value']

def report(dicti):
    if 'values' not in dicti.keys():
        dicti['value'] = super_dict[dicti['id']]
    if 'value' in dicti.keys():
        dicti['value'] = super_dict[dicti['id']]
    if 'values' in dicti.keys():
        for dicti_small in dicti['values']:
            report(dicti_small)

for a in tests['tests']:
    report(a)

with open('report.json', 'w') as outfile:
    json.dump(tests['tests'], outfile)