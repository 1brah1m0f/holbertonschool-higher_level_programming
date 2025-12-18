#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
        


        def area(self):
            return self.__size * self.__size
        def my_print(self):
            if self.__size == 0:
                print()
                return
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()

    @property
    def position(self):
        return self.__positon
    
    @position.setter
    def position(self, value):
        if (isinstance(value[0], int) and value[0] > 0) and (isinstance(value[1], int) and value[1] > 0):
            self.__position = value
        else:
            raise TypeError("size must be an integer")       

    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
