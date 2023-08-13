#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if isinstance(my_list, list):
        if 0 <= idx < len(my_list):
            new_list = [n for n in my_list]
            new_list[idx] = element
    return my_list
