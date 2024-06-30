n = int(input())
l = [list(map(str, input().split())) for i in range(n)]

# print(n)
# print(l)

for i in range(n):
    l[i][1] = float(l[i][1])

# print(l)

ge = 0
le = 999999999999999

for i in range(n):
    if l[i][0] == "ge":
        if ge < l[i][1]:
            ge = l[i][1]
    else:
        if le > l[i][1]:
            le = l[i][1]

print(ge, le)