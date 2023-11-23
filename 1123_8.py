n = int(input())
l = [int(input()) for i in range(n)]
l_f = l.copy()
l.sort(reverse=True)
l2 = list(set(l))
l2.sort(reverse=True)
l3 = []
for i in l2:
    l3.append(l.count(i))
l4 = []
x = 0
for i in range(len(l3)):
    l4.append(x)
    x += l3[i]
for i in range(n):
    i2 = l2.index(l_f[i])
    print(l4[i2]+1)
