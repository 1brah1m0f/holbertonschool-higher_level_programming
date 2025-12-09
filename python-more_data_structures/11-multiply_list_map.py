#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    new_list = []
    for i in my_list:
        new_list.append(i * number)
    return new_list
