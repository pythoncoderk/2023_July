n = int(input())
l = [list(input()) for i in range(n)]
for i in range(n):
    for j in range(4):
        l[i][j] = int(l[i][j])

x = l.pop(0)

# print(x)
# print(n)
# print(l)

for i in range(n-1):
    for j in range(4):
        x[j] = x[j] ^ l[i][j]

for i in x:
    print(i, end="")