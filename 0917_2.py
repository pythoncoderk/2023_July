n = int(input())
l = []
for i in range(n):
    x = input()
    if l.count(x) >= 1:
        l2 = []
        for j in l:
            if j != x:
                l2.append(j)
            else:
                pass
        l2.insert(0, x)
        l = l2

    else:
        l.append(x)
for i in l:
    print(i)