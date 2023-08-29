#!/usr/bin/python3

"""
Module demonstrating private instance variables
"""


class Square:
    """
    Square - The blueprint
    """

    def __init__(self, size):
        """
        __init__ - The initializer
        """
        self.__size = size
