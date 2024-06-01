n, k, p = map(int, input().split())
l = list(map(str, input().split()))

# print(n, k, p)
# print(l)

l.sort()

# print(l)

l2 = []
l3 = []
while l:
    x = l.pop(0)
    l2.append(x)
    if len(l2) == k:
        l3.append(l2)
        l2 = []
l3.append(l2)
for i in l3[p-1]:
    print(i)