n = int(input())
l = [input() for i in range(n)]
# print(n)
# print(l)
l2 = []
for i in range(n):
    if l[i] in l2:
        x = l2.index(l[i])
        l2.remove(l[i])
        l2.append(l[i])
    else:
        l2.append(l[i])
l2.reverse()
for i in l2:
    print(i)