n = int(input())
l = list(map(int, input().split()))

# print(n)
# print(l)

l_c = [l.count(l[i]) for i in range(n)]

# print(l_c)

max_l = max(l_c)

l3 = [l[i] for i in range(n) if l_c[i] == max_l]
# print(l3)

l3 = set(l3)
l3 = list(l3)
l3.sort()
print(*l3)
