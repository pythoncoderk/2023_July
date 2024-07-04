n = 3
k = 20
l = [5, 8, 9]

x = 0
chk = False
loop = False
while loop == False:
    count = bin(x)
    count = list(count[2:].zfill(3))
    total = 0
    for i in range(len(count)):
        if count[i] == "1":
            total += l[i]
        if total == k:
            chk = True
    x += 1
    for i in range(len(count)):
        count[i] = int(count[i])
    if sum(count) == n:
        loop = True

print("Yes" if chk else "No")
