#Chapter 12 Challenges - pg.149

#1. Define a class called Apple with four instance variables that represent four
#   attributes of an apple.

class Apple():
    def __init__(self, color, size, sweet, ripe):
        self.color = color
        self.size = size
        self.sweet = sweet
        self.ripe = riple


#2. Create a Circle class with a method called area that calculates and returns
#   its area. Then create a Circle object, call area on it, and print the result.
#   Use Python's pi function in the built-in math module.

import math

class Circle():
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = math.pi * (self.radius**2)
        return area


smallCircle = Circle(5)
print(smallCircle.area())
print()


#3. Create a Triangle class with a method called area that calculates and
#   returns its area. Then create a Triangle object, call area on it, and
#   print the result.

class Triangle():
    def __init__(self, height, base):
        self.height = height
        self.base = base

    def area(self):
        area = (1/2) * self.height * self.base
        return area


lilTri = Triangle(5, 4)
print(lilTri.area())
print()

#4. Make a Hexagon class with a method called calculate_perimeter that calculates
#   and returns its perimeter. Then create a Hexagon object, call
#   calculate_perimeter on it, and print the result.

class Hexagon():
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        perimeter = 6 * self.side
        return perimeter

bigHex = Hexagon(12)
print(bigHex.calculate_perimeter())
print()

