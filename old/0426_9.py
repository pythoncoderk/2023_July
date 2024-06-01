n = int(input())
l = list(map(int, input().split()))

# print(n)
# print(l)

count_l = [l.count(l[i]) for i in range(n)]

# print(count_l)

max_l = max(count_l)

l2 = [l[i] for i in range(n) if count_l[i] == max_l]

l2 = set(l2)
l2 = list(l2)
l2.sort()

print(*l2)