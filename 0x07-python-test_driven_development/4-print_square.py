#!/usr/bin/python3
"""
The print square module implements a `print_square` function
that print a square of size `size`

It also run some doctest
"""


def print_square(size):
    """
    >>> print_square(4)
    ####
    ####
    ####
    ####

    >>> print_square(-3.142)
    Traceback (most recent call last):
        ...
    TypeError: size must be an integer

    >>> print_square(10)
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########

    >>> print_square("cat")
    Traceback (most recent call last):
        ...
    TypeError: size must be an integer

    >>> print_square(-1)
    Traceback (most recent call last):
        ...
    ValueError: size must be >= 0

    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    elif not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif size == 0:
        print()
    else:
        for i in range(size):
            print("#" * size)
