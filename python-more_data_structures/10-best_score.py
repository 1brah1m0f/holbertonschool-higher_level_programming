#!/usr/bin/python3
def best_score(a_dictionary):
    a = 0
    mi = max(a_dictionary)
    for i in a_dictionary:
        if i == mi:
            return i
