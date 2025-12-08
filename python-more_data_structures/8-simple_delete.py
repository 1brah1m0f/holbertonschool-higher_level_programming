#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for i in a_dictionary:
        a_dictionary[f"{i}"] = int((a_dictionary[f"{i}"]*2))
