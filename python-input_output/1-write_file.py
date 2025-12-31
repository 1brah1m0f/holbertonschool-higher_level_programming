#!/usr/bin/python3
"""hello i am Shixi Ibrahimov"""


def write_file(filename="", text=""):
    """i am Shixi"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
