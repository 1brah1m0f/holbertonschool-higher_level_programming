#!/usr/bin/python3
for i in range(100):
    a = i // 10
    b = i % 10
    if a >= b:
        continue
    if i != 89:
        print("{:02d}, ".format(i), end="")
    else:
        print("89")
