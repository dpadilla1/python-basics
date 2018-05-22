#Chapter 9 Challenges - pg.129

#1. Find a file on your computer and print its contents using Python.

with open("ch9_q1.txt", "r") as f:
    print(f.read())

print()


#2. Write a program that asks a user a question, and saves their answer
#   to a file.

ans = input("What's up? ")

with open("ch9_q2.txt", "w") as f:
    f.write(ans)

#test
with open("ch9_q2.txt", "r") as f:
    print("\n" + '"' + f.read() + '" has been saved.')

print()


#3. Take the items in this list: [["Top Gun", "Risky Business", "Minority
#   Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man
#   on Fire", "Flight"]] and write them to a CSV file. The data from each list
#   should be a row in the file, with each item in the list separated by a comma.

import csv


movList = [["Top Gun", "Risky Business", "Minority Report"],
           ["Titanic", "The Revenant", "Inception"],
           ["Training Day", "Man on Fire", "Flight"]]

with open("ch9_q3.csv", "w", newline='') as f:
    w = csv.writer(f, delimiter=",")
    for row in movList:
        w.writerow(row)

#test
with open("ch9_q3.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))
    print("-----" + "\n")

#DOES NOT WORK - FIND OUT WHY
    print(r)
    for row in r:
        print(row)


    
