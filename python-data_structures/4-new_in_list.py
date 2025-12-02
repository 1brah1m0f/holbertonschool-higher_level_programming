#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        new_list = replace_in_list(my_list, idx, new_element)
    return my_list
    return new_list