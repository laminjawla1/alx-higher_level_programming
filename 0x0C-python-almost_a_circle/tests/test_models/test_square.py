#!/usr/bin/python3
"""This module test the square instances"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    TestSquare - Test the square instances
    """

    def test_no_args(self):
        with self.assertRaises(TypeError):
            sq = Square()

    def test_square_initialization(self):
        sq = Square(2, 3, 1, id=100)
        self.assertEqual(100, sq.id)

    def test_size_getter(self):
        sq = Square(2, 3, 1, id=100)
        self.assertEqual(2, sq.size)

    def test_size_setter_type_error(self):
        sq = Square(2, 3, 1, id=100)
        with self.assertRaises(TypeError):
            sq.size = float

    def test_size_setter_value_error(self):
        sq = Square(2, 3, 2, id=100)
        with self.assertRaises(ValueError):
            sq.size = -2023

    def test_size_setter_success(self):
        sq = Square(3, 1, 2, id=100)
        sq.width = 50
        self.assertEqual(50, sq.width)

    def test_x_getter(self):
        sq = Square(2, 1, 2, id=100)
        self.assertEqual(1, sq.x)

    def test_x_setter_type_error(self):
        sq = Square(2, 3, 2, id=100)
        with self.assertRaises(TypeError):
            sq.x = float

    def test_x_setter_value_error(self):
        sq = Square(2, 3, 2, id=100)
        with self.assertRaises(ValueError):
            sq.x = -2023

    def test_x_setter_success(self):
        sq = Square(2, 3, 2, id=100)
        sq.x = 50
        self.assertEqual(50, sq.x)

    def test_y_getter(self):
        sq = Square(9, 1, 2, id=100)
        self.assertEqual(2, sq.y)

    def test_y_setter_type_error(self):
        sq = Square(2, 3, 8, id=100)
        with self.assertRaises(TypeError):
            sq.y = float

    def test_y_setter_value_error(self):
        sq = Square(2, 7, 2, id=100)
        with self.assertRaises(ValueError):
            sq.y = -2023

    def test_x_setter_success(self):
        sq = Square(2, 3, 56, id=100)
        sq.y = 50
        self.assertEqual(50, sq.y)

    def test_area_1(self):
        sq = Square(7, 3, 2, id=100)
        self.assertEqual(49, sq.area())

    def test_area_2(self):
        sq = Square(10, 5, 1)
        self.assertEqual(100, sq.area())

    def test__str__(self):
        sq = Square(4, 6, 2, 43)
        s = "[Square] (43) 6/2 - 4"
        self.assertEqual(s, sq.__str__())

    def test__str__2(self):
        sq = Square(5, 1, id=10)
        s = "[Square] (10) 1/0 - 5"
        self.assertEqual(s, sq.__str__())

    def test_update_0_invalid_values(self):
        sq = Square(3, 4, 2, 99)
        with self.assertRaises(TypeError):
            sq.update("32", {"2": 2}, float, dict, "5")

    def test_update_0_no_values(self):
        sq = Square(5, 4, 2, 99)
        sq.update()
        self.assertEqual(sq.id, 99)

    def test_update_0_none(self):
        sq = Square(21, 4, 2, 99)
        sq.update(None)
        self.assertIsNone(sq.id)

    def test_update_0_valid_values(self):
        sq = Square(1, 4, 2, 99)
        sq.update(8, 3, 4, 5)
        self.assertEqual(sq.id, 8)

    def test_update_1_invalid_values(self):
        sq = Square(3, 5, 7, 99)
        with self.assertRaises(TypeError):
            sq.update(id="32", width=2.3, height=1.3, x=dict, y="5")

    def test_update_1_no_values(self):
        sq = Square(3, 5, 4, 2024)
        sq.update()
        self.assertEqual(sq.id, 2024)

    def test_update_1_none(self):
        sq = Square(3, 5, 2, 99)
        with self.assertRaises(TypeError):
            sq.update(size=None)

    def test_update_1_valid_values(self):
        sq = Square(5, 4, 2, 99)
        sq.update(id=1, width=2, height=3, x=4, y=5)
        self.assertEqual(sq.id, 1)

    def test_to_dictionary_1(self):
        sq = Square(2, 3, 4, 5)
        self.assertEqual(
            {
                "id": 5,
                "size": 2,
                "x": 3,
                "y": 4,
            },
            sq.to_dictionary(),
        )

    def test_to_dictionary_2(self):
        sq = Square(10, 2, 3, 1)
        expected = {"id": 1, "size": 10, "x": 2, "y": 3}
        self.assertEqual(sq.to_dictionary(), expected)

    def test_to_dictionary_3(self):
        sq = Square(7, 3, 0, 2)
        expected = {"id": 2, "size": 7, "x": 3, "y": 0}
        self.assertEqual(expected, sq.to_dictionary())

    def test_to_dictionary_4(self):
        with self.assertRaises(ValueError):
            Square(0, 0, 0, 3)

    def test_to_dictionary_5(self):
        with self.assertRaises(ValueError):
            Square(-5, -2, -1, 4)

    def test_to_dictionary_6(self):
        sq = Square(1000000, 500000, 9999, 5)
        expected = {"id": 5, "size": 1000000, "x": 500000, "y": 9999}
        self.assertEqual(expected, sq.to_dictionary())

    def test_to_dictionary_7(self):
        sq1 = Square(10, 5, 3, 1)
        sq2 = Square(5, 2, 3, 1)
        self.assertNotEqual(sq1.to_dictionary(), sq2)
