#!/usr/bin/python3
for i in range(100):
    if i == 89:
        print(89)
        break
    if i<10:
        print("0"+str(i),end=", ")
    else:
      if str(i)[0] == str(i)[-1]:
        continue
      else:
        if i > int(str(i)[::-1]):
            continue
        else:
            print(i,end=", ")
