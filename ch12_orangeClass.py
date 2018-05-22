#Orange Class - Chapter 12 - pg.144

class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        self.mold = 0
        print("Created!")
        
    def rot(self, days, temp):
        self.mold = days * temp

or1 = Orange(10, "dark orange")
print(or1)

or1.weight = 100
or1.color = "light orange"

print(or1.weight)
print(or1.color)


#pg.146

or2 = Orange(8, "dark orange")
or3 = Orange(14, "yellow")

#pg.147

orange = Orange(6, "orange")
print(orange.mold)
orange.rot(10, 98)
print(orange.mold)
