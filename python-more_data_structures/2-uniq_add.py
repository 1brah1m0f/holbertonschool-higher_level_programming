#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    s = 0
    for i in my_list:
        if i in new_list:
            continue
        else:
            new_list.append(i)
            s = s + i
    return s
