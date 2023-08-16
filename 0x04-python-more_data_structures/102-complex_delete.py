#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    trashes = list()
    for d in a_dictionary:
        try:
            trashes = [d for d in a_dictionary if a_dictionary[d] == value]
        except KeyError:
            pass
    for trash in trashes:
        del a_dictionary[trash]
    return a_dictionary
