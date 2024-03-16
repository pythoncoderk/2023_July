l = [list(map(int, input().split())) for i in range(3)]

l2 = [l[i][0] for i in range(3)]
l3 = [l[i][1] for i in range(3)]

# print(l2)
# print(l3)

l2_c = [l2.count(l2[i]) for i in range(3)]
l3_c = [l3.count(l3[i]) for i in range(3)]

# print(l2_c)
# print(l3_c)

l2_index = l2_c.index(1)
l3_index = l3_c.index(1)

# print(l2_index)
# print(l3_index)

print(f"{l2[l2_index]} {l3[l3_index]}")