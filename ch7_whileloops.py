#ch7 while-loops pg.108

x = 10
while x > 0:
    print('{}'.format(x))
    x -= 1

print("Happy New Year!" + "\n")


#while - break pg.110

qs = ["What is your name?",
      "What is your fav. color?",
      "What is your quest?"]

n = 0
while True:
    print("Type q to quit")
    a = input(qs[n])
    if a == "q":
        break
    n = (n + 1) % 3

print()


#continue-statement pg. 111

for i in range(1,6):
    if i == 3:
        continue
    print(i)

print()

#pg.112

i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1

print()
