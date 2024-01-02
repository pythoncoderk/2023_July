n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
for i in range(n):
    l[i][1] = int(l[i][1])

counts = 0
for i in range(n):
    if l[i][0] == "pants":
        counts += 1

price = 0
for i in range(n):
    price += l[i][1]

if counts != 0 and price >= 2000:
    print(price - 500)
else:
    print(price)