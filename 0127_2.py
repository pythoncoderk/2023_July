import math

n, m = map(int, input().split())
s = list(input())
s2 = s[::]
# print(n, m)
# print(s)
xor = []
# print(math.ceil(n / m))
for i in range(math.ceil(n / m)):
    x = []
    for j in range(m):
        if not s2:
            x.append(0)
        else:
            x.append(int(s2.pop(0)))
    xor.append(x)
# print(xor)

xor2 = [xor[0][i] for i in range(m)]
xor.pop(0)
# print(xor2)
# print(xor)
for i in range(len(xor)):
    for j in range(m):
        xor2[j] = xor2[j] ^ xor[i][j]
for i in xor2:
    print(i, end="")