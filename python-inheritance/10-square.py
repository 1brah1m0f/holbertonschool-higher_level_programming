#!/usr/bin/python3
"""Hi"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        Rectangle.integer_validator(self, name="size", value=size)
        self.__size = size

    def area(self):
        return self.__size * self.__size
