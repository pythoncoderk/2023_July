m, n = map(int, input().split())

l = [int(input()) for i in range(m)]

# print(m, n)
# print(l)

l2 = [[l[i], n % l[i]] for i in range(m)]

# print(l2)

l3 = l2[::]
# print(l3)
l3 = sorted(l3, key=lambda x: (x[1], -x[0]))
# print(l3)

final = 0
for i in range(m):
    if l3[0] == l2[i]:
        final = i + 1
print(final)