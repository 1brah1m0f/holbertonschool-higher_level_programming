#!/usr/bin/python3
"""hm"""


class Square:
    """hello"""

    def __init__(self, size=0):

        """Raises:
            TypeError: size must be an integer
            ValueError: Size must be >= 0"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size
