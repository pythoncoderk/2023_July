n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
for i in range(n):
    l[i][1] = int(l[i][1])
# print(n)
# print(l)

for i in range(n):
    l[i][1] = int(l[i][1])

l2 = [l[i][0] for i in range(n)]
l3 = set(l2)
l3 = list(l3)

l_names = []
for i in range(n):
    l_names.append(l[i][0])
l_names_counts = []
for i in l3:
    l_names_counts.append(l_names.count(i))

# print(l_names)
# print(l_names_counts)

max_name = l_names_counts.index(max(l_names_counts))
print(l_names[max_name])
# print(l3)
# print(l2)
# print(l)
counts_max = []
for i in range(len(l3)):
    x = []
    for j in range(n):
        if l3[i] == l[j][0]:
            x.append(l[j][1])
    counts_max.append(sum(x))
counts_max_index = counts_max.index(max(counts_max))
print(l3[counts_max_index])