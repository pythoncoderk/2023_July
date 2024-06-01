n = int(input())
l = [list(input()) for i in range(n)]

for i in range(n):
    for j in range(4):
        l[i][j] = int(l[i][j])

# print(n)
# print(l)

l2 = l[0]
for i in range(n-1):
    for j in range(4):
        l2[j] = l2[j] ^ l[i+1][j]

for i in l2:
    print(i, end="")