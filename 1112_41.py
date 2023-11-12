n = int(input())
l = [int(input()) for i in range(n)]
l2 = []
for i in l:
    if i % 2 == 1:
        l2.append(i)
l2.sort()
for i in l2:
    print(i)