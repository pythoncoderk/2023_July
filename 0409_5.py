n, k = map(int, input().split())
l = [[int(input()) for j in range(n)] for i in range(3)]

# print(n, k)
# print(l)

l2 = []
for i in range(3):
    l4 = []
    for j in range(n-k+1):
        l3 = []
        for p in range(j, j+k):
            l3.append(l[i][p])
        l4.append(sum(l3)/k)
    l2.append(min(l4))

min_l = min(l2)
index_l = l2.index(min_l)

print(index_l + 1)
