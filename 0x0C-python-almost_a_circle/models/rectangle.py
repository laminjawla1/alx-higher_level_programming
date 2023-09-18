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
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """x getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """x setter"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates and return the area"""
        return self.__width * self.__height

    def display(self):
        """Prints the current instance with the value '#'"""
        for i in range(0, self.__y):
            print()
        n_space = self.__x
        for i in range(0, self.__height):
            print(" " * n_space + "#" * self.__width)

    def __str__(self):
        """The string representation of the current object"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """Update the current instance of the Rectangle class"""
        if args and len(args):
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass
        elif kwargs and len(kwargs):
            if 'id' in kwargs:
                self.id = kwargs['id']
            for attr_name in ['width', 'height', 'x', 'y']:
                if attr_name in kwargs:
                    setattr(self, attr_name, kwargs[attr_name])
    
    def to_dictionary(self):
        """To dictionary"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
