#!/usr/bin/python3
def get_numerator(l):
    n = 0
    for t in l:
        for i in t:
            n += i
    return n


def get_denominator(l):
    n = 0
    for t in l:
        n += t[1]
    return n


def weight_average(my_list=[]):
    if not my_list:
        return 0
    numerator = get_numerator(my_list)
    denominator = get_denominator(my_list)
    return numerator / denominator
