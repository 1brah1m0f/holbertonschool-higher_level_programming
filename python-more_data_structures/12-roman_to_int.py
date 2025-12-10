#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    a = []
    s = 0
    for i in roman_string:
        if i == "I":
            a.append(1)
        elif i == "V":
            a.append(5)
        elif i == "X":
            a.append(10)
        elif i == "L":
            a.append(50)
        elif i == "C":
            a.append(100)
        elif i == "D":
            a.append(500)
        elif i == "M":
            a.append(1000)
        if len(roman_string) == 1:
            s = a[0]
            return s
    for i in range(len(a) - 1):
        if a[i] < a[i + 1]:
            s -= a[i]
        else:
            s += a[i]
    s += a[-1]
    return s
