# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 22:00:02 2020

@author: SU
"""

def compareTriplets(a,b):
    comp =[]
    alice=0
    bob=0
    for i in range(len(a)) :
        comp.append(a[i]-b[i])

    for comp_ in comp:
        if comp_>0:
            alice+=1
        elif comp_<0:
            bob+=1

    
    final_score = [alice, bob]
    return final_score
            
print(compareTriplets([5,6,7], [3,6,10]));