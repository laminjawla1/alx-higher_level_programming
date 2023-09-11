#!/usr/bin/python3

"""
The rectangle module implements
the Rectangle class which serves
as a blueprint for Rectangle instances
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


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

    def area(self):
        """Calculates and returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
