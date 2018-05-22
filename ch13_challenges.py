#Chapter 13 Challenges - pg.162


class Shape():
    def __init__(self):
        pass

    def what_am_i(self):
        print("I am a shape.")


class Rectangle(Shape):
    def __init__(self, l, w):
        self.len = l
        self.width = w

    def calculate_perimeter(self):
        perimeter = (self.len*2) + (self.width*2)
        return perimeter


class Square(Shape):
    def __init__(self, s):
        self.side = s

    def calculate_perimeter(self):
        perimeter = 4 * self.side
        return perimeter

    def change_size(self, new_side):
        self.side += new_side


#1. Create Rectang;e and Square classes with a method called calculate_perimeter
#   that calculates the perimeter of the shapes they represent. Create Rectangle
#   and Square objects and call the method on both of them.

a_rectangle = Rectangle(10, 20)
print(a_rectangle.calculate_perimeter())
a_Square = Square(5)
print(a_Square.calculate_perimeter())
print()


#2. Define a method in your Square class called change_size that allows you to
#   pass in a number that increases or decreases (if the number is negative)
#   each side of a Square object by that number.

a_Square.change_size(-4)
print(a_Square.side)
print(a_Square.calculate_perimeter())
print()


#3. Create a class called Shape. Define a method in it called what_am_i that
#   prints "I am a shape" when called. Change your Square and Rectangle classes
#   from the previous challenges to inherit from Shape, create Square and
#   Rectangle objects, and call the new method on both of them.

b_Square = Square(10)
b_Rectangle = Rectangle(2, 3)
b_Square.what_am_i()
b_Rectangle.what_am_i()
print()


#4. Create a class called Horse and a class called Rider. Use composition to
#   model a horse that has a rider.

class Horse():
    def __init__(self, weight, rider):
        self.weight = weight
        self.rider = rider

class Rider():
    def __init__(self, name):
        self.name = name

    def print_name(self):
        return self.name


a_Rider = Rider("Derek")
a_Horse = Horse(50, a_Rider)
print(a_Horse.rider)
print(a_Horse.rider.name)
print(a_Horse.rider.print_name())
print()


