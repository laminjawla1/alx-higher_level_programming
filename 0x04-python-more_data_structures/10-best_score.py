#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    name = next(iter(a_dictionary))
    score = a_dictionary[name]
    for key, value in a_dictionary.items():
        if value > score:
            name = key
            score = value
    return name
