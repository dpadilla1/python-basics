#ch5 Challenges

#1

favorite_musicians = ["TBS", "ADTR", "FYS"]
print(favorite_musicians)
print()

#2

list_tuples = [(89.999, 145.3333), (24.3255, 988.33)]
print(list_tuples)
print()

#3

about_me = {"height": "5'7",
            "favorite color": "blue",
            "favorite author": "idk"}
print(about_me)
print()

#4

x = 0
while x == 0:
    n = input("What what would you like to know about me? ")
    if n in about_me:
        print(about_me[n])
        
        #if n == "height":
        #    print(about_me["height"])
        #elif n == "favorite color":
        #    print(about_me["favorite color"])
        #elif n == "favorite author":
        #    print(about_me["favorite author"])
        #else:
        #    print("Dont have an answer yet")
        
    elif n == "0":
        x = 1
        print("End.")
        print()
    else:
        print("That attribute does not exist.")

#Better Answer

answer = input("Type height, favorite color, or favorite author.")
if answer in about_me:
    print(about_me[answer])
    print()

#5

fav_musicians = {"TBS": ["Cute", "Last Summer", "Brooklyn"],
                 "ADTR": ["Downfall", "Lauderdale", "Faith"]}
print(fav_musicians)
print()

#End
input("Press any key to exit.")




