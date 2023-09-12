#!/usr/bin/python3
"""Save to json file module"""

import json


def save_to_json_file(my_obj, filename):
    """Save to json file"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
