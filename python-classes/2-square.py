#!/usr/bin/python3
"""Defines a Square class with private size and validation."""


class Square:
    """
    Represents a square.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square, validating the size.

        Args:
            size (int): The size of the new square.

        Raises:
            TypeError: .
            ValueError: If size is less than zero.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
