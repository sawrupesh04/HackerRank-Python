#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 15:16:17 2019

@author: rupesh
"""

defect, total = tuple(map(int, input().split()))

# probability
p = defect/total

# No of trials
n = int(input())

gd = ((1-p)**(n-1))*p
print(gd)