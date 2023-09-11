#!/usr/bin/python3
"""
Implements inherits from
"""


def inherits_from(obj, a_class):
    """
    Returns true is obj is a subclass of a_class
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
