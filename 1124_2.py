n, k, p = map(int, input().split())
l = list(map(str, input().split()))
# print(l)
l.sort()
# print(l)
l2 = []
while len(l2) != n:
    l3 = []
    if len(l) >= k:
        for i in range(k):
            l3.append(l.pop(0))
        l2.append(l3)
    else:
        for i in range(len(l)):
            l3.append(l.pop(0))
        l2.append(l3)
# print(l2)

for i in l2[p-1]:
    print(i)