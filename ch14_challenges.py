#Chapter 14 Challenges - pg.169


#1. Add a square_list class variable to a class called Square so that every
#   time you create a new Square object, the new object gets added to the list.

class Square():
    square_list = []

    def __init__(self, s):
        self.side = s
        self.square_list.append(self)

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.side, self.side, self.side, self.side) 


sq1 = Square(5)
sq2 = Square(6)
sq3 = Square(2)

for eachSquare in Square.square_list:
    print(eachSquare)
    
for x in range(0, len(Square.square_list)):
    print(Square.square_list[x].side)


#2. Change the Square class so that when you print a Square object, a message
#   prints telling you the len of each of the four sides of the shape. For
#   example, if you create a square with Square(29) and print it, Python should
#   print 29 by 29 by 29 by 29.

sq4 = Square(29)
print(sq4)


#3. Write a function that takes two objects as parameters and returns True if
#   they are the same object, and False if not.

def sameObject(a, b):
    if a is b:
        return True
    else:
        return False
#much faster solution
#   return a is b

sq5 = sq1

print(sameObject(sq1, sq5))
print(sameObject(sq2, sq3))

