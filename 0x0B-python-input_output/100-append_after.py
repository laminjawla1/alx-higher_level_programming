#!/usr/bin/python3
"""Append after module"""


def append_after(filename="", search_string="", new_string=""):
    """Append after a line in a file"""
    content = ""
    with open(filename) as f:
        line = f.readline()
        while line:
            content += line
            if search_string in line:
                content += new_string
            line = f.readline()
    with open(filename, "w") as f:
        f.write(content)
