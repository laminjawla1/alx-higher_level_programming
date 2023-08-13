#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        m = my_list[0]
        for n in my_list:
            if n > m:
                m = n
        return m
    return None
