#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    s = ""
    s1 = 0
    for i in a_dictionary:
        if a_dictionary[i] > s1:
            s1 = a_dictionary[i]
            s = i
    return s
