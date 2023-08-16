#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for array in matrix:
        new_matrix.append([n**2 for n in array])
    return new_matrix
