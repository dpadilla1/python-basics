#writing a csv file - pg.127

import csv


with open("st.csv", "w", newline='') as f:
    w = csv.writer(f,
                   delimiter=",")
    w.writerow(["one",
                "two",
                "three"])
    w.writerow(["four",
                "five",
                "six"])

with open("st.csv", "r") as g:
    r = csv.reader(g,
                   delimiter=",")
    for row in r:
        print(",".join(row))


