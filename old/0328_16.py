n, k, p = map(int, input().split())
l = list(map(str, input().split()))
l.sort()
# print(n, k, p)
# print(l)

l2 = []
while l:
    l3 = []
    for i in range(k):
        if l:
            l3.append(l.pop(0))
    l2.append(l3)

for i in range(len(l2[p-1])):
    print(l2[p-1][i])

