#!/usr/bin/python3
import unittest

max_integer = __import__("6-max_integer").max_integer

"""
This module implements a test case for the `max_integer` function which
when given a list of numbers, finds the max in it
"""


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([22, 2, 3, 4]), 22)
        self.assertEqual(max_integer([0, 0, 0, 0, 0]), 0)
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([[], [], []]), [])
        self.assertEqual(
            max_integer(
                [
                    [1, 2, 3, 4],
                    [1, 4, 3, 23],
                    [1, 2, 5, 9],
                ]
            ),
            [1, 4, 3, 23],
        )

    def test_max_integer_types(self):
        with self.assertRaises(TypeError):
            max_integer(["2", 5, 3])
        with self.assertRaises(TypeError):
            max_integer([str, float, int, "you", 3.4, 89])

    def test_max_integer_none(self):
        self.assertIsNone(max_integer([]))
