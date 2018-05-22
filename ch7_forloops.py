#ch7 for-loops pg.105

tv = ["Got", "Narcos", "Vice"]

i = 0
for show in tv:
    tv[i] = tv[i].upper()
    i += 1

print(tv)
print()

#other syntax

for i, show in enumerate(tv):
    tv[i] = tv[i].lower()

print(tv)
print()


#pg.107

tv = ["Got", "Narcos", "Vice"]
coms = ["Arrested Development", "friends", "Always Sunny"]
all_shows = []

for show in tv:
    show = show.upper()
    all_shows.append(show)

for show in coms:
    show = show.upper()
    all_shows.append(show)

print(all_shows)
print()


#range function

for i in range(1,11):
    print(i)

print()
