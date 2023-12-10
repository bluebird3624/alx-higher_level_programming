#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return  map(lambda row:list(map(lambda element:element**2,row)),matrix)
