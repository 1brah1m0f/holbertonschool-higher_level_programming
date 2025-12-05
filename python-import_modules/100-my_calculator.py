#!/usr/bin/python3
import sys
import math
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    a , n, b = sys.argv[1], sys.argv[2], sys.argv[3]
    a, b = int(a), int(b)
    if n == "+":
        print("{} {} {} = {}".format(a, n, b, add(a, b)))
    elif n == "-":
        print("{} {} {} = {}".format(a, n, b, sub(a, b)))
    elif n == "*":
        print("{} {} {} = {}".format(a, n, b, mul(a, b)))
    elif n == "/":
        print("{} {} {} = {}".format(a, n, b, div(a, b)))
