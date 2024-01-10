k, n = map(int, input().split())
l = list(map(int, input().split()))

# print(k, n)
# print(l)

l3 = []
for i in range(k - n + 1):
    l2 = []
    for j in range(n):
        l2.append(l[j+i])
    l3.append(l2)
l4 = [sum(l3[i]) for i in range(n)]
max_l = max(l4)
final_count = l4.count(max_l)
index_l = l4.index(max_l)
final_index = l3[index_l][0]

print(f"{final_count} {final_index}")