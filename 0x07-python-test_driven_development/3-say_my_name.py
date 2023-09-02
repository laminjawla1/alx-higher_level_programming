#!/usr/bin/python3
"""
Say my name module implements a function called `say_my_name`
which when provided a first name and a last name,
say `My name is <first_name> <last_name>
"""


def say_my_name(first_name, last_name=""):
    """say_my_name - A function that takes the users first_name
        and last_name and prints: My name is <first_name> <last_name>

    >>> say_my_name("Lamin", "Jawla")
    My name is Lamin Jawla

    >>> say_my_name("Muslim", "Sage")
    My name is Muslim Sage

    >>> say_my_name("Lamin")
    My name is Lamin

    >>> say_my_name("Lamin", 10)
    Traceback (most recent call last):
        ...
    TypeError: last_name must be a string

    >>> say_my_name(50)
    Traceback (most recent call last):
        ...
    TypeError: first_name must be a string

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
