n = int(input())

l = []
for i in range(n):
    w = input()
    if w in l:
        for j in range(len(l)):
            if l[j] == w:
                w2 = l.pop(j)
                l.insert(0, w2)
    else:
        l.insert(0, w)
for i in l:
    print(i)

