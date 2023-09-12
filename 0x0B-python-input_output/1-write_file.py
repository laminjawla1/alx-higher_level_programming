#!/usr/bin/python3
"""The write file module"""


def write_file(filename="", text=""):
    """Writes to a file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
