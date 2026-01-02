#!/usr/bin/python3
"""this is """


def append_write(filename="", text=""):
    """mimim"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
