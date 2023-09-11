#!/usr/bin/python3
"""Implements the base class"""


class BaseGeometry:
    """Base class for the Geometry"""

    def area(self):
        """Empty area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates an integer"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
