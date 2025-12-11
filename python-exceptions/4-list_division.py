#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    a = []
    result = 0
    for i in range (list_length):
        try:
           a.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            a.append(result)
        except TypeError:
            print("wrong type")
            a.append(result)
        except IndexError:
            a.append(result)
        finally:
            pass
    if len(my_list_2) < len(my_list_1):
        print("out of range")
    return a
