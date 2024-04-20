n, q = map(int, input().split())
l = list(map(int, input().split()))

# print(n, q)
# print(l)

l2 = []
for i in range(q):
    if l[i] in l2:
        x = l2.index(l[i])
        l2.pop(x)
    else:
        l2.append(l[i])
len_l2 = len(l2)
print(n-len_l2)

