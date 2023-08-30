#!/usr/bin/python3

"""
Module demonstrating private instance variables
"""


class Square:
    """
    Square - The blueprint
    """

    def __init__(self, size=0):
        """
        __init__ - The initializer
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size: int = size

    def area(self):
        """
        area - Calculates the area of a circle
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        size - Gets the size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        size - Sets the size
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, other):
        """Checks if object 1 is equal to object 2"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Checks if object 1 is not equal to object 2"""
        return self.area() != other.area()

    def __lt__(self, other):
        """Checks if object 1 is less than object 2"""
        return self.area() < other.area()

    def __le__(self, other):
        """Checks if object 1 is less than or equal object 2"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Checks if object 1 is greater than object 2"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Checks if object 1 is greater than or equal to object 2"""
        return self.area() >= other.area()
