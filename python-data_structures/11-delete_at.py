#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = []
    s = 0
    for i in my_list:
        if idx != s:
            new_list.append(i)
        s = s + 1
    return new_list
