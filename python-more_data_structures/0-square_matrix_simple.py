#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    s=[]
    new_matrix = []
    for i in matrix:
        for j in i:
            j*=j
            j.append(s)
        s.append(new_matrix)
    return matrix
