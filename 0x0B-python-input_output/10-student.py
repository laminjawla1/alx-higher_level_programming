#!/usr/bin/python3
"""The student module"""


class Student:
    """Blueprint for the student objects"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
        if isinstance(attrs, list) and all(isinstance(s, str) for s in attrs):
            return {
                key: val for key, val in self.__dict__.items() if key in attrs
            }
        return self.__dict__
