n = int(input())
l = [input() for i in range(n)]

# print(n)
# print(l)

l2 = set(l)
l2 = list(l2)

# print(l2)

l3 = [l.count(l2[i]) for i in range(len(l2))]
# print(l3)

d = {l2[k]: l3[k] for k in range(len(l2))}
# print(d)

d_sort = sorted(d.items(), key=lambda x:x[1], reverse=True)
# print(d_sort)
print(d_sort[0][0])