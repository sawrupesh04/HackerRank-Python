#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 10:38:26 2019

@author: rupesh
"""

import numpy

nm_inputs = list(map(int, input().split()))

arr = [list(map(int, input().split())) for _ in range(nm_inputs[0])]
    
arr = numpy.array(arr)

print(numpy.transpose(arr))
print(arr.flatten())

#################################################################
nmp_inputs = list(map(int, input().split()))

n = numpy.array([list(map(int, input().split())) for _ in range(nmp_inputs[0])])
m = numpy.array([list(map(int, input().split())) for _ in range(nmp_inputs[1])])

numpy.concatenate((n, m), axis=0)

##################################################################

shape = tuple(map(int, input().split()))

print(numpy.zeros(shape, dtype='int'))
print(numpy.ones(shape, dtype='int'))

#################################################################

numpy.eye(3, 3)

