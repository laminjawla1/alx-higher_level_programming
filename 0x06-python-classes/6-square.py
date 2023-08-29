#!/usr/bin/python3

"""
Module demonstrating private instance variables
"""


class Square:
    """
    Square - The blueprint
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        __init__ - The initializer
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size: int = size
        self.__position = position

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

    @property
    def position(self):
        """
        position - Gets object's position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        position - Sets object's position
        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not any(type(item) != int for item in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """
        my_print - Prints a square of size size
        """
        if self.__size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print()
        n_space = self.__position[0]
        for i in range(self.__size):
            print(" " * n_space + "#" * self.__size)
