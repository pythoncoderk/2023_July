m, n = map(int, input().split())
l = [int(input()) for i in range(m)]

# print(m, n)
# print(l)

l2 = [[l[i], n % l[i]] for i in range(m)]

# print(l2)

l_sort = sorted(l2, key=lambda x:(x[1], -x[0]))

# print(l_sort)

final = l_sort[0]

for i in range(m):
    if final == l2[i]:
        print(i + 1)
        break