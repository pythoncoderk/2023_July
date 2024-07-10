n, k, p = map(int, input().split())

l = list(map(str, input().split()))
l.sort()

# print(n, k, p)
# print(l)

l2 = []
x = 1
l3 = []
while l != []:
    if x <= k:
        l3.append(l.pop(0))
        x += 1
    else:
        l2.append(l3)
        l3 = []
        x = 1
l2.append(l3)

for i in range(len(l2[p - 1])):
    print(l2[p - 1][i])