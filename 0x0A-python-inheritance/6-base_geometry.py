#!/usr/bin/python3
"""Implements the base class"""


class BaseGeometry:
    """Base class for the Geometry"""

    def area(self):
        """Empty area"""
        raise Exception("area() is not implemented")
