#!/usr/bin/python3
"""Load from json file module"""

import json


def load_from_json_file(filename):
    """Loads a json obj from a file"""
    with open(filename, "r") as f:
        return json.load(f)
