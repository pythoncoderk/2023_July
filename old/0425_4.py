m, n = map(int, input().split())
l = [int(input()) for i in range(m)]

# print(m, n)
# print(l)

l2 = []
for i in range(m):
    l3 = [l[i], n % l[i], i+1]
    l2.append(l3)

# print(l2)

sorted_l = sorted(l2, key=lambda x: x[0], reverse=True)
sorted_l2 = sorted(sorted_l, key=lambda x: x[1])

print(sorted_l2[0][2])