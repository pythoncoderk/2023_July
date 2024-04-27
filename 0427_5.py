n = int(input())
l = list(map(int, input().split()))

# print(n)
# print(l)

l2 = [l.count(l[i]) for i in range(n)]

# print(l2)

count_max = max(l2)

l3 = [l[i] for i in range(n) if l2[i] == count_max]

l3 = set(l3)
l3 = list(l3)
l3.sort()
print(*l3)