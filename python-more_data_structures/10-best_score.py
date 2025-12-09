#!/usr/bin/python3
def best_score(a_dictionary):
    s = ""
    for i in a_dictionary:
        if a_dictionary[i] > s:
            s = i
    return s
