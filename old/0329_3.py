n = int(input())
l = [list(input()) for i in range(n)]
for i in range(n):
    for j in range(4):
        l[i][j] = int(l[i][j])

# print(n)
# print(l)

l1 = l[0]
l2 = l[1:]

for i in range(n-1):
    for j in range(4):
        l1[j] = l1[j] ^ l2[i][j]
for _ in l1:
    print(_, end="")



