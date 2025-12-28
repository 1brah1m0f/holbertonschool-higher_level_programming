from abc import ABC, abstractmethod
#Abstract method

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return("Bark")

class Cat(Animal):
    def sound(self):
        return("Meow")
    
dog=Dog()
cat=Cat()
print(dog.sound())
print(cat.sound())
