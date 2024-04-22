m, n = map(int, input().split())
l = [list(map(int, input().split())) for i in range(m)]

# print(m, n)
# print(l)

l2 = []
for i in range(m-n+1):
    x = 0
    for j in range(i, i+n):
        x += l[j][1]
    l2.append(x)
# print(l2)

min_l = min(l2)
min_index = l2.index(min_l)

# print(min_l)
# print(min_index)

print(f"{l[min_index][0]} {l[min_index][0]+n-1}")