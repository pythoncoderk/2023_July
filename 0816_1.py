n = int(input())

l = [int(input()) for i in range(n)]

l2 = []
for i in l:
    if i not in l2:
        l2.append(i)

for i in l2:
    print(i)