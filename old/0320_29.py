n = int(input())

l = [list(map(str, input().split())) for i in range(n)]

# print(n)
# print(l)

for i in range(n):
    l[i][1] = float(l[i][1])

# print(l)

ge = 0
le = 999

for i in range(n):
    if l[i][0] == "le":
        if le > l[i][1]:
            le = l[i][1]
    else:
        if ge < l[i][1]:
            ge = l[i][1]

print(f"{ge} {le}")