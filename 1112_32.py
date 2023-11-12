n = int(input())
l = [input() for i in range(n)]
l2 = []
for i in l:
    if i in l2:
        l2.remove(i)
        l2.insert(0, i)
    else:
        l2.insert(0, i)
for i in l2:
    print(i)