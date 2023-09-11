#!/usr/bin/python3
"""
Defines the add_attribute function
"""


def add_attribute(obj, attr, val):
    """Sets a new attribute for the obj"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, val)
