#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    tuple_a_cp = ()
    tuple_b_cp = ()

    if len_a == 0:
        tuple_a_cp = (0, 0)
    elif len_a == 1:
        tuple_a_cp = (tuple_a[0], 0)
    else:
        tuple_a_cp = tuple(tuple_a[:2])

    if len_b == 0:
        tuple_b_cp = (0, 0)
    elif len_b == 1:
        tuple_b_cp = (tuple_b[0], 0)
    else:
        tuple_b_cp = tuple(tuple_b[:2])

    return tuple(a + b for a, b in zip(tuple_a_cp, tuple_b_cp))
