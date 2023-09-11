#!/usr/bin/python3
"""
Implements the MyList class
"""


class MyList(list):
    """
    Inherits from the list class
    """

    def __init__(self):
        """Using the init method from the list class"""
        list.__init__(self)

    def print_sorted(self):
        """Prints the list in sorted"""
        print(sorted(self))
