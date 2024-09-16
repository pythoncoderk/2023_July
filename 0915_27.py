y, x, n = map(int, input().split())
l = [input() for _ in range(n)]

# print(y, x, n)
# print(l)

for i in range(n):
    if l[i] == "N":
        y -= 1
    elif l[i] == "E":
        x += 1
    elif l[i] == "S":
        y += 1
    elif l[i] == "W":
        x -= 1
    print(y, x)

