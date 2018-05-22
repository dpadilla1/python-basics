rhymes = {"1": "fun",
          "2": "blue",
          "3": "me",
          "4": "floor",
          "5": "live"}

x = 0
while(x == 0):
    n = input("Type a number: ")
    if n in rhymes:
        rhyme = rhymes[n]
        print(rhyme)
    elif n == "0":
        x = 1
        print("End.")
    else:
        print("Not found.")
