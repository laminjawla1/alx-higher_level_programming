#!/usr/bin/python3
"""
This module implements a function
that multiple two matrices

"""


def matrix_mul(m_a, m_b):
    """
    matrix_mul - A function that multiplies two matrices

    It also implements some doctest

    >>> matrix_mul((1, 2, 3), [4, 5, 6])
    Traceback (most recent call last):
        ...
    TypeError: m_a must be a list

    >>> matrix_mul([1, 2, 3], (4, 5, 6))
    Traceback (most recent call last):
        ...
    TypeError: m_b must be a list

    >>> matrix_mul([1, 2, 3], [4, 5, 6])
    Traceback (most recent call last):
        ...
    TypeError: m_a must be a list of lists

    >>> matrix_mul([[1, 2], [3, 4]], [1, 2])
    Traceback (most recent call last):
        ...
    TypeError: m_b must be a list of lists

    >>> matrix_mul([[], []], [[1, 3], [1, 2]])
    Traceback (most recent call last):
        ...
    TypeError: m_a can't be empty

    >>> matrix_mul([[1, 2], [2, 3]], [[], []])
    Traceback (most recent call last):
        ...
    TypeError: m_b can't be empty

    >>> matrix_mul([["cat", 2], [2, 3]], [[4, 3], [1, 9]])
    Traceback (most recent call last):
        ...
    TypeError: m_a should contain only integers or floats

    >>> matrix_mul([[8, 2], [2, 3]], [["not_a_num", 3], [1, 9]])
    Traceback (most recent call last):
        ...
    TypeError: m_b should contain only integers or floats

    >>> matrix_mul([[8], [2, 3]], [[4, 3], [1, 9]])
    Traceback (most recent call last):
        ...
    TypeError: each row of m_a must be of the same size

    >>> matrix_mul([[8, 4], [2, 3]], [[4], [1, 9]])
    Traceback (most recent call last):
        ...
    TypeError: each row of m_b must be of the same size

    """

    # Checking for the arguments to a list
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    
    # Checking for the arguments to be a list of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    
    # Checking for an empty list
    if not all(len(row) > 0 for row in m_a):
        raise TypeError("m_a can't be empty")
    if not all(len(row) > 0 for row in m_b):
        raise TypeError("m_b can't be empty")
    
    # Checking elements must be either an int or a float
    for row in m_a:
        if not all(isinstance(i, int) or isinstance(i, float) for i in row):
            raise TypeError(
                "m_a should contain only integers or floats"
            )
    for row in m_b:
        if not all(isinstance(i, int) or isinstance(i, float) for i in row):
            raise TypeError(
                "m_b should contain only integers or floats"
            )
    # Checking for length for the rows of each matrix
    def_len = len(m_a[0])
    if not all(len(row) == def_len for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    def_len = len(m_b[0])
    if not all(len(row) == def_len for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
