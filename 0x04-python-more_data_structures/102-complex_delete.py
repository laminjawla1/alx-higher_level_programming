#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = a_dictionary.keys()
    for key in list(keys):
        if a_dictionary.get(key) == value:
            del a_dictionary[key]
    return a_dictionary
