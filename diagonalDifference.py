# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 22:15:52 2020

@author: SU
"""

def diagonalDifference(arr):
    diagonal = 0
    anti_diagonal=0
    n = len(arr)
    for i in range(n):
        diagonal+=arr[i][i]
        anti_diagonal+=arr[i][n-1-i]
    
    res = abs(diagonal-anti_diagonal)
    return res

print(diagonalDifference([[1,0],[3,4]]))