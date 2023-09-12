#!/usr/bin/python3
"""The read file module"""


def read_file(filename=""):
    """Reads and prints the contents of a file"""
    with open(filename, encoding="UTF-8") as f:
        for line in f:
            print(line, end="")
