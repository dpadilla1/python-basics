#Chapter 14 - pg.166

#MAGIC METHODS

class Lion:
    def __init__(self, name):
        self.name = name

#magic method inherited from Object class, overridden
    def __repr__(self):
        return self.name

lion = Lion("Dilbert")
print(lion)
print()


#pg.167 - operand magic method

class AlwaysPositive:
    def __init__(self, number):
        self.n = number

    def __add__(self, other):
        return abs(self.n + other.n)


x = AlwaysPositive(-20)
y = AlwaysPositive(10)


print(x + y)
#(x + y) basically means x.add(y), or add(x, y)
