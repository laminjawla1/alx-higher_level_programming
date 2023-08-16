#!/usr/bin/python3
def roman_to_int(roman_string):
    integer = 0
    # if the roman_string is not a string or None, return 0
    if not isinstance(roman_string, str) or not roman_string:
        return integer
    roman_ints = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    for c in roman_string:
        try:
            integer += roman_ints[c]
        except KeyError:
            return 0
    return integer
