#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for column in matrix:
            print("{:d}".format(column), end=" ")
        print()
