#Chapter 13 - pg.154

#POLYMORPHISM

print("Hello, World!")
print(200)
print(200.1)

#type function returns data type of object

print(type("Hello, World!"))
print(type(200))
print(type(200.1))

#do not run

#WITHOUT POLYMORPHISM
shapes = [tr1, sql, crl]
for a_shape in shapes:
    if type(a_shape) == "Triangle":
        a_shape.draw_triangle()
    if type(a_shape) == "Square":
        a_shape.draw_square()
    if type(a_shape) == "Circle":
        a_shape.draw_circle()


#WITH POLYMORPHISM
shapes = [tr1, sql, crl]
for a_shape in shapes:
    a_shape.draw()

    
