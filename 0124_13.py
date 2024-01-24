n = int(input())
l = list(map(int, input().split()))
# print(l)

l2 = [l.count(l[i]) for i in range(n)]
# print(l2)

max_count = max(l2)
# print(max_count)

l3 = [l[i] for i in range(n) if l2[i] == max_count]
# print(l3)

s1 = set(l3)
s1 = list(s1)
s1.sort()
print(*s1)