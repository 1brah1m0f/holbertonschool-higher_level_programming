#!/usr/bin/python3
class Fish:
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")

class Bird:

    def fly(self):
        print("The bird is swimming")


    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")

f = FlyingFish()
f.fly()
f.swim()
f.habitat()

print(FlyingFish.mro())