#!/usr/bin/python3
"""hm"""


class Rectangle:
    """mimimim"""

    number_of_instances = 0
    
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2
        
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    def __str__(self):
        """Düzbucaqlını '#' simvolu ilə təsvir edən string qaytarır"""
        if self.__width == 0 or self.__height == 0:
            return

        rect_str = []
        for i in range(self.__height):
            rect_str.append("#" * self.__width)

        return "\n".join(rect_str)

    def __repr__(self):
        """Return string to recreate new instance with eval()"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
