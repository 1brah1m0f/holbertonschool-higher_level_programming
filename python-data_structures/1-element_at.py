#!/usr/bin/python3
def element_at(my_list, idx):
    if idx >= len(my_list) :
        None
    else:
        print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
    return
