n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

# print(n)
# print(l)

l2 = [l[i][0] + l[i][1] for i in range(n)]
# print(l2)


l3 = [l2.count(l2[i]) for i in range(n)]
# print(l3)

max_l = max(l3)

l4 = [l2[i] for i in range(n) if l3[i] == max_l]
# print(l4)

l4 = set(l4)
l4 = list(l4)
l4.sort()
print(l4[0])