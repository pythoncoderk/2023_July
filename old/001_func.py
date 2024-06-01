m, n = map(int, input().split())
l = [int(input()) for i in range(m)]

# print(m, n)
# print(l)

l2 = [[i, l[i], n % l[i]] for i in range(m)]

# print(l2)

sort_2 = sorted(l2, key=lambda x: (x[2], -x[1]))

# print(sort_2)
print((sort_2[0][0])+1)

