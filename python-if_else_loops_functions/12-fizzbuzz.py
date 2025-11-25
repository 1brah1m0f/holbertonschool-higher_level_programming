#!/usr/bin/python3
for i in range(1,101):
    if i == 100:
        print("Buzz")
        break
    if i % 3 == 0:
        print("Fizz", end = " ")
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz",end = " ")
    elif i % 5 == 0:
        print("Buzz",end = " ")
    else:
        print(i,end = " ")
