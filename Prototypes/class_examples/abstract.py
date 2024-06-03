# This is an example of how to use abstract methods for polymorphism/inheritance 
# like you could using a C# parent class or interface

from abc import ABC, abstractmethod

class animal(ABC):
    @abstractmethod
    def move():
        pass
    @abstractmethod
    def eat():
        pass


class bird(animal):
    def __init__(self, name: str):
        self.name = name

    def move(self):
        print(f"{self.name} went flying")

    def eat():
        pass # If abstract function eat isn't overridden, a TypeError will be raised
    

def main():
    robin = bird("robin")
    robin.move()

if __name__ == "__main__":
    main()