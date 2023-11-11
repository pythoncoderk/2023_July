n = int(input())
l = [int(input()) for i in range(n)]
l2 = []
for i in l:
    if i in l2:
        pass
    else:
        l2.append(i)
for i in l2:
    print(i)