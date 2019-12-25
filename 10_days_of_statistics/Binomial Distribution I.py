#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 13:51:21 2019

@author: rupesh
"""

import math

b_g_ratio = list(map(float, input().split()))
# probability
p = b_g_ratio[0]/(1+b_g_ratio[0])

# No of experiments
n = 6

# Atleast 3 success (>=3)

bn1 = sum([(math.factorial(n)/(math.factorial(i)*math.factorial(n-i)))*(p**i)*((1-p)**(n-i)) for i in range(3, 7)])

print(round(bn1, 3))