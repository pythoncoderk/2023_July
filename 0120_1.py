n, m = map(int, input().split())
l = list(map(int, input().split()))

# print(n, m)
# print(l)
l2 = []
for i in range(n-m+1):
    x = 0
    for j in range(i, i+m):
         x += l[j]
    l2.append(x / (n))
# print(l2)

l_max = max(l2)
l_count = l2.count(l_max)
l_index = l2.index(l_max)

print(f"{l_count} {l_index+1}")