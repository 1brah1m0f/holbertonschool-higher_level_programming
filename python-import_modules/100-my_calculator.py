#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
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
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)