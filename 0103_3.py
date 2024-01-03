x, y = map(int, input().split())
l = list(map(int, input().split()))

# print(x, y)
# print(l)

counts = y
z = 0
l2 = []
l3 = []
while counts != x+1:
    i = counts - y
    for j in range(i, counts):
        l2.append(l[i])
        i += 1

    l3.append(sum(l2) / y)
    l2 = []
    counts += 1
# print(l3)
max_l = max(l3)
max_count = l3.count(max_l)
max_index = l3.index(max_l)
print(f"{max_count} {max_index+1}")







