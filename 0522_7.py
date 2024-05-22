n = int(input())
m = int(input())

d = {k: 1 for k in range(1, n + 1)}
d[1] = 0
# print(d)

total = sum(d.values())
i = 1
chk = True
while total != 0:
    i += m
    if i > n:
        i -= n
    if d[i] == 0:
        print("no")
        exit()
    else:
        d[i] = 0
    total = sum(d.values())

print("yes")
