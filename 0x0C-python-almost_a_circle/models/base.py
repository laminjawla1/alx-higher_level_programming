#!/usr/bin/python3
"""
This module contains the base class in the models package

This class will the be base for all the other classes
"""

import json
import csv
import turtle


class Base:
    """
    Base - The blueprint for the objects
    to be instantiated

    This will be the base class for all the classes
    to be created in this project
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """The initializer"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """To json string"""
        return json.dumps(list_dictionaries) if list_dictionaries else "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file"""
        filename = cls.__name__ + ".json"
        if not list_objs:
            list_objs = []
        with open(filename, "w", encoding="utf") as f:
            list_dict_objs = [obj.to_dictionary() for obj in list_objs]
            f.write(Base.to_json_string(list_dict_objs))

    @staticmethod
    def from_json_string(json_string):
        """from json string"""
        return json.loads(json_string) if json_string else []

    @classmethod
    def create(cls, **dictionary):
        """Create"""
        if dictionary and len(dictionary):
            obj = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
            obj.update(**dictionary)
            return obj

    @classmethod
    def load_from_file(cls):
        """Loads attributes from a file and create instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                list_dicts = Base.from_json_string(f.read())
                return [cls.create(**obj) for obj in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save list objects to a csv file"""
        filename = cls.__name__ + ".csv"
        if cls.__name__ == "Rectangle":
            fieldnames = ["id", "width", "height", "x", "y"]
        else:
            fieldnames = ["id", "size", "x", "y"]
        with open(filename, "w", newline="") as csv_file:
            if not list_objs:
                csv_file.write("[]")
            else:
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Loads a csv file name create objects from it"""
        filename = cls.__name__ + ".csv"
        if cls.__name__ == "Rectangle":
            fieldnames = ["id", "width", "height", "x", "y"]
        else:
            fieldnames = ["id", "size", "x", "y"]
        try:
            with open(filename, "r") as csv_file:
                reader = csv.DictReader(csv_file, fieldnames=fieldnames)
                list_dicts = [
                    dict([k, int(v)] for k, v in d.items()) for d in reader
                ]
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    def draw(list_rectangles, list_squares):
        """
        Draws rectangles and squares from list of rectangles and squares
        """
        t = turtle.Turtle()
        t.screen.bgcolor("green")
        t.pensize(3)
        t.shape("turtle")

        t.color("red")
        for rec in list_rectangles:
            t.showturtle()
            t.up()
            t.goto(rec.x, rec.y)
            t.down()
            for _ in range(2):
                t.forward(rec.width)
                t.left(90)
                t.forward(rec.height)
                t.left(90)
            t.hideturtle()

        t.color("blue")
        for sq in list_squares:
            t.showturtle()
            t.up()
            t.goto(sq.x, sq.y)
            t.down()
            for i in range(2):
                t.forward(sq.width)
                t.left(90)
                t.forward(sq.height)
                t.left(90)
            t.hideturtle()

        turtle.exitonclick()
