#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new = {}
    b = sorted(a_dictionary)
    for i in b:
        print(f"{i}: {a_dictionary[i]}")
