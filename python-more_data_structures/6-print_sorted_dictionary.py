#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new = {}
    b = sorted(a_dictionary)
    for i in b:
        new[f"{i}"] = (a_dictionary[(f"{i}")])
    print(new)
