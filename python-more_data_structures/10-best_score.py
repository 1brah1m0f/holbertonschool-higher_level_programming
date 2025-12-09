#!/usr/bin/python3
def best_score(a_dictionary):
    s = ""
    s1 = 0
    for i in a_dictionary:
        if a_dictionary[i] > s1:
            s1 = a_dictionary[i]
            s = i
    if s1 = 0:
        s = None
    return s
