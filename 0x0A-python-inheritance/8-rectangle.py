#!/usr/bin/python3
BaseGeometry = __import__("7-base_geometry").BaseGeometry

"""
The rectangle module
"""


class Rectangle(BaseGeometry):
    """
    The Rectangle class inheriting from BaseGeometry
    """

    def __init__(self, width, height):
        """
        Initializer
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
