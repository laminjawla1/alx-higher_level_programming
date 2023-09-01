#!/usr/bin/python3
"""
Add integer module, adds two integers
"""


def add_integer(a, b=98):
    """Adds two numbers and return the result

    >>> add_integer(1, 2)
    3
    >>> add_integer(2, 1)
    3
    >>> add_integer(0, 2)
    2
    >>> add_integer(2, 0)
    2
    >>> add_integer(-5, 8)
    3
    >>> add_integer(-5, 2)
    -3
    >>> add_integer(1)
    99
    >>> add_integer(2.5, 3.5)
    5
    >>> add_integer(1.2, 0.5)
    1
    >>> add_integer("cat", 2)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer
    >>> add_integer(10, "dog")
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer

    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
