#!/usr/bin/python3
"""
The matrix module defines the `matrix_divided` function
which receives a matrix and divides each [i][j] element
by the div value
"""


def matrix_divided(matrix, div):
    """This function takes a matrix and divide each row by the div

    >>> matrix = [[1, 2, 3], [4, 5, 6]]

    >>> matrix_divided(matrix, 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

    >>> print(matrix)
    [[1, 2, 3], [4, 5, 6]]

    >>> matrix = [(1, 2, 3), [4, 5, 6]]
    >>> matrix_divided(matrix, 3)
    Traceback (most recent call last):
        ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats

    >>> matrix = [["cat", 2, 3], ["dog", 5, 6]]
    >>> matrix_divided(matrix, 3)
    Traceback (most recent call last):
        ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats

    >>> matrix = [[2, 3], [8, 5, 6]]
    >>> matrix_divided(matrix, 3)
    Traceback (most recent call last):
        ...
    TypeError: Each row of the matrix must have the same size

    >>> matrix = [[1, 2, 3], [8, 5, 6]]
    >>> matrix_divided(matrix, "cat")
    Traceback (most recent call last):
        ...
    TypeError: div must be a number

    >>> matrix = [[1, 2, 3], [8, 5, 6]]
    >>> matrix_divided(matrix, 0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: division by zero

    """
    new_matrix = []

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if not all(isinstance(i, int) or isinstance(i, float) for i in row):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )
    default_len = len(matrix[0])
    if not all(len(row) == default_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        new_matrix.append([round(i / div, 2) for i in row])
    return new_matrix
