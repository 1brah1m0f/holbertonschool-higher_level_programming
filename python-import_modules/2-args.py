#!/usr/bin/python3
import sys
if __name__ == "__main__":
    a=(len(sys.argv)) - 1
    if a == 0:
            print("0 arguments.")
    elif a == 1:
        print("1 argument:")
        print("{}: {}".format(1, sys.argv[1])) 
    else:
        print(f"{a} arguments:")
        for i in range(1,a+1):
            print("{}: {}".format(i, sys.argv[i])) 
