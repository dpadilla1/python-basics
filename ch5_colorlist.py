colors = ["purple",
          "orange",
          "green"]
x = 0

while(x == 0):
    guess = input("Guess a color: ")
    
    if guess in colors:
        print("You guessed correctly!")
        x = 1
    else:
        print("Wrong! Try again.")
    
