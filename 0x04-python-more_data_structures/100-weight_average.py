#!/usr/bin/python3
def get_numerator(_list):
    n = 0
    p = 1
    for t in _list:
        for i in t:
            p *= i
        n += p
        p = 1
    return n


def get_denominator(_list):
    n = 0
    for t in _list:
        n += t[1]
    return n


def weight_average(my_list=[]):
    if not my_list:
        return 0
    numerator = get_numerator(my_list)
    denominator = get_denominator(my_list)
    return numerator / denominator
