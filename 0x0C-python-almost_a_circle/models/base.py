#!/usr/bin/python3
"""
This module contains the base class in the models package

This class will the be base for all the other classes
"""


class Base:
    """
    Base - The blueprint for the objects
    to be instantiated

    This will be the base class for all the classes
    to be created in this project
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """The initializer"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
