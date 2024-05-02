import math

n, m = map(int, input().split())
s = list(input())

# print(n, m)
# print(s)

l = []
l2 = []
count = 0
while len(l) != math.ceil(n/m):
    if count < m:
        if s != []:
            l2.append(int(s.pop(0)))
            count += 1
        else:
            if count < m:
                l2.append(0)
                count += 1
            else:
                l.append(l2)
                break
    else:
        l.append(l2)
        l2 = []
        count = 0

# print(l)

x = l.pop(0)
for i in range(len(l)):
    for j in range(m):
        x[j] = x[j] ^ l[i][j]

for i in x:
    print(i, end="")