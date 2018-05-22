#Chapter 7 Challenges - pg.114


#1. Print each item in the following list: ["The Walking Dead", "Entourage",
#   "The Sopranos", "The Vampire Diaries"].
list1 = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
for show in list1:
    print(show)

print()


#2. Print all the numbers from 25 to 50.
for num in range(25, 51):
    print(num)

print()


#3. Print each item in the list from the first challenge and their indexes.
i = 0
for show in list1:
    print(show + " at index: ")
    print(i)
    i += 1

print()

#STUDY THIS!
#4. Write a program with an infinite loop (with the option to type q to quit)
#   and a list of numbers. Each time through the loop ask the user to guess a
#   a number on the list and tell them whether or not they guessed correctly.
list2 = [0, 5, 9, 12, 15, 16, 18]
while True:
    x = input("Guess a number or type q to quit: ")
    if x == "q":
        break

    try:
        x = int(x)
    except ValueError:
        print("Please put a damn number or q to quit!")

    if x in list2:
        print("You guessed correctly!")
    else:
        print("WRONG!!!")

print()


#5. Multiply all the numbers in the list [8, 19, 148, 4] with all the numbers
#   in the list [9, 1, 33, 83], and append each result to a thrid list.
numlist1 = [8, 19, 148, 4]
numlist2 = [9, 1, 33, 83]
numlist3 = []
for i in numlist1:
    for j in numlist2:
        numlist3.append(i * j)

print(numlist3)

print()
