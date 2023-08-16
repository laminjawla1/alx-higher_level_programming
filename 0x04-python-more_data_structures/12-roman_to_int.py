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
    for i in range(len(roman_string)):
        try:
            num = roman_ints[roman_string[i]]
            next_num = None
            try:
                next_num = roman_ints[roman_string[i + 1]]
            except IndexError:
                pass
            if next_num:
                if num >= next_num:
                    integer += num
                elif num < next_num:
                    integer -= num
            else:
                integer += num
        except KeyError:
            return 0
    return integer
