import math

n, m = map(int, input().split())

s = list(input())

# print(n, m)
# print(s)

l = []
l2 = []
count = 0
while True:
    if len(s) != 0:
        if count < m:
            x = s.pop(0)
            l.append(int(x))
            count += 1
        else:
            count = 0
            l2.append(l)
            l = []
    else:
        if m != 1:
            l.append(0)
            l2.append(l)
            break
        else:
            l2.append(l)
            break
# print(l2)

x = l2[0]
for i in range(1, math.ceil(n/m)):
    for j in range(m):
        x[j] = x[j] ^ l2[i][j]

for i in x:
    print(i, end="")