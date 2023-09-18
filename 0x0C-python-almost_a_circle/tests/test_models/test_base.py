#!/usr/bin/python3
"""The base class for the test models"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    Testing the Base class instances
    """

    def test_no_args(self):
        obj_1 = Base()
        obj_2 = Base()
        self.assertEqual(obj_1.id, obj_2.id - 1)

    def test_3_ids(self):
        obj_1 = Base()
        obj_2 = Base()
        obj_3 = Base()
        self.assertEqual(obj_1.id, obj_3.id - 2)

    def test_provided_id(self):
        self.assertEqual(1997, Base(1997).id)

    def test_nb_instance_after_providing_id(self):
        obj_1 = Base()
        obj_2 = Base(1997)
        obj_3 = Base()
        self.assertEqual(obj_1.id, obj_3.id - 1)

    def test_str_id(self):
        obj_1 = Base("id")
        self.assertEqual(obj_1.id, "id")

    def test_float_id(self):
        obj = Base(3.145)
        self.assertAlmostEqual(obj.id, 3.145)

    def test_dict_id(self):
        obj = Base({"id": "my_id"})
        self.assertAlmostEqual(obj.id, {"id": "my_id"})

    def test_binary_id(self):
        self.assertEqual(bin(10), Base(bin(10)).id)

    def test_nan_id(self):
        obj = Base(float("nan"))
        self.assertNotEqual(obj.id, float("nan"))

    def test_none_id(self):
        obj_1 = Base(None)
        obj_2 = Base(None)
        self.assertEqual(obj_1.id, obj_2.id - 1)

    def test_multiple_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2, 3, 4, 5)


class TestBaseCreate(unittest.TestCase):
    """Testing the create method of the Base class."""

    def test_create_rectangle_original(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r1))

    def test_create_rectangle_new(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r2))

    def test_create_rectangle_is(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_create_rectangle_equals(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_create_square_original(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        _ = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s1))

    def test_create_square_new(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s2))

    def test_create_square_is(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(s1, s2)

    def test_create_square_equals(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertNotEqual(s1, s2)
