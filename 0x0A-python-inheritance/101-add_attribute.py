#!/usr/bin/python3
"""
Defines the add_attribute function
"""


def add_attribute(obj, attr, val):
    """Sets a new attribute for the obj"""
    if hasattr(obj, "__dict__"):
        setattr(obj, attr, val)
    raise TypeError("can't add new attribute")
