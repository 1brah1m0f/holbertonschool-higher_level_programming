#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    a = []
    for i in my_list:
        try:
            print("{:d}".format(i), end="")
            count = count + 1
        except IndexError:
            pass
        if i == x:
            break

    print()
    return count
