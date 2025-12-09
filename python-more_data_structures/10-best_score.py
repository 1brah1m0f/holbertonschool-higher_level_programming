#!/usr/bin/python3
def best_score(a_dictionary):
    s = 0
    for i in a_dictionary:
        if a_dictionary[i] > s:
            s = a_dictionary[i]
    return s
