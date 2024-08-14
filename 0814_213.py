n = int(input())
l = [int(input()) for i in range(n)]

l2 = []
for i in range(n):
    if l[i] not in l2:
        l2.append(l[i])

for i in l2:
    print(i)
