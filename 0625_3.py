n = int(input())
l = [input() for i in range(n)]

# print(n)
# print(l)

l2 = []
for i in range(n):
    if l[i] in l2:
        x = l2.index(l[i])
        l2.insert(0, l2.pop(x))
    else:
        l2.insert(0, l[i])

for i in l2:
    print(i)