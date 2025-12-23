#!/usr/bin/python3
"""
MyLis
"""


class MyList(list):
    """
    list sinfindən miras alan MyList sinfi.
    """
    def print_sorted(self):
        """
        Siyahını artan ardıcıllıqla çeşidlənmiş (sorted) şəkildə çap edir.
        Orijinal siyahını dəyişmir.
        """
        print(sorted(self))
