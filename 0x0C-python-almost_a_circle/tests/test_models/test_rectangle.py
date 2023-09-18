#!/usr/bin/python3
"""This module test the rectangle instances"""
import unittest, subprocess
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """
    TestRectangle - Test the rectangle instances
    """
    def test_no_args(self):
        with self.assertRaises(TypeError):
            rec = Rectangle()
    
    def test_rectangle_initialization(self):
        rec = Rectangle(2, 3, 1, 2, id=100)
        self.assertEqual(100, rec.id)
    
    def test_width_getter(self):
        rec = Rectangle(2, 3, 1, 2, id=100)
        self.assertEqual(2, rec.width)
    
    def test_width_setter_type_error(self):
        rec = Rectangle(2, 3, 1, 2, id=100)
        with self.assertRaises(TypeError):
            rec.width = float
    
    def test_width_setter_value_error(self):
        rec = Rectangle(2, 3, 1, 2, id=100)
        with self.assertRaises(ValueError):
            rec.width = -2023
    
    def test_width_setter_success(self):
        rec = Rectangle(2, 3, 1, 2, id=100)
        rec.width = 50
        self.assertEqual(50, rec.width)
    
    def test_height_getter(self):
        rec = Rectangle(2, 3, 1, 2, id=100)
        self.assertEqual(3, rec.height)
    
    def test_height_setter_type_error(self):
        rec = Rectangle(2, 3, 1, 2, id=100)
        with self.assertRaises(TypeError):
            rec.height = float
    
    def test_height_setter_value_error(self):
        rec = Rectangle(2, 3, 1, 2, id=100)
        with self.assertRaises(ValueError):
            rec.height = -2023
    
    def test_height_setter_success(self):
        rec = Rectangle(2, 3, 1, 2, id=100)
        rec.height = 50
        self.assertEqual(50, rec.height)
    
    def test_x_getter(self):
        rec = Rectangle(2, 3, 1, 2, id=100)
        self.assertEqual(1, rec.x)
    
    def test_x_setter_type_error(self):
        rec = Rectangle(2, 3, 1, 2, id=100)
        with self.assertRaises(TypeError):
            rec.x = float
    
    def test_x_setter_value_error(self):
        rec = Rectangle(2, 3, 1, 2, id=100)
        with self.assertRaises(ValueError):
            rec.x = -2023
    
    def test_x_setter_success(self):
        rec = Rectangle(2, 3, 1, 2, id=100)
        rec.x = 50
        self.assertEqual(50, rec.x)
    
    def test_y_getter(self):
        rec = Rectangle(2, 3, 1, 2, id=100)
        self.assertEqual(2, rec.y)
    
    def test_y_setter_type_error(self):
        rec = Rectangle(2, 3, 1, 2, id=100)
        with self.assertRaises(TypeError):
            rec.y = float
    
    def test_y_setter_value_error(self):
        rec = Rectangle(2, 3, 1, 2, id=100)
        with self.assertRaises(ValueError):
            rec.y = -2023
    
    def test_x_setter_success(self):
        rec = Rectangle(2, 3, 1, 2, id=100)
        rec.y = 50
        self.assertEqual(50, rec.y)
    
    def test_area_1(self):
        rec = Rectangle(2, 3, 1, 2, id=100)
        self.assertEqual(6, rec.area())
    
    def test_area_2(self):
        rec = Rectangle(10, 5, 1, 2)
        self.assertEqual(50, rec.area())
    
    def test__str__(self):
        rec = Rectangle(4, 6, 2, 1, 12)
        s  = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(s, rec.__str__())
    
    def test__str__2(self):
        rec = Rectangle(5, 5, 1, id=10)
        s  = "[Rectangle] (10) 1/0 - 5/5"
        self.assertEqual(s, rec.__str__())

    def test_update_0_invalid_values(self):
        rec = Rectangle(3, 5, 4, 2, 99)
        with self.assertRaises(TypeError):
            rec.update("32", {"2": 2}, float, dict, "5")

    def test_update_0_no_values(self):
        rec = Rectangle(3, 5, 4, 2, 99)
        rec.update()
        self.assertEqual(rec.id, 99)

    def test_update_0_none(self):
        rec = Rectangle(3, 5, 4, 2, 99)
        rec.update(None)
        self.assertIsNone(rec.id)

    def test_update_0_valid_values(self):
        rec = Rectangle(3, 5, 4, 2, 99)
        rec.update(1, 2, 3, 4, 5)
        self.assertEqual(rec.id, 1)

    def test_update_1_invalid_values(self):
        rec = Rectangle(3, 5, 4, 2, 99)
        with self.assertRaises(TypeError):
            rec.update(id="32", width=2.3, height=1.3, x=dict, y="5")

    def test_update_1_no_values(self):
        rec = Rectangle(3, 5, 4, 2, 99)
        rec.update()
        self.assertEqual(rec.id, 99)

    def test_update_1_none(self):
        rec = Rectangle(3, 5, 4, 2, 99)
        with self.assertRaises(TypeError):
            rec.update(id=None, width=None)

    def test_update_1_valid_values(self):
        rec = Rectangle(3, 5, 4, 2, 99)
        rec.update(id=1, width=2, height=3, x=4, y=5)
        self.assertEqual(rec.id, 1)

    def test_to_dictionary_1(self):
        rec = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual({
                "id": 5,
                "width": 1,
                "height":2,
                "x": 3,
                "y": 4,
            }, rec.to_dictionary()
        )

    def test_to_dictionary_2(self):
        rec = Rectangle(10, 5, 2, 3, 1)
        expected = {"id": 1, "width": 10, "height": 5, "x": 2, "y": 3}
        self.assertEqual(rec.to_dictionary(), expected)

    def test_to_dictionary_3(self):
        rec = Rectangle(7, 3, 0, 0, 2)
        expected = {"id": 2, "width": 7, "height": 3, "x": 0, "y": 0}
        self.assertEqual(expected, rec.to_dictionary())

    def test_to_dictionary_4(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 0, 0, 0, 3)

    def test_to_dictionary_5(self):
        with self.assertRaises(ValueError):
            Rectangle(-5, -2, -1, -3, 4)

    def test_to_dictionary_6(self):
        rec = Rectangle(1000000, 500000, 9999, 8888, 5)
        expected = {"id": 5, "width": 1000000, "height": 500000, "x": 9999, "y": 8888}
        self.assertEqual(expected, rec.to_dictionary())

    def test_to_dictionary_7(self):
        rec1 = Rectangle(10, 5, 2, 3, 1)
        rec2 = Rectangle(7, 5, 2, 3, 1)
        self.assertNotEqual(rec1.to_dictionary(), rec2)