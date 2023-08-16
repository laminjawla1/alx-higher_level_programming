#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = a_dictionary.keys()
    for key in keys:
        if a_dictionary.get(key) == value:
            del a_dictionary[trash]
    return a_dictionary
