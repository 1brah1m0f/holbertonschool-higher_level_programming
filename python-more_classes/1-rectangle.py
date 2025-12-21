#!/usr/bin/python3
"""hm"""


class Rectangle:
    """mimimim"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        return

    @property

    def width(self):
        return self.__height

    @width.setter
    def width(self, value):
        if isinstance(width, int):
            if width >= 0:
                self.__width = width
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

        pass
    @property

    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(height, int):
            if height >= 0:
                self.__height = height
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

        pass


