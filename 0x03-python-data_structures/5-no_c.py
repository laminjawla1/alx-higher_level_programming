#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for c in my_string:
        if not c in ["c", "C"]:
            new_str += c
    return new_str
