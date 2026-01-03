#!/usr/bin/python3
"""1"""


class Student:
    """1"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """1"""
        return self.__dict__
