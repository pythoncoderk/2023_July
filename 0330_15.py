x, y, z = map(int, input().split())
n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

# print(x, y, z)
# print(n)
# print(l)

total = 0
a = 0
l2 = []
for k in range(n):
    for i in range(l[a][0], l[a][1]+1):
        l2.append(i)
    for j in range(len(l2)-1):
        if 0 <= l2[j+1] <= 9:
            total += z

        elif 9 <= l2[j+1] <= 17:
            total += x

        elif 17 <= l2[j + 1] <= 22:
            total += y
        else:
            total += z
    l2 = []
    a += 1
print(total)