#!/usr/bin/python3
"""Docstring for python-input_output.0-student"""


class Student:
    """1"""

    def __init__(self, first_name, last_name, age):
        """mm"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """mimimim"""

        if attrs is None:
            return self.__dict__
        elif isinstance(attrs, list):
            result = {}
            for i in attrs:
                if i in self.__dict__:
                    result[i] = self.__dict__[i]
            return result
        else:
            return self.__dict__
