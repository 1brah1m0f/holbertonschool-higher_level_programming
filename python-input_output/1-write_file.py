#!/usr/bin/python3
"""hello i am Shixi Ibrahimov"""


def write_file(filename="", text=""):
    """i am Shixi"""
    with open(filename, "r" , encoding="utf-8") as f:
        text = len(f.read())
