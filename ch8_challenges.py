#Chapter 8 Challeges - pg.121

#2. Create a module named cubed with a function that takes a number as a
#   parameter, and returns the number cubed. Import and call the function
#   from another module.

import cubed


a = input("Please enter a number you wish to cube: ")
a = int(a)
aNew = cubed.cube(a)
print(aNew)

