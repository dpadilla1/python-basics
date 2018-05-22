# Chapter 6 Challenges, pg.100


#1. Print every character in the string "Camus".
for x in "Camus":
    print(x)
    
print()


#2. Write a program that collects two strings from a user, inserts them
#   into the string "Yesterday I wrote a [response_one]. I sent it to
#   [response_two]" and prints a new string.
str1 = input("Enter a string:")
str2 = input("Enter another string:")
str3 = "Yesterday I wrote a {}. I sent it to {}"
print(str3.format(str1, str2))

print()


#3. Use a method to make the string "aldous Huxley was born in 1894."
#   grammatically correct by capitalizing the first letter in the sentence.
print("aldous Huxley was born in 1894.".capitalize())

print()


#4. Take the string "Where now? Who now? When now?" and call a method that
#   returns a list that looksl ike: ["Where now?", "Who now?", "When now?"].
print("Where now? Who now? When now?".split("?"))

#Error in book.
print()


#5. Take the list ["The", "fox", "jumped", "over", "the", "fence", "."] and
#   turn it into a grammatically correct string. There should be a space
#   between each word, but no space between the word fence and the period that
#   follows it. (Don't forget, you learned a method that turns a list of
#   strings into a single string.)
lst = ["The",
       "fox",
       "jumped",
       "over",
       "the",
       "fence",
       "."]
sent = " ".join(lst[:5]) + " " + "".join(lst[5:])
print(sent)

#Book answer
fox = " ".join(lst)
fox = fox[0: -2] + "."
print(fox)

print()


#6. Replace every instance of "s" in "A screaming comes across the sky." with
#   a dollar sign.
print("A screaming comes across the sky.".replace("s", "$"))

print()


#7. Use a method to find the first index of the character "m" in the string
#   "Hemingway".
print("Hemingway".index("m"))

print()


#8. Find dialogue in your favorite book (containing quotes) and turn it into
#   a string.
bookLine1 = "And then Harry said, \"Look how big my wand is!\""
bookLine2 = '"Yo chill bruh," said Ron.'
print(bookLine1)
print(bookLine2)

print()


#9. Create the string "three three three" using concatenation, and then again
#   using multiplication.
conc = "three " + "three " + "three"
mult = "three "*3
print(conc)
print(mult)

print()


#10. Slice the string "It was a bright cold day in April, and the clocks were
#    striking thriteen." to only include the characters before the comma.
s1 = "It was a bright cold day in April, and the clocks were striking thirteen."
s1 = s1[0: s1.index(",")]
print(s1)

print()
