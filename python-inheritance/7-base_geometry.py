#!/usr/bin/python3
"""hm hm hm hm"""


class BaseGeometry:
    """mmimimiim omrun tekeri """

    def area(self):
        """Sahə hələ hesablanmayıb qqaqa"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Value-nun tam ədəd olub-olmadığını yoxlayır"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
