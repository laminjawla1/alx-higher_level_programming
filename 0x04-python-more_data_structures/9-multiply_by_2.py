#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = dict()
    for d in a_dictionary:
        new_dict.update({d, a_dictionary[d] * 2})
    return new_dict
