#!/usr/bin/python3
"""hm"""


class Square:
    """hello"""

    def __init__(self, area=0):

        """Raises:
            TypeError: size must be an integer
            ValueError: Size must be >= 0"""
        if not isinstance(area, int):
            raise TypeError("size must be an integer")

        if area < 0:
            raise ValueError("size must be >= 0")
        self.__area = area

    def size(self):
        return self.__area ** 0.5
