#ch7 nested loops pg.112

for i in range(1,3):
    print(i)
    for letter in ["a", "b", "c"]:
        print(letter)

print()


#pg.113

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
added = []
for i in list1:
    for j in list2:
        added.append(i + j)

print(added)
print()


#for inside while

while input('y or n?: ') != 'n':
    for i in range(1,6):
        print(i)

print()