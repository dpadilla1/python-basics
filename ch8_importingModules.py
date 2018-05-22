#ch8 importing modules - pg.118

#pow
import math

print(math.pow(2, 3))
print()


#random
import random

print(random.randint(0,100))
print()


#statistics
import statistics

#mean
nums = [1, 5, 33, 12, 46, 33, 2]
print(statistics.mean(nums))

#median
print(statistics.median(nums))

#mode
print(statistics.mode(nums))
print()


#keyword - to check if a string is a Python keyword
import keyword

print(keyword.iskeyword("for"))
print(keyword.iskeyword("football"))
print()

