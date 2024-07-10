t = int(input())
l = [input() for i in range(t)]

start = False
count = 0
melon = 0
for i in range(len(l)):
    if not start and l[i] == "melon":
        melon += 1
        start = True
    else:
        if start:
            count += 1
        if count >= 10:
            start = False
            count = 0
print(melon)