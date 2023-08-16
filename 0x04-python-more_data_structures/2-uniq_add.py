#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    history = []
    for n in my_list:
        if n not in history:
            result += n
            history.append(n)
    return result
