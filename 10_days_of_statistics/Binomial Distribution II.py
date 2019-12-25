#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 14:03:01 2019

@author: rupesh
"""

import math 

p, n = tuple(map(int, input().split()))

p = p/100

def probability(p, n, minr, maxr):
    proba = sum([(math.factorial(n)/(math.factorial(i)*math.factorial(n-i)))*(p**i)*((1-p)**(n-i)) for i in range(minr, maxr)])
    return proba

probability(p, n, 3, 11)