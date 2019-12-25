# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

n = int(input())
x = list(map(int, input().split()))
f = list(map(int, input().split()))



def icr(x, f):
    X = list()

    for i in range(len(f)):
        for _ in range(f[i]):
            X.append(x[i])
            
    new_x = sorted(X)
    
    new_x_half = int(len(new_x)/2)
    if len(new_x)%2==0:
        
        # Lower Half
        l = new_x[:new_x_half]
        
        # upper HAlf
        u = new_x[new_x_half:]
        
        l_half = int(len(l)/2)
        if len(l)%2==0:
            icr = (u[l_half]+u[l_half-1])/2 - (l[l_half]+l[l_half-1])/2
        else:
            icr = u[l_half]- l[l_half]
    else:
        q1 = new_x[:new_x_half]
        q3 = new_x[new_x_half+1:]
        #icr = new_x[new_x_half]
        
        q1_half = int(len(q1)/2)
        icr = q3[q1_half]- q1[q1_half]
        
    print(round(float(icr), 1))

icr(x, f)