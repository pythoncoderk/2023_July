n = int(input())

l = [list(map(str, input().split())) for i in range(n)]
for i in range(n):
    l[i][1] = float(l[i][1])
# print(n)
# print(l)

ge = 0
le = 999

for i in range(n):
    if l[i][0] == "ge" and ge < l[i][1]:
        ge = l[i][1]
    elif l[i][0] == "le" and le > l[i][1]:
        le = l[i][1]
print(f"{ge} {le}")


