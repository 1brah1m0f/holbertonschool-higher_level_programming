#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    for i in range (len(my_list_1)):
        try:
           a = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("wrong type")
        except TypeError:
            print("wrong type", end="")
        except IndexError:
            pass
    if my_list_2 != my_list_1:
        print("out of range")
    print(a)