#!/usr/bin/python3
"""salam"""


class Square:
    """Square clasin qururuq"""

    def __init__(self, size=0, position=(0, 0)):
        if isinstance(size, int):
#            sizenin int olub olmadiqin yoxlayir
            if size >= 0:
#            sizenin musbet olub olmadiqin yoxlayir
#             eger duzduse beraber edir sizeye eks halda valueError verir
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
        self.position = position

    def area(self):
        return self.__size * self.__size
#       sizenin areasin qaytarir

    def my_print(self):
        if self.__size == 0:
# eger size 0 disa bos setir cap edib dovrden cixir
            print()
            return
        for _ in range(self.__position[1]):
#           nece bos setir olacaqin gosterir 2 ci hissede
#           yani yuxaridan asagi nece bosluq olacaq
#           meselen eger bununu cavabi 2  (2, (0,2)) olsa
# 
# 
#           ##
#           ##
#           bele olur cixis
            print()

        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
#          bu soldan saga nece bosluq olacaqin gosterir meselen
#          (2, (1,0)) olsa burda 0 ci index 1 olur
#          ##
#          ## 
#          bele olur cixis

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or \
                len(value) != 2 or \
                not all(isinstance(n, int) and n >= 0 for n in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        # eger positionun her iki deyiseninden biri 
        # int yada + olmasa error verir
        self.__position = value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
#        sizeni yoxlayir eger int yada menfi olsa erorr verir
#        eger menfi olsa ValueError
#        eger int olmasa TypeError verir
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
