n = int(input())
l = list(map(str, input().split()))
m = int(input())
l2 = [list(map(str, input().split())) for i in range(m)]
for i in range(m):
    l2[i][1] = int(l2[i][1])

# print(n)
# print(l)
# print(m)
# print(l2)

d = {l[k]: 0 for k in range(n)}

# print(d)

for i in range(m):
    d[l2[i][0]] += l2[i][1]

# print(d)

l_d = list(d.items())

# print(l_d)

sort_l = sorted(l_d, key=lambda x: x[1], reverse=True)

# print(sort_l)

for i in range(len(sort_l)):
    print(sort_l[i][0])