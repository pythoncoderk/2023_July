n = int(input())
l = [input() for i in range(n)]
# print(n)
# print(l)
l2 = []
for i in range(n):
    if l[i] in l2:
        l2.remove(l[i])
        l2.insert(0, l[i])
    else:
        l2.insert(0, l[i])
# print(l2)
for i in l2:
    print(i)