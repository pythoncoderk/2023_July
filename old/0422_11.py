import math

m = int(input())
n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

# print(m)
# print(n)
# print(l)

x = l[0][0]
count = 0
total = 0
for i in range(n+1):
    if i != n:
        if x == l[i][0]:
            total += l[i][2]
        else:
            count += math.ceil(total / m)
            total = 0
            x = l[i][0]
            total += l[i][2]
    else:
        count += math.ceil(total / m)
print(count)

