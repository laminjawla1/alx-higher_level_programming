#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    for n in my_list:
        if my_list.count(n) == 1:
            result += n
    return result
