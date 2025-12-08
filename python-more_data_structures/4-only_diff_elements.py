#!/usr/bin/python3
def common_elements(set_1, set_2):
    s = []
    for i in set_1:
        if i not in set_2:
            s.append(i)
    for i in set_2:
        if i not in set_1:
            s.append(i)
    return s
