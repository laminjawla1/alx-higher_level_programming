#!/usr/bin/python3
"""Save to json file module"""


def save_to_json_file(my_obj, filename):
    """Save to json file"""
    with open(filename, "wb", encoding="utf-8") as f:
        f.write(my_obj)
