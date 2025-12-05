#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a ,n, b = input().split()
a, b = int(a), int(b)
if n == "+":
    print("{} {} {} = {}".format(a, n, b, add(a, b)))
elif n == "-":
    print("{} {} {} = {}".format(a, n, b, sub(a, b)))
elif n == "*":
    print("{} {} {} = {}".format(a, n, b, mul(a, b)))
elif n == "/":
    print("{} {} {} = {}".format(a, n, b, div(a, b)))