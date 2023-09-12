#!/usr/bin/python3
"""Append write module"""


def append_write(filename="", text=""):
    """Appends to a file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
