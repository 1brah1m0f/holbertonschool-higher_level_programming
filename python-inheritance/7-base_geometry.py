#!/usr/bin/python3
"""hello i am iron man"""


class BaseGeometry:
    """hm"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if isinstance(name, str):
            if not isinstance(value, int):
                raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
