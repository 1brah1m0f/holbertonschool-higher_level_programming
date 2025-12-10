#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    a = []
    for i in my_list:
        try:
            a.append("{:d}".format(i))
            count = count + 1
        except IndexError:
            pass
    return a
    return count
