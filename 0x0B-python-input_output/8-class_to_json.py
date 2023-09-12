#!/usr/bin/python3
"""Class to json module"""


def class_to_json(obj):
    """Class to json"""
    result = {}

    for attr, value in vars(obj).items():
        if type(value) in [str, int, bool]:
            result.update({attr: value})
        elif type(value) == list:
            result_dict[attr] = [class_to_json(item) for item in value]
        elif type(value) == dict:
            result_dict[attr] = {
                key: class_to_json(value) for key, value in attr_value.items()
            }
    return result
