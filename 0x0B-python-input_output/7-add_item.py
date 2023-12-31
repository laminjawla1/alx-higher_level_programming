#!/usr/bin/python3
"""Add items to a list module"""
from sys import argv
import json

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def main():
    """Entry point to the program"""
    filename = "add_item.json"
    try:
        my_list = load_from_json_file(filename)
    except FileNotFoundError:
        my_list = []
    my_list.extend(argv[1:])
    save_to_json_file(my_list, filename)


if __name__ == "__main__":
    main()
