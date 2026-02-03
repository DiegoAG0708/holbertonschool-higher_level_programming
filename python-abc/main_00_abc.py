#!/usr/bin/env python3
from task_00_abc import Animal, Dog, Cat

bobby = Dog()
garfield = Cat()

print(bobby.sound())
print(garfield.sound())

# Attempting to instantiate Animal directly will raise a TypeError
animal = Animal()
print(animal.sound())
