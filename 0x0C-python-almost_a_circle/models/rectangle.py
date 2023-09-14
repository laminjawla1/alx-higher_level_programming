#!/usr/bin/python3
"""
This module implements the Rectangle class
which inherits from the BaseClass from the
base.py
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle - The blueprint for the rectangle objects

    It inherits from the base class from the base.py
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializer"""
        super(Rectangle, self).__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter"""
        self.__width = value

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter"""
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        self.__x = value

    @property
    def y(self):
        """x getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """x setter"""
        self.__y = value
