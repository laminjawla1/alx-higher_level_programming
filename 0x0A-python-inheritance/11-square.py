#!/usr/bin/python3
"""
The square module
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    The blueprint for square objects
    """

    def __init__(self, size):
        """Initializer"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Calculates the area"""
        return self.__size * self.__size

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
