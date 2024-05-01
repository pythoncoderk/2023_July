x, y, z = map(int, input().split())
n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

# print(x, y, z)
# print(n)
# print(l)

total = 0
for i in range(n):
    l2 = []
    for j in range(l[i][0]+1, l[i][1]+1):
        l2.append(j)
    for k in range(len(l2)):
        if 9 < l2[k] <= 17:
            total += x
        elif 17 < l2[k] <= 22:
            total += y
        else:
            total += z
print(total)
