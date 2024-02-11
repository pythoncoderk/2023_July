l = list(map(int, input().split()))
# print(l)
l2 = []
for i in range(l[0], l[1]+1, l[2]):
    l2.append(i)
print(*l2)