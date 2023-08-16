#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    trashes = []
    for d in a_dictionary:
        try:
            if a_dictionary[d] == value:
                trashes.append(d)
        except KeyError:
            pass
    for trash in trashes:
        del a_dictionary[trash]
    return a_dictionary
