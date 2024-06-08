s = input()

l = [
    "SUN",
    "MON",
    "TUE",
    "WED",
    "THU",
    "FRI",
    "SAT"
     ]

x = l.index(s) + 1

count = 1
while True:
    if x >= 7:
        x = 0

    if l[x] != "SUN":
        count += 1
        x += 1
    else:
        break

print(count)