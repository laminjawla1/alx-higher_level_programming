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

        self.size = size
        self.position = position

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
            or any(isinstance(num, int) for num in value)
            or any(num < 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        my_print - Prints a square of size size
        """
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
