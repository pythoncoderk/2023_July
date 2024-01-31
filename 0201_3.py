n = int(input())
l = [list(input()) for i in range(n)]
# print(n)
# print(l)
xor = l[0]
for i in range(4):
    xor[i] = int(xor[i])
total_xor = []
for i in range(n-1):
    for j in range(4):
        xor[j] = xor[j] ^ int(l[i+1][j])
for i in range(4):
    print(xor[i], end="")
