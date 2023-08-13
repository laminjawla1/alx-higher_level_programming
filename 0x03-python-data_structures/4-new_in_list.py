#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    if not idx in range(0, len(my_list)):
        return my_list

    new_list = [item for item in my_list]
    new_list[idx] = element
    return new_list
