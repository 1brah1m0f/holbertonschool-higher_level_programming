#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        print(a/b)
    except ZeroDivisionError:
        return None
