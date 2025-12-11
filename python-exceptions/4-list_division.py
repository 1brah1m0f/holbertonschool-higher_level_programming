#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    a = []
    for i in range (len(my_list_1)):
        try:
           a.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("wrong type", end="")
            result = 0
        except TypeError:
            print("wrong type", end="")
            result = 0
        except IndexError:
            result = 0
            pass
        finally:
            a.append(result)
    if my_list_2 != my_list_1:
        print("out of range", end="")
    print(a)
